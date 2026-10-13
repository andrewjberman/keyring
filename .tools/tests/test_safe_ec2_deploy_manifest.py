"""MX-x-4 (a), row Z-W21-S23: safe-ec2-deploy.sh rewrites EC2_MANIFEST.json through a Python JSON parse/dump.

The helper lives inside the wrapper (a heredoc between `<<'MANIFEST_HELPER_PY'` and the terminator); this test extracts
that exact source and calls it, so what is proven is the code the wrapper runs. Offline; the real manifest is only READ
(copied to a temp dir).
"""
import difflib
import importlib.util
import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
WRAPPER = ROOT / "infra" / "aws" / "ec2" / "safe-ec2-deploy.sh"
REAL_MANIFEST = ROOT / "infra" / "aws" / "ec2" / "EC2_MANIFEST.json"

MOVABLE = ('"deployed_commit"', '"deployed_at"', '"deployed_by"', '"previous_deployed_commit"', '"_last_updated"')
NEW = dict(commit="deadbeef" * 5, timestamp="2026-10-01T12:00:00Z", agent="0.9.0_WK_TEST~1")


def _load_helper(tmp_path):
    src = WRAPPER.read_text(encoding="utf-8")
    m = re.search(r"<<'MANIFEST_HELPER_PY'\n(.*?)\nMANIFEST_HELPER_PY\n", src, re.S)
    assert m, "helper heredoc not found in safe-ec2-deploy.sh"
    f = tmp_path / "manifest_helper.py"
    f.write_text(m.group(1) + "\n", encoding="utf-8", newline="\n")
    spec = importlib.util.spec_from_file_location("manifest_helper", f)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def _fixture_text(escaped=True):
    dash = "\\u2014" if escaped else "\u2014"
    accent = "\\u00e9" if escaped else "\u00e9"
    body = (
        "{\n"
        '  "_schema_version": "1.1",\n'
        '  "_last_updated": "2026-01-01T00:00:00Z",\n'
        '  "services": {\n'
        '    "alpha": {\n'
        '      "source_path": "infra/aws/ec2/alpha",\n'
        '      "note": "alpha %s dash and caf%s",\n'
        '      "deployed_commit": "0000000",\n'
        '      "deployed_at": "2026-01-01T00:00:00Z"\n'
        "    },\n"
        '    "beta": {\n'
        '      "source_path": "infra/aws/ec2/beta",\n'
        '      "note": "beta %s dash %s%s",\n'
        '      "previous_deployed_commit": "0999999",\n'
        '      "deployed_commit": "1111111",\n'
        '      "deployed_at": "2026-02-02T00:00:00Z",\n'
        '      "deployed_by": "someone"\n'
        "    },\n"
        '    "gamma": {\n'
        '      "source_path": "infra/aws/ec2/gamma",\n'
        '      "ssh_key": null,\n'
        '      "note": "gamma %s"\n'
        "    }\n"
        "  }\n"
        "}\n"
    ) % (dash, accent, dash, dash, accent, dash)
    return body


def _run(tmp_path, text, service="beta", newline=None):
    helper = _load_helper(tmp_path)
    p = tmp_path / "EC2_MANIFEST.json"
    raw = text.encode("utf-8")
    if newline == "crlf":
        raw = text.replace("\n", "\r\n").encode("utf-8")
    p.write_bytes(raw)
    helper.update_manifest(str(p), service, NEW["commit"], NEW["timestamp"], NEW["agent"])
    return raw, p.read_bytes()


def _changed_lines(before: bytes, after: bytes):
    a = before.decode("utf-8").splitlines()
    b = after.decode("utf-8").splitlines()
    changed = []
    for tag, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
        if tag != "equal":
            changed += a[i1:i2] + b[j1:j2]
    return changed


@pytest.mark.parametrize("escaped", [True, False], ids=["escaped-ascii", "raw-utf8"])
def test_only_target_keys_move(tmp_path, escaped):
    before, after = _run(tmp_path, _fixture_text(escaped))
    changed = _changed_lines(before, after)
    assert changed, "helper changed nothing"
    for line in changed:
        assert line.strip().startswith(MOVABLE), "a non-target line moved: %r" % line
    d0, d1 = json.loads(before), json.loads(after)
    assert d1["services"]["beta"]["deployed_commit"] == NEW["commit"]
    assert d1["services"]["beta"]["deployed_at"] == NEW["timestamp"]
    assert d1["services"]["beta"]["deployed_by"] == NEW["agent"]
    assert d1["_last_updated"] == NEW["timestamp"]
    # every OTHER service entry is value-equal ...
    assert d0["services"]["alpha"] == d1["services"]["alpha"]
    assert d0["services"]["gamma"] == d1["services"]["gamma"]
    # ... and byte-equal as written (the escape style round-trips)
    for name in ("alpha", "gamma"):
        blk = re.search(r'    "%s": \{\n.*?\n    \}' % name, before.decode("utf-8"), re.S).group(0)
        assert blk.encode("utf-8") in after, "service %s block is not byte-equal after the round trip" % name
    if escaped:
        assert max(after) < 128, "escaped fixture must stay pure ASCII (no raw non-ASCII written)"
        assert b"\\u2014" in after
    else:
        assert "\u2014".encode("utf-8") in after and b"\\u2014" not in after
    # key order, new keys land at the end of the service entry exactly as jq did
    assert list(d0["services"]) == list(d1["services"])
    assert list(d0["services"]["beta"]) == list(d1["services"]["beta"])


