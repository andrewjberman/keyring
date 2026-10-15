"""MDPF_DEMQUE round 9, DQ-t-66 criterion AC1 (named tests in test_demque_yahoo_gate.py, stub frames, no network). GATE-OK when every named test PASSED; else GATE-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_the_yahoo_gate_excludes_exactly_the_active_set_names_and_no_p2_or_p3_name",
    "test_a_landed_name_in_no_tier_joins_the_rolling_cohort_and_the_daily_tier_keeps_the_stored_at_enrolment_and_extras",
    "test_the_day_request_stays_under_the_cap_with_a_thousand_landed_inactive_names",
    "test_the_daily_draw_skips_an_active_name_of_a_client_request_and_draws_a_p2_name",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_yahoo_gate.py", "GATE-OK", "GATE-BAD", TESTS))
