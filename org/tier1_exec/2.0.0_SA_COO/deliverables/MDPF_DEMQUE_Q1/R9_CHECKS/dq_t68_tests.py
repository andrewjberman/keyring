"""MDPF_DEMQUE round 9, DQ-t-68 criterion AC1 (named tests in test_demque_use_class.py, a local store directory, no network). USECLASS-OK when every named test PASSED; else USECLASS-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_the_index_gains_a_use_class_column_last_and_a_v2_held_name_reads_not_for_active_while_any_other_name_reads_inactive_use",
    "test_an_unreadable_or_absent_active_set_writes_not_for_active_for_every_name_and_never_inactive_use",
    "test_the_use_class_column_is_independent_of_the_porting_verdict_column",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_use_class.py", "USECLASS-OK", "USECLASS-BAD", TESTS))
