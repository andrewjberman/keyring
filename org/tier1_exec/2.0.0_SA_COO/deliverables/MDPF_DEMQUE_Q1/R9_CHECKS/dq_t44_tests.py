"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_need_class.py, no network). CLASS-OK when every named test PASSED; else CLASS-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_a_bloomberg_request_without_a_declared_need_class_or_window_start_is_refused', 'test_a_window_before_2012_or_a_non_client_start_beyond_365_days_of_its_need_date_is_refused_never_trimmed', 'test_the_card_a_slice_window_ends_at_the_frontier_for_a_held_name_and_at_the_last_trade_for_a_sold_one', 'test_a_request_whose_start_moves_later_draws_only_the_undrawn_in_window_rows_by_identity']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_need_class.py', 'CLASS-OK', 'CLASS-BAD', TESTS))
