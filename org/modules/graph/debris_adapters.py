"""debris_adapters -- comp-debris per-type activity adapters PAST Lambda (S3/DDB/EC2/EventBridge).

A SUBMODULE of comp-debris (NFRA_DECOMTOOL, CTO ruling-20 = extend IN-PLACE, not a separate tool).
comp_debris.py's --types path imports this; the band logic + the three binding refinements stay in
comp_debris (classify / BANDS / _HELD_RX) and are reused VERBATIM -- ONE classify(), N adapters. Each
adapter contributes ONLY its signal (last_activity_day, created_day, read_ok, signal_basis); the
central classify() assigns the band. Adding a type = adding an adapter, never touching the invariants.

SIGNALS (grounded live 2026-07-17; COMP_DEBRIS_EXTENSION_DESIGN_20260717.md):
  LAMBDA         : CW AWS/Lambda Invocations (the v1 signal -- included so --types is one ledger)
  DYNAMODB_TABLE : CW ConsumedRead+WriteCapacityUnits (Sum, daily)      -- mirrors Lambda
  S3_BUCKET      : CW NumberOfObjects delta (AllStorageTypes, daily)    -- write-cold, FREE + always-on;
                   read-activity BLIND (accepted per Andrew 2026-07-17) -> signal_basis says so
  EC2_INSTANCE   : CW CPUUtilization + NetworkIn (idle = both under floor) -- idle != stopped
  EVENT_RULE     : CW AWS/Events Invocations per RuleName (Sum, daily)  -- CADENCE-AWARE (below)

THE TWO LOAD-BEARING CONTROLS (CTO ruling-20 hard-required; the whole reason to build carefully):
  1. TRADING-CALENDAR DORMANCY (NEVER#1). A T-1 pipeline/data bucket write-cold over a weekend +
     market holiday is the CORRECT T-1 state, NOT debris. For pipeline/data resources (S3/DDB matching
     _PIPELINE_DATA_RX) the dormancy is counted in NYSE TRADING days via lib/trading_calendar -- the
     ONE frontier definition (CLAUDE.md NEVER#1) -- injected into classify() as age_fn. A Monday sweep
     does NOT false-flag Friday's data as dead. Wall-clock is kept for non-data resources.
  2. CADENCE-AWARE WINDOWING for scheduled resources. A monthly EVENT_RULE cold 23d is HEALTHY; a
     daily runner cold 21d IS a finding. The adapter reads ScheduleExpression (rate/cron) and judges
     HOT/COLD against the rule's OWN cadence -- never a flat window. Cadence only ever WIDENS the hot
     window for infrequent rules; it never shrinks it below the default.

Read-only, advisory, NEVER deletes. Author: 0.8.0_AE_CloudComp~B (NFRA_DECOMTOOL.TO-1). 2026-07-17.
"""
from __future__ import annotations

import datetime as dt
import math
import os
import re
import sys

_HERE = os.path.dirname(os.path.abspath(__file__))
_REPO = os.path.normpath(os.path.join(_HERE, "..", "..", ".."))
for _p in (_HERE, os.path.join(_REPO, "lib")):
    if _p not in sys.path:
        sys.path.insert(0, _p)
import comp_debris as cd  # noqa: E402  (classify, BANDS, _HELD_RX -- the invariants, reused verbatim)
import trading_calendar as tc  # noqa: E402  (the ONE trading-day frontier, NEVER#1)

EC2_CPU_FLOOR = 2.0          # avg %CPU below this on a day = "not actively computing"
EC2_NETIN_FLOOR = 1_000_000  # bytes/day NetworkIn below this = "not actively serving"

# T-1 PIPELINE / DATA resources: dormancy counted in TRADING days, not wall-clock (NEVER#1). A
# conservative superset of the data-plane naming. The direction of any misclassification is SAFE:
# applying trading-day counting to a non-T-1 resource only UNDER-counts its dormancy (looks healthier)
# -- it can never MANUFACTURE a false outage, the only error NEVER#1 forbids.
_PIPELINE_DATA_RX = re.compile(
    r"(opal-data-|opal-partner-|-nna\b|-aua\b|accounts|positions|holdings|"
    r"market-updates|served|platinum|silver-|gold-|-daily\b)", re.I)


def _cw(region: str):
    import boto3
    return boto3.client("cloudwatch", region_name=region)


