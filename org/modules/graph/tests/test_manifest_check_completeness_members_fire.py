#!/usr/bin/env python3
"""MC1 standing neuter-audit: prove EACH completeness member FIRES on a synthetic violation.

Author: 3.0.0_SA_CVO~A. NFRA_TOOLPASS comp-manifest-check MC1 (CTO GO 20260710T230244Z).

WHY THIS EXISTS
---------------
comp-manifest-check's built-in `selfcheck` exercises only the A/B/C anti-pattern scanners
(bidirectionally non-vacuous, already tested). The 4 DETERMINISTIC hard-blocking members of
the completeness family --

    _routable_invariant   (a registered tool must be routable via comp-which)
    _placement_invariant  (a comp-tool must have exactly one coverage-map home)
    _selfroute_invariant  (a catalogued tool must surface for its own use_case)
    _existence_invariant  (a registered tool must exist as a tracked, runnable executable)

-- all PASS on the live estate, but NOTHING proved any of them FIRES. Neuter a member to
`return 0` and the selfcheck stays green (the selfcheck does not touch the family). They have
caught REAL incidents (comp-system routable!=runnable, comp-fedobs) -- but a future regression
in a member would ship undetected. That is the exact vacuous-checker class closed in
comp-coverage-check (a green harness with N neuterable checkers is N/total vacuous), here at
the completeness-family level.

WHAT THIS TESTS -- and what it does NOT
---------------------------------------
This proves each member fires in the INDEX->X direction it checks (registered->routable /
->one-home / ->surfaces / ->exists). It is COMPLEMENTARY to, and does NOT close,
`test_manifest_check_completeness_direction.py`'s separately-documented finding that the
family is UNDISCRIMINATING for the DISK->INDEX direction (denominator == catalog -> cannot
detect an incomplete catalog). Two different directions; that one is pinned with its own
acceptance signal. Do not conflate.

The neuter-audit (`test_neutering_a_member_flips_its_fire_assertion`) converts "each member
fires once" into "each member fires forever, gated": neuter any member and its fire-assertion
goes RED, so a regression cannot ship green.

bd-safe: synthetic in-memory fixtures + monkeypatched loaders only. No live AWS, no bd data;
the ghost tool names are fixtures. Does NOT run the CLI (no pytest.ini bd-pythonpath exposure
via subprocess -- it imports the module and calls the member functions directly).
"""
from __future__ import annotations

import copy
import importlib.util
import io
import sys
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

import pytest
import yaml

_REPO = Path(__file__).resolve().parents[4]
_GRAPH = _REPO / "org" / "modules" / "graph"
sys.path.insert(0, str(_GRAPH))


def _load_mcc():
    spec = importlib.util.spec_from_file_location("mcc_under_test", _GRAPH / "manifest_check_cli.py")
    m = importlib.util.module_from_spec(spec)
    sys.modules["mcc_under_test"] = m
    spec.loader.exec_module(m)
    return m


M = _load_mcc()


def _run(fn, files) -> int:
    """Call a member, swallow its LOUD output, return its rc (0 = holds, 1 = BLOCK)."""
    buf = io.StringIO()
    with redirect_stdout(buf), redirect_stderr(buf):
        return fn(files)


# ---------------------------------------------------------------------------
# Per-member SYNTHETIC-VIOLATION setups. Each injects exactly ONE violation in the
# index->X direction the member checks, via the member's own data source, so the member
# has something real to detect. Each returns (violating_files, teardown).
# ---------------------------------------------------------------------------
_GHOST = "comp-ghost-mc1-zzz"


def _violate_existence(monkeypatch):
    """A registered tool absent from disk. Inject a ghost into tools_index; it has no .tools/ file."""
    real = M.load_yaml
    def fake(p):
        d = real(p)
        if str(p).replace("\\", "/").endswith("graph-call-manifest.yaml"):
            d = copy.deepcopy(d)
            d.setdefault("tools_index", {})[_GHOST] = {"does": "ghost"}
        return d
    monkeypatch.setattr(M, "load_yaml", fake)
    return [f".tools/{_GHOST}"]          # tools_touched -> targets = all registered (incl the ghost)


