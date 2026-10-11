"""MDPF_DEMQUE round 9, DQ-t-32 criterion AC2: the cause instrument on three of the REAL 14 rejected names (S3 + Yahoo reads, nothing written):
`lock_cause.py --names FTHSX,IWS,VWO --json` prints ONE JSON line {"names": [row, ...]}; a row carries symbol, cusip, asset_type, n_checked,
agreement_old_pct (client trade prices against the OLD locked file's as_traded_close), agreement_new_pct (against the NEW draw's),
disagreeing (list of {date, trade_type, near_exdiv, near_split}), first_lock_at, first_lock_predates_floor (bool: first lock before
2026-10-09T03:35Z, commit 52b8a3cca2) and cause in {draw-column, never-met-floor, wrong-symbol, unclassified}.
Checked: 3 rows for exactly those symbols; every field present and typed; agreement_new_pct within 1.5 points of the run's 40.7 (FTHSX),
83.3 (IWS), 87.2 (VWO); cause in the closed set. LCAUSE-OK; else LCAUSE-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

TOOL = os.path.join("data", "mdpf", "scripts", "demque", "lock_cause.py")
WANT = {"FTHSX": 40.7, "IWS": 83.3, "VWO": 87.2}
CAUSES = {"draw-column", "never-met-floor", "wrong-symbol", "unclassified"}
FIELDS = ("symbol", "cusip", "asset_type", "n_checked", "agreement_old_pct", "agreement_new_pct", "disagreeing", "first_lock_at",
          "first_lock_predates_floor", "cause")


def _bad(why):
    print("LCAUSE-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    r = subprocess.run([sys.executable, TOOL, "--names", ",".join(WANT), "--json"], capture_output=True, text=True, timeout=115, check=False)
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    if r.returncode != 0 or not lines:
        return _bad("tool rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip()))
    rows = {x.get("symbol"): x for x in json.loads(lines[-1]).get("names", [])}
    if set(rows) != set(WANT):
        return _bad("symbols %s != %s" % (sorted(rows), sorted(WANT)))
    for sym, row in rows.items():
        miss = [f for f in FIELDS if f not in row]
        new = row.get("agreement_new_pct")
        print("%s: new=%s old=%s checked=%s cause=%s predates=%s disagreeing=%s" % (
            sym, new, row.get("agreement_old_pct"), row.get("n_checked"), row.get("cause"),
            row.get("first_lock_predates_floor"), len(row.get("disagreeing") or [])))
        if miss:
            return _bad("%s lacks %s" % (sym, miss))
        if not isinstance(new, (int, float)) or abs(new - WANT[sym]) > 1.5:
            return _bad("%s agreement_new_pct %r is not within 1.5 of %s" % (sym, new, WANT[sym]))
        if row["cause"] not in CAUSES or not isinstance(row["first_lock_predates_floor"], bool) or not isinstance(row["disagreeing"], list):
            return _bad("%s cause/predates/disagreeing malformed" % sym)
    print("LCAUSE-OK 3 of 3 names read, causes %s" % sorted({r["cause"] for r in rows.values()}))
    return 0


if __name__ == "__main__":
    sys.exit(main())
