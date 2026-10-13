"""IRPT_DASHBD round 90, TO-DB-b-168 (issuer 2.0.0_SA_COO~D2): the day-grain read of the 7 UNEXPLAINED segments.

Usage: python -I tieout_day_read.py <repo_root> <mode> [--go]
  plan      OFFLINE. DRY_RUN is set to 1 before the estate client is imported. Reproduces round 89's selection of the
            UNEXPLAINED segments: tieout_neither_reasons.py is imported by path and NOT edited; its population and its
            classification are re-run here by the same rules, and the reproduced counts are asserted against that
            round's committed record. Each account is mapped to its Black Diamond internal id by the tier-1 rule of
            bd_population_pull_e3.py (imported by path; S3 GET/LIST of the cross-reference prefix only). ONE
            performanceSeries body is built per account for that account's segment window. The plan is written to the
            PRIVATE folder; only counts are printed.
  pull --go LIVE. The issuer's act; the worker never runs it. Refuses without --go, without the written plan, when a
            pull record already exists (no second pull), and when the plan rebuilt from scratch differs from the written
            plan. Then lifts DRY_RUN, mints one session through the estate's helpers, sends each account's request
            exactly once at one request per second, retries one transient failure, and aborts on the first
            non-transient error. Raw responses and the pull record are written ONLY under the private folder's pull/
            subfolder. Prints counts only. Never prints or writes a credential, cookie, bearer or response body.
  analyze   OFFLINE. Reads the private pull/ responses and the stored tables (worker 108's private folder, read only)
            and builds the daily table PRIVATELY: for each date, the served daily return against Black Diamond's daily
            return (the ratio of consecutive cumulatives), the difference in pp, and whether it exceeds DAY_DIFFERS_PP.
            Prints counts only. The reason for a differing day is not assigned here.
  selftest  OFFLINE. Synthetic fixtures only: no network, no session, no private table. Proves (a) the series body
            parity with the estate's bd_selected.requests_for on one synthetic Cottonwood-shaped mapping, used only
            inside this test, and (b) the day comparison and the window tolerance on a synthetic window with a named
            cause, its correction, and a negative arm. Prints SELFTEST PASS only when every check holds.

SERIES BODY. The estate has exactly one definition of the performanceSeries body: inline in bd_selected.requests_for,
behind a Cottonwood-only guard. series_body() below re-derives it for 49F from bd_adapter.build_period_request by the
same transformation (the series dict of requests_for). That is a re-derivation guarded by the selftest parity test.
requests_for is never called for production and no Cottonwood mapping is handed to it.
"""
import collections
import copy
import hashlib
import importlib
import importlib.util
import json
import os
import pickle
import sys
import time
import urllib.error
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parents[5]
PERF = "infra/aws/lambda/investor-reporting/performance"
PRIV = "C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~134/"
STORED = "C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~108/"
ROUND89_COPY = "C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~133/copy/"
ROUND89_RECORD = "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~133/NEITHER_12_REASONS.json"
XREF_MODULE = "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~6/bd_population_pull_e3.py"
PLAN_NAME = "DAY_READ_PLAN.json"
PULL_DIR = "pull/"
PULL_NAME = "DAY_PULL_RECORD.json"
DAY_TABLE_NAME = "DAY_TABLE_7.json"
TOL_PP = 0.35
DAY_DIFFERS_PP = 0.01
EXPECT_SEGMENTS, EXPECT_ACCOUNTS, EXPECT_NOFLOW, EXPECT_FLOW = 12, 7, None, 88
TRANSIENT_HTTP = (429, 502, 503, 504)
MODES = ("plan", "pull", "analyze", "selftest")


def die(msg):
    print("ERROR: " + msg)
    sys.exit(2)


