"""Offline test of unknown_lookup_probe.sh (issuer 2.0.0_SA_COO~G2): stub systemctl, systemd-run, journalctl and curl on PATH, a fake root whose transport.py and resident_session.py answer the
lookup three ways (clean 200 json, a 202 html WAF challenge, an exception), and run the script. Prints one RESULT line: UNK-PROBE-TEST-OK <n> cases or UNK-PROBE-TEST-FAIL <why>.
No network, no AWS, no host.

usage: python test_waf_lookup_probe.py        (run from the repository root; needs bash)
"""
import os
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
SCRIPT = HERE / "unknown_lookup_probe.sh"
cases = []


def check(name, ok, why=""):
    cases.append((name, bool(ok), why))
    print("CASE", "ok  " if ok else "FAIL", name, "" if ok else why, flush=True)


TRANSPORT = '''
import os


class Transport:
    def __init__(self, bundle):
        self.bundle = bundle
        self.jar = list(bundle.get("cookies") or [])

    @classmethod
    def from_bundle(cls, bundle, enrolled_user_id=None):
        return cls(bundle)

    def request(self, path, method="GET", payload=None, content_type=None):
        counter = os.environ["FAKE_COUNTER"]
        with open(counter, "a", encoding="ascii") as fh:
            fh.write(path.split("=")[-1] + "\\n")
        with open(counter, encoding="ascii") as fh:
            n = len(fh.read().split())
        plan = os.environ.get("FAKE_PLAN", "")
        mode = plan[n - 1] if n <= len(plan) else "c"
        if mode == "r":
            raise OSError("connection reset crumb=SECRETVALUE")
        if mode == "x":
            body = b"<html>awswaf challenge crumb=SECRETVALUE</html>"
            return {"status": 202, "waf_action": "challenge", "content_type": "text/html", "bytes": len(body), "body_complete": True,
                    "login_destination": False, "final_url_path": path.split("?")[0]}, body
        body = b'[{"symbol": "X"}]'
        return {"status": 200, "waf_action": None, "content_type": "application/json", "bytes": len(body), "body_complete": True,
                "login_destination": False, "final_url_path": path.split("?")[0]}, body
'''


def make_stubs(bindir, root, user, handled):
    interp = sys.executable.replace("\\", "/")
    (bindir / "systemctl").write_text(
        '#!/bin/bash\ncase "$*" in\n'
        '  *is-active*) echo active;;\n'
        '  *"-p MainPID"*) echo 4242;;\n'
        '  *"-p ActiveEnterTimestamp"*) echo "Fri 2026-10-16 13:28:25 UTC";;\n'
        '  *"-p User"*) echo %s;;\n'
        '  *"-p WorkingDirectory"*) echo %s;;\n'
        '  *"-p Environment"*) echo "PYTHONUNBUFFERED=1";;\n'
        '  *"-p ExecStart"*) echo "{ path=%s ; argv[]=%s %s/x.py ; ignore_errors=no }";;\n'
        'esac\n' % (user, root, interp, interp, root), encoding="ascii")
    (bindir / "journalctl").write_text(
        '#!/bin/bash\ncase "$*" in\n'
        '  *"-60 s"*) echo "Oct 16 14:00:00 h python3.12[1]: IRPT_RESIDENT_POLL handled=%d";;\n'
        '  *) echo "Oct 16 13:37:00 h python3.12[1]: IRPT_RESIDENT_POLL handled=0"\n'
        '     echo "Oct 16 13:40:45 h python3.12[1]: IRPT_RESIDENT_RESOLVE state=RETRY code=PROVIDER_READ_UNAVAILABLE:WAF_CHALLENGE"\n'
        '     echo "Oct 16 13:41:00 h python3.12[1]: IRPT_SESSION_ROTATION kept=1 names=a crumb=SECRETVALUE";;\n'
        'esac\n' % handled, encoding="ascii")
    (bindir / "curl").write_text('#!/bin/bash\ncase "$*" in\n  *PUT*) echo TOKEN;;\n  *public-ipv4*) echo 203.0.113.9;;\nesac\n', encoding="ascii")
    (bindir / "systemd-run").write_text(
        '#!/bin/bash\nWD=; ENVS=\n'
        'while [ $# -gt 0 ]; do\n  case "$1" in\n'
        '    -p) shift; case "$1" in WorkingDirectory=*) WD="${1#WorkingDirectory=}";; esac;;\n'
        '    --setenv=*) ENVS="$ENVS ${1#--setenv=}";;\n'
        '    --uid=*|--quiet|--wait|--pipe|--collect) ;;\n'
        '    *) break;;\n  esac\n  shift\ndone\n'
        'cd "$WD" || exit 99\nexec env $ENVS "$@"\n', encoding="ascii")
    for f in bindir.iterdir():
        f.chmod(0o755)


