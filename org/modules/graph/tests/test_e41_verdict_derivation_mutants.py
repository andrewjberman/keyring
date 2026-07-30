#!/usr/bin/env python3
"""Mutant-kill bar for the E4.1 telemetry verdict-derivation (NFRA_VELOCITY_ESTATE WS-E4.1).

Author: 0.7.0_AE_CloudOps. Dispatch: 2.0.0_SA_COO 20260730T053344Z, three binding
conditions, main-CTO gate-approved. Condition 2 names a REQUIRED MUTANT as the
acceptance test -- this file is that mutant, made permanent.

WHY THIS FILE EXISTS
--------------------
The M3 derivation landed 2026-07-23 (NFRA_MSBEFF.R1R3) and was NEVER EXERCISED. It
read healthy for a week on inspection alone. A passing assertion that has never been
mutated has never been tested, and "I ran a mutant once in a session" is a diary
entry -- it cannot fail later, when a future maintainer makes the plausible change.

Every test below fails RED under a specific, good-faith "improvement":

  * re-defaulting an undeclared tool's nonzero to FAIL ("UNKNOWN is noisy, and a
    nonzero IS a failure, surely") -> kills tests 2, 3, 6.
  * re-freezing the verdict set as a hand-maintained constant ("a dict lookup is
    faster than a yaml parse") -> kills test 5. That exact change has now been made
    FOUR times in this lineage; the yaml header records all four.
  * relaxing the registration invariant to a warning ("it blocks unrelated commits")
    -> kills tests 7, 8.
  * making the classifier's fallback revert to the old nonzero->FAIL blanket when the
    contract surface will not load ("fall back to the previous behaviour") -> kills
    test 9. That fallback is the difference between a broken classifier that reads
    clean and one that says so.

THE LOAD-BEARING DISTINCTION these tests protect: UNKNOWN is not a flavour of FAIL.
A contracted nonzero from an undeclared tool is not a crash, and there is no channel
for "I do not know" -- so not-knowing must render AS not-knowing, or it renders as
confidence. 50 of 70 registered tools are undeclared today, so this is not a corner
case; it is 71 percent of the roster.
"""
from __future__ import annotations

import copy
import importlib.util
from contextlib import contextmanager
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve().parent
_WS = _HERE.parents[3]


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, _HERE.parent / filename)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


oc = _load("comp_output_contract_under_test", "comp_output_contract.py")
mcc = _load("manifest_check_cli_under_test", "manifest_check_cli.py")

# A declared VERDICT tool with a contracted nonzero, used as the mutation victim.
# Chosen because its contract declares all three nonzero classes (verdict/verdict/refuse),
# so a single removal exercises every branch of the derivation at once.
VICTIM = "comp-blast"


def _clear_caches():
    for fn in (oc._exit_table, oc.declared_tools, oc.pending_tools,
               oc.registered_tools, oc.undeclared_registered):
        try:
            fn.cache_clear()
        except AttributeError:
            pass


@contextmanager
def _undeclared(tool):
    """Remove `tool`'s declaration from the in-memory contract surface, then restore it.

    Disk is never touched: the mutation is applied to the lru_cached doc and the derived
    exit table is rebuilt from it. Restoration is a deep-copy put-back, so a test that
    mutates nested structure cannot leak into the next test.
    """
    doc = oc._contracts_doc()
    contracts = doc.get("contracts") or {}
    saved = copy.deepcopy(contracts.get(tool))
    contracts.pop(tool, None)
    _clear_caches()
    try:
        yield
    finally:
        if saved is not None:
            contracts[tool] = saved
        _clear_caches()


# ---------------------------------------------------------------------------
# POSITIVE CONTROL -- run first, and it is a SEPARATE test on purpose.
# A control batched with its mutant is corrupted by the mutant's own presence.
# ---------------------------------------------------------------------------

def test_1_positive_control_declared_tool_classifies_from_its_contract():
    """The un-mutated baseline. If this is RED, every mutant below is meaningless.

    A sweep that cannot find a known-present instance is a broken instrument
    reporting silence -- so the control asserts the victim IS declared, not merely
    that classification returned something.
    """
    assert VICTIM in oc.declared_tools(), (
        "the mutation victim is not declared -- the mutant tests below would pass "
        "vacuously, measuring nothing")
    assert oc.classify_exit(VICTIM, 0) == oc.PASS
    assert oc.classify_exit(VICTIM, 2) == oc.VERDICT, "a contracted nonzero must not read as a crash"
    assert oc.classify_exit(VICTIM, 3) == oc.REFUSE, "an honest could-not-check must not read as a crash"
    assert oc.classify_exit(VICTIM, 99) == oc.FAIL, (
        "an UNDECLARED rc on a DECLARED tool is a real failure -- this is the one case "
        "that must still be FAIL, and conflating it with UNKNOWN would hide crashes")


