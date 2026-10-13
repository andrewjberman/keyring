"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_porting_verdict.py, a local store directory, no network). VERDICT-OK when every named test PASSED; else VERDICT-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_the_index_gains_a_porting_verdict_column_defaulting_to_unverified_for_every_name_when_no_verdicts_file_exists",
    "test_a_verdicts_file_sets_pass_fail_untestable_per_name_and_a_name_without_a_row_or_with_no_bloomberg_stays_unverified",
    "test_a_malformed_or_unreadable_verdicts_file_writes_unverified_for_every_name_and_never_pass",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_porting_verdict.py", "VERDICT-OK", "VERDICT-BAD", TESTS))
