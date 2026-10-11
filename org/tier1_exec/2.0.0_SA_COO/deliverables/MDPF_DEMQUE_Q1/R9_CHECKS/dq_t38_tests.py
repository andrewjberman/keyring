"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_lock_through.py, no network). THRU-OK when every named test PASSED; else THRU-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_the_lock_row_states_trades_through_beside_its_claim', 'test_a_name_with_no_trades_states_null_and_keeps_its_claim', 'test_the_row_key_set_is_the_declared_one_and_the_store_writes_it']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_lock_through.py', 'THRU-OK', 'THRU-BAD', TESTS))
