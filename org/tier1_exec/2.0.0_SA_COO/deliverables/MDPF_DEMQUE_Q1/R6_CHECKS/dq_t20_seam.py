"""MDPF_DEMQUE round 6, DQ-t-20 criterion AC2: the REAL history reserve reads at or above the ledger's measured daily history draw.
Runs `python data/mdpf/scripts/demque/ceiling_from_ledger.py --print` (reads the served demand ledger, read-only) for the measured
largest-day history cells, then reads data/mdpf/scripts/demque/bbg_allowance.json: history.reserve.value must be an int >= that draw,
claim "held", and its basis must name the demand ledger. RSVL-OK; else RSVL-BAD <reason>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

HOME = os.path.join("data", "mdpf", "scripts", "demque")

if __name__ == "__main__":
    r = subprocess.run([sys.executable, os.path.join(HOME, "ceiling_from_ledger.py"), "--print"], capture_output=True, text=True,
                       timeout=100, check=False)
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    if r.returncode != 0 or not lines:
        print("RSVL-BAD ceiling_from_ledger rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-400:]))
        sys.exit(1)
    measured = (json.loads(lines[-1]).get("history") or {}).get("value")
    with open(os.path.join(HOME, "bbg_allowance.json"), encoding="utf-8") as fh:
        res = (json.load(fh).get("history") or {}).get("reserve") or {}
    v = res.get("value")
    print("measured history day=%r reserve=%r" % (measured, res))
    if not isinstance(measured, int) or not isinstance(v, int) or v < measured or res.get("claim") != "held" \
            or "demand_ledger" not in str(res.get("basis", "")):
        print("RSVL-BAD reserve %r vs measured %r" % (v, measured))
        sys.exit(1)
    print("RSVL-OK history.reserve=%d >= measured %d" % (v, measured))
    sys.exit(0)
