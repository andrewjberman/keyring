"""MDPF_DEMQUE round 5, DQ-t-15 criterion AC2: one REAL request of each live Bloomberg kind is quoted with a finish day before it runs.
Runs `python data/mdpf/scripts/demque/bbg_quote.py --quote <file>` (reads files only; no Bloomberg call) on:
  reference    requests/SITEZ-SIGNIN-PREFLIGHT-REFDATA-20261009.json
  model_block  requests/AMGT_RESAPP-107a-ABNB-MODEL-BLOCK.json
  history      requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json
Each quote must carry a non-null finish_date and a finish_date_claim. QFIN-OK; else QFIN-BAD <request> <reason>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

MOD = os.path.join("data", "mdpf", "scripts", "demque", "bbg_quote.py")
REQ = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "requests")
KINDS = [("reference", "SITEZ-SIGNIN-PREFLIGHT-REFDATA-20261009.json"),
         ("model_block", "AMGT_RESAPP-107a-ABNB-MODEL-BLOCK.json"),
         ("history", "DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json")]

if __name__ == "__main__":
    bad = []
    for kind, name in KINDS:
        r = subprocess.run([sys.executable, MOD, "--quote", os.path.join(REQ, name)], capture_output=True, text=True,
                           timeout=100, check=False)
        lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
        if r.returncode != 0 or not lines:
            bad.append("%s rc=%d %s" % (name, r.returncode, (r.stderr or r.stdout)[-300:].strip()))
            continue
        q = json.loads(lines[-1])
        print("%s %s finish_date=%s finish_date_claim=%s gap=%s" % (kind, name, q.get("finish_date"), q.get("finish_date_claim"),
                                                                    q.get("allowance_gap")))
        if not q.get("finish_date") or not q.get("finish_date_claim"):
            bad.append("%s no finish day (gap %r)" % (name, q.get("allowance_gap")))
    if bad:
        print("QFIN-BAD " + " | ".join(bad))
        sys.exit(1)
    print("QFIN-OK %d of %d kinds quoted with a finish day" % (len(KINDS), len(KINDS)))
    sys.exit(0)
