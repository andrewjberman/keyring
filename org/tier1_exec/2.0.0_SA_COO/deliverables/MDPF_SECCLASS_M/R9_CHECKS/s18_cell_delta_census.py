#!/usr/bin/env python3
"""s18_cell_delta_census.py -- MDPF_SECCLASS-S18 class cell (CTO batches 220, 221): what the new A_03 liveness rule moves.

READ-ONLY. Applies A_03's own end-date rule (_compute_account_end_dates, imported from the deployed-to-be source) to the
current silver/transactions inputs twice -- the OLD open set (allocation file for the max trade date only) and the NEW one
(allocation UNION the accounts dimension) -- and prints which accounts change, split by the date their positions used to stop:

  frontier class : last trade == the prior served cube date (the 335 shape): only the new dates change.
  history class  : last trade <  the prior served cube date: SERVED HISTORY changes (rows appear from last trade + 1 day).

Streams the transactions per file (3 columns, aggregated per account) so laptop memory stays small. Not done here: the
transaction_id de-duplication A_03 applies (a census limit, stated in the output). Writes S18_CELL_DELTA_CENSUS_20261003.json.
"""
from __future__ import annotations

import importlib.util
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from io import BytesIO
from pathlib import Path

import boto3
import pandas as pd
import pyarrow.fs as pafs
import pyarrow.parquet as pq

ROOT = Path(__file__).resolve().parents[6]
GOLD = ROOT / "data" / "black_diamond" / "scripts" / "gold"
sys.path.insert(0, str(GOLD))
from lib.s3_layout import POSITIONS_CUBE_PREFIX, account_aua_timeseries_key, positions_cube_key  # noqa: E402

_spec = importlib.util.spec_from_file_location("a03", GOLD / "A_03.positions_cube.py")
a03 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(a03)

BUCKET = "opal-data-bd"
OUT = Path(__file__).resolve().parent / "S18_CELL_DELTA_CENSUS_20261003.json"
s3 = boto3.client("s3", region_name="us-east-1")


def read_parquet(key, columns=None):
    for attempt in range(6):   # body reads time out on this link now and then; a retry is a re-read, never a guess
        try:
            return pd.read_parquet(BytesIO(s3.get_object(Bucket=BUCKET, Key=key)["Body"].read()), columns=columns)
        except Exception:  # noqa: BLE001
            if attempt == 5:
                raise


_fs = pafs.S3FileSystem(region="us-east-1")


def per_file(key):
    # Column-pruned ranged reads: the three columns are ~2.5 pct of a file's bytes (this link reads under 0.4 MB/s).
    for attempt in range(6):
        try:
            pf = pq.ParquetFile(_fs.open_input_file(f"{BUCKET}/{key}"))
            cols = [c for c in ("account_id", "trade_date", "_source_file") if c in pf.schema_arrow.names]
            df = pf.read(columns=cols).to_pandas()
            break
        except Exception:  # noqa: BLE001
            if attempt == 5:
                raise
    df["trade_date"] = pd.to_datetime(df["trade_date"])
    daily = df["_source_file"].str.contains("TXN_DAILY", na=False) if "_source_file" in df.columns else False
    df["is_daily"] = daily
    g = df.groupby("account_id").agg(last=("trade_date", "max"), daily=("is_daily", "any"))
    return g, ("_source_file" in df.columns), len(df)


