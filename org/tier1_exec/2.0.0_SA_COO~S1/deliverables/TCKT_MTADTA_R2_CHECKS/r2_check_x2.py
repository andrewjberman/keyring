"""TCKT_MTADTA round 2, cell MD-x-2 checks (the collector's repair). Run from the repo (worktree) root.

  python r2_check_x2.py coverage    -> X2-COVERAGE-OK    (one coverage object per fire; a planted gap survives the next fire)
  python r2_check_x2.py attribution -> X2-ATTRIBUTION-OK (counts by each blob's own day; the cursor trims by age; id-only actors counted)
  python r2_check_x2.py invoker     -> X2-INVOKER-OK     (collector.tf and the client use the collector alias; keys equal builder output)
  python r2_check_x2.py budget      -> X2-BUDGET-OK      (a fire stops at its time budget, saves what it did, and the next fire finishes the backlog once)

Synthetic values only. The collector API this file drives is fixed in the order's worker face.
"""
import importlib.util
import json
import os
import re
import sys

ROOT = os.getcwd()
sys.path.insert(0, os.path.join(ROOT, "lib"))
PKG = os.path.join(ROOT, "data", "m365_metadata", "scripts", "collector")
COLLECTOR_TF = os.path.join(ROOT, "infra", "aws", "terraform", "trino", "collector.tf")
EIGHT = [n + "@opalinvest.com" for n in ("andrew", "alyssa", "bobby", "manav", "yang", "menachem", "jim", "jeanette")]
CFG = {"population": EIGHT, "object_ids": {}, "subject_key": "synthetic-test-key", "office_ips": []}
CTS = ("Audit.Exchange", "Audit.SharePoint", "Audit.General")


def mod(name):
    p = os.path.join(PKG, name + ".py")
    if not os.path.exists(p):
        raise FileNotFoundError(p)
    spec = importlib.util.spec_from_file_location("x2_" + name, p)
    m = importlib.util.module_from_spec(spec)
    if PKG not in sys.path:
        sys.path.insert(0, PKG)
    spec.loader.exec_module(m)
    return m


def ev(i, who="yang@opalinvest.com", t="2026-10-14T15:00:00", wl="SharePoint", **kw):
    d = {"Id": i, "CreationTime": t, "Operation": "FileAccessed", "Workload": wl, "RecordType": 6, "ResultStatus": "Succeeded",
         "UserId": who, "SiteUrl": "https://synthetic.example/sites/ops", "SourceFileName": "a.xlsx"}
    d.update(kw)
    return d


class Source:
    """list_content returns [{'id', 'created'}] and fetch(ct, id) returns the raw events; ids in `fail` raise on fetch."""

    def __init__(self, blobs, fail=()):
        self.blobs = blobs      # {content_type: [(id, created, [events])]}
        self.fail = set(fail)

    def list_content(self, ct, start, end):
        return [{"id": i, "created": c} for (i, c, _e) in self.blobs.get(ct, [])]

    def fetch(self, ct, blob_id):
        if blob_id in self.fail:
            raise RuntimeError("synthetic fetch failure")
        for (i, _c, e) in self.blobs.get(ct, []):
            if i == blob_id:
                return e
        raise KeyError(blob_id)


class Access:
    def __init__(self):
        self.objs = {}
        self.derived = []

    def derive_silver(self, date):
        self.derived.append(date)
        return {"ok": True, "rows": 0}

    def put(self, dataset, key, body):
        self.objs[(dataset, key)] = body
        return {"ok": True}

    def get_state(self, key):
        return self.objs.get(("state", key))


def blobs():
    return {"Audit.SharePoint": [
        ("a1", "2026-10-14T15:00:00.000Z", [ev("e-a1", t="2026-10-14T15:00:00")]),
        ("a2", "2026-10-14T16:00:00.000Z", [ev("e-a2", t="2026-10-14T16:00:00")]),
        ("b1", "2026-10-15T14:00:00.000Z", [ev("e-b1", t="2026-10-15T14:00:00")])]}


def records(acc, content_type="Audit.SharePoint"):
    out = {}
    for (ds, key), body in acc.objs.items():
        if ds == "gold" and "collection_coverage" in key:
            doc = json.loads(body)
            for r in doc["records"]:
                if r["content_type"] == content_type:
                    out[key] = out.get(key, []) + [r]
    return out


