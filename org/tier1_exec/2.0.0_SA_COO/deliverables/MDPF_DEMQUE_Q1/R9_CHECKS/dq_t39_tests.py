"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_split_hold.py, no network). SPLIT-OK when every named test PASSED; else SPLIT-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_a_name_that_gains_a_split_row_is_not_written_and_says_why', 'test_a_name_with_no_new_split_row_is_written_as_before', 'test_the_first_write_of_a_name_with_no_prior_file_is_unaffected']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_split_hold.py', 'SPLIT-OK', 'SPLIT-BAD', TESTS))
