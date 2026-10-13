"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_secclass_sync.py, no network). SYNC-OK when every named test PASSED; else SYNC-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_the_same_security_key_prints_equal_on_the_request_row_the_unresolved_entry_and_the_classification_row', 'test_a_security_already_classified_that_enters_through_a_second_request_gets_no_second_row', 'test_a_key_that_differs_between_the_three_places_is_reported_unequal_never_equal']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_secclass_sync.py', 'SYNC-OK', 'SYNC-BAD', TESTS))
