#!/usr/bin/env python3
"""test_round27_resolve.py -- NFRA_CTLPLN round 27, cell CT-as-1 (ruling XB-983c): the resolve verb of intake_fetch.py,
the re-check against the index's own metadata, and the fetchlist refusal of intake_closure.py for a non-Windows closure.

NO REAL NETWORK. Every release document is served by a LOOPBACK fake index this file starts on 127.0.0.1. Nothing is
downloaded, installed or written outside a temporary folder. The two tools are run at their own paths in this worktree.

Arms:
  a  three releases on one loopback index: a pure py3-none-any wheel is CHOSEN; a compiled release with a manylinux_2_17,
     a manylinux_2_28, a win_amd64 wheel and an sdist is CHOSEN as the manylinux_2_28 file; a sdist-only release is
     NO-WHEEL SDIST-ONLY
  b  a musllinux-only release is NO-WHEEL OTHER-PLATFORM-ONLY; a yanked manylinux_2_28 wheel is never chosen (the yanked
     release falls to its non-yanked manylinux_2_17 file); a release whose only fitting wheel is yanked is NO-WHEEL YANKED;
     a version the index does not publish is NO-WHEEL NO-RELEASE
  c  the approval gate: an approval file missing one exact name==version refuses the run, and the loopback server saw
     ZERO requests; the same run with a complete approval makes requests (difference control)
  d  exactly ONE request per member, and no request to any other path (no file, no project document, no attestation)
  e  the output JSON carries the index's sha256 and size, the rows are sorted by name, and the Markdown table is ASCII
  f  fetchlist on the saved Linux closure refuses with the stated message, writes nothing and exits 2; fetchlist on the
     saved Windows closure is byte-identical to its pre-change output (control: the two sha256 values were taken before
     the change, from the same closure and an absent assessment file)
  g  CONTROL of the instrument: the arm-a assertion, run on a hand-made result that picks the manylinux_2_17 file, FAILS
  h1 the re-check on a CHOSEN release: NEW-MEMBER for a distribution outside the closure, SPECIFIER-MISMATCH for a chosen
     version that violates a parent's specifier, HOST-CONFLICT for a host-satisfied member whose host version fails an
     index-side specifier, and ok=False
  h2 the clean case: HOST-OK for each host-satisfied member, no STOP line, ok=True; a requires_dist marker false for Linux
     (sys_platform == "win32") and a line naming an extra are not followed

LAST line: RESOLVE arms=<k>/<n> ok=<True|False>
Run: python .tools/tests/test_round27_resolve.py   (exit 0 = every arm PASS)
"""
from __future__ import annotations

import contextlib
import hashlib
import importlib.util
import io
import json
import pathlib
import sys
import tempfile
import threading
import traceback
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = pathlib.Path(__file__).resolve()
REPO = HERE.parents[2]
INTAKE = REPO / "org" / "devices" / "intake"
sys.path.insert(0, str(INTAKE))
import intake_fetch as F  # noqa: E402  (the tool at its own path in this worktree)

# the two Windows-closure hashes were taken BEFORE the change (fetchlist --from-file closure_cp314_win_amd64.json
# --assessment <absent file>); a change in either output is a change in the Windows fetch list
PRE_FETCHLIST_JSON_SHA = "47b486a5a5f4e030d40cdeeb320e29e90ba9f8992f2df147c62ac270d86ada2b"
PRE_FETCHLIST_MD_SHA = "5c4e64f97045118fd249488995e28659c1d6324338999eb04dc9cc71aac60f3f"
LINUX_CLOSURE = INTAKE / "closure_cp312_linux_x86_64_yfinance.json"
WIN_CLOSURE = INTAKE / "closure_cp314_win_amd64.json"
FETCHLIST_REFUSAL = ("fetchlist: this closure targets cp312-linux_x86_64; "
                     "use intake_fetch.py resolve to name its files")
TARGET = "cp312-linux_x86_64"
RELEASE_DATE = "2026-01-01T00:00:00.000000Z"


