"""MDPF_DEMQUE round 1, DQ-t-1 (FWD-1 hop 2) criterion AC1: the lock rule, by named tests in `test_demque_lock.py`
(run from data/mdpf/scripts/demque). LOCK-OK when every named test PASSED; else LOCK-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_file import run  # noqa: E402

TESTS = [
    "test_agreeing_series_locks_measured",
    "test_recycled_ticker_rejected_on_early_third",
    "test_too_few_agreeing_dates_rejected",
    "test_mutual_fund_uses_half_percent_band",
    "test_no_trade_prices_locks_with_claim_held",
    "test_trade_price_is_abs_amount_over_quantity_on_trade_rows_only",
]

if __name__ == "__main__":
    sys.exit(run("test_demque_lock.py", "LOCK-OK", "LOCK-BAD", TESTS))
