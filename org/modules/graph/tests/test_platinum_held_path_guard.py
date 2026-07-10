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


_HELD_BD = "data/black_diamond/scripts/gold/G_00_synthetic.py"
_NONHELD_INF = "data/inf/scripts/gold/INF_D_04.synthetic.py"
_KEY = "platinum/firm/mix_summary.json"


def test_guard_prevents_read_on_a_held_bd_path(monkeypatch):
    """THE GUARD BITES: on a held bd path, read_text is NEVER called (no held read).

    This assertion is the non-vacuity proof: delete the `_held_path_hit` guard and read_text
    gets called on the bd path -> `calls` is non-empty -> this test goes RED.
    """
    calls = []

    def fake_read_text(self, *a, **k):
        calls.append(str(self).replace("\\", "/"))
        return "def anything():\n    pass\n"

    monkeypatch.setattr(pathlib.Path, "read_text", fake_read_text)
    out = M._find_producer_function(_FakeSio(_HELD_BD), _KEY)
    assert out == "", "held gold script must degrade to metadata-only (empty producer fn)"
    assert calls == [], (
        f"SOVEREIGN VIOLATION: read_text was called on a HELD path {calls} -- the guard did not "
        f"bite. A held bd gold script's CONTENT was read to name a producer fn."
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
    """The load-bearing property: _held_path_hit NEVER opens a file, so calling the guard
    cannot itself read held content."""
    def boom(self, *a, **k):
        raise AssertionError("_held_path_hit opened a file -- it must be a pure string check")

    monkeypatch.setattr(pathlib.Path, "read_text", boom)
    monkeypatch.setattr(pathlib.Path, "open", boom)
    assert _TG._held_path_hit(_HELD_BD) is True, "bd gold path must be held"
    assert _TG._held_path_hit("schwab/silver/x.py") is True, "schwab silver must be held"
    assert _TG._held_path_hit(_NONHELD_INF) is False, "inf gold path must NOT be held"
    assert _TG._held_path_hit(None) is False, "None path is not held (no crash)"
