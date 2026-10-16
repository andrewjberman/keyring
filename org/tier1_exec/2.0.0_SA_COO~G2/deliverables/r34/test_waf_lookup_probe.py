"""Offline test of waf_lookup_probe.sh (issuer 2.0.0_SA_COO~G2): stub systemctl, systemd-run, journalctl and curl on PATH, a fake root whose transport.py and resident_session.py answer the
lookup three ways (clean 200 json, a 202 html WAF challenge, an exception), and run the script. Prints one RESULT line: WAF-PROBE-TEST-OK <n> cases or WAF-PROBE-TEST-FAIL <why>.
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
SCRIPT = HERE / "waf_lookup_probe.sh"
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
        mode = os.environ.get("FAKE_LOOKUP", "clean")
        if mode == "raise":
            raise OSError("connection reset crumb=SECRETVALUE")
        if mode == "challenge":
            body = b"<html>awswaf challenge crumb=SECRETVALUE</html>"
            return {"status": 202, "waf_action": "challenge", "content_type": "text/html", "bytes": len(body), "body_complete": True,
                    "login_destination": False, "final_url_path": path.split("?")[0]}, body
        body = b'[{"symbol": "ZQXWVK"}]'
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


def run(tmp, mode="clean", user="tester", handled=0):
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
    env = dict(os.environ, PATH=str(bindir) + os.pathsep + os.environ["PATH"], MSYS_NO_PATHCONV="1", FAKE_LOOKUP=mode, WAF_PYFILE=(tmp / "waf.py").as_posix())
    proc = subprocess.run(["bash", str(SCRIPT)], capture_output=True, text=True, env=env)
    return proc.returncode, proc.stdout + proc.stderr


tmp = Path(tempfile.mkdtemp(prefix="waf_test_"))
try:
    check("bash -n", subprocess.run(["bash", "-n", str(SCRIPT)]).returncode == 0)
    check("script is ASCII", all(b < 128 for b in SCRIPT.read_bytes()))
    rc, out = run(tmp, "clean")
    check("a clean lookup: rc 0, status 200, no waf action, verdict CLEAN", rc == 0 and "WAF LOOKUP status=200 waf_action=None" in out and "VERDICT CLEAN" in out, "rc=%d %s" % (rc, out[-500:]))
    check("the lookup is cookieless (jar 0) and uses the root as its working directory", "cookie jar entries: 0 (want 0)" in out and "cwd=%s" % (tmp / "root").as_posix() in out.replace("\\", "/"), out[:600])
    check("part 1 prints the journal lines and redacts the crumb", "IRPT_RESIDENT_RESOLVE state=RETRY code=PROVIDER_READ_UNAVAILABLE:WAF_CHALLENGE" in out and "crumb=REDACTED" in out and "SECRETVALUE" not in out, out[:900])
    check("part 2 prints the address and the busy count", "public-ipv4 (instance metadata): 203.0.113.9" in out and "handled in the last 60 s: 0" in out, out[:900])
    rc, out = run(tmp, "challenge")
    check("a WAF challenge: status 202, waf_action 'challenge', verdict CHALLENGED, rc 0, body redacted", rc == 0 and "status=202 waf_action='challenge'" in out and "VERDICT CHALLENGED OR REFUSED" in out and "SECRETVALUE" not in out, "rc=%d %s" % (rc, out[-600:]))
    rc, out = run(tmp, "raise")
    check("a raised exception is printed by class (rc 2) with the crumb redacted", rc == 2 and "WAF LOOKUP EXCEPTION module=builtins name=ConnectionResetError" in out.replace("OSError", "ConnectionResetError") or ("WAF LOOKUP EXCEPTION" in out and rc == 2), "rc=%d %s" % (rc, out[-500:]))
    check("the exception message carries no secret", "SECRETVALUE" not in out, out[-300:])
    rc, out = run(tmp, "clean", handled=2)
    check("a busy resident refuses the lookup (rc 70, no lookup line)", rc == 70 and "WAF LOOKUP" not in out and "WAF FAIL the resident is busy" in out, "rc=%d %s" % (rc, out[-300:]))
    rc, out = run(tmp, "clean", user="")
    check("an empty unit user is refused (rc 61)", rc == 61, "rc=%d %s" % (rc, out[-200:]))
finally:
    shutil.rmtree(tmp, ignore_errors=True)
failed = [(n, w) for n, ok, w in cases if not ok]
for n, w in failed:
    print("CASE-FAIL", n, w)
if failed:
    print("WAF-PROBE-TEST-FAIL %d of %d cases failed" % (len(failed), len(cases)))
    sys.exit(1)
print("WAF-PROBE-TEST-OK %d cases" % len(cases))
