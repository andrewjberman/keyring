#!/usr/bin/env python3
"""WS-E5: does the L0a boundary-report type express tonight's FIVE false-negative mechanisms?

Author: 0.7.0_AE_CloudOps. Dispatch: 2.0.0_SA_COO 20260730T112424Z (~C-confirmed at source).

ANSWER, DERIVED BY EXERCISE: ONE of the five. The other four are blocked by the type's ARITY,
not by its enums -- it carries exactly one `source`, one `address_space` and one `head`, so a
MISMATCH between the plane measured and the plane a claim ranges over has nowhere to live.

COO's instruction was explicit: *"Say so if it cannot -- that is a finding about the standard,
and it is more valuable than a suite that passes."* This file is that finding, made
re-runnable. It is an OBSERVATION instrument, not a gate: nothing here denies, blocks, or
refuses anything, because E5's enforcement is E1-gated and E1 has no registry yet.

WHY THIS IS A TEST AND NOT A MEMO
--------------------------------
A memo asserting "the type cannot express X" decays into an opinion. These tests DEMONSTRATE
it: they build a report the type's own validator accepts with ZERO violations, and show the
mechanism-2 defect fully present inside it. And they are written to FLIP when the gap closes --
`test_5_the_gap_is_the_arity` fails the day a claim-scope field lands, which converts this file
from documentation of a limit into verification of its fix. A test that merely records a gap
would go stale silently; one that fails on the fix cannot.

TONIGHT'S FIVE, and what each needs the report to answer:
  1 SHARED-WORKTREE SUBSTRATE DRIFT  did the plane I READ equal the plane that EXECUTED?
  2 WIDER-THAN-MEASURED (the spine)  does the CLAIM's axis equal the MEASURED axis?
  3 THE UNCOMPUTED HANDED FIGURE     was this number COMPUTED here, or carried in?
  4 THE INSTRUMENT CREATED THE FINDING  did the measurement ENVIRONMENT differ from production
                                        in the dimension under test?
  5 THE READ THAT OUTLIVED ITS CONSUMER does anything downstream still consume this node?

Only (5) is coverage-shaped, and coverage is what a boundary report is FOR. The other four are
all one family: *the plane I measured is not the plane the claim ranges over.*
"""
from __future__ import annotations

import sys
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(_HERE.parent))

import boundary_report as B  # noqa: E402


def _conformant():
    """A report the type's OWN validator accepts with zero violations.

    Modelled on a REAL mechanism-2 instance from this session: the comp-tool run sink's FAIL
    population, measured exactly. Cells must BALANCE to surface_total and non-applicable cells
    must carry method=None -- my first draft failed both and the validator caught it, which is
    the only reason the blindness demonstration below is worth anything. A blindness claim built
    on a report the validator already REJECTS proves nothing about the validator.
    """
    return {
        "tool": "comp-msbeff-rebaseline",
        "source": "org/mcp/comp-tool-runs.jsonl",
        "address_space": "json_key_path",
        "head": "3380a45f66",
        "surface_total": 10255,
        "cells": {
            "covered":  {"applicable": True,  "count": 10168, "method": "declared"},
            "member":   {"applicable": True,  "count": 87,    "method": "declared"},
            "doc_only": {"applicable": False, "count": None,  "method": None},
            "orphan":   {"applicable": False, "count": None,  "method": None},
        },
    }


# ---------------------------------------------------------------------------
# POSITIVE CONTROL -- separate, and first. A validator only ever seen to REJECT
# is as untested as one only ever seen to ACCEPT.
# ---------------------------------------------------------------------------

def test_1_positive_control_the_validator_accepts_a_conformant_report():
    v = B.validate(_conformant())
    assert v == [], "the fixture is not conformant, so every test below would be vacuous: %s" % v


def test_2_negative_control_the_validator_still_bites():
    """Paired with test_1 so 'accepts everything' cannot masquerade as 'accepts this'."""
    bad = _conformant()
    bad["cells"]["doc_only"]["count"] = 0          # N/A rendered as 0 -- the BR003 class
    bad["cells"]["doc_only"]["applicable"] = False
    assert B.validate(bad), "the validator accepted N/A-as-0; it is not enforcing applicability"


# ---------------------------------------------------------------------------
# THE SPINE: mechanism 2 survives a fully conformant report
# ---------------------------------------------------------------------------

def test_3_mechanism2_axis_mismatch_survives_a_ZERO_VIOLATION_report():
    """A conformant report + a claim about a DIFFERENT population = undetectable here.

    MEASURED axis: this DEVICE's run sink (gitignored, device-local).
    CLAIM   axis: "the estate".
    Every number correct, denominator printed, N/A honest -- composite WRONG.

    This is not a bug in the validator. It is the type's scope: a boundary report states what
    a DETECTOR could not see, and mechanism 2 is a detector that saw perfectly while a sentence
    beside it ranged wider. The sentence is not in the type.
    """
    rep = _conformant()
    assert B.validate(rep) == []
    # There is no field that could carry the claim's axis for a rule to compare against.
    claimish = [f for f in B.REQUIRED_TOP
                if any(t in f for t in ("claim", "propos", "scope", "asserts"))]
    assert claimish == [], (
        "a claim-bearing field now EXISTS (%s) -- update this test: the standard may now be "
        "able to express mechanism 2, which is the outcome we want" % claimish)


