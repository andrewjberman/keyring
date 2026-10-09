"""MDPF_DEMQUE round 4, DQ-t-10 criterion AC2: the reserve estimated from the REAL tier-1 producers' code. Runs
`python data/mdpf/scripts/demque/reserve_estimate.py --print`, which reads the producers as text (never imports them) and prints ONE JSON
line: {"bql": {"value": int, "claim": "held", "basis": str, "margin": float, "producers": {name: cells, ...}}, ...} for every channel it
can estimate. Requires a "bql" entry with an int value >= 0, claim exactly "held", a non-empty basis, a stated margin, and per-producer
parts whose sum times (1 + margin) rounds to the value. RSEAM-OK; else RSEAM-BAD <reason>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

MOD = os.path.join("data", "mdpf", "scripts", "demque", "reserve_estimate.py")

if __name__ == "__main__":
    if not os.path.isfile(MOD):
        print("RSEAM-BAD no file " + MOD)
        sys.exit(1)
    r = subprocess.run([sys.executable, MOD, "--print"], capture_output=True, text=True, timeout=100, check=False)
    print(r.stdout[-2000:] + r.stderr[-800:])
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    if r.returncode != 0 or not lines:
        print("RSEAM-BAD rc=%d no JSON line" % r.returncode)
        sys.exit(1)
    d = json.loads(lines[-1]).get("bql") or {}
    v, m, parts = d.get("value"), d.get("margin"), d.get("producers") or {}
    if not isinstance(v, int) or v < 0 or d.get("claim") != "held" or not d.get("basis") or not isinstance(m, (int, float)):
        print("RSEAM-BAD bql entry %r" % (d,))
        sys.exit(1)
    if not parts or round(sum(int(x) for x in parts.values()) * (1 + m)) != v:
        print("RSEAM-BAD parts %r x (1 + %r) != %r" % (parts, m, v))
        sys.exit(1)
    print("RSEAM-OK bql.reserve=%d held margin=%s producers=%s" % (v, m, parts))
    sys.exit(0)
