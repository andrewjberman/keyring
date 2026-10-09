"""MDPF_DEMQUE round 1, DQ-t-3 (FWD-1 hop 4) criterion AC1: the request, the quote in cells, the ranked daily draw and
the ledger row, by named tests in `test_demque_queue.py` (run from data/mdpf/scripts/demque; the pull is stubbed).
QUEUE-OK when every named test PASSED; else QUEUE-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_file import run  # noqa: E402

TESTS = [
    "test_quote_counts_cells_as_rows_times_fields",
    "test_quote_finish_date_from_daily_cap_and_queue_ahead",
    "test_draw_takes_lower_tier_number_first",
    "test_draw_writes_one_ledger_row_per_request_with_quote_beside_actual",
    "test_failure_is_a_ledger_row_with_zero_cells",
]

if __name__ == "__main__":
    sys.exit(run("test_demque_queue.py", "QUEUE-OK", "QUEUE-BAD", TESTS))