def test_target_without_prior_keys_appends_in_order(tmp_path):
    before, after = _run(tmp_path, _fixture_text(True), service="gamma")
    d1 = json.loads(after)
    assert list(d1["services"]["gamma"])[-3:] == ["deployed_commit", "deployed_at", "deployed_by"]
    for line in _changed_lines(before, after):
        assert line.strip().startswith(MOVABLE) or line.strip() in ('"note": "gamma \\u2014"', '"note": "gamma \\u2014",')


def test_crlf_convention_and_trailing_newline_preserved(tmp_path):
    before, after = _run(tmp_path, _fixture_text(True), newline="crlf")
    assert after.count(b"\r\n") == after.count(b"\n") and after.endswith(b"\r\n")
    lf_before, lf_after = _run(tmp_path, _fixture_text(True))
    assert lf_after.count(b"\r") == 0 and lf_after.endswith(b"\n")


def test_unknown_service_fails_and_leaves_file(tmp_path):
    helper = _load_helper(tmp_path)
    p = tmp_path / "EC2_MANIFEST.json"
    p.write_bytes(_fixture_text(True).encode("utf-8"))
    with pytest.raises(KeyError):
        helper.update_manifest(str(p), "no-such-service", "c", "t", "a")
    assert p.read_bytes() == _fixture_text(True).encode("utf-8")


def test_real_manifest_copy_roundtrip_moves_only_target(tmp_path):
    if not REAL_MANIFEST.is_file():
        pytest.skip("real EC2_MANIFEST.json absent: %s" % REAL_MANIFEST)
    text = REAL_MANIFEST.read_text(encoding="utf-8")
    svc = next(iter(json.loads(text)["services"]))
    before, after = _run(tmp_path, text, service=svc)
    b_lines = before.decode("utf-8").splitlines()
    for line in _changed_lines(before, after):
        # a key appended after a line that had no trailing comma re-writes that line with one (comma-only change)
        assert line.strip().startswith(MOVABLE) or (line.rstrip(",") in b_lines), "real-manifest copy: non-target line moved: %r" % line
    assert (b"\\u" in before) == (b"\\u" in after)


def test_wrapper_no_longer_rewrites_with_jq_tr():
    src = WRAPPER.read_text(encoding="utf-8")
    assert not re.search(r"\|\s*tr -d '\\r'\s*>\s*\"\$TEMP\"", src), "the jq | tr rewrite is still in the wrapper"
    assert "MANIFEST_HELPER_PY" in src


def test_negative_control_old_jq_tr_shape_differs(tmp_path):
    jq = shutil.which("jq")
    if not jq:
        pytest.skip("jq absent on PATH: the old `jq | tr` negative control cannot run (reason printed, not a pass of the control)")
    bash = shutil.which("bash")
    if not bash:
        pytest.skip("bash absent on PATH: the old `jq | tr` negative control cannot run")
    text = _fixture_text(True)
    p = tmp_path / "old_shape.json"
    p.write_bytes(text.encode("utf-8"))
    cmd = (
        'jq ".services[\\"beta\\"].deployed_commit = \\"%s\\" | .services[\\"beta\\"].deployed_at = \\"%s\\" | '
        '.services[\\"beta\\"].deployed_by = \\"%s\\" | ._last_updated = \\"%s\\"" "%s" | tr -d \'\\r\''
        % (NEW["commit"], NEW["timestamp"], NEW["agent"], NEW["timestamp"], p.as_posix())
    )
    old = subprocess.run([bash, "-c", cmd], capture_output=True).stdout
    assert old, "old-shape jq produced no output"
    _, new = _run(tmp_path, text)
    assert old != new, "the old jq|tr shape matched the helper's output on the escape fixture: control is not discriminating"
    # the old shape rewrote unrelated (alpha) lines, which the helper does not
    assert b"\\u2014" not in old.split(b'"beta"')[0], "expected jq to have un-escaped alpha's dash"


def test_new_commit_moves_previous_deployed_commit(tmp_path):
    text = _fixture_text(True)
    _, after = _run(tmp_path, text)
    b = json.loads(after)["services"]["beta"]
    assert b["previous_deployed_commit"] == "1111111"
    assert b["deployed_commit"] == NEW["commit"]


def test_equal_commit_leaves_previous_unchanged(tmp_path):
    text = _fixture_text(True)
    _, once = _run(tmp_path, text)
    helper = _load_helper(tmp_path)
    p = tmp_path / "EC2_MANIFEST.json"
    helper.update_manifest(str(p), "beta", NEW["commit"], "2027-01-01T00:00:00Z", "0.9.0_WK_TEST~2")
    twice = p.read_bytes()
    assert json.loads(twice)["services"]["beta"]["previous_deployed_commit"] == "1111111"
    for line in _changed_lines(once, twice):
        assert line.strip().startswith(('"deployed_at"', '"deployed_by"', '"_last_updated"')), line
