"""MDPF_DEMQUE round 6, DQ-t-20 (history reserve from the ledger; CTO round-5 analysis R1) criterion AC1: named tests in
data/mdpf/scripts/demque/test_demque_reserve_ledger.py (stub ledger rows, no S3). RSV-OK when every named test PASSED; else RSV-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_history_reserve_is_measured_daily_draw_plus_margin', 'test_reserve_carries_claim_held_and_ledger_basis', 'test_quote_names_allowance_not_positive_when_reserve_meets_ceiling']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_reserve_ledger.py', 'RSV-OK', 'RSV-BAD', TESTS))
