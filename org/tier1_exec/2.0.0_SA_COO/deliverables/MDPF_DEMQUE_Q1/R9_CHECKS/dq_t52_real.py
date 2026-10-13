"""MDPF_DEMQUE round 9, DQ-t-52 criterion AC2 (REAL crosswalk, silver transactions, price index and queue files, S3 read only, NO vendor call, nothing written):
`priority_gate.py --census` prints ONE JSON line {"index": {"names", "P1", "P2", "P3"}, "excluded_from_extension", "files": [{"name", "securities", "P1", "P2", "P3"}],
"rule": "..."}. Required: index names == P1 + P2 + P3 and names >= 300; excluded_from_extension == P2 + P3 of the index; the P3 count of the index is >= 1 (the 8 known former-client
names are landed); every file row has securities == P1 + P2 + P3; the IRPT device queue copy (`IRPT_BCKEND-AS-TRADED-CLOSES-878.json` under ~/.opal/demque/queue) carries P2 == 0 and P3 == 0;
the line names the rule (Andrew-direct 2026-10-13: former clients never drawn, match-open waits). GATE-REAL-OK; else GATE-REAL-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "priority_gate.py")


def _bad(why):
    print("GATE-REAL-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    r = subprocess.run([sys.executable, TOOL, "--census"], capture_output=True, text=True, timeout=115, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    if r.returncode != 0 or not ls:
        return _bad("rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip()))
    d = json.loads(ls[-1])
    ix = d.get("index") or {}
    print("index %s excluded_from_extension=%s files=%d" % (ix, d.get("excluded_from_extension"), len(d.get("files") or [])))
    for f in d.get("files") or []:
        print("  %-52s n=%s P1=%s P2=%s P3=%s" % (str(f.get("name"))[:52], f.get("securities"), f.get("P1"), f.get("P2"), f.get("P3")))
    ints = all(isinstance(ix.get(k), int) for k in ("names", "P1", "P2", "P3"))
    files = d.get("files") or []
    irpt = [f for f in files if "IRPT_BCKEND-AS-TRADED-CLOSES-878" in str(f.get("name")) and "queue" in str(f.get("name"))]
    arms = {
        "ints": ints,
        "index_sum": ints and ix["names"] == ix["P1"] + ix["P2"] + ix["P3"] and ix["names"] >= 300,
        "excluded": ints and d.get("excluded_from_extension") == ix["P2"] + ix["P3"],
        "p3_present": ints and ix["P3"] >= 1,
        "file_rows": bool(files) and all(f.get("securities") == (f.get("P1") or 0) + (f.get("P2") or 0) + (f.get("P3") or 0) for f in files),
        "irpt_queue_p1_only": bool(irpt) and all(f.get("P2") == 0 and f.get("P3") == 0 for f in irpt),
        "rule": "former client" in str(d.get("rule", "")).lower() and "2026-10-13" in str(d.get("rule", "")),
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arms=" + ",".join(bad))
    print("GATE-REAL-OK index %d names (P1 %d, P2 %d, P3 %d): %d left out of the extension" % (ix["names"], ix["P1"], ix["P2"], ix["P3"], d["excluded_from_extension"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