@pytest.mark.parametrize("measured,claimed", [
    ("tail", "interior"),
    ("basis", "corpus"),
    ("output-honesty", "input-existence"),
    ("calendar", "cadence"),
])
def test_4_the_four_adjacent_axis_pairs_are_not_REPRESENTABLE(measured, claimed):
    """COO's four-for-four: every input correct, the composite wrong every time.

    Both members of each pair would occupy the SAME single `source`/`address_space` slot, so the
    report cannot hold the pair, let alone compare it. If a future type can, this test should be
    rewritten to assert the comparison -- not deleted.
    """
    rep = _conformant()
    rep["source"] = "axis:%s" % measured
    assert B.validate(rep) == [], "fixture broke; the point below would be vacuous"
    # one slot, so the claimed axis simply overwrites the measured one -- no mismatch is visible
    rep2 = dict(rep, source="axis:%s" % claimed)
    assert B.validate(rep2) == []
    assert rep["source"] != rep2["source"]
    assert "source" in B.REQUIRED_TOP and len([f for f in B.REQUIRED_TOP if f == "source"]) == 1, (
        "the type now carries more than one source slot -- re-derive whether the pair is "
        "representable")


# ---------------------------------------------------------------------------
# WHAT THE TYPE *DOES* EXPRESS -- so this file is not only a complaint
# ---------------------------------------------------------------------------

def test_5_mechanism5_IS_expressible_via_the_orphan_cell():
    """`orphan` = "nothing downstream knows it exists" IS the read-that-outlived-its-consumer.

    So the standard is not inadequate in general -- it is adequate for exactly the shape it was
    built for (coverage), and mechanism 5 is that shape. Recording the YES matters as much as
    the NOs: a report that found only gaps would be a report nobody could act on.
    """
    assert "orphan" in B.CELLS
    assert "nothing downstream" in B.CELLS["orphan"]
    rep = _conformant()
    rep["cells"]["orphan"] = {"applicable": True, "count": 1, "method": "traversal"}
    rep["cells"]["covered"]["count"] = 10167          # keep the accounting balanced
    assert B.validate(rep) == [], "an orphan-bearing report should be conformant: %s" % B.validate(rep)


def test_6_the_gap_is_the_ARITY_not_the_ENUMS():
    """The discriminating claim, asserted so it can be refuted.

    If the blockage were vocabulary, adding enum members would fix it. It is not: `cells` and
    `methods` are rich and correct. The blockage is that there is ONE slot per axis, so a
    MISMATCH between two planes is unrepresentable regardless of how many enum members exist.
    """
    assert len(B.CELLS) >= 4 and len(B.METHODS) >= 3, "enums are not impoverished"
    one_per_axis = ("source", "address_space", "head")
    for f in one_per_axis:
        assert f in B.REQUIRED_TOP
    # No field name suggests a second plane / comparison partner.
    assert not [f for f in B.REQUIRED_TOP
                if any(t in f for t in ("_read", "_exec", "expected_", "_b", "other_"))]


def test_7_this_instrument_ARMS_NOTHING():
    """E5's enforcement is E1-gated. This file must never acquire a deny.

    Guard against the plausible next edit -- 'while we are here, make it fail the build'. There
    is no E1 registry, so there is no registration event to gate, and arming it here would be
    an enforcement nobody authorized.

    A TEXT SCAN IS THE WRONG INSTRUMENT HERE and the first draft of this test proved it: it
    grepped its own source for forbidden tokens, and the tokens matched their own entries in the
    forbidden list. Self-referential text-matching cannot separate "this file arms something"
    from "this file names the thing it must not do." So test the PROPERTY via the AST instead --
    the same distinction CLAUDE.md draws for F-010, where text-matching is sound only because
    `-F` moves the content OUT of the parsed surface. Here the content IS the parsed surface.
    """
    import ast
    tree = ast.parse(Path(__file__).read_text(encoding="utf-8"))

    # (a) no enforcement-capable module is imported at all.
    imported = set()
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            imported.update(a.name.split(".")[0] for a in node.names)
        elif isinstance(node, ast.ImportFrom) and node.module:
            imported.add(node.module.split(".")[0])
    for banned in ("subprocess", "shutil", "signal"):
        assert banned not in imported, (
            "this file imports %s -- E5 is an OBSERVATION instrument and its enforcement is "
            "E1-gated; arming it here would be an enforcement nobody authorized" % banned)

    # (b) the only SystemExit is the module's own test-runner guard, which exits THIS process
    #     when run directly. That is a runner idiom, not a gate over anyone else's work.
    exits = [n for n in ast.walk(tree)
             if isinstance(n, ast.Raise) and isinstance(n.exc, ast.Call)
             and getattr(n.exc.func, "id", "") == "SystemExit"]
    assert len(exits) <= 1, "more than one exit path -- something here now refuses"

    # (c) it observes the type; it never inspects a CALLER.
    assert "boundary_report" in imported


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
