"""MDPF_DEMQUE round 2, DQ-t-6 (FWD-1 hops 5-6, C-PRICES, C-ONCE) criterion AC1: the per-CUSIP price store and its index, by
named tests in data/mdpf/scripts/demque/test_demque_store.py (local directory, no S3). STORE-OK when every named test PASSED;
else STORE-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_dir import run  # noqa: E402

TESTS = [
    "test_only_the_locked_range_is_written",
    "test_rejected_lock_writes_nothing",
    "test_served_and_as_traded_kept_apart_with_actions",
    "test_index_row_per_cusip_carries_claim_and_range",
    "test_second_write_of_unchanged_history_is_a_noop",
]

if __name__ == "__main__":
    sys.exit(run(os.path.join("data", "mdpf", "scripts", "demque"), "test_demque_store.py", "STORE-OK", "STORE-BAD", TESTS))
