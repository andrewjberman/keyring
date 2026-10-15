"""
Tests for .tools/claude-usage-statusline.py (NFRA_MCPORTAL MP-pd-5, U2). Run: python -m pytest .tools/tests/test_claude_usage_statusline.py -v

The script is imported by path. Every test runs against a temp home and a temp config dir, so the real home and the
real ~/.claude are never touched. The seven test names are the contract of the cell's AC1 check.
"""
from __future__ import annotations

import builtins
import importlib.util
import io
import json
import os
import pathlib

SCRIPT = pathlib.Path(__file__).resolve().parents[1] / "claude-usage-statusline.py"
SPEC = importlib.util.spec_from_file_location("claude_usage_statusline", SCRIPT)
MOD = importlib.util.module_from_spec(SPEC)
SPEC.loader.exec_module(MOD)

ABSENT_REASON = ("rate_limits member not in the status-line payload "
                 "(present only for a subscription login after the first API response)")
OAUTH = {"emailAddress": "user@example.test", "organizationType": "claude_max", "organizationName": "Example Org"}


def _setup(tmp_path):
    home = tmp_path / "home"
    cfg = home / ".claude"
    cfg.mkdir(parents=True)
    return home, cfg


def _write_account(home, oauth=None):
    (home / ".claude.json").write_text(json.dumps({"oauthAccount": OAUTH if oauth is None else oauth}), encoding="utf-8")


def _payload(five=None, seven=None):
    limits = {}
    if five is not None:
        limits["five_hour"] = five
    if seven is not None:
        limits["seven_day"] = seven
    body = {"model": {"display_name": "x"}}
    if five is not None or seven is not None:
        body["rate_limits"] = limits
    return json.dumps(body)


def _run(stdin_text, home, cfg):
    out = io.StringIO()
    rc = MOD.main(stdin_text=stdin_text, config_dir=str(cfg), home=str(home), out=out)
    return rc, out.getvalue()


def _snapshot(cfg):
    return json.loads((cfg / "usage_snapshot.json").read_text(encoding="utf-8"))


MEASURED = _payload(five={"used_percentage": 42, "resets_at": "2026-10-14T23:00:00Z"},
                    seven={"used_percentage": 10, "resets_at": "2026-10-20T00:00:00Z"})
ABSENT = json.dumps({"model": {"display_name": "x"}})


def test_measured_payload_writes_snapshot_with_remaining(tmp_path):
    home, cfg = _setup(tmp_path)
    _write_account(home)
    rc, out = _run(MEASURED, home, cfg)
    assert rc == 0
    assert out == "5h 42% wk 10%\n"
    snap = _snapshot(cfg)
    assert snap["schema"] == 1
    assert snap["rate_limits_claim"] == "measured"
    assert snap["reason"] is None
    assert snap["five_hour"]["used_percentage"] == 42
    assert snap["five_hour"]["remaining_percentage"] == 58
    assert snap["five_hour"]["resets_at"] == "2026-10-14T23:00:00Z"
    assert snap["seven_day"]["used_percentage"] == 10
    assert snap["seven_day"]["remaining_percentage"] == 90
    assert snap["account_claim"] == "measured"


def test_payload_without_rate_limits_writes_absent_with_reason(tmp_path):
    home, cfg = _setup(tmp_path)
    _write_account(home)
    rc, out = _run(ABSENT, home, cfg)
    assert rc == 0
    assert out == "usage n/a\n"
    snap = _snapshot(cfg)
    assert snap["rate_limits_claim"] == "absent"
    assert snap["reason"] == ABSENT_REASON
    assert snap["five_hour"] is None
    assert snap["seven_day"] is None


def test_absent_never_replaces_measured_snapshot(tmp_path):
    home, cfg = _setup(tmp_path)
    _write_account(home)
    _run(MEASURED, home, cfg)
    before = (cfg / "usage_snapshot.json").read_bytes()
    rc, out = _run(ABSENT, home, cfg)
    assert rc == 0
    assert out == "usage n/a\n"
    assert (cfg / "usage_snapshot.json").read_bytes() == before


