"""kit_pip_no_egress.py -- measure which disarm of pip's package-index access works on THIS box's pip, and wrap pip with it.

THE HAZARD: `python -m pip download <name> --index-url <public index>` fetches a public package without asking, and an explicit
--index-url overrides an index set in the environment or in a config file. A disabled index and a failed fetch can print similar
errors, so only a listener that COUNTS REQUESTS tells them apart. The measured defect was exactly that explicit flag, so every
candidate is also run with the explicit loopback index set after its disarm is applied.

THE ONE RULE: NO REQUEST MAY LEAVE THIS MACHINE. Every pip process this tool starts runs inside a harness with two independent
redirects to loopback:
  Redirect A (index): the index set to http://127.0.0.1:<port>/simple/ (a listener that logs method and path, answers 404).
  Redirect B (proxy): HTTP_PROXY / HTTPS_PROXY / http_proxy / https_proxy set to a SECOND loopback listener that logs every
    request line (CONNECT included) and answers 502; NO_PROXY / no_proxy empty.
The package every probe asks for is a name with a random suffix, so even a leak would retrieve nothing. Each run uses a fresh
directory outside every git tree, its own HOME, cache and temporary directory, and PIP_CONFIG_FILE set to the null device so
that no ambient configuration is read. The tool never names a public host except as a string it refuses.

  measure [--out <json>] [--tmp-base <dir>]   the order of proof, then each candidate disarm, plain and with the explicit index.
  wrap [--from <json>] -- <pip args>          run python -m pip with the wrapper form applied: refuse every download verb, every
                                              request-making argument and every http(s) or other network URL, run nothing else.
  selfcheck                                   test the two listeners with Python-made requests; starts NO pip process.

Candidates: (a) PIP_NO_INDEX=1 in the environment; (b) a config file with no-index = true; (c) a config file whose index-url is a
dead loopback port; (d) the wrapper form. (b) is measured as the config file pip reads from PIP_CONFIG_FILE, because pip finds the
per-user file on Windows through the shell and this tool cannot redirect that lookup and writes nothing there. A candidate passes
only when its command makes ZERO requests to either listener, does not time out, and exits non-zero naming the probe package (the
wrapper: its refusal line and rc 3). holds_against_explicit counts the candidates that passed AND still held with the explicit index.
form= names the first non-wrapper candidate that holds; form=wrapper-only means no non-wrapper candidate holds against the explicit
index and only the wrapper does; form=NONE means no candidate holds. ok reflects the harness (positive reached, no public host seen,
no regression, no early stop), not whether a disarm exists.

LIMIT: the wrapper is bypassed by anyone who types a different interpreter or calls pip without it; the real control is a network
egress policy, which is outside this cell.

LAST line of measure: PIP-NO-EGRESS pip=<v> positive_requests=<n> candidates=<k> passing=<p> holds_against_explicit=<h> leaked_public=<0|n> form=<form|NONE> ok=<True|False>
"""
from __future__ import annotations

import argparse
import http.server
import json
import os
import pathlib
import re
import secrets
import shutil
import socket
import socketserver
import subprocess
import sys
import tempfile
import threading
import time

TIMEOUT = 60
LOOPBACK = "127.0.0.1"
PROXY_VARS = ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy")
NOPROXY_VARS = ("NO_PROXY", "no_proxy")
REFUSAL = ("REFUSED: this box does not download. Ask the laptop: org/devices/intake/ (request, check, Taildrop). "
           "No request was made.")
NOT_ALLOWED = ("REFUSED: not on the no-egress list (list, show, freeze, check, --version, --help, "
               "install --no-index --no-deps <local file>): %s. No request was made.")
