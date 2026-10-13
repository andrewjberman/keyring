#!/usr/bin/env python3
r"""ssh-tailnet-verify -- a one-shot read of FWD-27: does each box answer SSH by key, and refuse a password.

NFRA_CTLPLN TO CT-u-2; keyboard-interactive, identity and per-box login TO CT-ab-7. Boxes and addresses come from
the device register through lib/devices.py; no box name, address or login is typed here. Per box, one line with
four arms:

    BOX <name> <addr> port22=<v> key=<v> password_arm=<v> methods=<list or -> nontailnet_arm=NOT-DRIVEN (...)

    port22          TCP connect to <addr>:22. OPEN; CLOSED only for a refusal or a timeout; PROBE-ERROR for any
                    other failure, so a probe that could not run is never reported as a closed port.
    key             ssh by key (BatchMode, login <user>, the key file given by --identity or the default
                    %USERPROFILE%\.ssh\id_ed25519 with IdentitiesOnly, runs `hostname`). ANSWERED:<host> when the
                    printed name equals the box's name, tailnet name or an alias (case-insensitive); MISMATCH:<host>
                    when it does not; DENIED; PROBE-ERROR otherwise. NOT-RUN unless port22 is OPEN.
    password_arm    reads the server's advertised methods: ssh with PreferredAuthentications=none (BatchMode, public
                    key off) runs `true`, which sshd refuses, and its denial line `Permission denied (<list>)` names
                    the methods sshd offers (the list is printed as methods=). REFUSED when the list holds neither
                    password nor keyboard-interactive. ADVERTISED:<list> when `password` is there (the box allows a
                    password login, so it is not done). When `keyboard-interactive` is there, ONE keyboard-interactive
                    attempt decides (-vv, not batch mode, one password prompt, stdin empty): ADVERTISED:<list> when the
                    server sends a prompt (an info_req in the debug output); KBDINT-NO-PROMPT:<list> when it does not,
                    which counts as refused (the method is offered but no prompt is ever sent). LOGGED-IN when a login
                    succeeds with no credential (a failure); PROBE-ERROR when no list can be read or the attempt cannot
                    be graded (never REFUSED by default). NOT-RUN unless port22 is OPEN. The tool never sends a password.
    nontailnet_arm  NOT-DRIVEN for every box: this tool cannot source a connection from a non-tailnet address. The
                    firewall's remote scope is read from the box's own enable receipt, not here.

A box is done only when port22=OPEN, key=ANSWERED and password_arm is REFUSED or KBDINT-NO-PROMPT. Last line:
    SSH-VERIFY boxes=<n> done=<k> not_done=<list or ->
Exit 0 when every requested box is done, 1 otherwise, 2 on refusal.

    python .tools/ssh-tailnet-verify.py [--box <name> ...] [--user <login>] [--user-for <box>=<login> ...]
                                        [--identity <path>] [--timeout 5] [--selftest]

--user defaults to the environment variable OPAL_SSH_USER. A login may hold spaces (it is passed with -l). With
neither --user, OPAL_SSH_USER nor --user-for the tool refuses (REFUSED: no login name, rc 2); a box with no login
refuses the run before any probe. --selftest runs twelve cases against a loopback listener and a stub ssh; it
touches nothing beyond loopback and does not read the real register.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import pathlib
import re
import shutil
import socket
import subprocess
import sys
import tempfile
import threading

ROOT = pathlib.Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "lib"))
import devices  # noqa: E402  -- the one reader of the device register (lib/devices.py)

SSH_PORT = 22
OPEN = "OPEN"
CLOSED = "CLOSED"
PROBE_ERROR = "PROBE-ERROR"
NOT_RUN = "NOT-RUN"
REFUSED = "REFUSED"
LOGGED_IN = "LOGGED-IN"
ADVERTISED = "ADVERTISED"
KBDINT_NO_PROMPT = "KBDINT-NO-PROMPT"
DENIED = "DENIED"
PASSWORD_METHOD = "password"
KBDINT_METHOD = "keyboard-interactive"
METHOD_LIST = re.compile(r"permission denied \(([^)]*)\)", re.IGNORECASE)
# the server's keyboard-interactive prompt (SSH2_MSG_USERAUTH_INFO_REQUEST) as ssh logs it at -vv
PROMPT_SEEN = re.compile(r"input_userauth_info_req|userauth_info_request|receive packet: type 60", re.IGNORECASE)
FORBIDDEN_IN_LOGIN = "@'\"`$;&|<>()"
NONTAILNET = ("NOT-DRIVEN (this tool cannot source a non-tailnet connection; "
              "the firewall remote scope is read from the box's enable receipt)")

STUB = (
    "import json, os, sys\n"
    "argv = sys.argv[1:]\n"
    "log = os.environ.get('FAKE_SSH_ARGV_LOG', '')\n"
    "if log:\n"
    "    with open(log, 'a', encoding='ascii') as fh:\n"
    "        fh.write(json.dumps(argv) + '\\n')\n"
    "script = json.loads(os.environ.get('FAKE_SSH_SCRIPT', '{}'))\n"
    "if any('PreferredAuthentications=none' in a for a in argv):\n"
    "    arm = 'password'\n"
    "elif any('PreferredAuthentications=keyboard-interactive' in a for a in argv):\n"
    "    arm = 'kbdint'\n"
    "else:\n"
    "    arm = 'key'\n"
    "offered = 'keyboard-interactive' if arm == 'kbdint' else 'publickey'\n"
    "spec = script.get(arm) or {'rc': 255, 'out': '', 'err': 'Permission denied (%s).\\n' % offered}\n"
    "sys.stdout.write(spec.get('out', ''))\n"
    "sys.stderr.write(spec.get('err', ''))\n"
    "sys.exit(int(spec.get('rc', 255)))\n"
)


def ascii_only(text):
    return str(text).encode("ascii", "backslashreplace").decode("ascii")


def note(msg):
    print("DETAIL " + ascii_only(msg), file=sys.stderr)


def port_probe(addr, port, timeout, connect=socket.create_connection):
    try:
        sock = connect((addr, port), timeout)
    except (ConnectionRefusedError, socket.timeout, TimeoutError):
        return CLOSED
    except Exception as exc:  # the probe did not run to an answer
        note("port22 %s: probe could not complete (%s: %s)" % (addr, type(exc).__name__, exc))
        return PROBE_ERROR
    sock.close()
    return OPEN


def default_identity(env):
    """%USERPROFILE%\\.ssh\\id_ed25519 when it exists, else None. Not the MSYS home: Git Bash's ssh reads that."""
    base = env.get("USERPROFILE") or os.path.expanduser("~")
    path = os.path.join(base, ".ssh", "id_ed25519")
    return path if os.path.isfile(path) else None


