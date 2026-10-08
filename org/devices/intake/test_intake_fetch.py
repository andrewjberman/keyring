#!/usr/bin/env python3
"""Test intake_fetch.py against a FAKE index on 127.0.0.1. Nothing here contacts a real index:
every request goes to a listener this file starts, and the public-base cases patch the opener
and name resolution to raise so a stray socket would fail the case loudly.

Last line: INTAKE-FETCH-TEST cases=<k>/<n> ok=<True|False>
"""
import hashlib
import io
import json
import os
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import threading
import traceback
import urllib.error
import zipfile
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import intake_fetch as T  # noqa: E402

SERIAL = "0.9.0_WK_TEST~1"
os.environ["OPAL_AGENT_SERIAL"] = SERIAL


def make_wheel(tag="test"):
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, "w") as z:
        z.writestr("demo/__init__.py", "X = 1\n")
        z.writestr("demo-1.0.dist-info/METADATA", "Metadata-Version: 2.1\nName: demo\nVersion: 1.0\n" + tag + "\n")
    return buf.getvalue()


class Index:
    """A fake index. `files` maps a file name to its behaviour."""

    def __init__(self, other=None):
        self.files = {}
        self.name = "demo-pkg"
        self.version = "1.0"
        self.requests = []
        self.other = other
        self.attestation_status = 200
        self.extra_releases = {"0.9": ["2020-01-01T00:00:00.000000Z"]}
        self.server = ThreadingHTTPServer(("127.0.0.1", 0), self._handler())
        self.port = self.server.server_address[1]
        self.base = "http://127.0.0.1:%d" % self.port
        self.thread = threading.Thread(target=self.server.serve_forever, daemon=True)
        self.thread.start()

    def add(self, file_name, body, served=None, url=None, yanked=False, spelling=None, redirect_to=None):
        self.files[file_name] = {
            "body": body, "served": body if served is None else served, "yanked": yanked,
            "spelling": spelling or file_name, "url": url, "redirect_to": redirect_to,
        }

    def stop(self):
        self.server.shutdown()
        self.server.server_close()

    def _handler(self):
        idx = self

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def _send(self, code, body=b"", ctype="application/json", extra=None):
                self.send_response(code)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(body)))
                for k, v in (extra or {}).items():
                    self.send_header(k, v)
                self.end_headers()
                self.wfile.write(body)

            def do_GET(self):
                idx.requests.append(self.path)
                parts = self.path.split("/")
                if self.path == "/pypi/%s/%s/json" % (idx.name, idx.version):
                    urls = []
                    for fn, f in idx.files.items():
                        urls.append({
                            "filename": f["spelling"],
                            "url": f["url"] or "%s/files/%s" % (idx.base, f["spelling"]),
                            "digests": {"sha256": hashlib.sha256(f["body"]).hexdigest()},
                            "size": len(f["body"]),
                            "upload_time_iso_8601": "2021-05-05T00:00:00.000000Z",
                            "yanked": f["yanked"],
                            "requires_python": ">=3.8",
                        })
                    return self._send(200, json.dumps({"info": {"name": idx.name}, "urls": urls}).encode())
                if self.path == "/pypi/%s/json" % idx.name:
                    rel = {v: [{"upload_time_iso_8601": t} for t in ts] for v, ts in idx.extra_releases.items()}
                    rel[idx.version] = [{"upload_time_iso_8601": "2021-05-05T00:00:00.000000Z"}]
                    return self._send(200, json.dumps({"releases": rel}).encode())
                if len(parts) > 2 and parts[1] == "integrity" and parts[-1] == "provenance":
                    return self._send(idx.attestation_status, b"{}")
                if len(parts) == 3 and parts[1] in ("files", "hop"):
                    for f in idx.files.values():
                        if f["spelling"] == parts[2]:
                            if f["redirect_to"] and parts[1] == "files":
                                return self._send(302, b"", extra={"Location": f["redirect_to"]})
                            return self._send(200, f["served"], "application/octet-stream")
                return self._send(404, b"{}")

        return H


