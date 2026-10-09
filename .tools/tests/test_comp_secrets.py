"""Acceptance: `.tools/comp-secrets get` -- the `--json --reveal` / `--value-only` contract
(AMGT_RESAPP.TO-AMGT-rk-67).

RULED (`CTO_RULING_COMP_SECRETS_REVEAL_CONTRACT_20260919T155xZ.md` point 2, `ROUND16_CTO_RULINGS_20260921.md`
@dcd88f0acc s.1): `--json --reveal` used to fall through to the text block with no warning -- now it emits
JSON carrying the value. A new `--value-only` flag prints the bare value and nothing else, and requires
`--reveal`. The DEFAULT `--reveal` text block stays byte-identical to HEAD's own `cmd_get` on the same fake
(the one real caller, `lib.research.social.collect.read_api_key`, parses that block's `value:` line).

SECURITY BOUNDS (task order section 4, ABSOLUTE): every test stubs `_client()` with a FAKE; the only value
ANY assertion in this file may ever compare against is the literal sentinel below; no real boto3 client is
ever built, no `secretsmanager` call ever reaches AWS, and `lib.research.social.collect.read_api_key` is
NEVER called with its own `subprocess.run` unpatched.

`.tools/comp-secrets` carries no `.py` suffix -- loaded per `importlib.machinery.SourceFileLoader`, per the
house pattern this order names.

Usage: python -m pytest .tools/tests/test_comp_secrets.py -v
"""
from __future__ import annotations

import argparse
import importlib.machinery
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

import pytest

SENTINEL = "SENTINEL-NOT-A-SECRET"


def _ws() -> Path:
    out = subprocess.run(
        ["git", "rev-parse", "--show-toplevel"],
        cwd=str(Path(__file__).resolve().parent),
        capture_output=True,
        text=True,
    )
    return Path(out.stdout.strip())


def _load_module(path: Path, name: str):
    """Load a script with no .py suffix as a fresh, independently-named module."""
    loader = importlib.machinery.SourceFileLoader(name, str(path))
    spec = importlib.util.spec_from_loader(name, loader)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    loader.exec_module(mod)
    return mod


class FakeClient:
    """A stand-in for the boto3 secretsmanager client. Never real, never network -- one
    entry, one sentinel value (or one binary blob for the binary arms)."""

    def __init__(self, secret_string=None, secret_binary=None,
                 name="opal/comp-secrets-test/fake-secret"):
        self._name = name
        self._arn = f"arn:aws:secretsmanager:us-east-1:000000000000:secret:{name}-abc123"
        self._secret_string = secret_string
        self._secret_binary = secret_binary

    def list_secrets(self, **kw):
        return {"SecretList": [{"Name": self._name, "ARN": self._arn}]}

    def get_secret_value(self, SecretId=None):
        resp = {"VersionId": "v1"}
        if self._secret_binary is not None:
            resp["SecretBinary"] = self._secret_binary
        else:
            resp["SecretString"] = self._secret_string
        return resp


IDENT = "opal/comp-secrets-test/fake-secret"


def _ns(reveal=False, json_=False, value_only=False, ident=IDENT):
    return argparse.Namespace(ident=ident, reveal=reveal, json=json_, value_only=value_only)


@pytest.fixture
def mod(monkeypatch):
    m = _load_module(_ws() / ".tools" / "comp-secrets", "comp_secrets_under_test")
    monkeypatch.setattr(m, "_client", lambda: FakeClient(secret_string=SENTINEL))
    return m


def test_json_reveal_refused(mod, capsys):
    # Row D1-W324-S3 (1.0.0_SA_CTO, 2026-10-09): an exported descriptor never carries the value.
    rc = mod.cmd_get(_ns(reveal=True, json_=True))
    out = capsys.readouterr()
    assert rc == 2
    assert out.out == ""
    assert SENTINEL not in out.out
    assert SENTINEL not in out.err


def test_json_without_reveal_unchanged(mod, capsys):
    rc = mod.cmd_get(_ns(reveal=False, json_=True))
    out = capsys.readouterr()
    assert rc == 0
    data = json.loads(out.out)
    assert "shape" in data
    assert "value" not in data


def test_value_only_bare(mod, capsys):
    rc = mod.cmd_get(_ns(reveal=True, value_only=True))
    out = capsys.readouterr()
    assert rc == 0
    assert out.out == SENTINEL + "\n"
    assert out.err == ""


def test_value_only_requires_reveal(mod, capsys):
    rc = mod.cmd_get(_ns(reveal=False, value_only=True))
    out = capsys.readouterr()
    assert rc == 2
    assert out.out == ""
    assert SENTINEL not in out.out
    assert SENTINEL not in out.err


def test_text_block_unchanged(tmp_path, monkeypatch, capsys):
    ws = _ws()
    live = _load_module(ws / ".tools" / "comp-secrets", "comp_secrets_live_for_text_block")
    monkeypatch.setattr(live, "_client", lambda: FakeClient(secret_string=SENTINEL))
    rc_new = live.cmd_get(_ns(reveal=True))
    out_new = capsys.readouterr().out
    assert rc_new == 0

    head_bytes = subprocess.run(
        ["git", "show", "HEAD:.tools/comp-secrets"], cwd=str(ws), capture_output=True
    ).stdout
    head_path = tmp_path / "comp_secrets_head_src"
    head_path.write_bytes(head_bytes)
    head_mod = _load_module(head_path, "comp_secrets_head_for_text_block")
    monkeypatch.setattr(head_mod, "_client", lambda: FakeClient(secret_string=SENTINEL))
    rc_head = head_mod.cmd_get(_ns(reveal=True))
    out_head = capsys.readouterr().out
    assert rc_head == 0

    assert out_new == out_head
    assert out_new.count("\n") == 4


def test_collect_parser_still_reads(mod, monkeypatch, capsys):
    rc = mod.cmd_get(_ns(reveal=True))
    default_block = capsys.readouterr().out
    assert rc == 0

    ws = _ws()
    if str(ws) not in sys.path:
        sys.path.insert(0, str(ws))
    from lib.research.social import collect

    def fake_run(*a, **kw):
        return subprocess.CompletedProcess(args=[], returncode=0, stdout=default_block, stderr="")

    monkeypatch.setattr(collect.subprocess, "run", fake_run)
    value = collect.read_api_key(IDENT)
    assert value == SENTINEL


def test_new_modes_never_leak_to_stderr(mod, capsys):
    rc1 = mod.cmd_get(_ns(reveal=True, json_=True))
    captured1 = capsys.readouterr()
    assert rc1 == 2
    assert SENTINEL not in captured1.err

    rc2 = mod.cmd_get(_ns(reveal=True, value_only=True))
    captured2 = capsys.readouterr()
    assert rc2 == 0
    assert SENTINEL not in captured2.err


def test_binary_modes(monkeypatch, capsys):
    m = _load_module(_ws() / ".tools" / "comp-secrets", "comp_secrets_binary_modes")
    monkeypatch.setattr(m, "_client", lambda: FakeClient(secret_binary=b"x"))

    rc1 = m.cmd_get(_ns(reveal=True, json_=True))
    out1 = capsys.readouterr().out
    assert rc1 == 2
    assert out1 == ""

    rc2 = m.cmd_get(_ns(reveal=True, value_only=True))
    captured2 = capsys.readouterr()
    assert rc2 == 1
    assert captured2.out == ""