OUTDATED = "REFUSED: list --outdated asks the index for newer versions. No request was made."
REFUSED_RC = 3
# Added to every pip process the harness starts, so that a 502 answer is not retried (the retry sleeps would exceed the bound).
RETRY_ARGS = ["--retries", "0", "--timeout", "5"]
DOWNLOAD_VERBS = ("install", "download", "wheel", "index", "search")
ALLOWED_VERBS = ("list", "show", "freeze", "check")
INFO_FLAGS = ("--version", "-V", "--help", "-h")
OUTDATED_FLAGS = ("--outdated", "-o", "--uptodate", "-u")
REQUIREMENT_FLAGS = ("-r", "--requirement", "-e", "--editable")
# pip options that take a separate value; the verb is the first positional argument after skipping these and their values.
VALUE_OPTIONS = ("--index-url", "--extra-index-url", "--find-links", "-i", "-f", "--cache-dir", "--log", "--proxy", "--retries",
                 "--timeout", "--exists-action", "--trusted-host", "--cert", "--client-cert", "--progress-bar",
                 "--root-user-action", "--src", "--keyring-provider", "--use-feature", "--use-deprecated", "--python-version",
                 "--platform", "--abi", "--implementation", "--target", "-t", "--prefix", "--root", "--dest", "-d", "-c",
                 "--constraint", "-r", "--requirement", "-e", "--editable", "--config-settings", "-C", "--build-option",
                 "--global-option", "--install-option", "--report", "--format", "--path", "--exclude", "--only-binary",
                 "--no-binary")
URL_SCHEME = re.compile(r"([a-z][a-z0-9+.-]*)://", re.I)
VCS_PREFIX = re.compile(r"^(git|hg|svn|bzr)\+", re.I)
CANDIDATE_ORDER = ("env:PIP_NO_INDEX", "config:no-index", "config:index-url-dead-loopback", "wrapper")


def asc(text):
    return str(text).encode("ascii", "replace").decode("ascii")


def first_line(text):
    for line in str(text).splitlines():
        if line.strip():
            return line.strip()
    return ""


# ------------------------------------------------------------------------------------------------------------------ listeners
class Log:
    def __init__(self):
        self.lock = threading.Lock()
        self.items = []

    def add(self, line):
        with self.lock:
            self.items.append(line)

    def take(self):
        with self.lock:
            out, self.items = self.items, []
        return out


class IndexListener:
    """Loopback package-index stand-in: logs 'METHOD path host=<Host>' for every request, answers 404."""

    def __init__(self):
        self.log = Log()
        log = self.log

        class Handler(http.server.BaseHTTPRequestHandler):
            protocol_version = "HTTP/1.1"

            def answer(self):
                log.add("%s %s host=%s" % (self.command, self.path, self.headers.get("Host", "")))
                body = b'{"error":"not found"}'
                self.send_response(404)
                self.send_header("Content-Type", "application/json")
                self.send_header("Content-Length", str(len(body)))
                self.send_header("Connection", "close")
                self.end_headers()
                if self.command != "HEAD":
                    self.wfile.write(body)
                self.close_connection = True

            do_GET = do_HEAD = do_POST = do_PUT = do_DELETE = do_PATCH = do_OPTIONS = answer

            def log_message(self, *args):
                return

        self.server = http.server.ThreadingHTTPServer((LOOPBACK, 0), Handler)
        self.server.daemon_threads = True
        self.port = self.server.server_address[1]
        self.url = "http://%s:%d/simple/" % (LOOPBACK, self.port)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def close(self):
        self.server.shutdown()
        self.server.server_close()


class ProxyListener:
    """Loopback proxy stand-in: logs every request line (CONNECT host:port, or an absolute-URI GET) and answers 502, then closes.
    A connection that sends nothing is logged too, as '(empty-connection)': it is counted, never ignored."""

    def __init__(self):
        self.log = Log()
        log = self.log

        class Handler(socketserver.StreamRequestHandler):
            def handle(self):
                self.request.settimeout(5)
                request_line = ""
                host = ""
                try:
                    request_line = self.rfile.readline(65536).decode("latin-1").strip()
                    while request_line:
                        header = self.rfile.readline(65536).decode("latin-1")
                        if header in ("", "\r\n", "\n"):
                            break
                        if header.lower().startswith("host:"):
                            host = header.split(":", 1)[1].strip()
                except OSError:
                    pass
                log.add("%s | host=%s" % (request_line, host) if request_line else "(empty-connection)")
                try:
                    self.wfile.write(b"HTTP/1.1 502 Bad Gateway\r\nContent-Length: 0\r\nConnection: close\r\n\r\n")
                    self.wfile.flush()
                except OSError:
                    pass

        class Server(socketserver.ThreadingTCPServer):
            allow_reuse_address = True
            daemon_threads = True

        self.server = Server((LOOPBACK, 0), Handler)
        self.port = self.server.server_address[1]
        self.url = "http://%s:%d" % (LOOPBACK, self.port)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def close(self):
        self.server.shutdown()
        self.server.server_close()


