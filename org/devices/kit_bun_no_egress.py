"""kit_bun_no_egress.py -- measure which disarm of bun's silent auto-install actually works on THIS box's bun, and wrap bun with it.

THE HAZARD: bun, run on a file whose import does not resolve from a node_modules tree, downloads the package from the public
registry without asking. A fetch failure and a disabled install print the same error, so only a listener that COUNTS REQUESTS
can tell them apart.

THE ONE RULE: NO REQUEST MAY LEAVE THIS MACHINE. The test of the disarm must not itself be the egress, so every bun process this
tool starts runs inside a harness with two independent redirects to loopback:
  Redirect A (registry): bun's registry set to http://127.0.0.1:<port>/ (a listener that logs method and path, answers 404).
  Redirect B (proxy): HTTP_PROXY / HTTPS_PROXY / http_proxy / https_proxy set to a SECOND loopback listener that logs every
    request line (CONNECT included) and answers 502; NO_PROXY / no_proxy empty so even loopback goes through it if bun chooses.
The package every probe imports is a scoped name with a random suffix, so even a leak would retrieve nothing. Each run uses a fresh
directory outside every git tree and every node_modules / package.json ancestor, its own cache directory and its own HOME.

  measure [--out <json>] [--tmp-base <dir>]   run the harness in the ORDER OF PROOF, then each candidate disarm as its own arm.
  wrap [--from <json>] [--form <name>] [--allow-registry <reason>] -- <bun args>
                                              run bun with the passing form applied; refuse a registry verb.
  selfcheck                                   test the two listeners with Python-made requests; starts NO bun process.

It is the same script on every box: bun is resolved with shutil.which, no path and no version is written here.
LAST line of measure: BUN-NO-EGRESS bun=<v> positive_requests=<n> candidates=<k> passing=<p> leaked_public=<0|n> form=<form|NONE> ok=<..>
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

TIMEOUT = 30
LOOPBACK = "127.0.0.1"
PROXY_VARS = ("HTTP_PROXY", "HTTPS_PROXY", "http_proxy", "https_proxy")
NOPROXY_VARS = ("NO_PROXY", "no_proxy")
# The form the kit carries when `wrap` is given no measurement of its own: the form that measured as passing on the laptop's bun.
# A box with another bun runs `measure --out <json>` and passes `wrap --from <json>`; the default is only a starting point.
CARRIED_FORM = "flag:--no-install"
# Subcommands that can contact a package registry (or download bun itself): refused by wrap without --allow-registry.
REGISTRY_VERBS = ("install", "i", "add", "a", "x", "bunx", "create", "c", "update", "upgrade", "outdated", "audit", "info",
                  "publish", "remove", "rm")
VALUE_FLAGS = ("--cwd", "-c", "--config", "--filter", "--env-file", "--port", "--tsconfig-override", "--define", "-d",
               "--preload", "-r", "--inspect", "--conditions", "--workspaces", "-F")
INFO_ONLY = ("--version", "-v", "--revision", "--help", "-h")
FORM_PREFERENCE = ("flag:", "flag-after-subcommand:", "env:", "project-bunfig", "user-bunfig", "structural")


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


class RegistryListener:
    """Loopback registry stand-in: logs 'METHOD path host=<Host>' for every request, answers 404."""

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
        self.url = "http://%s:%d/" % (LOOPBACK, self.port)
        threading.Thread(target=self.server.serve_forever, daemon=True).start()

    def close(self):
        self.server.shutdown()
        self.server.server_close()


class ProxyListener:
    """Loopback proxy stand-in: logs every request line (CONNECT host:443, or an absolute-URI GET) and answers 502, then closes.
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
    """The host a logged request names: CONNECT host:port, an absolute-URI GET, else the Host header; '' when unknown."""
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


def landed_loopback(rec):
    """True when the arm's requests reached a loopback listener: the registry listener directly, or the proxy listener naming a
    loopback host (bun may route even a loopback registry through the proxy variable)."""
    return rec["requests_registry"] > 0 or any(is_loopback(request_host(x)) for x in rec["proxy_log"])


def public_hosts(lines):
    """The lines of a proxy log that name a public host (anything that is not loopback); an unreadable line counts as public."""
    return [x for x in lines if not is_loopback(request_host(x))]


