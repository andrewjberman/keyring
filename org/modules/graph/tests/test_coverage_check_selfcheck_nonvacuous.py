#!/usr/bin/env python3
"""Standing neuter-audit: prove comp-coverage-check's selfcheck is NON-VACUOUS.

Author: 3.0.0_SA_CVO~A. CTO ruling 20260710T213553Z (NFRA_TOOLPASS).

WHY THIS EXISTS
---------------
A tool's own selfcheck passing is NOT proof its checkers work. comp-coverage-check's
`selfcheck` reported 17/17 GREEN while 6 of its 12 checkers could be fully neutered
(`return []`) WITHOUT the selfcheck noticing -- the injected fixtures were contaminated
(a single injection tripped several checkers), so no case ISOLATED the broken one. That
is the comp-deadgrant-M3 class one level up: the harness that validates the harness.

This meta-test converts "12/12 flip once" into "12/12 flip forever, gated". For each
checker, it neuters that checker (monkeypatch `_CHECKERS[name] -> return []`) and asserts
the selfcheck goes RED. If a future checker is added WITHOUT a dedicated isolating case,
its neuter will not flip the selfcheck and this test fails -- vacuity cannot silently
regress. A green selfcheck with N neuterable checkers is N/total VACUOUS.

This is a HARNESS test only: it exercises the selfcheck's own fixtures, never live AWS /
bd / the estate. bd-safe (ledger YAMLs + .tools/ filenames only).
"""
from __future__ import annotations

import importlib.util
import io
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import pytest

_MOD = Path(__file__).resolve().parent.parent / "comp_coverage_check.py"


def _load():
    spec = importlib.util.spec_from_file_location("ccc_under_test", _MOD)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


C = _load()
_CHECKER_NAMES = sorted(C._CHECKERS.keys())


def _run_selfcheck() -> int:
    """Run selfcheck, swallowing its stdout/stderr, return its exit code."""
    buf = io.StringIO()
    with redirect_stdout(buf), redirect_stderr(buf):
        return C.selfcheck(emit_json=False)


def test_baseline_selfcheck_is_green():
    """Sanity: the clean, un-neutered selfcheck passes (all isolated + injected cases hold)."""
    assert _run_selfcheck() == C.PASS


@pytest.mark.parametrize("checker", _CHECKER_NAMES)
def test_neutering_each_checker_flips_the_selfcheck(checker, monkeypatch):
    """THE NEUTER-AUDIT. Neuter one checker -> the selfcheck MUST go RED.

    If this fails for `checker`, that checker is VACUOUSLY covered: the selfcheck does not
    have a case that isolates it, so a broken `checker` would ship GREEN. The remedy is a
    dedicated ISOLATED fixture in selfcheck() that trips ONLY `checker` (see the iso-N cases).
    """
    # neuter the checker in the live _CHECKERS registry that run_gate dispatches through
    monkeypatch.setitem(C._CHECKERS, checker, lambda led, **_: [])
    rc = _run_selfcheck()
    assert rc != C.PASS, (
        f"VACUOUS: neutering `{checker}` left the selfcheck GREEN (rc={rc}). No case isolates it -- "
        f"a broken `{checker}` would ship undetected. Add a dedicated ISOLATED fixture that trips ONLY it."
    )


def test_twelve_of_twelve_are_independently_exercised(monkeypatch):
    """Aggregate the audit: EVERY checker must be independently exercised (0 vacuous).

    This is the acceptance bar CVO committed to CTO (213553Z): 12/12 flip, 0 vacuous.
    """
    vacuous = []
    for name in _CHECKER_NAMES:
        orig = C._CHECKERS[name]
        C._CHECKERS[name] = lambda led, **_: []
        try:
            if _run_selfcheck() == C.PASS:
                vacuous.append(name)
        finally:
            C._CHECKERS[name] = orig
    assert not vacuous, (
        f"{len(vacuous)}/{len(_CHECKER_NAMES)} checkers are VACUOUSLY covered (selfcheck green while broken): "
        f"{vacuous}. Each needs a dedicated ISOLATED selfcheck fixture."
    )
