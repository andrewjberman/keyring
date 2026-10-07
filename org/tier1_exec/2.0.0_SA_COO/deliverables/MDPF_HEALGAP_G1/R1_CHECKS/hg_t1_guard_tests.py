"""MDPF_HEALGAP round 1, criterion HG1-t1-AC1: the runner's guard skips a date whose complete-stamp is
LISTED, with GetObject denied as on the real role, and pulls when the stamp is absent (difference control).

Last line: GUARD-TESTS-OK or GUARD-TESTS-BAD <reason>.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import _pytest_named

REQUIRED = [
    "test_guard_skips_on_listed_stamp_with_getobject_denied",
    "test_guard_pulls_when_stamp_absent_control",
]

if __name__ == "__main__":
    sys.exit(_pytest_named.run(REQUIRED, "GUARD-TESTS-OK", "GUARD-TESTS-BAD"))
