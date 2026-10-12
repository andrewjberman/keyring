#!/usr/bin/env python3
"""ssh-tailnet-verify -- a one-shot read of FWD-27: does each box answer SSH by key, and refuse a password.

NFRA_CTLPLN TO CT-u-2. Boxes and addresses come from the device register through lib/devices.py; no box name,
address or login is typed here. Per box, one line with four arms:

    BOX <name> <addr> port22=<v> key=<v> password_arm=<v> nontailnet_arm=NOT-DRIVEN (...)

    port22          TCP connect to <addr>:22. OPEN; CLOSED only for a refusal or a timeout; PROBE-ERROR for any
                    other failure, so a probe that could not run is never reported as a closed port.
    key             ssh by key (BatchMode, login <user>, runs `hostname`). ANSWERED:<host> when the printed name equals
                    the box's name, tailnet name or an alias (case-insensitive); MISMATCH:<host> when it does not;
                    DENIED; PROBE-ERROR otherwise. NOT-RUN unless port22 is OPEN.
    password_arm    ssh with password auth only (BatchMode, public key off). REFUSED when sshd answers Permission denied
                    or no more authentication methods; LOGGED-IN is a failure; PROBE-ERROR otherwise. NOT-RUN unless
                    port22 is OPEN. LIMIT: BatchMode never types or sends a password, so REFUSED shows that no login
                    was made without one; by itself it does not prove sshd has PasswordAuthentication off.
    nontailnet_arm  NOT-DRIVEN for every box: this tool cannot source a connection from a non-tailnet address. The
                    firewall's remote scope is read from the box's own enable receipt, not here.

A box is done only when port22=OPEN, key=ANSWERED and password_arm=REFUSED. Last line:
    SSH-VERIFY boxes=<n> done=<k> not_done=<list or ->
Exit 0 when every requested box is done, 1 otherwise, 2 on refusal.

    python .tools/ssh-tailnet-verify.py [--box <name> ...] [--user <login>] [--timeout 5] [--selftest]

--user defaults to the environment variable OPAL_SSH_USER; with neither set the tool refuses
(REFUSED: no login name, rc 2). --selftest runs six cases against a loopback listener and a stub ssh; it
touches nothing beyond loopback and does not read the real register.
"""
from __future__ import annotations

import argparse
import json
import math
import os
import pathlib
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
DENIED = "DENIED"
NONTAILNET = ("NOT-DRIVEN (this tool cannot source a non-tailnet connection; "
              "the firewall remote scope is read from the box's enable receipt)")

