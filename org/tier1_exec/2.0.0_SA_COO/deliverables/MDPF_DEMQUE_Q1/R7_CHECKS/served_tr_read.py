"""MDPF_DEMQUE round 7 carried read (issuer's real run of DQ-t-21's served write): after the scheduled daily draw, read the SERVED price
store (price_store.s3_root(), read-only) and report, per CUSIP in the index, whether prices.parquet carries the four total-return columns
after the three original ones, how many rows carry a total_return, their tr_source split, and any flags. Prints the index's as_of and
written time so a read before the draw says so. SERVED-TR-OK when at least one CUSIP's prices.parquet has
[date, close_served, as_traded_close, cash, total_return, tr_source, flags] in that order and every money-market symbol in
money_market.csv present in the store has no row sourced "yahoo"; SERVED-TR-NOT-YET when every file still has the three original
columns only; else SERVED-TR-BAD <reason>.
"""
from __future__ import annotations

import csv
import io
import os
import sys

import boto3
import pandas as pd

HERE = os.path.join("data", "mdpf", "scripts", "demque")
sys.path.insert(0, ".")
sys.path.insert(0, HERE)
import price_store  # noqa: E402

ORIG = ["date", "close_served", "as_traded_close"]
FULL = ORIG + ["cash", "total_return", "tr_source", "flags"]


def _get(s3, bucket, key) -> bytes:
    return s3.get_object(Bucket=bucket, Key=key)["Body"].read()


if __name__ == "__main__":
    root = price_store.s3_root()
    bucket, _, prefix = root[5:].partition("/")
    s3 = boto3.client("s3")
    idx = pd.read_parquet(io.BytesIO(_get(s3, bucket, prefix + "/index/index.parquet")))
    head = s3.head_object(Bucket=bucket, Key=prefix + "/index/index.parquet")
    print("index rows=%d as_of=%s written=%s" % (len(idx), sorted(set(map(str, idx.get("as_of", []))))[-1:],
                                                 head["LastModified"].isoformat()))
    with open(os.path.join(HERE, "money_market.csv"), encoding="utf-8") as fh:
        mm = {r["symbol"] for r in csv.DictReader(fh)}
    full, orig, other, mm_bad = 0, 0, [], []
    for _, row in idx.iterrows():
        key = "%s/cusip=%s/prices.parquet" % (prefix, row["cusip"])
        try:
            df = pd.read_parquet(io.BytesIO(_get(s3, bucket, key)))
        except Exception as exc:  # a missing object is a finding, not a skip
            other.append("%s unreadable: %s" % (row["cusip"], exc))
            continue
        cols = list(df.columns)
        if cols == FULL:
            full += 1
            if row.get("yahoo_symbol") in mm and (df["tr_source"] == "yahoo").any():
                mm_bad.append(str(row.get("yahoo_symbol")))
        elif cols == ORIG:
            orig += 1
        else:
            other.append("%s columns %s" % (row["cusip"], cols))
    print("prices.parquet: %d with the 7 columns, %d with the original 3, %d other" % (full, orig, len(other)))
    for o in other[:10]:
        print("  " + o)
    if other or mm_bad:
        print("SERVED-TR-BAD other=%d money_market_from_yahoo=%s" % (len(other), mm_bad))
        sys.exit(1)
    if full == 0:
        print("SERVED-TR-NOT-YET %d of %d files still carry the original 3 columns" % (orig, len(idx)))
        sys.exit(2)
    print("SERVED-TR-OK %d of %d files carry the 4 total-return columns after the original 3" % (full, len(idx)))
    sys.exit(0)