def request_host(log_line):
    """The host a logged request names: CONNECT host:port, an absolute-URI request, else the Host header; '' when unknown."""
    m = re.match(r"^CONNECT\s+(\[[^\]]+\]|[^:\s]+)(?::\d+)?\s", log_line)
    if m:
        return m.group(1).strip("[]").lower()
    m = re.match(r"^[A-Z]+\s+[a-z]+://(\[[^\]]+\]|[^/:\s]+)", log_line)
    if m:
        return m.group(1).strip("[]").lower()
    m = re.search(r"host=([^\s:|]+|\[[^\]]+\])", log_line)
    return m.group(1).strip("[]").lower() if m else ""


def is_loopback(host):
    return host in ("localhost", "::1") or host.startswith("127.")


def public_hosts(lines):
    """The lines of a proxy log that name a host which is not loopback; an unreadable line counts as public."""
    return [x for x in lines if not is_loopback(request_host(x))]


def selfcheck_listeners():
    """Python-made requests to both listeners, BEFORE any pip process: each must log exactly what was sent. Returns a dict."""
    idx, prx = IndexListener(), ProxyListener()
    try:
        conn = socket.create_connection((LOOPBACK, idx.port), timeout=5)
        conn.sendall(b"GET /simple/selfcheck-index/ HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n")
        reply_idx = conn.recv(4096).decode("latin-1")
        conn.close()
        conn = socket.create_connection((LOOPBACK, prx.port), timeout=5)
        conn.sendall(b"CONNECT selfcheck.invalid:443 HTTP/1.1\r\nHost: selfcheck.invalid:443\r\n\r\n")
        reply_connect = conn.recv(4096).decode("latin-1")
        conn.close()
        conn = socket.create_connection((LOOPBACK, prx.port), timeout=5)
        conn.sendall(b"GET http://selfcheck.invalid/x HTTP/1.1\r\nHost: selfcheck.invalid\r\n\r\n")
        reply_get = conn.recv(4096).decode("latin-1")
        conn.close()
        time.sleep(0.2)
        idx_log, prx_log = idx.log.take(), prx.log.take()
    finally:
        idx.close()
        prx.close()
    result = {
        "index_log": idx_log, "proxy_log": prx_log,
        "index_answers_404": reply_idx.startswith("HTTP/1.1 404"),
        "proxy_answers_502_connect": reply_connect.startswith("HTTP/1.1 502"),
        "proxy_answers_502_get": reply_get.startswith("HTTP/1.1 502"),
        "index_logged_one": len(idx_log) == 1 and idx_log[0].startswith("GET /simple/selfcheck-index/"),
        "proxy_logged_two": len(prx_log) == 2 and prx_log[0].startswith("CONNECT selfcheck.invalid:443")
        and prx_log[1].startswith("GET http://selfcheck.invalid/x"),
        "proxy_public_hosts_seen": len(public_hosts(prx_log)),
    }
    result["ok"] = all(result[k] for k in ("index_answers_404", "proxy_answers_502_connect", "proxy_answers_502_get",
                                           "index_logged_one", "proxy_logged_two")) and result["proxy_public_hosts_seen"] == 2
    return result


# ------------------------------------------------------------------------------------------------------------------ isolation
def ancestor_problems(path):
    """Every ancestor of `path` (itself included) that holds a node_modules, package.json or .git entry."""
    found = []
    here = pathlib.Path(path).resolve()
    for anc in [here] + list(here.parents):
        for name in ("node_modules", "package.json", ".git"):
            if (anc / name).exists():
                found.append("%s holds %s" % (anc, name))
    return found