class Counter:
    """A second listener on another port: counts every request it sees."""

    def __init__(self):
        self.hits = []
        me = self

        class H(BaseHTTPRequestHandler):
            def log_message(self, *a):
                pass

            def do_GET(self):
                me.hits.append(self.path)
                self.send_response(200)
                self.send_header("Content-Length", "2")
                self.end_headers()
                self.wfile.write(b"{}")

        self.server = ThreadingHTTPServer(("127.0.0.1", 0), H)
        self.port = self.server.server_address[1]
        self.base = "http://127.0.0.1:%d" % self.port
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def stop(self):
        self.server.shutdown()
        self.server.server_close()


class Env:
    """Temporary holding root and records root for one case."""

    def __enter__(self):
        self.dir = tempfile.mkdtemp(prefix="intake_test_")
        self.root = os.path.join(self.dir, "root")
        self.records = os.path.join(self.dir, "records")
        os.environ["OPAL_INTAKE_ROOT"] = self.root
        os.environ["OPAL_INTAKE_RECORDS"] = self.records
        return self

    def __exit__(self, *exc):
        os.environ.pop("OPAL_INTAKE_ROOT", None)
        os.environ.pop("OPAL_INTAKE_RECORDS", None)
        shutil.rmtree(self.dir, ignore_errors=True)

    def holding(self, batch="b1"):
        d = os.path.join(self.root, "holding", batch)
        return sorted(os.listdir(d)) if os.path.isdir(d) else []

    def record(self, file_name, batch="b1"):
        with open(os.path.join(self.records, batch, file_name + ".fetch.json"), encoding="ascii") as fh:
            return json.load(fh)


class A:
    def __init__(self, **kw):
        self.batch = "b1"
        self.name = "demo-pkg"
        self.version = "1.0"
        self.python_tag = "cp312"
        self.abi_tag = "cp312"
        self.platform_tag = "win_amd64"
        self.index_base = None
        self.approved_by = None
        self.__dict__.update(kw)


def run(a):
    rec = T.Fetch(a).execute()
    T.write_record(rec)
    return rec


WIN = "demo_pkg-1.0-cp312-cp312-win_amd64.whl"
LIN = "demo_pkg-1.0-cp311-cp311-manylinux2014_x86_64.whl"


# ---------------------------------------------------------------- cases

def case_happy():
    idx = Index()
    try:
        body = make_wheel()
        idx.add(WIN, body)
        with Env() as e:
            rec = run(A(index_base=idx.base))
            assert rec["outcome"] == "held", rec["reason"]
            assert e.holding() == [WIN], e.holding()
            with open(os.path.join(e.root, "holding", "b1", WIN), "rb") as fh:
                assert hashlib.sha256(fh.read()).hexdigest() == hashlib.sha256(body).hexdigest()
            assert len(rec["requests"]) == 4, len(rec["requests"])
            assert [r["method"] for r in rec["requests"]] == ["GET"] * 4
            assert all(r["status"] == 200 and r["url"].startswith(idx.base) for r in rec["requests"])
            assert rec["attestation"] == "present" and rec["attestation_url"].endswith("/provenance")
            assert rec["held_path"] == "holding/b1/" + WIN, rec["held_path"]
            assert rec["held_bytes"] == len(body) and rec["fetched_by"] == SERIAL
            assert rec["published"]["size"] == len(body) and rec["published"]["yanked"] is False
            assert rec["project"] == {"release_count": 2, "first_release_at": "2020-01-01T00:00:00.000000Z",
                                      "this_release_at": "2021-05-05T00:00:00.000000Z"}, rec["project"]
            saved = e.record(WIN)
            assert saved["outcome"] == "held"
            assert saved["schema"] == "intake-fetch/1"
            for key in ("batch", "requested", "index_base", "requests", "published", "project", "attestation",
                        "held_path", "held_sha256", "held_bytes", "outcome", "reason", "fetched_by", "at"):
                assert key in saved, key
    finally:
        idx.stop()


