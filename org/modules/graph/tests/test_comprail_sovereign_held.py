#!/usr/bin/env python3
"""GG1 regression: _comprail.gitignore_aware_files EXCLUDES sovereign-held prefixes by default.

comp-grep/comp-glob READ every file in the working set gitignore_aware_files returns. With an
empty/broad pathspec that set included the section-8 held trees (data/black_diamond/, canonical
schwab silver), so a bare `comp-grep foo` silently READ bd source (GG1). The chokepoint fix
excludes held prefixes BY DEFAULT (string-prefix predicate -- it never opens a held file), returns
a LOUD note (an excluded held path is NOT 'confirmed absent'), and honors an audited
--include-held directed override. data/inf + data/cot are in-scope firms -- NOT excluded.

bd-SAFE: builds a SYNTHETIC scratch git repo with bd-SHAPED PATHS (fake one-line files), never real
data/black_diamond. The guard decides by PATH STRING, so no held file is ever opened by these tests.
"""
from __future__ import annotations

import subprocess
import sys
from pathlib import Path

import pytest

_TOOLS = Path(__file__).resolve().parents[4] / ".tools"
sys.path.insert(0, str(_TOOLS))
import _comprail  # noqa: E402

_HELD = ["data/black_diamond/scripts/gold/synth.py",
         "data/canonical/schwab/silver/synth.py"]
_INSCOPE = ["data/inf/scripts/gold/synth.py",
            "data/cot/scripts/gold/synth.py",
            "src/app.py"]


@pytest.fixture
def repo(tmp_path) -> Path:
    subprocess.run(["git", "init", "-q"], cwd=tmp_path, check=True)
    for rel in _HELD + _INSCOPE:
        p = tmp_path / rel
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text("SENTINEL = 1\n", encoding="utf-8")
    subprocess.run(["git", "add", "-A"], cwd=tmp_path, check=True)
    return tmp_path


def _norm(fs):
    return {f.replace("\\", "/") for f in fs}


def test_default_excludes_held_keeps_inscope_and_notes_it(repo):
    with _armed():
        files, note, err = _comprail.gitignore_aware_files(str(repo), [])
        assert err is None
        got = _norm(files)
        for h in _HELD:
            assert h not in got, f"held path {h} must be EXCLUDED by default"
        for k in _INSCOPE:
            assert k in got, f"in-scope path {k} must remain (data/inf + data/cot are in-scope)"
        assert note and "EXCLUDED" in note and "not confirmed absent" in note, \
            f"a LOUD exclusion note is mandatory; got {note!r}"


def test_include_held_returns_held_with_loud_override_warn(repo):
    with _armed():
        files, note, err = _comprail.gitignore_aware_files(str(repo), [], include_held=True)
        assert err is None
        got = _norm(files)
        for h in _HELD:
            assert h in got, f"--include-held must RETURN {h}"
        assert note and "OVERRIDE" in note and "--include-held" in note, \
            f"--include-held must WARN loudly (audit); got {note!r}"


def test_pathspec_naming_held_is_loud_not_a_silent_zero(repo):
    with _armed():
        files, note, err = _comprail.gitignore_aware_files(str(repo), ["data/black_diamond"])
        assert err is None
        assert _norm(files) == set(), "a held-directed pathspec returns 0 files by default"
        assert note and "NOT searched" in note and "--include-held" in note, \
            "a held-directed miss must be a LOUD 'NOT searched', never a silent 0 (that would LIE)"


def test_inscope_pathspec_emits_no_held_note(repo):
    files, note, err = _comprail.gitignore_aware_files(str(repo), ["data/inf"])
    assert err is None and note is None, "an in-scope search must not emit a held note"
    assert "data/inf/scripts/gold/synth.py" in _norm(files)


def test_mutant_disabling_exclusion_regresses(repo, monkeypatch):
    """section-2a: with the held predicate mutated OFF, the default working set REGAINS the held
    paths -> the exclusion is load-bearing."""
    monkeypatch.setattr(_comprail, "_is_held", lambda p: False)
    files, note, err = _comprail.gitignore_aware_files(str(repo), [])
    got = _norm(files)
    assert all(h in got for h in _HELD), "mutant proof: without the predicate, held paths return (RED)"
    assert note is None


def test_markers_name_the_section8_held_prefixes():
    with _armed():
        assert "data/black_diamond/" in _comprail.HELD_PREFIXES
        assert any("schwab/silver" in p for p in _comprail.HELD_PREFIXES)


# ---------------------------------------------------------------------------
# RETRACTION-AWARE MECHANISM TESTING (2026-07-22).
# 1.0.0_SA_CTO lifted _comprail's hold on 2026-07-14 (HELD_PREFIXES = ()) executing Andrew's
# retraction -- correctly: machinery kept, tuple emptied, Andrew quoted verbatim in-file. These
# tests were never brought with it, so they asserted the hold was ARMED and went red the same day.
# Nobody saw it: pytest collection was aborting from 07-14 too, so this suite ran ZERO tests for
# 8 days.
# A test asserting a prohibition is a RATCHET against its own retraction -- the red reads as "the
# lift broke something", and the cheapest repair is to re-arm the hold. So the assertions are not
# deleted: they exercise the MECHANISM under a DECLARED hold, which also proves re-arming works.
# ---------------------------------------------------------------------------
import contextlib as _contextlib  # noqa: E402

_RETRACTED_PREFIXES = ("data/black_diamond/", "data/canonical/schwab/silver/")


@_contextlib.contextmanager
def _armed():
    old = _comprail.HELD_PREFIXES
    _comprail.HELD_PREFIXES = _RETRACTED_PREFIXES
    try:
        yield
    finally:
        _comprail.HELD_PREFIXES = old


def test_hold_is_RETRACTED_by_default_and_that_is_CORRECT(repo):
    """The control this suite never had. Without it there was no way to EXPRESS, let alone test,
    'the hold is off' -- which is why a retraction could fail to propagate and nothing noticed."""
    assert _comprail.HELD_PREFIXES == (), "the 2026-07-09 hold is RETRACTED; no prefix may be enforced"
    files, note, err = _comprail.gitignore_aware_files(str(repo), [])
    assert err is None
    got = _norm(files)
    for h in _HELD:
        assert h in got, f"post-retraction, {h} must be RETURNED, not excluded"
    assert note is None, f"no hold in force -> no held-note; got {note!r}"
