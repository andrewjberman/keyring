"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_card_a_slice.py, no network). SLICE-OK when every named test PASSED; else SLICE-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_a_security_carries_its_own_window_and_the_quote_sums_trading_days_inside_it', 'test_the_p1_slice_lists_priced_names_in_rank_order_and_every_window_ends_on_the_need_end_date', 'test_a_p1_name_with_no_trades_or_no_bloomberg_cusip_is_listed_unresolved_and_never_quoted']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_card_a_slice.py', 'SLICE-OK', 'SLICE-BAD', TESTS))