def _get_metric_data(cw, queries: list, days: int) -> dict:
    """queries: [{id, namespace, metric, dims:[{Name,Value}], stat}]. Returns {id: [(ts, value)]}.
    Batches <=500 per GetMetricData call and paginates NextToken. Daily period."""
    end = dt.datetime.now(dt.timezone.utc)
    start = end - dt.timedelta(days=days)
    out: dict = {}
    for i in range(0, len(queries), 500):
        chunk = queries[i:i + 500]
        mdq = [{
            "Id": q["id"],
            "MetricStat": {
                "Metric": {"Namespace": q["namespace"], "MetricName": q["metric"],
                           "Dimensions": q["dims"]},
                "Period": 86400, "Stat": q["stat"],
            },
            "ReturnData": True,
        } for q in chunk]
        token = None
        while True:
            kw = {"MetricDataQueries": mdq, "StartTime": start, "EndTime": end,
                  "ScanBy": "TimestampAscending"}
            if token:
                kw["NextToken"] = token
            resp = cw.get_metric_data(**kw)
            for r in resp.get("MetricDataResults", []):
                out.setdefault(r["Id"], []).extend(
                    list(zip(list(r.get("Timestamps", [])), r.get("Values", []))))
            token = resp.get("NextToken")
            if not token:
                break
    return out


def _last_nonzero_day(series: list):
    days = [(ts.date(), v) for ts, v in series if (v or 0) > 0]
    return max(days)[0].isoformat() if days else None


def _last_change_day(series: list):
    s = sorted(series, key=lambda x: x[0])
    last = None
    for k in range(1, len(s)):
        if s[k][1] != s[k - 1][1]:
            last = s[k][0].date()
    return last.isoformat() if last else None


# ---- the trading-day dormancy counter injected into classify() for T-1 resources (NEVER#1) -----
def _trading_age(now_date, last_d) -> int:
    """Dormancy in NYSE TRADING days: trading days between last activity and the expected priced
    frontier. Friday->Monday = ~0-1 trading days, so a healthy T-1 pipeline is never false-flagged
    COLD. Delegates entirely to lib/trading_calendar -- the ONE frontier definition."""
    return tc.trading_days_behind(last_d, tc.expected_last_trading_day(now_date))


def _is_t1_pipeline(name: str, rtype: str) -> bool:
    """A T-1 pipeline/data resource whose dormancy must be counted in trading days (NEVER#1)."""
    return rtype in ("S3_BUCKET", "DYNAMODB_TABLE") and bool(_PIPELINE_DATA_RX.search(name or ""))


# ---- cadence parsing for scheduled EVENT_RULEs (the second load-bearing control) ---------------
def _cadence_period_days(sched_expr):
    """Approximate a scheduled rule's fire interval in DAYS from its ScheduleExpression. rate(N unit)
    is exact; cron(...) is a documented heuristic (specific DOM->~monthly, specific DOW->~weekly, else
    daily). Returns None for an event-pattern rule (no schedule) -> judged on the DEFAULT window."""
    if not sched_expr:
        return None
    s = str(sched_expr).strip().lower()
    m = re.match(r"rate\((\d+)\s+(minute|hour|day|week|month)s?\)", s)
    if m:
        n = int(m.group(1))
        return n * {"minute": 1 / 1440, "hour": 1 / 24, "day": 1, "week": 7, "month": 30}[m.group(2)]
    if s.startswith("cron(") and s.endswith(")"):
        fields = s[5:-1].strip().split()
        if len(fields) >= 5:
            dom, month, dow = fields[2], fields[3], fields[4]
            if month not in ("*", "?") and any(c.isdigit() for c in month):
                return 365.0
            if dom not in ("*", "?"):
                return 30.0
            if dow not in ("*", "?"):
                return 7.0
            return 1.0
    return None


def _event_window(cadence, hot_days: int, days: int):
    """(eff_hot, eff_window) for an EVENT_RULE given its cadence. Cadence only WIDENS the hot window
    for an infrequent rule -- never shrinks it below the default. None cadence -> defaults unchanged."""
    if not cadence:
        return hot_days, days
    return max(hot_days, int(math.ceil(cadence * 1.5))), max(days, int(math.ceil(cadence * 3)))


# ---- adapters: each returns records [{rtype, name, created, hist, signal_basis[, cadence_days]}] -
def adapt_lambda(region: str, days: int) -> list:
    lam, cw, _ = cd._clients(region)
    recs = []
    for r in cd.list_lambdas(lam):
        recs.append({"rtype": "LAMBDA", "name": r["name"], "created": r.get("last_modified", ""),
                     "hist": cd.invocation_history(cw, r["name"], days), "signal_basis": "cw-invocations"})
    return recs


