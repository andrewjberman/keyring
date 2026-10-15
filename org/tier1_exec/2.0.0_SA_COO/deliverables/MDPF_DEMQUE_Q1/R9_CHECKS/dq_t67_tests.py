"""MDPF_DEMQUE round 9, DQ-t-67 criterion AC1 (named tests in test_demque_inactive_request.py, stub frames, no network). REQUEST-OK when every named test PASSED; else REQUEST-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_the_backfill_requests_chunk_the_symbolled_names_in_rank_order_and_every_name_appears_once",
    "test_every_request_validates_and_carries_the_floor_start_the_frontier_end_and_the_client_need_class",
    "test_a_name_without_a_symbol_is_left_out_and_counted",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_inactive_request.py", "REQUEST-OK", "REQUEST-BAD", TESTS))
