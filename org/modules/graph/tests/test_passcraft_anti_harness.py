"""AC1/AC4/AC5 anti-harness proof for NFRA_PASSCRAFT.TO-1's recon-scaffolding SDK.

The load-bearing invariant (PRD sec.0, the one CTO~A gates hardest) is that PASSCRAFT is SCAFFOLDING,
never a verdict: NO component may compute a pass/fail. These tests prove it structurally -- the recon
evidence pack carries NO verdict/pass/fail key ANYWHERE (checked recursively), for a believed-defective
tool as much as any other, while STILL surfacing the archetype's lead probes that WOULD expose it.
That is the mutant-kill applied to PASSCRAFT itself: it is shown UNABLE to conclude.

Run: python -m pytest org/modules/graph/tests/test_passcraft_anti_harness.py
"""
from __future__ import annotations

import os
import sys

import pytest

sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
import comp_passcraft as pc  # noqa: E402  (path set above so the sibling backend imports)


def test_taxonomy_is_8_moves_and_12_shapes():
    assert len(pc.MOVES) == 8
    assert len(pc.SHAPES) == 12


def test_ac1_recon_emits_eight_moves():
    pack = pc.recon("comp-freshness")
    assert isinstance(pack["moves"], list) and len(pack["moves"]) == 8


def test_ac1_no_verdict_key_anywhere():
    """AC1: the evidence pack carries NO verdict/pass/fail key anywhere -- structurally unable to
    conclude. This is the value PASSCRAFT must NEVER produce if it is scaffolding, not a harness."""
    pack = pc.recon("comp-freshness")
    assert not pc._has_verdict_key(pack)


def test_ac1_stops_at_verdict_door():
    pack = pc.recon("comp-freshness")
    assert "STOP" in pack["verdict_door"]


def test_ac4_known_defective_not_flagged_but_probe_surfaced():
    """AC4: a believed-defective tool (comp-freshness = aging-oracle in the census) is NOT auto-
    flagged (no verdict), AND the aging-oracle lead probe -- the one that WOULD expose it -- is
    surfaced. The mutant-kill on PASSCRAFT: it equips the human, it does not judge."""
    pack = pc.recon("comp-freshness")
    assert not pc._has_verdict_key(pack)
    shapes = {p["shape"] for p in pack["moves"][7]["lead_probes"]}
    assert "aging-oracle" in shapes


def test_ac4b_injected_archetype_loads_the_exposing_probe():
    """A hand-classified injected archetype loads the RIGHT exposing probe, still with no verdict."""
    pack = pc.recon("comp-iam", archetype="resource-blind")
    shapes = {p["shape"] for p in pack["moves"][7]["lead_probes"]}
    assert "resource-blind" in shapes
    assert not pc._has_verdict_key(pack)


def test_ac5_class_agnostic_non_comp_scanner():
    """AC5: the 12 shapes are structural, not Opal facts -- a NON-comp scanner reconned through the
    SAME 8 moves + taxonomy, no schema fork, no verdict."""
    pack = pc.recon(__file__, archetype="test-writes-prod")   # this very test file as a stand-in scanner
    assert len(pack["moves"]) == 8
    assert not pc._has_verdict_key(pack)
    shapes = {p["shape"] for p in pack["moves"][7]["lead_probes"]}
    assert "test-writes-prod" in shapes


def test_rc_check_unreadable_target_is_invocation_error_not_empty():
    """rc-check / R7: an unreadable target yields INVOCATION-ERROR, never a clean '0 found' -- a
    failed read is not a negative observation."""
    pack = pc.recon(os.path.join(pc.TOOLDIR, "comp-zzzz-does-not-exist"))
    assert pack["moves"][0]["invocation_error"] is not None


