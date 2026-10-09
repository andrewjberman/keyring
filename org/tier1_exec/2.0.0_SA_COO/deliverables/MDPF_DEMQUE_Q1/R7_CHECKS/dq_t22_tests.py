"""MDPF_DEMQUE round 7, DQ-t-22 (history backfill on non-trading days; CTO round-6 analysis R1) criterion AC1: named tests in
data/mdpf/scripts/demque/test_demque_nontrading.py (no network). NTD-OK when every named test PASSED; else NTD-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_history_backfill_quoted_on_non_trading_days_at_ceiling', 'test_trading_day_backfill_allowance_is_zero', 'test_history_ceiling_claim_measured_from_ledger']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_nontrading.py', 'NTD-OK', 'NTD-BAD', TESTS))
