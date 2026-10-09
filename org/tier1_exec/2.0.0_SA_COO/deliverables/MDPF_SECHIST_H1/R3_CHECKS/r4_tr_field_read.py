"""MDPF_SECHIST round 4, SH-t-8's take: the first SCHEDULED run with SH-t-8 at site Z carries the total-return level field.

Read only. Takes the newest s3://opal-data-etfs/bbg/<date>/run_manifest.json with as_of >= the floor and run_class "scheduled" whose
manifest carries `history_gap_fill` (the SH-t-8 marker), reads that partition's history_topup.parquet, and requires a non-null
TOT_RETURN_INDEX_GROSS_DVDS on at least one SALXX or FXFXX row.

Usage: python r4_tr_field_read.py [floor_yyyy-mm-dd]   (default 2026-10-09)
Last line: TRFIELD-READ-OK as_of=<d> rows=<n> nonnull=<k>   or   TRFIELD-READ-BAD <reason>.
"""
from __future__ import annotations

import io
import json
import sys

import boto3
import pandas as pd

BUCKET = "opal-data-etfs"
FIELD = "TOT_RETURN_INDEX_GROSS_DVDS"
MMF = ("SALXX", "FXFXX")


def main(argv: list[str]) -> int:
    floor = argv[1] if len(argv) > 1 else "2026-10-09"
    s3 = boto3.client("s3")
    dates = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix="bbg/", Delimiter="/"):
        for p in page.get("CommonPrefixes") or []:
            d = p["Prefix"][4:-1]
            if len(d) == 10 and d >= floor:
                dates.append(d)
    print("bbg/ date prefixes >= " + floor + ": " + str(len(dates)))
    for d in sorted(dates, reverse=True):
        try:
            m = json.loads(s3.get_object(Bucket=BUCKET, Key="bbg/" + d + "/run_manifest.json")["Body"].read())
        except s3.exceptions.NoSuchKey:
            continue
        if m.get("run_class") != "scheduled" or "history_gap_fill" not in m:
            print("skip " + d + " run_class=" + str(m.get("run_class")) + " sh_t8=" + str("history_gap_fill" in m))
            continue
        try:
            df = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=BUCKET, Key="bbg/" + d + "/history_topup.parquet")["Body"].read()))
        except s3.exceptions.NoSuchKey:
            print("TRFIELD-READ-BAD no-history_topup as_of=" + d)
            return 1
        if FIELD not in df.columns:
            print("TRFIELD-READ-BAD column-absent as_of=" + d)
            return 1
        sec = df[[c for c in df.columns if c.lower() in ("security", "ticker")][0]].astype(str)
        mmf = df[sec.str.split(" ").str[0].isin(MMF)]
        nonnull = int(mmf[FIELD].notna().sum())
        print("as_of=" + d + " mmf_rows=" + str(len(mmf)) + " nonnull=" + str(nonnull))
        if nonnull < 1:
            print("TRFIELD-READ-BAD all-null as_of=" + d)
            return 1
        print("TRFIELD-READ-OK as_of=" + d + " rows=" + str(len(mmf)) + " nonnull=" + str(nonnull))
        return 0
    print("TRFIELD-READ-BAD no-scheduled-sh-t8-manifest-since " + floor)
    return 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