def selfcheck_listeners():
    """Python-made requests to both listeners, BEFORE any bun process: each must log exactly what was sent. Returns a dict."""
    reg, prx = RegistryListener(), ProxyListener()
    try:
        conn = socket.create_connection((LOOPBACK, reg.port), timeout=5)
        conn.sendall(b"GET /selfcheck-registry HTTP/1.1\r\nHost: 127.0.0.1\r\nConnection: close\r\n\r\n")
        reply_reg = conn.recv(4096).decode("latin-1")
        conn.close()
        conn = socket.create_connection((LOOPBACK, prx.port), timeout=5)
        conn.sendall(b"CONNECT registry.invalid-selfcheck:443 HTTP/1.1\r\nHost: registry.invalid-selfcheck:443\r\n\r\n")
        reply_connect = conn.recv(4096).decode("latin-1")
        conn.close()
        conn = socket.create_connection((LOOPBACK, prx.port), timeout=5)
        conn.sendall(b"GET http://registry.invalid-selfcheck/x HTTP/1.1\r\nHost: registry.invalid-selfcheck\r\n\r\n")
        reply_get = conn.recv(4096).decode("latin-1")
        conn.close()
        time.sleep(0.2)
        reg_log, prx_log = reg.log.take(), prx.log.take()
    finally:
        reg.close()
        prx.close()
    result = {
        "registry_log": reg_log, "proxy_log": prx_log,
        "registry_answers_404": reply_reg.startswith("HTTP/1.1 404"),
        "proxy_answers_502_connect": reply_connect.startswith("HTTP/1.1 502"),
        "proxy_answers_502_get": reply_get.startswith("HTTP/1.1 502"),
        "registry_logged_one": len(reg_log) == 1 and reg_log[0].startswith("GET /selfcheck-registry"),
        "proxy_logged_two": len(prx_log) == 2 and prx_log[0].startswith("CONNECT registry.invalid-selfcheck:443")
        and prx_log[1].startswith("GET http://registry.invalid-selfcheck/x"),
        "proxy_public_hosts_seen": len(public_hosts(prx_log)),
    }
    result["ok"] = all(result[k] for k in ("registry_answers_404", "proxy_answers_502_connect", "proxy_answers_502_get",
                                           "registry_logged_one", "proxy_logged_two")) and result["proxy_public_hosts_seen"] == 2
    return result


# ------------------------------------------------------------------------------------------------------------------ isolation
def ancestor_problems(path):
    """Every ancestor of `path` (itself included) that holds a node_modules, package.json, .git or bunfig.toml entry."""
    found = []
    here = pathlib.Path(path).resolve()
    for anc in [here] + list(here.parents):
        for name in ("node_modules", "package.json", ".git", "bunfig.toml"):
            if (anc / name).exists():
                found.append("%s holds %s" % (anc, name))
    return found


def pick_tmp_base(explicit=None):
    """A base directory whose every ancestor is clean. Tries the explicit one, the system temp directory, then <drive root>/tmp
    (the drive prefix is derived from the system temp directory, never written here)."""
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
    return (up.startswith("BUN_") or up.startswith("NPM_CONFIG") or "PROXY" in up or "REGISTRY" in up or up.startswith("XDG_")
            or up in ("NODE_OPTIONS", "BUNFIG"))


def build_env(root, proxy_url, registry_envs, extra_env):
    """The child's environment only (passed as an env dictionary; this process's own environment is never changed)."""
    home = root / "home"
    cache = root / "cache"
    tmp = root / "tmp"
    for d in (home, cache, tmp, home / "AppData" / "Roaming", home / "AppData" / "Local", home / "xdg-config",
              home / "xdg-cache", home / "xdg-data", root / "bun-install"):
        d.mkdir(parents=True, exist_ok=True)
    env = {k: v for k, v in os.environ.items() if not ambient(k)}
    drive, tail = os.path.splitdrive(str(home))
    env.update({
        "HOME": str(home), "USERPROFILE": str(home), "HOMEDRIVE": drive, "HOMEPATH": tail or "\\",
        "APPDATA": str(home / "AppData" / "Roaming"), "LOCALAPPDATA": str(home / "AppData" / "Local"),
        "XDG_CONFIG_HOME": str(home / "xdg-config"), "XDG_CACHE_HOME": str(home / "xdg-cache"),
        "XDG_DATA_HOME": str(home / "xdg-data"), "TEMP": str(tmp), "TMP": str(tmp), "TMPDIR": str(tmp),
        "BUN_INSTALL": str(root / "bun-install"), "BUN_INSTALL_CACHE_DIR": str(cache), "BUN_TMPDIR": str(tmp),
        "NO_COLOR": "1", "FORCE_COLOR": "0", "BUN_DISABLE_ANALYTICS": "1", "DO_NOT_TRACK": "1",
    })
    if proxy_url:
        for name in PROXY_VARS:
            env[name] = proxy_url
        for name in NOPROXY_VARS:
            env[name] = ""
    for name, value in registry_envs.items():
        env[name] = value
    env.update(extra_env or {})
    return env


