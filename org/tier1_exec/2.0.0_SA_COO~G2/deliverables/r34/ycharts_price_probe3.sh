set -u
# IRPT_ANLREQ TO-READ-YCHARTS-PRICEFORM (issuer 2.0.0_SA_COO~G2, round 52): the ONE confirming read of CTO msg 10040 (ruling 2). The id:<TICKER> form and the id:level recipe form were both refused HTTP 400 for SPY
# on r34h. The CRO (research @c9f3005376, msg 10037) found the estate's working client: infra/aws/lambda/ycharts-market-data-pull/ycharts_client.py:219-249, fund_data(): the FULL quote-page form with
# calcs=id:price for a security or ETF (id:level only for a ^ index), 67 of 67 HTTP 200 in May. This read sends exactly those parameters for SPY, once, through the resident's stored session under the provider
# lease and the root's window budget (6 calls, 390 s). ONE request. The request is encoded as that client encodes it (urllib.parse.urlencode with its defaults). It prints the status, the content type, the answer's
# SHAPE (key names, lengths, the first and last point) and the existing price_adapter_ycharts reader's row count over the answer; never a body, cookie, token or secret.
# READ ONLY: nothing is written on the host but a temp file. Run it only 390 s or more after the last YCharts call from this host, while no upload or run uses the door.
# Written for IRPT_ANLREQ round 52. NOT RUN: a CloudOps applier runs it, as root (systemd-run needs it).
U=irpt-analysis-resident.service
echo "YCP3 unit: $(systemctl is-active $U) MainPID=$(systemctl show -p MainPID --value $U) ActiveEnter=$(systemctl show -p ActiveEnterTimestamp --value $U)"
USR=$(systemctl show -p User --value $U)
WD=$(systemctl show -p WorkingDirectory --value $U)
ENVS=$(systemctl show -p Environment --value $U)
PY=$(systemctl show -p ExecStart --value $U | grep -o 'argv\[\]=[^ ]*' | head -1 | cut -d= -f2)
echo "YCP3 user=$USR workdir=$WD interpreter=$PY"
if [ -z "$USR" ] || [ -z "$WD" ] || [ -z "$PY" ]; then echo "YCP3 FAIL a unit property is empty (user, workdir or interpreter)"; exit 61; fi
BUSY=$(journalctl -u $U --utc --since '-60 s' --no-pager 2>/dev/null | grep -c 'IRPT_RESIDENT_POLL handled=[1-9]')
echo "YCP3 resident messages handled in the last 60 s: $BUSY"
if [ "$BUSY" != "0" ]; then echo "YCP3 FAIL the resident is busy; no call made"; exit 70; fi
SETENV=""
for e in $ENVS; do SETENV="$SETENV --setenv=$e"; done
PYF=${YCP3_PYFILE:-/tmp/ycharts_price_probe3.py}
cat > "$PYF" <<'PYEOF'
import json
import os
import re
import sys
import time

root = os.getcwd()
for sub in ("reports", "ycharts/generate", "ycharts/session", "ycharts/extract", "ycharts/research", "_scope", "_ids", "_keys", "_authz", "intake", "ops", "lib"):
    sys.path.insert(0, root + "/" + sub)
print("YCP3 process: uid=%s cwd=%s" % (getattr(os, "getuid", lambda: -1)(), root))
bindings = json.load(open(root + "/reports/resident_bindings.json", encoding="utf-8"))
budget = bindings.get("ycharts_window_budget")
window_budget = (budget["calls"], budget["window_s"]) if isinstance(budget, dict) else None
print("YCP3 bindings: tiers=%s budget=%s" % (json.dumps((bindings.get("opal_pricing") or {}).get("tiers")), json.dumps(budget)))
import boto3  # noqa: E402  (the service's own environment)
import price_adapter_ycharts  # noqa: E402
import price_transport_ycharts  # noqa: E402
from resident_session import ResidentSession  # noqa: E402

FUND = "/charts/fund_data.json"
LOOKUP = "/securities/securities_info?securities="
ID_KEYS = ("id", "security_id", "display_security_id", "securitylist_security_id")


def clean(value):
    return re.sub(r"crumb=[^&\s'\"]*", "crumb=REDACTED", str(value))


