"""Bundle item 6 -- danger-map auto-refresh (census G1 @e7952ccba).

The map sat 207h stale while the reflex printed `!! STALE` on every commit
fabric-wide for 8 days; nothing acted. The fix is the TRIGGER, not the
reporting: refresh-on-stale-read at the shared consumer. These tests pin the
three behaviors that make it safe on the commit path: fresh = untouched,
locked = skip-with-honest-note, build-failure = degrade-never-block.
"""
from __future__ import annotations

import os
import sys
import types
from pathlib import Path

WS = Path(__file__).resolve().parents[4]
if str(WS) not in sys.path:
    sys.path.insert(0, str(WS))

from org.modules.graph import comp_pulse as cp  # noqa: E402


def _wire_tmp_map(monkeypatch, tmp_path, age_h: float | None):
    """Point the module at a temp map with a controlled age. None = absent."""
    risk = tmp_path / "risk.json"
    if age_h is not None:
        risk.write_text('{"edges": []}', encoding="utf-8")
        past = os.path.getmtime(risk) - age_h * 3600
        os.utime(risk, (past, past))
    monkeypatch.setattr(cp, "RISK", str(risk))
    monkeypatch.setattr(cp, "_REFRESH_LOCK", str(risk) + ".refresh.lock")
    return risk


def test_fresh_map_is_not_touched(monkeypatch, tmp_path):
    risk = _wire_tmp_map(monkeypatch, tmp_path, age_h=1.0)
    mtime_before = os.path.getmtime(risk)

    def _boom(*a, **k):
        raise AssertionError("subprocess must not run on a fresh map")
    monkeypatch.setattr(cp.subprocess, "run", _boom)
    assert cp._ensure_fresh_danger_map() is None
    assert os.path.getmtime(risk) == mtime_before


def test_stale_map_triggers_rebuild(monkeypatch, tmp_path):
    _wire_tmp_map(monkeypatch, tmp_path, age_h=40.0)
    calls = []

    def _fake_run(cmd, **k):
        calls.append(cmd)
        return types.SimpleNamespace(returncode=0, stdout="", stderr="")
    monkeypatch.setattr(cp.subprocess, "run", _fake_run)
    note = cp._ensure_fresh_danger_map()
    assert note is not None and "AUTO-REFRESHED" in note and "40.0h stale" in note
    assert len(calls) == 1 and calls[0][2] == "build"
    assert not os.path.exists(cp._REFRESH_LOCK), "lock must be released"


def test_absent_map_triggers_rebuild_with_absent_label(monkeypatch, tmp_path):
    _wire_tmp_map(monkeypatch, tmp_path, age_h=None)
    monkeypatch.setattr(cp.subprocess, "run",
                        lambda *a, **k: types.SimpleNamespace(returncode=0, stdout="", stderr=""))
    note = cp._ensure_fresh_danger_map()
    assert note is not None and "ABSENT" in note


def test_young_lock_skips_and_says_so(monkeypatch, tmp_path):
    _wire_tmp_map(monkeypatch, tmp_path, age_h=40.0)
    Path(cp._REFRESH_LOCK).write_text("12345", encoding="utf-8")  # fresh lock NOW

    def _boom(*a, **k):
        raise AssertionError("subprocess must not run while a young lock is held")
    monkeypatch.setattr(cp.subprocess, "run", _boom)
    note = cp._ensure_fresh_danger_map()
    assert note is not None and "SKIPPED" in note and "STALE tag stands" in note
    assert os.path.exists(cp._REFRESH_LOCK), "another refresher's lock must not be stolen"


def test_dead_refresher_lock_is_taken_over(monkeypatch, tmp_path):
    _wire_tmp_map(monkeypatch, tmp_path, age_h=40.0)
    lock = Path(cp._REFRESH_LOCK)
    lock.write_text("999999", encoding="utf-8")
    old = os.path.getmtime(lock) - 3600  # 1h-old lock = dead refresher
    os.utime(lock, (old, old))
    monkeypatch.setattr(cp.subprocess, "run",
                        lambda *a, **k: types.SimpleNamespace(returncode=0, stdout="", stderr=""))
    note = cp._ensure_fresh_danger_map()
    assert note is not None and "AUTO-REFRESHED" in note
    assert not os.path.exists(cp._REFRESH_LOCK)


def test_build_failure_degrades_never_blocks(monkeypatch, tmp_path):
    _wire_tmp_map(monkeypatch, tmp_path, age_h=40.0)
    monkeypatch.setattr(cp.subprocess, "run",
                        lambda *a, **k: types.SimpleNamespace(returncode=3, stdout="",
                                                              stderr="boom: corpus unreadable"))
    note = cp._ensure_fresh_danger_map()
    assert note is not None and "FAILED rc=3" in note and "STALE tag stands" in note
    assert "corpus unreadable" in note  # the failure is SAID, not swallowed
    assert not os.path.exists(cp._REFRESH_LOCK)
