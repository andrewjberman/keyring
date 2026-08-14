"""/mdpf-refresh driver -- fresh gold run + platinum publish for MDPF, one command.

Built on Andrew-direct 2026-08-14 ~1517Z (recorded at
org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20260814_EMITTER_EMPLOY_AND_REFRESH_SKILL.md):
"we should have a mechanism built, perhaps in the context of a skill that covers everything
that needs to happen ... to initiate a fresh gold and platinum reset run for mdpf."

WHAT IT FIRES: the SAME Lambdas the production schedules target (the sanctioned ad-hoc
accelerator form -- the schedules stay the production path; this is run-and-read QA/refresh,
never production evidence). Exercised reference: AE 0.7.0's tonight-refresh
(session_0541-0625Z_mdpf_trgaln_tonight_refresh.md) -- this driver encodes that same chain.

MODES
  status  read-only preflight: expected T-1, per-scope platinum as_of, monolith input
          freshness. Zero invocations.
  gold    (default) floor -> accrual -> publisher -> verify. Assumes monolith inputs current.
  full    vendor pulls + mirrors first (COT session+mirror, INF jwt+family+mirror), then gold.
          49F vendor legs are MORNING FILE DELIVERIES -- not ad-hoc invocable; reported only.
  --reland  after a run held CONFLICT keys: list them; with --confirm, DELETE the conflicted
          dated gold keys named by the run manifest and note re-land occurs on next build.
          RESERVED-CATEGORY: run this ONLY on Andrew's explicit in-session word (see SKILL.md).

DESIGN RULES HONORED: no watchers/alarms/monitors armed (standing moratorium); the INF gold
sentinel is NEVER written by hand (DOOR 6 -- forged completion signal); ad-hoc invokes carry
source labels that are NOT "aws.events" so the consolidator's A6 manifest records kind
honestly; boto3 throughout (no subprocess aws -- the MSYS argv class never enters);
device-agnostic (repo root resolved, no baked paths).
"""
from __future__ import annotations

import argparse
import datetime as dt
import json
import subprocess
import sys
import time
from pathlib import Path

import boto3
from botocore.config import Config


def _repo_root() -> Path:
    out = subprocess.run(["git", "rev-parse", "--show-toplevel"],
                         capture_output=True, text=True, check=True)
    return Path(out.stdout.strip())


sys.path.insert(0, str(_repo_root() / "lib"))
from trading_calendar import (  # noqa: E402
    expected_last_trading_day,
    prev_trading_day,
    trading_days_behind,
)

REGION = "us-east-1"
ASSETS = "opal-data-assets"
PORTAL = "opal-data-portal-v2"
SCOPES = ("49financial", "inflection", "cottonwood", "global")
MANIFEST_PREFIX = "portal/gold/mdpf/_manifests"

LAMBDA_FLOOR = "mdpf-gold-lambda"
LAMBDA_ACCRUAL = "mdpf-accrual-trigger"
LAMBDA_PUBLISHER = "opal-assets-mdpf-portal-publisher"
LAMBDA_COT_SESSION = "cot-bd-session-trigger"
LAMBDA_MIRROR = "opal-assets-ingest-mirror"
INF_CHAIN = ("inf-jwt-trigger", "inf-api-reps", "inf-accounts-v2-daily",
             "inf-bronze-trigger", "inf-api-assets-v2", "inf-api-eclipse",
             "inf-api-positions", "inf-api-txn")

ADHOC_SOURCE = {"source": "adhoc", "run_class": "adhoc-qa",
                "invoked_by": "mdpf-refresh-skill"}

_cfg = Config(region_name=REGION, read_timeout=900, retries={"max_attempts": 2})
_lam = boto3.client("lambda", config=_cfg)
_s3 = boto3.client("s3", config=_cfg)
_ssm = boto3.client("ssm", config=_cfg)


def log(msg: str) -> None:
    ts = dt.datetime.now(dt.timezone.utc).strftime("%H:%M:%SZ")
    print(f"[mdpf-refresh {ts}] {msg}", flush=True)


