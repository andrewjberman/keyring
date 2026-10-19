"""MDPF_DEMQUE DQ-t-79 criterion AC1 (named tests in test_demque_health_probe.py, no network). HEALTH-OK when every named test PASSED; else HEALTH-BAD.
Run from the worktree root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_a_sixth_empty_window_runs_the_health_probe_and_a_priced_answer_keeps_drawing",
    "test_an_empty_or_failed_health_probe_stops_the_fire_as_outage",
    "test_a_fourth_trigger_stops_the_fire_as_sparse_stop_and_names_the_windows",
    "test_the_health_probe_counts_against_the_fire_and_the_receipt_lists_it",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_health_probe.py", "HEALTH-OK", "HEALTH-BAD", TESTS))
