"""MDPF_DEMQUE round 9, DQ-t-65 criterion AC1 (named tests in test_demque_inactive_symbols.py, stub frames, no network). SYMBOLS-OK when every named test PASSED; else SYMBOLS-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_a_transaction_symbol_is_the_modal_non_blank_symbol_per_cusip_and_a_tie_takes_the_first_ascending",
    "test_the_symbol_precedence_is_the_index_then_the_request_files_then_the_transactions",
    "test_the_census_counts_the_names_whose_symbol_came_only_from_the_transactions",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_inactive_symbols.py", "SYMBOLS-OK", "SYMBOLS-BAD", TESTS))
