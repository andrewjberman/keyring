"""MDPF_DEMQUE round 5, DQ-t-18 (OPAL_BBGTML meter; CTO round-4 analysis R2) criterion AC1: named tests in
data/mdpf/scripts/demque/test_demque_bbgtml_meter.py (stub notebook runs, temporary ledger). METER-OK when every named test PASSED;
else METER-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_each_notebook_run_records_one_budget_line', 'test_unreadable_cells_record_null_with_claim_absent', 'test_ledger_day_without_meter_lines_carries_unmetered_line']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_bbgtml_meter.py', 'METER-OK', 'METER-BAD', TESTS))