def case_missing_file():
    idx = Index()
    try:
        idx.add("demo_pkg-1.0-cp310-cp310-win_amd64.whl", make_wheel("a"))
        idx.add("demo_pkg-1.0-py3-none-any.whl", make_wheel("b"))
        with Env() as e:
            rec = run(A(index_base=idx.base))
            assert rec["outcome"] == "refused" and rec["reason"] == "no such file for this release", rec
            assert sorted(rec["release_files"]) == ["demo_pkg-1.0-cp310-cp310-win_amd64.whl",
                                                    "demo_pkg-1.0-py3-none-any.whl"]
            assert e.holding() == []
            assert len(rec["requests"]) == 1
            assert e.record(WIN)["release_files"] == rec["release_files"]
    finally:
        idx.stop()


def case_digest_mismatch():
    idx = Index()
    try:
        idx.add(WIN, make_wheel("good"), served=make_wheel("EVIL"))
        with Env() as e:
            rec = run(A(index_base=idx.base))
            assert rec["outcome"] == "refused" and rec["reason"].startswith("digest mismatch"), rec["reason"]
            assert e.holding() == [], e.holding()
            assert rec["held_path"] is None and rec["held_sha256"] is None
            assert rec["received_sha256"] != rec["published"]["sha256"]
    finally:
        idx.stop()


def case_size_mismatch_and_overrun():
    idx = Index()
    try:
        body = make_wheel()
        idx.add(WIN, body, served=body + b"X" * 5000)
        with Env() as e:
            rec = run(A(index_base=idx.base))
            assert rec["outcome"] == "refused" and rec["reason"].startswith("digest mismatch"), rec["reason"]
            assert e.holding() == [], e.holding()
    finally:
        idx.stop()


def case_other_host_url():
    other = Counter()
    idx = Index()
    try:
        idx.add(WIN, make_wheel(), url="%s/files/%s" % (other.base, WIN))
        with Env() as e:
            rec = run(A(index_base=idx.base))
            assert rec["outcome"] == "refused" and "closed set" in rec["reason"], rec["reason"]
            assert other.hits == [], other.hits
            assert e.holding() == []
            assert all(r["url"].startswith(idx.base) for r in rec["requests"])
    finally:
        idx.stop()
        other.stop()


def case_wrong_segment_url():
    idx = Index()
    try:
        idx.add(WIN, make_wheel(), url="%s/files/other-1.0-py3-none-any.whl" % idx.base)
        with Env() as e:
            rec = run(A(index_base=idx.base))
            assert rec["outcome"] == "refused" and "exact file name" in rec["reason"], rec["reason"]
            assert not any("/files/" in p for p in idx.requests), idx.requests
            assert e.holding() == []
    finally:
        idx.stop()


def case_redirect_other_host():
    other = Counter()
    idx = Index()
    try:
        idx.add(WIN, make_wheel(), redirect_to="%s/files/%s" % (other.base, WIN))
        with Env() as e:
            rec = run(A(index_base=idx.base))
            assert rec["outcome"] == "refused" and "closed set" in rec["reason"], rec["reason"]
            assert other.hits == [], other.hits
            assert e.holding() == []
            assert rec["requests"][-1]["status"] == 302
    finally:
        idx.stop()
        other.stop()


def case_redirect_same_host_followed():
    idx = Index()
    try:
        body = make_wheel()
        idx.add(WIN, body, redirect_to="/hop/" + WIN)
        with Env() as e:
            rec = run(A(index_base=idx.base))
            assert rec["outcome"] == "held", rec["reason"]
            assert [r["status"] for r in rec["requests"]] == [200, 200, 200, 302, 200], rec["requests"]
            assert e.holding() == [WIN]
    finally:
        idx.stop()


def case_redirect_hop_cap():
    idx = Index()
    try:
        idx.add(WIN, make_wheel(), redirect_to="/files/" + WIN)  # redirects to itself forever
        with Env() as e:
            rec = run(A(index_base=idx.base))
            assert rec["outcome"] == "refused" and "redirect hops" in rec["reason"], rec["reason"]
            file_hops = [r for r in rec["requests"] if "/files/" in r["url"]]
            assert len(file_hops) == T.MAX_HOPS + 1, len(file_hops)
            assert e.holding() == []
    finally:
        idx.stop()


