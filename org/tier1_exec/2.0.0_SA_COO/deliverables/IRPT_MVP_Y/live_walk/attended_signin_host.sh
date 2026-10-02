# Leg A -- ONE ATTENDED operator sign-in on the host (sign-in option A, CTO rulings batch 131 item 3).
#
# Sent verbatim to the resident host by host_read.py (Systems Manager, root, HOST_READ_TIMEOUT_S=1080). THIS IS A LIVE
# VENDOR CALL: one sign-in. It is leg S (live_walk/leg_s_host.sh) with a display a person can reach:
#   - a virtual display, Xvnc :1, bound to 127.0.0.1:5901 only (-localhost, -nolisten tcp), with a ONE-RUN VNC password
#     (the CTO half's follow-up: the laptop's forward listens on localhost:5901 while open). The password is written
#     only to Xvnc's obfuscated password file and to /root/irpt-attended/vnc_password_current (0600, root); it is NEVER
#     printed here. Andrew reads it in his own Systems Manager shell. Both files are deleted at teardown;
#   - the wrapper run ONCE, headed on that display, with YC_ATTENDED=1: at a CAPTCHA the library HOLDS up to 600 s
#     for the person (Andrew, on his laptop: a Systems Manager port forward of 5901 and a VNC viewer on localhost:5901)
#     and then publishes through its own fenced path, exactly as leg S does;
#   - bounded: the wrapper at 840 s (240 s of sign-in plus the 600 s hold), then the process group is killed.
# Nothing here answers a challenge, records the screen, or reads a secret value. The printed receipt is leg S's
# redacted walk. Packet: SIGNIN_A/ (both halves before any run).
set -u
umask 077
D=/root/irpt-attended
mkdir -p "$D"
TS=$(date -u +%Y%m%dT%H%M%SZ)
echo "leg A start $TS"
command -v Xvnc >/dev/null 2>&1 || { echo "REFUSED: Xvnc is not installed (the packet's install leg comes first); nothing run"; echo "LEG_A_VERDICT=NOT_RUN:NO_XVNC"; exit 5; }
/usr/bin/python3.12 - "$D" "$TS" <<'PY'
import hashlib
import json
import os
import pwd
import re
import secrets
import signal
import subprocess
import sys
import time

D, TS = sys.argv[1], sys.argv[2]
H = "/opt/investor-reporting-ycharts"
WRAPPER = H + "/run-ycharts-session.sh"
UNIT = "irpt-analysis-resident.service"
REGION = "us-east-1"
DISPLAY, PORT = ":1", 5901
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+")
SECRET_KEY = re.compile(r"(?i)(value|password|token)$")


def mask(value):
    return EMAIL.sub("<email>", str(value))[:200]


def sh(*argv):
    return subprocess.run(argv, capture_output=True, text=True).stdout.strip()


def listeners():
    return [line.split()[3] for line in sh("ss", "-ltnH").splitlines() if line.split()[3].endswith(":%d" % PORT)]


pid = int(sh("systemctl", "show", UNIT, "-p", "MainPID", "--value") or 0)
if pid <= 0:
    print("REFUSED: the resident unit has no main pid; nothing run")
    print("LEG_A_VERDICT=NOT_RUN:NO_RESIDENT")
    sys.exit(3)
env = {}
for item in open("/proc/%d/environ" % pid, "rb").read().split(b"\0"):
    if b"=" in item:
        key, value = item.split(b"=", 1)
        if not key.decode().upper().startswith("PYTHON"):
            env[key.decode()] = value.decode()
pointers = open(H + "/secret-ids.env", encoding="utf-8").read()
if any("YC_RECORD_HAR" in text for text in (pointers, " ".join(env))):
    print("REFUSED: a HAR recording variable is set; nothing run")
    print("LEG_A_VERDICT=NOT_RUN:HAR")
    sys.exit(4)
