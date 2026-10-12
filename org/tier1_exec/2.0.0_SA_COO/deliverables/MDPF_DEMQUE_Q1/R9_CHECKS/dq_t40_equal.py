"""MDPF_DEMQUE round 9, DQ-t-40 criterion AC2: the cell-equality proof of the batched incremental pull against the per-symbol path.
Reads `org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~32/EQUALITY_REPORT.json` and requires: n_symbols >= 50 with at least
3 distinct asset classes named; equal_symbols == n_symbols_compared and mismatches == [] (or each listed with its cell); compared cell counts for
prices, dividends and splits all > 0 (dividends and splits INSIDE the incremental window); an isolated-failure arm (a planted bad ticker
recorded as a failure for that symbol alone, 0 price cells stored for it, the rest of its batch equal); and the MEASURED HTTP request counts of
both paths with a stated `verdict`. Then runs `batch_pull.py --spot 5` live (5 symbols, both paths) and requires equal 5 of 5.
EQ-OK <n symbols, http_batch vs http_single, verdict>; else EQ-BAD <why>. The check does not require the verdict to favour batching.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

REPORT = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "deliverables", "0.9.0_WK_MDPF_DEMQUE~32", "EQUALITY_REPORT.json")
TOOL = os.path.join("data", "mdpf", "scripts", "demque", "batch_pull.py")


def _bad(why):
    print("EQ-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(REPORT):
        return _bad("no file " + REPORT)
    d = json.load(open(REPORT, encoding="utf-8"))
    n = d.get("n_symbols_compared")
    classes = d.get("asset_classes") or []
    cells = d.get("cells_compared") or {}
    iso = d.get("isolated_failure") or {}
    http = d.get("http_requests") or {}
    print("n=%s classes=%s equal=%s mismatches=%d cells=%s http=%s verdict=%s" % (
        n, classes, d.get("equal_symbols"), len(d.get("mismatches") or []), cells, http, d.get("verdict")))
    if not (isinstance(n, int) and n >= 50 and len(set(classes)) >= 3):
        return _bad("fewer than 50 symbols or fewer than 3 asset classes")
    if d.get("equal_symbols") != n or d.get("mismatches"):
        return _bad("batched rows differ from per-symbol rows: %s" % (d.get("mismatches") or [])[:3])
    if not all(isinstance(cells.get(k), int) and cells[k] > 0 for k in ("prices", "dividends", "splits")):
        return _bad("a cell family compared 0 cells: %s" % cells)
    if not (iso.get("symbol") and iso.get("price_cells_stored") == 0 and iso.get("rest_of_batch_equal") is True):
        return _bad("the isolated-failure arm is missing or not clean: %s" % iso)
    if not (isinstance(http.get("per_symbol"), int) and isinstance(http.get("batched"), int) and d.get("verdict")):
        return _bad("HTTP request counts of both paths and a verdict are required: %s" % http)
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    r = subprocess.run([sys.executable, TOOL, "--spot", "5"], capture_output=True, text=True, timeout=100, check=False)
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    spot = json.loads(lines[-1]) if lines else {}
    print("spot: %s" % json.dumps(spot, sort_keys=True))
    if r.returncode != 0 or spot.get("equal") != 5 or spot.get("of") != 5:
        return _bad("live spot-check is not 5 of 5: rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-200:].strip()))
    print("EQ-OK n=%d, http per_symbol=%d batched=%d, verdict=%s" % (n, http["per_symbol"], http["batched"], d["verdict"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