def adapt_dynamodb(region: str, days: int) -> list:
    import boto3
    ddb = boto3.client("dynamodb", region_name=region)
    cw = _cw(region)
    tables, tok = [], None
    while True:
        kw = {"ExclusiveStartTableName": tok} if tok else {}
        r = ddb.list_tables(**kw)
        tables += r.get("TableNames", [])
        tok = r.get("LastEvaluatedTableName")
        if not tok:
            break
    meta = {}
    for t in tables:
        try:
            meta[t] = ddb.describe_table(TableName=t)["Table"].get("CreationDateTime")
        except Exception:  # noqa: BLE001
            meta[t] = None
    queries = []
    for i, t in enumerate(tables):
        for m in ("ConsumedReadCapacityUnits", "ConsumedWriteCapacityUnits"):
            queries.append({"id": f"d{i}_{m[8:12].lower()}", "namespace": "AWS/DynamoDB",
                            "metric": m, "dims": [{"Name": "TableName", "Value": t}], "stat": "Sum"})
    data = _get_metric_data(cw, queries, days)
    recs = []
    for i, t in enumerate(tables):
        series = data.get(f"d{i}_read", []) + data.get(f"d{i}_writ", [])
        created = meta[t].astimezone(dt.timezone.utc).isoformat() if meta.get(t) else ""
        recs.append({"rtype": "DYNAMODB_TABLE", "name": t, "created": created,
                     "hist": {"read": True, "last_invoked_day": _last_nonzero_day(series),
                              "total": int(sum(v for _, v in series))},
                     "signal_basis": "cw-capacity(read+write)"})
    return recs


def adapt_s3(region: str, days: int) -> list:
    import boto3
    s3 = boto3.client("s3", region_name=region)
    cw = _cw(region)
    buckets = s3.list_buckets().get("Buckets", [])
    queries = [{"id": f"s{i}", "namespace": "AWS/S3", "metric": "NumberOfObjects",
                "dims": [{"Name": "BucketName", "Value": b["Name"]},
                         {"Name": "StorageType", "Value": "AllStorageTypes"}], "stat": "Average"}
               for i, b in enumerate(buckets)]
    data = _get_metric_data(cw, queries, days)
    recs = []
    for i, b in enumerate(buckets):
        series = data.get(f"s{i}", [])
        created = b["CreationDate"].astimezone(dt.timezone.utc).isoformat() if b.get("CreationDate") else ""
        recs.append({"rtype": "S3_BUCKET", "name": b["Name"], "created": created,
                     "hist": {"read": bool(series), "last_invoked_day": _last_change_day(series),
                              "total": None},
                     "signal_basis": "storage-delta(write-only; READ-UNKNOWN)"})
    return recs


def adapt_ec2(region: str, days: int) -> list:
    import boto3
    ec2 = boto3.client("ec2", region_name=region)
    cw = _cw(region)
    insts = []
    for resv in ec2.describe_instances().get("Reservations", []):
        insts += resv.get("Instances", [])
    queries = []
    for i, ins in enumerate(insts):
        iid = ins["InstanceId"]
        queries.append({"id": f"e{i}_cpu", "namespace": "AWS/EC2", "metric": "CPUUtilization",
                        "dims": [{"Name": "InstanceId", "Value": iid}], "stat": "Average"})
        queries.append({"id": f"e{i}_net", "namespace": "AWS/EC2", "metric": "NetworkIn",
                        "dims": [{"Name": "InstanceId", "Value": iid}], "stat": "Sum"})
    data = _get_metric_data(cw, queries, days)
    recs = []
    for i, ins in enumerate(insts):
        cpu = data.get(f"e{i}_cpu", [])
        net = data.get(f"e{i}_net", [])
        active = {ts.date() for ts, v in cpu if (v or 0) >= EC2_CPU_FLOOR}
        active |= {ts.date() for ts, v in net if (v or 0) >= EC2_NETIN_FLOOR}
        last = max(active).isoformat() if active else None
        lt = ins.get("LaunchTime")
        created = lt.astimezone(dt.timezone.utc).isoformat() if lt else ""
        recs.append({"rtype": "EC2_INSTANCE", "name": ins.get("InstanceId"), "created": created,
                     "hist": {"read": bool(cpu or net), "last_invoked_day": last, "total": None},
                     "signal_basis": "cw-cpu>=%.0f%%|netin>=%db (idle!=stopped -> PURPOSE-REVIEW)"
                     % (EC2_CPU_FLOOR, EC2_NETIN_FLOOR)})
    return recs


