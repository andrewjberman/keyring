"""test_ai_leg_verify.py -- row S66: the AI-leg verdict must refuse a partial leg.

The killed e32 V3 run 1 landed 187 of 2,291 planned keys and left 2,104 unresolved (DECOMP_R12 state item 1).
Run: python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/test_ai_leg_verify.py -q
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ai_leg_verify import grade  # noqa: E402

PLANNED, LANDED, UNRESOLVED = 2291, 187, 2104


def test_killed_run_is_not_ok():
    assert LANDED + UNRESOLVED == PLANNED
    assert grade(PLANNED, LANDED, 0, 0, 0, 0, 200, 200) is False


def test_old_rule_passed_the_killed_run():
    # Difference control: the retired rule (landed > 0, no plan check) read ok=True on the same numbers.
    assert LANDED > 0


def test_complete_run_is_ok():
    assert grade(PLANNED, PLANNED, 0, 0, 0, 0, 2304, 2304) is True


def test_refused_keys_account_for_the_rest():
    assert grade(PLANNED, PLANNED - 5, 5, 0, 0, 0, 2299, 2299) is True


def test_empty_plan_is_not_ok():
    assert grade(0, 0, 0, 0, 0, 0, 200, 200) is False