def main():
    keys = sorted(o["Key"] for p in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=a03.S3_TXN_PREFIX)
                  for o in p.get("Contents", []) if o["Key"].endswith(".parquet"))
    with ThreadPoolExecutor(16) as pool:
        parts = list(pool.map(per_file, keys))
    print(f"read {len(parts):,} transaction files", flush=True)
    rows = sum(n for _, _, n in parts)
    no_src = sum(1 for _, has, _ in parts if not has)
    acct = pd.concat([g for g, _, _ in parts]).groupby(level=0).agg(last=("last", "max"), daily=("daily", "any"))
    max_trade = acct["last"].max()

    # The same synthetic per-account frame A_03's rule reads: one row per account carrying its last trade and source class.
    tx = pd.DataFrame({"account_id": acct.index, "trade_date": acct["last"].values,
                       "_source_file": ["TXN_DAILY" if d else "backfill" for d in acct["daily"].values]})

    alloc_date = max_trade.strftime("%Y-%m-%d")
    alloc_open, alive = a03._load_allocation_signals(alloc_date)
    dim_open = a03._load_dimension_open_accounts() or set()
    old_capped = a03._compute_account_end_dates(tx, set(alloc_open))
    new_capped = a03._compute_account_end_dates(tx, set(alloc_open) | dim_open)
    uncapped = {a: d for a, d in old_capped.items() if a not in new_capped}

    prior = a03._latest_served_cube_date()
    cube_dates = sorted(o["Key"].rsplit("/", 1)[-1].split(".")[0]
                        for p in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=POSITIONS_CUBE_PREFIX)
                        for o in p.get("Contents", []))
    pre_prior = max(d for d in cube_dates if d < prior.strftime("%Y-%m-%d"))
    held_pre = set(read_parquet(positions_cube_key(pre_prior), ["account_id"])["account_id"].astype(str))
    held_prior = set(read_parquet(positions_cube_key(prior.strftime("%Y-%m-%d")), ["account_id"])["account_id"].astype(str))
    the_drop = (held_pre - held_prior) & dim_open        # the S18 set: on the day before the latest partition, not on it

    frontier = {a: d for a, d in uncapped.items() if d >= pd.Timestamp(pre_prior)}
    history = {a: d for a, d in uncapped.items() if d < pd.Timestamp(pre_prior)}
    hist_days = sum((pd.Timestamp(pre_prior) - d).days for d in history.values())

    def last_aua(a):
        try:
            ts = json.loads(s3.get_object(Bucket=BUCKET, Key=account_aua_timeseries_key(a))["Body"].read())
            pts = [p for p in (ts.get("data") or []) if (p.get("total_aua") or 0) > 0]
            return a, (pts[-1]["date"], float(pts[-1]["total_aua"])) if pts else None
        except Exception as e:  # noqa: BLE001 -- recorded per account
            return a, ("unreadable", str(e)[:60])
    with ThreadPoolExecutor(8) as pool:
        hist_aua = dict(pool.map(last_aua, sorted(history)))
    hist_sum = sum(v[1] for v in hist_aua.values() if v and isinstance(v[1], float))
    by_month = pd.Series([d.strftime("%Y-%m") for d in history.values()]).value_counts().sort_index().to_dict() if history else {}

    out = {
        "claim": "measured (A_03's own rule over the current silver inputs, read-only); limit: no transaction_id de-dup",
        "inputs": {"txn_files": len(keys), "txn_rows": rows, "files_without__source_file": no_src,
                   "accounts": int(len(acct)), "max_trade_date": alloc_date,
                   "allocation_file_for_max_trade_date_open": len(alloc_open), "phantom_alive_set": len(alive),
                   "dimension_open": len(dim_open)},
        "cube": {"latest_partition": prior.strftime("%Y-%m-%d"), "day_before": pre_prior,
                 "accounts_day_before": len(held_pre), "accounts_latest": len(held_prior),
                 "dimension_open_on_day_before_absent_from_latest": len(the_drop)},
        "rule": {"old_capped": len(old_capped), "new_capped": len(new_capped), "uncapped_by_the_fix": len(uncapped),
                 "frontier_class": len(frontier), "frontier_class_covers_the_drop": len(the_drop & set(frontier)),
                 "drop_not_in_frontier_class": sorted(the_drop - set(frontier))[:25],
                 "history_class": len(history), "history_class_account_days": hist_days,
                 "history_class_by_last_trade_month": by_month,
                 "history_class_last_positive_aua_sum": round(hist_sum, 2),
                 "history_class_unreadable": sum(1 for v in hist_aua.values() if v and v[0] == "unreadable"),
                 "history_class_never_positive": sum(1 for v in hist_aua.values() if v is None)},
        "history_class_sample": {a: [history[a].strftime("%Y-%m-%d"), hist_aua.get(a)] for a in sorted(history)[:15]},
    }
    OUT.write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    print(json.dumps({k: out[k] for k in ("inputs", "cube", "rule")}, indent=1, default=str))
    print("WROTE", OUT)


if __name__ == "__main__":
    main()
