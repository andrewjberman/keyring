"""MDPF_STRATID round 1, ST-t-2 criterion AC1: the registry declares the SMA basis per (member, firm) at Global with a per-firm population default. T2-OK when every named test PASSED; else T2-BAD.
Run from the repo (worktree) root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_named import run  # noqa: E402

TESTS = ['test_pfde_cottonwood_is_additive_at_global', 'test_firm_population_inside_defaults_carve_out', 'test_undeclared_firm_population_is_not_counted', 'test_member_firm_row_overrides_firm_default', 'test_import_refuses_an_invalid_firm_row', 'test_global_scope_basis_of_pfde_is_additive']

if __name__ == "__main__":
    sys.exit(run("data/mdpf/tests/stratid/test_stratid_basis.py", "T2-OK", "T2-BAD", TESTS))
