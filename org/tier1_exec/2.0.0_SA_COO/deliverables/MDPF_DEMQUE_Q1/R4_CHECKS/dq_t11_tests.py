"""MDPF_DEMQUE round 4, DQ-t-11 (lock agreement floor, CTO msgs 1519 item 2 and 1522) criterion AC1: by named tests in data/mdpf/scripts/demque/test_demque_lock.py (no network, no Bloomberg, no
S3 write). The round-1 names that still describe the rule must pass (regression arm). FLOOR-OK when every named test PASSED; else FLOOR-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_agreeing_series_locks_measured', 'test_recycled_ticker_rejected_on_early_third', 'test_mutual_fund_uses_half_percent_band', 'test_no_trade_prices_locks_with_claim_held', 'test_trade_price_is_abs_amount_over_quantity_on_trade_rows_only', 'test_below_ninety_percent_agreement_is_rejected_low_trade_agreement', 'test_ninety_percent_floor_counts_within_each_types_band', 'test_exactly_ninety_percent_locks']

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_lock.py", "FLOOR-OK", "FLOOR-BAD", TESTS))
