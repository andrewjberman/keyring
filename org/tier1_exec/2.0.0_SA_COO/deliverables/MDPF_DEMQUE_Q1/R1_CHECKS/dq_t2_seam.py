"""MDPF_DEMQUE round 1, DQ-t-2 criterion AC2: the seam against the REAL neighbour -- Yahoo Finance, one request.
Runs `python data/mdpf/scripts/demque/yahoo_pull.py --probe AAPL`, which pulls AAPL's whole daily history once (with
actions, unadjusted) through the pacer on a scratch state file and prints:
  PROBE symbol=AAPL status=<status> rows=<n> splits=<k> as_traded_2020-08-28=<price>
AAPL closed at 499.23 as traded on 2020-08-28, the last session before its 4-for-1 split (2020-08-31); Yahoo serves that
day split-adjusted (~124.81). YSEAM-OK when status=OK, rows > 9000, splits >= 1 and the as-traded price is within 2% of
499.23; else YSEAM-BAD. This is the difference control: a pull that forgets to undo splits prints ~124.81 and fails.
"""
from __future__ import annotations

import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_file import run_cli  # noqa: E402

if __name__ == "__main__":
    rc, out = run_cli([os.path.join("data", "mdpf", "scripts", "demque", "yahoo_pull.py"), "--probe", "AAPL"])
    print(out[-3000:])
    m = re.search(r"^PROBE symbol=AAPL status=(\S+) rows=(\d+) splits=(\d+) as_traded_2020-08-28=([\d.]+)", out, re.M)
    if rc != 0 or not m:
        print("YSEAM-BAD rc=%d no PROBE line" % rc)
        sys.exit(1)
    status, rows, splits, px = m.group(1), int(m.group(2)), int(m.group(3)), float(m.group(4))
    if status != "OK" or rows <= 9000 or splits < 1 or abs(px - 499.23) / 499.23 > 0.02:
        print("YSEAM-BAD status=%s rows=%d splits=%d as_traded=%.2f" % (status, rows, splits, px))
        sys.exit(1)
    print("YSEAM-OK rows=%d splits=%d as_traded=%.2f" % (rows, splits, px))
    sys.exit(0)