def count_files(path):
    n = 0
    for _root, _dirs, files in os.walk(path):
        n += len(files)
    return n


class Harness:
    """Owns the two listeners, the probe name, the temporary base and the arm runner. One instance per measure run."""

    def __init__(self, bun, tmp_base=None):
        self.bun = bun
        self.base, self.rejected_bases = pick_tmp_base(tmp_base)
        self.run_root = pathlib.Path(tempfile.mkdtemp(prefix="kit-bun-noegress-", dir=str(self.base)))
        self.reg = RegistryListener()
        self.prx = ProxyListener()
        self.package = "@opal-no-such-scope-%s/probe" % secrets.token_hex(8)
        self.arms = []
        self.counter = 0

    def close(self):
        self.reg.close()
        self.prx.close()
        shutil.rmtree(str(self.run_root), ignore_errors=True)

    def arm(self, name, role, args, registry_forms=(), proxy=True, project_bunfig=(), user_bunfig=(), env_extra=None,
            structural=False, script="probe", apply=None, timeout=TIMEOUT):
        """One bun process, from its own fresh directory, inside the harness. Returns (and stores) the arm record."""
        self.counter += 1
        root = self.run_root / ("arm%02d" % self.counter)
        probe_dir = root / "probe"
        probe_dir.mkdir(parents=True)
        reg_envs = {}
        project_lines = list(project_bunfig)
        user_lines = list(user_bunfig)
        for form in registry_forms:
            if form.startswith("env:"):
                reg_envs[form[4:]] = self.reg.url
            elif form == "project-bunfig":
                project_lines.append('registry = "%s"' % self.reg.url)
            elif form == "user-bunfig":
                user_lines.append('registry = "%s"' % self.reg.url)
        if script == "probe":
            (probe_dir / "probe.js").write_text(
                'import probe from "%s";\nconsole.log("probe-loaded", typeof probe);\n' % self.package, encoding="utf-8")
        elif script == "fetchcheck":
            (probe_dir / "fetchcheck.js").write_text(
                'const r = await fetch("%s");\nconsole.log("fetch-status", r.status);\n' % (self.reg.url + "proxy-honor-check"),
                encoding="utf-8")
        if project_lines:
            (probe_dir / "bunfig.toml").write_text("[install]\n" + "\n".join(project_lines) + "\n", encoding="utf-8")
        if structural:
            (probe_dir / "node_modules").mkdir()
            (probe_dir / "package.json").write_text("{}\n", encoding="utf-8")
        else:
            # the probe directory itself may hold the bunfig.toml this arm plants on purpose; nothing above it may hold anything
            problems = ancestor_problems(probe_dir.parent) + [
                "%s holds %s" % (probe_dir, n) for n in ("node_modules", "package.json", ".git") if (probe_dir / n).exists()]
            if problems:
                raise RuntimeError("probe directory has a node_modules/package.json/.git ancestor: " + asc(problems))
        env = build_env(root, self.prx.url if proxy else "", reg_envs, env_extra)
        if user_lines:
            # bun reads $XDG_CONFIG_HOME/.bunfig.toml when XDG_CONFIG_HOME is set, else $HOME/.bunfig.toml: the harness sets
            # both variables, so the user-level file is written to both places (a file in only one is silently never read).
            for user_dir in (root / "home", root / "home" / "xdg-config"):
                (user_dir / ".bunfig.toml").write_text("[install]\n" + "\n".join(user_lines) + "\n", encoding="utf-8")
        out_path = root / "out.txt"
        started = time.time()
        timed_out = False
        with open(str(out_path), "wb") as sink:
            try:
                proc = subprocess.run([self.bun] + list(args), cwd=str(probe_dir), env=env, stdout=sink,
                                      stderr=subprocess.STDOUT, stdin=subprocess.DEVNULL, timeout=timeout)
                rc = proc.returncode
            except subprocess.TimeoutExpired:
                timed_out = True
                rc = "TIMEOUT"
        elapsed = time.time() - started
        time.sleep(0.3)
        reg_log, prx_log = self.reg.log.take(), self.prx.log.take()
        text = out_path.read_bytes().decode("utf-8", "replace")
        text = re.sub(r"\x1b\[[0-9;]*[A-Za-z]", "", text)
        err_lines = [x.strip() for x in text.splitlines() if "error" in x.lower()]
        record = {
            "name": name, "role": role, "args": list(args), "registry_forms": list(registry_forms), "proxy_set": bool(proxy),
            "project_bunfig": project_lines, "user_bunfig": user_lines, "env_extra": dict(env_extra or {}),
            "structural": bool(structural), "apply": apply,
            "proxy_env": {k: env.get(k) for k in PROXY_VARS + NOPROXY_VARS} if proxy else {},
            "isolated_home": env["HOME"] == env["USERPROFILE"] and str(root) in env["HOME"],
            "requests_registry": len(reg_log), "requests_proxy": len(prx_log), "registry_log": reg_log, "proxy_log": prx_log,
            "rc": rc, "timed_out": timed_out, "seconds": round(elapsed, 2),
            "first_error_line": asc((err_lines or [first_line(text)])[0])[:300], "output_head": asc(text)[:600], "output_full": asc(text)[:40000],
            "named_probe": ("opal-no-such-scope-" + self.package.split("-")[-1].split("/")[0]) in text,
            "mentions_loopback_registry": ("%s:%d" % (LOOPBACK, self.reg.port)) in text,
            "cache_files": count_files(root / "cache"),
            "leaked_public": len(public_hosts(prx_log)) if registry_forms else 0,
            "passed": None,
        }
        self.arms.append(record)
        return record


