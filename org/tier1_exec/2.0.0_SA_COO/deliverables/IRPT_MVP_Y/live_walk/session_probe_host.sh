# Leg P -- ONE liveness read of the stored YCharts session on the resident host, printing the answer's SHAPE.
#
# Sent verbatim to the host by host_read.py (Systems Manager, root). THIS IS A LIVE VENDOR CALL: exactly one GET of the
# report-template route, the same read a job makes first (recipe.step_template) and the capture library's own probe
# route. No sign-in, no POST, no retry. Authority and halves: the window packet that carries this file's sha256.
#
# It builds the resident's runtime with the unit's own factory, as the resident's user with the unit's PYTHONPATH,
# removes the session's capture workflow before anything is sent (an evicted answer is printed, never repaired), takes
# the provider operation lease as a job does (session.acquire(), one request, close), and prints the record's fields,
# the body's JSON key NAMES and PROBE_VERDICT. The route is read from the stored bundle's own probe evidence, not typed.
set -u
umask 077
UNIT=irpt-analysis-resident.service
PID=$(systemctl show $UNIT -p MainPID --value)
ROOT=$(readlink /proc/$PID/cwd)
SCRIPT=$(mktemp /tmp/irpt_session_probe.XXXXXX.py)
echo "session-probe start $(date -u +%Y%m%dT%H%M%SZ) resident pid $PID root $ROOT"
cat > "$SCRIPT" <<'PY'
import importlib
import json
import re
import sys

root = sys.argv[1]
sys.path.insert(0, root + "/ycharts/generate")
import resident_main  # noqa: F401,E402  (puts the package's directories on sys.path exactly as the unit's entry does)

runtime = importlib.import_module("resident_installed").build_resident_runtime()
session = runtime["assembly"].session
session.capture_workflow = None  # no sign-in can be reached from here: capture_session() now refuses

current = session.broker.current()
bundle = current.get("bundle") or {}
print("stored session read: state %s fence %s generation %s persisted_at %s" % (
    current.get("state"), current.get("fence"), str(current.get("generation"))[:8], bundle.get("persisted_at")))
path = (bundle.get("probe_evidence") or {}).get("probe_url_path")
if current.get("state") != "OK" or not isinstance(path, str) or not re.fullmatch(r"/custom_pdf_reports/generate/[0-9]{1,12}", path):
    print("PROBE_VERDICT=NOT_RUN:the stored bundle carries no probe route; nothing sent")
    sys.exit(0)
print("probe route: " + path)
try:
    transport = session.acquire()
    try:
        info, body = transport.request(path)
    finally:
        transport.close()
except Exception as exc:  # a refusal is printed as its class and closed code, never repaired or retried
    code = str(exc)
    print("PROBE_VERDICT=RAISED:%s:%s" % (type(exc).__name__, code if re.fullmatch(r"[A-Z][A-Z0-9_]{2,63}", code) else "-"))
    sys.exit(0)
print("  one request made; the lease is released")
for key in sorted(info):
    print("  info.%s = %s" % (key, repr(info[key])[:120]))
raw = body if isinstance(body, bytes) else b""
lowered = raw[:200000].lower()
print("  body: %d bytes; html page %s; mentions login %s; mentions captcha %s" % (
    len(raw), b"<html" in lowered, b"login" in lowered, b"captcha" in lowered))
doc = None
try:
    doc = json.loads(raw.decode("utf-8"))
    print("  body JSON: %s%s" % (type(doc).__name__, (
        " with keys " + ", ".join(sorted(str(k) for k in doc)[:40])) if isinstance(doc, dict) else ""))
except ValueError:
    print("  body is not JSON")
live = (info.get("status") == 200 and not info.get("waf_action") and info.get("login_destination") is False
        and isinstance(doc, dict) and isinstance(doc.get("sections"), list) and str(doc.get("id")) == path.rsplit("/", 1)[1])
if live:
    print("PROBE_VERDICT=LIVE")
elif info.get("waf_action"):
    print("PROBE_VERDICT=CHALLENGED:%s" % re.sub(r"[^A-Za-z0-9_]", "_", str(info.get("waf_action")))[:32])
else:
    print("PROBE_VERDICT=NOT_LIVE:status_%s" % info.get("status"))
PY
chown ec2-user "$SCRIPT"
sudo -u ec2-user env -i HOME=/home/ec2-user USER=ec2-user LOGNAME=ec2-user LANG=C.UTF-8 \
  PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin PYTHONPATH="$ROOT" PYTHONUNBUFFERED=1 \
  /usr/bin/python3.12 "$SCRIPT" "$ROOT" 2>&1 | cut -c1-400
echo "python rc ${PIPESTATUS[0]}"
rm -f "$SCRIPT"
echo "session-probe end $(date -u +%Y%m%dT%H%M%SZ)"
