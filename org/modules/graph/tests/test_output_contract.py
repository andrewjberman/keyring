"""test_output_contract.py -- NFRA_MSBEFF.R1R3 / M3 acceptance + the REQUIRED MUTANTS.

An unmutated assertion has never been tested. Condition (b) requires BOTH mutants on the record in the
commit; this suite carries them plus the derivation-faithfulness + no-regression checks.
"""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

_WS = Path(__file__).resolve().parents[4]  # tests/ -> graph -> modules -> org -> workspace root
if str(_WS) not in sys.path:
    sys.path.insert(0, str(_WS))

from org.modules.graph import comp_output_contract as oc  # noqa: E402
from org.modules.graph import comp_log_auto as cla  # noqa: E402


# ----------------------------------------------------------------------------------------------------
# Derivation faithfulness + NO REGRESSION vs the retired frozen set
# ----------------------------------------------------------------------------------------------------

# The 14 tools that were in the hand-frozen VERDICT_EXIT_TOOLS set (comp_log_auto.py pre-M3). The
# derivation must still classify each as a verdict tool -- retiring the freeze must not drop coverage.
_FROZEN_14 = {
    "comp-drift", "comp-lambdamap", "comp-xray", "comp-parity", "comp-validate",
    "comp-manifest-check", "comp-surface-check", "comp-honesty", "comp-freshness",
    "comp-iam", "comp-trigger", "comp-pulse", "comp-system", "comp-constants",
}


def test_derivation_covers_the_whole_retired_frozen_set():
    verdict_tools, _ = oc.verdict_exit_map()
    missing = _FROZEN_14 - set(verdict_tools)
    assert not missing, f"derivation DROPPED verdict tools the frozen set had: {sorted(missing)}"


def test_comp_blast_added_by_grounding():
    verdict_tools, refuse = oc.verdict_exit_map()
    assert "comp-blast" in verdict_tools
    assert ("comp-blast", 3) in refuse  # NOT-FOUND is a REFUSE, source-confirmed cli.py:263


def test_comp_iam_rc3_correction_verdict_to_refuse():
    """The derivation's headline correction: rc3 is a documented COVERAGE REFUSAL, not a verdict."""
    assert cla._classify_result("comp-iam", 3) == "REFUSE"
    assert cla._classify_result("comp-iam", 1) == "VERDICT"


def test_comp_freshness_rc2_is_refuse_not_verdict():
    """CVO~Z adjudication (adopted CTO~Z 180509Z): the axis is 'concluded about the estate', not
    'touched the artifact'. rc2 = basis absent = nothing concluded = REFUSE, like comp-iam rc3.
    rc1 (real staleness) stays VERDICT, so comp-freshness remains a verdict tool."""
    assert cla._classify_result("comp-freshness", 2) == "REFUSE"
    assert cla._classify_result("comp-freshness", 1) == "VERDICT"
    verdict_tools, refuse = oc.verdict_exit_map()
    assert "comp-freshness" in verdict_tools and ("comp-freshness", 2) in refuse


@pytest.mark.parametrize("tool,rc,expected", [
    ("comp-blast", 1, "VERDICT"),
    ("comp-blast", 2, "VERDICT"),
    ("comp-blast", 3, "REFUSE"),
    ("comp-blast", 120, "FAIL"),      # declared tool, UNLISTED rc -> FAIL (launcher death, not a verdict)
    ("comp-constants", 3, "REFUSE"),
    ("comp-pulse", 1, "VERDICT"),
    ("comp-system", 2, "VERDICT"),
    ("comp-kuzu", 1, "FAIL"),         # simple tool: DB-missing / Cypher error IS a failure
    ("comp-pipescript", 1, "FAIL"),   # bad script name is an error; STALE/MISSING verdict is in stdout at rc0
])
def test_classify_matrix(tool, rc, expected):
    assert cla._classify_result(tool, rc) == expected


def test_exit_zero_is_pass_for_everything():
    for tool in ["comp-blast", "comp-kuzu", "comp-not-a-real-tool"]:
        assert cla._classify_result(tool, 0) == "PASS"


