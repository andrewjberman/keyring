set -u
# IRPT_ANLREQ TO-READ-UNKNOWNS (issuer 2.0.0_SA_COO~G2, round 51): the CTO's condition after r34h (msgs 9761 and 9902): ONE paced read of UNKNOWN symbols that LOGS EVERY securities_info CALL,
# verifies included, so it separates "a count per window" from "unknown symbols trip the firewall earlier". No client data: the symbols are six made-up tickers that no one holds.
# READ ONLY: nothing is written on the host but a temp file. Each call is made the way the upload door makes it: SESSIONLESS (an empty cookie jar, the resident's own lookup user-agent, plain urllib,
# GET /securities/securities_info?securities=<SYMBOL>) by the running root's own transport code, in a transient unit with the resident service's own user, environment and interpreter. It does NOT use the stored
# session and does NOT take the provider lease; the CALLER makes sure the door is free (about 12 minutes) because every other YCharts call from this host shares the firewall window it measures.
# For each of up to N unknown tickers (6): one LOOKUP call of the unknown ticker, then (as the door's suggestion verify does for a NOT_FOUND symbol) one VERIFY call of a known ticker (AAPL), about 2 s later;
# the next ticker follows GAP seconds later (90). After a REST (390 s) at the start. The run STOPS at the first challenged or refused call. Every call is numbered in order.
# Reading: a first challenged call number n of 7 or more = consistent with a count of 6 calls per window; n of 6 or fewer, landing on an unknown LOOKUP = unknown symbols trip earlier than the count;
# none in 12 calls = no cutoff within the budget the release enforces.
# Written for IRPT_ANLREQ round 51. NOT RUN: a CloudOps applier runs it, as root (systemd-run needs it). Send it with a command timeout of at least 3600 s.
U=irpt-analysis-resident.service
echo "UNK unit: $(systemctl is-active $U) MainPID=$(systemctl show -p MainPID --value $U) ActiveEnter=$(systemctl show -p ActiveEnterTimestamp --value $U)"
USR=$(systemctl show -p User --value $U)
WD=$(systemctl show -p WorkingDirectory --value $U)
ENVS=$(systemctl show -p Environment --value $U)
PY=$(systemctl show -p ExecStart --value $U | grep -o 'argv\[\]=[^ ]*' | head -1 | cut -d= -f2)
echo "UNK user=$USR workdir=$WD interpreter=$PY"
if [ -z "$USR" ] || [ -z "$WD" ] || [ -z "$PY" ]; then echo "UNK FAIL a unit property is empty (user, workdir or interpreter)"; exit 61; fi
TOKEN=$(curl -s -m 3 -X PUT http://169.254.169.254/latest/api/token -H 'X-aws-ec2-metadata-token-ttl-seconds: 60' 2>/dev/null || true)
PUBIP=$(curl -s -m 3 -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4 2>/dev/null || true)
echo "UNK public-ipv4 (instance metadata): ${PUBIP:-none}"
BUSY=$(journalctl -u $U --utc --since '-60 s' --no-pager 2>/dev/null | grep -c 'IRPT_RESIDENT_POLL handled=[1-9]')
echo "UNK resident messages handled in the last 60 s: $BUSY"
if [ "$BUSY" != "0" ]; then echo "UNK FAIL the resident is busy; no lookup made"; exit 70; fi
SETENV=""
for e in $ENVS; do SETENV="$SETENV --setenv=$e"; done
PYF=${UNK_PYFILE:-/tmp/unknown_lookup_probe.py}
cat > "$PYF" <<'PYEOF'
import os
import re
import sys
import time

root = os.getcwd()
for sub in ("reports", "ycharts/generate", "ycharts/session", "ycharts/extract", "_scope", "_ids", "_keys", "_authz", "intake", "ops", "lib"):
    sys.path.insert(0, root + "/" + sub)
REST = float(os.environ.get("UNK_REST", "390"))
GAP = float(os.environ.get("UNK_GAP", "90"))
PAIR_GAP = float(os.environ.get("UNK_PAIR_GAP", "2"))
N = int(os.environ.get("UNK_N", "6"))
UNKNOWN = ["QQZXV01", "QQZXV02", "QQZXV03", "QQZXV04", "QQZXV05", "QQZXV06"]
KNOWN_VERIFY = "AAPL"
print("UNK process: uid=%s cwd=%s rest=%s gap=%s pair_gap=%s n=%s" % (getattr(os, "getuid", lambda: -1)(), root, REST, GAP, PAIR_GAP, N))
import transport as tp  # noqa: E402  (the running root's own transport)
from resident_session import LOOKUP_USER_AGENT  # noqa: E402


def clean(value):
    return re.sub(r"crumb=[^&\s'\"]*", "crumb=REDACTED", str(value))


def one(symbol):
    """One sessionless lookup on a fresh empty-jar transport. Returns (verdict, line)."""
    session = tp.Transport.from_bundle({"schema_version": 1, "capture_origin": "EC2", "cookies": [], "user_agent": LOOKUP_USER_AGENT})
    started = time.time()
    try:
        info, body = session.request("/securities/securities_info?securities=" + symbol)
    except BaseException as exc:  # a probe prints whatever is raised
        return "EXCEPTION", "module=%s name=%s message=%r" % (type(exc).__module__, type(exc).__name__, clean(exc)[:160])
    ok = info.get("status") == 200 and not info.get("waf_action") and info.get("content_type") == "application/json"
    return ("CLEAN" if ok else "CHALLENGED"), "status=%s waf_action=%r content_type=%s bytes=%s elapsed=%.2f" % (
        info.get("status"), info.get("waf_action"), info.get("content_type"), info.get("bytes"), time.time() - started)


print("UNK REST %.0f s" % REST, flush=True)
time.sleep(REST)
calls, lookups, first = 0, 0, None
for index, symbol in enumerate(UNKNOWN[:N], start=1):
    if index > 1:
        time.sleep(GAP)
    for kind, name in (("LOOKUP", symbol), ("VERIFY", KNOWN_VERIFY)):
        if kind == "VERIFY":
            time.sleep(PAIR_GAP)
        calls += 1
        lookups += kind == "LOOKUP"
        verdict, line = one(name)
        print("UNK CALL %d ticker=%d kind=%s symbol=%s t=%s verdict=%s %s" % (calls, index, kind, name, time.strftime("%H:%M:%SZ", time.gmtime()), verdict, line), flush=True)
        if verdict != "CLEAN":
            first = (calls, index, kind)
            break
    if first:
        break
if first:
    n, ticker, kind = first
    reading = ("CUTOFF AT CALL %d (%s of ticker %d): consistent with a count of 6 calls per window" % (n, kind, ticker)) if n >= 7 else (
        "CUTOFF AT CALL %d (%s of ticker %d): earlier than a count of 6 allows%s" % (n, kind, ticker, "; unknown symbols trip the firewall" if kind == "LOOKUP" else ""))
else:
    reading = "NO CUTOFF in %d calls: no trip within the budget the release enforces" % calls
print("UNK RESULT first_challenged_call=%s calls=%d unknown_lookups=%d" % (first[0] if first else "none", calls, lookups))
print("UNK VERDICT %s" % reading)
PYEOF
chmod 644 "$PYF"
echo "UNK script sha256: $(sha256sum "$PYF" | cut -d' ' -f1)"
systemd-run --quiet --wait --pipe --collect --uid="$USR" -p WorkingDirectory="$WD" --setenv=UNK_REST="${UNK_REST:-390}" --setenv=UNK_GAP="${UNK_GAP:-90}" --setenv=UNK_PAIR_GAP="${UNK_PAIR_GAP:-2}" --setenv=UNK_N="${UNK_N:-6}" $SETENV "$PY" "$PYF"
RC=$?
echo "UNK transient unit rc=$RC"
rm -f "$PYF"
exit $RC