def adapt_events(region: str, days: int) -> list:
    import boto3
    ev = boto3.client("events", region_name=region)
    cw = _cw(region)
    fetch_days = max(days, 100)   # scheduled rules can be quarterly -> a window wide enough to see a fire
    rules, tok = [], None
    while True:
        kw = {"NextToken": tok} if tok else {}
        r = ev.list_rules(**kw)
        rules += [{"name": rr["Name"], "sched": rr.get("ScheduleExpression")} for rr in r.get("Rules", [])]
        tok = r.get("NextToken")
        if not tok:
            break
    queries = [{"id": f"r{i}", "namespace": "AWS/Events", "metric": "Invocations",
                "dims": [{"Name": "RuleName", "Value": rr["name"]}], "stat": "Sum"}
               for i, rr in enumerate(rules)]
    data = _get_metric_data(cw, queries, fetch_days)
    recs = []
    for i, rr in enumerate(rules):
        series = data.get(f"r{i}", [])
        cadence = _cadence_period_days(rr["sched"])
        basis = "cw-events-invocations"
        if rr["sched"]:
            basis += " sched=%s cadence~%s" % (rr["sched"], ("%.2gd" % cadence) if cadence else "?")
        else:
            basis += " (event-pattern; default window)"
        recs.append({"rtype": "EVENT_RULE", "name": rr["name"], "created": "", "cadence_days": cadence,
                     "hist": {"read": True, "last_invoked_day": _last_nonzero_day(series),
                              "total": int(sum(v for _, v in series))},
                     "signal_basis": basis})
    return recs


ADAPTERS = {"lambda": adapt_lambda, "ddb": adapt_dynamodb, "s3": adapt_s3,
            "ec2": adapt_ec2, "events": adapt_events}


# ---- the multi-type ledger (reuses cd.classify + cd._HELD_RX -- the invariants) ----------------
def multi_ledger(records: list, now_date, days: int, hot_days: int) -> dict:
    held, classified = [], []
    for rec in records:
        if cd._HELD_RX.search(rec["name"] or ""):
            held.append(f"{rec['rtype']}:{rec['name']}")
            continue
        row = {"name": rec["name"], "last_modified": rec["created"]}
        # CONTROL 1: T-1 pipeline/data -> trading-day dormancy (NEVER#1). CONTROL 2: scheduled rule
        # -> cadence-derived hot/window. Everything else -> wall-clock defaults.
        age_fn = _trading_age if _is_t1_pipeline(rec["name"], rec["rtype"]) else None
        eff_hot, eff_window = hot_days, days
        if rec["rtype"] == "EVENT_RULE":
            eff_hot, eff_window = _event_window(rec.get("cadence_days"), hot_days, days)
        band = cd.classify(row, rec["hist"], now_date, eff_window, eff_hot, age_fn=age_fn)
        band["rtype"] = rec["rtype"]
        band["signal_basis"] = rec["signal_basis"]
        band["dormancy_basis"] = "trading-days" if age_fn else "wall-clock"
        classified.append(band)
    by_band = {b: [c for c in classified if c["band"] == b] for b in cd.BANDS}
    reap = sorted(by_band["COLD-DORMANT"], key=lambda c: -c.get("dormant_days", 0))
    return {"window_days": days, "hot_days": hot_days, "n_total": len(records),
            "n_held_excluded": len(held), "held_excluded": sorted(held),
            "counts": {b: len(by_band[b]) for b in cd.BANDS},
            "reap_rank_cold_dormant": reap,
            "purpose_review_stillborn_or_guard": by_band["STILLBORN-OR-GUARD"],
            "too_young": by_band["TOO-YOUNG"], "unknown": by_band["UNKNOWN"], "hot": by_band["HOT"]}


