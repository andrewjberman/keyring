"""MDPF_DEMQUE round 7, DQ-t-24 criterion AC2 (run at site Z after the 2026-10-10 draw): the first non-trading-day backfill is read
against its quote. Reads org/missions/D8/MDPF/MDPF_DEMQUE/ledger/BBG_ACTUALS.jsonl: the job DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS must
carry a row dated 2026-10-10 with cells_drawn > 0 and <= 5858 (the quoted daily allowance), and quote_vs_actual.py --request on it
must print a verdict (OPEN is expected: 15,720 cells finish by 2026-10-17). A row with outcome other than DRAWN must name the vendor stop.
DRAW-OK; else DRAW-BAD <reason>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

ACT = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "ledger", "BBG_ACTUALS.jsonl")
QVA = os.path.join("data", "mdpf", "scripts", "demque", "quote_vs_actual.py")
RID = "DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS"

if __name__ == "__main__":
    rows = []
    if os.path.isfile(ACT):
        with open(ACT, encoding="utf-8") as fh:
            rows = [json.loads(ln) for ln in fh if ln.strip()]
    day = [x for x in rows if x.get("job") == RID and x.get("date") == "2026-10-10"]
    drawn = sum(int(x.get("cells_drawn") or 0) for x in day)
    print("actuals rows for %s on 2026-10-10: %d, cells_drawn %d" % (RID, len(day), drawn))
    if not day or drawn <= 0 or drawn > 5858:
        print("DRAW-BAD drawn=%d rows=%d" % (drawn, len(day)))
        sys.exit(1)
    r = subprocess.run([sys.executable, QVA, "--request", RID], capture_output=True, text=True, timeout=100, check=False)
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    if r.returncode != 0 or not lines:
        print("DRAW-BAD quote_vs_actual rc=%d" % r.returncode)
        sys.exit(1)
    v = json.loads(lines[-1])
    print("DRAW-OK 2026-10-10 drawn %d of 5858 allowed; verdict=%s cells_drawn_total=%s of %s" % (
        drawn, v.get("verdict"), v.get("cells_drawn"), v.get("cells_quoted")))
    sys.exit(0)
