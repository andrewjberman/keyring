"""MDPF_DEMQUE round 8, DQ-t-25 (CTO round-7 analysis R1 + D1-S5) criterion AC1: named tests in test_demque_tier_quote.py (no network). TQ-OK when every named test PASSED; else TQ-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")

TESTS = ['test_tier2_history_with_both_claims_measured_still_walks_non_trading_days', 'test_tier1_history_reads_positive_allowance_today_on_a_trading_day_and_finishes_that_day', 'test_tier2_history_ceiling_not_measured_has_null_finish_with_reason_and_zero_on_trading_day']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_tier_quote.py', 'TQ-OK', 'TQ-BAD', TESTS))
