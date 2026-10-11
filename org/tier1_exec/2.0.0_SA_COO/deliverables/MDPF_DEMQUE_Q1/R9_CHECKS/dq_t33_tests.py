"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_quote_remaining.py, no network). QR-OK when every named test PASSED; else QR-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_requote_of_a_partly_drawn_request_prices_the_remaining_cells', 'test_history_cells_are_priced_on_trading_days', 'test_complete_row_closes_the_request_and_sets_the_drawn_date', 'test_refreeze_chains_a_second_superseded_quote']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_quote_remaining.py', 'QR-OK', 'QR-BAD', TESTS))
