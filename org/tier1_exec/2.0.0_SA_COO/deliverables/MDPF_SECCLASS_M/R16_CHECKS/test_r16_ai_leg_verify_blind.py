"""MDPF_SECCLASS round 16 cell SC-e-80 check (row D1-S15): ai_leg_verify refuses when keys are absent but the logs it was given yield
zero reason lines for them -- the shape a timestamp-prefixed log produced on e49 (387 reason lines read as 0, no error).

Pure-function arms only (no AWS). Run: python -m pytest -q org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R16_CHECKS/test_r16_ai_leg_verify_blind.py
"""
import importlib.util
from pathlib import Path

HERE = Path(__file__).resolve().parent
MOD = HERE.parent / "R12_CHECKS" / "ai_leg_verify.py"


def _load():
    spec = importlib.util.spec_from_file_location("ai_leg_verify", MOD)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def test_prefixed_log_with_absent_keys_is_refused(tmp_path):
    m = _load()
    log = tmp_path / "run.log"
    log.write_text("[+   154.0s] UNRESOLVED KEY1: no class (refused: x)\n[+   155.0s] UNRESOLVED KEY2: class y\n", encoding="utf-8")
    reasons = m.read_unresolved([str(log)])
    problem = m.blind_log_refusal(["KEY1", "KEY2"], reasons, [str(log)])
    assert problem, "absent keys + logs given + zero reason lines for them must refuse"


def test_readable_log_is_not_refused(tmp_path):
    m = _load()
    log = tmp_path / "run.stripped.log"
    log.write_text("UNRESOLVED KEY1: no class (refused: x)\n", encoding="utf-8")
    assert m.blind_log_refusal(["KEY1"], m.read_unresolved([str(log)]), [str(log)]) is None


def test_no_logs_given_is_not_this_refusal():
    m = _load()
    assert m.blind_log_refusal(["KEY1"], {}, []) is None
