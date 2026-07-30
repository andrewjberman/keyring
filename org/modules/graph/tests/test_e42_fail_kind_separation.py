#!/usr/bin/env python3
"""Mutant-kill bar for E4.2 -- the FAIL column's three meanings (NFRA_VELOCITY_ESTATE WS-E4.2).

Author: 0.7.0_AE_CloudOps. Dispatch 2.0.0_SA_COO 20260730T053344Z: "Separate them IN THE
MACHINE RECORD, not in a report. Note the consequence you are unlocking: a rising FAIL
count is currently indistinguishable from BETTER NEGATIVE-CONTROLLING, which is a GOOD
thing reading as a bad one."

THE THREE MEANINGS HAVE DIFFERENT OWNERS AND OPPOSITE SIGNS
  (a) negative_control -- a probe engineered to fail, proving a tool can detect. MORE IS
      BETTER. Counting it as failure inverts the sign of the improvement signal.
  (b) usage_error      -- the caller passed something unusable. Says nothing about the estate.
  (c) finding          -- the tool worked and the estate is wrong.

AND TWO HONEST UNKNOWNS, which in the live data are the MAJORITY (54 of 87 FAIL rows at
build time -- 62%). They exist because the alternative is guessing, and a
plausible-but-wrong bucket answers the improvement question confidently and wrongly:
  undeclared_rc   -- the rc is absent from the contract. Live: 19 rows carry rc=120 across
                     6 tools, declared by nobody. TWO causal hypotheses were tested and
                     BOTH REFUTED (harness-rc corruption -- the rate ROSE after the 07-28
                     mount fix; CPython broken-pipe flush -- a piped python exits 1, and
                     comp-opalbizsem --list exits 2 both piped and unpiped). Cause
                     UNDETERMINED, owned item, NOT given a meaning.
  kind_undeclared -- the rc IS declared fail but carries no `kind:`. Live: comp-kuzu rc1 is
                     30 rows, the single highest-value declaration outstanding.

THE TRAPS -- each fails RED under a specific good-faith change:
  * defaulting an unknown kind to `finding` ("a failure is a finding, surely") -> tests 4, 5.
    This is the one that would quietly re-create the two-meaning-null this workstream closes.
  * populating fail_kind on non-FAIL rows -> test 6. A kind on a PASS is a category error a
    consumer will read as real.
  * hand-freezing a {tool: kind} map instead of deriving from the contract -> test 7.
  * dropping the coverage denominator so the undeclared tail goes invisible -> test 8.
"""
from __future__ import annotations

import copy
import importlib.util
from contextlib import contextmanager
from pathlib import Path

import pytest

_HERE = Path(__file__).resolve().parent


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, _HERE.parent / filename)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


oc = _load("comp_output_contract_e42", "comp_output_contract.py")

# comp-pipescript rc1/rc2 are declared `class: fail, kind: usage` -- the transcription of the
# owner's own meaning text ("usage / argument error"), not a new semantic.
USAGE_TOOL, USAGE_RC = "comp-pipescript", 2
# comp-kuzu rc1 is declared fail with NO kind -> the honest kind_undeclared bucket.
NOKIND_TOOL, NOKIND_RC = "comp-kuzu", 1


def _clear():
    for fn in (oc._exit_table, oc._fail_kind_table, oc.declared_tools):
        try:
            fn.cache_clear()
        except AttributeError:
            pass


@contextmanager
def _patch_exit(tool, rc, spec):
    """Temporarily set one exit_codes entry on the in-memory contract surface."""
    doc = oc._contracts_doc()
    c = (doc.get("contracts") or {}).get(tool)
    saved = copy.deepcopy(c.get("exit_codes")) if isinstance(c, dict) else None
    if isinstance(c, dict):
        c.setdefault("exit_codes", {})[str(rc)] = spec
    _clear()
    try:
        yield
    finally:
        if isinstance(c, dict) and saved is not None:
            c["exit_codes"] = saved
        _clear()


