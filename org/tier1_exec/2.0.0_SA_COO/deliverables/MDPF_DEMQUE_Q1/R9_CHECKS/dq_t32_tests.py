"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_lock_cause.py, no network). LC-OK when every named test PASSED; else LC-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_agreement_is_computed_against_the_old_file_and_the_new_draw', 'test_disagreeing_dates_are_listed_with_exdiv_split_and_trade_type', 'test_hold_record_sets_claim_held_with_the_reason_and_keeps_every_other_key']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_lock_cause.py', 'LC-OK', 'LC-BAD', TESTS))