# ------------------------------------------------------------------------------------------------------------------ grading
def grade_candidate(arm, positive_requests):
    """PASS only with zero requests on BOTH listeners, no timeout, the import actually attempted (bun's output names the probe
    package, so a flag-syntax error is not a pass), and the same run's positive arm non-zero."""
    return bool(positive_requests > 0 and arm["requests_registry"] == 0 and arm["requests_proxy"] == 0
                and not arm["timed_out"] and arm["named_probe"])


def audit_grades(arms):
    """Independent re-check of every graded arm: a PASS with any request or a timeout is a REGRESSION of the grader."""
    return ["%s graded PASS with registry=%d proxy=%d timed_out=%s" % (a["name"], a["requests_registry"], a["requests_proxy"],
                                                                     a["timed_out"])
            for a in arms if a["role"] == "candidate" and a["passed"] is True
            and (a["requests_registry"] or a["requests_proxy"] or a["timed_out"])]


def summarize(result, grader=grade_candidate):
    """Grade the candidate arms, audit the grades, and build the BUN-NO-EGRESS fields. Pure: starts no bun process."""
    arms = result["arms"]
    positive = next((a for a in arms if a["role"] == "positive-final"), None)
    positive_requests = (positive["requests_registry"] + positive["requests_proxy"]) if positive else 0
    candidates = [a for a in arms if a["role"] == "candidate"]
    for arm in candidates:
        arm["passed"] = bool(grader(arm, positive_requests))
    regressions = audit_grades(arms)
    passing = [a for a in candidates if a["passed"] and not regressions]
    leaked = sum(a["leaked_public"] for a in arms)
    form = "NONE"
    for prefix in FORM_PREFERENCE:
        hit = [a for a in passing if a["name"].startswith(prefix)]
        if hit:
            form = hit[0]["name"]
            break
    ok = bool(positive_requests > 0 and leaked == 0 and passing and not regressions and not result.get("stopped"))
    return {"bun": result.get("bun_version", "unknown"), "positive_requests": positive_requests, "candidates": len(candidates),
            "passing": len(passing), "leaked_public": leaked, "form": form, "ok": ok, "regressions": regressions}


