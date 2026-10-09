"""MDPF_DEMQUE round 5, DQ-t-16 criterion AC2: the REAL standing request prices per run. Runs
`python data/mdpf/scripts/demque/standing.py --quote requests/ETFS_RIVALS-HISTORY-OWED-DAILY.json` (files only; the standing
shape's quote, beside bbg_quote.py, which DQ-t-15 owns this round) and requires: rc 0, a JSON
line with "per_run": true and cells {"bloomberg_history": <the request's cap_cells_per_run>}, and the request file carrying
"shape": "standing". SSEAM-OK; else SSEAM-BAD <reason>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

MOD = os.path.join("data", "mdpf", "scripts", "demque", "standing.py")
REQ = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "requests", "ETFS_RIVALS-HISTORY-OWED-DAILY.json")

if __name__ == "__main__":
    if not os.path.isfile(MOD):
        print("SSEAM-BAD no file " + MOD)
        sys.exit(1)
    with open(REQ, encoding="utf-8") as fh:
        req = json.load(fh)
    if req.get("shape") != "standing":
        print("SSEAM-BAD request shape %r, not 'standing'" % req.get("shape"))
        sys.exit(1)
    r = subprocess.run([sys.executable, MOD, "--quote", REQ], capture_output=True, text=True, timeout=100, check=False)
    print(r.stdout[-1500:] + r.stderr[-800:])
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    if r.returncode != 0 or not lines:
        print("SSEAM-BAD rc=%d no JSON line" % r.returncode)
        sys.exit(1)
    q = json.loads(lines[-1])
    if q.get("per_run") is not True or (q.get("cells") or {}).get("bloomberg_history") != req.get("cap_cells_per_run"):
        print("SSEAM-BAD per_run=%r cells=%r cap=%r" % (q.get("per_run"), q.get("cells"), req.get("cap_cells_per_run")))
        sys.exit(1)
    print("SSEAM-OK per_run cells=%r" % (q.get("cells"),))
    sys.exit(0)
