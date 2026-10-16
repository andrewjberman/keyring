set -u
# IRPT_ANLREQ TO-READ-YCHARTS-RECIPEFORM (issuer 2.0.0_SA_COO~G2, round 52): the follow-up to ycharts_price_probe.sh, which measured that GET /charts/fund_data.json?securities=id:<TICKER>,include:true,&zoom=max
# answers a plain ticker (SPY, AAPL) with HTTP 400 text/plain, signed in and signed out (r34h, 22:58Z). CTO msg 9991 ruled: find the form the working recipe path already uses. The CRO's captured map
# (org/missions/D9/IRPT/IRPT_YCDGEN/deliverables/maps/overview_map.json, call benchmark_level_series) is a working one-security series call: securities=id:^SPXTR,include:true,, with calcs=id:level,include:true,,
# zoom=max, maxPoints=100000, partner=basic_2000. This read asks the three unknowns again with THAT form, a plain ticker first and a typed lookup id only if the plain one is refused:
#   A1  signed-in session, id:SPY in the recipe form. If it answers rows the existing price_adapter_ycharts reader parses: A2 signed-in id:AAPL, then A3 SIGNED-OUT id:SPY (the session unknown).
#   B   only if A1 is refused or empty: B1 a sessionless lookup of SPY for its typed id (security_id), B2 signed-in recipe form with the typed id, B3 (if B2 answers) signed-out recipe form with the typed id.
# FOUR outbound requests at most, 3 s apart, every one through the provider lease under the root's window budget (6 calls, 390 s), made in a transient unit with the resident service's own user, environment and
# interpreter, from the running root's own code. Run it only 390 s or more after the last YCharts call from this host. READ ONLY: nothing is written on the host but a temp file. Market data only (SPY, AAPL):
# no client data; no cookie, token or secret is printed; a body is summarised, never printed.
# Written for IRPT_ANLREQ round 52. NOT RUN: a CloudOps applier runs it, as root (systemd-run needs it), only while no upload or run uses the door.
U=irpt-analysis-resident.service
echo "YCP2 unit: $(systemctl is-active $U) MainPID=$(systemctl show -p MainPID --value $U) ActiveEnter=$(systemctl show -p ActiveEnterTimestamp --value $U)"
USR=$(systemctl show -p User --value $U)
WD=$(systemctl show -p WorkingDirectory --value $U)
ENVS=$(systemctl show -p Environment --value $U)
PY=$(systemctl show -p ExecStart --value $U | grep -o 'argv\[\]=[^ ]*' | head -1 | cut -d= -f2)
echo "YCP2 user=$USR workdir=$WD interpreter=$PY"
if [ -z "$USR" ] || [ -z "$WD" ] || [ -z "$PY" ]; then echo "YCP2 FAIL a unit property is empty (user, workdir or interpreter)"; exit 61; fi
BUSY=$(journalctl -u $U --utc --since '-60 s' --no-pager 2>/dev/null | grep -c 'IRPT_RESIDENT_POLL handled=[1-9]')
echo "YCP2 resident messages handled in the last 60 s: $BUSY"
if [ "$BUSY" != "0" ]; then echo "YCP2 FAIL the resident is busy; no call made"; exit 70; fi
SETENV=""
for e in $ENVS; do SETENV="$SETENV --setenv=$e"; done
PYF=${YCP2_PYFILE:-/tmp/ycharts_price_probe2.py}
cat > "$PYF" <<'PYEOF'
import json
import os
import re
import sys
import time

root = os.getcwd()
for sub in ("reports", "ycharts/generate", "ycharts/session", "ycharts/extract", "ycharts/research", "_scope", "_ids", "_keys", "_authz", "intake", "ops", "lib"):
    sys.path.insert(0, root + "/" + sub)
print("YCP2 process: uid=%s cwd=%s" % (getattr(os, "getuid", lambda: -1)(), root))
bindings = json.load(open(root + "/reports/resident_bindings.json", encoding="utf-8"))
budget = bindings.get("ycharts_window_budget")
window_budget = (budget["calls"], budget["window_s"]) if isinstance(budget, dict) else None
print("YCP2 bindings: tiers=%s budget=%s" % (json.dumps((bindings.get("opal_pricing") or {}).get("tiers")), json.dumps(budget)))
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


session = ResidentSession(secrets_client=boto3.client("secretsmanager", region_name=bindings["region"]),
                          dynamo_client=boto3.client("dynamodb", region_name=bindings["region"]), jobs_table=bindings["jobs_table"],
                          enrolled_user_id=bindings["enrolled_user_id"], clock=time.time, window_budget=window_budget)
state = {"calls": 0}
result = {"plain": "UNREAD", "typed": "SKIP", "shape": "UNREAD", "second_symbol": "SKIP", "signed_out": "SKIP", "form": "NONE"}


