#!/usr/bin/env python3
"""comp-platinum sovereign guard: _find_producer_function must NEVER read a held gold script.

Author: 3.0.0_SA_CVO~A. NFRA_TOOLPASS comp-platinum (CTO GO 20260710T233222Z, gated fix).

THE DEFECT (source-established, NOT run on bd): comp-platinum's `--firm` defaults to bd
(platinum_cli.py:146 `... or "bd"`), so a BARE `page`/`reverse` traces the bd gold tree and
reaches `_find_producer_function` (:308), which did an UNGUARDED
`Path(sio.file_path).read_text(...)` to name the producer function -- reading
`data/black_diamond/scripts/gold/*.py` CONTENT with no bd argument at all (a held read).

THE FIX (CTO, gated): the canonical shared chokepoint before the read --
    if _held_path_hit(getattr(sio, "file_path", None)):
        return ""        # bd/schwab held: metadata-only; the trace still shows the script NAME.
`_held_path_hit` (trace_graph.py) is a PURE str check -- it never opens the file, so the guard
itself cannot read held content.

THIS TEST -- bidirectional, fully SYNTHETIC (read_text is mocked; NO real bd file is ever read):
  * the guard BITES: on a held (bd) path, read_text is NEVER called (the held read is prevented).
    This assertion flips RED the instant the guard is removed -> it is the non-vacuity proof.
  * the guard does NOT OVER-FIRE: on a non-held (inf) path, read_text IS called and the producer
    fn is still named -- the fix degrades ONLY held scripts.
  * `_held_path_hit` never opens a file (the load-bearing property that the guard is not itself a
    held read) -- proven by making Path.read_text/open raise if called.

bd-safe: no real read of any data/black_diamond file (read_text mocked); the paths are strings.
Hermetic: imports the module, no CLI subprocess -> no pytest.ini bd-pythonpath landmine, and it
NEVER runs comp-platinum bare/--firm bd (which would read held content).
"""
from __future__ import annotations

import importlib.util
import pathlib
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[4]
_GRAPH = _REPO / "org" / "modules" / "graph"
sys.path.insert(0, str(_GRAPH))


def _load(name, filename):
    spec = importlib.util.spec_from_file_location(name, _GRAPH / filename)
    m = importlib.util.module_from_spec(spec)
    sys.modules[name] = m
    spec.loader.exec_module(m)
    return m


# trace_graph must load first (platinum_cli imports _held_path_hit from it)
_TG = _load("trace_graph_platinum_sut", "trace_graph.py")
M = _load("platinum_cli_sut", "platinum_cli.py")


class _FakeSio:
    """Minimal ScriptIO stand-in: only `.file_path` is read by _find_producer_function."""
    def __init__(self, file_path):
        self.file_path = file_path


_BD_PATH = "data/black_diamond/scripts/gold/G_00_synthetic.py"
_NONHELD_INF = "data/inf/scripts/gold/INF_D_04.synthetic.py"
_KEY = "platinum/firm/mix_summary.json"


# F11 REPAIR (TO ADHOC.graph-tests-hygiene-f11-family, 0.8.0_AE_CloudComp~D): the hold-era
# assertions (bd held-by-default) went stale-red after the retraction landed
# (SOVEREIGN_HELD_PATHS=() @7a07814b94). TRUTH DETERMINATION at HEAD: LIFTED, mechanism
# retained -- platinum_cli.py:313 still guards via _held_path_hit, whose predicate
# (sovereign_held.is_held_path) resolves the governance set at CALL time; the set is empty.
# The guard mechanism is now tested via an INJECTED synthetic marker patched into the
# predicate's own defining globals; governance values are never re-asserted.
_SYNTH_ZONE = "synthetic_held_zone_f11"
_SYNTH_HELD = _SYNTH_ZONE + "/scripts/gold/G_00_synthetic.py"