# ---------------------------------------------------------------------------
# POSITIVE CONTROLS -- separate, first
# ---------------------------------------------------------------------------

def test_1_positive_control_a_declared_usage_exit_types_as_usage_error():
    """Tests the MECHANISM, on a declaration this test INJECTS ITSELF.

    It deliberately does NOT assert that comp-pipescript is declared `kind: usage` in the
    live yaml. An earlier version did, and it was wrong twice over: (1) it made the suite
    fail on a fresh clone if the declaration landed in a later commit than the code -- a
    RED for a non-defect, which is how a suite gets disabled; (2) it measured the DATA
    rather than the derivation, so a test named "positive control" would have gone green or
    red for reasons unrelated to the code it guards. The live declaration state is
    REPORTED, not asserted, by test_8b.
    """
    assert oc.classify_exit(USAGE_TOOL, USAGE_RC) == oc.FAIL, (
        "precondition: this rc must classify FAIL for a fail_kind to be meaningful")
    with _patch_exit(USAGE_TOOL, USAGE_RC, {"class": "fail", "kind": "usage",
                                            "meaning": "usage / argument error"}):
        assert oc.classify_fail_kind(USAGE_TOOL, USAGE_RC) == oc.FK_USAGE_ERROR


def test_2_positive_control_a_declared_fail_with_no_kind_is_LOUD_not_guessed():
    assert oc.classify_exit(NOKIND_TOOL, NOKIND_RC) == oc.FAIL
    assert oc.classify_fail_kind(NOKIND_TOOL, NOKIND_RC) == oc.FK_KIND_UNDECLARED, (
        "a fail exit with no declared kind was assigned a meaning it does not have")


def test_3_the_synthetic_flag_wins_and_marks_a_DELIBERATE_probe():
    """(a) is a property of the INVOCATION, not of the exit code -- so the run-time flag
    outranks any contract declaration, and it applies even to a probe that passed (a
    negative control that did NOT trip is itself worth seeing).
    """
    assert oc.classify_fail_kind(USAGE_TOOL, USAGE_RC, synthetic=True) == oc.FK_NEGATIVE_CONTROL
    assert oc.classify_fail_kind("comp-blast", 0, synthetic=True) == oc.FK_NEGATIVE_CONTROL


# ---------------------------------------------------------------------------
# THE CORE TRAP: never default an unknown into one of the three
# ---------------------------------------------------------------------------

def test_4_an_UNDECLARED_rc_is_undeclared_rc_and_NEVER_a_finding():
    """MUTANT: `return _fail_kind_table().get(tool,{}).get(rc, FK_FINDING)` -> RED.

    rc=120 is the live instance: 19 rows, 6 tools, declared by nobody, cause UNDETERMINED
    after two refuted hypotheses. Bucketing it as a finding would put 22 rows of
    unexplained exits into the estate-is-wrong column and make the estate look worse for a
    reason nobody can name.
    """
    got = oc.classify_fail_kind(USAGE_TOOL, 120)
    assert got == oc.FK_UNDECLARED_RC, (
        "an rc absent from the contract was typed %r instead of undeclared_rc" % got)
    assert got != oc.FK_FINDING and got != oc.FK_USAGE_ERROR


def test_5_the_two_unknowns_are_DISTINGUISHABLE_from_each_other():
    """They have different owners and different fixes, so collapsing them loses the routing.

    undeclared_rc   -> find out what this exit MEANS (tool owner)
    kind_undeclared -> the meaning is known, TYPE it (a one-line contract edit)
    """
    a = oc.classify_fail_kind(USAGE_TOOL, 120)          # rc not in the contract at all
    b = oc.classify_fail_kind(NOKIND_TOOL, NOKIND_RC)   # rc declared fail, kind absent
    assert a == oc.FK_UNDECLARED_RC
    assert b == oc.FK_KIND_UNDECLARED
    assert a != b, "the two kinds of not-knowing collapsed into one"


