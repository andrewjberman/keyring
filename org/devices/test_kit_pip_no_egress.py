"""test_kit_pip_no_egress.py -- the pip no-egress kit, pure tests. NO PIP PROCESS STARTS AND NO REQUEST LEAVES THIS MACHINE.

(1) the wrapper's verb and flag classification over a table of argument lists, each row with its expected allow or refuse; (2) the
refusal text is exactly the required line, and a refused call starts no process; (3) an allowed call reaches pip unchanged (decided
with a stub: no process starts); (4) the index and proxy listeners count the requests Python makes to them, and the host parser
names the host; (5) the candidate grader passes only the zero-request, named, untimed arm, and its independent audit catches a
planted pass that made a request; (6) the form decision names the first non-wrapper form that holds, wrapper-only, or NONE;
(7) the kit source is ASCII, bakes no user path, and names no public host.
LAST line: KIT-PIP-TESTS ok=<True|False> cases=<k>/<n>.
"""
from __future__ import annotations

import contextlib
import importlib.util
import io
import json
import pathlib
import re
import shutil
import socket
import sys
import tempfile
import time
import types

HERE = pathlib.Path(__file__).resolve().parent
TOOL = HERE / "kit_pip_no_egress.py"
spec = importlib.util.spec_from_file_location("kit_pip_no_egress", str(TOOL))
kit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(kit)

RESULTS = []
REFUSAL_LITERAL = ("REFUSED: this box does not download. Ask the laptop: org/devices/intake/ (request, check, Taildrop). "
                   "No request was made.")

# (argument list, expected action): the table the wrapper is judged by.
TABLE = [
    (["list"], "ALLOW"),
    (["show", "six"], "ALLOW"),
    (["freeze"], "ALLOW"),
    (["check"], "ALLOW"),
    (["--version"], "ALLOW"),
    (["--help"], "ALLOW"),
    (["list", "--format=json"], "ALLOW"),
    (["-v", "list"], "ALLOW"),
    (["--cache-dir", "cachedir", "list"], "ALLOW"),
    (["install", "--no-index", "--no-deps", "wheelhouse/six-1.16.0-py2.py3-none-any.whl"], "ALLOW"),
    (["install", "--no-index", "--no-deps", "--find-links", "wheelhouse", "six"], "ALLOW"),
    (["install", "--help"], "ALLOW"),
    (["list", "--index-url", "file:///wheelhouse"], "ALLOW"),
    (["install", "--no-index", "--no-deps", "--target", "t", "--retries", "0", "six"], "ALLOW"),
    (["download", "--help"], "ALLOW"),
    (["download", "--no-index", "--no-deps", "-d", "out", "six"], "ALLOW"),
    (["install", "six==1.16.0"], "REFUSE"),
    (["install", "--no-deps", "six"], "REFUSE"),
    (["download", "--no-deps", "-d", "out", "six==1.16.0"], "REFUSE"),
    (["wheel", "six"], "REFUSE"),
    (["index", "versions", "six"], "REFUSE"),
    (["search", "six"], "REFUSE"),
    (["-q", "download", "six"], "REFUSE"),
    (["install", "--index-url", "https://pypi.org/simple", "six"], "REFUSE"),
    (["install", "--index-url=https://pypi.org/simple", "six"], "REFUSE"),
    (["install", "-i", "https://example.org/simple", "six"], "REFUSE"),
    (["install", "-ihttp://127.0.0.1:9/simple", "six"], "REFUSE"),
    (["install", "--extra-index-url", "http://127.0.0.1:9/simple", "six"], "REFUSE"),
    (["install", "--find-links", "https://example.org/wheels/", "six"], "REFUSE"),
    (["install", "-f", "http://example.org/wheels/", "six"], "REFUSE"),
    (["install", "--no-index", "--find-links", "https://example.org/wheels/", "six"], "REFUSE"),
    (["install", "--no-index", "https://example.org/six-1.16.0-py2.py3-none-any.whl"], "REFUSE"),
    (["install", "--no-index", "six @ https://example.org/six.whl"], "REFUSE"),
    (["install", "--no-index", "git+https://example.org/repo.git"], "REFUSE"),
    (["install", "--no-index", "-r", "reqs.txt"], "REFUSE"),
    (["install", "--no-index", "-e", "."], "REFUSE"),
    (["list", "--outdated"], "REFUSE"),
    (["list", "-o"], "REFUSE"),
    (["list", "--uptodate"], "REFUSE"),
    ([], "REFUSE"),
    (["uninstall", "six"], "REFUSE"),
    (["config", "list"], "REFUSE"),
    (["Install", "six"], "REFUSE"),
    (["--proxy", "http://proxy.example.org:8080", "list"], "REFUSE"),
    (["--proxy=http://proxy.example.org:8080", "list"], "REFUSE"),
    (["install", "--NO-INDEX", "six"], "REFUSE"),
    (["list", "--index-url", "HTTP://EXAMPLE.ORG/simple"], "REFUSE"),
]


