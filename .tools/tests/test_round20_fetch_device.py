#!/usr/bin/env python3
"""Round-20 fetch device key and wrapper refusal (NFRA_CTLPLN CT-aj-1, FWD-19 and FWD-18 laptop arm).

--device  one fetch through the real org/devices/intake/intake_fetch.py code path. Its index is a local loopback stub
          (no network). The record must carry device (from AGENTBUS_DEVICE); the downloads reader counts it for that
          device; a record with no device key, or a null device, is counted under unattributed and never for a box.
--wrapper the kit's `wrap -- download six` in a child process whose environment has PIP_NO_INDEX=1 and every index and
          proxy variable pointed at a counting loopback listener: exit code non-zero, zero connections, and the refusal
          text names org/devices/intake.

Last line: FETCH-DEVICE arms=<k>/<n> ok=<True|False>, or WRAPPER-REFUSAL rc=<rc> names_route=<True|False> ok=<True|False>.
"""
import hashlib
import http.server
import json
import os
import shutil
import socket
import socketserver
import subprocess
import sys
import tempfile
import threading
import time

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.normpath(os.path.join(HERE, "..", ".."))
FETCH = os.path.join(REPO, "org", "devices", "intake", "intake_fetch.py")
REQUEST = os.path.join(REPO, "org", "devices", "intake", "intake_request.py")
KIT = os.path.join(REPO, "org", "devices", "kit_pip_no_egress.py")
SERIAL = "0.9.0_WK_NFRA_CTLPLN~112"
DEVICE = "laptop"
OTHER = "dell1"
FILE = "six-1.16.0-py3-none-any.whl"
BODY = b"round-20 stub wheel bytes\n"
BATCH = "rt20-a"
NO_DEVICE_BATCH = "rt20-b"
NO_SUCH_REG_KEY = "HKCU\\Software\\OpalRound20NoSuchKey"
ROUTE = "org/devices/intake"


def last_line(text):
    lines = [x for x in text.splitlines() if x.strip()]
    return lines[-1] if lines else ""


def read_json(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh)


def write_json(path, doc):
    with open(path, "w", encoding="ascii", newline="\n") as fh:
        fh.write(json.dumps(doc, indent=2) + "\n")


class IndexStub:
    """Loopback index answering the three documents intake_fetch.py reads for one exact file."""

    def __init__(self):
        self.port = 0
        outer = self

        class Handler(http.server.BaseHTTPRequestHandler):
            def log_message(self, fmt, *args):
                pass

            def _send(self, status, body, ctype):
                self.send_response(status)
                self.send_header("Content-Type", ctype)
                self.send_header("Content-Length", str(len(body)))
                self.end_headers()
                self.wfile.write(body)

            def do_GET(self):
                base = "http://127.0.0.1:%d" % outer.port
                sha = hashlib.sha256(BODY).hexdigest()
                if self.path == "/pypi/six/1.16.0/json":
                    doc = {"urls": [{"filename": FILE, "url": base + "/files/" + FILE,
                                     "digests": {"sha256": sha}, "size": len(BODY),
                                     "upload_time_iso_8601": "2021-05-05T00:00:00Z",
                                     "yanked": False, "requires_python": ">=2.7"}]}
                    return self._send(200, json.dumps(doc).encode("ascii"), "application/json")
                if self.path == "/pypi/six/json":
                    doc = {"releases": {"1.15.0": [{"upload_time_iso_8601": "2020-01-01T00:00:00Z"}],
                                        "1.16.0": [{"upload_time_iso_8601": "2021-05-05T00:00:00Z"}]}}
                    return self._send(200, json.dumps(doc).encode("ascii"), "application/json")
                if self.path == "/files/" + FILE:
                    return self._send(200, BODY, "application/octet-stream")
                return self._send(404, b"{}", "application/json")

        self.server = http.server.ThreadingHTTPServer(("127.0.0.1", 0), Handler)
        self.port = self.server.server_address[1]
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def close(self):
        self.server.shutdown()
        self.server.server_close()


