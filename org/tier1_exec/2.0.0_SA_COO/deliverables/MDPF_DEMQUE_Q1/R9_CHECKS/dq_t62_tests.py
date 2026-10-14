"""MDPF_DEMQUE round 9, DQ-t-62 criterion AC1 (named tests in test_demque_symbol_forms.py, stub fetches, no network). FORM-OK when every named test PASSED; else FORM-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_a_class_share_symbol_without_a_dash_is_pulled_in_its_yahoo_dash_form_and_keyed_as_given",
    "test_a_symbol_with_no_override_is_pulled_unchanged_in_every_fetch_path",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_symbol_forms.py", "FORM-OK", "FORM-BAD", TESTS))