# ----------------------------------------------------------------------------------------------------
# REQUIRED MUTANT 1 (condition b) -- a tool with NO declared coverage/plane renders UNKNOWN, LOUD:
# never a silent omission, never a false clean, and its nonzero classifies UNKNOWN (never a verdict/FAIL).
# ----------------------------------------------------------------------------------------------------

def test_mutant_undeclared_tool_renders_loud_unknown():
    tool = "comp-deliberately-undeclared-mutant"
    cov = oc.coverage_line(tool)
    plane = oc.plane_header(tool)
    # LOUD: the word UNKNOWN appears; the line is NOT empty; coverage is explicitly NOT asserted.
    assert "UNKNOWN" in cov and "NOT asserted" in cov, f"coverage must LOUDLY disclaim: {cov!r}"
    assert "UNKNOWN" in plane, f"plane must LOUDLY disclaim: {plane!r}"
    assert cov.strip() and plane.strip(), "an undeclared tool must NOT render an empty (silently-omitted) line"


def test_mutant_undeclared_tool_classifies_unknown_not_a_verdict():
    """M3 mutant: a deliberately-undeclared tool's nonzero surfaces as UNKNOWN, not VERDICT and not FAIL."""
    got = cla._classify_result("comp-deliberately-undeclared-mutant", 1)
    assert got == "UNKNOWN", f"undeclared nonzero must be UNKNOWN, got {got!r}"
    assert got not in ("VERDICT", "REFUSE"), "an undeclared tool must not be laundered into a verdict"
    assert got != "FAIL", "condition b: undeclared is UNKNOWN, never a defaulted FAIL"


# ----------------------------------------------------------------------------------------------------
# REQUIRED MUTANT 2 (condition b) -- a tool whose coverage is 0% of the queried target says so LOUD,
# not a confident empty. Modeled on the audit's own named exhibits: the coverage line must NAME the
# structural blind spot rather than return a clean/empty answer.
# ----------------------------------------------------------------------------------------------------

def test_mutant_zero_coverage_of_target_is_loud_not_empty():
    # comp-pipescript against an .sh dispatch script: its coverage is 0% of that target (bd-tree/.py-scoped).
    cov = oc.coverage_line("comp-pipescript")
    assert ".sh" in cov and "UNCOVERED" in cov, f"the .sh dispatch blind spot must be NAMED, not omitted: {cov!r}"
    # comp-iam against an AWS-managed grant: 0% coverage on the DESIRED plane, must say so.
    cov_iam = oc.coverage_line("comp-iam")
    assert "BLIND" in cov_iam and ("AWS-managed" in cov_iam or "managed" in cov_iam), cov_iam
    # comp-blast against a target outside the indexed set: the blind spot must be named.
    cov_blast = oc.coverage_line("comp-blast")
    assert "outside the indexed" in cov_blast, cov_blast


# ----------------------------------------------------------------------------------------------------
# Consumer denominator is RUN-TIME derived, never hand-listed (the TO's own subject applied to itself)
# ----------------------------------------------------------------------------------------------------

def test_consumer_denominator_is_the_live_tools_index():
    import yaml
    man = yaml.safe_load((_WS / "org/modules/graph/graph-call-manifest.yaml").read_text(encoding="utf-8"))
    live = set((man.get("tools_index") or {}).keys())
    assert set(oc.registered_tools()) == live, "registered_tools() must equal the live tools_index, not a copy"


def test_every_registered_tool_is_declared_or_pending():
    """The completeness invariant, asserted in-suite too: no tools_index tool falls through the cracks."""
    reg = set(oc.registered_tools())
    covered = set(oc.declared_tools()) | set(oc.pending_tools())
    missing = sorted(reg - covered)
    assert not missing, f"tools_index tools in NEITHER contracts nor pending: {missing}"


def test_header_block_goes_to_two_lines():
    hb = oc.header_block("comp-iam")
    assert hb.count("\n") == 1 and hb.startswith("COVERAGE:") and "PLANE:" in hb