def login_problem(user):
    """None for a plain account name (spaces allowed: the login is passed with -l), else the reason."""
    if (not user.isascii()) or user.startswith("-") or any(
            ord(c) < 0x20 or c in FORBIDDEN_IN_LOGIN for c in user):
        return "login name is not a plain account name"
    return None


def parse_user_for(items):
    """--user-for BOX=LOGIN values -> {box label: login}. Raises ValueError, naming the bad value."""
    mapping = {}
    for item in items:
        label, sep, user = item.partition("=")
        label, user = label.strip(), user.strip()
        if not sep or not label or not user:
            raise ValueError("--user-for expects BOX=LOGIN, got %r" % item)
        problem = login_problem(user)
        if problem:
            raise ValueError("--user-for %s: %s" % (label, problem))
        mapping[label] = user
    return mapping


def _common_opts(timeout):
    return ["-o", "BatchMode=yes",
            "-o", "ConnectTimeout=%d" % max(1, int(math.ceil(timeout))),
            "-o", "StrictHostKeyChecking=accept-new"]


def key_argv(ssh_cmd, user, addr, timeout, identity=None):
    argv = list(ssh_cmd) + _common_opts(timeout)
    if identity:
        argv += ["-i", identity, "-o", "IdentitiesOnly=yes"]
    return argv + ["-o", "PasswordAuthentication=no", "-l", user, addr, "hostname"]


