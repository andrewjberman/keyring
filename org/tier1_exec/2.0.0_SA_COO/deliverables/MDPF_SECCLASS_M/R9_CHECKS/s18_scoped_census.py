#!/usr/bin/env python3
"""s18_scoped_census.py -- MDPF_SECCLASS-S18 class cell: the SCOPED liveness rule's delta, beside the as-ruled one.

READ-ONLY. s18_cell_delta_census.py measured the as-ruled rule (every account OPEN in the accounts dimension carries forward):
it uncaps 4,095 accounts, 3,568 of them with a last trade before 09-30 (back to 2020) -- served history would gain ~3.55M
account-days. This census measures the scoped rule: an account carries forward when it is OPEN in the dimension AND held a
position in the cube partition of the reference day (the latest existing partition strictly before the new frontier).

Also reads the drop accounts the as-ruled frontier class did not cover: source class, last trade, units on both days.
Writes S18_SCOPED_CENSUS_20261003.json.
"""
from __future__ import annotations

import json
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import pandas as pd

sys.path.insert(0, str(Path(__file__).resolve().parent))
import s18_cell_delta_census as c  # noqa: E402  (reuses its readers and A_03 import)

OUT = Path(__file__).resolve().parent / "S18_SCOPED_CENSUS_20261003.json"


def main():
    a03 = c.a03
    keys = sorted(o["Key"] for p in c.s3.get_paginator("list_objects_v2").paginate(Bucket=c.BUCKET, Prefix=a03.S3_TXN_PREFIX)
                  for o in p.get("Contents", []) if o["Key"].endswith(".parquet"))
    with ThreadPoolExecutor(16) as pool:
        parts = list(pool.map(c.per_file, keys))
    acct = pd.concat([g for g, _, _ in parts]).groupby(level=0).agg(last=("last", "max"), daily=("daily", "any"))
    frontier = acct["last"].max()
    tx = pd.DataFrame({"account_id": acct.index, "trade_date": acct["last"].values,
                       "_source_file": ["TXN_DAILY" if d else "backfill" for d in acct["daily"].values]})

    cube_dates = sorted(o["Key"].rsplit("/", 1)[-1].split(".")[0]
                        for p in c.s3.get_paginator("list_objects_v2").paginate(Bucket=c.BUCKET, Prefix=c.POSITIONS_CUBE_PREFIX)
                        for o in p.get("Contents", []))
    ref = max(d for d in cube_dates if d < frontier.strftime("%Y-%m-%d"))
    ref_df = c.read_parquet(c.positions_cube_key(ref))
    held_ref = set(ref_df["account_id"].astype(str))
    latest = max(cube_dates)
    latest_df = c.read_parquet(c.positions_cube_key(latest))
    held_latest = set(latest_df["account_id"].astype(str))

    alloc_open, _alive = a03._load_allocation_signals(frontier.strftime("%Y-%m-%d"))
    dim_open = a03._load_dimension_open_accounts() or set()
    carry = (dim_open & held_ref) | set(alloc_open)
    old_capped = a03._compute_account_end_dates(tx, set(alloc_open))
    new_capped = a03._compute_account_end_dates(tx, carry)
    uncapped = {a: d for a, d in old_capped.items() if a not in new_capped}
    history = {a: d for a, d in uncapped.items() if d < pd.Timestamp(ref)}

    drop = (held_ref - held_latest) & dim_open
    still_dropped = sorted(a for a in drop if a not in uncapped)
    detail = {}
    for a in still_dropped:
        r = acct.loc[a] if a in acct.index else None
        detail[a] = {"daily_feed": bool(r["daily"]) if r is not None else None,
                     "last_trade": str(r["last"].date()) if r is not None else None,
                     "capped_old_rule": str(old_capped[a].date()) if a in old_capped else None,
                     "rows_on_ref": ref_df[ref_df["account_id"].astype(str) == a][["asset_name", "units"]]
                     .head(8).to_dict("records")}

    out = {
        "claim": "measured (A_03's own rule, current silver inputs, read-only); limit: no transaction_id de-dup",
        "frontier": str(frontier.date()), "reference_day": ref, "latest_partition": latest,
        "dimension_open": len(dim_open), "held_on_reference_day": len(held_ref),
        "carry_set_dimension_open_and_held": len(dim_open & held_ref), "allocation_confirmed": len(alloc_open),
        "old_capped": len(old_capped), "scoped_capped": len(new_capped), "scoped_uncapped": len(uncapped),
        "scoped_uncapped_with_last_trade_before_reference_day": len(history),
        "drop_set": len(drop), "drop_set_carried_by_scoped_rule": len(drop & set(uncapped)),
        "drop_set_not_carried": detail,
    }
    OUT.write_text(json.dumps(out, indent=1, default=str), encoding="utf-8")
    print(json.dumps(out, indent=1, default=str))
    print("WROTE", OUT)


if __name__ == "__main__":
    main()