def test_never_opens_credentials_file(tmp_path, monkeypatch):
    home, cfg = _setup(tmp_path)
    _write_account(home)
    (cfg / ".credentials.json").write_text('{"claudeAiOauth": {"accessToken": "planted"}}', encoding="utf-8")
    accesses = []

    def guard(name, real):
        def guarded(*args, **kwargs):
            target = args[0] if args else kwargs.get("file", kwargs.get("path"))
            if target is not None and str(target).endswith(".credentials.json"):
                accesses.append("%s:%s" % (name, target))
                raise PermissionError("credentials access is forbidden in this test")
            return real(*args, **kwargs)
        return guarded

    for owner, attr in ((builtins, "open"), (io, "open"), (os, "open"), (os, "stat"), (os, "lstat"),
                        (os.path, "exists"), (os.path, "isfile"),
                        (pathlib.Path, "open"), (pathlib.Path, "read_text"), (pathlib.Path, "read_bytes"),
                        (pathlib.Path, "exists"), (pathlib.Path, "is_file"), (pathlib.Path, "stat")):
        monkeypatch.setattr(owner, attr, guard("%s.%s" % (owner.__name__, attr), getattr(owner, attr)))
    rc, out = _run(MEASURED, home, cfg)
    assert rc == 0
    assert out == "5h 42% wk 10%\n"
    assert _snapshot(cfg)["rate_limits_claim"] == "measured"
    assert accesses == []


def test_bad_stdin_prints_nothing_exits_zero_and_keeps_previous_file(tmp_path):
    home, cfg = _setup(tmp_path)
    _write_account(home)
    _run(MEASURED, home, cfg)
    before = (cfg / "usage_snapshot.json").read_bytes()
    rc, out = _run("not json", home, cfg)
    assert rc == 0
    assert out == ""
    assert (cfg / "usage_snapshot.json").read_bytes() == before


def test_atomic_write_leaves_no_partial_file(tmp_path, monkeypatch):
    home, cfg = _setup(tmp_path)
    _write_account(home)
    # Case 1: no previous snapshot; the replace fails. The directory must hold no snapshot and no temp file.
    def failing_replace(src, dst):
        raise OSError("simulated failure between temp write and replace")
    monkeypatch.setattr(os, "replace", failing_replace)
    rc, out = _run(MEASURED, home, cfg)
    assert rc == 0
    assert out == ""
    assert sorted(p.name for p in cfg.iterdir()) == []
    # Case 2: a previous snapshot exists; the failed replace leaves it intact and still no stray temp file.
    monkeypatch.undo()
    _run(MEASURED, home, cfg)
    before = (cfg / "usage_snapshot.json").read_bytes()
    monkeypatch.setattr(os, "replace", failing_replace)
    rc, out = _run(_payload(five={"used_percentage": 77}), home, cfg)
    assert rc == 0
    assert out == ""
    assert (cfg / "usage_snapshot.json").read_bytes() == before
    assert sorted(p.name for p in cfg.iterdir()) == ["usage_snapshot.json"]


def test_account_fields_only_named_keys(tmp_path):
    home, cfg = _setup(tmp_path)
    oauth = dict(OAUTH, accessToken="SECRET-TOKEN-VALUE", billingType="stripe_subscription",
                 organizationRateLimitTier="default_claude_max_5x")
    _write_account(home, oauth)
    rc, out = _run(MEASURED, home, cfg)
    assert rc == 0
    snap = _snapshot(cfg)
    assert snap["account_claim"] == "measured"
    assert snap["account"] == {"email": "user@example.test", "plan": "claude_max", "organization": "Example Org"}
    assert set(snap["account"]) == {"email", "plan", "organization"}
    assert "SECRET-TOKEN-VALUE" not in (cfg / "usage_snapshot.json").read_text(encoding="utf-8")