def password_argv(ssh_cmd, user, addr, timeout):
    # offers sshd the 'none' method only: no password is ever sent, and sshd's denial names what it advertises
    return list(ssh_cmd) + _common_opts(timeout) + [
        "-o", "PreferredAuthentications=none", "-o", "PubkeyAuthentication=no",
        "-l", user, addr, "true"]


def kbdint_argv(ssh_cmd, user, addr, timeout):
    # One keyboard-interactive attempt, logged at -vv so the server's prompt shows in the output. Not BatchMode:
    # batch mode can stop the request before it is sent, and a request never sent would read a real password path
    # as refused. stdin is empty (DEVNULL) and one password prompt is allowed.
    return list(ssh_cmd) + [
        "-vv", "-o", "ConnectTimeout=%d" % max(1, int(math.ceil(timeout))),
        "-o", "StrictHostKeyChecking=accept-new",
        "-o", "PreferredAuthentications=keyboard-interactive", "-o", "PubkeyAuthentication=no",
        "-o", "NumberOfPasswordPrompts=1", "-l", user, addr, "true"]


def _as_text(value):
    if value is None:
        return ""
    if isinstance(value, bytes):
        return value.decode("utf-8", "replace")
    return str(value)


def run_ssh(argv, timeout):
    """(rc, stdout, stderr); rc None when the probe could not start or ran past its bound. A probe past its bound
    keeps the output it had written, so a prompt logged before the bound is still graded."""
    try:
        cp = subprocess.run(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            timeout=2 * timeout + 10, encoding="utf-8", errors="replace")
    except subprocess.TimeoutExpired as exc:
        return None, _as_text(exc.stdout), _as_text(exc.stderr) + "\nprobe ran past its bound\n"
    except OSError as exc:
        return None, "", "probe could not start (%s)" % exc
    return cp.returncode, cp.stdout, cp.stderr


def key_verdict(rc, out, err, own):
    if rc is None:
        note("key arm: %s" % err)
        return PROBE_ERROR
    if rc == 0:
        lines = [ln.strip() for ln in out.splitlines() if ln.strip()]
        printed = lines[-1] if lines else ""
        if printed and printed.lower() in own:
            return "ANSWERED:%s" % printed
        return "MISMATCH:%s" % (printed or "(nothing printed)")
    text = (out + err).lower()
    if "permission denied" in text:
        return DENIED
    note("key arm: ssh rc=%s with no permission verdict: %s" % (rc, (err or out).strip()[:200]))
    return PROBE_ERROR


def password_verdict(rc, out, err):
    """Grades the none probe. Returns (verdict, methods). A verdict of None means keyboard-interactive is listed
    and one keyboard-interactive attempt decides (kbdint_verdict)."""
    if rc is None:
        note("password arm: %s" % err)
        return PROBE_ERROR, None
    if rc == 0:
        return LOGGED_IN, None
    found = METHOD_LIST.search(out + err)
    if not found:
        note("password arm: ssh rc=%s with no advertised-method list: %s" % (rc, (err or out).strip()[:200]))
        return PROBE_ERROR, None
    methods = [m.strip().lower() for m in found.group(1).split(",") if m.strip()]
    if PASSWORD_METHOD in methods:
        return "%s:%s" % (ADVERTISED, ",".join(methods)), methods
    if KBDINT_METHOD in methods:
        return None, methods
    return REFUSED, methods


def kbdint_verdict(rc, out, err, methods):
    text = out + err
    if rc == 0:
        return LOGGED_IN
    if PROMPT_SEEN.search(text):
        return "%s:%s" % (ADVERTISED, ",".join(methods))
    if rc is None:
        note("keyboard-interactive arm: %s" % err.strip()[-200:])
        return PROBE_ERROR
    if "permission denied" in text.lower():
        return "%s:%s" % (KBDINT_NO_PROMPT, ",".join(methods))
    note("keyboard-interactive arm: ssh rc=%s with no permission verdict" % rc)
    return PROBE_ERROR


