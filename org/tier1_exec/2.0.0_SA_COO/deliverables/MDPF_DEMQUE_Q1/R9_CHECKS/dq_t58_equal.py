"""MDPF_DEMQUE round 9, DQ-t-58 criterion AC2: the cell-equality proof of the WIRED incremental path INCLUDING THE TOTAL-RETURN COLUMNS (pair A condition 1).

Reads `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~50/INCREMENTAL_WIRED_EQUALITY_REPORT.json` and requires: no_split_arm.n >= 50 with equal == n and
mismatches == []; cells_compared prices, dividends, splits AND tr all > 0 (tr = the cells of cash, total_return, tr_source, flags compared against the full path's); a split_arm with at
least 1 symbol with refilled false, held_restatement true and files_unchanged true (a gained split is HELD, never written); `relock_held` naming LCEYX and FTHSX (AMENDED 2026-10-13, row W50-S2); http_requests an int <= 120. Then runs
`incremental_equal.py --spot 5 --tr` live (5 symbols, both paths, scratch pacer, TR columns compared) and requires equal 5 of 5 and tr_cells > 0.
WIREEQ-OK; else WIREEQ-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

REPORT = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "deliverables", "0.9.0_WK_MDPF_DEMQUE~50", "INCREMENTAL_WIRED_EQUALITY_REPORT.json")
TOOL = os.path.join("data", "mdpf", "scripts", "demque", "incremental_equal.py")


def _bad(why):
    print("WIREEQ-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(REPORT):
        return _bad("no file " + REPORT)
    d = json.load(open(REPORT, encoding="utf-8"))
    ns, sp = d.get("no_split_arm") or {}, d.get("split_arm") or {}
    cells = d.get("cells_compared") or {}
    print("no_split n=%s equal=%s mismatches=%d | split n=%s held=%s unchanged=%s | cells=%s http=%s" % (
        ns.get("n"), ns.get("equal"), len(ns.get("mismatches") or []), sp.get("n"), sp.get("held_restatement"), sp.get("files_unchanged"), cells, d.get("http_requests")))
    if not (isinstance(ns.get("n"), int) and ns["n"] >= 50 and ns.get("equal") == ns["n"] and not ns.get("mismatches")):
        return _bad("the no-split arm is not 50+ symbols all equal")
    if not all(isinstance(cells.get(k), int) and cells[k] > 0 for k in ("prices", "dividends", "splits", "tr")):
        return _bad("a cell family compared 0 cells (the TR columns must be compared): %s" % cells)
    if not (isinstance(sp.get("n"), int) and sp["n"] >= 1 and sp.get("held_restatement") is True and sp.get("files_unchanged") is True and sp.get("refilled") is False):
        return _bad("the split arm is missing, was written, or did not hold: %s" % sp)
    if not (isinstance(d.get("http_requests"), int) and d["http_requests"] <= 120):
        return _bad("http_requests missing or above 120: %s" % d.get("http_requests"))
    held = d.get("relock_held") or []
    print("relock_held: %s" % held)
    if not ("LCEYX" in held and "FTHSX" in held):
        return _bad("relock_held must name LCEYX and FTHSX (row W50-S2: served LOCKED, a relock over the combined history REJECTS): %s" % held)
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    r = subprocess.run([sys.executable, TOOL, "--spot", "5", "--tr"], capture_output=True, text=True, timeout=100, check=False)
    ls = [x for x in r.stdout.splitlines() if x.strip().startswith("{")]
    spot = json.loads(ls[-1]) if ls else {}
    print("spot: %s" % json.dumps(spot, sort_keys=True))
    if r.returncode != 0 or spot.get("equal") != 5 or spot.get("of") != 5 or not (isinstance(spot.get("tr_cells"), int) and spot["tr_cells"] > 0):
        return _bad("live spot-check is not 5 of 5 with TR cells compared: rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-200:].strip()))
    print("WIREEQ-OK %d symbols equal on a no-split day including %d TR cells; %d gained-split name(s) HELD, files unchanged; http %d" % (ns["n"], cells["tr"], sp["n"], d["http_requests"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
