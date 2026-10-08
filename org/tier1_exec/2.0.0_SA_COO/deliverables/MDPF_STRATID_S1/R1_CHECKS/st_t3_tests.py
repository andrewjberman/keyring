"""MDPF_STRATID round 1, ST-t-3 criterion AC1: the Global fold adds additive Cottonwood sleeves once, withholds overlap and unmeasured overlap by name. T3-OK when every named test PASSED; else T3-BAD.
Run from the repo (worktree) root."""
from __future__ import annotations

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from _pytest_named import run  # noqa: E402

TESTS = ['test_additive_sleeve_added_to_global_total_and_by_model', 'test_overlap_dollars_withheld_and_named', 'test_unmeasured_overlap_withholds_whole_member', 'test_undeclared_firm_member_not_counted', 'test_carve_out_member_never_added', 'test_category_tree_and_aum_metrics_count_it_once', 'test_cottonwood_and_49financial_views_unchanged']

if __name__ == "__main__":
    sys.exit(run("data/mdpf/tests/stratid/test_stratid_global_fold.py", "T3-OK", "T3-BAD", TESTS))