if listeners():
    print("REFUSED: something already listens on %d: %s; nothing run" % (PORT, listeners()))
    print("LEG_A_VERDICT=NOT_RUN:PORT_IN_USE")
    sys.exit(6)
owner = pwd.getpwuid(os.stat("/proc/%d" % pid).st_uid)
groups = os.getgrouplist(owner.pw_name, owner.pw_gid)
print("resident pid %d user %s cwd %s" % (pid, owner.pw_name, os.readlink("/proc/%d/cwd" % pid)))
for path in (WRAPPER, H + "/ycharts_session.js"):
    print("pin %s %s" % (os.path.basename(path), hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]))
library = open(H + "/ycharts_session.js", encoding="utf-8").read()
if "YC_ATTENDED" not in library:
    print("REFUSED: the host library has no attended mode (the packet's resident install comes first); nothing run")
    print("LEG_A_VERDICT=NOT_RUN:NO_ATTENDED_MODE")
    sys.exit(7)
ids = dict(line.split("=", 1) for line in pointers.splitlines() if "=" in line and not line.startswith("#"))
session_id = ids["YC_SESSION_SECRET_ID"].strip().strip('"')


def session_changed():
    return sh("aws", "secretsmanager", "describe-secret", "--secret-id", session_id, "--query", "LastChangedDate",
              "--output", "text", "--region", REGION)


# ONE-RUN password: 8 characters (VNC authentication reads 8), never printed. Xvnc reads the obfuscated file as the
# resident's user; Andrew reads the plain file as root in his own session.
secret_dir = os.path.join(owner.pw_dir, ".irpt-attended")
os.makedirs(secret_dir, mode=0o700, exist_ok=True)
os.chown(secret_dir, owner.pw_uid, owner.pw_gid)
os.chmod(secret_dir, 0o700)
password = secrets.token_urlsafe(9)[:8]
passwd_file = os.path.join(secret_dir, "vnc.passwd")
plain_file = os.path.join(D, "vnc_password_current")
obfuscated = subprocess.run(["vncpasswd", "-f"], input=(password + "\n").encode(), capture_output=True).stdout
if len(obfuscated) != 8:
    print("REFUSED: vncpasswd did not produce a password file; nothing run")
    print("LEG_A_VERDICT=NOT_RUN:NO_VNC_PASSWORD")
    sys.exit(9)
for path, data, uid, gid in ((passwd_file, obfuscated, owner.pw_uid, owner.pw_gid), (plain_file, (password + "\n").encode(), 0, 0)):
    fd = os.open(path, os.O_WRONLY | os.O_CREAT | os.O_TRUNC, 0o600)
    os.write(fd, data)
    os.close(fd)
    os.chown(path, uid, gid)
del password
display = subprocess.Popen(["Xvnc", DISPLAY, "-localhost", "-nolisten", "tcp", "-SecurityTypes", "VncAuth",
                            "-PasswordFile", passwd_file,
                            "-rfbport", str(PORT), "-geometry", "1366x900", "-depth", "24"],
                           stdin=subprocess.DEVNULL, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL,
                           start_new_session=True, user=owner.pw_name, group=owner.pw_gid, extra_groups=groups,
                           env={"HOME": owner.pw_dir, "PATH": "/usr/bin:/bin"})
for _ in range(20):
    if listeners():
        break
    time.sleep(0.5)
bound = listeners()
print("display %s pid %d listening on %s" % (DISPLAY, display.pid, bound))
if not bound or any(not b.startswith(("127.0.0.1:", "[::1]:")) for b in bound):
    os.killpg(display.pid, signal.SIGKILL)
    for path in (passwd_file, plain_file):
        os.remove(path)
    print("REFUSED: the display did not bind to loopback only; torn down; nothing run")
    print("LEG_A_VERDICT=NOT_RUN:DISPLAY_BINDING")
    sys.exit(8)
print("VNC password for this run: in %s (0600, root), never printed here; deleted at teardown" % plain_file)
print("ATTENDED_READY %s: port-forward 5901 and open localhost:5901; the hold waits up to 600 s at a CAPTCHA"
      % time.strftime("%Y-%m-%dT%H:%M:%SZ", time.gmtime()))