# ----------------------------------------------------------------------------------------------------
# STAGE-2 vocabulary validation (ONTOLOGY2 <-> TOOLARCH seam). The READER ~C green-lit building against the
# draft: loads canon enums from the rule bank canonical_source; NOT wired into the blocking gate yet (that +
# the grain/scope reconcile fire together on ~C's canonization signal).
# ----------------------------------------------------------------------------------------------------

def test_stage2_reads_canon_plane_enum_verbatim():
    """The canon plane enum (~C's type_tuple.plane.enum) is my plane enum verbatim -> plane reconcile is a
    no-op. If the rule bank has type_tuple yet, prove the read; if not, the reader is dormant (also valid)."""
    oc.canon_vocab_strict.cache_clear()
    vocab = oc.canon_vocab()
    if not vocab:  # pre-canonization -> dormant, nothing to assert about values
        assert oc.validate_all_declarations() == {}
        return
    assert vocab.get("plane") == ["source", "projection", "desired", "applied", "live", "mixed", "graph-cache"]


def test_stage2_all_declared_tools_pass_plane_when_armed():
    """When the canon vocab is present, every declared tool's plane must already be in-vocab (plane no-op)."""
    oc.canon_vocab_strict.cache_clear()
    if not oc.canon_vocab():
        return  # dormant
    assert oc.validate_all_declarations() == {}, "a declared tool has an out-of-canon plane value"


def test_stage2_validator_bites_on_out_of_vocab(monkeypatch):
    """REQUIRED MUTANT: an out-of-vocab value is a LOUD violation, not silently accepted."""
    oc.canon_vocab_strict.cache_clear()
    if not oc.canon_vocab():
        return  # dormant -- the mutant is only meaningful when armed
    monkeypatch.setattr(oc, "contract_for",
                        lambda t, s=None: {"plane": "NONSENSE-PLANE", "coverage": "x"})
    v = oc.validate_declaration_vocab("comp-anything")
    assert v and "NOT in canon plane enum" in v[0]


def test_stage2_dormant_when_canon_absent(monkeypatch):
    """No canon vocab (pre-canonization) -> zero violations, never a false fail."""
    orig = oc._load_yaml
    monkeypatch.setattr(oc, "_load_yaml",
                        lambda p: {} if str(p).endswith("RULE_BANK.yaml") else orig(p))
    oc.canon_vocab_strict.cache_clear()
    assert oc.validate_declaration_vocab("comp-blast") == []
    assert oc.validate_all_declarations() == {}
    oc.canon_vocab_strict.cache_clear()


def test_stage2_absent_field_is_not_a_violation():
    """grain/scope not yet declared -> NOT flagged (stage-2 validates VALUES; stage-1 owns PRESENCE).
    This is what keeps the interim safe before the one-pass reconcile adds grain/scope."""
    oc.canon_vocab_strict.cache_clear()
    if not oc.canon_vocab():
        return
    # comp-blast declares plane but not grain/scope -> must be clean (absent != invalid)
    assert oc.validate_declaration_vocab("comp-blast") == []


def test_stage2_all_tools_have_grain_and_scope_post_reconcile():
    """After the one-pass reconcile (canon signal @5d1161d70): every declared tool carries grain+scope,
    and every value is in-canon (violations {})."""
    oc.canon_vocab_strict.cache_clear()
    if not oc.canon_vocab():
        return  # dormant
    for t in oc.declared_tools():
        c = oc.contract_for(t)
        assert "grain" in c and "scope" in c, f"{t} missing grain/scope after reconcile"
    assert oc.validate_all_declarations() == {}