def coverage():
    run = mod("collect")
    cr = mod("coverage_record")
    bad = []
    k1 = cr.fire_key("2026-10-14", "2026-10-15T20:00:00Z")
    k2 = cr.fire_key("2026-10-14", "2026-10-15T21:00:00Z")
    if k1 == k2 or not re.fullmatch(r"m365-metadata/trino/gold/collection_coverage/date=2026-10-14/coverage_20261015T200000Z\.json", k1):
        bad.append("fire_key %r %r" % (k1, k2))
    acc = Access()
    out1 = run.run_once(Source(blobs(), fail={"a2"}), acc, CFG, now="2026-10-15T20:00:00Z")
    first = records(acc)
    if sorted(set(acc.derived)) != ["2026-10-14", "2026-10-15"]:
        bad.append("the collector must call derive_silver once per Eastern day it wrote bronze for: %r" % (acc.derived,))
    k_day14_f1 = [k for k in first if "date=2026-10-14" in k and "20261015T200000Z" in k]
    if not k_day14_f1 or not any(r["gap"] for r in first[k_day14_f1[0]]):
        bad.append("fire 1 did not record the planted gap on 2026-10-14")
    run.run_once(Source(blobs()), acc, CFG, now="2026-10-15T21:00:00Z", cursor=out1["cursor"])
    after = records(acc)
    if k_day14_f1 and not any(r["gap"] for r in after.get(k_day14_f1[0], [])):
        bad.append("fire 2 overwrote fire 1's gap")
    if not any("20261015T210000Z" in k for k in after):
        bad.append("fire 2 wrote no coverage object of its own")
    if bad:
        print("X2-COVERAGE-REFUSED " + "; ".join(bad))
        return 1
    print("X2-COVERAGE-OK objects=%d" % len(after))
    return 0


def attribution():
    run = mod("collect")
    flt = mod("filter")
    bad = []
    acc = Access()
    run.run_once(Source(blobs(), fail={"a2"}), acc, CFG, now="2026-10-15T20:00:00Z")
    rec = records(acc)
    by_day = {}
    for k, rs in rec.items():
        day = re.search(r"date=(\d{4}-\d{2}-\d{2})", k).group(1)
        by_day[day] = rs[0]
    d14, d15 = by_day.get("2026-10-14"), by_day.get("2026-10-15")
    if not d14 or (d14["listed"], d14["fetched"], d14["gap"]) != (2, 1, True):
        bad.append("day 2026-10-14 counts %r" % (d14,))
    if not d15 or (d15["listed"], d15["fetched"], d15["gap"]) != (1, 1, False):
        bad.append("day 2026-10-15 counts %r" % (d15,))
    old = {"last_end": "2026-10-15T19:00:00Z", "seen": {"Audit.SharePoint": {"old-blob": "2026-10-01T00:00:00Z", "recent": "2026-10-15T10:00:00Z"}}}
    out2 = run.run_once(Source(blobs()), Access(), CFG, now="2026-10-15T21:00:00Z", cursor=old)
    seen = out2["cursor"]["seen"].get("Audit.SharePoint")
    if not isinstance(seen, dict) or "old-blob" in seen or "b1" not in seen:
        bad.append("the cursor did not trim by age and keep the new ids: %r" % (seen,))
    guid = "0f1e2d3c-4b5a-6978-8796-a5b4c3d2e1f0"
    kept, c = flt.process_batch([ev("g1", who=guid), ev("o1", who="outsider@opalinvest.com"), ev("m1")], CFG)
    if len(kept) != 1 or c.get("dropped_id_only") != 1 or c["dropped"].get("SharePoint") != 2:
        bad.append("id-only counter %r" % (c,))
    if not all("dropped_id_only" in r for rs in rec.values() for r in rs):
        bad.append("coverage records must carry dropped_id_only")
    if bad:
        print("X2-ATTRIBUTION-REFUSED " + "; ".join(bad))
        return 1
    print("X2-ATTRIBUTION-OK")
    return 0


