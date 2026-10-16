set -u
# IRPT_ANLREQ TO-READ-WAFLOOK (issuer 2.0.0_SA_COO~G2, round 41): the CTO's decision on R3_SET2_WAF_READ (msg 9422), steps 1 and 2, as ONE read-only script.
# READ ONLY: nothing is written on the host but a temp file; ONE outbound request, made the way the upload door makes its ticker lookup: SESSIONLESS (an empty cookie jar,
# the resident's own lookup user-agent, plain urllib, GET /securities/securities_info?securities=ZQXWVK) by the running root's own transport code, in a transient unit with the
# resident service's own user, environment and interpreter (the root is the service's WorkingDirectory). It does NOT use the stored session and does NOT take the provider lease.
# Part 1 (journal, 13:36Z to 13:45Z by default): the session, capture, refresh, rotation, eviction and WAF lines, and the unit's start time.
# Part 2 (the host's public address as the instance metadata service reports it, and a busy guard: it refuses to look up while the resident handled a message in the last 60 s).
# Part 3 (the ONE lookup): prints the HTTP status, the WAF action header, the content type, the byte count and the first 200 characters of the body (a crumb= token redacted).
# Written for IRPT_ANLREQ round 41. NOT RUN: a CloudOps applier runs it, as root (systemd-run needs it).
U=irpt-analysis-resident.service
SINCE=${WAF_SINCE:-2026-10-16 13:36:00}
UNTIL=${WAF_UNTIL:-2026-10-16 13:45:00}
SYM=${WAF_SYMBOL:-ZQXWVK}
echo "WAF unit: $(systemctl is-active $U) MainPID=$(systemctl show -p MainPID --value $U) ActiveEnter=$(systemctl show -p ActiveEnterTimestamp --value $U)"
USR=$(systemctl show -p User --value $U)
WD=$(systemctl show -p WorkingDirectory --value $U)
ENVS=$(systemctl show -p Environment --value $U)
PY=$(systemctl show -p ExecStart --value $U | grep -o 'argv\[\]=[^ ]*' | head -1 | cut -d= -f2)
echo "WAF user=$USR workdir=$WD interpreter=$PY"
if [ -z "$USR" ] || [ -z "$WD" ] || [ -z "$PY" ]; then echo "WAF FAIL a unit property is empty (user, workdir or interpreter)"; exit 61; fi
echo "WAF PART 1 journal window: $SINCE to $UNTIL (UTC)"
TOTAL=$(journalctl -u $U --utc --since "$SINCE" --until "$UNTIL" --no-pager 2>/dev/null | wc -l)
echo "WAF journal window lines: $TOTAL"
journalctl -u $U --utc --since "$SINCE" --until "$UNTIL" --no-pager 2>/dev/null | grep -i -E 'capture|refresh|session|rotation|evict|BROWSER_ATTENTION|waf|challenge|IRPT_RESIDENT_RESOLVE' | cut -c1-260 | sed -e 's/crumb=[^& ]*/crumb=REDACTED/g' | head -60
echo "WAF journal lines naming the session or a capture: $(journalctl -u $U --utc --since "$SINCE" --until "$UNTIL" --no-pager 2>/dev/null | grep -c -i -E 'capture|refresh|session|rotation|evict')"
echo "WAF PART 2 address and busy guard"
TOKEN=$(curl -s -m 3 -X PUT http://169.254.169.254/latest/api/token -H 'X-aws-ec2-metadata-token-ttl-seconds: 60' 2>/dev/null || true)
PUBIP=$(curl -s -m 3 -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4 2>/dev/null || true)
echo "WAF public-ipv4 (instance metadata): ${PUBIP:-none}"
BUSY=$(journalctl -u $U --utc --since '-60 s' --no-pager 2>/dev/null | grep -c 'IRPT_RESIDENT_POLL handled=[1-9]')
echo "WAF resident messages handled in the last 60 s: $BUSY"
if [ "$BUSY" != "0" ]; then echo "WAF FAIL the resident is busy; no lookup made"; exit 70; fi
SETENV=""
for e in $ENVS; do SETENV="$SETENV --setenv=$e"; done
PYF=${WAF_PYFILE:-/tmp/waf_lookup_probe.py}
cat > "$PYF" <<'PYEOF'
import os
import re
import sys
import time

root = os.getcwd()
for sub in ("reports", "ycharts/generate", "ycharts/session", "ycharts/extract", "_scope", "_ids", "_keys", "_authz", "intake", "ops", "lib"):
    sys.path.insert(0, root + "/" + sub)
symbol = os.environ.get("WAF_SYMBOL", "ZQXWVK")
print("WAF PART 3 process: uid=%s cwd=%s" % (getattr(os, "getuid", lambda: -1)(), root))
import transport as tp  # noqa: E402  (the running root's own transport)
from resident_session import LOOKUP_USER_AGENT  # noqa: E402


def clean(value):
    return re.sub(r"crumb=[^&\s'\"]*", "crumb=REDACTED", str(value))


session = tp.Transport.from_bundle({"schema_version": 1, "capture_origin": "EC2", "cookies": [], "user_agent": LOOKUP_USER_AGENT})
print("WAF PART 3 cookie jar entries: %d (want 0)" % len(list(getattr(session, "jar", ()))))
route = "/securities/securities_info?securities=" + symbol
started = time.time()
try:
    info, body = session.request(route)
except BaseException as exc:  # a probe prints whatever is raised
    print("WAF LOOKUP EXCEPTION module=%s name=%s message=%r" % (type(exc).__module__, type(exc).__name__, clean(exc)[:200]))
    sys.exit(2)
print("WAF LOOKUP status=%s waf_action=%r content_type=%s bytes=%s body_complete=%s login_destination=%s final_url_path=%s elapsed=%.2f" % (
    info.get("status"), info.get("waf_action"), info.get("content_type"), info.get("bytes"), info.get("body_complete"), info.get("login_destination"),
    info.get("final_url_path"), time.time() - started))
print("WAF LOOKUP BODY[:200] %r" % clean(body[:200].decode("utf-8", "replace")))
print("WAF LOOKUP VERDICT %s" % ("CLEAN 200 json, no waf action" if info.get("status") == 200 and not info.get("waf_action") and info.get("content_type") == "application/json" else "CHALLENGED OR REFUSED"))
PYEOF
chmod 644 "$PYF"
echo "WAF script sha256: $(sha256sum "$PYF" | cut -d' ' -f1)"
systemd-run --quiet --wait --pipe --collect --uid="$USR" -p WorkingDirectory="$WD" --setenv=WAF_SYMBOL="$SYM" $SETENV "$PY" "$PYF"
RC=$?
echo "WAF transient unit rc=$RC"
rm -f "$PYF"
exit $RC