def test_6_fail_kind_is_ABSENT_on_every_non_FAIL_row(monkeypatch):
    """MUTANT: populate fail_kind for VERDICT/REFUSE/PASS -> RED.

    A kind on a PASS is a category error a consumer will read as real. None (key omitted)
    is the only honest value.
    """
    assert oc.classify_fail_kind("comp-blast", 0) is None, "rc 0 must carry no fail_kind"
    assert oc.classify_exit("comp-blast", 2) == oc.VERDICT
    assert oc.classify_fail_kind("comp-blast", 2) is None, "a VERDICT is not a fail"
    assert oc.classify_exit("comp-blast", 3) == oc.REFUSE
    assert oc.classify_fail_kind("comp-blast", 3) is None, "a REFUSE is not a fail"
    # an UNDECLARED tool's nonzero is UNKNOWN, not FAIL -> also no kind
    assert oc.classify_exit("comp-zzz-nope", 1) == oc.UNKNOWN
    assert oc.classify_fail_kind("comp-zzz-nope", 1) is None


# ---------------------------------------------------------------------------
# DERIVED, NOT FROZEN -- inherits E4.1 condition 1 one level down
# ---------------------------------------------------------------------------

def test_7_the_kind_is_DERIVED_from_the_contract_not_a_frozen_map():
    """MUTANT: hardcode a {tool: kind} dict -> RED, because this test moves only the DATA."""
    before = oc.classify_fail_kind(NOKIND_TOOL, NOKIND_RC)
    assert before == oc.FK_KIND_UNDECLARED
    with _patch_exit(NOKIND_TOOL, NOKIND_RC, {"class": "fail", "kind": "finding"}):
        assert oc.classify_fail_kind(NOKIND_TOOL, NOKIND_RC) == oc.FK_FINDING, (
            "the kind did not track the contract surface -- it is frozen somewhere")
    assert oc.classify_fail_kind(NOKIND_TOOL, NOKIND_RC) == before, "restore leaked"


def test_7b_an_out_of_vocab_kind_does_not_silently_become_a_meaning():
    """A typo in a declaration must not mint a new bucket or pick a flattering one."""
    with _patch_exit(NOKIND_TOOL, NOKIND_RC, {"class": "fail", "kind": "usagge"}):
        got = oc.classify_fail_kind(NOKIND_TOOL, NOKIND_RC)
        assert got == oc.FK_KIND_UNDECLARED, (
            "an out-of-vocab kind %r was accepted as a meaning" % got)


# ---------------------------------------------------------------------------
# THE DENOMINATOR MUST STAY VISIBLE
# ---------------------------------------------------------------------------

def test_8_fail_kind_coverage_prints_the_undeclared_tail_by_name(monkeypatch):
    """MUTANT: return only a count, or drop the tail -> RED.

    A bounded-and-visible tail is the whole reason this is safe to ship half-declared. An
    invisible tail is how the pending list becomes a permanent silence.
    """
    cov = oc.fail_kind_coverage()
    for k in ("declared_fail_exits", "with_kind", "without_kind", "note"):
        assert k in cov
    assert isinstance(cov["without_kind"], list)
    assert cov["declared_fail_exits"] >= cov["with_kind"]
    # the tail must be NAMED, not counted
    if cov["without_kind"]:
        assert all(":" in x for x in cov["without_kind"]), (
            "the tail must name tool:rc pairs so the fix is actionable")
    assert "never defaulted" in cov["note"]


