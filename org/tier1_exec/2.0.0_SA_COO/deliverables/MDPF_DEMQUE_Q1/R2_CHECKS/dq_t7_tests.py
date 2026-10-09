"""MDPF_DEMQUE round 2, DQ-t-7 (FWD-2, FWD-4; enrichment @5a392db104) criterion AC1: the queue's enrichment, by named tests in
data/mdpf/scripts/demque/test_demque_queue.py (stubbed fetch, no network, no S3). The round-1 names must still pass (regression
arm). QUEUE2-OK when every named test PASSED; else QUEUE2-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_dir import run  # noqa: E402

TESTS = [
    # round 1, unchanged (regression arm)
    "test_quote_counts_cells_as_rows_times_fields",
    "test_quote_finish_date_from_daily_cap_and_queue_ahead",
    "test_draw_takes_lower_tier_number_first",
    "test_draw_writes_one_ledger_row_per_request_with_quote_beside_actual",
    "test_failure_is_a_ledger_row_with_zero_cells",
    # round 2
    "test_dividends_and_splits_fields_accepted_and_counted",
    "test_draw_hands_each_ok_result_to_the_callback",
    "test_ledger_upload_targets_builder_address_and_is_dry_by_default",
]

if __name__ == "__main__":
    sys.exit(run(os.path.join("data", "mdpf", "scripts", "demque"), "test_demque_queue.py", "QUEUE2-OK", "QUEUE2-BAD", TESTS))
