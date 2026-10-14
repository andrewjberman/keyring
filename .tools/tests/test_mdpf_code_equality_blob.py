"""Tests for .tools/mdpf-code-equality.py: EQUAL is decided on the git index blob, not the working-tree bytes.

Each test builds its own temp git repository (LF blob, CRLF or untracked working copy) and a fake S3 client, so the
result does not depend on the checkout's line endings. No network, no AWS.
"""
import hashlib
import importlib.util
import os
import subprocess
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.normpath(os.path.join(HERE, "..", "mdpf-code-equality.py"))


def _load_tool():
    spec = importlib.util.spec_from_file_location("mdpf_code_equality_blob_tests", TOOL)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _git(repo, *args):
    env = {k: v for k, v in os.environ.items() if not k.startswith("GIT_")}
    got = subprocess.run(["git", "-C", repo, "-c", "core.autocrlf=false", "-c", "user.name=t", "-c", "user.email=t@t"]
                         + list(args), capture_output=True, env=env)
    if got.returncode != 0:
        raise RuntimeError("git %s failed: %s" % (args, got.stderr[:200]))
    return got


def _md5(body):
    return hashlib.md5(body).hexdigest()


class _FakeS3:
    def __init__(self, objects):
        self.objects = objects  # {key: etag}

    def get_paginator(self, _name):
        return self

    def paginate(self, Bucket, Prefix):
        yield {"Contents": [{"Key": k, "ETag": '"%s"' % v} for k, v in sorted(self.objects.items()) if k.startswith(Prefix)]}


def _write(path, body):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as fh:
        fh.write(body)


def test_crlf_working_file_equal_by_blob():
    mod = _load_tool()
    lf = b"x\ny\n"
    with tempfile.TemporaryDirectory() as td:
        _git(td, "init", "-q")
        _write(os.path.join(td, "data", "x", "a.txt"), lf)
        _git(td, "add", "data/x/a.txt")
        _git(td, "commit", "-q", "-m", "x")
        # the working copy is rewritten CRLF; the index blob stays LF
        _write(os.path.join(td, "data", "x", "a.txt"), lf.replace(b"\n", b"\r\n"))
        mod.ROOT = td
        res = mod.compare_tree(os.path.join(td, "data", "x"), "b", "p/", _FakeS3({"p/a.txt": _md5(lf)}))
    assert "a.txt" in res["equal"]
    assert "a.txt" not in res["differ"]
    assert res["basis"] == {"a.txt": "blob"}
    assert res["worktree_cr"] == {"a.txt": 2}


def test_true_difference_stays_differ():
    mod = _load_tool()
    lf = b"x\ny\n"
    with tempfile.TemporaryDirectory() as td:
        _git(td, "init", "-q")
        _write(os.path.join(td, "data", "x", "a.txt"), lf)
        _git(td, "add", "data/x/a.txt")
        _git(td, "commit", "-q", "-m", "x")
        mod.ROOT = td
        res = mod.compare_tree(os.path.join(td, "data", "x"), "b", "p/", _FakeS3({"p/a.txt": _md5(b"other\n")}))
    assert "a.txt" in res["differ"]
    assert "a.txt" not in res["equal"]
    assert res["basis"] == {"a.txt": "blob"}
    assert "a.txt" not in res["worktree_cr"]


def test_no_index_entry_reads_the_working_tree():
    mod = _load_tool()
    body = b"c\r\nc\r\n"
    with tempfile.TemporaryDirectory() as td:
        _git(td, "init", "-q")
        _write(os.path.join(td, "data", "x", "c.txt"), body)  # untracked: no index entry
        mod.ROOT = td
        res = mod.compare_tree(os.path.join(td, "data", "x"), "b", "p/", _FakeS3({"p/c.txt": _md5(body)}))
    assert "c.txt" in res["equal"]
    assert res["basis"] == {"c.txt": "worktree"}
    assert "c.txt" not in res["worktree_cr"]
