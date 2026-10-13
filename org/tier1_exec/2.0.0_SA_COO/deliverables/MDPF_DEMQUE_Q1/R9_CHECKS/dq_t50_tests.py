"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_b1_request.py, no network). B1-OK when every named test PASSED; else B1-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_option_c_dates_are_flow_dates_and_month_ends_before_2026_04_22_and_every_trading_day_after_with_the_2012_floor', 'test_a_security_with_a_total_return_override_prices_two_fields_and_a_dates_entry_prices_its_trading_days_only', 'test_a_fixed_one_dollar_money_market_fund_is_skipped_with_its_reason_and_an_unread_type_is_pulled']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_b1_request.py', 'B1-OK', 'B1-BAD', TESTS))
