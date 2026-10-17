"""SOC2_MSLOGS round 1, cell SM-c-1 checks (the collector switches to raw). Run from the repo (worktree) root.

  python s1_check_c1.py raw       -> C1-RAW-OK       (every account, four feeds, byte-for-byte bronze, no filter left)
  python s1_check_c1.py switch    -> C1-SWITCH-OK    (an old-era cursor re-fetches the 7 days; already stored is not a gap; derive is budgeted)
  python s1_check_c1.py recollect -> C1-RECOLLECT-OK (a window run leaves the cursor alone; the handler's window rules)
  python s1_check_c1.py derive_time -> C1-DERIVETIME-OK (a fire never runs past its Lambda limit; derive keeps a reserved share, newest day first)
  python s1_check_c1.py derive_par  -> C1-DERIVEPAR-OK  (owed days are derived concurrently, up to max_workers at a time, newest first)
  python s1_check_c1.py derive_client -> C1-DERIVECLIENT-OK (the handler's derive call has a long read timeout and no automatic retry)

Synthetic values only. The collector API this file drives is fixed in the order's worker face.
"""
import gzip
import importlib.util
import json
import os
import re
import sys

ROOT = os.getcwd()
PKG = os.path.join(ROOT, "data", "m365_metadata", "scripts", "collector")
LAMBDA = os.path.join(ROOT, "infra", "aws", "lambda", "m365-metadata-collector", "handler.py")
FOUR = ["Audit.Exchange", "Audit.SharePoint", "Audit.General", "Audit.AzureActiveDirectory"]
NOW = "2026-10-16T12:00:00Z"
KEY_RE = re.compile(r"^m365-metadata/trino/bronze/audit_records/date=(\d{8})/(.+)\.json\.gz$")


def mod(name):
    p = os.path.join(PKG, name + ".py")
    if not os.path.exists(p):
        raise FileNotFoundError(p)
    spec = importlib.util.spec_from_file_location("c1_" + name, p)
    m = importlib.util.module_from_spec(spec)
    if PKG not in sys.path:
        sys.path.insert(0, PKG)
    spec.loader.exec_module(m)
    return m


def cid(ct, n):
    kind = ct.split(".", 1)[1]
    return "2026101512%011d$2026101512%011d$audit_%s$Audit_%s$na0001" % (n, n, kind.lower(), kind)


