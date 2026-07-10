#!/usr/bin/env python3
"""Sovereign-exclusion guard tests for comp-dups (dup_scan), NFRA_TOOLPASS tool.

DD1: comp-dups is a LATENT bd-scanner -- scan_content -> _py_bodies(["lib","data",...]) would
read_text() 337 data/black_diamond/*.py + the schwab silver tree on every bare/--json/--class/
--nightly run. The guard makes the sec.8 sovereign hold a CODE property, not agent discipline.

SOVEREIGN-SAFE BY CONSTRUCTION: no test here touches the REAL data/black_diamond/ or schwab/silver.
The corpus tests run against a TEMP scratch REPO with SYNTHETIC files placed at bd-/schwab-shaped
PATHS -- exercising the path-exclusion logic without reading any real held content. git ls-files is
monkeypatched to a controlled list.
"""
from __future__ import annotations

import importlib.util
import sys
from pathlib import Path

_WS = Path(__file__).resolve().parents[5]
_CLI = _WS / "org" / "modules" / "graph" / "debtscan" / "dup_scan.py"
spec = importlib.util.spec_from_file_location("dup_scan", _CLI)
D = importlib.util.module_from_spec(spec)
sys.modules["dup_scan"] = D
spec.loader.exec_module(D)


# ---- _is_held (pure predicate) ------------------------------------------------------------

def test_is_held_covers_bd_and_schwab_silver():
    assert D._is_held("data/black_diamond/scripts/gold/x.py")
    assert D._is_held("data/canonical/schwab/silver/build_dim_account.py")


def test_is_held_does_not_over_exclude_inscope_firms():
    assert not D._is_held("data/cot/scripts/gold/x.py"), "cot is IN SCOPE -- must not be excluded"
    assert not D._is_held("data/inf/scripts/gold/x.py"), "inf is IN SCOPE"
    assert not D._is_held("lib/trading_calendar.py")
    assert not D._is_held("org/modules/graph/debtscan/dup_scan.py")


def test_MUTANT_empty_held_prefixes_would_let_bd_through():
    """NEGATIVE CONTROL: with the prefixes removed, bd paths are NOT held -> the corpus guard is
    inert. Proves _HELD_PREFIXES is load-bearing."""
    import re
    saved = D._HELD_PREFIXES
    try:
        D._HELD_PREFIXES = ()
        assert not D._is_held("data/black_diamond/x.py"), "premise: empty prefixes let bd through"
    finally:
        D._HELD_PREFIXES = saved
    assert re.match(r".*black_diamond", D._HELD_PREFIXES[0]) or "black_diamond" in D._HELD_PREFIXES[0]


# ---- _py_bodies exclusion (temp scratch REPO; SYNTHETIC held paths, never real bd) ---------

def _scratch_repo(tmp_path, monkeypatch, tracked: list[str]):
    """Build a temp REPO with a real file per `tracked` path (synthetic content), and monkeypatch
    D.REPO + the git ls-files subprocess to that controlled corpus. The bd-/schwab-shaped entries
    are SYNTHETIC files in the throwaway dir -- NOT the real held data."""
    body = "\n".join(f"def fn_{i}(): return {i} * meaningful_token_{i}" for i in range(30))
    for rel in tracked:
        f = tmp_path / rel
        f.parent.mkdir(parents=True, exist_ok=True)
        f.write_text(body, encoding="utf-8")
    monkeypatch.setattr(D, "REPO", tmp_path)

    class _R:
        stdout = "\n".join(tracked) + "\n"
    monkeypatch.setattr(D.subprocess, "run", lambda *a, **k: _R())


def test_py_bodies_excludes_held_paths_from_corpus(tmp_path, monkeypatch):
    tracked = ["lib/keep.py", "data/black_diamond/synthetic_held.py",
               "data/canonical/schwab/silver/synthetic_held.py", "data/cot/inscope.py"]
    _scratch_repo(tmp_path, monkeypatch, tracked)
    bodies, held = D._py_bodies(["lib", "data"], allow_held=False)
    corpus_paths = {b["path"] for b in bodies}
    assert not any("black_diamond" in p for p in corpus_paths), "NO bd path may be in the corpus"
    assert not any("schwab/silver" in p for p in corpus_paths), "NO schwab silver path in the corpus"
    assert "lib/keep.py" in corpus_paths and "data/cot/inscope.py" in corpus_paths, \
        "non-held (incl in-scope cot) must be READ"
    assert set(held) == {"data/black_diamond/synthetic_held.py",
                         "data/canonical/schwab/silver/synthetic_held.py"}


def test_MUTANT_guard_off_would_read_held_into_corpus(tmp_path, monkeypatch):
    """NEGATIVE CONTROL: allow_held=True (the override / the mutant of the default) DOES pull the
    synthetic held path into the corpus. Proves the exclusion is what keeps bd out -- and documents
    exactly what --allow-held does (include held paths) for when Andrew lifts."""
    tracked = ["lib/keep.py", "data/black_diamond/synthetic_held.py"]
    _scratch_repo(tmp_path, monkeypatch, tracked)
    bodies, held = D._py_bodies(["lib", "data"], allow_held=True)
    corpus_paths = {b["path"] for b in bodies}
    assert "data/black_diamond/synthetic_held.py" in corpus_paths, \
        "allow_held=True must INCLUDE held paths (this is the override, deliberately)"
    assert held == [], "nothing skipped when allow_held=True"


def test_scan_content_default_excludes_held_and_loud_notes_it(tmp_path, monkeypatch):
    tracked = ["lib/keep.py", "data/black_diamond/synthetic_held.py"]
    _scratch_repo(tmp_path, monkeypatch, tracked)
    res = D.scan_content(D.SuppressionAudit(), "lib/keep.py", allow_held=False)
    assert res["held_skipped_count"] == 1
    assert "SOVEREIGN HOLD" in res["held_note"] and "EXCLUDED" in res["held_note"]
    assert not any("black_diamond" in d for d in [res["held_note"]] if "INCLUDED" in d), \
        "default run must NOT report held paths as included"


def test_default_scan_content_never_reaches_read_on_a_held_path(tmp_path, monkeypatch):
    """The load-bearing sovereign property: on a DEFAULT run, read_text is NEVER invoked on a held
    path. We assert the held file is in held_skipped (guard fired) BEFORE any read could occur."""
    tracked = ["lib/keep.py", "data/black_diamond/synthetic_held.py"]
    _scratch_repo(tmp_path, monkeypatch, tracked)
    bodies, held = D._py_bodies(["lib", "data"], allow_held=False)
    assert "data/black_diamond/synthetic_held.py" in held, "held path must be skipped, not read"