def invoker():
    run = mod("collect")
    cr = mod("coverage_record")
    ac = mod("access_client")
    import opal_naming as n

    bad = []

    def strip(a):
        return a.split("s3://opal-data-trino/", 1)[1]

    if run.bronze_key(__import__("datetime").date(2026, 10, 15), "Audit.SharePoint", "20261015T200000Z") != strip(
            n.address("m365-metadata", "trino", "bronze", "audit_events", "date=20261015", object="Audit.SharePoint_20261015T200000Z.json.gz")):
        bad.append("bronze key is not builder output")
    if run.CURSOR_KEY != strip(n.address("m365-metadata", "trino", "state", "subscription_cursor", "current", object="cursor.json")):
        bad.append("cursor key is not builder output")
    if cr.fire_key("2026-10-15", "2026-10-15T20:00:00Z") != strip(
            n.address("m365-metadata", "trino", "gold", "collection_coverage", "date=2026-10-15", object="coverage_20261015T200000Z.json")):
        bad.append("coverage key is not builder output")
    seen = {}

    class Payload:
        def read(self):
            return b"{}"

    class Client:
        def invoke(self, **kw):
            seen.update(kw)
            return {"Payload": Payload()}

    inv = ac.lambda_invoker(Client(), "globgrph-trino-access-lambda", "collector")
    inv({"op": "get_state", "key": "k"})
    if seen.get("Qualifier") != "collector":
        bad.append("the client must invoke the collector alias (Qualifier)")
    if not os.path.exists(COLLECTOR_TF):
        bad.append("no collector.tf")
    else:
        t = open(COLLECTOR_TF, encoding="utf-8").read()
        if re.search(r'^\s*data\s+"', t, re.M):
            bad.append("collector.tf still reads a data source")
        pol = re.search(r'resource\s+"aws_iam_policy"\s+"collector".*?\n}\n', t, re.S)
        if not pol or "aws_lambda_alias.collector.arn" not in pol.group(0):
            bad.append("the collector's invoke grant must name the collector alias ARN")
        if pol and re.search(r"s3:|kms:", pol.group(0)):
            bad.append("the collector role holds an S3 or KMS action")
    if bad:
        print("X2-INVOKER-REFUSED " + "; ".join(bad))
        return 1
    print("X2-INVOKER-OK")
    return 0


def budget():
    run = mod("collect")
    bad = []
    n_blobs = 60

    class Clock:
        def __init__(self):
            self.t = 0.0

        def __call__(self):
            return self.t

    clock = Clock()
    fetched_ids = []

    class SlowSource:
        """60 blobs spread over 3 Eastern days; every fetch costs 1 second of the fake clock."""

        def list_content(self, ct, start, end):
            if ct != "Audit.SharePoint":
                return []
            out = []
            for i in range(n_blobs):
                day = 13 + i // 20
                out.append({"id": "b%02d" % i, "created": "2026-10-%02dT15:%02d:00.000Z" % (day, i % 20)})
            return out

        def fetch(self, ct, blob_id):
            clock.t += 1.0
            fetched_ids.append(blob_id)
            i = int(blob_id[1:])
            day = 13 + i // 20
            return [ev("e-" + blob_id, t="2026-10-%02dT15:%02d:00" % (day, i % 20))]

    acc = Access()
    cur = None
    fires = 0
    complete = False
    first = None
    while fires < 10 and not complete:
        clock.t = 0.0
        fires += 1
        out = run.run_once(SlowSource(), acc, CFG, now="2026-10-15T%02d:00:00Z" % (12 + fires), cursor=cur, clock=clock,
                           budget_seconds=25, max_workers=1)
        if first is None:
            first = out
        cur = out["cursor"]
        complete = out.get("complete") is True
    if not first or first.get("complete") is not False or not (0 < first["fetched"] <= 26):
        bad.append("fire 1 must stop at its 25-second budget with complete=False and a partial count: %r" % ({k: v for k, v in (first or {}).items() if k != "cursor"},))
    if not complete or fires < 3:
        bad.append("the backlog should finish in a few fires (fires=%d complete=%r)" % (fires, complete))
    if sorted(fetched_ids) != ["b%02d" % i for i in range(n_blobs)]:
        bad.append("every blob must be fetched exactly once across the fires (fetched %d distinct %d)" % (len(fetched_ids), len(set(fetched_ids))))
    if first and parse_ok(first["cursor"].get("last_end")) is None:
        bad.append("the cursor has no readable last_end")
    docs = [json.loads(b) for (ds, k), b in acc.objs.items() if ds == "gold" and "collection_coverage" in k]
    if not docs or not any(d.get("complete") is False for d in docs) or not any(d.get("complete") is True for d in docs):
        bad.append("coverage documents must carry complete=false for a stopped fire and complete=true for the finishing fire")
    if bad:
        print("X2-BUDGET-REFUSED " + "; ".join(bad))
        return 1
    print("X2-BUDGET-OK fires=%d blobs=%d" % (fires, n_blobs))
    return 0


def parse_ok(v):
    try:
        mod("coverage_record").parse_utc(v)
        return v
    except Exception:  # noqa: BLE001
        return None


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"coverage": coverage, "attribution": attribution, "invoker": invoker, "budget": budget}.get(mode)
    try:
        sys.exit(fn() if fn else 2)
    except FileNotFoundError as e:
        print("X2-%s-REFUSED missing %s" % (mode.upper(), e))
        sys.exit(1)
    except Exception as e:  # noqa: BLE001
        print("X2-%s-REFUSED %s: %s" % (mode.upper(), type(e).__name__, e))
        sys.exit(1)
