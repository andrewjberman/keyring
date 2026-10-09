"""MDPF_DEMQUE round 2, DQ-t-6 criterion AC2: the hop-6 file contract ADVI_COTBKF reads (CTO adjudication 2026-10-09T0108Z, act 2).
Reads org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~5/PRICE_STORE_CONTRACT.md and requires:
  - the store's per-CUSIP address and its index address, each EXACTLY as lib.opal_naming.address() prints them today
    (computed here from the builder, so a hand-typed or drifted path fails);
  - a line `KEY NAMESPACE: ` naming the 9-character Commonwealth CUSIP;
  - the column names date, close_served, as_traded_close, and claim;
  - a worked example for CUSIP 00162Q866 (AMLP).
CONTRACT-OK; else CONTRACT-BAD <reason>. Whether dell2 can consume it is graded at the drain's AMLP trace, not here.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.getcwd())

DOC = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "deliverables", "0.9.0_WK_MDPF_DEMQUE~5",
                   "PRICE_STORE_CONTRACT.md")

if __name__ == "__main__":
    if not os.path.isfile(DOC):
        print("CONTRACT-BAD no file " + DOC)
        sys.exit(1)
    from lib.opal_naming import address
    need = [str(address("yahoo", "global", "silver", "price_history", "cusip=00162Q866")),
            str(address("yahoo", "global", "silver", "price_history", "index"))]
    text = open(DOC, encoding="utf-8").read()
    missing = [n for n in need if n not in text]
    if missing:
        print("CONTRACT-BAD builder address absent: " + ", ".join(missing))
        sys.exit(1)
    if "KEY NAMESPACE:" not in text or "CUSIP" not in text:
        print("CONTRACT-BAD no 'KEY NAMESPACE:' line naming the CUSIP")
        sys.exit(1)
    for col in ("date", "close_served", "as_traded_close", "claim", "00162Q866", "AMLP"):
        if col not in text:
            print("CONTRACT-BAD missing " + col)
            sys.exit(1)
    print("CONTRACT-OK " + " ".join(need))
    sys.exit(0)