def last_line(s):
    return ("BUN-NO-EGRESS bun=%s positive_requests=%d candidates=%d passing=%d leaked_public=%d form=%s ok=%s"
            % (s["bun"], s["positive_requests"], s["candidates"], s["passing"], s["leaked_public"], s["form"], s["ok"]))


def arm_line(a):
    return ("ARM %-44s role=%-14s registry=%d proxy=%d rc=%s cache_files=%d verdict=%s | %s"
            % (a["name"][:44], a["role"], a["requests_registry"], a["requests_proxy"], a["rc"], a["cache_files"],
               {None: "-", True: "PASS", False: "FAIL"}[a["passed"]], a["first_error_line"][:110]))


def discover_env_names(bun):
    """Search the bun binary's bytes for the environment-variable names it carries (BUN_CONFIG_*, BUN_FEATURE_FLAG_* and the like);
    return (all names found, the subset whose name reads as an install / auto-install switch)."""
    names = set()
    pat = re.compile(rb"BUN_[A-Z0-9_]{3,80}")
    with open(bun, "rb") as handle:
        carry = b""
        while True:
            chunk = handle.read(32 * 1024 * 1024)
            if not chunk:
                break
            data = carry + chunk
            for m in pat.finditer(data):
                names.add(m.group(0).decode("ascii"))
            carry = data[-128:]
    switch = re.compile(r"(DISABLE|NO|SKIP|OFF|NEVER)_?.*(INSTALL|AUTO)|(INSTALL|AUTO).*(DISABLE|OFF|NEVER|SKIP)|AUTO_?INSTALL")
    related = sorted(n for n in names if switch.search(n) and n not in ("BUN_INSTALL", "BUN_INSTALL_CACHE_DIR"))
    return sorted(names), related


