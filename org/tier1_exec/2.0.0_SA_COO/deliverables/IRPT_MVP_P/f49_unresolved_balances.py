#!/usr/bin/env python3
"""Goal criterion 2, 49F: do the accounts Performance cannot compute hold any money?

The census (performance_resolvability_census.py, ee51ffafac) found 49F 6692 COMPUTED of 7454 not-terminated
directory accounts: 724 UNAVAILABLE-NO-LINKABLE-DAYS and 38 UNMAPPED. The directory states no termination for
them, so "active" there means "not known terminated". This reads the custodian's own latest balance
(schwab/<master>/silver/dim_balance, the object CTO 100712 names for 49F custody) for every account and bands
each outcome by market value: ABSENT (no balance row), ZERO (|mv| < 1 dollar), POSITIVE. An account with money
that Performance cannot compute is a real criterion-2 gap; a zero or absent one is a directory-termination gap.

Read-only, no vendor call, account ids never written. Reuses the census module's own functions.
Usage (backend worktree root):
  python org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_P/f49_unresolved_balances.py --ytd-end 2026-09-24 --out <receipt.json>
"""
from __future__ import annotations

import argparse
import importlib.util
import io
import json
import sys
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
_spec = importlib.util.spec_from_file_location("census", HERE / "performance_resolvability_census.py")
census = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(census)

BALANCE_PREFIX = "schwab/08335338/silver/dim_balance/"   # the CTO 100712 49F custody object, by listing
MV_COLUMNS = ("net_mv_positions", "net_mv_plus_cash")   # positions only; positions + cash
# NOT eqty_incl_option: measured 2026-09-25 it is populated for 85 of 7534 accounts (margin only), so it
# reads zero for 6239 of the 6324 accounts holding positions.


def latest_balances(s3, bucket):
    parts = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=BALANCE_PREFIX, Delimiter="/"):
        parts += [p["Prefix"] for p in page.get("CommonPrefixes", [])]
    latest = sorted(parts)[-1]
    frame = census.pd.read_parquet(io.BytesIO(s3.get_object(Bucket=bucket, Key=latest + "data.parquet")["Body"].read()))
    values = {}
    for row in frame[["account_id", *MV_COLUMNS]].itertuples(index=False):
        values[str(row[0]).strip().zfill(10)] = {c: (float(v) if v == v else 0.0) for c, v in zip(MV_COLUMNS, row[1:])}
    return latest.rstrip("/").rsplit("=", 1)[-1], list(MV_COLUMNS), values


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--ytd-end", required=True)
    ap.add_argument("--out", required=True)
    args = ap.parse_args(argv)
    s3 = census.boto3.client("s3", region_name="us-east-1")
    firm = census.tenants._CANONICAL_49F
    info = census.lookup(firm)
    dir_as_of, entries, active, _indicators = census.active_accounts(s3, firm)

    bucket, prefix = info["bucket"], "%s/%s/" % (info["trees"]["advi"]["gold_root"], census.TABLE_DAILY)
    parts = sorted(p["Prefix"][len(prefix) + 5:].rstrip("/") for page in s3.get_paginator("list_objects_v2").paginate(
        Bucket=bucket, Prefix=prefix, Delimiter="/") for p in page.get("CommonPrefixes", []))
    start = "%s-01-01" % args.ytd_end[:4]
    before = [d for d in parts if d < start]
    read = ([before[-1]] if before else []) + [d for d in parts if start <= d <= args.ytd_end]
    with census.ThreadPoolExecutor(max_workers=16) as pool:
        daily = census.pd.concat(list(pool.map(lambda d: census.pd.read_parquet(io.BytesIO(s3.get_object(
            Bucket=bucket, Key="%sdate=%s/data.parquet" % (prefix, d))["Body"].read()),
            columns=["account_id", "business_date", "r_net", "r_gross", "status"]), read)), ignore_index=True)
    all_keys = set(daily["account_id"].astype(str))
    latest_keys = set(daily.loc[daily["business_date"].astype(str).str[:10] == read[-1], "account_id"].astype(str))
    by_canonical_latest = {census.opaque_account(firm, k): k for k in latest_keys}
    by_canonical_any = {census.opaque_account(firm, k): k for k in all_keys}
    spine = {date.fromisoformat(d) for d in read}

    bal_date, mv_column, balances = latest_balances(s3, "opal-data-assets")
    bands = {}
    for a in active:
        key = by_canonical_latest.get(a)
        if key is None:
            outcome, bal_key = "UNMAPPED", by_canonical_any.get(a)
        else:
            outcome = census.ppr.link_account_period(daily, key, "YTD", args.ytd_end, spine,
                                                     earliest_partition=parts[0])["outcome"]
            bal_key = key
        if outcome == "COMPUTED":
            continue
        values = balances.get(bal_key) if bal_key else None
        row = bands.setdefault(outcome, {c: {"ABSENT": 0, "ZERO": 0, "POSITIVE": 0, "positive_total": 0.0}
                                         for c in MV_COLUMNS})
        for c in MV_COLUMNS:
            mv = None if values is None else values[c]
            band = "ABSENT" if mv is None else ("ZERO" if abs(mv) < 1.0 else "POSITIVE")
            row[c][band] += 1
            if band == "POSITIVE":
                row[c]["positive_total"] = round(row[c]["positive_total"] + mv, 2)
    receipt = {"schema_version": "irpt-f49-unresolved-balances-v1", "by": "2.0.0_SA_COO~P",
               "criterion": "goal (2), 49F: the accounts Performance cannot compute, by custodian market value",
               "directory_as_of": dir_as_of, "directory_entries": entries, "accounts_not_terminated": len(active),
               "engine_latest_partition": read[-1], "balance_date": bal_date, "balance_columns": mv_column,
               "balance_accounts": len(balances), "unresolved_by_outcome_and_band": bands,
               "identifiers": "no account id is written"}
    Path(args.out).write_text(json.dumps(receipt, indent=1) + "\n", encoding="utf-8")
    print(json.dumps(receipt, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
