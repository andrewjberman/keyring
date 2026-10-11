"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_lock_partition.py, no network). LP-OK when every named test PASSED; else LP-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = ['test_latest_partition_is_the_greatest_date_partition_holding_parquet', 'test_trades_through_is_the_max_trade_date_of_the_loaded_rows', 'test_claim_is_held_when_the_window_runs_past_the_trades']

if __name__ == "__main__":
    sys.exit(run(HOME, 'test_demque_lock_partition.py', 'LP-OK', 'LP-BAD', TESTS))