def run_fetch(env_extra, batch, index_base):
    env = dict(os.environ)
    env.update(env_extra)
    cmd = [sys.executable, FETCH, "fetch", "--batch", batch, "--name", "six", "--version", "1.16.0",
           "--python-tag", "py3", "--abi-tag", "none", "--platform-tag", "any", "--index-base", index_base]
    p = subprocess.run(cmd, capture_output=True, text=True, env=env, timeout=120)
    return p.returncode, p.stdout, p.stderr


def run_downloads(intake, device, day):
    cmd = [sys.executable, REQUEST, "downloads", "--device", device, "--day", day, "--root", intake]
    p = subprocess.run(cmd, capture_output=True, text=True, env=dict(os.environ), timeout=120)
    return p.returncode, last_line(p.stdout)


def load_or_none(path):
    try:
        return read_json(path)
    except (OSError, ValueError):
        return None


def device_arms():
    tmp = tempfile.mkdtemp(prefix="round20_fetch_device_")
    stub = IndexStub()
    results = []

    def arm(label, ok):
        results.append(bool(ok))
        print("ARM %-2d %s %s" % (len(results), "PASS" if ok else "FAIL", label))

    try:
        intake = os.path.join(tmp, "intake")
        records = os.path.join(intake, "records")
        holding = os.path.join(tmp, "holding")
        os.makedirs(intake)
        index = "http://127.0.0.1:%d" % stub.port
        base_env = {"OPAL_INTAKE_ROOT": holding, "OPAL_INTAKE_RECORDS": records, "OPAL_AGENT_SERIAL": SERIAL}

        rc, out, _err = run_fetch(dict(base_env, AGENTBUS_DEVICE=DEVICE), BATCH, index)
        rec = load_or_none(os.path.join(records, BATCH, FILE + ".fetch.json"))
        arm("fetch through intake_fetch.py against the loopback stub: rc 0, outcome held",
            rc == 0 and "outcome=held" in last_line(out))
        arm("the fetch record carries device=%s, derived from AGENTBUS_DEVICE" % DEVICE,
            rec is not None and rec.get("device") == DEVICE)
        arm("the fetch record keeps schema intake-fetch/1 and names the fetching seat",
            rec is not None and rec.get("schema") == "intake-fetch/1" and rec.get("fetched_by") == SERIAL)

        if rec is None:
            day, n_req = "19990101", 0
        else:
            day, n_req = rec["at"][:10].replace("-", ""), len(rec["requests"])
        # an old-shape record (no device key) and a null-device record, both on the same day
        os.makedirs(os.path.join(records, "rt20-old"))
        write_json(os.path.join(records, "rt20-old", "old_shape.whl.fetch.json"),
                   {"schema": "intake-fetch/1", "at": rec["at"] if rec else "1999-01-01T00:00:00Z",
                    "requests": [{"url": "u"}]})
        write_json(os.path.join(records, "rt20-old", "null_device.whl.fetch.json"),
                   {"schema": "intake-fetch/1", "device": None, "at": rec["at"] if rec else "1999-01-01T00:00:00Z",
                    "requests": [{"url": "u"}, {"url": "v"}]})

        rc_l, line_l = run_downloads(intake, DEVICE, day)
        arm("downloads %s %s: the fetch record counted (requests=%d files=1), old and null records unattributed=2"
            % (DEVICE, day, n_req),
            rc_l == 0 and line_l == "DOWNLOADS-TODAY device=%s day=%s requests=%d files=1 unattributed=2"
            % (DEVICE, day, n_req))
        rc_o, line_o = run_downloads(intake, OTHER, day)
        arm("downloads %s %s: the laptop record is not counted for another box (unattributed=2 is not theirs)"
            % (OTHER, day),
            rc_o == 0 and line_o == "DOWNLOADS-TODAY device=%s day=%s requests=0 files=0 unattributed=2"
            % (OTHER, day))
        rc_e, line_e = run_downloads(intake, DEVICE, "19990101")
        arm("downloads %s on a day with no records: zero, unattributed=0" % DEVICE,
            rc_e == 0 and line_e == "DOWNLOADS-TODAY device=%s day=19990101 requests=0 files=0 unattributed=0" % DEVICE)

        # a box that cannot be named: the record carries device null and is never guessed to belong to a box
        rc2, out2, _err2 = run_fetch({"OPAL_INTAKE_ROOT": holding, "OPAL_INTAKE_RECORDS": records,
                                      "OPAL_AGENT_SERIAL": SERIAL, "AGENTBUS_DEVICE": "",
                                      "AGENTBUS_REG_KEY": NO_SUCH_REG_KEY}, NO_DEVICE_BATCH, index)
        rec2 = load_or_none(os.path.join(records, NO_DEVICE_BATCH, FILE + ".fetch.json"))
        arm("a fetch on an unnamed box: rc 0, record carries device null",
            rc2 == 0 and rec2 is not None and "device" in rec2 and rec2.get("device") is None)
        rc_3, line_3 = run_downloads(intake, DEVICE, day)
        arm("downloads %s %s after the unnamed fetch: unattributed=3, files still 1" % (DEVICE, day),
            rc_3 == 0 and line_3 == "DOWNLOADS-TODAY device=%s day=%s requests=%d files=1 unattributed=3"
            % (DEVICE, day, n_req))
    finally:
        stub.close()
        shutil.rmtree(tmp, ignore_errors=True)
    k, n = sum(results), len(results)
    return k, n, k == n


