"""MDPF_DEMQUE round 9, DQ-t-71 criterion AC1 (named tests in test_demque_pacer_cap.py, no network). CAP-OK when every named test PASSED; else CAP-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_the_pacer_stops_a_draw_at_six_hundred_requests_and_not_before",
    "test_the_standing_extension_request_cap_is_the_daily_cap_less_the_tier_two_reserve",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_pacer_cap.py", "CAP-OK", "CAP-BAD", TESTS))
