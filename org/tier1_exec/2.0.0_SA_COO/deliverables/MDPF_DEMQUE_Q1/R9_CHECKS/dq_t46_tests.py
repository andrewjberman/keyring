"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_p1_coverage.py, no network). COVER-OK when every named test PASSED; else COVER-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_a_held_day_with_units_and_market_value_prices_exactly_at_value_over_units', 'test_the_three_classes_partition_the_priced_names_and_the_residual_counts_only_uncovered_days', 'test_the_coverage_output_carries_cusips_and_counts_and_never_an_account_key']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_p1_coverage.py', 'COVER-OK', 'COVER-BAD', TESTS))
