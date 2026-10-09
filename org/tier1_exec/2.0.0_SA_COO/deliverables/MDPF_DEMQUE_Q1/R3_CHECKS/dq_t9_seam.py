"""MDPF_DEMQUE round 3, DQ-t-9 criterion AC2: the seam against the REAL neighbours -- the two Bloomberg requests AMGT_RESAPP filed on
the queue (org/missions/D8/MDPF/MDPF_DEMQUE/requests/) and the real producer module they name. Runs
`python data/mdpf/scripts/demque/bbg_quote.py --quote <file>` on each and parses the one JSON line it prints.
Requires: the ICT identity request (channel reference, 1 security x 4 static fields) quotes EXACTLY {"bloomberg_reference": 4}; the ABNB
model-block request quotes a positive integer under "bloomberg_model_block" with a per-group breakdown whose parts sum to it; both carry
"finish_date" (a date or null) and, when null, a non-empty "allowance_gap". BSEAM-OK; else BSEAM-BAD <reason>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys

REQ = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "requests")
MOD = os.path.join("data", "mdpf", "scripts", "demque", "bbg_quote.py")


def q(name: str) -> dict:
    r = subprocess.run([sys.executable, MOD, "--quote", os.path.join(REQ, name)], capture_output=True, text=True, timeout=100,
                       check=False)
    print(r.stdout[-1500:] + r.stderr[-800:])
    if r.returncode != 0:
        raise SystemExit("BSEAM-BAD rc=%d on %s" % (r.returncode, name))
    line = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")][-1]
    return json.loads(line)


if __name__ == "__main__":
    if not os.path.isfile(MOD):
        print("BSEAM-BAD no file " + MOD)
        sys.exit(1)
    ict = q("AMGT_RESAPP-493c-ICT-IDENTITY.json")
    if ict.get("cells") != {"bloomberg_reference": 4}:
        print("BSEAM-BAD ICT cells=%r (want {'bloomberg_reference': 4})" % (ict.get("cells"),))
        sys.exit(1)
    abnb = q("AMGT_RESAPP-107a-ABNB-MODEL-BLOCK.json")
    n = (abnb.get("cells") or {}).get("bloomberg_model_block")
    parts = abnb.get("breakdown") or {}
    if not isinstance(n, int) or n <= 0 or sum(int(v) for v in parts.values()) != n:
        print("BSEAM-BAD ABNB cells=%r breakdown=%r" % (n, parts))
        sys.exit(1)
    for name, d in (("ICT", ict), ("ABNB", abnb)):
        if "finish_date" not in d or (d["finish_date"] is None and not d.get("allowance_gap")):
            print("BSEAM-BAD %s has no finish_date and no allowance_gap" % name)
            sys.exit(1)
    print("BSEAM-OK ICT=4 ABNB=%d (%s)" % (n, ", ".join("%s=%s" % kv for kv in parts.items())))
    sys.exit(0)