def summarise(answer):
    """The answer's SHAPE (never its body): top-level keys, the chart_data nesting, the raw_data length and its first and last point."""
    out = {"type": type(answer).__name__}
    if isinstance(answer, dict):
        out["top_keys"] = sorted(answer)[:12]
        try:
            cd = answer["chart_data"]
            out["chart_data_len"] = len(cd)
            out["chart_data0_len"] = len(cd[0])
            out["point_keys"] = sorted(cd[0][0])[:12]
            raw = cd[0][0]["raw_data"]
            out["raw_data_len"] = len(raw)
            if raw:
                out["first_point"] = [raw[0][0], raw[0][1]]
                out["last_point"] = [raw[-1][0], raw[-1][1]]
        except (KeyError, IndexError, TypeError) as exc:
            out["shape_error"] = type(exc).__name__
    return out


# The estate client's parameters, in its order (ycharts_client.py:230-247), for calc=price.
ESTATE = [("aiSummaries", ""), ("calcs", "id:price,include:true,,"), ("chartId", ""), ("chartType", "interactive"), ("correlations", ""), ("customGrowthAmount", ""),
          ("dataInLegend", "value"), ("dateSelection", "range"), ("displayDateRange", "false"), ("endDate", ""), ("format", "real"), ("legendOnChart", "false"),
          ("lineAnnotations", ""), ("nameInLegend", "name_and_ticker"), ("note", ""), ("partner", "basic_2000"), ("performanceDisclosure", "false"), ("quoteLegend", "false"),
          ("recessions", "false"), ("scaleType", "linear"), ("securities", "id:SPY,include:true,,"), ("securityGroup", ""), ("securitylistName", ""), ("securitylistSecurityId", ""),
          ("source", "false"), ("splitType", "single"), ("startDate", ""), ("title", ""), ("units", "false"), ("useCustomColors", "false"), ("useEstimates", "false"),
          ("zoom", "max"), ("hideValueFlags", "false"), ("redesign", "true"), ("chartAnnotations", ""), ("axisExtremes", ""), ("sortColumn", ""), ("sortDirection", ""),
          ("le_o", "quote_page_fund_data"), ("maxPoints", "100000"), ("chartCreator", "false")]
import urllib.parse  # noqa: E402

session = ResidentSession(secrets_client=boto3.client("secretsmanager", region_name=bindings["region"]),
                          dynamo_client=boto3.client("dynamodb", region_name=bindings["region"]), jobs_table=bindings["jobs_table"],
                          enrolled_user_id=bindings["enrolled_user_id"], clock=time.time, window_budget=window_budget)
path = FUND + "?" + urllib.parse.urlencode(dict(ESTATE))
started = time.time()
status, ctype, answer = None, None, None
try:
    facade = session.acquire()
    try:
        info, body = facade.request(path)
    finally:
        facade.close()
    status, ctype = info.get("status"), info.get("content_type")
    answer = json.loads(body) if status == 200 else None
except BaseException as exc:  # a probe prints whatever is raised
    print("YCP3 CALL 1 mode=session what=fund_data:SPY:estate-form verdict=EXCEPTION module=%s name=%s message=%r" % (type(exc).__module__, type(exc).__name__, clean(exc)[:200]), flush=True)
shape = summarise(answer) if answer is not None else {"status": status, "content_type": ctype}
print("YCP3 CALL 1 mode=session what=fund_data:SPY:estate-form params=%d t=%s elapsed=%.2f status=%s shape=%s" % (len(ESTATE), time.strftime("%H:%M:%SZ", time.gmtime()), time.time() - started, status, json.dumps(shape, sort_keys=True)), flush=True)
rows = price_adapter_ycharts.make_reader(lambda p, q, answer=answer: answer)("SPY", "1990-01-01", "2100-01-01") if answer is not None else []
if answer is not None:
    print("YCP3 adapter symbol=SPY rows=%d first=%s last=%s" % (len(rows), rows[0] if rows else None, rows[-1] if rows else None), flush=True)
print("YCP3 RESULT status=%s shape=%s rows=%d calls=1" % (status, "ADAPTER_PARSES" if rows else ("NOT_PARSED" if answer is not None else "UNREAD"), len(rows)))
PYEOF
chmod 644 "$PYF"
echo "YCP3 script sha256: $(sha256sum "$PYF" | cut -d' ' -f1)"
systemd-run --quiet --wait --pipe --collect --uid="$USR" -p WorkingDirectory="$WD" $SETENV "$PY" "$PYF"
RC=$?
echo "YCP3 transient unit rc=$RC"
rm -f "$PYF"
exit $RC