def expected_t1() -> str:
    """The serve target: the last COMPLETE trading day. expected_last_trading_day returns
    TODAY mid-session on a trading day (its contract is the T+1-priced frontier), so the
    serve target is its prev_trading_day when it lands on an unsettled today. PASS in the
    verify step is the estate's own bar: trading_days_behind(as_of, frontier) <= 1 (the
    platinum source_vintage_last 'current' threshold), with the equality target printed."""
    now = dt.datetime.now(dt.timezone.utc)
    frontier = expected_last_trading_day(now)
    d = prev_trading_day(frontier)
    return d.isoformat() if hasattr(d, "isoformat") else str(d)


def behind(as_of: "str | None") -> "int | None":
    if not as_of:
        return None
    return trading_days_behind(as_of, expected_last_trading_day(
        dt.datetime.now(dt.timezone.utc)))


def platinum_as_of(scope: str) -> "tuple[str | None, str | None]":
    key = f"platinum/mdpf/{scope}/aggregate-aua-timeseries.json"
    try:
        o = _s3.get_object(Bucket=PORTAL, Key=key)
    except Exception:  # noqa: BLE001
        return None, None
    doc = json.loads(o["Body"].read())
    return doc.get("as_of_last"), o["LastModified"].strftime("%Y-%m-%dT%H:%M:%SZ")


def head_time(bucket: str, key: str) -> "str | None":
    try:
        h = _s3.head_object(Bucket=bucket, Key=key)
        return h["LastModified"].strftime("%Y-%m-%dT%H:%M:%SZ")
    except Exception:  # noqa: BLE001
        return None


def latest_partition(prefix: str) -> "str | None":
    dates = []
    for page in _s3.get_paginator("list_objects_v2").paginate(
            Bucket=ASSETS, Prefix=prefix + "/", Delimiter="/"):
        for cp in page.get("CommonPrefixes", []):
            p = cp["Prefix"]
            if "date=" in p:
                dates.append(p.split("date=")[1].rstrip("/"))
    return max(dates) if dates else None


def invoke(name: str, payload: dict) -> dict:
    log(f"invoke {name} ...")
    r = _lam.invoke(FunctionName=name, InvocationType="RequestResponse",
                    Payload=json.dumps(payload).encode())
    body = r["Payload"].read()
    if r.get("FunctionError"):
        log(f"  ERROR: {name} FunctionError={r['FunctionError']}: {body[:400]!r}")
        raise RuntimeError(f"{name} failed")
    try:
        out = json.loads(body)
    except Exception:  # noqa: BLE001
        out = {"raw": body.decode(errors="replace")[:400]}
    log(f"  {name} -> {json.dumps(out)[:300]}")
    return out


def _find_ssm_ref(obj) -> "tuple[str | None, str | None]":
    """Recursively hunt (command_id, instance_id) in a lambda response."""
    cmd = inst = None
    def walk(o):
        nonlocal cmd, inst
        if isinstance(o, dict):
            for k, v in o.items():
                lk = str(k).lower()
                if isinstance(v, str):
                    if "command" in lk and "id" in lk:
                        cmd = v
                    if ("instance" in lk and "id" in lk) or lk == "runner":
                        # `runner` matched empirically 2026-08-14: the accrual
                        # trigger returns {"runner": "i-...", "ssm_command_id":
                        # ...} and the instance-only hunt missed it, so pass 3
                        # published without awaiting the accrual SSM (it ended
                        # Success; the miss cost nothing that day, but the wait
                        # exists for the day it does).
                        inst = v
                walk(v)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(obj)
    return cmd, inst


def wait_ssm(cmd: str, inst: str, label: str, timeout_s: int = 600) -> str:
    t0 = time.time()
    while time.time() - t0 < timeout_s:
        try:
            r = _ssm.get_command_invocation(CommandId=cmd, InstanceId=inst)
            st = r["Status"]
        except _ssm.exceptions.InvocationDoesNotExist:
            st = "Pending"
        if st in ("Success", "Failed", "Cancelled", "TimedOut"):
            log(f"  {label} SSM {cmd[:8]} -> {st}")
            return st
        time.sleep(10)
    log(f"  WARN {label} SSM {cmd[:8]} still running after {timeout_s}s -- proceeding is "
        f"NOT safe; aborting this leg")
    return "Timeout"


