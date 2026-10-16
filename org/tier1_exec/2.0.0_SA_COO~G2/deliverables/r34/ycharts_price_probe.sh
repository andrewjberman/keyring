set -u
# IRPT_ANLREQ TO-READ-YCPRICE (issuer 2.0.0_SA_COO~G2, round 51): the CTO's THREE-UNKNOWNS measurement (msgs 9727 and 9902), as ONE read-only script, run on r34h AFTER the unknown-symbol paced read and a 390 s rest.
#   1. the id form: does GET /charts/fund_data.json?securities=id:<TICKER>,include:true,&zoom=max answer a plain ticker (SPY and AAPL) with a non-empty series?
#   2. the served shape: is the answer's chart_data[0][0].raw_data a list of [epoch_ms, level] pairs that the existing price_adapter_ycharts reader parses into rows?
#   3. the session: does the same route answer a SIGNED-OUT caller (the door's sessionless transport) as it answers the signed-in resident session?
# READ ONLY: THREE outbound requests in all, made in a transient unit with the resident service's own user, environment and interpreter, from the running root's own code. Calls 1 and 2 go through the
# resident's stored session and the provider lease under the host's own window budget (the root's bindings): the same path the YCharts price tier takes. Call 3 is sessionless (empty cookie jar). Nothing is
# written on the host but a temp file. Market data only (SPY, AAPL): no client data, no cookie, token or secret is printed; a body is summarised, never printed.
# Written for IRPT_ANLREQ round 51. NOT RUN: a CloudOps applier runs it, as root (systemd-run needs it), only while no upload or run uses the door and after the unknown-symbol read's report plus 390 s.
U=irpt-analysis-resident.service
echo "YCP unit: $(systemctl is-active $U) MainPID=$(systemctl show -p MainPID --value $U) ActiveEnter=$(systemctl show -p ActiveEnterTimestamp --value $U)"
USR=$(systemctl show -p User --value $U)
WD=$(systemctl show -p WorkingDirectory --value $U)
ENVS=$(systemctl show -p Environment --value $U)
PY=$(systemctl show -p ExecStart --value $U | grep -o 'argv\[\]=[^ ]*' | head -1 | cut -d= -f2)
echo "YCP user=$USR workdir=$WD interpreter=$PY"
if [ -z "$USR" ] || [ -z "$WD" ] || [ -z "$PY" ]; then echo "YCP FAIL a unit property is empty (user, workdir or interpreter)"; exit 61; fi
BUSY=$(journalctl -u $U --utc --since '-60 s' --no-pager 2>/dev/null | grep -c 'IRPT_RESIDENT_POLL handled=[1-9]')
echo "YCP resident messages handled in the last 60 s: $BUSY"
if [ "$BUSY" != "0" ]; then echo "YCP FAIL the resident is busy; no call made"; exit 70; fi
SETENV=""
for e in $ENVS; do SETENV="$SETENV --setenv=$e"; done
PYF=${YCP_PYFILE:-/tmp/ycharts_price_probe.py}
cat > "$PYF" <<'PYEOF'
import json
import os
import re
import sys
import time

root = os.getcwd()
for sub in ("reports", "ycharts/generate", "ycharts/session", "ycharts/extract", "ycharts/research", "_scope", "_ids", "_keys", "_authz", "intake", "ops", "lib"):
    sys.path.insert(0, root + "/" + sub)
print("YCP process: uid=%s cwd=%s" % (getattr(os, "getuid", lambda: -1)(), root))
bindings = json.load(open(root + "/reports/resident_bindings.json", encoding="utf-8"))
budget = bindings.get("ycharts_window_budget")
window_budget = (budget["calls"], budget["window_s"]) if isinstance(budget, dict) else None
print("YCP bindings: tiers=%s budget=%s" % (json.dumps((bindings.get("opal_pricing") or {}).get("tiers")), json.dumps(budget)))
import boto3  # noqa: E402  (the service's own environment)
import price_adapter_ycharts  # noqa: E402
import price_transport_ycharts  # noqa: E402
from resident_session import ResidentSession  # noqa: E402

