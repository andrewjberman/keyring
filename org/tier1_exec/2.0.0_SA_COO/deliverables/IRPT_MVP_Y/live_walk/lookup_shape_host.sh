# TWO ticker lookups on the resident host, each printing the answer's SHAPE and no body.
#
# Sent verbatim to the host by host_read.py (Systems Manager, root). THIS IS A LIVE VENDOR CALL: exactly two GETs of
# /securities/securities_info for AAPL and VNQ, the lookup the upload flow makes. No sign-in, no POST, no retry.
# Authority: CTO rulings batch 72 items 9 to 11 (item 11 is the CTO half); Andrew's standing word of 2026-09-23, whose
# record names "the sessionless ticker lookups of the upload flow". COO half: ledger irpt-hop3-lookup-shape-20261001,
# which carries this file's sha256.
#
#   GET 1  exactly as the resident makes it: the unit's own factory (resident_installed:build_resident_runtime), as the
#          resident's user with the unit's PYTHONPATH, session.acquire() (the provider operation lease), one request,
#          close.
#   GET 2  with NO session at all: no cookie jar, the same request headers, after the lease's own spacing.
#
# The capture path is unreachable: the script removes the session's capture workflow before anything is sent, so an
# evicted answer is printed, never repaired. Printed per GET: every field of the answer's record (method, route, status,
# content type, byte count, WAF action, login-destination flag, final path); which of the resolver's acceptance
# conditions fail, by name; the body's SHAPE (JSON type, length, key NAMES of the first row, three booleans for an HTML,
# login or captcha page); the classification per symbol when the answer is acceptable.
set -u
umask 077
UNIT=irpt-analysis-resident.service
PID=$(systemctl show $UNIT -p MainPID --value)
ROOT=$(readlink /proc/$PID/cwd)
SCRIPT=$(mktemp /tmp/irpt_lookup_shape.XXXXXX.py)
echo "lookup-shape start $(date -u +%Y%m%dT%H%M%SZ) resident pid $PID root $ROOT"
cat > "$SCRIPT" <<'PY'
import importlib
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request

root = sys.argv[1]
sys.path.insert(0, root + "/ycharts/generate")
import resident_main  # noqa: F401,E402  (puts the package's directories on sys.path exactly as the unit's entry does)

runtime = importlib.import_module("resident_installed").build_resident_runtime()
session = runtime["assembly"].session
session.capture_workflow = None  # no sign-in can be reached from here: capture_session() now refuses
from operation_lease import OperationLease  # noqa: E402
from resolution_broker import MAX_RESPONSE_BYTES, ROUTE  # noqa: E402
from security_resolution import classify_batch  # noqa: E402
from transport import BASE  # noqa: E402
from upload_resolution import RESOLUTION_SOURCE  # noqa: E402

symbols = ["AAPL", "VNQ"]
account = str(session.broker.enrolled_user_id)
query = ROUTE + "?" + urllib.parse.urlencode({"securities": ",".join(symbols)})


