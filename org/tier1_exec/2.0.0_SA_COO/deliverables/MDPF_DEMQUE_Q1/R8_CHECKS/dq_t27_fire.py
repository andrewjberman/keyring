"""MDPF_DEMQUE round 8, DQ-t-27 criterion AC3 (the first scheduled fire; date-gated): read the real actuals ledger for the TR request.
The first row of a non-trading day AFTER 2026-10-10 (t24's day) must be DRAWN by the standing drawer with cells_drawn equal to
that day's share: min(5,858 ceiling, 15,720 quoted minus the cells drawn on earlier days). `quote_vs_actual.py` then reads the request
ON_TIME against its re-frozen finish when the cells are all drawn, OPEN while they are not. FIRE-OK; else FIRE-BAD <why>.
At the base (no fire yet): `FIRE-BAD no scheduled fire row after 2026-10-10`.
"""
from __future__ import annotations

import datetime as dt
import json
import os
import sys

sys.path.insert(0, ".")
LEDGER = os.path.join("org", "missions", "D8", "MDPF", "MDPF_DEMQUE", "ledger", "BBG_ACTUALS.jsonl")
RID = "DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS"
CEILING, QUOTED, T24_DAY = 5858, 15720, "2026-10-10"


def main() -> int:
    from lib.trading_calendar import is_trading_day
    rows = [json.loads(ln) for ln in open(LEDGER, encoding="utf-8").read().splitlines() if ln.strip()]
    mine = [r for r in rows if r.get("job") == RID and r.get("channel") == "history"]
    fires = sorted((r for r in mine if r["date"] > T24_DAY and not is_trading_day(dt.date.fromisoformat(r["date"]))),
                   key=lambda r: r["date"])
    if not fires:
        print("FIRE-BAD no scheduled fire row after %s" % T24_DAY)
        return 1
    first = fires[0]
    before = sum(int(r.get("cells_drawn") or 0) for r in mine if r["date"] < first["date"])
    share = min(CEILING, QUOTED - before)
    print("first fire: date=%s cells_drawn=%s outcome=%s drawer=%s drawn_before=%d day_share=%d" % (
        first["date"], first.get("cells_drawn"), first.get("outcome"), first.get("drawer"), before, share))
    if first.get("outcome") != "DRAWN" or first.get("cells_drawn") != share:
        print("FIRE-BAD outcome/cells differ from the day share")
        return 1
    print("FIRE-OK the first scheduled non-trading-day fire drew its day share")
    return 0


if __name__ == "__main__":
    sys.exit(main())
