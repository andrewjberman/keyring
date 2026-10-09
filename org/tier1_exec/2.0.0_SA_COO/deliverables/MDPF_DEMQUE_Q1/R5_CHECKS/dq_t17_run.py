"""MDPF_DEMQUE round 5, DQ-t-17 criterion AC2: the REAL comparison, Bloomberg against Yahoo under the total-return method. Runs
`python data/mdpf/scripts/demque/tr_compare.py --names ED,BX,CSCO --out <temp json>`: Bloomberg's stored
DAY_TO_DAY_TOT_RETURN_GROSS_DVDS history (read-only) against a Yahoo pull (as-traded close plus ex-date cash). Requires for every name:
days_compared >= 200; median_abs_daily_diff_bp, cum_tr_bloomberg and cum_tr_yahoo numeric; and an events list (each ex-date or split
with its amount and that day's two returns). TRCMP-OK; else TRCMP-BAD <reason>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

MOD = os.path.join("data", "mdpf", "scripts", "demque", "tr_compare.py")
NAMES = ["ED", "BX", "CSCO"]
NUMS = ("median_abs_daily_diff_bp", "cum_tr_bloomberg", "cum_tr_yahoo")

if __name__ == "__main__":
    if not os.path.isfile(MOD):
        print("TRCMP-BAD no file " + MOD)
        sys.exit(1)
    out = os.path.join(tempfile.mkdtemp(), "tr.json")
    r = subprocess.run([sys.executable, MOD, "--names", ",".join(NAMES), "--out", out], capture_output=True, text=True, timeout=600,
                       check=False)
    print(r.stdout[-2000:] + r.stderr[-800:])
    if r.returncode != 0 or not os.path.isfile(out):
        print("TRCMP-BAD rc=%d no output" % r.returncode)
        sys.exit(1)
    with open(out, encoding="utf-8") as fh:
        d = json.load(fh)
    bad = []
    for n in NAMES:
        e = (d.get("names") or {}).get(n) or {}
        num = all(isinstance(e.get(k), (int, float)) for k in NUMS)
        if not isinstance(e.get("days_compared"), int) or e["days_compared"] < 200 or not num or not isinstance(e.get("events"), list):
            bad.append("%s %r" % (n, {k: e.get(k) for k in ("days_compared",) + NUMS}))
        else:
            print("%s days=%d median_abs_diff_bp=%.2f cum_bbg=%.4f cum_yahoo=%.4f events=%d" % (
                n, e["days_compared"], e["median_abs_daily_diff_bp"], e["cum_tr_bloomberg"], e["cum_tr_yahoo"], len(e["events"])))
    if bad:
        print("TRCMP-BAD " + " | ".join(bad))
        sys.exit(1)
    print("TRCMP-OK %d names" % len(NAMES))
    sys.exit(0)
