"""MDPF_DEMQUE round 7, DQ-t-24 (the first non-trading-day history backfill at site Z; CTO round-6 analysis R1) criterion AC1: named
tests in data/mdpf/scripts/demque/test_demque_bbg_backfill.py (a stub Bloomberg client, no network). BKF-OK when every named test
PASSED; else BKF-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_backfill_stops_at_the_days_allowance', 'test_backfill_stops_on_a_vendor_limit_warning', 'test_trading_day_backfill_draws_nothing']

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_bbg_backfill.py", "BKF-OK", "BKF-BAD", TESTS))
