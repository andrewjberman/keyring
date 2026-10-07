#!/usr/bin/env python3
"""sector_industry_group_values.py -- MDPF_SECCLASS SC-e-25 measuring script (read-only, us-east-1).

Reads every bbg/<date>/characteristics.parquet partition in s3://opal-data-etfs and the newest served
gold/holding/date=<date>/holding.parquet, and writes M/SECTOR_INDUSTRY_GROUP_VALUES_<YYYYMMDD>.json.
No S3 write, no table write. Run from the repo root.
"""
import datetime
import io
import json
import os
import re
import sys

import boto3
import pandas as pd

BUCKET = "opal-data-etfs"
OUT_DIR = os.path.join("org", "tier1_exec", "2.0.0_SA_COO", "deliverables", "MDPF_SECCLASS_M")
SECTOR_COL = "GICS_SECTOR_NAME"
IG_COL = "GICS_INDUSTRY_GROUP_NAME"
GICS_SECTORS = ["Energy", "Materials", "Industrials", "Consumer Discretionary", "Consumer Staples", "Health Care",
                "Financials", "Information Technology", "Communication Services", "Utilities", "Real Estate"]


def list_keys(s3, prefix):
    keys = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=prefix):
        keys += [o["Key"] for o in page.get("Contents", [])]
    return keys


def read_parquet(s3, key):
    return pd.read_parquet(io.BytesIO(s3.get_object(Bucket=BUCKET, Key=key)["Body"].read()))


def vals(df, col):
    if col not in df.columns:
        return []
    return sorted(set(df[col].dropna().astype(str)))


def main():
    s3 = boto3.client("s3", region_name="us-east-1")
    now = datetime.datetime.now(datetime.timezone.utc)
    chars = sorted(k for k in list_keys(s3, "bbg/") if k.endswith("/characteristics.parquet"))
    per_part = {}
    for k in chars:
        d = re.match(r"bbg/([^/]+)/", k).group(1)
        df = read_parquet(s3, k)
        per_part[d] = {"key": f"s3://{BUCKET}/{k}", "rows": len(df),
                       "has_sector_col": SECTOR_COL in df.columns, "has_industry_group_col": IG_COL in df.columns,
                       "sector_values": vals(df, SECTOR_COL), "industry_group_values": vals(df, IG_COL)}
    newest = max(per_part)
    nk = per_part[newest]["key"]
    cdf = read_parquet(s3, nk[len(f"s3://{BUCKET}/"):])
    char = {"key": nk, "rows": len(cdf), "sector_values": vals(cdf, SECTOR_COL),
            "industry_group_values": vals(cdf, IG_COL)}
    hk = max(k for k in list_keys(s3, "gold/holding/") if k.endswith("/holding.parquet"))
    hdf = read_parquet(s3, hk)
    served = {"key": f"s3://{BUCKET}/{hk}", "rows": len(hdf),
              "sector_values": vals(hdf, "sub_asset_class"), "industry_group_values": vals(hdf, "industry_group"),
              "sector_null": int(hdf["sub_asset_class"].isna().sum()),
              "industry_group_null": int(hdf["industry_group"].isna().sum()),
              "industry_group_basis_values": vals(hdf, "industry_group_basis"),
              "industry_group_basis_counts": {str(k): int(v) for k, v in
                                               hdf["industry_group_basis"].value_counts(dropna=False).items()}}
    union = {"partitions_read": len(per_part),
             "sector_values": sorted({v for p in per_part.values() for v in p["sector_values"]}),
             "industry_group_values": sorted({v for p in per_part.values() for v in p["industry_group_values"]})}
    # per-value first/last partition seen
    seen = {}
    for d in sorted(per_part):
        for kind in ("sector_values", "industry_group_values"):
            for v in per_part[d][kind]:
                seen.setdefault(kind, {}).setdefault(v, [d, d])[1] = d
    union["first_last_seen"] = seen
    cs, ci = set(char["sector_values"]), set(char["industry_group_values"])
    ss, si = set(served["sector_values"]), set(served["industry_group_values"])
    gs = set(GICS_SECTORS)
    us, ui = set(union["sector_values"]), set(union["industry_group_values"])
    diffs = {
        "sector": {
            "characteristics_not_in_served": sorted(cs - ss), "served_not_in_characteristics": sorted(ss - cs),
            "characteristics_not_in_producer_GICS_SECTORS": sorted(cs - gs),
            "producer_GICS_SECTORS_not_in_characteristics": sorted(gs - cs),
            "served_not_in_producer_GICS_SECTORS": sorted(ss - gs),
            "producer_GICS_SECTORS_not_in_served": sorted(gs - ss),
            "union_not_in_newest_characteristics": sorted(us - cs),
            "union_not_in_producer_GICS_SECTORS": sorted(us - gs),
        },
        "industry_group": {
            "characteristics_not_in_served": sorted(ci - si), "served_not_in_characteristics": sorted(si - ci),
            "union_not_in_newest_characteristics": sorted(ui - ci),
            "union_not_in_served": sorted(ui - si), "served_not_in_union": sorted(si - ui),
        },
    }
    doc = {"measured_at": now.isoformat(), "sources": {"characteristics": char, "served_holding": served},
           "union_over_partitions": union, "per_partition": per_part,
           "producer_vocab": {"GICS_SECTORS": GICS_SECTORS}, "diffs": diffs}
    out = os.path.join(OUT_DIR, f"SECTOR_INDUSTRY_GROUP_VALUES_{now.strftime('%Y%m%d')}.json")
    with open(out, "w", encoding="utf-8") as fh:
        json.dump(doc, fh, indent=2, sort_keys=True, ensure_ascii=True)
    print(f"wrote {out} partitions={len(per_part)} newest={newest} char_rows={char['rows']} served_rows={served['rows']}")
    print(json.dumps(diffs, indent=1))
    return 0


if __name__ == "__main__":
    sys.exit(main())