def run_order_of_proof(h, discover=True, loopback_registry_only=False):
    """The ordered proof. Returns the result dict; sets result['stopped'] and stops at the first failure."""
    result = {"bun_path_resolved": True, "arms": h.arms, "steps": [], "stopped": None, "tmp_base": str(h.base),
              "rejected_tmp_bases": [r[0] for r in h.rejected_bases], "package": h.package}

    def step(label, rec, note=""):
        result["steps"].append({"step": label, "registry": rec["requests_registry"], "proxy": rec["requests_proxy"],
                                "rc": rec["rc"], "note": note})

    sc = selfcheck_listeners()
    result["listener_selfcheck"] = {k: v for k, v in sc.items() if k not in ("registry_log", "proxy_log")}
    if not sc["ok"]:
        result["stopped"] = "STEP-pre: the listeners did not log the Python-made requests; no bun process started"
        return result
    # (0) bun --version only, both listeners up
    r0 = h.arm("version", "version", ["--version"], proxy=True)
    result["bun_version"] = first_line(r0["output_head"]) or "unknown"
    step("0 bun --version", r0, "any request here is a finding: a version check that phones home")
    if r0["requests_registry"] or r0["requests_proxy"]:
        result["stopped"] = "STEP-0: bun --version made %d request(s)" % (r0["requests_registry"] + r0["requests_proxy"])
        return result
    # (0b) ADDITION to the order, loopback-only by construction: does this bun's HTTP client honour the proxy variables?
    rb = h.arm("proxy-honor-check", "proxy-honor", ["run", "fetchcheck.js"], proxy=True, script="fetchcheck")
    proxy_honored = rb["requests_proxy"] > 0
    result["proxy_honored"] = proxy_honored
    step("0b proxy-honour fetch of a loopback URL", rb,
         "URL is the loopback registry listener; honoured=%s (a request on the proxy listener) " % proxy_honored)
    # (1) the proxy proof: Redirect B alone, registry at its default, the strongest disarm
    # --loopback-registry-only (CTO msg 106253): every arm whose registry address is NOT itself loopback is skipped, because on a
    # bun version where the proxy is unproven such an arm relies on the proxy alone to keep the request on the machine.
    result["loopback_registry_only"] = bool(loopback_registry_only)
    result["skipped_arms"] = []
    if loopback_registry_only:
        result["skipped_arms"].append("1 proxy proof (registry at its default)")
    else:
        r1 = h.arm("proxy-proof", "proxy-proof", ["--no-install", "run", "probe.js"], proxy=True)
        step("1 proxy proof, --no-install, registry default", r1, "expect zero; this arm cannot prove the proxy works")
        if r1["requests_registry"] or r1["requests_proxy"]:
            result["stopped"] = "STEP-1: the disarmed probe made %d request(s)" % (r1["requests_registry"] + r1["requests_proxy"])
            return result
    # (2) the positive arm, Redirect A and B, no disarm. All forms of A at once first (the safest first trial: any one of them
    # landing on loopback keeps the request on this machine), then each form alone only when the proxy net is proven.
    forms_all = ["env:BUN_CONFIG_REGISTRY", "env:NPM_CONFIG_REGISTRY", "project-bunfig"]
    r2 = h.arm("positive-all-forms", "positive", ["run", "probe.js"], registry_forms=forms_all, proxy=True)
    step("2 positive arm, all three forms of Redirect A + proxy, no disarm", r2)
    total2 = r2["requests_registry"] + r2["requests_proxy"]
    if total2 == 0:
        result["stopped"] = ("STEP-2: zero requests on both listeners with no disarm (rc=%s, first error: %s): cannot tell where "
                             "the request went; no further bun run" % (r2["rc"], r2["first_error_line"]))
        return result
    effective = []
    if landed_loopback(r2):
        if loopback_registry_only:
            # a single form that this bun ignores would leave the registry at its public default: not run under this switch
            result["skipped_arms"].append("2 each form of Redirect A alone")
            result["forms_not_isolated"] = "--loopback-registry-only: every arm carries all three forms of Redirect A at once"
            effective = list(forms_all)
        elif proxy_honored:
            # the proxy is a proven second net: each form alone is now a safe trial
            for form in forms_all:
                rf = h.arm("positive-alone:" + form, "positive-form", ["run", "probe.js"], registry_forms=[form], proxy=True)
                step("2 positive arm, Redirect A form %s alone" % form, rf)
                if landed_loopback(rf):
                    effective.append(form)
        else:
            result["forms_not_isolated"] = "the proxy was not shown to be honoured, so a single-form trial could not be made safe"
            effective = list(forms_all)
    else:
        result["stopped"] = ("STEP-2: with all forms of Redirect A set, no request reached a loopback listener (proxy=%d, public "
                             "hosts named on the proxy=%d): Redirect A is ineffective in every form tried; the proxy kept "
                             "the request on this machine" % (r2["requests_proxy"], r2["leaked_public"]))
        return result
    result["effective_registry_forms"] = effective
    if not effective:
        result["stopped"] = "STEP-2: no form of Redirect A landed alone on the registry listener"
        return result
    reg_forms = effective
    # the positive arm for the candidates' own run: the SAME redirects the candidates carry, no disarm
    rp = h.arm("positive-final", "positive-final", ["run", "probe.js"], registry_forms=reg_forms, proxy=True)
    step("2 positive arm with the redirects every candidate carries", rp)
    if rp["requests_registry"] + rp["requests_proxy"] == 0:
        result["stopped"] = "STEP-2: the final positive arm made zero requests"
        return result

    def cand(name, args, **kw):
        return h.arm(name, "candidate", args, registry_forms=reg_forms, proxy=True, **kw)

    cand("flag:--no-install", ["--no-install", "run", "probe.js"], apply={"type": "args-before-subcommand",
                                                                           "args": ["--no-install"]})
    cand("flag-after-subcommand:--no-install", ["run", "--no-install", "probe.js"],
         apply={"type": "args-after-subcommand", "args": ["--no-install"]})
    cand("project-bunfig", ["run", "probe.js"], project_bunfig=['auto = "disable"'])
    cand("user-bunfig", ["run", "probe.js"], user_bunfig=['auto = "disable"'])
    # (d) environment variables: what the binary names, and what --help says
    result["env_names_in_binary"], related = discover_env_names(h.bun) if discover else ([], [])
    result["env_names_tried"] = related
    result["bun_config_names_in_binary"] = [n for n in result["env_names_in_binary"] if n.startswith("BUN_CONFIG_")]
    for hargs in (["--help"], ["run", "--help"]):
        rh = h.arm("help:" + " ".join(hargs), "help", hargs, registry_forms=reg_forms, proxy=True)
        result.setdefault("help_lines", {})[" ".join(hargs)] = [
            asc(x.strip())[:200] for x in rh["output_full"].splitlines() if re.search(r"install|auto|registry", x, re.I)]
        step("d help text: bun " + " ".join(hargs), rh)
    # CONTROL for the user-level reading, with NO network by construction: a user-level bunfig that is a SYNTAX ERROR, run with the
    # strongest disarm. If `bun run` reads the file (from HOME or XDG_CONFIG_HOME, both set and both written), bun stops on the
    # config error and never names the probe package; if it does not read it, bun reports the unresolved probe import. This
    # separates "the user-level setting did not work" from "the user-level file was never read" without a single request.
    rc_user = h.arm("control:user-bunfig-is-read-by-run", "control", ["--no-install", "run", "probe.js"],
                    registry_forms=reg_forms, proxy=True, user_bunfig=["auto = "])
    result["user_bunfig_is_read_by_run"] = not rc_user["named_probe"]
    step("c control: a malformed user-level bunfig is read by `bun run`", rc_user,
         "read=%s (a config error instead of the probe's resolution error proves the temporary-home file was read)"
         % result["user_bunfig_is_read_by_run"])
    for name in related:
        cand("env:%s=1" % name, ["run", "probe.js"], env_extra={name: "1"},
             apply={"type": "env", "name": name, "value": "1"})
    cand("structural", ["run", "probe.js"], structural=True)
    return result