# ---------------------------------------------------------------------------
# THE REQUIRED MUTANT (condition 2)
# ---------------------------------------------------------------------------

def test_2_required_mutant_undeclared_tool_surfaces_unknown_not_fail():
    """MUTANT: delete VICTIM's declaration -> every nonzero must become UNKNOWN.

    RED under: `return table.get(tool, {}).get(rc, FAIL)` or any other re-defaulting
    of an unknown contract to FAIL. That is the pre-M3 blanket which produced the
    false comp-drift 50 percent and the gate-firing over-count.
    """
    with _undeclared(VICTIM):
        assert VICTIM not in oc.declared_tools()
        for rc in (2, 3, 99):
            got = oc.classify_exit(VICTIM, rc)
            assert got == oc.UNKNOWN, (
                f"rc={rc} on an UNDECLARED tool classified {got!r}, not UNKNOWN -- "
                "not-knowing is rendering as a verdict")
        assert oc.classify_exit(VICTIM, 0) == oc.PASS, (
            "rc 0 is PASS regardless of declaration -- an undeclared tool that "
            "SUCCEEDED is not an unknown")


def test_3_mutant_restores_cleanly_so_the_mutation_is_the_only_variable():
    """The restore leg. Without it, a leaked mutation makes later tests lie."""
    with _undeclared(VICTIM):
        assert oc.classify_exit(VICTIM, 2) == oc.UNKNOWN
    assert oc.classify_exit(VICTIM, 2) == oc.VERDICT, (
        "the contract surface did not restore -- test isolation is broken and any "
        "green below this line is untrustworthy")


def test_4_undeclared_tool_goes_loud_on_BOTH_header_lines():
    """UNKNOWN must be LOUD, not an omitted line (condition 2's 'never a silent omission').

    RED under: returning "" or skipping the header for an undeclared tool -- the
    failure mode where a missing declaration looks like a clean answer.
    """
    with _undeclared(VICTIM):
        cov = oc.coverage_line(VICTIM)
        plane = oc.plane_header(VICTIM)
        assert "UNKNOWN" in cov and "no output contract declared" in cov
        assert "coverage NOT asserted" in cov, (
            "the coverage line must explicitly disclaim, not merely omit a number")
        assert cov.strip() != "" and plane.strip() != ""
        assert "UNKNOWN" in plane and "VINTAGE: UNKNOWN" in plane


def test_5_never_registered_ghost_is_distinguishable_from_pending():
    """Two kinds of not-knowing must not collapse into one.

    'registered but awaiting a contract' and 'not registered in tools_index at all'
    are different findings with different owners. RED under a single generic
    UNKNOWN reason string.
    """
    ghost = "comp-does-not-exist-9999"
    assert ghost not in oc.registered_tools()
    assert oc.classify_exit(ghost, 1) == oc.UNKNOWN
    assert "not registered in tools_index" in oc.coverage_line(ghost)
    pend = oc.pending_tools()
    if pend:
        assert "awaiting a contract" in oc.coverage_line(pend[0]), (
            "a pending tool must report a DIFFERENT reason than an absent one")


# ---------------------------------------------------------------------------
# CONDITION 1 -- the verdict set is DERIVED, never frozen
# ---------------------------------------------------------------------------

def test_6_verdict_set_is_derived_from_the_contract_surface_not_frozen():
    """MUTANT: re-freeze the verdict set as a module constant -> RED.

    The trap: this test mutates only the DATA (the contract doc) and asserts the
    DERIVED set moves with it. A hand-frozen list cannot move without a code edit,
    so it fails here. This exact re-freezing has happened four times in this
    lineage -- see comp-output-contracts.yaml's SUPERSESSION HISTORY.
    """
    before, _ = oc.verdict_exit_map()
    assert VICTIM in before, "positive control: the victim must be in the derived verdict set"
    with _undeclared(VICTIM):
        after, _ = oc.verdict_exit_map()
        assert VICTIM not in after, (
            "the verdict set did NOT track the contract surface -- it is frozen "
            "somewhere, which is the exact defect M3 retired")
        assert len(after) == len(before) - 1


def test_7_refuse_exits_are_also_derived():
    """Same trap, second axis: REFUSE bindings must be derived, not enumerated."""
    _, before = oc.verdict_exit_map()
    assert any(t == VICTIM for t, _rc in before)
    with _undeclared(VICTIM):
        _, after = oc.verdict_exit_map()
        assert not any(t == VICTIM for t, _rc in after)


# ---------------------------------------------------------------------------
# CONDITION 1's ENFORCEMENT -- the registration invariant must BLOCK
# ---------------------------------------------------------------------------