class CountingListener:
    def __init__(self):
        self.hits = []
        hits = self.hits

        class Handler(socketserver.BaseRequestHandler):
            def handle(self):
                hits.append(self.client_address)

        self.server = socketserver.ThreadingTCPServer(("127.0.0.1", 0), Handler)
        self.server.daemon_threads = True
        self.port = self.server.server_address[1]
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def close(self):
        self.server.shutdown()
        self.server.server_close()


def wrapper_check():
    listener = CountingListener()
    try:
        url = "http://127.0.0.1:%d" % listener.port
        # positive control: a connection from this process reaches the listener and is counted
        socket.create_connection(("127.0.0.1", listener.port), timeout=5).close()
        deadline = time.time() + 5
        while not listener.hits and time.time() < deadline:
            time.sleep(0.05)
        control_ok = len(listener.hits) == 1
        listener.hits.clear()

        env = dict(os.environ)
        env.update({"PIP_NO_INDEX": "1", "PIP_INDEX_URL": url + "/simple/", "PIP_EXTRA_INDEX_URL": url + "/simple/",
                    "HTTP_PROXY": url, "HTTPS_PROXY": url, "http_proxy": url, "https_proxy": url})
        p = subprocess.run([sys.executable, KIT, "wrap", "--", "download", "six"],
                           capture_output=True, text=True, env=env, timeout=120)
        time.sleep(0.5)
        text = p.stdout + p.stderr
        rc = p.returncode
        names_route = ROUTE in text
        no_network = len(listener.hits) == 0
        print(text.rstrip())
        print("ARM 1  %s positive control: the counting listener sees one connection from this process"
              % ("PASS" if control_ok else "FAIL"))
        print("ARM 2  %s child exit code non-zero (rc=%d)" % ("PASS" if rc != 0 else "FAIL", rc))
        print("ARM 3  %s refusal text names %s" % ("PASS" if names_route else "FAIL", ROUTE))
        print("ARM 4  %s zero connections to the counting listener (hits=%d), PIP_NO_INDEX=1 in the child"
              % ("PASS" if no_network else "FAIL", len(listener.hits)))
        ok = bool(control_ok and rc != 0 and names_route and no_network)
        return rc, names_route, ok
    finally:
        listener.close()


def main(argv):
    if "--device" in argv:
        k, n, ok = device_arms()
        print("FETCH-DEVICE arms=%d/%d ok=%s" % (k, n, ok))
        return 0 if ok else 1
    if "--wrapper" in argv:
        rc, names_route, ok = wrapper_check()
        print("WRAPPER-REFUSAL rc=%d names_route=%s ok=%s" % (rc, names_route, ok))
        return 0 if ok else 1
    print("usage: test_round20_fetch_device.py --device | --wrapper", file=sys.stderr)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
