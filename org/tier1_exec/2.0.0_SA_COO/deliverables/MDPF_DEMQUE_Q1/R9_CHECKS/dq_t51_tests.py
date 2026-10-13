"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_porting_intervals.py, no network). INT-OK when every named test PASSED; else INT-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_a_fixed_length_that_does_not_fit_is_replaced_by_a_sha256_drawn_length_that_fits_so_every_testable_security_has_five_intervals', 'test_a_window_under_ten_trading_days_is_untestable_with_a_reason_and_never_a_fail', 'test_every_interval_is_at_least_five_trading_days_and_overlap_is_allowed']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_porting_intervals.py', 'INT-OK', 'INT-BAD', TESTS))