def refused_arm(pw):
    """True for the verdicts that mean no password path: REFUSED, or a keyboard-interactive offer with no prompt."""
    return pw == REFUSED or pw.split(":", 1)[0] == KBDINT_NO_PROMPT


def verify_box(row, user, timeout, ssh_cmd=("ssh",), port=SSH_PORT, connect=socket.create_connection,
               identity=None):
    name = row["name"]
    addr = (row.get("tailnet_address") or "").strip()
    own = {name.lower()}
    if row.get("tailnet_name"):
        own.add(row["tailnet_name"].lower())
    own.update(a.lower() for a in row.get("aliases", []))
    methods = None
    if addr:
        port22 = port_probe(addr, port, timeout, connect)
    else:
        note("%s: the register holds no tailnet_address" % name)
        port22 = PROBE_ERROR
    if port22 == OPEN:
        rc, out, err = run_ssh(key_argv(ssh_cmd, user, addr, timeout, identity), timeout)
        key = key_verdict(rc, out, err, own)
        rc, out, err = run_ssh(password_argv(ssh_cmd, user, addr, timeout), timeout)
        pw, methods = password_verdict(rc, out, err)
        if pw is None:
            rc, out, err = run_ssh(kbdint_argv(ssh_cmd, user, addr, timeout), timeout)
            pw = kbdint_verdict(rc, out, err, methods)
    else:
        key = pw = NOT_RUN
    done = port22 == OPEN and key.startswith("ANSWERED:") and refused_arm(pw)
    return {"name": name, "addr": addr, "port22": port22, "key": key, "password_arm": pw,
            "methods": methods, "done": done}


def box_line(res):
    methods = ",".join(res["methods"]) if res.get("methods") else "-"
    return ascii_only("BOX %s %s port22=%s key=%s password_arm=%s methods=%s nontailnet_arm=%s" % (
        res["name"], res["addr"] or "-", res["port22"], res["key"], res["password_arm"], methods, NONTAILNET))


def run(argv, env, emit):
    ap = argparse.ArgumentParser(description="One-shot read: does each box answer SSH by key and refuse a password.")
    ap.add_argument("--box", nargs="+", action="extend", default=None, metavar="NAME")
    ap.add_argument("--user", default=None)
    ap.add_argument("--user-for", action="append", default=[], metavar="BOX=LOGIN")
    ap.add_argument("--identity", default=None, metavar="PATH")
    ap.add_argument("--timeout", type=float, default=5.0)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest(emit)
    if args.timeout <= 0:
        emit("REFUSED: --timeout must be positive")
        return 2
    default_user = (args.user if args.user is not None else env.get("OPAL_SSH_USER", "")).strip()
    try:
        per_box = parse_user_for(args.user_for)
    except ValueError as exc:
        emit(ascii_only("REFUSED: %s" % exc))
        return 2
    if not default_user and not per_box:
        emit("REFUSED: no login name (give --user, --user-for or set OPAL_SSH_USER)")
        return 2
    if default_user and login_problem(default_user):
        emit("REFUSED: login name is not a plain account name")
        return 2
    identity = args.identity if args.identity is not None else default_identity(env)
    if identity is not None and not os.path.isfile(identity):
        emit(ascii_only("REFUSED: --identity is not a file: %s" % identity))
        return 2
    try:
        reg = devices.load()
    except devices.RegisterError as exc:
        emit(ascii_only("REFUSED: device register unavailable -- %s" % exc))
        return 2
    rows = devices.devices(reg)
    by_name = {r["name"]: r for r in rows}
    chosen = []
    if args.box:
        for label in args.box:
            canon = devices.resolve(label, reg)
            if canon is None:
                emit(ascii_only("REFUSED: %s is not a box in the device register (holds: %s)" % (
                    label, ", ".join(devices.names(reg)))))
                return 2
            if canon not in chosen:
                chosen.append(canon)
    else:
        chosen = [r["name"] for r in rows]
    login_for = {}
    for label, login in per_box.items():
        canon = devices.resolve(label, reg)
        if canon is None:
            emit(ascii_only("REFUSED: %s is not a box in the device register (holds: %s)" % (
                label, ", ".join(devices.names(reg)))))
            return 2
        login_for[canon] = login
    plan = []
    for canon in chosen:
        login = login_for.get(canon, default_user)
        if not login:
            emit(ascii_only("REFUSED: no login name for %s (give --user, --user-for %s=<login> or set OPAL_SSH_USER)"
                            % (canon, canon)))
            return 2
        plan.append((canon, login))
    results = []
    for canon, login in plan:
        res = verify_box(by_name[canon], login, args.timeout, identity=identity)
        emit(box_line(res))
        results.append(res)
    not_done = [r["name"] for r in results if not r["done"]]
    emit("SSH-VERIFY boxes=%d done=%d not_done=%s" % (
        len(results), len(results) - len(not_done), ",".join(not_done) or "-"))
    return 0 if not not_done else 1


