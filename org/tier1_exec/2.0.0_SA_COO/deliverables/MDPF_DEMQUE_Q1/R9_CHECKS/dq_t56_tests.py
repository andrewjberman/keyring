"""MDPF_DEMQUE round 9 criterion AC1 (named tests in test_demque_drawer_cusip_entries.py, no network). DRAWER-OK when every named test PASSED; else DRAWER-BAD.
"""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R2_CHECKS"))
from _pytest_dir import run  # noqa: E402

HOME = os.path.join("data", "mdpf", "scripts", "demque")
TESTS = [
    "test_a_cusip_entry_resolves_to_a_bloomberg_identifier_and_the_first_draw_of_an_unverified_form_is_a_one_row_probe",
    "test_a_dates_entry_draws_only_its_undrawn_trading_days_by_identity_one_request_per_consecutive_run",
    "test_a_per_entry_fields_override_draws_that_entrys_fields_and_a_reference_request_draws_securities_by_fields",
    "test_the_drawer_skips_a_client_request_security_the_priority_gate_excludes_and_fails_closed",
]

if __name__ == "__main__":
    sys.exit(run(HOME, "test_demque_drawer_cusip_entries.py", "DRAWER-OK", "DRAWER-BAD", TESTS))