def test_8b_report_the_live_declaration_state_without_asserting_it(capsys):
    """REPORTS, never asserts. The live tail is a migration fact that changes as owners
    declare; a test that asserts it goes RED on someone else's correct progress. What must
    hold is only that the tail is ENUMERABLE -- test_8 owns that.
    """
    cov = oc.fail_kind_coverage()
    print("\n[live fail-kind coverage] %d declared fail-exits, %d kinded, %d not: %s"
          % (cov["declared_fail_exits"], cov["with_kind"],
             len(cov["without_kind"]), ", ".join(cov["without_kind"]) or "(none)"))
    print("[live] %s rc%d -> %s" % (USAGE_TOOL, USAGE_RC,
                                    oc.classify_fail_kind(USAGE_TOOL, USAGE_RC)))
    assert isinstance(cov["without_kind"], list)  # enumerable is the only invariant here


def test_9_appender_emits_fail_kind_only_when_applicable(monkeypatch, tmp_path):
    """The wiring: the typed field reaches the machine record, and is OMITTED not nulled.

    MUTANT: always write the key (even as null) -> RED, because a consumer cannot then
    distinguish "not a fail" from "kind unknown" -- the exact two-meaning-null again.
    """
    import json
    cla = _load("comp_log_auto_e42", "comp_log_auto.py")
    sink = tmp_path / "org" / "mcp"
    sink.mkdir(parents=True)
    (tmp_path / "org" / "mcp" / "comp-tool-runs.jsonl").write_text("", encoding="utf-8")

    monkeypatch.delenv("COMP_SYNTHETIC_FIXTURE", raising=False)
    cla._append_log(tmp_path, USAGE_TOOL, "io", USAGE_RC, "0.7.0_AE_CloudOps", "(no-TO)")
    cla._append_log(tmp_path, "comp-blast", "x", 0, "0.7.0_AE_CloudOps", "(no-TO)")
    rows = [json.loads(x) for x in
            (tmp_path / "org" / "mcp" / "comp-tool-runs.jsonl").read_text(encoding="utf-8").splitlines() if x.strip()]
    assert len(rows) == 2
    fail_row, pass_row = rows[0], rows[1]
    # Assert the WIRING against the derivation the appender itself uses -- NOT against a
    # hardcoded kind. Which kind this tool's rc carries is a property of the contract yaml
    # and may land in a different commit than this code; the wiring is what this test owns.
    expected = cla._oc.classify_fail_kind(USAGE_TOOL, USAGE_RC)
    assert expected is not None, "precondition: this rc must produce SOME kind"
    assert fail_row["fail_kind"] == expected, (
        "the appender did not write the kind its own derivation returns")
    assert "fail_kind" not in pass_row, (
        "fail_kind was written on a PASS row -- omission is the honest encoding")
    assert "synthetic" not in pass_row


def test_10_synthetic_env_var_reaches_the_record_as_a_TYPED_field(monkeypatch, tmp_path):
    """The suffix stays for legacy miners, but the typed field is what a new consumer reads.

    MUTANT: keep only the text suffix -> RED. A miner that must grep-exclude a substring
    cannot aggregate, and that is why only 6 of 10,276 rows were ever countable as probes.
    """
    import json
    cla = _load("comp_log_auto_e42b", "comp_log_auto.py")
    (tmp_path / "org" / "mcp").mkdir(parents=True)
    (tmp_path / "org" / "mcp" / "comp-tool-runs.jsonl").write_text("", encoding="utf-8")
    monkeypatch.setenv("COMP_SYNTHETIC_FIXTURE", "1")
    cla._append_log(tmp_path, USAGE_TOOL, "io", USAGE_RC, "0.7.0_AE_CloudOps", "(no-TO)")
    row = json.loads((tmp_path / "org" / "mcp" / "comp-tool-runs.jsonl").read_text(encoding="utf-8").strip())
    assert row["synthetic"] is True
    assert row["fail_kind"] == oc.FK_NEGATIVE_CONTROL
    assert "SYNTHETIC TEST FIXTURE" in row["result"], (
        "the legacy suffix was dropped -- existing miners key on it; this must be additive")


if __name__ == "__main__":
    raise SystemExit(pytest.main([__file__, "-v"]))