def test_every_archetype_maps_to_real_shapes():
    """Every archetype's lead probes reference real shapes in the taxonomy (no dangling probe)."""
    shape_names = {name for name, _ in pc.SHAPES}
    for arch, order in pc.ARCHETYPE_PROBES.items():
        assert arch in shape_names, arch
        for s in order:
            assert s in shape_names, (arch, s)


def test_embedded_self_test_passes():
    ok, checks = pc._self_test()
    assert ok, [c for c in checks if not c["pass"]]


# ---- TO-2: the ToolAudit CSE emitter (NFRA_CSE-conformant, anti-harness one layer up) ----

def _valid_audit():
    return {"tool": "comp-freshness", "verdict": "DEFECTIVE -- HAND-AUTHORED lead, not computed",
            "class": "INFERRED", "rail": {"R1": "fail"}, "evidence_ref": ".tools/comp-freshness",
            "question_class": "DYNAMIC",   # FP-R0: aging-oracle = a what-value-flowed question
            "falsifier": "false if it reads the date-key not mtime", "domain": "aws-cloud",
            "shared_substrate": ["trading_calendar"]}


def test_to2_valid_toolaudit_emits_nfra_cse_conformant_record():
    """A hand-authored ToolAudit emits {tool_audit, cse}, and the CSE passes cse_schema.validate
    (schema + provenance + confidence + AC6 head + AC2 fidelity decompression)."""
    import cse_schema as cs
    mk = "git:testvintage"
    rec = pc.emit_tool_audit(_valid_audit(), mk)
    assert {"tool_audit", "cse"} <= set(rec)
    cok, cerr = cs.validate(pc.build_tool_audit_cse(_valid_audit(), mk))
    assert cok, cerr


def test_to2_ac2_empty_evidence_ref_rejected_fail_closed():
    """AC2: a verdict with no cited evidence is inadmissible -> ToolAuditError (fail-closed)."""
    bad = dict(_valid_audit(), evidence_ref="")
    with pytest.raises(pc.ToolAuditError):
        pc.emit_tool_audit(bad, "git:testvintage")


def test_to2_anti_harness_missing_verdict_rejected():
    """THE anti-harness proof for the emitter: it has NO verdict-deriving path -- a ToolAudit missing
    the hand-authored verdict cannot be completed by the emitter and is REJECTED."""
    no_verdict = {k: v for k, v in _valid_audit().items() if k != "verdict"}
    with pytest.raises(pc.ToolAuditError):
        pc.emit_tool_audit(no_verdict, "git:testvintage")


def test_to2_verdict_serialized_verbatim_never_altered():
    audit = _valid_audit()
    rec = pc.emit_tool_audit(audit, "git:testvintage")
    assert rec["tool_audit"]["verdict"] == audit["verdict"]


def test_to2_class_off_r1_enum_rejected():
    bad = dict(_valid_audit())
    bad["class"] = "MAYBE"
    with pytest.raises(pc.ToolAuditError):
        pc.emit_tool_audit(bad, "git:testvintage")


# ---- FP-R0 (FRONTPASS_RULES_canonical_20260712, R0 RULED IN): the QUESTION-class consistency lint ----
# It is a CONSISTENCY LINT (checks the hand-authored question_class/class/evidence_ref triple for
# coherence), NOT a verdict engine -- it computes no tool verdict, so the anti-harness invariant holds.

def _dyn_obs(evidence_ref):
    a = dict(_valid_audit(), question_class="DYNAMIC", evidence_ref=evidence_ref)
    a["class"] = "OBSERVED"
    return a


def test_fpr0_question_class_required_fail_closed():
    """question_class is REQUIRED -- an absent question-class is 'never classified', not a pass."""
    no_qc = {k: v for k, v in _valid_audit().items() if k != "question_class"}
    with pytest.raises(pc.ToolAuditError):
        pc.emit_tool_audit(no_qc, "git:testvintage")


def test_fpr0_question_class_off_vocab_rejected():
    with pytest.raises(pc.ToolAuditError):
        pc.emit_tool_audit(dict(_valid_audit(), question_class="MAYBE"), "git:testvintage")