def raw_blob(who, n=2):
    """Raw bytes as the API serves them: indented, non-ASCII, trailing newline. NOT re-serialised by the checks."""
    recs = [{"Id": "r-%s-%d" % (who.split("@")[0], i), "CreationTime": "2026-10-15T14:0%d:00", "Operation": "FileAccessed",
             "UserId": who, "ClientIP": "203.0.113.%d" % (7 + i), "ObjectId": "https://x.example/café-%d.xlsx" % i,
             "ExtendedProperties": [{"Name": "UserAgent", "Value": "Synthetic/1.0 ü"}]} for i in range(n)]
    for i, r in enumerate(recs):
        r["CreationTime"] = r["CreationTime"] % i
    return (json.dumps(recs, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


class Source:
    def __init__(self, blobs):
        self.blobs = blobs   # {ct: [(id, created, raw_bytes)]}
        self.list_calls = []
        self.fetched = []

    def list_content(self, ct, start, end):
        self.list_calls.append((ct, start, end))
        return [{"id": i, "created": c} for (i, c, _r) in self.blobs.get(ct, [])]

    def fetch_raw(self, ct, blob_id):
        self.fetched.append(blob_id)
        for (i, _c, r) in self.blobs.get(ct, []):
            if i == blob_id:
                return r
        raise KeyError(blob_id)


class Access:
    def __init__(self, preseed=(), clock=None, derive_cost=0.0):
        self.objs = {}
        self.preseed = set(preseed)
        self.derived = []
        self.puts = []
        self.events = []
        self.clock = clock
        self.derive_cost = derive_cost

    def put(self, dataset, key, body):
        self.puts.append((dataset, key))
        self.events.append(("put", dataset))
        if dataset == "bronze" and (key in self.objs.get("bronze", {}) or key in self.preseed):
            return {"ok": False, "already_stored": True, "error": "exists"}
        self.objs.setdefault(dataset, {})[key] = body
        return {"ok": True}

    def get_state(self, key):
        return self.objs.get("state", {}).get(key)

    def derive_silver(self, date):
        self.derived.append(date)
        self.events.append(("derive", date, None if self.clock is None else self.clock.t))
        if self.clock is not None:
            self.clock.t += self.derive_cost
        return {"ok": True, "rows": 0}


class Clock:
    def __init__(self):
        self.t = 0.0

    def __call__(self):
        return self.t


def blobs_for(n_per=1):
    out = {}
    n = 0
    for ct in FOUR:
        lst = []
        for k in range(n_per):
            n += 1
            who = "outsider%d@opalinvest.com" % n if ct != "Audit.AzureActiveDirectory" else "signin.user@opalinvest.com"
            lst.append((cid(ct, n), "2026-10-15T1%d:00:00.000Z" % (k + 2), raw_blob(who)))
        out[ct] = lst
    return out


def cov_docs(acc):
    return [json.loads(b) for k, b in acc.objs.get("gold", {}).items() if "collection_coverage" in k]


def raw():
    run = mod("collect")
    rr = mod("raw_records")
    bad = []
    if list(rr.CONTENT_TYPES) != FOUR:
        bad.append("CONTENT_TYPES must be the four feeds incl. Audit.AzureActiveDirectory: %r" % (list(rr.CONTENT_TYPES),))
    for gone in ("filter.py",):
        if os.path.exists(os.path.join(PKG, gone)):
            bad.append("%s still exists in the collector package" % gone)
    if os.path.exists(os.path.join(ROOT, "data", "m365_metadata", "scripts", "population.json")):
        bad.append("population.json still exists")
    src = ""
    for f in os.listdir(PKG):
        if f.endswith(".py"):
            src += open(os.path.join(PKG, f), encoding="utf-8").read()
    if os.path.exists(LAMBDA):
        src += open(LAMBDA, encoding="utf-8").read()
    for word in ("TCKT", "population", "subject_key", "office_ips", "SUBJECT_KEY", "process_batch"):
        if word in src:
            bad.append("the collector still mentions %r" % word)
    blobs = blobs_for(1)
    acc = Access()
    out = run.run_once(Source(blobs), acc, {}, NOW)
    stored = acc.objs.get("bronze", {})
    if len(stored) != 4:
        bad.append("expected 4 bronze objects (one per blob), got %d" % len(stored))
    want = {i: r for lst in blobs.values() for (i, _c, r) in lst}
    seen_ids = set()
    for key, body in stored.items():
        m = KEY_RE.match(key)
        if not m:
            bad.append("bronze key outside the audit_records grammar: %s" % key)
            continue
        if m.group(1) != "20261015":
            bad.append("the date partition must be the Eastern date of the blob's created time: %s" % key)
        blob_id = m.group(2)
        seen_ids.add(blob_id)
        if blob_id not in want:
            bad.append("a bronze key whose name is not a content id: %s" % key)
        elif gzip.decompress(body) != want[blob_id]:
            bad.append("stored bytes differ from the served blob for %s" % blob_id)
    if seen_ids != set(want):
        bad.append("not every blob landed: missing %r" % sorted(set(want) - seen_ids))
    if out.get("complete") is not True or out.get("failed") != 0:
        bad.append("the fire did not complete clean: %r" % ({k: v for k, v in out.items() if k != "cursor"},))
    app = os.path.join(ROOT, "data", "m365_metadata", "scripts", "app", "start_subscriptions.py")
    if not os.path.exists(app):
        bad.append("no start_subscriptions.py")
    else:
        a_src = open(app, encoding="utf-8").read()
        if "EXCLUDED_CONTENT_TYPES" in a_src or "Audit.AzureActiveDirectory" not in a_src:
            bad.append("start_subscriptions.py must start the sign-in feed and carry no exclusion list")
        spec = importlib.util.spec_from_file_location("c1_start", app)
        sm = importlib.util.module_from_spec(spec)
        sys.path.insert(0, os.path.dirname(app))
        spec.loader.exec_module(sm)
        if sorted(sm.CONTENT_TYPES) != sorted(FOUR):
            bad.append("start_subscriptions.CONTENT_TYPES is %r" % (sm.CONTENT_TYPES,))
    for rel in (("scripts", "app", "start_subscriptions.py"), ("scripts", "tests", "test_app.py"), ("scripts", "tests", "test_collector.py")):
        p = os.path.join(ROOT, "data", "m365_metadata", *rel)
        if os.path.exists(p) and "TCKT" in open(p, encoding="utf-8").read():
            bad.append("%s mentions TCKT" % "/".join(rel))
    if bad:
        print("C1-RAW-REFUSED " + "; ".join(bad))
        return 1
    print("C1-RAW-OK blobs=%d" % len(stored))
    return 0


def switch():
    run = mod("collect")
    bad = []
    blobs = blobs_for(2)
    old = {"last_end": "2026-10-16T11:00:00Z",
           "seen": {"Audit.SharePoint": {blobs["Audit.SharePoint"][0][0]: "2026-10-15T12:00:00Z"}, "Audit.Exchange": [blobs["Audit.Exchange"][0][0]]}}
    src = Source(blobs)
    acc = Access()
    out = run.run_once(src, acc, {}, NOW, cursor=old)
    total = sum(len(v) for v in blobs.values())
    if out["fetched"] != total:
        bad.append("an old-era cursor must re-fetch the whole window: fetched %d of %d" % (out["fetched"], total))
    cur = out["cursor"]
    if cur.get("era") != "raw" or not isinstance(cur.get("seen"), dict):
        bad.append("the new cursor must carry era 'raw' and a seen map: %r" % ({k: v for k, v in cur.items() if k != "seen"},))
    out2 = run.run_once(Source(blobs), Access(), {}, NOW, cursor=cur)
    if out2["fetched"] != 0:
        bad.append("a second fire with the raw cursor fetched %d blobs again" % out2["fetched"])
    docs = cov_docs(acc)
    if not docs or not all(d.get("era") == "raw" for d in docs):
        bad.append("coverage documents must carry era 'raw'")
    some = next(iter(blobs["Audit.General"]))
    pre = "m365-metadata/trino/bronze/audit_records/date=20261015/%s.json.gz" % some[0]
    acc2 = Access(preseed=[pre])
    out3 = run.run_once(Source(blobs), acc2, {}, NOW, cursor=None)
    if out3.get("already_stored") != 1 or out3.get("failed") != 0:
        bad.append("an already-stored blob is neither failed nor ignored: %r" % ({k: v for k, v in out3.items() if k != "cursor"},))
    for d in cov_docs(acc2):
        for r in d["records"]:
            if r.get("gap") or r.get("status") in ("GAP", "LOST"):
                bad.append("already stored read as a gap: %r" % (r,))
                break
    # derive: once per Eastern day with bronze, and the day before it; budgeted, with the rest carried in the cursor.
    clock = Clock()
    acc3 = Access(clock=clock, derive_cost=30.0)
    one = {"Audit.General": [(cid("Audit.General", 1), "2026-10-15T14:00:00.000Z", raw_blob("a@opalinvest.com")),
                              (cid("Audit.General", 2), "2026-10-14T14:00:00.000Z", raw_blob("b@opalinvest.com")),
                              (cid("Audit.General", 3), "2026-10-13T14:00:00.000Z", raw_blob("c@opalinvest.com"))]}
    clock.t = 0.0
    f1 = run.run_once(Source(one), acc3, {}, NOW, cursor=None, clock=clock, budget_seconds=20, max_workers=1)
    pending = f1["cursor"].get("derive_pending")
    if sorted(set(acc3.derived)) != sorted(acc3.derived) or acc3.derived != sorted(acc3.derived, reverse=True):
        bad.append("derive dates must be called once each, newest day first: %r" % (acc3.derived,))
    if not acc3.derived or not isinstance(pending, list) or not pending:
        bad.append("a fire out of derive time must carry derive_pending in the cursor (derived %r, pending %r)" % (acc3.derived, pending))
    want_days = {"2026-10-12", "2026-10-13", "2026-10-14", "2026-10-15"}
    clock.t = 0.0
    run.run_once(Source(one), acc3, {}, NOW, cursor=f1["cursor"], clock=clock, budget_seconds=20, max_workers=1)
    for _ in range(3):
        if set(acc3.derived) >= want_days:
            break
        f1 = run.run_once(Source(one), acc3, {}, NOW, cursor=f1["cursor"], clock=clock, budget_seconds=20, max_workers=1)
    if not set(acc3.derived) >= want_days:
        bad.append("derive_pending never drained: derived %r" % (sorted(set(acc3.derived)),))
    if bad:
        print("C1-SWITCH-REFUSED " + "; ".join(bad))
        return 1
    print("C1-SWITCH-OK")
    return 0


class TimedSource(Source):
    """A source whose every fetch costs fetch_cost seconds on the injected clock."""

    def __init__(self, blobs, clock, fetch_cost=1.0):
        super().__init__(blobs)
        self.clock = clock
        self.fetch_cost = fetch_cost

    def fetch_raw(self, ct, blob_id):
        self.clock.t += self.fetch_cost
        return super().fetch_raw(ct, blob_id)


def many_blobs(n, days=("2026-10-10", "2026-10-11", "2026-10-12", "2026-10-13", "2026-10-14", "2026-10-15")):
    lst = []
    for i in range(n):
        d = days[i % len(days)]
        lst.append((cid("Audit.General", i + 1), "%sT%02d:00:00.000Z" % (d, 14 + (i // len(days)) % 8), raw_blob("u%d@opalinvest.com" % i, 1)))
    return {"Audit.General": lst}


def derive_time():
    """A fire must end inside its Lambda limit (900 s; budget 840 as the handler passes) even when derive calls are slow, derive must keep
    a reserved share while a backlog is being fetched, the newest day goes first, and the cursor is saved BEFORE derive begins."""
    run = mod("collect")
    bad = []
    LIMIT_END = 885.0   # the handler's budget (840) plus the 45 s grace: nothing may run past it

    clock = Clock()
    acc = Access(clock=clock, derive_cost=40.0)
    out = run.run_once(TimedSource(many_blobs(1200), clock), acc, {}, NOW, cursor=None, clock=clock, budget_seconds=840, max_workers=1)
    if clock.t > LIMIT_END:
        bad.append("a fire with 40 s derives ended at %.0f s, past %.0f" % (clock.t, LIMIT_END))
    if len(acc.derived) < 3:
        bad.append("a fire with a fetch backlog ran only %d derive calls (derive needs a reserved share)" % len(acc.derived))
    if acc.derived != sorted(acc.derived, reverse=True):
        bad.append("derive must go newest day first: %r" % (acc.derived,))
    puts_before = [e for e in acc.events[:next((i for i, e in enumerate(acc.events) if e[0] == "derive"), len(acc.events))] if e[0] == "put"]
    if ("put", "state") not in puts_before:
        bad.append("the cursor must be saved BEFORE the first derive call, so a timeout in derive loses nothing")
    pend = out["cursor"].get("derive_pending")
    if not isinstance(pend, list) or set(pend) & set(acc.derived):
        bad.append("the final cursor must list exactly the days not derived: pending %r, derived %r" % (pend, acc.derived))
    state_docs = [json.loads(b) for k, b in acc.objs.get("state", {}).items()]
    if not state_docs:
        bad.append("no cursor was written")

    clock2 = Clock()
    acc2 = Access(clock=clock2, derive_cost=120.0)
    run.run_once(TimedSource(many_blobs(1200), clock2), acc2, {}, NOW, cursor=None, clock=clock2, budget_seconds=840, max_workers=1)
    if clock2.t > LIMIT_END:
        bad.append("a fire with 120 s derives ended at %.0f s, past %.0f" % (clock2.t, LIMIT_END))
    if not acc2.derived:
        bad.append("a fire must make progress on derive even when each call is slow")

    clock3 = Clock()
    acc3 = Access(clock=clock3, derive_cost=1.0)
    out3 = run.run_once(TimedSource(many_blobs(5), clock3), acc3, {}, NOW, cursor=None, clock=clock3, budget_seconds=90, max_workers=1)
    if out3["fetched"] < 1:
        bad.append("a small budget must still fetch (the derive reserve is a share of the budget, never all of it)")
    if bad:
        print("C1-DERIVETIME-REFUSED " + "; ".join(bad))
        return 1
    print("C1-DERIVETIME-OK end=%.0f derives=%d" % (clock.t, len(acc.derived)))
    return 0


def derive_par():
    """The door's derive of a busy day takes 60-100 s, so derive over several owed days must run CONCURRENTLY (up to max_workers at a time)."""
    import threading
    import time

    run = mod("collect")
    bad = []

    class ParAccess(Access):
        def __init__(self):
            super().__init__()
            self.lock = threading.Lock()
            self.inflight = 0
            self.max_inflight = 0
            self.started = []

        def derive_silver(self, date):
            with self.lock:
                self.started.append(date)
                self.inflight += 1
                self.max_inflight = max(self.max_inflight, self.inflight)
            time.sleep(0.3)
            with self.lock:
                self.inflight -= 1
                self.derived.append(date)
            return {"ok": True, "rows": 0}

    acc = ParAccess()
    out = run.run_once(Source(many_blobs(60)), acc, {}, NOW, cursor=None, max_workers=4)
    if acc.max_inflight < 2:
        bad.append("derive ran one day at a time (max in flight %d); owed days must run concurrently" % acc.max_inflight)
    if acc.max_inflight > 4:
        bad.append("more derive calls in flight (%d) than max_workers" % acc.max_inflight)
    if not acc.started or acc.started[0] != max(acc.started):
        bad.append("the newest day must start first: %r" % (acc.started,))
    if sorted(set(acc.derived)) != sorted(acc.derived):
        bad.append("a day was derived twice: %r" % (acc.derived,))
    if (out["cursor"].get("derive_pending") or []):
        bad.append("an unbudgeted fire must derive every owed day: pending %r" % (out["cursor"].get("derive_pending"),))
    if bad:
        print("C1-DERIVEPAR-REFUSED " + "; ".join(bad))
        return 1
    print("C1-DERIVEPAR-OK max_inflight=%d days=%d" % (acc.max_inflight, len(acc.derived)))
    return 0


def derive_client():
    """The first live fires with a derive of 60-100 s were killed by the DEFAULT boto3 client: a 60 s read timeout with 5 attempts re-invoked
    the door for the same day five times (door log, 2026-10-17 00:42-00:47Z). The derive call needs a long read timeout and no automatic retry."""
    import re

    bad = []
    src = open(LAMBDA, encoding="utf-8").read()
    rt = [int(x) for x in re.findall(r"read_timeout\s*=\s*(\d+)", src)]
    if not rt or max(rt) < 200 or max(rt) > 290:
        bad.append("the handler must build a derive client with read_timeout between 200 and 290 s (found %r)" % (rt,))
    if not re.search(r"max_attempts[\"']?\s*[:=]\s*1", src):
        bad.append("the derive client must set max_attempts to 1 (no automatic re-invoke of a derive)")
    if "Config" not in src:
        bad.append("the handler does not build a botocore Config")
    if bad:
        print("C1-DERIVECLIENT-REFUSED " + "; ".join(bad))
        return 1
    print("C1-DERIVECLIENT-OK")
    return 0


def recollect():
    run = mod("collect")
    bad = []
    blobs = blobs_for(1)
    first = Access()
    run.run_once(Source(blobs), first, {}, NOW)
    pre = list(first.objs.get("bronze", {}))
    src = Source(blobs)
    acc = Access(preseed=pre)
    out = run.run_once(src, acc, {}, NOW, cursor={"last_end": NOW, "era": "raw", "seen": {}},
                       window=("2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z"))
    if any(a != "2026-10-15T00:00:00Z" or b != "2026-10-16T00:00:00Z" for (_ct, a, b) in src.list_calls):
        bad.append("a window run listed outside its window: %r" % (src.list_calls[:3],))
    if any(d == "state" for (d, _k) in acc.puts):
        bad.append("a window run wrote the cursor")
    if out.get("already_stored") != 4 or out.get("failed") != 0:
        bad.append("four stored blobs must read already_stored=4, failed=0: %r" % ({k: v for k, v in out.items() if k != "cursor"},))
    docs = cov_docs(acc)
    if not docs or not all(d.get("recollect") is True for d in docs):
        bad.append("coverage documents of a window run must carry recollect=true")
    for d in docs:
        for r in d["records"]:
            if r.get("gap"):
                bad.append("already stored read as a gap")
                break
    if not os.path.exists(LAMBDA):
        bad.append("no collector handler")
    else:
        spec = importlib.util.spec_from_file_location("c1_handler", LAMBDA)
        h = importlib.util.module_from_spec(spec)
        sys.path.insert(0, PKG)
        spec.loader.exec_module(h)
        ok = h.parse_recollect({"recollect": {"start": "2026-10-15T00:00:00Z", "end": "2026-10-16T00:00:00Z"}}, NOW)
        if tuple(ok) != ("2026-10-15T00:00:00Z", "2026-10-16T00:00:00Z"):
            bad.append("parse_recollect returned %r" % (ok,))
        for name, ev in (("missing end", {"recollect": {"start": "2026-10-15T00:00:00Z"}}),
                         ("end before start", {"recollect": {"start": "2026-10-16T00:00:00Z", "end": "2026-10-15T00:00:00Z"}}),
                         ("older than 7 days", {"recollect": {"start": "2026-10-01T00:00:00Z", "end": "2026-10-02T00:00:00Z"}}),
                         ("span over 7 days", {"recollect": {"start": "2026-10-08T00:00:00Z", "end": "2026-10-16T11:00:00Z"}}),
                         ("not strings", {"recollect": {"start": 1, "end": 2}})):
            try:
                h.parse_recollect(ev, NOW)
                bad.append("parse_recollect accepted %s" % name)
            except ValueError:
                pass
    if bad:
        print("C1-RECOLLECT-REFUSED " + "; ".join(bad))
        return 1
    print("C1-RECOLLECT-OK")
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"raw": raw, "switch": switch, "recollect": recollect, "derive_time": derive_time,
          "derive_par": derive_par, "derive_client": derive_client}.get(mode)
    try:
        sys.exit(fn() if fn else 2)
    except FileNotFoundError as e:
        print("C1-%s-REFUSED missing %s" % (mode.upper(), e))
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print("C1-%s-REFUSED %s: %s" % (mode.upper(), type(e).__name__, str(e)[:200]))
        sys.exit(1)