PATH = "/charts/fund_data.json"


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
                out["first_point"] = [type(raw[0][0]).__name__, raw[0][0], type(raw[0][1]).__name__]
                out["last_point"] = [raw[-1][0], raw[-1][1]]
        except (KeyError, IndexError, TypeError) as exc:
            out["shape_error"] = type(exc).__name__
    return out


session = ResidentSession(secrets_client=boto3.client("secretsmanager", region_name=bindings["region"]),
                          dynamo_client=boto3.client("dynamodb", region_name=bindings["region"]), jobs_table=bindings["jobs_table"],
                          enrolled_user_id=bindings["enrolled_user_id"], clock=time.time, window_budget=window_budget)
result = {"id_form": "UNREAD", "shape": "UNREAD", "signed_out": "UNREAD"}
calls = (("session", "SPY"), ("session", "AAPL"), ("sessionless", "SPY"))
for n, (mode, symbol) in enumerate(calls, start=1):
    if n > 1:
        time.sleep(3)
    params = {"securities": "id:" + symbol + ",include:true,", "zoom": "max"}
    started = time.time()
    try:
        if mode == "session":
            answer = price_transport_ycharts.make_transport(session)(PATH, params)
            info = {"status": 200}
        else:
            import urllib.parse
            facade = session.acquire_sessionless()
            try:
                info, body = facade.request(PATH + "?" + urllib.parse.urlencode(params, safe=":,"))
            finally:
                facade.close()
            answer = json.loads(body) if info.get("status") == 200 else None
    except BaseException as exc:  # a probe prints whatever is raised
        print("YCP CALL %d mode=%s symbol=%s verdict=EXCEPTION module=%s name=%s message=%r" % (n, mode, symbol, type(exc).__module__, type(exc).__name__, clean(exc)[:200]), flush=True)
        key = "id_form" if mode == "session" else "signed_out"
        result[key] = "ERROR:" + type(exc).__name__
        continue
    shape = summarise(answer) if answer is not None else {"status": info.get("status"), "waf_action": info.get("waf_action"), "content_type": info.get("content_type")}
    print("YCP CALL %d mode=%s symbol=%s t=%s elapsed=%.2f status=%s shape=%s" % (n, mode, symbol, time.strftime("%H:%M:%SZ", time.gmtime()), time.time() - started, info.get("status"), json.dumps(shape, sort_keys=True)), flush=True)
    rows = None
    if answer is not None:
        rows = price_adapter_ycharts.make_reader(lambda path, p, answer=answer: answer)(symbol, "1990-01-01", "2100-01-01")
        print("YCP CALL %d adapter rows=%d first=%s last=%s" % (n, len(rows), rows[0] if rows else None, rows[-1] if rows else None), flush=True)
    if mode == "session":
        if rows:
            result["id_form"] = "OK" if result["id_form"] in ("UNREAD", "OK") else result["id_form"]
            result["shape"] = "ADAPTER_PARSES" if result["shape"] in ("UNREAD", "ADAPTER_PARSES") else result["shape"]
        else:
            result["id_form"] = "EMPTY_FOR_" + symbol
            result["shape"] = "NOT_PARSED"
    else:
        result["signed_out"] = "ANSWERS" if rows else ("REFUSED:%s" % info.get("status"))
print("YCP RESULT id_form=%s shape=%s signed_out=%s" % (result["id_form"], result["shape"], result["signed_out"]))
PYEOF
chmod 644 "$PYF"
echo "YCP script sha256: $(sha256sum "$PYF" | cut -d' ' -f1)"
systemd-run --quiet --wait --pipe --collect --uid="$USR" -p WorkingDirectory="$WD" $SETENV "$PY" "$PYF"
RC=$?
echo "YCP transient unit rc=$RC"
rm -f "$PYF"
exit $RC
