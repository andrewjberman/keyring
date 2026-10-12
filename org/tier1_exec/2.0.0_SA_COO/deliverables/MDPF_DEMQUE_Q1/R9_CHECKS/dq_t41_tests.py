"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_rolling_tiers.py, no network). TIER-OK when every named test PASSED; else TIER-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_daily_tier_is_the_stored_names_plus_the_advi_funds_every_trading_day', 'test_rolling_names_are_visited_in_rank_blocks_each_within_five_trading_days', 'test_a_day_never_exceeds_the_cap_and_names_not_yet_landed_are_excluded_and_counted']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_rolling_tiers.py', 'TIER-OK', 'TIER-BAD', TESTS))
