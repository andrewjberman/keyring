"""MDPF_DEMQUE DQ-t-76 criterion AC1 (named tests in test_demque_probe_empty.py, no network). PROBE-OK when every named test PASSED; else PROBE-BAD.
Run from the worktree root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_an_empty_probe_security_is_skipped_and_the_next_cusip_security_verifies_the_form",
    "test_three_empty_probes_leave_the_form_unverified_and_refuse_the_request",
    "test_a_probe_that_names_the_wrong_security_or_errors_still_leaves_the_form_unverified",
    "test_the_history_probe_asks_the_previous_trading_day_not_the_first_undrawn_day",
    "test_the_skipped_probe_security_is_listed_in_the_receipt_and_cooled_for_seven_days",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_probe_empty.py", "PROBE-OK", "PROBE-BAD", TESTS))