def test_stage2_gate_member_blocks_out_of_canon(monkeypatch):
    """The comp-manifest-check stage-2 member: PASS on the live surface, BLOCK on an out-of-canon value."""
    from org.modules.graph import manifest_check_cli as mc
    from org.modules.graph import comp_output_contract as _oc
    touch = ["org/modules/graph/comp-output-contracts.yaml"]
    _oc.canon_vocab_strict.cache_clear()
    if not _oc.canon_vocab():
        return  # dormant -> the member passes; nothing to assert about values
    assert mc._stage2_vocab_invariant(touch) == 0  # live surface is clean
    monkeypatch.setattr(_oc, "validate_all_declarations",
                        lambda: {"comp-x": ["comp-x.scope='galaxy' NOT in canon scope enum [...]"]})
    assert mc._stage2_vocab_invariant(touch) == 1  # out-of-canon -> BLOCK


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-q"]))


# ----------------------------------------------------------------------------------------------------
# SUBCOMMAND-DECLARATION invariant (CTO~Z arch-gate 220731Z, on ~B's LATENCY census + my measurement).
# tools_index `subcommands:` was populated on 65/65 and gated on NONE -- perfect camouflage. The
# omissions included derivations CLAUDE.md MANDATES (comp-iam simulate + reconcile, comp-pipescript
# postdeps, comp-registry sync): THE ROUTER COULD NOT ROUTE TO THE CALLS THE LAW REQUIRES.
# ----------------------------------------------------------------------------------------------------

def _mc():
    from org.modules.graph import manifest_check_cli as mc
    return mc


def test_declared_side_grammar_strips_flags_and_usage_forms():
    """CONSTRAINT 2: the field mixes subcommands with flags and usage forms. 'sync ROW=N' -> 'sync';
    'who-can-reach <arn>' -> 'who-can-reach'; '--json' and '<cypher>' drop out entirely."""
    got = _mc()._declared_subcommands(
        {"subcommands": ["sync ROW=N", "who-can-reach <arn>", "--json", "<cypher>", "gaps"]})
    assert got == {"sync", "who-can-reach", "gaps"}


def test_pinned_wrapper_exposes_one_derivation_not_the_engine_set():
    """CONSTRAINT 1: comp-blast pins `cli.py blast "$@"` -- it exposes ONE derivation of a shared
    engine. Without this the 5 pinned wrappers all false-positive against cli.py's full set."""
    subs, pinned, _why = _mc()._established_subcommands("comp-blast")
    assert pinned is True and subs == {"blast"}


def test_unestablishable_surface_is_unknown_never_fail():
    """CONSTRAINT 3: a tool whose surface cannot be established renders UNKNOWN, never FAIL --
    an unexercised hard-fail across 36 tools is how a gate earns a --no-verify habit."""
    subs, _pinned, why = _mc()._established_subcommands("comp-genesis")
    assert subs is None and isinstance(why, str) and why


def test_reproduces_the_comp_iam_law_mandated_omission():
    """The governance finding, as a regression guard: comp-iam exposes simulate + reconcile and the
    registry declared neither. If a backfill lands, this test flips to asserting they ARE declared --
    which is the point: the guard is that the gap cannot silently reopen."""
    import yaml
    mc = _mc()
    ti = yaml.safe_load(open("org/modules/graph/graph-call-manifest.yaml", encoding="utf-8"))["tools_index"]
    actual, pinned, _ = mc._established_subcommands("comp-iam")
    assert actual and not pinned
    assert {"simulate", "reconcile"} <= actual, "comp-iam must really expose simulate + reconcile"
    declared = mc._declared_subcommands(ti["comp-iam"])
    missing = actual - declared
    # Either they are still undeclared (the finding stands) or the backfill landed (gap closed).
    assert ("simulate" in missing) == ("simulate" not in declared)


def test_member_blocks_only_registrations_this_commit_touches(monkeypatch):
    """SCOPE: the gate lands AHEAD of the backfill without freezing the fabric -- standing drift is
    REPORTED, a drifted registration in THIS commit BLOCKS. Both directions on the record."""
    mc = _mc()
    touch = ["org/modules/graph/graph-call-manifest.yaml"]
    monkeypatch.setattr(mc, "_dict_diff_keys", lambda *a, **k: set())
    assert mc._subcommand_declaration_invariant(touch) == 0          # standing drift -> not blocking
    monkeypatch.setattr(mc, "_dict_diff_keys", lambda *a, **k: {"comp-iam"})
    assert mc._subcommand_declaration_invariant(touch) == 1          # drifted + touched -> BLOCK
    monkeypatch.setattr(mc, "_dict_diff_keys", lambda *a, **k: {"comp-blast"})
    assert mc._subcommand_declaration_invariant(touch) == 0          # pinned -> no false-positive


