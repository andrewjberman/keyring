"""MDPF_DEMQUE round 6, DQ-t-19 criterion AC2: FWD-4 READ, not waited on. Runs
`python data/mdpf/scripts/demque/quote_vs_actual.py --request SITEZ-SIGNIN-PREFLIGHT-REFDATA-20261009` (files only: the frozen quote
requests/<id>.quote.json and the actuals ledger/BBG_ACTUALS.jsonl) and requires ONE JSON line whose verdict is ON_TIME or LATE (a read of
a drawn request; OPEN fails this check), with finish_date and drawn_date both present. FWD4-OK verdict=...; else FWD4-BAD <reason>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

MOD = os.path.join("data", "mdpf", "scripts", "demque", "quote_vs_actual.py")
RID = "SITEZ-SIGNIN-PREFLIGHT-REFDATA-20261009"

if __name__ == "__main__":
    if not os.path.isfile(MOD):
        print("FWD4-BAD no file " + MOD)
        sys.exit(1)
    r = subprocess.run([sys.executable, MOD, "--request", RID], capture_output=True, text=True, timeout=100, check=False)
    print(r.stdout[-1500:] + r.stderr[-800:])
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    if r.returncode != 0 or not lines:
        print("FWD4-BAD rc=%d no JSON line" % r.returncode)
        sys.exit(1)
    q = json.loads(lines[-1])
    if q.get("verdict") not in ("ON_TIME", "LATE") or not q.get("finish_date") or not q.get("drawn_date"):
        print("FWD4-BAD %r" % (q,))
        sys.exit(1)
    print("FWD4-OK verdict=%s finish_date=%s drawn_date=%s" % (q["verdict"], q["finish_date"], q["drawn_date"]))
    sys.exit(0)
