"""MDPF_DEMQUE round 5, DQ-t-18 criterion AC2 (run at site Z): the demand ledger names OPAL_BBGTML. Runs the uploader DRY
(`python data/mdpf/scripts/demque/bbg_ledger_upload.py --day <day>`; no AWS write) for the given day (default: the latest bbg_budget
ledger day on this box) and requires at least one row whose mode starts with "bbgtml": a metered notebook run, or the one
"bbgtml-unmetered" row (cells null, claim "absent") on a day the meter recorded nothing. BBGTML-OK; else BBGTML-BAD <reason>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

MOD = os.path.join("data", "mdpf", "scripts", "demque", "bbg_ledger_upload.py")

if __name__ == "__main__":
    day = sys.argv[1] if len(sys.argv) > 1 else None
    if day is None:
        sys.path.insert(0, os.path.join("data", "etfs", "scripts", "rivalfunds"))
        import bbg_budget  # noqa: E402
        days = sorted(p.stem.replace("bbg_budget_", "") for p in bbg_budget.ledger_dir().glob("bbg_budget_*.jsonl"))
        if not days:
            print("BBGTML-BAD no bbg_budget ledger day under %s" % bbg_budget.ledger_dir())
            sys.exit(1)
        day = days[-1]
    r = subprocess.run([sys.executable, MOD, "--day", day], capture_output=True, text=True, timeout=100, check=False)
    print(r.stdout[-2500:] + r.stderr[-800:])
    rows = [json.loads(ln) for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    hits = [x for x in rows if str(x.get("mode", "")).startswith("bbgtml")]
    if r.returncode != 0 or not hits:
        print("BBGTML-BAD rc=%d day=%s rows=%d bbgtml_rows=0" % (r.returncode, day, len(rows)))
        sys.exit(1)
    print("BBGTML-OK day=%s bbgtml_rows=%d of %d" % (day, len(hits), len(rows)))
    sys.exit(0)