def selftest(emit):
    results = []
    tmp = tempfile.mkdtemp(prefix="ssh-verify-selftest-")
    listener = None
    saved = os.environ.get("FAKE_SSH_SCRIPT")

    def set_script(key, password, kbdint=None):
        os.environ["FAKE_SSH_SCRIPT"] = json.dumps({"key": key, "password": password, "kbdint": kbdint})

    def ok(out):
        return {"rc": 0, "out": out, "err": ""}

    def deny(methods):
        # sshd's denial names the methods it advertises; the password probe reads this list
        return {"rc": 255, "out": "", "err": "fake-host: Permission denied (%s).\n" % methods}

    def first_argv(path):
        with open(path, encoding="ascii") as fh:
            return json.loads(fh.readline())

    try:
        stub = os.path.join(tmp, "fake_ssh.py")
        with open(stub, "w", encoding="ascii") as fh:
            fh.write(STUB)
        fake = [sys.executable, "-I", stub]
        missing = [os.path.join(tmp, "no-such-ssh-binary")]
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.bind(("127.0.0.1", 0))
        listener.listen(4)
        open_port = listener.getsockname()[1]

        def accept_forever():
            # a real port answers: drain connections so the backlog never fills and a later probe cannot time out
            while True:
                try:
                    conn, _ = listener.accept()
                except OSError:
                    return
                conn.close()
        threading.Thread(target=accept_forever, daemon=True).start()
        probe = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        probe.bind(("127.0.0.1", 0))
        closed_port = probe.getsockname()[1]
        probe.close()
        box = {"name": "fake-box-one", "tailnet_name": "fake-box-one", "aliases": ["fbone-alias"],
               "tailnet_address": "127.0.0.1"}

        def case_own_name_done():
            set_script(ok("fake-box-one\n"), deny("publickey"))
            r = verify_box(box, "probe-user", 3, fake, open_port)
            set_script(ok("FBONE-ALIAS\n"), deny("publickey"))
            alias = verify_box(box, "probe-user", 3, fake, open_port)
            argv_ok = ("BatchMode=yes" in key_argv(fake, "probe-user", "127.0.0.1", 3)
                       and "PasswordAuthentication=no" in key_argv(fake, "probe-user", "127.0.0.1", 3)
                       and "PreferredAuthentications=none" in password_argv(fake, "probe-user", "127.0.0.1", 3)
                       and "PubkeyAuthentication=no" in password_argv(fake, "probe-user", "127.0.0.1", 3)
                       and password_argv(fake, "probe-user", "127.0.0.1", 3)[-1] == "true")
            passed = (r["port22"] == OPEN and r["key"] == "ANSWERED:fake-box-one"
                      and r["password_arm"] == REFUSED and r["done"] and alias["key"] == "ANSWERED:FBONE-ALIAS"
                      and argv_ok)
            return passed, "port22=%s key=%s password_arm=%s done=%s alias=%s argv_ok=%s" % (
                r["port22"], r["key"], r["password_arm"], r["done"], alias["key"], argv_ok)

        def case_closed_is_closed():
            set_script(ok("fake-box-one\n"), deny("publickey"))
            r = verify_box(box, "probe-user", 3, fake, closed_port)
            passed = (r["port22"] == CLOSED and r["key"] == NOT_RUN and r["password_arm"] == NOT_RUN
                      and not r["done"])
            return passed, "port22=%s key=%s done=%s" % (r["port22"], r["key"], r["done"])

        def case_cannot_start_is_probe_error():
            set_script(ok("fake-box-one\n"), deny("publickey"))
            a = verify_box(box, "probe-user", 3, missing, open_port)

            def boom(address, timeout=None):
                raise OSError("probe socket could not be created")
            b = verify_box(box, "probe-user", 3, fake, open_port, connect=boom)
            passed = (a["port22"] == OPEN and a["key"] == PROBE_ERROR and a["password_arm"] == PROBE_ERROR
                      and not a["done"]
                      and b["port22"] == PROBE_ERROR and b["key"] == NOT_RUN and not b["done"])
            return passed, "ssh-missing: port22=%s key=%s | connect-raises: port22=%s key=%s" % (
                a["port22"], a["key"], b["port22"], b["key"])

        def case_mismatch_not_done():
            set_script(ok("someone-else\n"), deny("publickey"))
            r = verify_box(box, "probe-user", 3, fake, open_port)
            passed = r["key"] == "MISMATCH:someone-else" and not r["done"]
            return passed, "key=%s done=%s" % (r["key"], r["done"])

        def case_password_login_not_done():
            set_script(ok("fake-box-one\n"), ok("fake-box-one\n"))
            r = verify_box(box, "probe-user", 3, fake, open_port)
            passed = r["password_arm"] == LOGGED_IN and r["key"].startswith("ANSWERED") and not r["done"]
            return passed, "key=%s password_arm=%s done=%s" % (r["key"], r["password_arm"], r["done"])

        def case_no_login_refuses():
            emitted = []
            rc = run([], {}, emitted.append)
            passed = rc == 2 and any(s.startswith("REFUSED: no login name") for s in emitted)
            return passed, "rc=%s first=%s" % (rc, emitted[0] if emitted else "(none)")

        def case_password_advertised_not_done():
            set_script(ok("fake-box-one\n"), deny("publickey,password"))
            r = verify_box(box, "probe-user", 3, fake, open_port)
            passed = (r["key"] == "ANSWERED:fake-box-one" and r["password_arm"] == "ADVERTISED:publickey,password"
                      and not r["done"])
            return passed, "key=%s password_arm=%s done=%s" % (r["key"], r["password_arm"], r["done"])

        def case_publickey_only_refused_done():
            set_script(ok("fake-box-one\n"), deny("publickey"))
            r = verify_box(box, "probe-user", 3, fake, open_port)
            passed = r["key"] == "ANSWERED:fake-box-one" and r["password_arm"] == REFUSED and r["done"]
            return passed, "key=%s password_arm=%s done=%s" % (r["key"], r["password_arm"], r["done"])

        def case_kbdint_no_prompt_refused():
            # the server lists keyboard-interactive but sends no prompt: no password path, so the box is done
            set_script(ok("fake-box-one\n"), deny("publickey,keyboard-interactive"), deny("keyboard-interactive"))
            r = verify_box(box, "probe-user", 3, fake, open_port)
            passed = (r["key"] == "ANSWERED:fake-box-one"
                      and r["password_arm"] == "KBDINT-NO-PROMPT:publickey,keyboard-interactive"
                      and r["methods"] == ["publickey", "keyboard-interactive"] and r["done"])
            return passed, "key=%s password_arm=%s methods=%s done=%s" % (
                r["key"], r["password_arm"], r["methods"], r["done"])

        def case_kbdint_prompt_advertised():
            # the server sends a keyboard-interactive prompt: a password path exists, so the box is not done
            prompt = {"rc": 255, "out": "",
                      "err": "debug2: input_userauth_info_req\nfake-host: Permission denied (keyboard-interactive).\n"}
            set_script(ok("fake-box-one\n"), deny("publickey,keyboard-interactive"), prompt)
            r = verify_box(box, "probe-user", 3, fake, open_port)
            passed = r["password_arm"] == "ADVERTISED:publickey,keyboard-interactive" and not r["done"]
            return passed, "key=%s password_arm=%s done=%s" % (r["key"], r["password_arm"], r["done"])

        def case_identity_reaches_argv():
            log = os.path.join(tmp, "argv-identity.log")
            ident = "C:\\Users\\probe\\.ssh\\id_ed25519"
            set_script(ok("fake-box-one\n"), deny("publickey"))
            os.environ["FAKE_SSH_ARGV_LOG"] = log
            try:
                r = verify_box(box, "probe-user", 3, fake, open_port, identity=ident)
            finally:
                os.environ.pop("FAKE_SSH_ARGV_LOG", None)
            argv = first_argv(log)
            argv_ok = ("-i" in argv and argv[argv.index("-i") + 1] == ident
                       and "IdentitiesOnly=yes" in argv)
            passed = r["key"] == "ANSWERED:fake-box-one" and argv_ok
            return passed, "key=%s -i-reaches-argv=%s" % (r["key"], argv_ok)

        def case_user_for_space_reaches_l():
            log = os.path.join(tmp, "argv-login.log")
            mapped = parse_user_for(["fake-box-one=Opal Bloomberg"])
            set_script(ok("fake-box-one\n"), deny("publickey"))
            os.environ["FAKE_SSH_ARGV_LOG"] = log
            try:
                r = verify_box(box, mapped["fake-box-one"], 3, fake, open_port)
            finally:
                os.environ.pop("FAKE_SSH_ARGV_LOG", None)
            argv = first_argv(log)
            l_ok = any(argv[i] == "-l" and argv[i + 1] == "Opal Bloomberg" for i in range(len(argv) - 1))
            passed = mapped == {"fake-box-one": "Opal Bloomberg"} and r["done"] and l_ok
            return passed, "map=%s -l-reaches-argv=%s done=%s" % (mapped, l_ok, r["done"])

        cases = [
            ("own-name-key-is-done", case_own_name_done),
            ("closed-port-is-closed", case_closed_is_closed),
            ("probe-cannot-start-is-probe-error", case_cannot_start_is_probe_error),
            ("hostname-mismatch-not-done", case_mismatch_not_done),
            ("password-login-logged-in-not-done", case_password_login_not_done),
            ("no-login-refuses", case_no_login_refuses),
            ("password-advertised-not-done", case_password_advertised_not_done),
            ("publickey-only-refused-is-done", case_publickey_only_refused_done),
            ("kbdint-no-prompt-refused", case_kbdint_no_prompt_refused),
            ("kbdint-prompt-advertised", case_kbdint_prompt_advertised),
            ("identity-reaches-argv", case_identity_reaches_argv),
            ("user-for-space-reaches-l", case_user_for_space_reaches_l),
        ]
        for label, fn in cases:
            try:
                passed, detail = fn()
            except Exception as exc:  # a crashed case is a failed case, never a pass
                passed, detail = False, "raised %s: %s" % (type(exc).__name__, exc)
            results.append(passed)
            emit(ascii_only("CASE %d %s ok=%s %s" % (len(results), label, passed, detail)))
    finally:
        if listener is not None:
            listener.close()
        if saved is None:
            os.environ.pop("FAKE_SSH_SCRIPT", None)
        else:
            os.environ["FAKE_SSH_SCRIPT"] = saved
        os.environ.pop("FAKE_SSH_ARGV_LOG", None)
        shutil.rmtree(tmp)
    k, n = sum(1 for p in results if p), len(results)
    emit("SSH-VERIFY-SELFTEST cases=%d/%d ok=%s" % (k, n, k == n))
    return 0 if k == n else 1


def main(argv):
    return run(argv, os.environ, print)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