def pick_tmp_base(explicit=None):
    """A base directory whose every ancestor is clean. Tries the explicit one, the system temporary directory, then <drive root>/tmp
    (the drive prefix is derived from the system temporary directory, never written here)."""
    candidates = []
    if explicit:
        candidates.append(pathlib.Path(explicit))
    sys_tmp = pathlib.Path(tempfile.gettempdir()).resolve()
    candidates.append(sys_tmp)
    candidates.append(pathlib.Path(sys_tmp.anchor) / "tmp")
    rejected = []
    for cand in candidates:
        cand.mkdir(parents=True, exist_ok=True)
        problems = ancestor_problems(cand)
        if not problems:
            return cand, rejected
        rejected.append((str(cand), problems))
    raise RuntimeError("no clean temporary base: " + asc(rejected))


def ambient(name):
    up = name.upper()
    return (up.startswith("PIP_") or "PROXY" in up or up in ("NO_PROXY", "REQUESTS_CA_BUNDLE", "CURL_CA_BUNDLE", "SSL_CERT_FILE",
                                                             "PYTHONPATH", "PYTHONUSERBASE") or up.startswith("XDG_"))


def build_env(root, proxy_url, extra_env):
    """The child's environment only (passed as an environment dictionary; this process's own environment is never changed)."""
    home = root / "home"
    cache = root / "cache"
    tmp = root / "tmp"
    for d in (home, cache, tmp, home / "AppData" / "Roaming", home / "AppData" / "Local"):
        d.mkdir(parents=True, exist_ok=True)
    env = {k: v for k, v in os.environ.items() if not ambient(k)}
    drive, tail = os.path.splitdrive(str(home))
    env.update({
        "HOME": str(home), "USERPROFILE": str(home), "HOMEDRIVE": drive, "HOMEPATH": tail or "\\",
        "APPDATA": str(home / "AppData" / "Roaming"), "LOCALAPPDATA": str(home / "AppData" / "Local"),
        "TEMP": str(tmp), "TMP": str(tmp), "TMPDIR": str(tmp),
        "PIP_CACHE_DIR": str(cache), "PIP_CONFIG_FILE": os.devnull, "PIP_DISABLE_PIP_VERSION_CHECK": "1",
        "PIP_NO_INPUT": "1", "PYTHONNOUSERSITE": "1", "PYTHONDONTWRITEBYTECODE": "1", "NO_COLOR": "1",
    })
    if proxy_url:
        for name in PROXY_VARS:
            env[name] = proxy_url
        for name in NOPROXY_VARS:
            env[name] = ""
    env.update(extra_env or {})
    return env