def recipe_params(ident):
    """The CRO's captured benchmark_level_series form with `ident` in place of ^SPXTR; no date window."""
    return {"securities": "id:" + ident + ",include:true,,", "calcs": "id:level,include:true,,", "zoom": "max", "maxPoints": "100000", "partner": "basic_2000"}


def call(mode, what, request):
    """One call. Returns (answer or None, status text). Prints the call line; never a body."""
    if state["calls"]:
        time.sleep(3)
    state["calls"] += 1
    n, started = state["calls"], time.time()
    try:
        answer, status = request()
    except BaseException as exc:  # a probe prints whatever is raised
        print("YCP2 CALL %d mode=%s what=%s verdict=EXCEPTION module=%s name=%s message=%r" % (n, mode, what, type(exc).__module__, type(exc).__name__, clean(exc)[:200]), flush=True)
        return None, "%s:%s" % (type(exc).__name__, clean(exc)[:60])
    shape = summarise(answer) if answer is not None else {"status": status}
    print("YCP2 CALL %d mode=%s what=%s t=%s elapsed=%.2f status=%s shape=%s" % (n, mode, what, time.strftime("%H:%M:%SZ", time.gmtime()), time.time() - started, status, json.dumps(shape, sort_keys=True)), flush=True)
    return answer, status


def session_fund(ident):
    return lambda: (price_transport_ycharts.make_transport(session)(FUND, recipe_params(ident)), 200)


def sessionless_get(path):
    facade = session.acquire_sessionless()
    try:
        return facade.request(path)
    finally:
        facade.close()


def sessionless_fund(ident):
    import urllib.parse

    def request():
        info, body = sessionless_get(FUND + "?" + urllib.parse.urlencode(recipe_params(ident), safe=":,"))
        return (json.loads(body) if info.get("status") == 200 else None), info.get("status")
    return request


def rows_of(answer, symbol):
    if answer is None:
        return []
    rows = price_adapter_ycharts.make_reader(lambda path, p, answer=answer: answer)(symbol, "1990-01-01", "2100-01-01")
    print("YCP2 adapter symbol=%s rows=%d first=%s last=%s" % (symbol, len(rows), rows[0] if rows else None, rows[-1] if rows else None), flush=True)
    return rows


answer, status = call("session", "fund_data:SPY:plain", session_fund("SPY"))
rows = rows_of(answer, "SPY")
if rows:
    result.update(plain="OK", shape="ADAPTER_PARSES", form="RECIPE_PLAIN")
    answer, status = call("session", "fund_data:AAPL:plain", session_fund("AAPL"))
    result["second_symbol"] = "OK" if rows_of(answer, "AAPL") else "FAIL:%s" % (status,)
    answer, status = call("sessionless", "fund_data:SPY:plain", sessionless_fund("SPY"))
    result["signed_out"] = "ANSWERS" if rows_of(answer, "SPY") else "REFUSED:%s" % (status,)
else:
    result["plain"] = "REFUSED:%s" % (status,) if answer is None else "EMPTY"
    info_rows, status = call("sessionless", "lookup:SPY", lambda: (lambda r: (json.loads(r[1]) if r[0].get("status") == 200 else None, r[0].get("status")))(sessionless_get(LOOKUP + "SPY")))
    row = info_rows[0] if isinstance(info_rows, list) and info_rows and isinstance(info_rows[0], dict) else None
    print("YCP2 LOOKUP SPY row_keys=%s id_fields=%s" % (json.dumps(sorted(row)[:20]) if row else "[]", json.dumps({k: row.get(k) for k in ID_KEYS if k in row}, sort_keys=True) if row else "{}"), flush=True)
    sid = (row or {}).get("security_id") or (row or {}).get("id")
    if isinstance(sid, str) and sid:
        answer, status = call("session", "fund_data:SPY:typed", session_fund(sid))
        if rows_of(answer, "SPY"):
            result.update(typed="OK", shape="ADAPTER_PARSES", form="RECIPE_TYPED")
            answer, status = call("sessionless", "fund_data:SPY:typed", sessionless_fund(sid))
            result["signed_out"] = "ANSWERS" if rows_of(answer, "SPY") else "REFUSED:%s" % (status,)
        else:
            result["typed"] = "REFUSED:%s" % (status,) if answer is None else "EMPTY"
    else:
        result["typed"] = "NO_TYPED_ID"
print("YCP2 RESULT form=%s plain=%s typed=%s shape=%s second_symbol=%s signed_out=%s calls=%d" % (result["form"], result["plain"], result["typed"], result["shape"], result["second_symbol"], result["signed_out"], state["calls"]))
PYEOF
chmod 644 "$PYF"
echo "YCP2 script sha256: $(sha256sum "$PYF" | cut -d' ' -f1)"
systemd-run --quiet --wait --pipe --collect --uid="$USR" -p WorkingDirectory="$WD" $SETENV "$PY" "$PYF"
RC=$?
echo "YCP2 transient unit rc=$RC"
rm -f "$PYF"
exit $RC