def case_attestation_absent():
    idx = Index()
    try:
        idx.attestation_status = 404
        idx.add(WIN, make_wheel())
        with Env():
            rec = run(A(index_base=idx.base))
            assert rec["attestation"] == "absent", rec["attestation"]
            assert rec["outcome"] == "held"
            idx.attestation_status = 500
            rec2 = run(A(index_base=idx.base, batch="b2"))
            assert rec2["attestation"] == "unread", rec2["attestation"]
    finally:
        idx.stop()


def case_linux_name():
    idx = Index()
    try:
        idx.add(LIN, make_wheel("linux"))
        idx.add(WIN, make_wheel("win"))
        with Env() as e:
            rec = run(A(index_base=idx.base, python_tag="cp311", abi_tag="cp311",
                        platform_tag="manylinux2014_x86_64"))
            assert rec["requested"]["file_name"] == LIN, rec["requested"]
            assert rec["outcome"] == "held", rec["reason"]
            assert e.holding() == [LIN], e.holding()
            assert T.build_file_name("PyYAML", "6.0.3", "cp311", "cp311", "manylinux2014_x86_64") == \
                "pyyaml-6.0.3-cp311-cp311-manylinux2014_x86_64.whl"
            assert T.build_file_name("Typing-Extensions.x", "1", "py3", "none", "any") == \
                "typing_extensions_x-1-py3-none-any.whl"
    finally:
        idx.stop()


def case_index_spelling():
    idx = Index()
    try:
        idx.add(WIN, make_wheel(), spelling="Demo.Pkg-1.0-cp312-cp312-win_amd64.whl")
        with Env() as e:
            rec = run(A(index_base=idx.base))
            assert rec["outcome"] == "held", rec["reason"]
            assert rec["requested"]["file_name"] == WIN
            assert rec["index_file_name"] == "Demo.Pkg-1.0-cp312-cp312-win_amd64.whl"
            assert e.holding() == [WIN]
            # a different non-distribution part is never accepted
            idx.files.clear()
            idx.add("Demo.Pkg-1.0-cp312-cp312-win32.whl", make_wheel())
            rec2 = run(A(index_base=idx.base, batch="b2"))
            assert rec2["outcome"] == "refused" and rec2["reason"] == "no such file for this release"
    finally:
        idx.stop()


def case_yanked():
    idx = Index()
    try:
        idx.add(WIN, make_wheel(), yanked=True)
        with Env() as e:
            rec = run(A(index_base=idx.base))
            assert rec["outcome"] == "refused" and "yanked" in rec["reason"], rec["reason"]
            assert rec["published"]["yanked"] is True
            assert e.holding() == []
    finally:
        idx.stop()


def case_connection_error_one_retry():
    s = socket.socket()
    s.bind(("127.0.0.1", 0))
    port = s.getsockname()[1]
    s.close()  # nothing listens here: connection refused
    with Env():
        rec = run(A(index_base="http://127.0.0.1:%d" % port))
        assert rec["outcome"] == "failed" and "after one retry" in rec["reason"], rec["reason"]
        assert len(rec["requests"]) == 2, len(rec["requests"])
        assert rec["requests"][0].get("retried") is True and rec["requests"][1].get("error")


class Tripwire(Exception):
    pass


