"""MDPF_DEMQUE round 5, DQ-t-17 (ADDENDUM v0.5 total-return comparison; CTO round-4 analysis item 3) criterion AC1: named tests in
data/mdpf/scripts/demque/test_demque_tr_compare.py (synthetic frames, no network). TRM-OK when every named test PASSED; else TRM-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_daily_tr_from_as_traded_close_and_exdate_cash', 'test_split_day_is_not_a_return', 'test_comparison_aligns_on_common_trade_dates_only']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_tr_compare.py', 'TRM-OK', 'TRM-BAD', TESTS))
