#!/usr/bin/env python3
"""49F Performance cross-check: Opal's engine (f49_engine's linker) against Black Diamond performancePeriod.

Andrew-direct 2026-09-24 ~20:5xZ (record @964fb4ed6b): "we just match the same shape and compare against
Black Diamond". The 08-19 harness (4.0.0_SA_CRO~A, BD_PERFORMANCE_ENDPOINT_VS_GIPS_ENGINE_COMPARISON_20260819.md)
as a per-account census: BD's own pulled performancePeriod (the deployed opal-assets-bd49f-reporting-pull
bronze, one file per BD account) against the engine's twr_daily linked by the engine lane's own
parity_period_returns.link_account_period over the SAME window. Accounts pair through dim_account_xref
(BD externalId -> Schwab number), zero-padded to the engine's 10-digit key.

READ-ONLY. No vendor call (BD's figures are ones the estate already pulled). Output: a receipt with
band counts and distribution, account ids HASHED; per-account rows go to --detail (a local path).

Bands on |engine YTD - BD YTD| in basis points (TWR, cumulative, unannualised on both sides):
EXACT < 0.5, TIGHT < 10, LOOSE < 100, DIVERGENT >= 100; plus UNPAIRED (no xref row / no engine key)
and the engine cell's own UNAVAILABLE-* outcomes. The bands are a census, not a verdict.

Usage (backend worktree root):
  python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/f49_bd_crosscheck.py \
      --pull-date 2026-09-01 [--sample 300 --seed 20260924 | --all] --out <receipt.json> [--detail <rows.json>]
"""
from __future__ import annotations

import argparse
import hashlib
import io
import json
import random
import statistics
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[5]
for p in (ROOT / "lib", ROOT / "data/assets/scripts/gold/runners_49f",
          ROOT / "infra/aws/lambda/investor-reporting/performance"):
    sys.path.insert(0, str(p))

import boto3  # noqa: E402
import pandas as pd  # noqa: E402

import opal_naming  # noqa: E402
import parity_period_returns as ppr  # noqa: E402
from f49_engine import TABLE_DAILY  # noqa: E402

BD_BUCKET = "opal-data-assets"                                     # the puller's own FIRM-SEP-guarded plane
BD_PREFIX = "blackdiamond/49f/bronze/reporting_performance/"       # its bronze table
XREF_PREFIX = "blackdiamond/49f/silver/dim_account_xref/"
BANDS = ((0.5, "EXACT"), (10.0, "TIGHT"), (100.0, "LOOSE"))


def _h(value):
    return hashlib.sha256(str(value).encode()).hexdigest()[:12]


def _band(bp):
    for limit, name in BANDS:
        if abs(bp) < limit:
            return name
    return "DIVERGENT"