def case_public_without_approval_zero_sockets():
    calls = []
    orig_make, orig_gai, orig_conn = T.make_opener, socket.getaddrinfo, socket.socket.connect

    def boom(*a, **k):
        calls.append(a)
        raise Tripwire("a socket or name lookup was attempted")

    T.make_opener = boom
    socket.getaddrinfo = boom
    socket.socket.connect = boom
    try:
        with Env() as e:
            rec = run(A(name="pyyaml", version="6.0.3", python_tag="cp314", abi_tag="cp314"))
            assert rec["index_base"] == "https://pypi.org"
            assert rec["outcome"] == "refused" and "--approved-by" in rec["reason"], rec["reason"]
            assert rec["requests"] == [] and calls == [], calls
            assert os.path.isfile(os.path.join(e.records, "b1", rec["requested"]["file_name"] + ".fetch.json"))
            assert "requests=0 outcome=refused" in T.summary_line(rec)
            # an approval file that does not name the exact line is also refused with no socket
            ap = os.path.join(e.dir, "approval.txt")
            with open(ap, "w") as fh:
                fh.write("pyyaml==6.0.2\nrequests==6.0.3\n")
            rec = run(A(name="pyyaml", version="6.0.3", python_tag="cp314", abi_tag="cp314", approved_by=ap))
            assert rec["outcome"] == "refused" and "exact pyyaml==6.0.3" in rec["reason"], rec["reason"]
            assert rec["requests"] == [] and calls == [], calls
            assert rec["approval"]["sha256"] and rec["approval"]["matched"] is False
            rec = run(A(name="pyyaml", version="6.0.3", python_tag="cp314", abi_tag="cp314",
                        approved_by=os.path.join(e.dir, "missing.txt")))
            assert rec["outcome"] == "refused" and "does not exist" in rec["reason"]
            assert calls == []
            # a non-public, non-loopback base without approval is refused the same way
            rec = run(A(index_base="https://example.invalid"))
            assert rec["outcome"] == "refused" and rec["requests"] == [] and calls == []
            # difference control: a valid approval DOES reach the opener (which is the tripwire,
            # so nothing leaves; the fetch ends failed with its connection errors recorded)
            with open(ap, "w") as fh:
                fh.write("batch approved\npyyaml==6.0.3\n")
            T.make_opener = lambda loopback: (_ for _ in ()).throw(urllib.error.URLError("tripwire"))
            rec = run(A(name="pyyaml", version="6.0.3", python_tag="cp314", abi_tag="cp314", approved_by=ap))
            assert rec["outcome"] == "failed" and len(rec["requests"]) == 2, rec
            assert rec["approval"]["matched"] is True
            assert rec["requests"][0]["url"] == "https://pypi.org/pypi/pyyaml/6.0.3/json"
    finally:
        T.make_opener, socket.getaddrinfo, socket.socket.connect = orig_make, orig_gai, orig_conn


def case_public_host_rule():
    p = T.Policy("https://pypi.org")
    p.check("https://pypi.org/pypi/x/1/json")
    p.check("https://files.pythonhosted.org/packages/ab/cd/x-1-py3-none-any.whl", "x-1-py3-none-any.whl")
    for bad in ("http://pypi.org/pypi/x/1/json", "https://evil.example/x.whl", "https://pypi.org.evil.example/x",
                "https://user:pw@pypi.org/x", "https://pypi.org:8443/x", "ftp://pypi.org/x"):
        try:
            p.check(bad)
        except T.Refuse:
            continue
        raise AssertionError("not refused: " + bad)
    try:
        p.check("https://files.pythonhosted.org/a/b/other.whl", "x-1-py3-none-any.whl")
    except T.Refuse:
        pass
    else:
        raise AssertionError("segment not enforced")
    q = T.Policy("http://127.0.0.1:5555")
    q.check("http://127.0.0.1:5555/files/a.whl", "a.whl")
    for bad in ("http://127.0.0.1:5556/a", "http://localhost:5555/a", "http://example.com:5555/a", "ftp://127.0.0.1:5555/a"):
        try:
            q.check(bad)
        except T.Refuse:
            continue
        raise AssertionError("not refused: " + bad)
    assert T.is_loopback_base("http://localhost:1") and T.is_loopback_base("http://[::1]:1")
    assert not T.is_loopback_base("https://pypi.org")