def _load(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


IC = _load("intake_closure", INTAKE / "intake_closure.py")


class Index:
    """Loopback fake index. releases maps (name, version) to a release document, or to None for a 404."""

    def __init__(self, releases):
        self.releases = releases
        self.paths = []
        me = self

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def do_GET(self):
                me.paths.append(self.path)
                parts = self.path.split("/")
                doc = None
                if len(parts) == 5 and parts[1] == "pypi" and parts[4] == "json":
                    doc = me.releases.get((parts[2], parts[3]))
                body = json.dumps(doc).encode("ascii") if doc is not None else b"{}"
                self.send_response(200 if doc is not None else 404)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), H)
        self.base = "http://127.0.0.1:%d" % self.server.server_address[1]
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()


def file_entry(fn, body=b"wheel-bytes", yanked=False, requires_python=">=3.8"):
    return {"filename": fn, "url": "http://127.0.0.1/files/" + fn,
            "digests": {"sha256": hashlib.sha256(body).hexdigest()}, "size": len(body),
            "upload_time_iso_8601": RELEASE_DATE, "yanked": yanked, "requires_python": requires_python,
            "packagetype": "bdist_wheel" if fn.endswith(".whl") else "sdist"}


def release(name, version, entries, requires_dist=None):
    return {"info": {"name": name, "version": version, "requires_dist": requires_dist},
            "urls": entries}


def closure_file(tmp, members, label=TARGET, name="closure.json"):
    doc = {"schema": "intake-closure/1", "target": {"label": label}, "members": members}
    path = pathlib.Path(tmp) / name
    path.write_text(json.dumps(doc, indent=1), encoding="ascii")
    return str(path)


def member(name, version, host_class=None):
    return {"name": name, "norm": name.lower(), "version": version, "class": "PURE", "host_class": host_class}


def approval_file(tmp, lines, name="approval.md"):
    path = pathlib.Path(tmp) / name
    path.write_text("batch\n" + "\n".join(lines) + "\n", encoding="ascii")
    return str(path)