def test_fpr0_dynamic_observed_from_source_rejected():
    """THE BITE: a DYNAMIC question claimed OBSERVED from a SOURCE file:line is inadmissible -- reading
    the code that could produce a runtime fact does not OBSERVE it (that claim is INFERRED)."""
    with pytest.raises(pc.ToolAuditError):
        pc.emit_tool_audit(_dyn_obs("org/modules/graph/comp_passcraft.py:1"), "git:testvintage")


def test_fpr0_dynamic_observed_from_exercise_accepted():
    """NOT over-firing: the SAME dynamic OBSERVED claim backed by an EXERCISED run is admissible --
    FP-R0 bars source, not exercise (exercise is what PROMOTES a dynamic claim to OBSERVED)."""
    rec = pc.emit_tool_audit(_dyn_obs("EXERCISED: paired-run 2026-07-12 shows FRESH-on-stale"),
                             "git:testvintage")
    assert {"tool_audit", "cse"} <= set(rec)


def test_fpr0_static_observed_from_source_accepted():
    """FP-R0 touches ONLY dynamic questions: a STATIC fact (e.g. 'does the file define X') IS
    observable from source, so STATIC + OBSERVED + a source ref is fine."""
    a = dict(_valid_audit(), question_class="STATIC", evidence_ref="org/modules/graph/comp_passcraft.py:1")
    a["class"] = "OBSERVED"
    rec = pc.emit_tool_audit(a, "git:testvintage")
    assert {"tool_audit", "cse"} <= set(rec)


def test_to2_no_verdict_deriving_function_in_module():
    """Structural anti-harness: the module exposes no function that DERIVES a verdict from evidence.
    Every verdict-touching entrypoint takes the verdict as an INPUT (build/validate/emit_tool_audit).
    NOTE: this is NAME-based and therefore weak on its own (a verdict-computer named innocuously would
    slip it); test_ac4_anti_harness_missing_verdict_reject_is_non_vacuous below is the FUNCTIONAL guard."""
    import inspect
    for name, obj in inspect.getmembers(pc, inspect.isfunction):
        assert not any(tok in name.lower() for tok in ("compute_verdict", "derive_verdict",
                                                       "decide_verdict", "score_verdict", "judge")), name


def test_ac4_anti_harness_missing_verdict_reject_is_non_vacuous(monkeypatch):
    """AC4 NON-VACUITY (closes the name-based gap above): the anti-harness 'no verdict-deriving path'
    property must BITE against an INJECTED derive path, not be vacuously true. Neuter: monkeypatch
    validate so a missing verdict is auto-supplied (a DERIVE path). The missing-verdict audit -- which
    the real code REJECTS -- is then NO LONGER rejected, so the property FLIPS. That proves the REJECT
    property holds ONLY because no derive path exists (a functional guard the name-check cannot give)."""
    real_validate = pc.validate_tool_audit
    no_verdict = {k: v for k, v in _valid_audit().items() if k != "verdict"}

    # sanity: WITHOUT the mutant, the property holds -- a missing verdict IS rejected.
    with pytest.raises(pc.ToolAuditError):
        pc.emit_tool_audit(no_verdict, "git:testvintage")

    def deriving_validate(a, mkh):   # the mutant: DERIVE a verdict instead of requiring one
        return real_validate(dict(a, verdict=(a.get("verdict") or "DERIVED-BY-MUTANT")), mkh)

    monkeypatch.setattr(pc, "validate_tool_audit", deriving_validate)
    rec = pc.emit_tool_audit(no_verdict, "git:testvintage")   # WITH the derive path: must NOT raise now
    assert {"tool_audit", "cse"} <= set(rec), (
        "the injected verdict-deriving path defeated the reject property -- so the real property is "
        "non-vacuous (it depends on there being no derive path)")
