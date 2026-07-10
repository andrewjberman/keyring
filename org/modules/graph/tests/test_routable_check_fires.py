#!/usr/bin/env python3
"""comp-routable-check standing non-vacuity test: prove the REGISTERED-IMPLIES-REACHABLE gate FIRES.

Author: 3.0.0_SA_CVO~A. NFRA_TOOLPASS comp-routable-check (CTO GO 20260710T233905Z).

comp-routable-check FAILs when a tools_index tool is UNREACHABLE via comp-which -- either
ABSENT-FROM-PROVIDER or present with routable=False. Front-passed CLEAN and proven non-vacuous
in scratch (both FAIL branches bite), but that proof lived ONLY in a scratchpad -- the gate has
NO committed unit test of its fire (only .tools/comp-which-routing-test.py, a LIVE post-merge
oracle, not a unit test). Same class as the comp-manifest-check MC1 completeness family: a gate
whose fire is unproven in CI. This is the standing committed guard.

Each test monkeypatches `_load` to a SYNTHETIC (tools_index, caps, exempt) state and calls
`check()` -- so a future regression in the fire logic (`if routable: continue` /
`unreachable.append`) flips a fire assertion RED. Test-only; tool source unchanged.

bd-CLEAN: reads nothing (synthetic in-memory state); no bd, no data, no held path. Hermetic:
imports the tool module directly (via SourceFileLoader -- the tool is extensionless, so plain
spec_from_file_location returns a None loader), no CLI subprocess -> no pytest.ini bd-pythonpath.
"""
from __future__ import annotations

import importlib.machinery
import importlib.util
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[4]
_TOOL = _REPO / ".tools" / "comp-routable-check"
# the tool imports comp_capability_provider inside _load(); make the graph module importable
sys.path.insert(0, str(_REPO / "org" / "modules" / "graph"))


def _load_extensionless(name, path):
    """Import an extensionless executable: SourceFileLoader + spec_from_loader. Plain
    spec_from_file_location returns a None loader for a file with no .py suffix."""
    loader = importlib.machinery.SourceFileLoader(name, str(path))
    spec = importlib.util.spec_from_loader(name, loader)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    loader.exec_module(m)
    return m


M = _load_extensionless("comp_routable_check_sut", _TOOL)


class _Cap:
    """A capability_provider capability stand-in: check() reads .id / .routable / .kind."""
    def __init__(self, cid, routable, kind="surface"):
        self.id = cid
        self.routable = routable
        self.kind = kind


def _caps(*specs):
    return {s[0]: _Cap(*s) for s in specs}


_TARGET = "comp-real-target-zzz"      # a synthetic tools_index tool NOT in the EXCLUDE set


def test_routable_false_fires(monkeypatch):
    """A registered tool present in the provider with routable=False -> unreachable ROUTABLE=FALSE."""
    monkeypatch.setattr(M, "_load", lambda: ({_TARGET}, _caps((_TARGET, False, "surface")), {}))
    _targets, unreachable, _uncat, _exempt = M.check()
    assert (_TARGET, "ROUTABLE=FALSE", "surface") in unreachable, (
        f"routable=False did not fire ROUTABLE=FALSE; unreachable={unreachable}"
    )
    assert len(unreachable) == 1


def test_absent_from_provider_fires(monkeypatch):
    """A registered tool with NO provider capability -> unreachable ABSENT-FROM-PROVIDER."""
    monkeypatch.setattr(M, "_load", lambda: ({_TARGET}, {}, {}))   # caps empty -> absent
    _targets, unreachable, _uncat, _exempt = M.check()
    assert (_TARGET, "ABSENT-FROM-PROVIDER", "") in unreachable, (
        f"absent-from-provider did not fire; unreachable={unreachable}"
    )


def test_exempt_suppresses_with_a_reason(monkeypatch):
    """The declarative escape: routable=False BUT routing_exempt:<reason> -> exempted, NOT
    unreachable (an exemption is a visible fact on the record, never a silent pass)."""
    reason = "intentional: cross-surface aggregator, no single routing home"
    monkeypatch.setattr(
        M, "_load",
        lambda: ({_TARGET}, _caps((_TARGET, False, "surface")), {_TARGET: reason}))
    _targets, unreachable, _uncat, exempted = M.check()
    assert unreachable == [], f"an EXEMPT tool must not be unreachable; got {unreachable}"
    assert (_TARGET, reason) in exempted, f"exempt tool not reported on the record; exempted={exempted}"


def test_routable_target_is_reachable_baseline(monkeypatch):
    """NEGATIVE CONTROL: a routable registered tool does NOT fire. Without this, a gate that
    always reported unreachable would pass the fire tests above."""
    monkeypatch.setattr(M, "_load", lambda: ({_TARGET}, _caps((_TARGET, True, "surface")), {}))
    _targets, unreachable, _uncat, _exempt = M.check()
    assert unreachable == [], f"a routable tool must be reachable; got {unreachable}"


def test_excluded_run_primitives_are_not_targets(monkeypatch):
    """comp-grep/comp-glob/comp-which are run-primitives / the router itself -- excluded from
    targets, so even absent-from-provider they never fire. Pins the EXCLUDE-set behaviour."""
    ti = set(M.EXCLUDE) | {_TARGET}
    monkeypatch.setattr(M, "_load", lambda: (ti, _caps((_TARGET, True, "surface")), {}))
    targets, unreachable, _uncat, _exempt = M.check()
    assert not (set(M.EXCLUDE) & targets), "EXCLUDE run-primitives leaked into targets"
    assert unreachable == []