def import_by_path(path, name):
    spec = importlib.util.spec_from_file_location(name, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def canon(obj):
    return json.dumps(obj, sort_keys=True, separators=(",", ":")).encode("ascii")


def sha256_bytes(raw):
    return hashlib.sha256(raw).hexdigest()


def sha256_file(path):
    with open(path, "rb") as fh:
        return hashlib.sha256(fh.read()).hexdigest()


def read_json(path):
    with open(path, "rb") as fh:
        return json.loads(fh.read().decode("utf-8"))


def estate_setup(root):
    """Put the estate's performance package on sys.path and import the adapter (DRY_RUN already set by main)."""
    perf = str(Path(root) / PERF)
    if perf not in sys.path:
        sys.path.insert(0, perf)
    return importlib.import_module("bd_adapter")


def series_body(bd_adapter, vendor_id, start, end):
    """The 49F performanceSeries body for one account and one window: a re-derivation of bd_selected.requests_for's
    series dict, from the period body that bd_adapter.build_period_request builds (guarded by selftest parity)."""
    period, _index = bd_adapter.build_period_request(vendor_id, start, end, start, int(end[:4]))
    options = period["parameters"]["dataPointOptions"]
    return {
        "perfFrequency": 0,
        "parameters": {
            "advancedFilters": [],
            "accountFilters": {"accounts": [vendor_id]},
            "perfFrequency": 0,
            "groupings": ["Account"],
            "dateRange": {"startDate": start, "endDate": end, "excludeHistoryRanges": False},
            "dataPointOptions": {k: v for k, v in options.items() if k not in ("asOfDatePoints", "dateRangePoints")},
            "schemaFilters": {"useSectorScheme": False},
            "supervisedState": "Any",
            "benchmarks": {"includeBenchmarkTypes": [], "specificTopLevelBenchmarks": []},
        },
        "benchmarkLevelDisplay": copy.deepcopy(period["benchmarkLevelDisplay"]),
    }


def cumulative(daily):
    out, p = [], 1.0
    for r in daily:
        p *= 1.0 + r
        out.append(p - 1.0)
    return out


def daily_from_cumulative(cums):
    """Daily return of each point from consecutive cumulatives; the first point is measured from the window start."""
    out, prev = [], 0.0
    for c in cums:
        out.append((1.0 + c) / (1.0 + prev) - 1.0)
        prev = c
    return out


def window_return(daily):
    p = 1.0
    for r in daily:
        p *= 1.0 + r
    return p - 1.0


def window_misses(served, bd):
    """True when the window built from the served daily returns is outside TOL_PP of Black Diamond's window."""
    return abs(window_return(bd) - window_return(served)) * 100.0 > TOL_PP


def compare_days(served, bd):
    rows = []
    for i, (s, b) in enumerate(zip(served, bd)):
        diff_pp = (b - s) * 100.0
        rows.append({"i": i, "served": s, "bd": b, "diff_pp": diff_pp, "differs": abs(diff_pp) > DAY_DIFFERS_PP})
    return rows


def series_points(body):
    """Read a performanceSeries body as parse_series does (perfDates or dates; levels[0] cumulatives). A length
    mismatch is refused, never zipped."""
    levels = body.get("levels") or []
    if not levels:
        die("the series response carries no levels")
    dates = [str(d)[:10] for d in (body.get("perfDates") or body.get("dates") or [])]
    cums = ((levels[0].get("seriesPoints") or {}).get("timeWeightedReturns") or {}).get("cumulatives") or []
    if len(dates) != len(cums) or not dates:
        die("series dates and cumulatives are not aligned; refusing to zip them")
    return dates, [float(c) for c in cums]


def http_status_of(err):
    msg = str(err)
    if " -> HTTP " in msg:
        try:
            return int(msg.split(" -> HTTP ", 1)[1].split(":", 1)[0])
        except ValueError:
            return -1
    return -1


# ---- plan: round 89's selection, re-run by the same rules -----------------------------------------------------

def reproduce_selection(nr):
    """Round 89's population and classification (tieout_neither_reasons.main), re-run here without editing it."""
    read = nr.prev.load("read90.pkl")
    rows = nr.prev.load("table90.pkl")
    gold, txn = read["gold"], read["txn"]
    txn_by = collections.defaultdict(list)
    for t in txn:
        txn_by[str(t["account_number"]).strip().lstrip("0")].append(t)

    def bd_days(acct):
        fl, inc = collections.defaultdict(float), collections.defaultdict(float)
        for t in txn_by[str(acct).strip().lstrip("0")]:
            rd = t.get("return_date")
            if not rd:
                continue
            d = str(rd)[:10]
            if t.get("external_flow") in ("Contribution", "Withdrawal"):
                fl[d] += nr.fnum(t.get("market_value"))
            inc[d] += nr.fnum(t.get("income"))
        return dict(fl), dict(inc)

    flow_n, neither = 0, []
    for r in rows:
        acct, seg, o, b, v = r["a"], r["seg"], r["o"], r["b"], r["v2"]
        series = gold[acct]
        window = [d for d in sorted(series) if seg["start"] <= d <= seg["end"]]
        if not any(series[d]["flow"] for d in window):
            continue
        if v.get("bdr") is None or b.get("fees") is None or o.get("mean") is None:
            continue
        w0 = nr.make_w(series, window)
        before = [d for d in series if d < seg["start"]]
        prior_mv = series[max(before)].get("mv") if before else None
        base = o["mean"]
        add = b["fees"] / base if base > 0 else 0.0
        gross = (1.0 + v["bdr"]) * (1.0 + add) - 1.0
        days = [series[d] for d in window if series[d]["r"] is not None]
        c_bd = nr.closes(gross, nr.prev.relink(days, "bd_default", prior_mv))
        c_end = nr.closes(gross, nr.prev.relink(days, "end", prior_mv))
        flow_n += 1
        if not (c_bd or c_end):
            bdf, bdi = bd_days(acct)
            neither.append({"acct": acct, "seg": seg, "o": o, "b": b, "v": v, "w0": w0, "prior_mv": prior_mv,
                            "gross": gross, "bdf": bdf, "bdi": bdi})
    return flow_n, neither


def classify(nr, s):
    """The reason round 89 assigns: the first of tests 1..5 whose correction alone closes the segment, else UNEXPLAINED."""
    o, b, w0, prior_mv, gross = s["o"], s["b"], s["w0"], s["prior_mv"], s["gross"]
    bdf, bdi = s["bdf"], s["bdi"]
    t1 = nr.test_missing(w0)
    t2 = nr.test_flow_absent(w0, bdf)
    t3 = nr.test_non_trading(w0)
    t4 = nr.income_pairs(w0, bdi)
    t5 = nr.accrual_identity(o, b)
    hold = {1: len(t1) > 0, 2: len(t2) > 0, 3: len(t3) > 0, 4: len(t4) > 0, 5: t5}

    def apply_series(k, w_list):
        if k == 1:
            return nr.corr_missing(w_list, prior_mv)
        if k == 2:
            return nr.corr_flow_absent(w_list, bdf)
        if k == 3:
            return nr.corr_non_trading(w_list)
        return nr.corr_income(w_list, t4)

    def single_closes(k):
        if not hold[k]:
            return False
        if k == 5:
            ar = nr.accrual_r(nr.r_of(w0, prior_mv), o, b)
            return ar is not None and nr.closes(gross, ar)
        wk = apply_series(k, w0)
        return wk is not None and nr.closes(gross, nr.r_of(wk, prior_mv))

    for k in (1, 2, 3, 4, 5):
        if single_closes(k):
            return nr.NAMES[k - 1]
    return nr.NAMES[5]


def plan_unexplained(root, nr):
    flow_n, neither = reproduce_selection(nr)
    if flow_n != EXPECT_FLOW or len(neither) != EXPECT_SEGMENTS:
        die("the round-89 population does not reproduce (flow %d, neither %d)" % (flow_n, len(neither)))
    classed = [(s, classify(nr, s)) for s in neither]
    got = {n: sum(1 for _, reason in classed if reason == n) for n in nr.NAMES}
    with open(str(Path(root) / ROUND89_RECORD), "rb") as fh:
        expected = json.loads(fh.read().decode("utf-8"))["by_reason"]
    if got != expected:
        die("the reproduced reasons differ from round 89's committed record")
    unexpl = [s for s, reason in classed if reason == nr.NAMES[5]]
    if len(unexpl) != EXPECT_ACCOUNTS or len({s["acct"] for s in unexpl}) != EXPECT_ACCOUNTS:
        die("expected %d UNEXPLAINED segments in %d accounts, got %d segments" % (EXPECT_ACCOUNTS, EXPECT_ACCOUNTS, len(unexpl)))
    return flow_n, got, unexpl


def build_plan(root, bd_adapter):
    nr = import_by_path(HERE / "tieout_neither_reasons.py", "tieout_neither_reasons")
    flow_n, got, unexpl = plan_unexplained(root, nr)
    bpe = import_by_path(Path(root) / XREF_MODULE, "bd_population_pull_e3")
    try:
        xref, xref_key = bpe.load_xref()
    except Exception as e:  # class name only: a message can carry a bucket or key path
        die("the cross-reference read failed (%s); the plan is not completed" % type(e).__name__)
    requests = []
    for i, s in enumerate(unexpl):
        bd, _why = bpe.map_account(s["acct"], xref)
        if bd is None:
            die("UNEXPLAINED segment %d of %d is not mapped by the tier-1 rule; never guessed" % (i + 1, len(unexpl)))
        seg = s["seg"]
        requests.append({"index": i, "account": s["acct"], "bd_account_id": bd, "start": seg["start"], "end": seg["end"],
                         "stored_window_return": s["v"]["bdr"],
                         "body": series_body(bd_adapter, bd, seg["start"], seg["end"])})
    if len({r["bd_account_id"] for r in requests}) != len(requests):
        die("two UNEXPLAINED accounts map to one Black Diamond id; refusing to guess")
    copy_eq = (sha256_file(ROUND89_COPY + "read90.pkl") == sha256_file(STORED + "read90.pkl")
               and sha256_file(ROUND89_COPY + "table90.pkl") == sha256_file(STORED + "table90.pkl"))
    return {"tolerance_pp": TOL_PP, "dry_run": 1, "vendor_calls": 0, "xref_partition": xref_key,
            "round89_copy_equals_stored": copy_eq, "reproduced_by_reason": got, "flow_segments": flow_n,
            "requests": requests, "plan_sha256": sha256_bytes(canon([r["body"] for r in requests]))}


def run_plan(root, bd_adapter):
    plan = build_plan(root, bd_adapter)
    os.makedirs(PRIV, exist_ok=True)
    with open(PRIV + PLAN_NAME, "wb") as fh:
        fh.write((json.dumps(plan, indent=1, sort_keys=True) + "\n").encode("ascii"))
    n = len(plan["requests"])
    print("requests %d daily_ranges %d vendor_calls %d dry_run %d" % (n, n, plan["vendor_calls"], plan["dry_run"]))
    print("unexplained segments %d in accounts %d; reproduced reasons match round 89 record; round-89 copy equals stored: %s"
          % (n, len({r["account"] for r in plan["requests"]}), str(plan["round89_copy_equals_stored"]).lower()))
    print("plan_sha256 %s" % plan["plan_sha256"])
    print("OK: plan written to the private folder; counts only")


# ---- pull: the issuer's live act, never run by the worker -----------------------------------------------------

def last_equals_stored(body, stored):
    try:
        last = body["levels"][0]["seriesPoints"]["timeWeightedReturns"]["cumulatives"][-1]
    except (KeyError, IndexError, TypeError):
        return False
    return isinstance(last, (int, float)) and abs(float(last) - float(stored)) <= 1e-9


def run_pull(root, argv, bd_adapter):
    if "--go" not in argv:
        die("pull is LIVE and needs --go; without --go this mode refuses and makes no call")
    plan_path = PRIV + PLAN_NAME
    if not os.path.isfile(plan_path):
        die("no written plan; run plan first")
    pdir = PRIV + PULL_DIR
    rec_path = pdir + PULL_NAME
    if os.path.exists(rec_path):
        die("a pull record already exists; no second pull")
    written = read_json(plan_path)
    rebuilt = build_plan(root, bd_adapter)
    if canon(rebuilt) != canon(written):
        die("the plan rebuilt from scratch differs from the written plan; refusing to call")
    os.makedirs(pdir, exist_ok=True)
    with open(rec_path, "xb") as fh:  # exclusive create: the marker itself blocks a second pull
        fh.write((json.dumps({"status": "STARTED", "plan_sha256": written["plan_sha256"]}) + "\n").encode("ascii"))
    os.environ["DRY_RUN"] = "0"
    h = bd_adapter.load_bd_helpers(force=True)
    if h.DRY_RUN:
        die("the estate helper is still DRY; refusing")
    tenants = importlib.import_module("tenants")
    path = tenants.verification_route_for(tenants._LEGACY_SHORT_ID["49F"]).paths["performanceSeries"]
    try:
        cookie = h.load_bd_session()
        token = h.get_clientview_token(cookie)
        del cookie
    except Exception as e:  # class name only
        record = {"status": "ABORTED", "aborted_on": "session: %s" % type(e).__name__, "plan_sha256": written["plan_sha256"],
                  "requests": len(written["requests"]), "http_ok": 0, "http_failed": len(written["requests"]),
                  "session_token_mints": 0, "per_request": []}
        with open(rec_path, "wb") as fh:
            fh.write((json.dumps(record, indent=1, sort_keys=True) + "\n").encode("ascii"))
        die("the session could not be minted (%s); no request was sent" % type(e).__name__)
    interval = 1.0
    retries_left = 1
    http_ok, aborted, last_start, per = 0, None, None, []
    for r in written["requests"]:
        if last_start is not None:
            wait = last_start + interval - time.monotonic()
            if wait > 0:
                time.sleep(wait)
        rec = {"index": r["index"], "http_status": None, "last_equals_stored": None, "retried": False}
        while True:
            last_start = time.monotonic()
            try:
                payload = h._request("POST", path, token=token, body=r["body"], raw=True)
            except RuntimeError as e:
                status = http_status_of(e)
                rec["http_status"] = status
            except (urllib.error.URLError, OSError, TimeoutError):
                status = 0
                rec["http_status"] = 0
            else:
                rec["http_status"] = 200
                try:
                    body = json.loads(payload.decode("utf-8"))
                except ValueError:
                    aborted = "response not JSON (index %d)" % r["index"]
                    break
                with open(pdir + "series_%02d.json" % r["index"], "wb") as fh:
                    fh.write(payload)
                rec["last_equals_stored"] = last_equals_stored(body, r["stored_window_return"])
                http_ok += 1
                break
            if (status in TRANSIENT_HTTP or status == 0) and retries_left > 0:
                retries_left -= 1
                rec["retried"] = True
                time.sleep(interval)
                continue
            aborted = "HTTP %d (index %d)" % (status, r["index"])
            break
        per.append(rec)
        if aborted:
            break
    n = len(written["requests"])
    for i in range(len(per), n):
        per.append({"index": written["requests"][i]["index"], "http_status": None, "last_equals_stored": None,
                    "retried": False, "not_sent": True})
    record = {"status": "ABORTED" if aborted else "COMPLETE", "aborted_on": aborted,
              "plan_sha256": written["plan_sha256"], "requests": n, "http_ok": http_ok, "http_failed": n - http_ok,
              "retries_used": 1 - retries_left, "session_token_mints": 1, "per_request": per}
    with open(rec_path, "wb") as fh:
        fh.write((json.dumps(record, indent=1, sort_keys=True) + "\n").encode("ascii"))
    print("requests %d http_ok %d http_failed %d retries_used %d status %s"
          % (n, http_ok, n - http_ok, 1 - retries_left, record["status"]))
    print("last_equals_stored in plan order: %s" % [x["last_equals_stored"] for x in per])
    return 1 if aborted else 0


# ---- analyze: offline, private daily table -------------------------------------------------------------------

def run_analyze(root, bd_adapter):
    plan_path = PRIV + PLAN_NAME
    rec_path = PRIV + PULL_DIR + PULL_NAME
    if not os.path.isfile(plan_path):
        die("no written plan; run plan first")
    if not os.path.isfile(rec_path):
        die("no pull record: the issuer's live pull has not run; nothing to analyze")
    rec = read_json(rec_path)
    if rec.get("status") not in ("COMPLETE", "ABORTED"):
        die("the pull record is not a finished pull")
    plan = read_json(plan_path)
    with open(STORED + "read90.pkl", "rb") as fh:
        gold = pickle.load(fh)["gold"]
    table, tot_days, tot_diff = [], 0, 0
    for r in plan["requests"]:
        raw_path = PRIV + PULL_DIR + "series_%02d.json" % r["index"]
        if not os.path.isfile(raw_path):
            table.append({"index": r["index"], "days_compared": 0, "days_differing": 0, "not_answered": True, "rows": []})
            continue
        dates, cums = series_points(read_json(raw_path))
        bd_daily = daily_from_cumulative(cums)
        series = gold[r["account"]]
        rows, absent = [], 0
        for d, b in zip(dates, bd_daily):
            s = (series.get(d) or {}).get("r")
            if s is None:
                absent += 1
                continue
            cmp = compare_days([s], [b])[0]
            rows.append({"date": d, "served": s, "bd": b, "diff_pp": cmp["diff_pp"], "differs": cmp["differs"]})
        differing = sum(1 for x in rows if x["differs"])
        table.append({"index": r["index"], "days_compared": len(rows), "days_differing": differing,
                      "served_absent": absent, "not_answered": False, "rows": rows})
        tot_days += len(rows)
        tot_diff += differing
    os.makedirs(PRIV, exist_ok=True)
    with open(PRIV + DAY_TABLE_NAME, "wb") as fh:
        fh.write((json.dumps({"day_differs_pp": DAY_DIFFERS_PP, "requests": table}, indent=1, sort_keys=True) + "\n").encode("ascii"))
    for t in table:
        print("request %d: days_compared %d days_differing %d served_absent %s"
              % (t["index"] + 1, t["days_compared"], t["days_differing"], t.get("served_absent", "n/a")))
    print("total days_compared %d days_differing %d; private daily table written" % (tot_days, tot_diff))
    return 0


# ---- selftest: synthetic only ----------------------------------------------------------------------------------

def run_selftest(root, bd_adapter):
    fails = []
    tenants = importlib.import_module("tenants")
    bds = importlib.import_module("bd_selected")
    canonical = "acc_" + "a" * 24
    mapping = {"firm_id": tenants._CANONICAL_COT, "canonical_account_id": canonical, "vendor_account_id": 424242,
               "vendor_external_id": "SYNTHETIC-EXTERNAL", "currency": "USD", "source_revision": "synthetic-fixture"}
    start, end = "2026-01-02", "2026-03-31"
    estate = bds.requests_for(mapping, canonical, start, end)["performanceSeries"]
    mine = series_body(bd_adapter, 424242, start, end)
    parity = canon(estate) == canon(mine)
    if not parity:
        fails.append("series body parity with bd_selected.requests_for")
    mutated = copy.deepcopy(mine)
    mutated["parameters"]["groupings"] = ["Security"]
    if canon(estate) == canon(mutated):
        fails.append("negative control: the parity comparison must see a changed grouping")

    bd_daily = [0.0010, 0.0020, -0.0010, 0.0000, 0.0030, 0.0010, 0.0005]
    served = [0.0010, 0.0020, 0.0000, 0.0000, -0.0020, 0.0010, 0.0005]
    recon = daily_from_cumulative(cumulative(bd_daily))
    recon_ok = max(abs(a - b) for a, b in zip(recon, bd_daily)) <= 1e-12
    if not recon_ok:
        fails.append("the daily return rebuilt from cumulatives")
    differing = [x["i"] for x in compare_days(served, recon) if x["differs"]]
    if differing != [2, 4]:
        fails.append("the differing days are %r, expected [2, 4]" % differing)
    uncorrected_misses = window_misses(served, recon)
    if not uncorrected_misses:
        fails.append("the uncorrected window must miss the tolerance")
    named = list(served)
    named[4] = recon[4]  # the named cause (synthetic: day 4) corrected alone
    corrected_closes = not window_misses(named, recon)
    if not corrected_closes:
        fails.append("the window must re-close after the named cause is corrected")
    neg_open = window_misses(list(served), recon) and window_misses(
        [served[0], served[1], recon[2], served[3], served[4], served[5], served[6]], recon)
    if not neg_open:
        fails.append("negative arm: a correction that is not the cause must leave the window open")

    print("parity %s; daily differing %s; uncorrected misses %s; named correction closes %s; negative arm open %s"
          % (str(parity).lower(), differing, str(uncorrected_misses).lower(), str(corrected_closes).lower(),
             str(neg_open).lower()))
    if fails:
        for f in fails:
            print("FAIL: " + f)
        print("SELFTEST FAIL")
        return 1
    print("SELFTEST PASS")
    return 0


def main(argv):
    if len(argv) < 3 or argv[2] not in MODES:
        die("usage: python -I tieout_day_read.py <repo_root> plan|pull|analyze|selftest [--go]")
    root = Path(argv[1]).resolve()
    mode = argv[2]
    os.environ["DRY_RUN"] = "1"
    bd_adapter = estate_setup(root)
    if mode == "plan":
        run_plan(root, bd_adapter)
        return 0
    if mode == "pull":
        return run_pull(root, argv, bd_adapter)
    if mode == "analyze":
        return run_analyze(root, bd_adapter)
    return run_selftest(root, bd_adapter)


if __name__ == "__main__":
    sys.exit(main(sys.argv))