def multi_render(led: dict) -> str:
    L = ["comp-debris --types -- multi-type coldest-first ledger (ADVISORY; NEVER deletes; hold-aware)",
         "  window %dd (hot %dd) | %d resources | %d held EXCLUDED | per-row SIGNAL BASIS + DORMANCY BASIS"
         % (led["window_days"], led["hot_days"], led["n_total"], led["n_held_excluded"]),
         "  bands: " + " ".join("%s=%d" % (b, led["counts"][b]) for b in cd.BANDS),
         "  NEVER#1: T-1 pipeline/data dormancy counted in TRADING days (lib/trading_calendar);",
         "  scheduled rules judged against their OWN cadence -- a weekend/monthly gap is NOT debris.",
         "",
         "  REAP RANK -- COLD-DORMANT only (dormancy AFTER activity; coldest first):"]
    if not led["reap_rank_cold_dormant"]:
        L.append("    (none dormant-after-activity in window)")
    for c in led["reap_rank_cold_dormant"][:30]:
        L.append("    %4d%-2s %-15s %-40s last=%s  [%s]"
                 % (c.get("dormant_days", 0), "td" if c.get("dormancy_basis") == "trading-days" else "d",
                    c["rtype"], c["name"], c.get("last_invoked"), c["signal_basis"]))
    sob = led["purpose_review_stillborn_or_guard"]
    if sob:
        L += ["", "  PURPOSE REVIEW -- STILLBORN-OR-GUARD (%d): older than window, zero activity" % len(sob)]
        for c in sob[:20]:
            L.append("    %-15s %-40s created=%s  [%s]" % (c["rtype"], c["name"], c["created"], c["signal_basis"]))
    if led["counts"]["UNKNOWN"]:
        L += ["", "  UNKNOWN (%d): blind read / no creation date -- NOT cold (see signal_basis)." % led["counts"]["UNKNOWN"]]
    L += ["", "  CONFIRMATION PASS (run ON this cold tail; NOT in this tool): comp-heat federated,",
          "  comp-dups, comp-deadgrant, comp-trigger, comp-iam-usage. Reaping is a human, never-widen act."]
    return "\n".join(L)


def collect(types: list, region: str, days: int):
    """Run the requested adapters; a failed adapter is surfaced, never assumed-cold."""
    records, errors = [], []
    for t in types:
        if t not in ADAPTERS:
            errors.append("unknown type '%s' (known: %s)" % (t, ",".join(ADAPTERS)))
            continue
        try:
            records += ADAPTERS[t](region, days)
        except Exception as e:  # noqa: BLE001
            errors.append("adapter %s failed: %s" % (t, str(e)[:160]))
    return records, errors


