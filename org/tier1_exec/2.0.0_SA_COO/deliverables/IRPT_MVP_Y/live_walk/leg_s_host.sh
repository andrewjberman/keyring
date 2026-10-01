# Leg S -- ONE operator run of the canonical YCharts sign-in wrapper in the resident's own process context.
#
# Sent verbatim to the resident host by host_read.py (Systems Manager, root). THIS IS A LIVE VENDOR CALL: one sign-in.
# Authority: CTO rulings batch 70 (2026-10-01) item 1 leg S; Andrew's standing word of 2026-09-23 item 3 (the host's own
# session sign-in and maintenance). Packet: HOP7B/WINDOW_PACKET_HOP7B_SIGNIN_THEN_JOB_20261001.md, both halves.
#
# What "the resident's context" means here, each read from the running unit and not typed:
#   user and groups  -- the owner of the resident's main pid
#   environment      -- /proc/<pid>/environ minus every PYTHON* name (host_capture.capture_env does exactly this)
#   argv, cwd        -- /bin/bash <wrapper>, in the wrapper's directory; stdin /dev/null; its own session
# Two differences from the resident's call, both deliberate: stdout goes to a 0600 file instead of a pipe, and stderr
# goes to a 0600 file instead of /dev/null. The wrapper is run ONCE. Nothing here retries, answers a challenge, or
# reads a secret value. The printed receipt is a redacted walk: booleans and numbers as they are, strings masked for
# e-mail addresses and cut at 200 characters, and no leaf under a key named value, password or token.
set -u
umask 077
D=/root/irpt-leg-s
mkdir -p "$D"
TS=$(date -u +%Y%m%dT%H%M%SZ)
echo "leg S start $TS selinux=$(getenforce 2>&1)"
/usr/bin/python3.12 - "$D" "$TS" <<'PY'
import hashlib
import json
import os
import pwd
import re
import signal
import subprocess
import sys
import time

D, TS = sys.argv[1], sys.argv[2]
H = "/opt/investor-reporting-ycharts"
WRAPPER = H + "/run-ycharts-session.sh"
UNIT = "irpt-analysis-resident.service"
REGION = "us-east-1"
EMAIL = re.compile(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+")
SECRET_KEY = re.compile(r"(?i)(value|password|token)$")


def mask(value):
    return EMAIL.sub("<email>", str(value))[:200]


def sh(*argv):
    return subprocess.run(argv, capture_output=True, text=True).stdout.strip()


pid = int(sh("systemctl", "show", UNIT, "-p", "MainPID", "--value") or 0)
if pid <= 0:
    print("REFUSED: the resident unit has no main pid; nothing run")
    sys.exit(3)
env = {}
for item in open("/proc/%d/environ" % pid, "rb").read().split(b"\0"):
    if b"=" in item:
        key, value = item.split(b"=", 1)
        if not key.decode().upper().startswith("PYTHON"):
            env[key.decode()] = value.decode()
pointers = open(H + "/secret-ids.env", encoding="utf-8").read()
if any("YC_RECORD_HAR" in text for text in (pointers, " ".join(env))):
    print("REFUSED: a HAR recording variable is set; a recorded run is a different packet; nothing run")
    sys.exit(4)
owner = pwd.getpwuid(os.stat("/proc/%d" % pid).st_uid)
print("resident pid %d user %s cwd %s" % (pid, owner.pw_name, os.readlink("/proc/%d/cwd" % pid)))
print("environment names passed: " + " ".join(sorted(env)))
for path in (WRAPPER, H + "/ycharts_session.js"):
    print("pin %s %s" % (os.path.basename(path), hashlib.sha256(open(path, "rb").read()).hexdigest()[:16]))
ids = dict(line.split("=", 1) for line in pointers.splitlines() if "=" in line and not line.startswith("#"))
session_id = ids["YC_SESSION_SECRET_ID"].strip().strip('"')


def session_changed():
    return sh("aws", "secretsmanager", "describe-secret", "--secret-id", session_id, "--query", "LastChangedDate",
              "--output", "text", "--region", REGION)


before = session_changed()
print("stored session last changed BEFORE: " + before)
out_path, err_path = (os.path.join(D, "leg_s_%s.%s" % (TS, kind)) for kind in ("stdout", "stderr"))
start = time.time()
with open(out_path, "wb") as out, open(err_path, "wb") as err:
    child = subprocess.Popen(["/bin/bash", WRAPPER], cwd=H, env=env, stdin=subprocess.DEVNULL, stdout=out, stderr=err,
                             start_new_session=True, user=owner.pw_name, group=owner.pw_gid,
                             extra_groups=os.getgrouplist(owner.pw_name, owner.pw_gid))
    try:
        rc = child.wait(timeout=240)
    except subprocess.TimeoutExpired:
        rc = "TIMEOUT_240S"
    finally:
        try:
            os.killpg(child.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass
        child.wait()
data = open(out_path, "rb").read()
print("rc %s seconds %.1f stdout bytes %d stderr bytes %d" % (rc, time.time() - start, len(data), os.path.getsize(err_path)))
print("receipt files (mode, name): " + ", ".join("%o %s" % (os.stat(p).st_mode & 0o777, p) for p in (out_path, err_path)))
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
print("LEG_S_VERDICT=" + verdict)
PY
echo "leg S end $(date -u +%Y%m%dT%H%M%SZ)"