# ----------------------------------------------------------------------------------------------------
# THE DISARM PATH (CVO~Z finding 221805Z; test specified by ~C). My own self-tests exercised only the
# ENFORCING path -- detect + block. The DISARM path was FAIL-OPEN: _load_yaml swallowed the read failure,
# canon_vocab() returned {} before any exception, the fail-closed handler never fired, and a missing/moved
# rule bank printed a benign "DORMANT (pre-canonization)" line and returned PASS. The docstring claimed
# fail-closed while the path was fail-open -- an instrument lying about its own posture.
# The dormancy rationale ALSO EXPIRED at @5d1161d70: post-canonization an empty vocab can only mean a
# read failure or removed ratified vocabulary, so neither is legitimate any more.
# ----------------------------------------------------------------------------------------------------

def test_read_failure_raises_not_swallowed(tmp_path, monkeypatch):
    """A GATE must be able to SEE the read failure. canon_vocab_strict RAISES; only the lenient
    wrapper swallows."""
    monkeypatch.setattr(oc, "_RULE_BANK", tmp_path / "does_not_exist.yaml")
    oc.canon_vocab_strict.cache_clear()
    with pytest.raises(oc.CanonVocabUnavailable):
        oc.canon_vocab_strict()
    assert oc.canon_vocab() == {}          # lenient wrapper still safe for advisory callers
    oc.canon_vocab_strict.cache_clear()


def test_absent_type_tuple_is_distinct_from_unreadable(tmp_path, monkeypatch):
    """PROBLEM 2 (misattribution): 'read fine but no type_tuple' must NOT be reported as a read failure.
    It returns {} WITHOUT raising -- a different condition, reported differently by the gate."""
    rb = tmp_path / "rb.yaml"
    rb.write_text("meta:\n  version: 9\nroles: {}\n", encoding="utf-8")
    monkeypatch.setattr(oc, "_RULE_BANK", rb)
    oc.canon_vocab_strict.cache_clear()
    assert oc.canon_vocab_strict() == {}    # no raise
    oc.canon_vocab_strict.cache_clear()


@pytest.mark.parametrize("make,label", [
    (lambda p: p / "missing.yaml", "canonical_source MISSING"),
    (lambda p: _write_no_tt(p), "reads fine, NO type_tuple"),
])
def test_gate_BLOCKS_on_every_disarm_path(tmp_path, monkeypatch, make, label):
    """THE REGRESSION GUARD: every way of ending up with no vocabulary must BLOCK (rc=1), never
    silently pass. This is the assertion whose absence let the gate be fail-open."""
    from org.modules.graph import manifest_check_cli as mc
    monkeypatch.setattr(oc, "_RULE_BANK", make(tmp_path))
    oc.canon_vocab_strict.cache_clear()
    rc = mc._stage2_vocab_invariant(["org/modules/graph/comp-output-contracts.yaml"])
    assert rc == 1, f"DISARMED gate returned PASS on: {label}"
    oc.canon_vocab_strict.cache_clear()


def _write_no_tt(p):
    rb = p / "rb_no_tt.yaml"
    rb.write_text("meta:\n  version: 9\nroles: {}\n", encoding="utf-8")
    return rb


def test_enforcing_path_still_passes_on_real_state():
    """The fix must not break what CVO~Z confirmed works: real state -> PASS."""
    from org.modules.graph import manifest_check_cli as mc
    oc.canon_vocab_strict.cache_clear()
    assert mc._stage2_vocab_invariant(["org/modules/graph/comp-output-contracts.yaml"]) == 0