def measure(out=None, tmp_base=None, out_stream=None, loopback_registry_only=False):
    out_stream = out_stream or sys.stdout
    bun = shutil.which("bun")
    if not bun:
        print("BUN-NO-EGRESS bun=NOT-INSTALLED positive_requests=0 candidates=0 passing=0 leaked_public=0 form=NONE ok=False",
              file=out_stream)
        return 1, None
    h = Harness(bun, tmp_base)
    try:
        try:
            result = run_order_of_proof(h, loopback_registry_only=loopback_registry_only)
        except Exception as exc:  # a harness error stops the proof, it is never swallowed: the arms so far are still printed
            result = {"arms": h.arms, "steps": [], "stopped": "HARNESS-EXCEPTION: %s: %s" % (type(exc).__name__, asc(exc)),
                      "bun_version": "unknown"}
        summary = summarize(result)
    finally:
        h.close()
    result["summary"] = summary
    for name in result.get("skipped_arms") or []:
        print("SKIPPED %s -- --loopback-registry-only: its registry address is not itself loopback" % name, file=out_stream)
    for s in result.get("steps", []):
        print("STEP %-72s registry=%d proxy=%d rc=%s %s" % (s["step"][:72], s["registry"], s["proxy"], s["rc"], asc(s["note"])),
              file=out_stream)
    for a in result["arms"]:
        print(arm_line(a), file=out_stream)
    if result.get("stopped"):
        print("STOPPED: " + asc(result["stopped"]), file=out_stream)
    for r in summary["regressions"]:
        print("REGRESSION: " + r, file=out_stream)
    result["bun_path"] = "(resolved by shutil.which on the measuring box; not recorded)"
    if out:
        pathlib.Path(out).write_text(json.dumps(result, indent=1, default=str), encoding="ascii")
    print(last_line(summary), file=out_stream)
    return (0 if summary["ok"] else 1), result


# ------------------------------------------------------------------------------------------------------------------ wrap
def subcommand_index(args):
    """Index of the first positional argument (the bun subcommand or script), skipping flags and the value of a value flag."""
    i = 0
    while i < len(args):
        a = args[i]
        if a in VALUE_FLAGS:
            i += 2
            continue
        if a.startswith("-"):
            i += 1
            continue
        return i
    return -1


