#!/usr/bin/env python3
"""A2 BACKFILL_CAP 50 to 62: the plan's DEFAULT cap, read through the real function, is 62.

Run from the worktree root. Loads integrations/bloomberg/pipeline/etf_daily_pull.py the way its own test does (spec_from_file_location),
then asks history_backfill_plan for 70 securities with nothing stored and NO cap argument. Expect 62 planned, 8 capped, needing 70,
in sorted-ticker order. Prints A2-CAP-OK planned=62 capped=8; otherwise A2-CAP-BAD <what was read>. Offline: no network, no S3.
"""
import importlib.util
import os
import sys
from datetime import date

PATH = os.path.join("integrations", "bloomberg", "pipeline", "etf_daily_pull.py")


def main():
    spec = importlib.util.spec_from_file_location("etf_daily_pull_a2_check", PATH)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    tickers = ["T%03d" % i for i in range(70)]
    plan = m.history_backfill_plan(["%s US Equity" % t for t in tickers], {}, date(2026, 10, 20))
    planned, capped, need = list(plan["backfill"]), plan["capped"], plan["needing_count"]
    if m.BACKFILL_CAP == 62 and len(planned) == 62 and len(capped) == 8 and need == 70 and planned == tickers[:62] and capped == tickers[62:]:
        print("A2-CAP-OK planned=62 capped=8")
        return 0
    print("A2-CAP-BAD BACKFILL_CAP=%r planned=%d capped=%d needing=%d" % (m.BACKFILL_CAP, len(planned), len(capped), need))
    return 1


if __name__ == "__main__":
    sys.exit(main())
