"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_lag_report.py, no network). LAG-OK when every named test PASSED; else LAG-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_the_enrolment_declares_the_basis_and_a_cycle_per_tier_and_a_disagreeing_rolling_cycle_is_refused', 'test_the_lag_report_counts_every_indexed_name_in_one_tier_with_its_measured_lag', 'test_a_name_older_than_its_tier_cycle_is_listed_over_and_never_counted_within']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_lag_report.py', 'LAG-OK', 'LAG-BAD', TESTS))