# ---- offline self-test: the two load-bearing controls as discriminating mutants (no AWS) -------
def self_test() -> bool:
    print("=== debris_adapters self-test (offline mutants; reuses cd.classify) ===")
    now = dt.date(2026, 7, 17)
    days, hot = 30, 7

    def iso(d):
        return "%sT00:00:00+00:00" % d

    ok = []

    def ck(name, cond, detail=""):
        ok.append(cond)
        print(f"  [{'PASS' if cond else 'FAIL'}] {name}" + (f"  ({detail})" if detail else ""))

    records = [
        {"rtype": "DYNAMODB_TABLE", "name": "cfg-table-cold", "created": iso("2026-01-01"),
         "hist": {"read": True, "last_invoked_day": "2026-06-20", "total": 5}, "signal_basis": "cw-capacity"},
        {"rtype": "S3_BUCKET", "name": "ops-flat-old", "created": iso("2025-01-01"),
         "hist": {"read": True, "last_invoked_day": None, "total": None}, "signal_basis": "storage-delta"},
        {"rtype": "S3_BUCKET", "name": "bucket-new", "created": iso("2026-07-10"),
         "hist": {"read": True, "last_invoked_day": None, "total": None}, "signal_basis": "storage-delta"},
        {"rtype": "EC2_INSTANCE", "name": "ec2-blind", "created": iso("2026-01-01"),
         "hist": {"read": False, "error": "AccessDenied"}, "signal_basis": "cw-cpu"},
        {"rtype": "LAMBDA", "name": "inf-gold-trigger", "created": iso("2026-01-01"),
         "hist": {"read": True, "last_invoked_day": None, "total": 0}, "signal_basis": "cw-invocations"},
        {"rtype": "EVENT_RULE", "name": "rule-hot", "created": iso("2026-01-01"), "cadence_days": 1.0,
         "hist": {"read": True, "last_invoked_day": "2026-07-16", "total": 900}, "signal_basis": "cw-events"},
    ]
    led = multi_ledger(records, now, days, hot)
    reap = {c["name"] for c in led["reap_rank_cold_dormant"]}
    ck("ddb_dormant_is_reap", reap == {"cfg-table-cold"} and led["reap_rank_cold_dormant"][0]["dormant_days"] == 27, f"reap={reap}")
    ck("s3_flat_old_is_stillborn",
       any(c["name"] == "ops-flat-old" for c in led["purpose_review_stillborn_or_guard"]) and "ops-flat-old" not in reap)
    ck("s3_new_is_too_young", any(c["name"] == "bucket-new" for c in led["too_young"]) and "bucket-new" not in reap)
    ck("ec2_blind_is_unknown", any(c["name"] == "ec2-blind" for c in led["unknown"]) and "ec2-blind" not in reap)
    ck("held_excluded", "LAMBDA:inf-gold-trigger" in led["held_excluded"]
       and all("inf-gold-trigger" not in {c["name"] for c in led[k]}
               for k in ("reap_rank_cold_dormant", "purpose_review_stillborn_or_guard", "unknown", "too_young", "hot")))
    ck("event_hot_is_hot", any(c["name"] == "rule-hot" for c in led["hot"]) and "rule-hot" not in reap)
    ck("signal_basis_on_every_row", all(c.get("signal_basis") for c in led["reap_rank_cold_dormant"] + led["hot"]))

    # CONTROL 1 -- the FALSE-OUTAGE MUTANT (NEVER#1). A T-1 data bucket last-written the trading day
    # before the 2026-07-03 NYSE holiday+weekend, read Monday. WALL-CLOCK = 4d -> COLD-DORMANT (false
    # outage). TRADING days = ~1 -> HOT. The verdicts MUST diverge; the T-1 name takes the healthy path.
    mnow, mhot = dt.date(2026, 7, 6), 3
    t1 = {"rtype": "S3_BUCKET", "name": "opal-data-inf", "created": iso("2025-01-01"),
          "hist": {"read": True, "last_invoked_day": "2026-07-02", "total": None}, "signal_basis": "storage-delta"}
    ops = {"rtype": "S3_BUCKET", "name": "ops-scratch-bucket", "created": iso("2025-01-01"),
           "hist": {"read": True, "last_invoked_day": "2026-07-02", "total": None}, "signal_basis": "storage-delta"}
    t1_led = multi_ledger([t1], mnow, 30, mhot)
    ops_led = multi_ledger([ops], mnow, 30, mhot)
    ck("MUTANT.t1_pipeline_weekend_is_HOT_not_debris",
       any(c["name"] == "opal-data-inf" for c in t1_led["hot"]) and not t1_led["reap_rank_cold_dormant"],
       f"dormancy_basis={(t1_led['hot'] or [{}])[0].get('dormancy_basis')}")
    ck("MUTANT.wall_clock_control_WOULD_have_flagged",
       "ops-scratch-bucket" in {c["name"] for c in ops_led["reap_rank_cold_dormant"]},
       "SAME Fri->Mon dates under wall-clock DO reap -- proves the fold changed the verdict, not a no-op")

    # CONTROL 2 -- the CADENCE MUTANT. A monthly rule cold 23d is HEALTHY (HOT); a daily runner cold
    # 21d IS a finding. Same absolute age, opposite verdict -- cadence is the discriminator.
    monthly = {"rtype": "EVENT_RULE", "name": "fred-ingestion-monthly-late", "created": iso("2026-01-01"),
               "cadence_days": 30.0, "hist": {"read": True, "last_invoked_day": "2026-06-24", "total": 6},
               "signal_basis": "cw-events"}
    daily = {"rtype": "EVENT_RULE", "name": "some-fees-runner-daily", "created": iso("2026-01-01"),
             "cadence_days": 1.0, "hist": {"read": True, "last_invoked_day": "2026-06-26", "total": 21},
             "signal_basis": "cw-events"}
    cled = multi_ledger([monthly, daily], dt.date(2026, 7, 17), 120, hot)
    creap = {c["name"] for c in cled["reap_rank_cold_dormant"]}
    ck("CADENCE.monthly_23d_is_HOT_not_debris",
       any(c["name"] == "fred-ingestion-monthly-late" for c in cled["hot"]) and "fred-ingestion-monthly-late" not in creap)
    ck("CADENCE.daily_21d_IS_a_finding", "some-fees-runner-daily" in creap)

    good = all(ok)
    print("  " + ("OK: multi-type never-active!=cold, UNKNOWN-band, hold-aware, signal-basis-per-row, "
                  "trading-calendar false-outage mutant + cadence mutant -- all held"
                  if good else "ERROR: debris_adapters self-test FAILED"))
    return good


if __name__ == "__main__":
    sys.exit(0 if self_test() else 1)
