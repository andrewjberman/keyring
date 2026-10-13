"""MDPF_DEMQUE round 9, DQ-t-48 criterion AC3: the cell-equality proof of the incremental append against the full re-pull. Reads
`org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~40/INCREMENTAL_EQUALITY_REPORT.json` and requires: no_split_arm.n >= 50 with equal == n and
mismatches == []; cells_compared prices, dividends, splits all > 0; a split_arm with at least 1 symbol whose gained split triggered the full re-pull
(refilled == true) and equal == true; http_requests an int <= 120. Then runs `incremental_equal.py --spot 5` live (5 symbols, both paths, scratch pacer) and requires
equal 5 of 5. INCEQ-OK; else INCEQ-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

REPORT = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "deliverables", "0.9.0_WK_MDPF_DEMQUE~40", "INCREMENTAL_EQUALITY_REPORT.json")
TOOL = os.path.join("data", "mdpf", "scripts", "demque", "incremental_equal.py")


def _bad(why):
    print("INCEQ-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(REPORT):
        return _bad("no file " + REPORT)
    d = json.load(open(REPORT, encoding="utf-8"))
    ns, sp = d.get("no_split_arm") or {}, d.get("split_arm") or {}
    cells = d.get("cells_compared") or {}
    print("no_split n=%s equal=%s mismatches=%d | split n=%s refilled=%s equal=%s | cells=%s http=%s" % (
        ns.get("n"), ns.get("equal"), len(ns.get("mismatches") or []), sp.get("n"), sp.get("refilled"), sp.get("equal"), cells, d.get("http_requests")))
    if not (isinstance(ns.get("n"), int) and ns["n"] >= 50 and ns.get("equal") == ns["n"] and not ns.get("mismatches")):
        return _bad("the no-split arm is not 50+ symbols all equal")
    if not all(isinstance(cells.get(k), int) and cells[k] > 0 for k in ("prices", "dividends", "splits")):
        return _bad("a cell family compared 0 cells: %s" % cells)
    if not (isinstance(sp.get("n"), int) and sp["n"] >= 1 and sp.get("refilled") is True and sp.get("equal") is True):
        return _bad("the split arm is missing, did not refill, or is not equal: %s" % sp)
    if not (isinstance(d.get("http_requests"), int) and d["http_requests"] <= 120):
        return _bad("http_requests missing or above 120: %s" % d.get("http_requests"))
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    r = subprocess.run([sys.executable, TOOL, "--spot", "5"], capture_output=True, text=True, timeout=100, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    spot = json.loads(ls[-1]) if ls else {}
    print("spot: %s" % json.dumps(spot, sort_keys=True))
    if r.returncode != 0 or spot.get("equal") != 5 or spot.get("of") != 5:
        return _bad("live spot-check is not 5 of 5: rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-200:].strip()))
    print("INCEQ-OK %d symbols equal on a no-split day, %d split arm refilled and equal, http %d" % (ns["n"], sp["n"], d["http_requests"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