class Harness:
    """Owns the two listeners, the probe name, the dead port, the temporary base and the arm runner. One instance per measure run."""

    def __init__(self, tmp_base=None):
        self.base, self.rejected_bases = pick_tmp_base(tmp_base)
        self.run_root = pathlib.Path(tempfile.mkdtemp(prefix="kit-pip-noegress-", dir=str(self.base)))
        self.index = IndexListener()
        self.prx = ProxyListener()
        self.package = "opal-no-such-pkg-%s" % secrets.token_hex(8)
        probe = socket.socket()
        probe.bind((LOOPBACK, 0))
        self.dead_port = probe.getsockname()[1]
        probe.close()
        self.kit = pathlib.Path(__file__).resolve()
        self.pip_version = "unknown"
        self.arms = []
        self.counter = 0

    def close(self):
        self.index.close()
        self.prx.close()
        shutil.rmtree(str(self.run_root), ignore_errors=True)

    def download_args(self, index_url=None):
        """The command every candidate runs: a download of the probe name into a relative directory of the arm's own probe directory."""
        args = ["download", "--no-deps", "-d", "out", self.package] + list(RETRY_ARGS)
        if index_url:
            args += ["--index-url", index_url]
        return args

    def arm(self, name, role, pip_args, env_extra=None, config_text=None, wrapped=False):
        """One pip process (or one wrapper process), from its own fresh directory, inside the harness. Returns the arm record."""
        self.counter += 1
        root = self.run_root / ("arm%02d" % self.counter)
        probe_dir = root / "probe"
        probe_dir.mkdir(parents=True)
        problems = ancestor_problems(probe_dir)
        if problems:
            raise RuntimeError("probe directory has a node_modules/package.json/.git ancestor: " + asc(problems))
        extra = dict(env_extra or {})
        if config_text is not None:
            cfg_dir = root / "pipconfig"
            cfg_dir.mkdir()
            cfg = cfg_dir / "pip.conf"
            cfg.write_text(config_text, encoding="ascii")
            extra["PIP_CONFIG_FILE"] = str(cfg)
        env = build_env(root, self.prx.url, extra)
        if wrapped:
            command = [sys.executable, str(self.kit), "wrap", "--"] + list(pip_args)
        else:
            command = [sys.executable, "-m", "pip"] + list(pip_args)
        self.index.log.take()
        self.prx.log.take()
        out_path = root / "out.txt"
        started = time.time()
        timed_out = False
        rc = None
        with open(str(out_path), "wb") as sink:
            try:
                proc = subprocess.run(command, cwd=str(probe_dir), env=env, stdout=sink, stderr=subprocess.STDOUT,
                                      stdin=subprocess.DEVNULL, timeout=TIMEOUT)
                rc = proc.returncode
            except subprocess.TimeoutExpired:
                timed_out = True
                rc = "TIMEOUT"
        elapsed = time.time() - started
        time.sleep(0.3)
        index_log = self.index.log.take()
        prx_log = self.prx.log.take()
        text = out_path.read_bytes().decode("utf-8", "replace")
        text = re.sub(r"\x1b\[[0-9;]*[A-Za-z]", "", text)
        if wrapped:
            named = REFUSAL in text and rc == REFUSED_RC
        else:
            named = self.package in text
        err_lines = [x.strip() for x in text.splitlines() if "error" in x.lower() or "refused" in x.lower()]
        record = {
            "name": name, "role": role, "command_tail": [asc(x) for x in pip_args], "wrapped": bool(wrapped),
            "env_extra_keys": sorted((env_extra or {}).keys()), "config_text": config_text,
            "index_url_in_args": "--index-url" in list(pip_args),
            "proxy_env": {k: env.get(k) for k in PROXY_VARS + NOPROXY_VARS},
            "requests_index": len(index_log), "requests_proxy": len(prx_log),
            "index_log": index_log, "proxy_log": prx_log,
            "rc": rc, "timed_out": timed_out, "seconds": round(elapsed, 2), "named": bool(named),
            "first_error_line": asc((err_lines or [first_line(text)])[0])[:300],
            "output_full": asc(text)[:40000],
            "leaked_public": len(public_hosts(prx_log)),
            "passed": None,
        }
        self.arms.append(record)
        return record


# ------------------------------------------------------------------------------------------------------------------ grading
def grade_arm(arm, positive_requests):
    """PASS only with zero requests on BOTH listeners, no timeout, the probe package (or the wrapper refusal) named in the output,
    and the same run's positive arm non-zero."""
    return bool(positive_requests > 0 and arm["requests_index"] == 0 and arm["requests_proxy"] == 0 and not arm["timed_out"]
                and arm["named"])


def audit_grades(arms):
    """Independent re-check of every graded arm: a PASS with any request or a timeout is a REGRESSION of the grader."""
    return ["%s graded PASS with index=%d proxy=%d timed_out=%s" % (a["name"], a["requests_index"], a["requests_proxy"],
                                                                 a["timed_out"])
            for a in arms if a["role"] in ("candidate", "explicit") and a["passed"] is True
            and (a["requests_index"] or a["requests_proxy"] or a["timed_out"])]


