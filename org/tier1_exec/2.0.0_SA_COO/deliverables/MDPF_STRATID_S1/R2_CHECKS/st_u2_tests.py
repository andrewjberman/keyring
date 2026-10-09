"""MDPF_STRATID round 2, ST-u-2 criterion AC1: for every SMA strategy amount at Global the served record states whether it is
also inside a Model figure, and an account set up to sit in both is held out once and named. U2-OK when every named test PASSED;
else U2-BAD. Run from the repo (worktree) root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", "R1_CHECKS"))
from _pytest_named import run  # noqa: E402

TESTS = ['test_additive_entry_states_inside_model_value_per_date', 'test_tree_member_names_held_out_amounts',
         'test_carve_out_member_states_it_is_not_inside_a_model', 'test_statement_moves_no_figure']

if __name__ == "__main__":
    sys.exit(run("data/mdpf/tests/stratid/test_stratid_round2_inside_model.py", "U2-OK", "U2-BAD", TESTS))