def _fake_yaml_loader(tools_index, declared, pending):
    """Build a load_yaml stand-in keyed on which artifact is being asked for."""
    def _loader(path, *a, **kw):
        name = str(path)
        if name.endswith("graph-call-manifest.yaml"):
            return {"tools_index": {t: {} for t in tools_index}}
        if name.endswith("comp-output-contracts.yaml"):
            return {"contracts": {t: {} for t in declared},
                    "pending_declaration": list(pending)}
        return {}
    return _loader


def test_8_registration_invariant_PASSES_when_every_tool_is_covered(monkeypatch, capsys):
    """Positive control for the gate, run SEPARATELY from the block case."""
    monkeypatch.setattr(mcc, "load_yaml",
                        _fake_yaml_loader(["comp-alpha", "comp-beta"],
                                          ["comp-alpha"], ["comp-beta"]))
    rc = mcc._output_contract_invariant(["org/modules/graph/comp-output-contracts.yaml"])
    out = capsys.readouterr().out
    assert rc == 0, f"the invariant blocked a fully-covered roster: {out}"
    assert "output-contract invariant PASS" in out
    assert "2 tools_index tool(s)" in out, "the gate must PRINT its denominator, not just a verdict"


def test_9_registration_invariant_BLOCKS_a_tool_in_neither_list(monkeypatch, capsys):
    """MUTANT: a tools_index tool in NEITHER contracts NOR pending -> must BLOCK and NAME it.

    RED under: downgrading this member to advisory, or to the ramp. It is
    ramp-exempt on purpose -- an under-covered contract surface silently reverts M3
    to the frozen-list failure mode.
    """
    monkeypatch.setattr(mcc, "load_yaml",
                        _fake_yaml_loader(["comp-alpha", "comp-orphan"],
                                          ["comp-alpha"], []))
    rc = mcc._output_contract_invariant(["org/modules/graph/comp-output-contracts.yaml"])
    out = capsys.readouterr().out
    assert rc == 1, "an uncovered tools_index tool did NOT block"
    assert "BLOCKED" in out
    assert "comp-orphan" in out, (
        "the gate blocked without naming the offender -- an unactionable denial "
        "trains agents to bypass it")


def test_10_invariant_is_fail_closed_when_it_cannot_evaluate(monkeypatch, capsys):
    """MUTANT: return 0 on an unevaluable surface -> RED.

    An unevaluable completeness gate must not read as 'passed'.
    """
    def _boom(path, *a, **kw):
        raise RuntimeError("contract surface unreadable")
    monkeypatch.setattr(mcc, "load_yaml", _boom)
    rc = mcc._output_contract_invariant(["org/modules/graph/comp-output-contracts.yaml"])
    out = capsys.readouterr().out
    assert rc == 1, "the invariant failed OPEN on an unreadable contract surface"
    assert "could not be evaluated" in out


def test_11_invariant_does_not_tax_unrelated_commits(monkeypatch):
    """The scoping half: it fires at registration time, not on every commit.

    Guards against the plausible over-correction (fire always) that would get the
    member disabled for being noisy -- the way a real gate actually dies.
    """
    monkeypatch.setattr(mcc, "load_yaml",
                        _fake_yaml_loader(["comp-alpha", "comp-orphan"], ["comp-alpha"], []))
    assert mcc._output_contract_invariant(["data/inf/scripts/gold/whatever.py"]) == 0
    assert mcc._output_contract_invariant([]) == 0


# ---------------------------------------------------------------------------
# FAIL-HONEST FALLBACK -- the appender's degradation path
# ---------------------------------------------------------------------------

def test_12_appender_degrades_to_unknown_not_to_the_old_fail_blanket(monkeypatch):
    """MUTANT: make comp_log_auto's fallback return FAIL when the derivation is
    unavailable -> RED.

    This is the subtlest one. If the contract helper cannot import, the tempting
    'fall back to previous behaviour' restores exactly the nonzero->FAIL blanket M3
    retired -- and it would do so SILENTLY, on every row, while the code above it
    still reads like a derivation. A broken classifier that reads clean is the class
    this whole workstream closes.
    """
    cla = _load("comp_log_auto_under_test", "comp_log_auto.py")
    assert cla._classify_result(VICTIM, 2) == oc.VERDICT, "positive control before disabling"
    monkeypatch.setattr(cla, "_OC_OK", False)
    monkeypatch.setattr(cla, "_oc", None)
    assert cla._classify_result(VICTIM, 2) == "UNKNOWN", (
        "with the derivation unavailable the appender reverted to a verdict it "
        "cannot justify")
    assert cla._classify_result(VICTIM, 0) == "PASS", "rc 0 needs no contract to be a PASS"


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
