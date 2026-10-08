"""MDPF_DEMQUE round 1, DQ-t-1 criterion AC2: the seam against the REAL neighbour -- Commonwealth's own silver
transactions. Runs `python data/mdpf/scripts/demque/lock.py --probe 5`, which must read the real transactions for the
first 5 YAHOO-sourced CUSIPs of the ADVI_COTBKF price-need file and print one line per CUSIP:
  PROBE cusip=<cusip> symbol=<symbol or -> trades=<n>
SEAM-OK when exactly 5 PROBE lines print, rc 0, and at least one has trades > 0; else SEAM-BAD.
"""
from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_file import run_cli  # noqa: E402

if __name__ == "__main__":
    rc, out = run_cli([os.path.join("data", "mdpf", "scripts", "demque", "lock.py"), "--probe", "5"])
    print(out[-3000:])
    rows = re.findall(r"^PROBE cusip=(\S+) symbol=(\S+) trades=(\d+)", out, re.M)
    if rc != 0 or len(rows) != 5 or not any(int(r[2]) > 0 for r in rows):
        print("SEAM-BAD rc=%d probe_lines=%d" % (rc, len(rows)))
        sys.exit(1)
    print("SEAM-OK probe_lines=5 with_trades=%d" % sum(1 for r in rows if int(r[2]) > 0))
    sys.exit(0)