def summarize(result, grader=grade_arm):
    """Grade the candidate and explicit arms, audit the grades, and build the PIP-NO-EGRESS fields. Pure: starts no process."""
    arms = result["arms"]
    by_name = {a["name"]: a for a in arms}
    positive = result.get("positive")
    positive_requests = (positive["requests_index"] + positive["requests_proxy"]) if positive else 0
    cands = result.get("candidates", [])
    for c in cands:
        plain, explicit = by_name[c["plain_arm"]], by_name[c["explicit_arm"]]
        plain["passed"] = bool(grader(plain, positive_requests))
        explicit["passed"] = bool(grader(explicit, positive_requests))
        c["passed"] = plain["passed"]
        c["holds"] = explicit["passed"]
    regressions = audit_grades(arms)
    passing = [c for c in cands if c["passed"] and not regressions]
    holding = [c for c in cands if c["passed"] and c["holds"] and not regressions]
    leaked = sum(a["leaked_public"] for a in arms)
    order = dict((name, i) for i, name in enumerate(CANDIDATE_ORDER))
    nonwrap = sorted([c for c in holding if c["name"] != "wrapper"], key=lambda c: order.get(c["name"], 99))
    if nonwrap:
        form = nonwrap[0]["name"]
    elif any(c["name"] == "wrapper" for c in holding):
        form = "wrapper-only"
    else:
        form = "NONE"
    ok = bool(positive_requests > 0 and leaked == 0 and not regressions and not result.get("stopped")
              and len(cands) == len(CANDIDATE_ORDER))
    return {"pip": result.get("pip_version", "unknown"), "positive_requests": positive_requests, "candidates": len(cands),
            "passing": len(passing), "holds_against_explicit": len(holding), "leaked_public": leaked, "form": form,
            "wrapper_holds": any(c["name"] == "wrapper" for c in holding), "ok": ok, "regressions": regressions}


def last_line(s):
    return ("PIP-NO-EGRESS pip=%s positive_requests=%d candidates=%d passing=%d holds_against_explicit=%d leaked_public=%d "
            "form=%s ok=%s" % (s["pip"], s["positive_requests"], s["candidates"], s["passing"], s["holds_against_explicit"],
                               s["leaked_public"], s["form"], s["ok"]))


def arm_line(a):
    return ("ARM %-40s role=%-10s index=%d proxy=%d rc=%s named=%s verdict=%s | %s"
            % (a["name"][:40], a["role"], a["requests_index"], a["requests_proxy"], a["rc"], a["named"],
               {None: "-", True: "PASS", False: "FAIL"}[a["passed"]], a["first_error_line"][:110]))


