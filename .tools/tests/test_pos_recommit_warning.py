"""MX-x-5(b): proof-of-spec-check WARNs, naming each row, when an instance already at HEAD is re-committed
carrying PENDING-THIS-COMMIT rows. Offline: a temp git repo, the checker imported with its _REPO_ROOT re-pointed."""
import importlib.util
import json
import subprocess
from pathlib import Path

import pytest

CHECKER = Path(__file__).resolve().parent.parent / "proof-of-spec-check.py"
INST = "inst.proof.json"


def _git(repo, *a):
    return subprocess.run(["git", "-C", str(repo), "-c", "user.name=t", "-c", "user.email=t@t", *a],
                          capture_output=True, text=True, check=True).stdout.strip()


def _write(repo, pin_a="PENDING-THIS-COMMIT", pin_b="PENDING-THIS-COMMIT", note="v1"):
    inst = {"note": note, "artifacts_produced": [
        {"kind": "file", "path_or_key": "a.txt", "commit_or_etag": pin_a},
        {"kind": "file", "path_or_key": "b.txt", "commit_or_etag": pin_b}]}
    (repo / INST).write_text(json.dumps(inst), encoding="utf-8")
    return inst


@pytest.fixture
def mod(tmp_path, monkeypatch):
    _git(tmp_path, "init", "-q")
    spec = importlib.util.spec_from_file_location("pos_under_test", CHECKER)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    m._REPO_ROOT = tmp_path
    monkeypatch.chdir(tmp_path)
    return m


def _run(m, repo, capsys):
    inst = json.loads((repo / INST).read_text(encoding="utf-8"))
    m.artifact_resolution_check(inst, inst_path=repo / INST)
    return [ln for ln in capsys.readouterr().out.splitlines() if ln.startswith("WARN:")]


def test_recommit_with_pending_rows_warns(mod, tmp_path, capsys):
    (tmp_path / "a.txt").write_text("1\n")
    (tmp_path / "b.txt").write_text("1\n")
    _write(tmp_path)
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-qm", "first")
    (tmp_path / "a.txt").write_text("2\n")
    (tmp_path / "b.txt").write_text("2\n")
    _write(tmp_path, note="v2")
    _git(tmp_path, "add", "a.txt", "b.txt", INST)
    warns = _run(mod, tmp_path, capsys)
    assert len(warns) == 2, warns
    assert any("a.txt" in w for w in warns) and any("b.txt" in w for w in warns)


def test_first_commit_is_silent(mod, tmp_path, capsys):
    (tmp_path / "a.txt").write_text("1\n")
    (tmp_path / "b.txt").write_text("1\n")
    _write(tmp_path)
    _git(tmp_path, "add", "-A")
    assert _run(mod, tmp_path, capsys) == []


def test_all_pinned_is_silent(mod, tmp_path, capsys):
    (tmp_path / "a.txt").write_text("1\n")
    (tmp_path / "b.txt").write_text("1\n")
    _write(tmp_path)
    _git(tmp_path, "add", "-A")
    _git(tmp_path, "commit", "-qm", "first")
    h = _git(tmp_path, "rev-parse", "HEAD")
    _write(tmp_path, h, h, note="v2")
    _git(tmp_path, "add", INST)
    assert _run(mod, tmp_path, capsys) == []