def run_leg_with_ssm(name: str, payload: dict, label: str) -> None:
    out = invoke(name, payload)
    cmd, inst = _find_ssm_ref(out)
    if cmd and inst:
        st = wait_ssm(cmd, inst, label)
        if st != "Success":
            raise RuntimeError(f"{label}: SSM ended {st}")
    else:
        log(f"  ({label}: no SSM ref in response -- treating the synchronous return as "
            f"completion)")


def latest_run_manifest() -> "tuple[str | None, dict | None]":
    keys = []
    for page in _s3.get_paginator("list_objects_v2").paginate(
            Bucket=ASSETS, Prefix=MANIFEST_PREFIX + "/"):
        for o in page.get("Contents", []):
            keys.append((o["LastModified"], o["Key"]))
    if not keys:
        return None, None
    key = max(keys)[1]
    doc = json.loads(_s3.get_object(Bucket=ASSETS, Key=key)["Body"].read())
    return key, doc


def manifest_conflicts(doc: dict) -> list:
    """Conflict rows from the A6 run manifest. The rows live under `writes` (measured
    2026-08-14 on the live manifest: top keys run/scopes/writes/errors) -- this function
    originally read `objects`/`rows` and returned a CLEAN FALSE ZERO for two passes while
    the guard held 12 keys; the fallbacks are kept behind the real field, never instead."""
    rows = ((doc or {}).get("writes") or (doc or {}).get("objects")
            or (doc or {}).get("rows") or [])
    if isinstance(rows, dict):
        rows = list(rows.values())
    return [r for r in rows if isinstance(r, dict) and r.get("status") == "conflict"]


def preflight() -> str:
    t1 = expected_t1()
    print(f"\n== PREFLIGHT ==  serve target T-1 (trading calendar): {t1}")
    for s in SCOPES:
        as_of, lm = platinum_as_of(s)
        b = behind(as_of)
        mark = "---" if as_of is None else ("OK " if b is not None and b <= 1 else "LAG")
        print(f"  platinum {s:<12} as_of_last={as_of}  written={lm}  "
              f"[{mark} behind={b}]")
    print("  monolith inputs:")
    for label, prefix in (
            ("49f smartx fact_model_aum_daily", "smartx/platform/silver/fact_model_aum_daily"),
            ("49f schwab fact_rps_s2", "schwab/08242234/silver/fact_rps_s2"),
            ("inf orion fact_assets", "orion/inflection/silver/fact_assets"),
            ("inf eclipse fact_portfolios_full", "eclipse/inflection/silver/fact_portfolios_full"),
            ("cot bd fact_holdings", "blackdiamond/cottonwood/silver/fact_holdings")):
        print(f"    {label:<38} latest date= {latest_partition(prefix)}")
    dim = head_time(ASSETS, "blackdiamond/cottonwood/gold/dim_model_portfolio/"
                            f"date={t1}/data.parquet")
    print(f"    cot dim_model_portfolio @T-1: {'present ' + dim if dim else 'absent (fed by the INF-sentinel convergence path)'}")
    return t1


