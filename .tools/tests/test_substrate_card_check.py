"""Controls for .tools/substrate-card-check.py -- the set_by != carded_by rule the v3.1 schema only
describes. Three arms: (1) a REAL committed v3.1 card passes (baseline first -- a battery from a failing
base means nothing); (2) the self-adjudication mutant FIRES; (3) a foreign adjudicator on the same card
PASSES (the rule must not fire on the legal case). Run: python -m pytest .tools/tests/test_substrate_card_check.py -q
"""
from __future__ import annotations

import copy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
TOOL = ROOT / ".tools" / "substrate-card-check.py"
CARD = ROOT / "org/tier2_senior/0.4.0_DS_ClientPlatform~V/deliverables/D11_CARDS/MOTIF_c2c3_materialize_spec.card.json"


def _load():
    spec = importlib.util.spec_from_file_location("scc", TOOL)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)  # type: ignore[union-attr]
    return mod


def _fixture():
    mod = _load()
    schema = json.loads(mod.SCHEMA_PATH.read_text(encoding="utf-8"))
    card = json.loads(CARD.read_text(encoding="utf-8"))
    return mod, schema, card


def test_real_card_is_valid_baseline():
    mod, schema, card = _fixture()
    violations, _ = mod.check_card(card, schema)
    assert violations == [], violations


def test_self_adjudication_fires():
    mod, schema, card = _fixture()
    m = copy.deepcopy(card)
    m["forward_disposition"]["set_by"] = m["carded_by"]
    m["forward_disposition"]["standing"] = m["forward_disposition"].get("standing") or "undecided"
    violations, _ = mod.check_card(m, schema)
    assert any("set_by == carded_by" in v for v in violations), violations


def test_foreign_adjudicator_passes_control():
    mod, schema, card = _fixture()
    m = copy.deepcopy(card)
    m["forward_disposition"]["set_by"] = "3.0.0_SA_CVO~X"
    violations, _ = mod.check_card(m, schema)
    assert not any("set_by == carded_by" in v for v in violations), violations


# RULE 3 controls -- a NULL VALUE under a NON-NULL basis. Same three-arm shape as above and for the same
# reason: baseline FIRST, then the mutant must FIRE, then the LEGAL pairing must PASS. The legal arm is the
# load-bearing one here -- `unmeasured` beside basis `absent` is CORRECT and is a certified pairing in the
# estate (code_heat_snap), so an arm that fired on it would manufacture defects in accepted work.
def _basis_fixture():
    """A card carrying a basis map, with the (section, key) this arm needs. Built from the real card."""
    mod, schema, card = _fixture()
    card = copy.deepcopy(card)
    card.setdefault("trust", {}).setdefault("failure_mode", {})
    card["trust"]["failure_mode"]["distinguishable_from_true_negative"] = (
        "rc=255 NoSuchBucket on stderr, distinct from KeyCount=0")
    card["trust"]["failure_mode"].setdefault("basis_by_field", {})[
        "distinguishable_from_true_negative"] = "measured"
    return mod, schema, card


def test_rule3_baseline_real_value_under_measured_passes():
    mod, _schema, card = _basis_fixture()
    assert mod.null_value_basis_violations(card) == []


def test_rule3_null_value_under_measured_fires():
    mod, _schema, card = _basis_fixture()
    card["trust"]["failure_mode"]["distinguishable_from_true_negative"] = "unmeasured"
    v = mod.null_value_basis_violations(card)
    assert any("carries no measurement" in x for x in v), v


def test_rule3_null_value_under_absent_basis_passes_control():
    """The CERTIFIED legal pairing: value `unmeasured`, basis `absent`. MUST NOT fire."""
    mod, _schema, card = _basis_fixture()
    card["trust"]["failure_mode"]["distinguishable_from_true_negative"] = "unmeasured"
    card["trust"]["failure_mode"]["basis_by_field"]["distinguishable_from_true_negative"] = "absent"
    assert mod.null_value_basis_violations(card) == []


def test_rule3_missing_basis_entry_is_silent_not_a_violation():
    mod, _schema, card = _basis_fixture()
    card["trust"]["failure_mode"]["distinguishable_from_true_negative"] = "unmeasured"
    del card["trust"]["failure_mode"]["basis_by_field"]["distinguishable_from_true_negative"]
    assert mod.null_value_basis_violations(card) == []