def case_list_reads_batch():
    idx = Index()
    try:
        idx.add(WIN, make_wheel())
        idx.add(LIN, make_wheel("l"), served=make_wheel("bad"))
        with Env() as e:
            run(A(index_base=idx.base))
            run(A(index_base=idx.base, python_tag="cp311", abi_tag="cp311", platform_tag="manylinux2014_x86_64"))
            run(A(index_base=idx.base, python_tag="cp39", abi_tag="cp39"))  # no such file -> refused
            out = subprocess.run([sys.executable, os.path.join(HERE, "intake_fetch.py"), "list", "--batch", "b1"],
                                 capture_output=True, text=True, timeout=60, env=dict(os.environ))
            lines = out.stdout.strip().splitlines()
            assert out.returncode == 0, out.stderr
            assert lines[-1] == "INTAKE-HELD batch=b1 records=3 held=1 refused=2 failed=0", lines[-1]
            assert any(WIN in ln and "outcome=held" in ln and SERIAL in ln and "in-holding" in ln for ln in lines), lines
            assert e.holding() == [WIN]
            empty = subprocess.run([sys.executable, os.path.join(HERE, "intake_fetch.py"), "list", "--batch", "nobatch"],
                                   capture_output=True, text=True, timeout=60, env=dict(os.environ))
            assert empty.stdout.strip().splitlines()[-1] == "INTAKE-HELD batch=nobatch records=0 held=0 refused=0 failed=0"
    finally:
        idx.stop()


def case_cli_last_line():
    idx = Index()
    try:
        body = make_wheel()
        idx.add(WIN, body)
        with Env() as e:
            out = subprocess.run(
                [sys.executable, os.path.join(HERE, "intake_fetch.py"), "fetch", "--batch", "b1", "--name", "demo-pkg",
                 "--version", "1.0", "--python-tag", "cp312", "--abi-tag", "cp312", "--platform-tag", "win_amd64",
                 "--index-base", idx.base],
                capture_output=True, text=True, timeout=60, env=dict(os.environ))
            last = out.stdout.strip().splitlines()[-1]
            pat = (r"^INTAKE-FETCH batch=b1 file=%s requests=4 outcome=held sha256=%s bytes=%d attestation=present$"
                   % (re.escape(WIN), hashlib.sha256(body).hexdigest()[:12], len(body)))
            assert out.returncode == 0 and re.match(pat, last), (out.returncode, last, out.stderr)
            assert e.holding() == [WIN]
    finally:
        idx.stop()


def case_record_is_ascii_and_rewrites_safe():
    idx = Index()
    try:
        idx.add(WIN, make_wheel(), yanked=False)
        with Env() as e:
            first = run(A(index_base=idx.base))
            assert first["outcome"] == "held"
            idx.files[WIN]["spelling"] = WIN
            idx.files.clear()
            idx.add("other-1.0-py3-none-any.whl", make_wheel())
            second = run(A(index_base=idx.base))  # refused: the held record must stay authoritative
            assert second["outcome"] == "refused"
            assert e.record(WIN)["outcome"] == "held"
            names = os.listdir(os.path.join(e.records, "b1"))
            assert any(n.endswith(".attempt.json") for n in names), names
            for n in names:
                with open(os.path.join(e.records, "b1", n), "rb") as fh:
                    fh.read().decode("ascii")
    finally:
        idx.stop()


CASES = [
    case_happy, case_missing_file, case_digest_mismatch, case_size_mismatch_and_overrun, case_other_host_url,
    case_wrong_segment_url, case_redirect_other_host, case_redirect_same_host_followed, case_redirect_hop_cap,
    case_attestation_absent, case_linux_name, case_index_spelling, case_yanked, case_connection_error_one_retry,
    case_public_without_approval_zero_sockets, case_public_host_rule, case_list_reads_batch, case_cli_last_line,
    case_record_is_ascii_and_rewrites_safe,
]


def main():
    ok = 0
    for fn in CASES:
        try:
            fn()
            print("PASS: %s" % fn.__name__)
            ok += 1
        except Exception:
            print("FAIL: %s" % fn.__name__)
            traceback.print_exc(file=sys.stdout)
    print("INTAKE-FETCH-TEST cases=%d/%d ok=%s" % (ok, len(CASES), ok == len(CASES)))
    return 0 if ok == len(CASES) else 1


if __name__ == "__main__":
    sys.exit(main())
