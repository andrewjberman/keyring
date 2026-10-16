"""TCKT_MTADTA round 1, cell MD-c-1 checks. Run from the repo (worktree) root.

  python r1_check_c1.py guard    -> C1-GUARD-OK    (population filter + field levers, planted events)
  python r1_check_c1.py coverage -> C1-COVERAGE-OK (coverage record: gap, quiet day, LOST past 7 days)
  python r1_check_c1.py collect  -> C1-COLLECT-OK  (one fire, end to end, writing only through the access door)

Planted values are SYNTHETIC. The collector API this file drives is fixed in the order's worker face.
"""
import gzip
import importlib.util
import json
import os
import re
import sys

ROOT = os.getcwd()
PKG = os.path.join(ROOT, "data", "m365_metadata", "scripts", "collector")
EIGHT = ["andrew", "alyssa", "bobby", "manav", "yang", "menachem", "jim", "jeanette"]
EIGHT = [n + "@opalinvest.com" for n in EIGHT]
CFG = {
    "population": EIGHT,
    "object_ids": {},
    "subject_key": "synthetic-test-key",
    "office_ips": ["198.51.100.1"],
}


def mod(name):
    p = os.path.join(PKG, name + ".py")
    if not os.path.exists(p):
        raise FileNotFoundError(p)
    spec = importlib.util.spec_from_file_location("c1_" + name, p)
    m = importlib.util.module_from_spec(spec)
    sys.path.insert(0, PKG)
    spec.loader.exec_module(m)
    return m


def ev(**kw):
    base = {"Id": "id-1", "CreationTime": "2026-10-15T14:00:00", "Operation": "FileAccessed", "Workload": "SharePoint",
            "RecordType": 6, "ResultStatus": "Succeeded", "UserId": "yang@opalinvest.com", "ClientIP": "203.0.113.7",
            "SiteUrl": "https://opalinvest.sharepoint.com/sites/ops", "SourceFileName": "recon.xlsx",
            "SourceRelativeUrl": "Shared Documents/Ops", "ObjectId": "https://x/recon.xlsx", "ItemType": "File",
            "ExtendedProperties": [{"Name": "secret", "Value": "SHOULD-NOT-SURVIVE"}]}
    base.update(kw)
    return base


def guard():
    f = mod("filter")
    bad = []
    kept, counters = f.process_batch([
        ev(Id="in-1", UserId="YANG@OpalInvest.com"),
        ev(Id="out-1", UserId="outsider@opalinvest.com"),
        ev(Id="via-1", UserId="svc@opalinvest.com", SendAsUserSmtp="manav@opalinvest.com", Workload="Exchange"),
        ev(Id="mail-1", Workload="Exchange", Operation="Send", Subject="Q3 wire for ACME Fund",
           Recipients=["zed@opalinvest.com", "bob@evil.example.com", "alyssa@opalinvest.com"], ClientIP="198.51.100.1"),
        ev(Id="mail-2", Workload="Exchange", Operation="Send", Subject="Q3 wire for ACME Fund", Recipients=[]),
    ], CFG)
    ids = sorted(k.get("event_id") for k in kept)
    if ids != ["in-1", "mail-1", "mail-2", "via-1"]:
        bad.append("kept ids %r" % (ids,))
    blob = json.dumps(kept)
    for s in ("outsider@", "SHOULD-NOT-SURVIVE", "zed@opalinvest.com", "evil.example.com", "203.0.113.7", "198.51.100.1",
              "Q3 wire", "ACME Fund", "ExtendedProperties"):
        if s in blob:
            bad.append("leaked %r" % s)
    if "internal-other" not in blob or '"external"' not in blob and "external" not in blob:
        bad.append("class tokens missing")
    if "alyssa@opalinvest.com" not in blob:
        bad.append("a member's own address was not kept")
    if not any(k.get("actor") == "yang@opalinvest.com" for k in kept):
        bad.append("actor not lower-cased to the member")
    hs = [k.get("subject_hash") for k in kept if k.get("event_id") in ("mail-1", "mail-2")]
    if len(hs) != 2 or hs[0] != hs[1] or not re.fullmatch(r"[0-9a-f]{64}", str(hs[0])):
        bad.append("subject hash not a stable 64-hex value %r" % (hs,))
    cfg2 = dict(CFG, subject_key="another-key")
    k2, _ = f.process_batch([ev(Id="mail-3", Workload="Exchange", Subject="Q3 wire for ACME Fund")], cfg2)
    if k2 and k2[0].get("subject_hash") == hs[0]:
        bad.append("subject hash does not depend on the key")
    flags = {k.get("event_id"): k.get("client_ip_class") for k in kept}
    if flags.get("in-1") != "remote" or flags.get("mail-1") != "office":
        bad.append("ip class %r" % flags)
    if sum(v for v in (counters.get("dropped") or {}).values()) != 1:
        bad.append("drop counter %r" % (counters,))
    if getattr(f, "CONTENT_TYPES", None) != ["Audit.Exchange", "Audit.SharePoint", "Audit.General"]:
        bad.append("CONTENT_TYPES must be the three, AzureActiveDirectory out")
    if bad:
        print("C1-GUARD-REFUSED " + "; ".join(bad))
        return 1
    print("C1-GUARD-OK kept=%d dropped=%s" % (len(kept), counters.get("dropped")))
    return 0