def _inject(monkeypatch):
    """Arm the mechanism in BOTH sovereign_held module instances. trace_graph binds the predicate
    relatively when package-imported and bare when standalone (trace_graph.py:27-32), and
    platinum_cli's guard (:308) imports the PACKAGE trace_graph at call time -- so the standalone
    _TG instance this test loaded and the package instance the guard consults are two distinct
    module objects over one file. Patching only one leaves the other un-armed (measured: the
    guard test failed with a single-instance patch). is_held_path reads SOVEREIGN_HELD_PATHS
    from its defining module's globals at call time; substring semantics (sovereign_held.py:80)
    make the marker match by construction."""
    import importlib
    if str(_REPO) not in sys.path:
        sys.path.insert(0, str(_REPO))
    _sh_pkg = importlib.import_module("org.modules.graph.sovereign_held")
    monkeypatch.setattr(_sh_pkg, "SOVEREIGN_HELD_PATHS", (_SYNTH_ZONE + "/",))
    monkeypatch.setitem(_TG._shared_is_held_path.__globals__,
                        "SOVEREIGN_HELD_PATHS", (_SYNTH_ZONE + "/",))


def test_bd_path_is_read_post_lift(monkeypatch):
    """POST-LIFT TRUTH: nothing is held, so a bd gold path IS read and its producer fn named --
    the read HAPPENS now (this inverts the hold-era assertion, deliberately)."""
    calls = []

    def fake_read_text(self, *a, **k):
        calls.append(str(self).replace("\\", "/"))
        return "def synthetic_producer():\n    s3.put_object(Key='mix_summary.json')\n"

    monkeypatch.setattr(pathlib.Path, "read_text", fake_read_text)
    out = M._find_producer_function(_FakeSio(_BD_PATH), _KEY)
    assert out == "synthetic_producer", (
        f"post-lift: a bd gold script must be read + its producer fn named like any other, got {out!r}"
    )
    assert len(calls) == 1, f"expected exactly one read of the bd path post-lift, got {calls}"


def test_guard_prevents_read_under_injected_hold(monkeypatch):
    """THE GUARD BITES under injection: on a path under the INJECTED marker, read_text is NEVER
    called. Non-vacuity: neuter the :313 guard and the read happens -> this test goes RED."""
    _inject(monkeypatch)
    calls = []

    def fake_read_text(self, *a, **k):
        calls.append(str(self).replace("\\", "/"))
        return "def anything():\n    pass\n"

    monkeypatch.setattr(pathlib.Path, "read_text", fake_read_text)
    out = M._find_producer_function(_FakeSio(_SYNTH_HELD), _KEY)
    assert out == "", "an injected-held script must degrade to metadata-only (empty producer fn)"
    assert calls == [], (
        f"MECHANISM FAILURE: read_text was called on an injected-held path {calls} -- "
        f"the :313 chokepoint did not bite."
    )


def test_guard_does_not_overfire_on_a_non_held_inf_path(monkeypatch):
    """NEGATIVE CONTROL: on a non-held (inf) path the read HAPPENS and the fn is named.

    The fix must degrade ONLY held scripts; over-firing on inf would silently blank every
    non-held producer-fn name.
    """
    calls = []

    def fake_read_text(self, *a, **k):
        calls.append(str(self).replace("\\", "/"))
        return "def synthetic_producer():\n    s3.put_object(Key='mix_summary.json')\n"

    monkeypatch.setattr(pathlib.Path, "read_text", fake_read_text)
    out = M._find_producer_function(_FakeSio(_NONHELD_INF), _KEY)
    assert out == "synthetic_producer", (
        f"non-held inf script must still be read + its producer fn named, got {out!r}"
    )
    assert len(calls) == 1 and "data/inf" in calls[0], (
        f"expected exactly one read of the inf path, got {calls}"
    )


def test_held_path_hit_is_a_pure_string_check_never_opens(monkeypatch):
    """The load-bearing property (unchanged by the lift): _held_path_hit NEVER opens a file, so
    calling the guard cannot itself read held content. Values updated to post-lift truth +
    injection: real trees are NOT held; the injected marker IS -- all decided without a file op."""
    _inject(monkeypatch)

    def boom(self, *a, **k):
        raise AssertionError("_held_path_hit opened a file -- it must be a pure string check")

    monkeypatch.setattr(pathlib.Path, "read_text", boom)
    monkeypatch.setattr(pathlib.Path, "open", boom)
    assert _TG._held_path_hit(_SYNTH_HELD) is True, "injected marker must be held (mechanism)"
    assert _TG._held_path_hit(_BD_PATH) is False, "post-lift: bd gold path is NOT held"
    assert _TG._held_path_hit(_NONHELD_INF) is False, "inf gold path must NOT be held"
    assert _TG._held_path_hit(None) is False, "None path is not held (no crash)"
