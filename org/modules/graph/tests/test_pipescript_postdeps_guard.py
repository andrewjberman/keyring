"""Dial F1 (SEV-HIGH) -- the comp-pipescript postdeps two-half guard, incident-as-fixture.

DIAL_RECORD_comp-pipescript_20260804.md F1 (@7900435cb, amended @2c9b1bb9c), built under
TO ADHOC.comp-pipescript-postdeps-f1-guard (2.0.0_SA_COO -> 0.8.0_AE_CloudComp~D):

  (a) unknown script_id returned rc=0 "No dependencies declared" -- byte-identical to a
      known-clean script, ON THE MODE THAT EXISTS BECAUSE OF THE $22M INCIDENT.
  (b) flagless postdeps silently defaulted to bd (the silent-tree-default class the 07-30
      stub killed for the io family).
  THE COMPOSITION (flagless + typo'd script) = double false-clean on the $22M guard.
  Per CVO (RAVC close 070735Z) the composition IS the load-bearing test -- this file is it.

Half (b) resolution is NAMED-DEFAULT-LOUD, not required-flag: the live-caller inventory found
3 dispatch-gate call sites (bd/cot/inf gold_dispatch check_partial_deps) invoking postdeps
flagless with stdout-grep parsing and rc+stderr swallowed -- a flagless rc=2 refusal would
silently vacuate the WORKING bd $22M-class gate (empty stdout = zero BLOCKING lines = pass),
the exact silent caller-break the TO forbids. With half (a) live, flagless+unknown still dies
at rc=2, so the composition is closed either way.

The validation universe is DERIVED at runtime (tree DAG script ids UNION deps-config keys) --
predicate-not-roster; build_canonical_prices_v2 (deps key, NOT a tree id) pins the UNION.

Exercises the REAL engine (subprocess), read-only, sovereign-trivial.
# rail-checked: assurance fixture for the postdeps guard (dial F1, incident-as-fixture law)
Author: 0.8.0_AE_CloudComp~D, 2026-08-04.
"""
from __future__ import annotations

import os
import subprocess
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_WS = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(_HERE))))
_CLI = os.path.join(_WS, "org", "modules", "graph", "pipeline_cli.py")

UNKNOWN = "ZZZ_NO_SUCH_SCRIPT.py"          # resolves to id 'zzz_no_such_script' -- in NO tree
KNOWN_NO_DEPS = "A_00"                     # real bd tree id, NO declared deps in the yaml
KNOWN_WITH_DEPS = "build_canonical_prices" # bd deps key (post_steps) -- NOT a bd tree DAG id
                                           # (pins the scripts-UNION-deps-keys universe)


def _postdeps(*args: str):
    r = subprocess.run([sys.executable, _CLI, "postdeps", *args], cwd=_WS,
                       capture_output=True, text=True, timeout=120)
    return r.returncode, r.stdout + r.stderr


def test_composition_flagless_unknown_is_refused_rc2():
    """THE COMPOSITION (dial F1): flagless + typo'd script must NEVER read as clean.
    Pre-fix: rc=0 'No dependencies declared' from a silently-defaulted bd config."""
    rc, out = _postdeps(UNKNOWN)
    assert rc == 2, f"composition (flagless+unknown) must be REFUSED rc=2, got rc={rc}"
    assert "No dependencies declared" not in out, \
        "the false-clean string must NOT appear for an unknown script id"
    assert "REFUSED" in out, "refusal must be loud and named"


def test_unknown_script_with_firm_refused_naming_tree_and_universe():
    """Half (a): unknown id under an explicit --firm -> rc=2 naming the tree searched and
    the universe size (print the denominator)."""
    rc, out = _postdeps(UNKNOWN, "--firm", "bd")
    assert rc == 2, f"unknown script id must be REFUSED rc=2, got rc={rc}"
    assert "bd" in out, "refusal must name the tree searched"
    assert "universe" in out.lower(), "refusal must name the validation universe"
    assert any(ch.isdigit() for ch in out), "refusal must print the universe size (denominator)"
    assert "No dependencies declared" not in out


def test_known_tree_script_with_no_deps_still_answers_rc0():
    """DISCRIMINATION: a script that EXISTS in the tree but has no declared deps is a TRUE
    no-deps answer -- rc=0 must be preserved (the guard fires on unknown, not on empty)."""
    rc, out = _postdeps(KNOWN_NO_DEPS, "--firm", "bd")
    assert rc == 0, f"known tree script with no declared deps must stay rc=0, got rc={rc}"
    assert "No dependencies declared" in out


def test_deps_key_not_in_tree_dag_is_still_known():
    """UNION pin: build_canonical_prices is a deps-config key but NOT a tree DAG id.
    A tree-ids-only universe would refuse it -- the universe must be scripts UNION deps keys."""
    rc, out = _postdeps(KNOWN_WITH_DEPS, "--firm", "bd")
    assert rc == 0, f"a declared deps key must never be refused as unknown, got rc={rc}"
    assert "[BLOCKING] Must run:" in out, \
        "declared post-steps must still print (the live bd dispatch gate greps this line)"


def test_flagless_default_is_named_loud():
    """Half (b): flagless with a bare id still answers from bd, but the default is NAMED
    LOUD in the output -- never silent (pre-fix: bare '[bd]' banner, no default notice)."""
    rc, out = _postdeps(KNOWN_NO_DEPS)
    assert rc == 0, f"flagless known-bd-script must still answer (live callers), got rc={rc}"
    assert "DEFAULT" in out, "the defaulted tree must be announced loud, never silent"