def run_order_of_proof(h):
    """The ordered proof. Returns the result dict; sets result['stopped'] and stops at the first failure."""
    result = {"arms": h.arms, "steps": [], "stopped": None, "candidates": [], "positive": None, "tmp_base": str(h.base),
              "rejected_tmp_bases": [r[0] for r in h.rejected_bases], "package": h.package, "dead_port": h.dead_port}

    def step(label, rec, note=""):
        result["steps"].append({"step": label, "index": rec["requests_index"], "proxy": rec["requests_proxy"],
                                "rc": rec["rc"], "note": note})

    sc = selfcheck_listeners()
    result["listener_selfcheck"] = {k: v for k, v in sc.items() if k not in ("index_log", "proxy_log")}
    if not sc["ok"]:
        result["stopped"] = "STEP-pre: the listeners did not log the Python-made requests; no pip process started"
        return result
    # (0) pip --version only, both listeners up: any request here is a finding, a version check that phones home
    v = h.arm("version", "version", ["--version"])
    result["pip_version"] = (re.match(r"pip (\S+)", first_line(v["output_full"])) or [None, "unknown"])[1] if v["rc"] == 0 else "unknown"
    h.pip_version = result["pip_version"]
    step("0 pip --version", v, "any request here is a finding")
    if v["rc"] != 0 or v["requests_index"] or v["requests_proxy"]:
        result["stopped"] = "STEP-0: pip --version failed or made %d request(s)" % (v["requests_index"] + v["requests_proxy"])
        return result
    # (1) the positive arm: the plain download with the explicit loopback index, both redirects on, no disarm
    pos = h.arm("positive", "positive", h.download_args(h.index.url))
    result["positive"] = pos
    step("1 positive arm: explicit loopback index, both redirects, no disarm", pos)
    if pos["requests_index"] + pos["requests_proxy"] == 0:
        result["stopped"] = ("STEP-1: zero requests on both listeners (rc=%s, first error: %s): the harness cannot see a request; "
                             "no candidate measured" % (pos["rc"], pos["first_error_line"]))
        return result
    # (2) control: a config file that does not parse must be READ by pip (the error names the config), and no request may follow
    ctrl = h.arm("control:config-file-is-read", "control", h.download_args(h.index.url), config_text="[global\n")
    result["config_file_is_read"] = bool(re.search(r"config|pars", ctrl["output_full"], re.I)) and not (
        ctrl["requests_index"] or ctrl["requests_proxy"])
    step("2 control: a malformed config file is read by pip", ctrl,
         "read=%s (a config error proves PIP_CONFIG_FILE was read)" % result["config_file_is_read"])
    # (3) candidates: each plain (the same command, no index flag) and with the explicit loopback index after its disarm
    specs = [
        ("env:PIP_NO_INDEX", None, {"PIP_NO_INDEX": "1"}, False),
        ("config:no-index", "[global]\nno-index = true\n", None, False),
        ("config:index-url-dead-loopback", "[global]\nindex-url = http://%s:%d/simple/\n" % (LOOPBACK, h.dead_port), None, False),
        ("wrapper", None, None, True),
    ]
    for name, cfg, env_extra, wrapped in specs:
        plain = h.arm(name, "candidate", h.download_args(), env_extra=env_extra, config_text=cfg, wrapped=wrapped)
        expl = h.arm(name + " +explicit-index", "explicit", h.download_args(h.index.url), env_extra=env_extra, config_text=cfg,
                     wrapped=wrapped)
        result["candidates"].append({"name": name, "plain_arm": plain["name"], "explicit_arm": expl["name"]})
        step("3 candidate %s: plain" % name, plain)
        step("3 candidate %s: explicit index after the disarm" % name, expl)
    return result


def measure(out=None, tmp_base=None, out_stream=None):
    out_stream = out_stream or sys.stdout
    h = Harness(tmp_base)
    try:
        try:
            result = run_order_of_proof(h)
        except Exception as exc:  # a harness error stops the proof and is never swallowed: the arms so far are still printed
            result = {"arms": h.arms, "steps": [], "candidates": [], "positive": None, "pip_version": h.pip_version,
                      "stopped": "HARNESS-EXCEPTION: %s: %s" % (type(exc).__name__, asc(exc))}
        result["pip_version"] = result.get("pip_version", h.pip_version)
        summary = summarize(result)
    finally:
        h.close()
    result["summary"] = summary
    for s in result.get("steps", []):
        print("STEP %-72s index=%d proxy=%d rc=%s %s" % (s["step"][:72], s["index"], s["proxy"], s["rc"], asc(s["note"])),
              file=out_stream)
    for a in result["arms"]:
        print(arm_line(a), file=out_stream)
    if result.get("stopped"):
        print("STOPPED: " + asc(result["stopped"]), file=out_stream)
    for r in summary["regressions"]:
        print("REGRESSION: " + r, file=out_stream)
    if sys.platform == "win32":
        print("NOTE: candidate (b) is measured as the config file pip reads from PIP_CONFIG_FILE; the per-user file is located "
              "by the shell on this platform, is not redirected, and was not written. Both paths use one option parser.",
              file=out_stream)
    if out:
        pathlib.Path(out).write_text(json.dumps(result, indent=1, default=str), encoding="ascii")
    print(last_line(summary), file=out_stream)
    return (0 if summary["ok"] else 1), result


# ------------------------------------------------------------------------------------------------------------------ classify and wrap
def has_network_url(token):
    """True for any URL whose scheme is not file (http, https, ftp, git+https and the like, anywhere in the token)."""
    return any(m.group(1).lower() != "file" for m in URL_SCHEME.finditer(token))


