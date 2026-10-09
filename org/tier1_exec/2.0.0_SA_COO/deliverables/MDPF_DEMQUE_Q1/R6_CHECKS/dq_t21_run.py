"""MDPF_DEMQUE round 6, DQ-t-21 criterion AC2: the REAL total-return column shows both D1-S3 guards. Runs
`python data/mdpf/scripts/demque/tr_column.py --names LNVGY,FXFXX --out <temp json>` (Yahoo read, Bloomberg stored history read-only; no
price-store write) and requires: an LNVGY row dated 2025-12-11 flagged "missing_cash" (guard a), and FXFXX rows whose tr_source is
"bloomberg" or "accrual" with at least one non-zero total return and no row sourced "yahoo" (guard b). TRCOL-OK; else TRCOL-BAD <reason>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
import tempfile

MOD = os.path.join("data", "mdpf", "scripts", "demque", "tr_column.py")

if __name__ == "__main__":
    if not os.path.isfile(MOD):
        print("TRCOL-BAD no file " + MOD)
        sys.exit(1)
    out = os.path.join(tempfile.mkdtemp(), "trc.json")
    r = subprocess.run([sys.executable, MOD, "--names", "LNVGY,FXFXX", "--out", out], capture_output=True, text=True, timeout=600,
                       check=False)
    print(r.stdout[-1500:] + r.stderr[-800:])
    if r.returncode != 0 or not os.path.isfile(out):
        print("TRCOL-BAD rc=%d no output" % r.returncode)
        sys.exit(1)
    with open(out, encoding="utf-8") as fh:
        d = json.load(fh)
    ln = (d.get("names") or {}).get("LNVGY") or []
    mm = (d.get("names") or {}).get("FXFXX") or []
    flag = [x for x in ln if str(x.get("date", "")).startswith("2025-12-11") and "missing_cash" in (x.get("flags") or [])]
    srcs = {x.get("tr_source") for x in mm}
    nonzero = [x for x in mm if isinstance(x.get("total_return"), (int, float)) and x["total_return"] != 0]
    bad = []
    if not flag:
        bad.append("LNVGY 2025-12-11 not flagged missing_cash")
    if not mm or "yahoo" in srcs or not srcs <= {"bloomberg", "accrual"} or not nonzero:
        bad.append("FXFXX sources %r, non-zero rows %d of %d" % (sorted(map(str, srcs)), len(nonzero), len(mm)))
    if bad:
        print("TRCOL-BAD " + " | ".join(bad))
        sys.exit(1)
    print("TRCOL-OK LNVGY missing_cash 2025-12-11; FXFXX %d rows from %s, %d non-zero" % (len(mm), sorted(srcs), len(nonzero)))
    sys.exit(0)