def run(tmp, plan="", user="tester", handled=0):
    root, bindir = tmp / "root", tmp / "bin"
    for d in (root, bindir):
        if d.exists():
            shutil.rmtree(d)
    (root / "ycharts" / "generate").mkdir(parents=True)
    (root / "ycharts" / "session").mkdir(parents=True)
    bindir.mkdir()
    (root / "ycharts" / "generate" / "transport.py").write_text(TRANSPORT, encoding="utf-8")
    (root / "ycharts" / "session" / "resident_session.py").write_text('LOOKUP_USER_AGENT = "Mozilla/5.0 test"\n', encoding="utf-8")
    make_stubs(bindir, root.as_posix(), user, handled)
    counter = tmp / "calls.txt"
    if counter.exists():
        counter.unlink()
    env = dict(os.environ, PATH=str(bindir) + os.pathsep + os.environ["PATH"], MSYS_NO_PATHCONV="1", FAKE_PLAN=plan, FAKE_COUNTER=counter.as_posix(),
               UNK_PYFILE=(tmp / "unk.py").as_posix(), UNK_REST="0", UNK_GAP="0", UNK_PAIR_GAP="0")
    proc = subprocess.run(["bash", str(SCRIPT)], capture_output=True, text=True, env=env)
    calls = counter.read_text(encoding="ascii").split() if counter.exists() else []
    return proc.returncode, proc.stdout + proc.stderr, calls


tmp = Path(tempfile.mkdtemp(prefix="unk_test_"))
try:
    check("bash -n", subprocess.run(["bash", "-n", str(SCRIPT)]).returncode == 0)
    check("script is ASCII", all(b < 128 for b in SCRIPT.read_bytes()))
    rc, out, calls = run(tmp, "")
    check("all clean: 12 calls, rc 0, no cutoff, six unknown lookups", rc == 0 and len(calls) == 12 and "UNK RESULT first_challenged_call=none calls=12 unknown_lookups=6" in out and "NO CUTOFF" in out, "rc=%d calls=%d %s" % (rc, len(calls), out[-500:]))
    check("the order is lookup of an unknown ticker then the verify of a known one, six times", calls == ["QQZXV01", "AAPL", "QQZXV02", "AAPL", "QQZXV03", "AAPL", "QQZXV04", "AAPL", "QQZXV05", "AAPL", "QQZXV06", "AAPL"], str(calls))
    check("every call is numbered and named LOOKUP or VERIFY in the output", all(("UNK CALL %d ticker=" % n) in out for n in range(1, 13)) and out.count("kind=LOOKUP") == 6 and out.count("kind=VERIFY") == 6, out[:900])
    check("the process is cookieless in the root's cwd", "cwd=%s" % (tmp / "root").as_posix() in out.replace("\\", "/"), out[:600])
    rc, out, calls = run(tmp, "cccc" + "x")
    check("a challenge at call 5 (an unknown LOOKUP): the run stops there; earlier than a count of 6 allows; unknown symbols trip", len(calls) == 5 and "first_challenged_call=5 calls=5 unknown_lookups=3" in out and "unknown symbols trip the firewall" in out, "calls=%d %s" % (len(calls), out[-500:]))
    rc, out, calls = run(tmp, "ccccc" + "x")
    check("a challenge at call 6 (a VERIFY): earlier than a count of 6 allows, but not blamed on an unknown lookup", len(calls) == 6 and "first_challenged_call=6" in out and "earlier than a count of 6 allows" in out and "unknown symbols trip" not in out, "calls=%d %s" % (len(calls), out[-500:]))
    rc, out, calls = run(tmp, "cccccc" + "cx")
    check("a challenge at call 8 (a VERIFY): consistent with a count of 6 calls per window", len(calls) == 8 and "first_challenged_call=8" in out and "consistent with a count of 6 calls per window" in out, "calls=%d %s" % (len(calls), out[-500:]))
    check("the challenged body never reaches the output", "SECRETVALUE" not in out, out[-300:])
    rc, out, calls = run(tmp, "r")
    check("a raised exception is a first-call cutoff with the class printed and the secret redacted", "verdict=EXCEPTION module=builtins name=OSError" in out and "first_challenged_call=1" in out and "SECRETVALUE" not in out, "rc=%d %s" % (rc, out[-500:]))
    rc, out, calls = run(tmp, "", handled=2)
    check("a busy resident refuses the whole read (rc 70, no call)", rc == 70 and not calls and "UNK FAIL the resident is busy" in out, "rc=%d %s" % (rc, out[-300:]))
    rc, out, calls = run(tmp, "", user="")
    check("an empty unit user is refused (rc 61)", rc == 61 and not calls, "rc=%d %s" % (rc, out[-200:]))
finally:
    shutil.rmtree(tmp, ignore_errors=True)
failed = [(n, w) for n, ok, w in cases if not ok]
for n, w in failed:
    print("CASE-FAIL", n, w)
if failed:
    print("UNK-PROBE-TEST-FAIL %d of %d cases failed" % (len(failed), len(cases)))
    sys.exit(1)
print("UNK-PROBE-TEST-OK %d cases" % len(cases))