def shape(label, info, body):
    for key in sorted(info):
        print("  info.%s = %s" % (key, repr(info[key])[:120]))
    conditions = {
        "method is GET": info.get("method") == "GET",
        "path is the route": info.get("path") == ROUTE,
        "final path is the route": info.get("final_url_path") == ROUTE,
        "status is 200": info.get("status") == 200,
        "body complete": info.get("body_complete") is True,
        "not a login destination": info.get("login_destination") is False,
        "no WAF action": not info.get("waf_action"),
        "content type is application/json": info.get("content_type") == "application/json",
        "body is bytes within the size bound": isinstance(body, bytes) and 0 < len(body) <= MAX_RESPONSE_BYTES,
        "byte count equals the body": isinstance(body, bytes) and info.get("bytes") == len(body),
    }
    for name, held in conditions.items():
        print("  %-40s %s" % (name, "holds" if held else "FAILS"))
    raw = body if isinstance(body, bytes) else b""
    lowered = raw[:200000].lower()
    print("  body: %d bytes; html page %s; mentions login %s; mentions captcha %s" % (
        len(raw), b"<html" in lowered, b"login" in lowered, b"captcha" in lowered))
    rows = None
    try:
        rows = json.loads(raw.decode("utf-8"))
        if isinstance(rows, list):
            first = rows[0] if rows else None
            print("  body JSON: list of %d; first row %s" % (len(rows), (
                "keys " + ", ".join(sorted(str(k) for k in first)[:40])) if isinstance(first, dict) else type(first).__name__))
        elif isinstance(rows, dict):
            print("  body JSON: object with keys " + ", ".join(sorted(str(k) for k in rows)[:40]))
        else:
            print("  body JSON: " + type(rows).__name__)
    except ValueError:
        print("  body is not JSON")
    if all(conditions.values()) and isinstance(rows, list):
        receipt = {"http_status": 200, "complete": True, "final_url_path": ROUTE, "account_id": account,
                   "source_revision": RESOLUTION_SOURCE, "requested": symbols,
                   "observed_at": "2026-10-01T00:00:00+00:00", "json": rows}
        for symbol, result in sorted(classify_batch(symbols, receipt, account_id=account,
                                                    source_revision=RESOLUTION_SOURCE).items()):
            print("  classified %s: state %s reason %s candidates %d" % (
                symbol, result.get("state"), result.get("reason"), len(result.get("candidates") or [])))
        print("%s_VERDICT=ACCEPTED" % label)
    else:
        failed = [name for name, held in conditions.items() if not held] or ["body is not a JSON list"]
        print("%s_VERDICT=REFUSED:%s" % (label, "; ".join(failed)))


current = session.broker.current()
print("stored session read: state %s fence %s generation %s" % (
    current.get("state"), current.get("fence"), str(current.get("generation"))[:8]))

print("--- GET 1: as the resident makes it (its session, its provider lease)")
user_agent = (current.get("bundle") or {}).get("user_agent") or "Mozilla/5.0"
try:
    transport = session.acquire()
    try:
        info, body = transport.request(query)
    finally:
        transport.close()
    print("  one request made; the lease is released")
    shape("WITH_SESSION", info, body)
except Exception as exc:  # a refusal is printed as its class and closed code, never repaired or retried
    code = str(exc)
    print("WITH_SESSION_VERDICT=RAISED:%s:%s" % (
        type(exc).__name__, code if re.fullmatch(r"[A-Z][A-Z0-9_]{2,63}", code) else "-"))

time.sleep(OperationLease.SPACING + 1.0)
print("--- GET 2: with NO session (no cookie jar), the same headers, after the lease's spacing")


class SameOriginRedirect(urllib.request.HTTPRedirectHandler):
    def redirect_request(self, request, fp, code, message, headers, new_url):
        if urllib.parse.urlsplit(new_url).netloc != urllib.parse.urlsplit(BASE).netloc:
            return None
        return super().redirect_request(request, fp, code, message, headers, new_url)


request = urllib.request.Request(BASE + query, method="GET", headers={
    "User-Agent": user_agent, "X-Requested-With": "XMLHttpRequest",
    "Accept": "application/json, text/plain, */*", "Referer": BASE + "/dashboard/"})
try:
    response = urllib.request.build_opener(SameOriginRedirect()).open(request, timeout=60)
except urllib.error.HTTPError as error:
    response = error
with response:
    bare = response.read()
    bare_info = {"method": "GET", "path": ROUTE, "status": response.status,
                 "content_type": response.headers.get_content_type(), "bytes": len(bare),
                 "set_cookie_count": len(response.headers.get_all("Set-Cookie", [])),
                 "waf_action": response.headers.get("x-amzn-waf-action"),
                 "login_destination": bool(re.search(r"/accounts?/login", response.url)),
                 "final_url_path": urllib.parse.urlsplit(response.url).path, "body_complete": True}
print("  one request made; no cookie was sent")
shape("NO_SESSION", bare_info, bare)
PY
chown ec2-user "$SCRIPT"
sudo -u ec2-user env -i HOME=/home/ec2-user USER=ec2-user LOGNAME=ec2-user LANG=C.UTF-8 \
  PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin PYTHONPATH="$ROOT" PYTHONUNBUFFERED=1 \
  /usr/bin/python3.12 "$SCRIPT" "$ROOT" 2>&1 | cut -c1-400
echo "python rc ${PIPESTATUS[0]}"
rm -f "$SCRIPT"
echo "lookup-shape end $(date -u +%Y%m%dT%H%M%SZ)"