def coverage():
    c = mod("coverage_record")
    now = "2026-10-16T12:00:00Z"
    bad = []
    quiet = c.build_record("2026-10-15", "Audit.SharePoint", listed=3, fetched=3, events=0, dropped={}, now=now)
    gap = c.build_record("2026-10-15", "Audit.SharePoint", listed=3, fetched=1, events=2, dropped={"SharePoint": 4}, now=now)
    lost = c.build_record("2026-10-01", "Audit.SharePoint", listed=0, fetched=0, events=0, dropped={}, now=now, gap=True)
    if quiet.get("status") != "no activity collected" or quiet.get("gap"):
        bad.append("quiet day %r" % quiet)
    if not gap.get("gap") or gap.get("status") == "no activity collected" or gap.get("dropped") != {"SharePoint": 4}:
        bad.append("gap day %r" % gap)
    if lost.get("status") != "LOST":
        bad.append("a gap older than 7 days must read LOST: %r" % lost)
    if quiet.get("status") == gap.get("status"):
        bad.append("a quiet day and a gap day read alike")
    if bad:
        print("C1-COVERAGE-REFUSED " + "; ".join(bad))
        return 1
    print("C1-COVERAGE-OK")
    return 0


class Source:
    def __init__(self, batches):
        self.batches = batches

    def list_content(self, content_type, start, end):
        return ["blob-%s-%d" % (content_type, i) for i in range(len(self.batches.get(content_type, [])))]

    def fetch(self, content_type, blob):
        i = int(blob.rsplit("-", 1)[1])
        return self.batches[content_type][i]


class Access:
    def __init__(self):
        self.puts = []

    def put(self, dataset, key, body):
        self.puts.append((dataset, key, body))
        return {"ok": True}

    def get_state(self, key):
        return None


def collect():
    run = mod("collect")
    bad = []
    src = Source({"Audit.SharePoint": [[ev(Id="s1"), ev(Id="s2", UserId="nobody@opalinvest.com")]],
                  "Audit.Exchange": [[ev(Id="x1", Workload="Exchange")]], "Audit.General": []})
    acc = Access()
    out = run.run_once(src, acc, CFG, now="2026-10-15T15:00:00Z")
    bronze = [p for p in acc.puts if p[0] == "bronze"]
    if not bronze:
        bad.append("nothing written to bronze")
    seen = []
    for _, key, body in bronze:
        if not key.startswith("m365-metadata/trino/bronze/audit_events/date="):
            bad.append("bronze key %r" % key)
        seen += [json.loads(x)["event_id"] for x in gzip.decompress(body).decode().splitlines() if x.strip()]
    if sorted(seen) != ["s1", "x1"]:
        bad.append("bronze holds %r" % (sorted(seen),))
    if not any(p[0] == "state" for p in acc.puts):
        bad.append("no cursor written")
    if not any(p[0] == "gold" and "collection_coverage" in p[1] for p in acc.puts):
        bad.append("no coverage record written")
    again = run.run_once(src, acc, CFG, now="2026-10-15T15:00:00Z", cursor=(out or {}).get("cursor"))
    if again and again.get("fetched", 0) != 0:
        bad.append("a second fire fetched the same blobs again")
    srcs = "".join(open(os.path.join(PKG, f), encoding="utf-8").read() for f in os.listdir(PKG) if f.endswith(".py"))
    if re.search(r"client\(\s*['\"]s3['\"]|resource\(\s*['\"]s3['\"]", srcs):
        bad.append("the collector holds an S3 client; it must write through the access door only")
    if bad:
        print("C1-COLLECT-REFUSED " + "; ".join(bad))
        return 1
    print("C1-COLLECT-OK bronze_objects=%d" % len(bronze))
    return 0


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    fn = {"guard": guard, "coverage": coverage, "collect": collect}.get(mode)
    try:
        sys.exit(fn() if fn else 2)
    except FileNotFoundError as e:
        print("%s-REFUSED missing %s" % (mode.upper(), e))
        sys.exit(1)
