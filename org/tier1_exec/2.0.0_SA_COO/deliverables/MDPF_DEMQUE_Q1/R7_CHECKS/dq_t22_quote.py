"""MDPF_DEMQUE round 7, DQ-t-22 criterion AC2: the REAL 15,720-cell history request quoted over non-trading days. Runs
`python data/mdpf/scripts/demque/bbg_quote.py --quote requests/DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json --today <day>` twice (files and
the trading calendar only). Day 2026-10-09 (a trading day): finish_date 2026-10-17 (the third non-trading day: 10-10, 10-11, 10-17 at
5,858 a day), allowance_today 0, claims.ceiling "measured". Day 2026-10-10 (a Saturday): allowance_today 5858. NTDQ-OK; else NTDQ-BAD.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

MOD = os.path.join("data", "mdpf", "scripts", "demque", "bbg_quote.py")
REQ = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "requests", "DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS.json")


def q(day):
    r = subprocess.run([sys.executable, MOD, "--quote", REQ, "--today", day], capture_output=True, text=True, timeout=100, check=False)
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    if r.returncode != 0 or not lines:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip())
    return json.loads(lines[-1]), None


if __name__ == "__main__":
    a, ea = q("2026-10-09")
    b, eb = q("2026-10-10")
    if ea or eb:
        print("NTDQ-BAD " + (ea or eb))
        sys.exit(1)
    print("2026-10-09: finish_date=%s allowance_today=%s ceiling_claim=%s gap=%s" % (
        a.get("finish_date"), a.get("allowance_today"), (a.get("claims") or {}).get("ceiling"), a.get("allowance_gap")))
    print("2026-10-10: finish_date=%s allowance_today=%s" % (b.get("finish_date"), b.get("allowance_today")))
    ok = (a.get("finish_date") == "2026-10-17" and a.get("allowance_today") == 0
          and (a.get("claims") or {}).get("ceiling") == "measured" and b.get("allowance_today") == 5858)
    if not ok:
        print("NTDQ-BAD")
        sys.exit(1)
    print("NTDQ-OK finish 2026-10-17; trading day 0; Saturday 5858; ceiling measured")
    sys.exit(0)
