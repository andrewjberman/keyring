"""MDPF_STRATID round 2, ST-u-1 criterion AC1: Cottonwood is declared OUTSIDE, every Cottonwood sleeve is counted once at Global
or held out by name, and a member carried on two bases at Global (49financial carve-out + Cottonwood additive) validates per firm.
U1-OK when every named test PASSED; else U1-BAD. Run from the repo (worktree) root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R1_CHECKS"))
from _pytest_named import run  # noqa: E402

TESTS = ['test_cottonwood_declared_outside', 'test_fully_overlapped_member_held_out_by_name_not_added',
         'test_two_basis_member_validates_per_firm', 'test_zero_overlap_member_counted_in_its_bucket',
         'test_undeclared_firm_still_not_counted']

if __name__ == "__main__":
    sys.exit(run("data/mdpf/tests/stratid/test_stratid_round2_firm_basis.py", "U1-OK", "U1-BAD", TESTS))
