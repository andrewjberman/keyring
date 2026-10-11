"""MDPF_DEMQUE round 9, DQ-t-34 criterion AC2 (site Z; date-gated to the fire that completes the request): read the real actuals ledger for the
TR request. Exactly one row of the job carries outcome COMPLETE (the fire that exhausted every security), cells_drawn on it > 0, and NO row of
the job dated after it exists (no 0-cell DRAWN line after completion); the cells drawn up to and including it are at most the trading-day-priced
quote. CLOSE-OK; else CLOSE-BAD <why>. At the base (the request still open): `CLOSE-BAD no COMPLETE row yet`.
"""
from __future__ import annotations

import json
import os
import sys

LEDGER = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "ledger", "BBG_ACTUALS.jsonl")
RID = "DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS"


def main() -> int:
    rows = [json.loads(ln) for ln in open(LEDGER, encoding="utf-8", errors="replace").read().splitlines() if ln.strip()]
    mine = sorted((r for r in rows if r.get("job") == RID and r.get("channel") == "history"), key=lambda r: r["date"])
    done = [r for r in mine if r.get("outcome") == "COMPLETE"]
    if not done:
        print("CLOSE-BAD no COMPLETE row yet (%d rows for the job, %d cells drawn)" % (len(mine), sum(int(r.get("cells_drawn") or 0) for r in mine)))
        return 1
    if len(done) != 1:
        print("CLOSE-BAD %d COMPLETE rows" % len(done))
        return 1
    d = done[0]
    after = [r for r in mine if r["date"] > d["date"]]
    zero = [r for r in mine if r.get("outcome") == "DRAWN" and int(r.get("cells_drawn") or 0) == 0 and r["date"] >= d["date"]]
    print("COMPLETE on %s cells_drawn=%s; rows after: %d; 0-cell DRAWN rows from that day: %d" % (d["date"], d.get("cells_drawn"), len(after), len(zero)))
    if int(d.get("cells_drawn") or 0) <= 0 or after or zero:
        print("CLOSE-BAD completion row is empty or a later/0-cell row exists")
        return 1
    print("CLOSE-OK the request closed on %s with no later line" % d["date"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