env.update(DISPLAY=DISPLAY, YC_HEADLESS="0", YC_ATTENDED="1", YC_ATTENDED_WAIT_S="600")
print("environment names passed: " + " ".join(sorted(env)))
before = session_changed()
print("stored session last changed BEFORE: " + before)
out_path, err_path = (os.path.join(D, "leg_a_%s.%s" % (TS, kind)) for kind in ("stdout", "stderr"))
start = time.time()
try:
    with open(out_path, "wb") as out, open(err_path, "wb") as err:
        child = subprocess.Popen(["/bin/bash", WRAPPER], cwd=H, env=env, stdin=subprocess.DEVNULL, stdout=out,
                                 stderr=err, start_new_session=True, user=owner.pw_name, group=owner.pw_gid,
                                 extra_groups=groups)
        try:
            rc = child.wait(timeout=840)
        except subprocess.TimeoutExpired:
            rc = "TIMEOUT_840S"
        finally:
            try:
                os.killpg(child.pid, signal.SIGKILL)
            except ProcessLookupError:
                pass
            child.wait()
finally:
    try:
        os.killpg(display.pid, signal.SIGKILL)
    except ProcessLookupError:
        pass
    display.wait()
    for path in (passwd_file, plain_file):
        try:
            os.remove(path)
        except FileNotFoundError:
            pass
print("display torn down; listening on %d now: %s; password files left: %d" % (
    PORT, listeners(), sum(os.path.exists(path) for path in (passwd_file, plain_file))))
data = open(out_path, "rb").read()
print("rc %s seconds %.1f stdout bytes %d stderr bytes %d" % (rc, time.time() - start, len(data), os.path.getsize(err_path)))
receipts = []
for line in data.decode("utf-8", "replace").splitlines():
    if line.startswith("[orchestrator]"):
        print(mask(line))
    elif line.startswith("{"):
        try:
            receipts.append(json.loads(line))
        except ValueError:
            print("an unparseable receipt line of %d bytes" % len(line))
print("receipt lines: %d" % len(receipts))
lines = []


def walk(node, path):
    if isinstance(node, dict):
        for key in sorted(node):
            walk(node[key], path + [str(key)])
    elif isinstance(node, list):
        if all(not isinstance(item, (dict, list)) for item in node):
            leaf(path, "[" + ", ".join(mask(item)[:60] for item in node[:24]) + "]")
        else:
            for index, item in enumerate(node[:16]):
                walk(item, path + [str(index)])
    else:
        leaf(path, node)


def leaf(path, value):
    if isinstance(value, str) and SECRET_KEY.search(path[-1] if path else ""):
        value = "<not printed>"
    lines.append("  %s = %s" % (".".join(path), mask(value)))


verdict = "FAILED:NO_RECEIPT"
for receipt in receipts[:2]:
    walk(receipt, [])
    if receipt.get("ok") is True and receipt.get("task") == "probe" and (receipt.get("result") or {}).get("authenticated") is True and rc == 0:
        verdict = "AUTHENTICATED"
    else:
        failure = str(receipt.get("failure_class") or "NOT_AUTHENTICATED")
        verdict = ("CHALLENGED:" if "CHALLENGE" in failure.upper() else "FAILED:") + mask(failure)[:64]
print("\n".join(lines[:220]))
if len(lines) > 220:
    print("  ... %d more leaves in the 0600 file" % (len(lines) - 220))
print("--- stderr, masked, first 60 lines")
for line in open(err_path, "rb").read().decode("utf-8", "replace").splitlines()[:60]:
    print("  " + mask(line))
after = session_changed()
print("stored session last changed AFTER:  " + after + (" (a new version)" if after != before else " (unchanged)"))
print("LEG_A_VERDICT=" + verdict)
PY
echo "leg A end $(date -u +%Y%m%dT%H%M%SZ)"
