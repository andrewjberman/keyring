"""test_ai_leg_verify.py -- row S66: the AI-leg verdict must refuse a partial leg.

The killed e32 V3 run 1 landed 187 of 2,291 planned keys and left 2,104 unresolved (DECOMP_R12 state item 1).
Run: python -m pytest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/test_ai_leg_verify.py -q
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ai_leg_verify import grade, is_final_refusal, read_unresolved  # noqa: E402

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


def test_transport_refusals_are_not_final():
    for why in ("no class (refused: KIMI_TIMEOUT)", "no class (refused: KIMI_HTTP_429)",
                "no class (refused: KIMI_ERROR: [Errno 104] Connection reset)", "no class (refused: KIMI_MALFORMED)",
                "no class (refused: KIMI_LENGTH_STARVED)", None, ""):
        assert is_final_refusal(why) is False, why


def test_model_stated_refusals_are_final():
    for why in ("no class (a private placement with no public listing)", "class 'other' is not one of the six",
                "no sub-class for equity", "sub-class 'Micro Cap' is not carried by the table for equity",
                "no class (refused: KIMI_VOCAB_VIOLATION: asset_class='real_estate' reason='REIT')"):
        assert is_final_refusal(why) is True, why


def test_last_reason_per_key_wins(tmp_path):
    a = tmp_path / "run_a.log"
    b = tmp_path / "run_b.log"
    a.write_text("AI chunk 0-25: keys_sent=25\nUNRESOLVED ABC: no class (refused: KIMI_TIMEOUT)\n", encoding="utf-8")
    b.write_text("UNRESOLVED ABC: no sub-class for equity\nUNRESOLVED XYZ: no class (refused: KIMI_HTTP_429)\n",
                 encoding="utf-8")
    got = read_unresolved([a, b])
    assert got == {"ABC": "no sub-class for equity", "XYZ": "no class (refused: KIMI_HTTP_429)"}
    assert is_final_refusal(got["ABC"]) and not is_final_refusal(got["XYZ"])