def requirement_problem(token):
    """-r / --requirement / -e / --editable, bare or with an attached value: a requirements or editable source can name a URL."""
    if token in REQUIREMENT_FLAGS or token.startswith("--requirement=") or token.startswith("--editable="):
        return True
    return (token[:2] in ("-r", "-e") and not token.startswith("--") and len(token) > 2)


def verb_index(args):
    """Index of the first positional argument (the pip verb), skipping flags and the values of value options; -1 when none."""
    i = 0
    while i < len(args):
        a = args[i]
        if a in VALUE_OPTIONS:
            i += 2
            continue
        if a.startswith("-"):
            i += 1
            continue
        return i
    return -1


def classify(args):
    """(action, message) for one list of pip arguments: ALLOW or REFUSE. Starts no process. Any URL that is not file:// refuses,
    wherever it stands (an option value, an attached value, a direct requirement); then the verb decides."""
    args = [str(a) for a in args]
    for a in args:
        if has_network_url(a) or VCS_PREFIX.match(a) or requirement_problem(a):
            return "REFUSE", REFUSAL
    if any(a == "--proxy" or a.startswith("--proxy=") for a in args):
        return "REFUSE", NOT_ALLOWED % "--proxy"
    idx = verb_index(args)
    info = any(a in INFO_FLAGS for a in args)
    if idx < 0:
        if info:
            return "ALLOW", "information flag only"
        return "REFUSE", NOT_ALLOWED % "(no verb)"
    verb = args[idx]
    if verb in DOWNLOAD_VERBS:
        if "--no-index" in args or info:
            return "ALLOW", "%s with --no-index or help: no index is consulted" % verb
        return "REFUSE", REFUSAL
    if verb in ALLOWED_VERBS:
        if verb == "list" and any(a in OUTDATED_FLAGS for a in args):
            return "REFUSE", OUTDATED
        return "ALLOW", "%s needs no index" % verb
    if info:
        return "ALLOW", "help or version for %s" % verb
    return "REFUSE", NOT_ALLOWED % asc(verb)


def wrap(argv):
    if "--" not in argv:
        print("usage: wrap [--from <json>] -- <pip args>", file=sys.stderr)
        return REFUSED_RC
    cut = argv.index("--")
    ap = argparse.ArgumentParser(prog="wrap", add_help=False)
    ap.add_argument("--from", dest="from_json")
    opts = ap.parse_args(argv[:cut])
    args = argv[cut + 1:]
    env = dict(os.environ)
    if opts.from_json:
        with open(opts.from_json, encoding="utf-8") as handle:
            summary = json.load(handle).get("summary", {})
        if not summary.get("wrapper_holds"):
            print("REFUSED: the measurement at %s did not show the wrapper form holding on this box; no pip process was run."
                  % asc(opts.from_json), file=sys.stderr)
            return REFUSED_RC
        if summary.get("form") == "env:PIP_NO_INDEX":
            env["PIP_NO_INDEX"] = "1"
    action, message = classify(args)
    if action == "REFUSE":
        print(message, file=sys.stderr)
        return REFUSED_RC
    return subprocess.run([sys.executable, "-m", "pip"] + args, env=env).returncode


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "wrap":
        return wrap(argv[1:])
    ap = argparse.ArgumentParser(description="measure and wrap pip's package-index access without sending a request")
    sub = ap.add_subparsers(dest="cmd", required=True)
    pm = sub.add_parser("measure")
    pm.add_argument("--out")
    pm.add_argument("--tmp-base")
    sub.add_parser("selfcheck")
    ns = ap.parse_args(argv)
    if ns.cmd == "selfcheck":
        sc = selfcheck_listeners()
        print(json.dumps(sc, indent=1))
        print("PIP-LISTENER-SELFCHECK ok=%s" % sc["ok"])
        return 0 if sc["ok"] else 1
    rc, _ = measure(ns.out, ns.tmp_base)
    return rc


if __name__ == "__main__":
    sys.exit(main())