def _ytd_point(body, window_end):
    node = (body.get("levels") or [None])[0] or {}
    for point in node.get("dateRangePoints") or []:
        rng = point.get("dateRange") or {}
        if (str(rng.get("startDate", ""))[:10], str(rng.get("endDate", ""))[:10]) == (
                "%s-01-01" % window_end[:4], window_end):
            twr = point.get("timeWeightedReturns") or {}
            return {"bd_id": str((node.get("descriptor") or {}).get("levelKey")),
                    "bd_external_id": str((node.get("accountInfo") or {}).get("externalId")),
                    "twr": twr.get("return"), "annualized": twr.get("returnAnnualized"),
                    "days_held": twr.get("daysHeld"), "bmv": point.get("beginningMarketValue"),
                    "emv": point.get("endingMarketValue"), "net_additions": point.get("netAdditions")}
    return None


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--pull-date", required=True)
    ap.add_argument("--sample", type=int, default=300)
    ap.add_argument("--seed", type=int, default=20260924)
    ap.add_argument("--all", action="store_true")
    ap.add_argument("--out", required=True)
    ap.add_argument("--detail")
    args = ap.parse_args(argv)
    s3 = boto3.client("s3", region_name="us-east-1")

    keys = [o["Key"] for page in s3.get_paginator("list_objects_v2").paginate(
        Bucket=BD_BUCKET, Prefix=BD_PREFIX + args.pull_date + "/") for o in page.get("Contents", [])]
    window_ends = sorted({k.rsplit("_", 1)[-1][:10] for k in keys})
    if len(window_ends) != 1:
        raise SystemExit("expected one window end in the pull, found %s" % window_ends)
    window_end = window_ends[0]
    chosen = keys if args.all else random.Random(args.seed).sample(keys, min(args.sample, len(keys)))

    def read_bd(key):
        return _ytd_point(json.loads(s3.get_object(Bucket=BD_BUCKET, Key=key)["Body"].read()), window_end)

    with ThreadPoolExecutor(max_workers=16) as pool:
        bd = [r for r in pool.map(read_bd, chosen) if r is not None]

    xref_parts = sorted(p["Prefix"] for page in s3.get_paginator("list_objects_v2").paginate(
        Bucket=BD_BUCKET, Prefix=XREF_PREFIX, Delimiter="/") for p in page.get("CommonPrefixes", []))
    xref_key = [o["Key"] for o in s3.list_objects_v2(Bucket=BD_BUCKET, Prefix=xref_parts[-1])["Contents"]
                if o["Key"].endswith(".parquet")][0]
    xref = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=BD_BUCKET, Key=xref_key)["Body"].read()))

    firm = opal_naming.lookup("49financial")
    prefix = "%s/%s/" % (firm["trees"]["advi"]["gold_root"], TABLE_DAILY)
    parts = sorted(p["Prefix"][len(prefix) + 5:].rstrip("/") for page in s3.get_paginator("list_objects_v2").paginate(
        Bucket=firm["bucket"], Prefix=prefix, Delimiter="/") for p in page.get("CommonPrefixes", []))
    start = "%s-01-01" % window_end[:4]
    before = [d for d in parts if d < start]
    read = ([before[-1]] if before else []) + [d for d in parts if start <= d <= window_end]

    def read_day(day):
        raw = s3.get_object(Bucket=firm["bucket"], Key="%sdate=%s/data.parquet" % (prefix, day))["Body"].read()
        return pd.read_parquet(io.BytesIO(raw), columns=["account_id", "business_date", "r_net", "r_gross", "status"])

    with ThreadPoolExecutor(max_workers=16) as pool:
        daily = pd.concat(list(pool.map(read_day, read)), ignore_index=True)
    spine = {date.fromisoformat(d) for d in read}
    engine_keys = set(daily["account_id"].astype(str))

    to_schwab = {str(r.bd_account_id): str(r.schwab_account_id) for r in xref.itertuples()
                 if pd.notna(r.schwab_account_id)}
    rows = []
    for point in bd:
        row = {"bd_id_h": _h(point["bd_id"]), "bd_twr": point["twr"], "bd_annualized": point["annualized"],
               "bd_days_held": point["days_held"]}
        # dim_account_xref.bd_account_id is BD's externalId (z + 10 digits), measured 6202 of 6202.
        schwab = to_schwab.get(point["bd_external_id"])
        key = None if schwab is None else schwab.zfill(10)
        if key is None or key not in engine_keys or point["twr"] is None:
            row["outcome"] = "UNPAIRED" if point["twr"] is not None else "BD-NO-VALUE"
            rows.append(row)
            continue
        cell = ppr.link_account_period(daily, key, "YTD", window_end, spine, earliest_partition=parts[0])
        row.update({"engine_outcome": cell["outcome"], "engine_days_linked": cell["days_linked"],
                    "engine_days_neutral": cell["days_neutral"]})
        if cell["outcome"] != ppr.OUTCOME_COMPUTED:
            row["outcome"] = cell["outcome"]
        else:
            diff_bp = (float(cell["r_net_cum"]) - float(point["twr"])) * 1e4
            row.update({"engine_twr": float(cell["r_net_cum"]), "diff_bp": diff_bp, "outcome": _band(diff_bp)})
        rows.append(row)

    census = {}
    for r in rows:
        census[r["outcome"]] = census.get(r["outcome"], 0) + 1
    diffs = [abs(r["diff_bp"]) for r in rows if "diff_bp" in r]
    receipt = {
        "schema_version": "irpt-f49-bd-crosscheck-v1", "by": "2.0.0_SA_COO~P",
        "authority": "Andrew-direct @964fb4ed6b (CTO 100886)",
        "pull_date": args.pull_date, "window": [start, window_end], "metric": "TWR cumulative, net (engine r_net) vs BD timeWeightedReturns.return",
        "bd_files_in_pull": len(keys), "sampled": len(chosen), "sample_seed": None if args.all else args.seed,
        "bd_ytd_points_read": len(bd), "xref_key": xref_key, "engine_partitions_read": len(read),
        "engine_earliest_partition": parts[0], "bands_bp": {name: limit for limit, name in BANDS},
        "census": dict(sorted(census.items())), "denominator": len(rows),
        "compared": len(diffs),
        "abs_diff_bp": ({"median": statistics.median(diffs), "p90": sorted(diffs)[int(0.9 * (len(diffs) - 1))],
                         "max": max(diffs)} if diffs else None),
        "bd_annualized_values": sorted({str(r.get("bd_annualized")) for r in rows}),
        "identifiers": "account ids are hashed (sha256[:12]); no client identifier is written",
    }
    Path(args.out).write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
    if args.detail:
        Path(args.detail).write_text(json.dumps(rows, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=1))
    return 0


if __name__ == "__main__":
    main()