def gold_publish(t1: str) -> int:
    start = dt.datetime.now(dt.timezone.utc)

    out = invoke(LAMBDA_FLOOR, dict(ADHOC_SOURCE, floor="mdpf-refresh-skill"))
    status = str(out.get("status", "?"))
    mkey, mdoc = latest_run_manifest()
    conflicts = manifest_conflicts(mdoc)
    log(f"floor status={status}; run manifest {mkey}; conflicts={len(conflicts)}")
    if conflicts:
        print("\n!! CONFLICT-HELD DATED GOLD KEYS (recorded, NOT overwritten -- by design):")
        for c in conflicts:
            print(f"   {c.get('key')}")
        print("   Resolution is delete-and-re-land, RESERVED-CATEGORY: requires Andrew's")
        print("   explicit in-session word, then: mdpf_refresh.py --reland --confirm")
        print("   (which deletes EXACTLY the keys above and re-runs the floor).")
    if status not in ("green", "ok", "success"):
        log(f"floor returned status={status} -- read the manifest before proceeding; "
            f"aborting the chain here")
        return 1

    run_leg_with_ssm(LAMBDA_ACCRUAL, dict(ADHOC_SOURCE), "accrual")

    pub = invoke(LAMBDA_PUBLISHER, dict(ADHOC_SOURCE))
    log(f"publisher -> {json.dumps(pub)[:200]}")

    print("\n== VERIFY (served platinum vs serve target) ==")
    fails = 0
    for s in SCOPES:
        as_of, lm = platinum_as_of(s)
        b = behind(as_of)
        fresh = lm is not None and lm >= start.strftime("%Y-%m-%dT%H:%M:%SZ")
        ok = (b is not None and b <= 1) and fresh
        fails += 0 if ok else 1
        print(f"  {s:<12} as_of_last={as_of} (target {t1}, behind={b})  written={lm} "
              f"({'fresh' if fresh else 'STALE -- publisher did not rewrite it this run'})"
              f"  [{'PASS' if ok else 'FAIL'}]")
    # inflection reconstructed-date transparency (EVR)
    try:
        o = _s3.get_object(Bucket=PORTAL,
                           Key="platinum/mdpf/inflection/aggregate-aua-timeseries.json")
        doc = json.loads(o["Body"].read())
        rec = ((doc.get("meta") or {}).get("reconstructed") or {}).get("dates") or []
        empty = [doc["dates"][i] for i in range(len(doc.get("dates", [])))
                 if doc["model_aua"][i] is None and doc["non_model_aua"][i] is None]
        print(f"  inflection: reconstructed dates served={rec}; fully-empty dates={empty}")
    except Exception as e:  # noqa: BLE001
        print(f"  inflection reconstructed-date read failed: {e}")
    return 0 if fails == 0 else 1


def full_upstream() -> None:
    log("FULL mode: vendor pulls + mirrors first (49F legs are morning file deliveries -- "
        "not invocable; their freshness is preflight-reported only)")
    run_leg_with_ssm(LAMBDA_COT_SESSION, dict(ADHOC_SOURCE), "cot-session")
    invoke(LAMBDA_MIRROR, {"firm": "cot"})
    for fn in INF_CHAIN:
        run_leg_with_ssm(fn, dict(ADHOC_SOURCE), fn)
    invoke(LAMBDA_MIRROR, {"firm": "inf"})
    log("upstream legs complete (NOTE: the INF gold sentinel is never hand-written -- "
        "DOOR 6; serving does not need it, the monolith carries all MDPF inputs)")


def reland(confirm: bool) -> int:
    mkey, mdoc = latest_run_manifest()
    conflicts = manifest_conflicts(mdoc)
    if not conflicts:
        print(f"No conflict rows in the latest run manifest ({mkey}). Nothing to re-land.")
        return 0
    print(f"Latest run manifest: {mkey}")
    print(f"{len(conflicts)} conflict-held dated gold key(s):")
    for c in conflicts:
        print(f"  {c.get('key')}")
    if not confirm:
        print("\nDRY-RUN (no --confirm). These deletes are RESERVED-CATEGORY: run again with")
        print("--reland --confirm ONLY on Andrew's explicit in-session word.")
        return 0
    for c in conflicts:
        k = c.get("key")
        _s3.delete_object(Bucket=ASSETS, Key=k)
        print(f"  deleted s3://{ASSETS}/{k}")
    print("Conflicted keys deleted. Re-run the gold mode now; the fresh build re-lands them.")
    return 0


def main() -> int:
    ap = argparse.ArgumentParser(description="/mdpf-refresh driver")
    ap.add_argument("mode", nargs="?", default="gold",
                    choices=["status", "gold", "full"])
    ap.add_argument("--reland", action="store_true")
    ap.add_argument("--confirm", action="store_true")
    args = ap.parse_args()

    if args.reland:
        return reland(args.confirm)
    t1 = preflight()
    if args.mode == "status":
        return 0
    if args.mode == "full":
        full_upstream()
    return gold_publish(t1)


if __name__ == "__main__":
    sys.exit(main())
