"""MDPF_DEMQUE round 4, DQ-t-13 criterion AC2: the ranking against the REAL neighbours -- Commonwealth's silver crosswalk and
transactions (read-only) and the ADVI_COTBKF price-need file. Runs `python data/mdpf/scripts/demque/rank.py --probe 10`, which ranks the
first 10 YAHOO rows of the need file and prints one line per security, best first:
  RANK <n> cusip=<cusip> priority=<P1|P2|P3> score=<number> reason=<text>
Requires exactly 10 lines, n = 1..10 in order, priorities non-decreasing (P1 before P2 before P3), and within one priority scores
non-increasing. No account number or name may print. KSEAM-OK; else KSEAM-BAD <reason>.
"""
from __future__ import annotations

import os
import re
import subprocess
import sys

MOD = os.path.join("data", "mdpf", "scripts", "demque", "rank.py")

if __name__ == "__main__":
    if not os.path.isfile(MOD):
        print("KSEAM-BAD no file " + MOD)
        sys.exit(1)
    env = dict(os.environ, PYTHONPATH=os.getcwd())
    r = subprocess.run([sys.executable, MOD, "--probe", "10"], capture_output=True, text=True, timeout=110, check=False, env=env)
    print(r.stdout[-2500:] + r.stderr[-800:])
    rows = re.findall(r"^RANK (\d+) cusip=(\S+) priority=(P[123]) score=([-\d.eE+]+) reason=(.+)$", r.stdout, re.M)
    if r.returncode != 0 or len(rows) != 10:
        print("KSEAM-BAD rc=%d lines=%d" % (r.returncode, len(rows)))
        sys.exit(1)
    if [int(x[0]) for x in rows] != list(range(1, 11)):
        print("KSEAM-BAD ranks not 1..10 in order")
        sys.exit(1)
    for a, b in zip(rows, rows[1:]):
        if a[2] > b[2] or (a[2] == b[2] and float(a[3]) < float(b[3])):
            print("KSEAM-BAD order broken at %s -> %s" % (a[1], b[1]))
            sys.exit(1)
    print("KSEAM-OK 10 ranked; priorities %s" % "".join(x[2][1] for x in rows))
    sys.exit(0)
