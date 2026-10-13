"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_porting_test.py, no network). PORT-OK when every named test PASSED; else PORT-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_the_five_intervals_are_a_deterministic_sha256_draw_inside_the_held_window_with_one_month_quarter_and_year_lengths', 'test_a_security_passes_only_when_every_interval_return_is_within_ten_basis_points_and_one_miss_fails_it', 'test_the_request_carries_at_most_ten_single_day_cells_a_security_on_trading_days_inside_the_window']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_porting_test.py', 'PORT-OK', 'PORT-BAD', TESTS))