STUB = (
    "import json, os, sys\n"
    "argv = sys.argv[1:]\n"
    "script = json.loads(os.environ.get('FAKE_SSH_SCRIPT', '{}'))\n"
    "arm = 'password' if any('PreferredAuthentications=password' in a for a in argv) else 'key'\n"
    "spec = script.get(arm) or {'rc': 255, 'out': '', 'err': 'Permission denied (publickey).\\n'}\n"
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


def _common_opts(timeout):
    return ["-o", "BatchMode=yes",
            "-o", "ConnectTimeout=%d" % max(1, int(math.ceil(timeout))),
            "-o", "StrictHostKeyChecking=accept-new"]


def key_argv(ssh_cmd, user, addr, timeout):
    return list(ssh_cmd) + _common_opts(timeout) + [
        "-o", "PasswordAuthentication=no", "%s@%s" % (user, addr), "hostname"]


def password_argv(ssh_cmd, user, addr, timeout):
    return list(ssh_cmd) + _common_opts(timeout) + [
        "-o", "PreferredAuthentications=password", "-o", "PubkeyAuthentication=no",
        "%s@%s" % (user, addr), "hostname"]


def run_ssh(argv, timeout):
    """(rc, stdout, stderr); rc None when the probe could not start or ran past its bound."""
    try:
        cp = subprocess.run(argv, stdin=subprocess.DEVNULL, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                            timeout=2 * timeout + 10, encoding="utf-8", errors="replace")
    except subprocess.TimeoutExpired:
        return None, "", "probe ran past its bound"
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
    if rc is None:
        note("password arm: %s" % err)
        return PROBE_ERROR
    if rc == 0:
        return LOGGED_IN
    text = (out + err).lower()
    if "permission denied" in text or "no more authentication methods" in text:
        return REFUSED
    note("password arm: ssh rc=%s with no refusal verdict: %s" % (rc, (err or out).strip()[:200]))
    return PROBE_ERROR


def verify_box(row, user, timeout, ssh_cmd=("ssh",), port=SSH_PORT, connect=socket.create_connection):
    name = row["name"]
    addr = (row.get("tailnet_address") or "").strip()
    own = {name.lower()}
    if row.get("tailnet_name"):
        own.add(row["tailnet_name"].lower())
    own.update(a.lower() for a in row.get("aliases", []))
    if addr:
        port22 = port_probe(addr, port, timeout, connect)
    else:
        note("%s: the register holds no tailnet_address" % name)
        port22 = PROBE_ERROR
    if port22 == OPEN:
        rc, out, err = run_ssh(key_argv(ssh_cmd, user, addr, timeout), timeout)
        key = key_verdict(rc, out, err, own)
        rc, out, err = run_ssh(password_argv(ssh_cmd, user, addr, timeout), timeout)
        pw = password_verdict(rc, out, err)
    else:
        key = pw = NOT_RUN
    done = port22 == OPEN and key.startswith("ANSWERED:") and pw == REFUSED
    return {"name": name, "addr": addr, "port22": port22, "key": key, "password_arm": pw, "done": done}


def box_line(res):
    return ascii_only("BOX %s %s port22=%s key=%s password_arm=%s nontailnet_arm=%s" % (
        res["name"], res["addr"] or "-", res["port22"], res["key"], res["password_arm"], NONTAILNET))


def run(argv, env, emit):
    ap = argparse.ArgumentParser(description="One-shot read: does each box answer SSH by key and refuse a password.")
    ap.add_argument("--box", nargs="+", action="extend", default=None, metavar="NAME")
    ap.add_argument("--user", default=None)
    ap.add_argument("--timeout", type=float, default=5.0)
    ap.add_argument("--selftest", action="store_true")
    args = ap.parse_args(argv)
    if args.selftest:
        return selftest(emit)
    if args.timeout <= 0:
        emit("REFUSED: --timeout must be positive")
        return 2
    user = (args.user if args.user is not None else env.get("OPAL_SSH_USER", "")).strip()
    if not user:
        emit("REFUSED: no login name (give --user or set OPAL_SSH_USER)")
        return 2
    if (not user.isascii()) or user.startswith("-") or any(c.isspace() or c in "@'\"`$;&|<>()" for c in user):
        emit("REFUSED: login name is not a plain account name")
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
    results = []
    for canon in chosen:
        res = verify_box(by_name[canon], user, args.timeout)
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

    def set_script(key, password):
        os.environ["FAKE_SSH_SCRIPT"] = json.dumps({"key": key, "password": password})

    def ok(out):
        return {"rc": 0, "out": out, "err": ""}

    def deny(arm):
        return {"rc": 255, "out": "", "err": "fake-host: Permission denied (%s).\n" % arm}

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
            set_script(ok("fake-box-one\n"), deny("password"))
            r = verify_box(box, "probe-user", 3, fake, open_port)
            set_script(ok("FBONE-ALIAS\n"), deny("password"))
            alias = verify_box(box, "probe-user", 3, fake, open_port)
            argv_ok = ("BatchMode=yes" in key_argv(fake, "probe-user", "127.0.0.1", 3)
                       and "PasswordAuthentication=no" in key_argv(fake, "probe-user", "127.0.0.1", 3)
                       and "PreferredAuthentications=password" in password_argv(fake, "probe-user", "127.0.0.1", 3)
                       and "PubkeyAuthentication=no" in password_argv(fake, "probe-user", "127.0.0.1", 3))
            passed = (r["port22"] == OPEN and r["key"] == "ANSWERED:fake-box-one"
                      and r["password_arm"] == REFUSED and r["done"] and alias["key"] == "ANSWERED:FBONE-ALIAS"
                      and argv_ok)
            return passed, "port22=%s key=%s password_arm=%s done=%s alias=%s argv_ok=%s" % (
                r["port22"], r["key"], r["password_arm"], r["done"], alias["key"], argv_ok)

        def case_closed_is_closed():
            set_script(ok("fake-box-one\n"), deny("password"))
            r = verify_box(box, "probe-user", 3, fake, closed_port)
            passed = (r["port22"] == CLOSED and r["key"] == NOT_RUN and r["password_arm"] == NOT_RUN
                      and not r["done"])
            return passed, "port22=%s key=%s done=%s" % (r["port22"], r["key"], r["done"])

        def case_cannot_start_is_probe_error():
            set_script(ok("fake-box-one\n"), deny("password"))
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
            set_script(ok("someone-else\n"), deny("password"))
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

        cases = [
            ("own-name-key-is-done", case_own_name_done),
            ("closed-port-is-closed", case_closed_is_closed),
            ("probe-cannot-start-is-probe-error", case_cannot_start_is_probe_error),
            ("hostname-mismatch-not-done", case_mismatch_not_done),
            ("password-login-logged-in-not-done", case_password_login_not_done),
            ("no-login-refuses", case_no_login_refuses),
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
        shutil.rmtree(tmp)
    k, n = sum(1 for p in results if p), len(results)
    emit("SSH-VERIFY-SELFTEST cases=%d/%d ok=%s" % (k, n, k == n))
    return 0 if k == n else 1


def main(argv):
    return run(argv, os.environ, print)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
