"""MDPF_HEALGAP round 1, criterion HG1-t1-AC2: an event carrying {"induce": "auth-lapse"} fails the pull the
way a lapsed login does (an HTTP 401 RuntimeError) before the session secret is read, and a date already
complete still skips (difference control: the guard runs first).

Last line: INDUCE-TESTS-OK or INDUCE-TESTS-BAD <reason>.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _pytest_named

REQUIRED = [
    "test_induced_auth_lapse_raises_before_session_read",
    "test_induced_auth_lapse_skipped_on_complete_day",
]

if __name__ == "__main__":
    sys.exit(_pytest_named.run(REQUIRED, "INDUCE-TESTS-OK", "INDUCE-TESTS-BAD"))
