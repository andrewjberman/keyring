"""MDPF_DEMQUE round 3, DQ-t-9 (C-METER Bloomberg; FWD-3, FWD-4) criterion AC1: the Bloomberg quote and the actuals record, by named
tests in data/mdpf/scripts/demque/test_demque_bbg.py (no network, no Terminal). The round-1/2 queue tests must still pass (regression arm,
test_demque_queue.py). BBGQ-OK when every named test PASSED in both files; else BBGQ-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
NEW = [
    "test_reference_request_quotes_securities_times_fields",
    "test_history_request_quotes_weekdays_times_fields_per_security",
    "test_model_block_quote_reads_the_producers_declared_fields",
    "test_allowance_unknown_gives_no_finish_date_and_names_the_gap",
    "test_allowance_known_gives_finish_date_above_the_reserve",
    "test_actual_recorded_beside_quote_and_unquoted_draw_is_labelled",
]
OLD = [
    "test_quote_counts_cells_as_rows_times_fields",
    "test_draw_takes_lower_tier_number_first",
    "test_dividends_and_splits_fields_accepted_and_counted",
]

if __name__ == "__main__":
    a = run(HOME, "test_demque_bbg.py", "BBGQ-NEW-OK", "BBGQ-BAD", NEW)
    b = run(HOME, "test_demque_queue.py", "BBGQ-REGRESSION-OK", "BBGQ-BAD", OLD) if a == 0 else 1
    if a == 0 and b == 0:
        print("BBGQ-OK")
        sys.exit(0)
    print("BBGQ-BAD")
    sys.exit(1)
