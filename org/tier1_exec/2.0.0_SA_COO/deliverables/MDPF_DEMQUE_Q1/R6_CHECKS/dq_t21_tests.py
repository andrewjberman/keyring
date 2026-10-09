"""MDPF_DEMQUE round 6, DQ-t-21 (the total-return column with both D1-S3 guards; CTO round-5 analysis R2) criterion AC1: named tests
in data/mdpf/scripts/demque/test_demque_tr_column.py (synthetic frames, no network). TRC-OK when every named test PASSED; else TRC-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_tr_is_close_plus_exdate_cash_over_prior_close_split_safe', 'test_missing_cash_flag_on_non_exdate_gap_against_bloomberg', 'test_money_market_tr_from_bloomberg_never_yahoo_zero', 'test_existing_price_columns_unchanged']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_tr_column.py', 'TRC-OK', 'TRC-BAD', TESTS))
