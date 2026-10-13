"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_incremental.py, no network). INC-OK when every named test PASSED; else INC-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_the_window_is_the_last_five_trading_days_after_the_stored_max_and_never_wider_than_the_gap', 'test_a_gap_wider_than_five_days_or_a_new_split_in_the_window_is_a_targeted_refill_never_a_wider_standing_window', 'test_appending_the_incremental_rows_equals_the_full_repull_on_a_no_split_day', 'test_a_gained_split_triggers_the_full_repull_and_the_result_equals_the_full_path']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_incremental.py', 'INC-OK', 'INC-BAD', TESTS))