def record(label, ok, detail):
    RESULTS.append(ok)
    print("CASE %d %s: %s" % (len(RESULTS), "PASS" if ok else "FAIL", detail))


def base_arm(**kw):
    arm = {"name": "x", "role": "candidate", "requests_index": 0, "requests_proxy": 0, "timed_out": False, "named": True,
           "passed": None, "leaked_public": 0}
    arm.update(kw)
    return arm


def main():
    # (1) the classification table: every row, one case each
    for args, expected in TABLE:
        action, _message = kit.classify(args)
        record("classify", action == expected, "classify(%r) = %s, expected %s" % (args, action, expected))

    # (2) the refusal text is exactly the required line; a download refusal carries it; a refused call starts no process
    record("refusal-text", kit.REFUSAL == REFUSAL_LITERAL, "kit.REFUSAL equals the required line: %s" % (kit.REFUSAL == REFUSAL_LITERAL))
    _a, msg_download = kit.classify(["download", "--no-deps", "six"])
    record("refusal-download-message", msg_download == REFUSAL_LITERAL, "download refusal message is the required line: %s"
           % (msg_download == REFUSAL_LITERAL))
    _a, msg_outdated = kit.classify(["list", "--outdated"])
    record("refusal-outdated-message", msg_outdated.startswith("REFUSED: list --outdated"),
           "list --outdated refusal names the verb: %s" % msg_outdated.startswith("REFUSED: list --outdated"))
    _a, msg_unknown = kit.classify(["uninstall", "six"])
    record("refusal-unknown-message", msg_unknown.startswith("REFUSED: not on the no-egress list"),
           "unknown verb refusal names the list: %s" % msg_unknown.startswith("REFUSED: not on the no-egress list"))

    calls = []

    def no_process(*a, **k):
        calls.append((a, k))
        raise AssertionError("a process was started")

    real_subprocess = kit.subprocess
    kit.subprocess = types.SimpleNamespace(run=no_process)
    try:
        buf = io.StringIO()
        with contextlib.redirect_stderr(buf):
            rc_refused = kit.wrap(["--", "download", "--no-deps", "-d", "out", "six"])
        record("wrap-refusal-rc-and-text", rc_refused == 3 and buf.getvalue() == REFUSAL_LITERAL + "\n" and not calls,
               "wrap refuses a download with rc=%s, stderr is the required line, calls=%d" % (rc_refused, len(calls)))
    finally:
        kit.subprocess = real_subprocess

    # (3) an allowed call reaches pip unchanged; the stub stands in for the process, so none starts
    seen = []

    def stub_run(argv, **kw):
        seen.append(argv)
        return types.SimpleNamespace(returncode=0)

    kit.subprocess = types.SimpleNamespace(run=stub_run)
    try:
        rc_allowed = kit.wrap(["--", "list", "--format=json"])
    finally:
        kit.subprocess = real_subprocess
    expected_argv = [sys.executable, "-m", "pip", "list", "--format=json"]
    record("wrap-allowed-unchanged", rc_allowed == 0 and seen == [expected_argv],
           "wrap passes list --format=json unchanged to pip: %s" % (seen == [expected_argv]))

    # wrap --from: a measurement that did not show the wrapper holding refuses before anything runs
    tmp_dir = pathlib.Path(tempfile.mkdtemp(prefix="kit-pip-test-"))
    try:
        json_path = tmp_dir / "m.json"
        json_path.write_text(json.dumps({"summary": {"form": "NONE", "wrapper_holds": False}}), encoding="utf-8")
        kit.subprocess = types.SimpleNamespace(run=no_process)
        try:
            buf2 = io.StringIO()
            with contextlib.redirect_stderr(buf2):
                rc_from = kit.wrap(["--from", str(json_path), "--", "list"])
        finally:
            kit.subprocess = real_subprocess
        record("wrap-from-unmeasured-refused", rc_from == 3 and not calls and "did not show the wrapper form" in buf2.getvalue(),
               "wrap --from with wrapper_holds False refuses with rc=%s and starts no process" % rc_from)
    finally:
        shutil.rmtree(str(tmp_dir), ignore_errors=True)

    # (4) the listeners count what Python sends, and the host parser names the host
    idx = kit.IndexListener()
    try:
        for path in ("/simple/a/", "/simple/b/", "/simple/c/"):
            conn = socket.create_connection((kit.LOOPBACK, idx.port), timeout=5)
            conn.sendall(("GET %s HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n" % path).encode("ascii"))
            conn.recv(4096)
            conn.close()
        time.sleep(0.2)
        logged = idx.log.take()
    finally:
        idx.close()
    record("index-listener-counts", len(logged) == 3 and all(x.startswith("GET /simple/") for x in logged),
           "index listener logged %d of 3 requests" % len(logged))

    prx = kit.ProxyListener()
    try:
        conn = socket.create_connection((kit.LOOPBACK, prx.port), timeout=5)
        conn.sendall(b"CONNECT example-public.invalid:443 HTTP/1.1\r\nHost: example-public.invalid:443\r\n\r\n")
        conn.recv(4096)
        conn.close()
        conn = socket.create_connection((kit.LOOPBACK, prx.port), timeout=5)
        conn.sendall(b"GET http://127.0.0.1:9/simple/x/ HTTP/1.1\r\nHost: 127.0.0.1:9\r\nConnection: close\r\n\r\n")
        conn.recv(4096)
        conn.close()
        time.sleep(0.2)
        plog = prx.log.take()
    finally:
        prx.close()
    record("proxy-listener-counts-and-flags-public", len(plog) == 2 and len(kit.public_hosts(plog)) == 1,
           "proxy listener logged %d lines, public-host lines %d" % (len(plog), len(kit.public_hosts(plog))))
    record("request-host-connect", kit.request_host("CONNECT example-public.invalid:443 HTTP/1.1 | host=x") == "example-public.invalid",
           "CONNECT line names its host")
    record("request-host-absolute-uri", kit.request_host("GET http://127.0.0.1:9/simple/x/ HTTP/1.1 | host=127.0.0.1:9") == "127.0.0.1",
           "absolute-URI GET names loopback")
    record("request-host-header", kit.request_host("GET /simple/x/ host=127.0.0.1:9") == "127.0.0.1", "a bare request names its Host")

    # (5) the grader: only the zero-request, named, untimed arm passes; the independent audit catches a planted pass
    record("grade-pass", kit.grade_arm(base_arm(), 1) is True, "a clean named arm with a positive run passes")
    record("grade-fails-on-index-request", kit.grade_arm(base_arm(requests_index=1), 1) is False, "an index request fails the arm")
    record("grade-fails-unnamed", kit.grade_arm(base_arm(named=False), 1) is False, "an arm that names neither package nor refusal fails")
    record("grade-fails-without-positive", kit.grade_arm(base_arm(), 0) is False, "no positive request means no candidate passes")
    planted = [base_arm(name="planted", role="candidate", passed=True, requests_proxy=1)]
    record("audit-catches-planted-pass", len(kit.audit_grades(planted)) == 1, "a PASS that made a request is a regression")

    # (6) the form decision, from synthetic arms: which candidates pass plain and hold against the explicit index
    def form_for(plain_ok, explicit_ok):
        arms = [base_arm(name="positive", role="positive", requests_index=0, requests_proxy=1)]
        cands = []
        for name in kit.CANDIDATE_ORDER:
            p, e = name, name + " +explicit-index"
            arms.append(base_arm(name=p, role="candidate"))
            arms.append(base_arm(name=e, role="explicit"))
            cands.append({"name": name, "plain_arm": p, "explicit_arm": e})
        allowed = set(plain_ok) | set(n + " +explicit-index" for n in explicit_ok)
        result = {"arms": arms, "positive": arms[0], "candidates": cands, "pip_version": "test"}
        return kit.summarize(result, grader=lambda a, p: a["name"] in allowed)

    s_env = form_for(["env:PIP_NO_INDEX"], ["env:PIP_NO_INDEX"])
    record("form-names-first-nonwrapper", s_env["form"] == "env:PIP_NO_INDEX" and s_env["holds_against_explicit"] == 1,
           "form=%s holds=%d" % (s_env["form"], s_env["holds_against_explicit"]))
    s_wrap = form_for(["env:PIP_NO_INDEX", "wrapper"], ["wrapper"])
    record("form-wrapper-only", s_wrap["form"] == "wrapper-only" and s_wrap["wrapper_holds"] is True,
           "a non-wrapper that passes but does not hold leaves form=%s" % s_wrap["form"])
    s_none = form_for([], [])
    record("form-none", s_none["form"] == "NONE" and s_none["passing"] == 0 and s_none["ok"] is True,
           "no candidate passes gives form=%s, and the harness still reads ok=%s" % (s_none["form"], s_none["ok"]))
    s_leak = kit.summarize({"arms": [base_arm(name="positive", role="positive", leaked_public=1, requests_proxy=1)],
                            "positive": base_arm(name="positive", role="positive", requests_proxy=1), "candidates": []},
                           grader=lambda a, p: False)
    record("leak-means-not-ok", s_leak["ok"] is False and s_leak["leaked_public"] == 1, "a public host seen makes ok=False")

    # (7) source hygiene: ASCII, no user path, no public host named in the kit
    src = TOOL.read_text(encoding="ascii")
    record("source-ascii", all(ord(c) < 128 for c in src), "kit source is ASCII")
    path_hit = re.search(r"[A-Za-z]:[\\/]Users|/c/Users|/home/", src)
    record("source-no-user-path", path_hit is None, "kit source carries no user path")
    record("source-no-public-host", "pypi" not in src.lower(), "kit source names no public package host")

    passed = sum(1 for ok in RESULTS if ok)
    ok_all = passed == len(RESULTS)
    print("KIT-PIP-TESTS ok=%s cases=%d/%d" % (ok_all, passed, len(RESULTS)))
    return 0 if ok_all else 1


if __name__ == "__main__":
    sys.exit(main())
