"""MDPF_HEALGAP round 2, HG-t-3 (FWD-2) criterion AC1: the runner's per-feed run result, by named tests in
`test_healgap_result.py` (run from the runner folder). RESULT-OK when every named test PASSED; else RESULT-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_file import run  # noqa: E402

TESTS = [
    "test_result_all_three_arrived_is_complete",
    "test_result_missing_feed_is_partial_and_raises_without_stamp",
    "test_induce_drop_feed_skips_exactly_that_feed",
    "test_reattempt_records_healed_at_for_the_filled_feed",
    "test_result_readable_without_logs",
]

if __name__ == "__main__":
    sys.exit(run("test_healgap_result.py", "RESULT-OK", "RESULT-BAD", TESTS))