def run_tool(argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = F.main(argv)
    text = buf.getvalue()
    text.encode("ascii")  # every line the verb prints is ASCII
    return rc, text


def resolve_argv(closure, approval, base, out=None, host=None):
    argv = ["resolve", "--closure", closure, "--target", TARGET, "--approved-by", approval, "--index-base", base]
    if host:
        argv += ["--host-pydeps", host]
    if out:
        argv += ["--out", out]
    return argv


def rows_by_name(path):
    doc = json.loads(pathlib.Path(path).read_text(encoding="ascii"))
    return doc, {r["name"]: r for r in doc["rows"]}


def arm_a_failures(rows):
    """The arm-a assertion, applied to a list of rows (dicts with name, outcome, file_name). Empty = every assertion holds."""
    want = {"purepkg": ("CHOSEN", "purepkg-1.0-py3-none-any.whl"),
            "compiled": ("CHOSEN", "compiled-2.0-cp312-cp312-manylinux_2_28_x86_64.whl"),
            "sourceonly": ("NO-WHEEL", None)}
    got = {r["name"]: r for r in rows}
    fails = []
    for name, (outcome, fn) in want.items():
        r = got.get(name)
        if r is None:
            fails.append("%s: no row" % name)
        elif r.get("outcome") != outcome:
            fails.append("%s: outcome %s, want %s" % (name, r.get("outcome"), outcome))
        elif fn is not None and r.get("file_name") != fn:
            fails.append("%s: file %s, want %s" % (name, r.get("file_name"), fn))
        elif outcome == "NO-WHEEL" and r.get("reason") != "SDIST-ONLY":
            fails.append("%s: reason %s, want SDIST-ONLY" % (name, r.get("reason")))
    return fails


def arm_a(tmp):
    releases = {
        ("purepkg", "1.0"): release("purepkg", "1.0", [file_entry("purepkg-1.0-py3-none-any.whl")]),
        ("compiled", "2.0"): release("compiled", "2.0", [
            file_entry("compiled-2.0-cp312-cp312-manylinux_2_17_x86_64.whl"),
            file_entry("compiled-2.0-cp312-cp312-manylinux_2_28_x86_64.whl"),
            file_entry("compiled-2.0-cp312-cp312-win_amd64.whl"),
            file_entry("compiled-2.0.tar.gz")]),
        ("sourceonly", "3.0"): release("sourceonly", "3.0", [file_entry("sourceonly-3.0.tar.gz")]),
    }
    idx = Index(releases)
    try:
        closure = closure_file(tmp, [member("purepkg", "1.0"), member("compiled", "2.0"), member("sourceonly", "3.0")],
                               name="a_closure.json")
        approval = approval_file(tmp, ["purepkg==1.0", "compiled==2.0", "sourceonly==3.0"], "a_approval.md")
        out = str(pathlib.Path(tmp) / "a_out.json")
        rc, text = run_tool(resolve_argv(closure, approval, idx.base, out))
    finally:
        idx.stop()
    doc, _ = rows_by_name(out)
    fails = arm_a_failures(doc["rows"])
    assert rc == 1 and not fails, (rc, fails)
    return "purepkg -> %s; compiled -> %s (not manylinux_2_17, not win_amd64, not the sdist); sourceonly -> NO-WHEEL SDIST-ONLY" % (
        "purepkg-1.0-py3-none-any.whl", "compiled-2.0-cp312-cp312-manylinux_2_28_x86_64.whl")


def arm_b(tmp):
    releases = {
        ("muslpkg", "1.0"): release("muslpkg", "1.0", [file_entry("muslpkg-1.0-cp312-cp312-musllinux_1_1_x86_64.whl")]),
        ("yankedpkg", "1.0"): release("yankedpkg", "1.0", [
            file_entry("yankedpkg-1.0-cp312-cp312-manylinux_2_28_x86_64.whl", yanked=True),
            file_entry("yankedpkg-1.0-cp312-cp312-manylinux_2_17_x86_64.whl")]),
        ("yankonly", "1.0"): release("yankonly", "1.0", [
            file_entry("yankonly-1.0-cp312-cp312-manylinux_2_28_x86_64.whl", yanked=True)]),
        ("gone", "9.9"): None,
    }
    idx = Index(releases)
    try:
        members = [member("muslpkg", "1.0"), member("yankedpkg", "1.0"), member("yankonly", "1.0"), member("gone", "9.9")]
        closure = closure_file(tmp, members, name="b_closure.json")
        approval = approval_file(tmp, ["muslpkg==1.0", "yankedpkg==1.0", "yankonly==1.0", "gone==9.9"], "b_approval.md")
        out = str(pathlib.Path(tmp) / "b_out.json")
        rc, text = run_tool(resolve_argv(closure, approval, idx.base, out))
    finally:
        idx.stop()
    _doc, got = rows_by_name(out)
    assert got["muslpkg"]["outcome"] == "NO-WHEEL" and got["muslpkg"]["reason"] == "OTHER-PLATFORM-ONLY", got["muslpkg"]
    assert "cp312-cp312-musllinux_1_1_x86_64" in got["muslpkg"]["tags"], got["muslpkg"]["tags"]
    assert got["yankedpkg"]["outcome"] == "CHOSEN" and got["yankedpkg"]["file_name"] == \
        "yankedpkg-1.0-cp312-cp312-manylinux_2_17_x86_64.whl", got["yankedpkg"]
    assert "yankedpkg-1.0-cp312-cp312-manylinux_2_28_x86_64.whl" not in json.dumps(got["yankedpkg"]), got["yankedpkg"]
    assert got["yankonly"]["outcome"] == "NO-WHEEL" and got["yankonly"]["reason"] == "YANKED", got["yankonly"]
    assert got["gone"]["outcome"] == "NO-WHEEL" and got["gone"]["reason"] == "NO-RELEASE" and got["gone"]["release_status"] == 404
    assert rc == 1 and '"ok": false' in pathlib.Path(out).read_text(encoding="ascii")
    return ("muslpkg NO-WHEEL OTHER-PLATFORM-ONLY (tag cp312-cp312-musllinux_1_1_x86_64); yankedpkg CHOSEN the 2_17 file, "
            "the yanked 2_28 never; yankonly NO-WHEEL YANKED; gone NO-WHEEL NO-RELEASE (HTTP 404)")


def arm_c(tmp):
    releases = {("purepkg", "1.0"): release("purepkg", "1.0", [file_entry("purepkg-1.0-py3-none-any.whl")]),
                ("compiled", "2.0"): release("compiled", "2.0", [
                    file_entry("compiled-2.0-cp312-cp312-manylinux_2_28_x86_64.whl")])}
    members = [member("purepkg", "1.0"), member("compiled", "2.0")]
    closure = closure_file(tmp, members, name="c_closure.json")
    partial = approval_file(tmp, ["purepkg==1.0"], "c_partial.md")  # compiled==2.0 is missing
    idx = Index(releases)
    try:
        rc, text = run_tool(resolve_argv(closure, partial, idx.base))
        refused_paths = list(idx.paths)
        full = approval_file(tmp, ["purepkg==1.0", "compiled==2.0"], "c_full.md")
        rc2, text2 = run_tool(resolve_argv(closure, full, idx.base))
        granted_paths = list(idx.paths)
    finally:
        idx.stop()
    assert rc == 2 and "REFUSED" in text and "compiled==2.0" in text and "lacks 1 of 2" in text, (rc, text)
    assert refused_paths == [], refused_paths
    assert rc2 in (0, 1) and len(granted_paths) == 2, (rc2, granted_paths)
    return ("partial approval: rc=2, 'lacks 1 of 2 exact line(s): compiled==2.0', server requests=%d; "
            "complete approval: server requests=%d (difference control)" % (len(refused_paths), len(granted_paths)))


def arm_d(tmp):
    releases = {("purepkg", "1.0"): release("purepkg", "1.0", [file_entry("purepkg-1.0-py3-none-any.whl")]),
                ("compiled", "2.0"): release("compiled", "2.0", [
                    file_entry("compiled-2.0-cp312-cp312-manylinux_2_28_x86_64.whl")]),
                ("sourceonly", "3.0"): release("sourceonly", "3.0", [file_entry("sourceonly-3.0.tar.gz")])}
    idx = Index(releases)
    try:
        closure = closure_file(tmp, [member("purepkg", "1.0"), member("compiled", "2.0"), member("sourceonly", "3.0")],
                               name="d_closure.json")
        approval = approval_file(tmp, ["purepkg==1.0", "compiled==2.0", "sourceonly==3.0"], "d_approval.md")
        out = str(pathlib.Path(tmp) / "d_out.json")
        run_tool(resolve_argv(closure, approval, idx.base, out))
        paths = list(idx.paths)
    finally:
        idx.stop()
    expected = sorted("/pypi/%s/%s/json" % (n, v) for n, v in (("compiled", "2.0"), ("purepkg", "1.0"), ("sourceonly", "3.0")))
    assert sorted(paths) == expected and len(paths) == 3, (paths, expected)
    doc, _ = rows_by_name(out)
    assert [r["release_status"] for r in doc["rows"]] == [200, 200, 200] and len(doc["requests"]) == 3, doc["requests"]
    assert all(r["url"].endswith("/json") for r in doc["requests"]), doc["requests"]
    return "3 members -> %d requests, one per release document (%s); no file, project or attestation path" % (
        len(paths), ", ".join(p for p in sorted(paths)))


def arm_e(tmp):
    body = b"purepkg-payload-for-the-digest-check"
    releases = {("purepkg", "1.0"): release("purepkg", "1.0", [file_entry("purepkg-1.0-py3-none-any.whl", body=body)]),
                ("zeta", "1.0"): release("zeta", "1.0", [file_entry("zeta-1.0-py3-none-any.whl")]),
                ("alpha", "1.0"): release("alpha", "1.0", [file_entry("alpha-1.0-py3-none-any.whl")])}
    idx = Index(releases)
    try:
        closure = closure_file(tmp, [member("zeta", "1.0"), member("purepkg", "1.0"), member("alpha", "1.0")],
                               name="e_closure.json")
        approval = approval_file(tmp, ["zeta==1.0", "purepkg==1.0", "alpha==1.0"], "e_approval.md")
        out = str(pathlib.Path(tmp) / "e_out.json")
        rc, text = run_tool(resolve_argv(closure, approval, idx.base, out))
    finally:
        idx.stop()
    doc, got = rows_by_name(out)
    assert got["purepkg"]["sha256"] == hashlib.sha256(body).hexdigest(), got["purepkg"]
    assert got["purepkg"]["size"] == len(body), got["purepkg"]
    assert got["purepkg"]["upload_time"] == RELEASE_DATE and rc == 0 and doc["ok"] is True
    names = [r["name"] for r in doc["rows"]]
    assert names == ["alpha", "purepkg", "zeta"], names
    md = pathlib.Path(out[:-5] + ".md").read_bytes()
    md.decode("ascii")
    assert b"purepkg-1.0-py3-none-any.whl" in md and b"| 1 | alpha |" in md
    assert pathlib.Path(out).read_bytes().decode("ascii")
    return "sha256 and size equal the index's values (%s..., %d bytes); rows sorted %s; .md ASCII" % (
        hashlib.sha256(body).hexdigest()[:12], len(body), ",".join(names))


def arm_f(tmp):
    buf = io.StringIO()
    out_linux = str(pathlib.Path(tmp) / "f_linux.json")
    with contextlib.redirect_stdout(buf):
        rc_linux = IC.main(["fetchlist", "--from-file", str(LINUX_CLOSURE), "--assessment",
                            str(pathlib.Path(tmp) / "no_assessment.md"), "--out", out_linux])
    refusal = buf.getvalue().strip().splitlines()
    assert rc_linux == 2 and refusal == [FETCHLIST_REFUSAL], (rc_linux, refusal)
    assert not pathlib.Path(out_linux).exists(), "a refused fetchlist wrote a file"
    out_json = pathlib.Path(tmp) / "f_win.json"
    out_md = pathlib.Path(tmp) / "f_win.md"
    with contextlib.redirect_stdout(io.StringIO()):
        rc_win = IC.main(["fetchlist", "--from-file", str(WIN_CLOSURE), "--assessment",
                          str(pathlib.Path(tmp) / "no_assessment.md"), "--out", str(out_json), "--md", str(out_md)])
    sha_json = hashlib.sha256(out_json.read_bytes()).hexdigest()
    sha_md = hashlib.sha256(out_md.read_bytes()).hexdigest()
    assert rc_win == 0 and sha_json == PRE_FETCHLIST_JSON_SHA and sha_md == PRE_FETCHLIST_MD_SHA, (sha_json, sha_md)
    return ("linux closure: rc=2 and the stated message only, no file written; windows closure: rc=0, json sha256 %s... "
            "and md sha256 %s... equal the pre-change values" % (sha_json[:12], sha_md[:12]))


def arm_g(tmp):
    """CONTROL: the arm-a assertion on a hand-made result that names the manylinux_2_17 file must FAIL."""
    hand = [{"name": "purepkg", "outcome": "CHOSEN", "file_name": "purepkg-1.0-py3-none-any.whl"},
            {"name": "compiled", "outcome": "CHOSEN", "file_name": "compiled-2.0-cp312-cp312-manylinux_2_17_x86_64.whl"},
            {"name": "sourceonly", "outcome": "NO-WHEEL", "reason": "SDIST-ONLY", "file_name": None}]
    fails = arm_a_failures(hand)
    assert fails == ["compiled: file compiled-2.0-cp312-cp312-manylinux_2_17_x86_64.whl, "
                     "want compiled-2.0-cp312-cp312-manylinux_2_28_x86_64.whl"], fails
    return "control FAILED as required: %s" % fails[0]


def _recheck_run(tmp, releases, members, approval_lines, host_dists, name):
    idx = Index(releases)
    try:
        closure = closure_file(tmp, members, name=name + "_closure.json")
        approval = approval_file(tmp, approval_lines, name + "_approval.md")
        host = pathlib.Path(tmp) / (name + "_host.json")
        host.write_text(json.dumps({"schema": "intake-host-pydeps/1", "dists": host_dists}), encoding="ascii")
        out = str(pathlib.Path(tmp) / (name + "_out.json"))
        rc, text = run_tool(resolve_argv(closure, approval, idx.base, out, host=str(host)))
    finally:
        idx.stop()
    return rc, text, out


def arm_h1(tmp):
    releases = {
        ("alpha", "1.0"): release("alpha", "1.0", [file_entry("alpha-1.0-py3-none-any.whl")], requires_dist=[
            "newdep>=1.0", "beta<2", "hosty<2", "clean>=1",
            'winonly>=1; sys_platform == "win32"', 'extra_only>=1; extra == "fast"']),
        ("beta", "2.0"): release("beta", "2.0", [file_entry("beta-2.0-py3-none-any.whl")]),
    }
    members = [member("alpha", "1.0"), member("beta", "2.0"), member("hosty", "2.0", "HOST-SATISFIED"),
               member("clean", "1.5", "HOST-SATISFIED")]
    rc, text, out = _recheck_run(tmp, releases, members, ["alpha==1.0", "beta==2.0"],
                                 {"hosty": "2.0", "clean": "1.5"}, "h1")
    lines = text.splitlines()
    assert "NEW-MEMBER newdep required by alpha >=1.0" in lines, lines
    assert "SPECIFIER-MISMATCH beta 2.0 unmet by alpha <2" in lines, lines
    assert "HOST-CONFLICT hosty host 2.0 unmet by alpha <2 STOP" in lines, lines
    assert "HOST-OK clean host 1.5 meets alpha >=1" in lines, lines
    assert not any(ln.startswith("NEW-MEMBER winonly") or "extra_only" in ln for ln in lines), lines
    assert rc == 1 and lines[-1].endswith("new_members=1 specifier_mismatches=1 host_conflicts=1"), lines[-1]
    assert " ok=False " in lines[-1], lines[-1]
    return "NEW-MEMBER newdep, SPECIFIER-MISMATCH beta 2.0 <2, HOST-CONFLICT hosty 2.0 <2, HOST-OK clean; last line: %s" % lines[-1]


def arm_h2(tmp):
    releases = {
        ("alpha", "1.0"): release("alpha", "1.0", [file_entry("alpha-1.0-py3-none-any.whl")], requires_dist=[
            "clean>=1", 'winonly>=1; sys_platform == "win32"', 'extra_only>=1; extra == "fast"']),
        ("beta", "2.0"): release("beta", "2.0", [file_entry("beta-2.0-py3-none-any.whl")], requires_dist=None),
    }
    members = [member("alpha", "1.0"), member("beta", "2.0"), member("hosty", "2.0", "HOST-SATISFIED"),
               member("clean", "1.5", "HOST-SATISFIED")]
    rc, text, out = _recheck_run(tmp, releases, members, ["alpha==1.0", "beta==2.0"],
                                 {"hosty": "2.0", "clean": "1.5"}, "h2")
    lines = text.splitlines()
    stops = [ln for ln in lines if ln.startswith(("NEW-MEMBER", "SPECIFIER-MISMATCH", "HOST-CONFLICT"))]
    assert stops == [], stops
    assert "HOST-OK clean host 1.5 meets alpha >=1" in lines and "HOST-OK hosty host 2.0 meets none-from-chosen-parents" in lines, lines
    assert "NO-METADATA beta==2.0 requires_dist absent from the release document" in lines, lines
    assert rc == 0 and lines[-1] == ("INTAKE-RESOLVE target=cp312-linux_x86_64 members=2 chosen=2 no_wheel=0 requests=2 "
                                     "ok=True new_members=0 specifier_mismatches=0 host_conflicts=0"), lines[-1]
    return "no STOP line; HOST-OK clean and hosty; winonly (win32) and extra_only not followed; last line: %s" % lines[-1]


ARMS = [("a  choice: pure, manylinux_2_28 over 2_17/win/sdist, sdist-only", arm_a),
        ("b  other-platform, yanked never chosen, yanked-only, no release", arm_b),
        ("c  approval gate: refusal before any socket, difference control", arm_c),
        ("d  one request per member, no other path", arm_d),
        ("e  output JSON sha256/size from the index, rows sorted, ASCII md", arm_e),
        ("f  fetchlist refuses a Linux closure; Windows output byte-identical", arm_f),
        ("g  CONTROL: the arm-a assertion on a manylinux_2_17 result FAILS", arm_g),
        ("h1 re-check issues: NEW-MEMBER, SPECIFIER-MISMATCH, HOST-CONFLICT", arm_h1),
        ("h2 re-check clean: HOST-OK, win32 marker and extra not followed", arm_h2)]


def main():
    passed = 0
    with tempfile.TemporaryDirectory(prefix="resolve-test-") as td:
        for i, (title, fn) in enumerate(ARMS, 1):
            try:
                detail = fn(pathlib.Path(td))
                passed += 1
                print("PASS arm %s: %s -- %s" % (title.split()[0], title, detail))
            except Exception as exc:  # noqa: BLE001 - a failing arm is reported, never raised
                print("FAIL arm %s: %s -- %s: %s" % (title.split()[0], title, type(exc).__name__, IC.asc(exc)[:300]))
                traceback.print_exc(limit=4, file=sys.stdout)
    ok = passed == len(ARMS)
    print("RESOLVE arms=%d/%d ok=%s" % (passed, len(ARMS), ok))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
