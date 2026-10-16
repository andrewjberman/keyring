set -u
# IRPT_ANLREQ TO-READ-PACING (issuer 2.0.0_SA_COO~G2, round 45): PRD v0.22 item 4, the CRO's one measured read (RESEARCH_20261016_YCHARTS_PACING_AND_YFINANCE_FIRST.md section 2), as ONE read-only script.
# READ ONLY: nothing is written on the host but a temp file. Up to TWELVE outbound requests, each made the way the upload door makes its ticker lookup: SESSIONLESS (an empty cookie jar,
# the resident's own lookup user-agent, plain urllib, GET /securities/securities_info?securities=<SYMBOL>) by the running root's own transport code, in a transient unit with the
# resident service's own user, environment and interpreter. It does NOT use the stored session and does NOT take the provider lease; the CALLER makes sure no upload and no run is
# using the door while it runs (about 21 minutes), because every other YCharts call from this host shares the firewall window it measures.
# Phase A: rest REST seconds (390 by default, the measured clearing time), then up to N lookups (6) of six KNOWN symbols GAP_A seconds apart (90).
# Phase B: rest REST seconds again, then up to N lookups of six other KNOWN symbols GAP_B seconds apart (5). Each phase STOPS at its first challenge or refusal (a further call would only
# lengthen the block) and prints the index of that call. The two cutoffs are comparable because both phases start from the same rest.
# Reading (the CRO's): the same cutoff index in A and B = a count per window; a different one = something else (spacing, or bot detection).
# Written for IRPT_ANLREQ round 45. NOT RUN: a CloudOps applier runs it, as root (systemd-run needs it). Send it with a command timeout of at least 1800 s.
U=irpt-analysis-resident.service
echo "PACE unit: $(systemctl is-active $U) MainPID=$(systemctl show -p MainPID --value $U) ActiveEnter=$(systemctl show -p ActiveEnterTimestamp --value $U)"
USR=$(systemctl show -p User --value $U)
WD=$(systemctl show -p WorkingDirectory --value $U)
ENVS=$(systemctl show -p Environment --value $U)
PY=$(systemctl show -p ExecStart --value $U | grep -o 'argv\[\]=[^ ]*' | head -1 | cut -d= -f2)
echo "PACE user=$USR workdir=$WD interpreter=$PY"
if [ -z "$USR" ] || [ -z "$WD" ] || [ -z "$PY" ]; then echo "PACE FAIL a unit property is empty (user, workdir or interpreter)"; exit 61; fi
TOKEN=$(curl -s -m 3 -X PUT http://169.254.169.254/latest/api/token -H 'X-aws-ec2-metadata-token-ttl-seconds: 60' 2>/dev/null || true)
PUBIP=$(curl -s -m 3 -H "X-aws-ec2-metadata-token: $TOKEN" http://169.254.169.254/latest/meta-data/public-ipv4 2>/dev/null || true)
echo "PACE public-ipv4 (instance metadata): ${PUBIP:-none}"
BUSY=$(journalctl -u $U --utc --since '-60 s' --no-pager 2>/dev/null | grep -c 'IRPT_RESIDENT_POLL handled=[1-9]')
echo "PACE resident messages handled in the last 60 s: $BUSY"
if [ "$BUSY" != "0" ]; then echo "PACE FAIL the resident is busy; no lookup made"; exit 70; fi
SETENV=""
for e in $ENVS; do SETENV="$SETENV --setenv=$e"; done
PYF=${PACE_PYFILE:-/tmp/paced_lookup_probe.py}
cat > "$PYF" <<'PYEOF'
import os
import re
import sys
import time

root = os.getcwd()
for sub in ("reports", "ycharts/generate", "ycharts/session", "ycharts/extract", "_scope", "_ids", "_keys", "_authz", "intake", "ops", "lib"):
    sys.path.insert(0, root + "/" + sub)
REST = float(os.environ.get("PACE_REST", "390"))
GAP_A = float(os.environ.get("PACE_GAP_A", "90"))
GAP_B = float(os.environ.get("PACE_GAP_B", "5"))
N = int(os.environ.get("PACE_N", "6"))
SYMS_A = ["SPY", "AAPL", "MSFT", "QQQ", "VTI", "IWM"]
SYMS_B = ["DIA", "XLK", "XLF", "EFA", "AGG", "GLD"]
print("PACE process: uid=%s cwd=%s rest=%s gap_a=%s gap_b=%s n=%s" % (getattr(os, "getuid", lambda: -1)(), root, REST, GAP_A, GAP_B, N))
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


def phase(name, symbols, gap):
    print("PACE PHASE %s rest %.0f s" % (name, REST), flush=True)
    time.sleep(REST)
    cutoff = None
    for index, symbol in enumerate(symbols[:N], start=1):
        if index > 1:
            time.sleep(gap)
        verdict, line = one(symbol)
        print("PACE PHASE %s call=%d symbol=%s t=%s verdict=%s %s" % (name, index, symbol, time.strftime("%H:%M:%SZ", time.gmtime()), verdict, line), flush=True)
        if verdict != "CLEAN":
            cutoff = index
            break
    return cutoff


a = phase("A", SYMS_A, GAP_A)
b = phase("B", SYMS_B, GAP_B)
print("PACE RESULT cutoff_A=%s cutoff_B=%s (the index of the first challenged call; none = all %d clean)" % (a if a else "none", b if b else "none", N))
print("PACE VERDICT %s" % ("SAME CUTOFF: a count per window" if a == b and a else "BOTH CLEAN: no cutoff within %d calls" % N if a is None and b is None else "DIFFERENT CUTOFFS: not a plain count per window"))
PYEOF
chmod 644 "$PYF"
echo "PACE script sha256: $(sha256sum "$PYF" | cut -d' ' -f1)"
systemd-run --quiet --wait --pipe --collect --uid="$USR" -p WorkingDirectory="$WD" --setenv=PACE_REST="${PACE_REST:-390}" --setenv=PACE_GAP_A="${PACE_GAP_A:-90}" --setenv=PACE_GAP_B="${PACE_GAP_B:-5}" --setenv=PACE_N="${PACE_N:-6}" $SETENV "$PY" "$PYF"
RC=$?
echo "PACE transient unit rc=$RC"
rm -f "$PYF"
exit $RC