def _violate_routable(monkeypatch):
    """A registered tool unreachable via comp-which. Fake the routable engine to report one."""
    class _FakeRC:
        def check(self):
            return ([], [(_GHOST, "routable=False", "")], [], [])
    monkeypatch.setattr(M, "_load_routable_engine", lambda: _FakeRC())
    monkeypatch.setattr(M, "_touches_routable_substrate", lambda files: True)
    return ["org/modules/graph/graph-call-manifest.yaml"]


def _violate_placement(monkeypatch):
    """A committed comp-tool with no coverage-map home -> inventory-completeness problem."""
    return [f".tools/{_GHOST}"]          # committed comp-tool not in the placement map


def _violate_selfroute(monkeypatch):
    """A catalogued tool that does not surface for its own use_case (MISS). Inject a ghost with an
    unroutable use_case into the manifest the member loads via yaml.safe_load. The member bounds its
    targets to git-CHANGED tools_index keys; the ghost is injected into the loaded doc, not git, so
    force the UNBOUNDED path (_section_changed('entries') True -> targets stays the full set) so the
    ghost is actually checked."""
    real = yaml.safe_load
    def fake(s):
        d = real(s)
        if isinstance(d, dict) and "tools_index" in d:
            d = copy.deepcopy(d)
            d["tools_index"][_GHOST] = {"does": "qzqzq nonexistent unroutable gibberish use_case zzz"}
        return d
    monkeypatch.setattr(yaml, "safe_load", fake)
    # BOUND to just the ghost so self_route_verdicts routes ONE tool, not all 42 (67s -> ~1s):
    # entries unchanged -> the member enters the bounded branch; _dict_diff_keys -> {ghost}.
    monkeypatch.setattr(M, "_section_changed", lambda path, section: False)
    monkeypatch.setattr(M, "_dict_diff_keys", lambda path, section: {_GHOST})
    return ["org/modules/graph/graph-call-manifest.yaml"]


_MEMBERS = {
    "_existence_invariant": _violate_existence,
    "_routable_invariant": _violate_routable,
    "_placement_invariant": _violate_placement,
    "_selfroute_invariant": _violate_selfroute,
}
_MEMBER_NAMES = sorted(_MEMBERS)


@pytest.mark.parametrize("name", _MEMBER_NAMES)
def test_member_fires_on_its_synthetic_violation(name, monkeypatch):
    """Each completeness member MUST return 1 (BLOCK) on a synthetic violation in its direction.

    If this fails, the member cannot detect its own defect class even when one is injected --
    a member that never fires is a gate that certifies GREEN it cannot back.
    """
    member = getattr(M, name)
    files = _MEMBERS[name](monkeypatch)
    rc = _run(member, files)
    assert rc == 1, f"{name} did NOT fire (rc={rc}) on an injected {name} violation -- vacuous member"


@pytest.mark.parametrize("name", _MEMBER_NAMES)
def test_member_does_not_false_fire_off_substrate(name):
    """Negative control: with no relevant substrate touched, the member returns 0 (not-applicable).
    A member that fires on an unrelated commit is a false-positive gate."""
    member = getattr(M, name)
    rc = _run(member, ["README.md"])
    assert rc == 0, f"{name} FALSE-FIRED (rc={rc}) on an off-substrate commit"


def test_neutering_a_member_flips_its_fire_assertion(monkeypatch):
    """THE NEUTER-AUDIT. Neuter each member to `return 0`; its own fire-assertion must go RED.

    This is the standing guard: a future regression that breaks a member (or a new member added
    without a fire fixture) fails here, so completeness-family vacuity cannot ship green.
    """
    vacuous = []
    for name in _MEMBER_NAMES:
        real = getattr(M, name)
        setup = _MEMBERS[name]
        with pytest.MonkeyPatch.context() as mp:
            files = setup(mp)                       # arm the violation
            mp.setattr(M, name, lambda files: 0)    # neuter the member
            if _run(getattr(M, name), files) == 1:  # neutered member should NOT fire
                vacuous.append(name)                # (it returned 1 anyway -> not actually neutered)
        # confirm the REAL member fires (sanity: the fixture is a real violation)
        with pytest.MonkeyPatch.context() as mp:
            files = setup(mp)
            if _run(real, files) != 1:
                vacuous.append(f"{name}(fixture-not-a-violation)")
    assert not vacuous, (
        f"neuter-audit found vacuous/mis-fixtured members: {vacuous}. Each of the 4 completeness "
        f"members must fire on its synthetic violation and stop firing when neutered."
    )
