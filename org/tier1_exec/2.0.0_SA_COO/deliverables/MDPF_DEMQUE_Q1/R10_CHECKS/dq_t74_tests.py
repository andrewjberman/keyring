"""MDPF_DEMQUE DQ-t-74 criterion AC1 (named tests in test_demque_outcome_per_request.py, no network). OUT-OK when every named test PASSED; else OUT-BAD.
Run from the worktree root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_a_request_drawn_complete_before_a_later_requests_stop_is_recorded_complete",
    "test_the_request_that_stopped_the_run_is_recorded_stopped_even_with_cells_drawn",
    "test_a_run_that_stops_still_reports_the_run_as_stopped_and_names_the_reason",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_outcome_per_request.py", "OUT-OK", "OUT-BAD", TESTS))
