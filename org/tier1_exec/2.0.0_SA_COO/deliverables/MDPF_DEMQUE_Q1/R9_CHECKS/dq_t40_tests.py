"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_batch_pull.py, stub fetch, no network). BATCH-OK when every named test PASSED; else BATCH-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_incremental_window_starts_the_day_after_each_stored_max', 'test_a_symbol_the_vendor_refuses_is_a_failure_for_that_symbol_alone_never_a_price', 'test_batch_rows_equal_per_symbol_rows_on_a_universe_with_splits_and_dividends_in_the_window']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_batch_pull.py', 'BATCH-OK', 'BATCH-BAD', TESTS))