def decide(args, allow_reason=None):
    """Return (action, message): REFUSE / ALLOW-REGISTRY / PASS-INFO / APPLY-FORM. Starts no process."""
    if not args:
        return "REFUSE", "REFUSED: no bun arguments given"
    if any(a == "--install" or a.startswith("--install=") or a == "-i" for a in args):
        return "REFUSE", "REFUSED: an --install flag would change the auto-install setting this wrapper applies"
    idx = subcommand_index(args)
    sub = args[idx] if idx >= 0 else ""
    effective = sub
    if sub == "pm" and idx + 1 < len(args) and args[idx + 1] in ("view", "info"):
        effective = "pm " + args[idx + 1]
    if effective in REGISTRY_VERBS or effective in ("pm view", "pm info"):
        if allow_reason:
            return "ALLOW-REGISTRY", ("LOUD: --allow-registry given (reason: %s): this bun %s may contact a package registry and "
                                      "request may leave this machine" % (asc(allow_reason), effective))
        return "REFUSE", ("REFUSED: bun %s can contact the package registry, and no request may leave this machine. Use the "
                          "link or none provisioning modes (.tools/wk-provision.sh), or pass --allow-registry <reason>." % effective)
    if all(a in INFO_ONLY for a in args):
        return "PASS-INFO", "bun %s runs bare: nothing is resolved, so there is nothing to disarm" % " ".join(args)
    return "APPLY-FORM", ""


def apply_form(form, args, env):
    """Apply the carried form to (args, env); returns (args, env, error)."""
    args = list(args)
    env = dict(env)
    if form.startswith("flag:"):
        return form[5:].split() + args, env, ""
    if form.startswith("flag-after-subcommand:"):
        idx = subcommand_index(args)
        if idx < 0:
            return args, env, "no subcommand to place %s after" % form
        return args[:idx + 1] + form.split(":", 1)[1].split() + args[idx + 1:], env, ""
    if form.startswith("env:") and "=" in form:
        name, value = form[4:].split("=", 1)
        env[name] = value
        return args, env, ""
    return args, env, ("form %s cannot be applied by wrap (a project or user bunfig, or a directory layout, is not a command-line "
                       "form); use a flag or environment form, or run `measure` on this bun" % form)


def wrap(argv):
    if "--" not in argv:
        print("usage: wrap [--from <json>] [--form <name>] [--allow-registry <reason>] -- <bun args>", file=sys.stderr)
        return 2
    cut = argv.index("--")
    ap = argparse.ArgumentParser(prog="wrap", add_help=False)
    ap.add_argument("--from", dest="from_json")
    ap.add_argument("--form")
    ap.add_argument("--allow-registry", dest="allow")
    opts = ap.parse_args(argv[:cut])
    args = argv[cut + 1:]
    action, message = decide(args, opts.allow)
    if action == "REFUSE":
        print(message, file=sys.stderr)
        return 2
    bun = shutil.which("bun")
    if not bun:
        print("REFUSED: bun not found on PATH", file=sys.stderr)
        return 2
    if action == "ALLOW-REGISTRY":
        print(message, file=sys.stderr)
        return subprocess.run([bun] + args).returncode
    if action == "PASS-INFO":
        return subprocess.run([bun] + args).returncode
    form = opts.form or CARRIED_FORM
    if opts.from_json:
        form = json.loads(pathlib.Path(opts.from_json).read_text(encoding="ascii")).get("summary", {}).get("form", "NONE")
    if form == "NONE":
        print("REFUSED: measure found no passing disarm for this bun; wrap carries only the refusal of registry verbs, so it will "
              "not run a file that could auto-install", file=sys.stderr)
        return 2
    final, env, err = apply_form(form, args, os.environ)
    if err:
        print("REFUSED: " + err, file=sys.stderr)
        return 2
    print("wrap: form=%s applied: bun %s" % (form, " ".join(final)), file=sys.stderr)
    return subprocess.run([bun] + final, env=env).returncode


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if argv and argv[0] == "wrap":
        return wrap(argv[1:])
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    pm = sub.add_parser("measure")
    pm.add_argument("--out")
    pm.add_argument("--tmp-base")
    pm.add_argument("--loopback-registry-only", action="store_true", dest="loopback_only",
                    help="skip every arm whose registry address is not itself loopback, and say so (for a bun version on which the proxy is unproven)")
    sub.add_parser("selfcheck")
    sub.add_parser("wrap")
    ns = ap.parse_args(argv)
    if ns.cmd == "selfcheck":
        sc = selfcheck_listeners()
        print(json.dumps({k: v for k, v in sc.items()}, indent=1))
        print("BUN-LISTENER-SELFCHECK ok=%s" % sc["ok"])
        return 0 if sc["ok"] else 1
    rc, _ = measure(ns.out, ns.tmp_base, loopback_registry_only=ns.loopback_only)
    return rc


if __name__ == "__main__":
    sys.exit(main())
