"""MDPF_DEMQUE round 8, DQ-t-27 (CTO round-7 analysis R2, drawer half) criterion AC1: named tests in test_demque_standing_drawer.py (stub client, no network). DRW-OK when every named test PASSED; else DRW-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")

TESTS = ['test_drawer_schedule_is_one_fire_per_non_trading_day_for_the_horizon', 'test_drawer_draws_min_of_allowance_and_remaining_in_rank_order', 'test_drawer_on_a_trading_day_draws_nothing']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_standing_drawer.py', 'DRW-OK', 'DRW-BAD', TESTS))
