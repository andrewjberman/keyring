"""CTO batch 63 item 3(a): which close does a positions partition dated D hold? Consecutive-partition price comparison.

Usage: python seam.py <bucket> <prefix> <key col,key col> <price col> <value col or -> <first date> <last date>

For every pair of consecutive calendar-day partitions in [first, last]: the keys present in both with a positive price in both, how
many carry the SAME price, and each partition's total value. A partition that repeats the one before it (100 percent unchanged)
holds the same close. Under an own-date basis the Friday-to-Saturday pair is unchanged and Sunday-to-Monday changes; under a
prior-trading-day basis Friday-to-Saturday CHANGES (Saturday is the first to hold Friday's close) and Sunday-to-Monday is unchanged.
The seam is the weekday whose partition repeats the previous weekday's. Read-only; an absent partition is printed as ABSENT.
"""
from __future__ import annotations

import datetime as dt
import io
import sys

import boto3
import pyarrow.parquet as pq


def main() -> None:
    bucket, prefix, keycols, pricecol, valuecol, first, last = sys.argv[1:8]
    keys = keycols.split(",")
    s3 = boto3.client("s3", region_name="us-east-1")

    def load(day):
        resp = s3.list_objects_v2(Bucket=bucket, Prefix="%sdate=%s/" % (prefix, day))
        objs = [o["Key"] for o in resp.get("Contents", []) if o["Key"].endswith(".parquet")]
        if not objs:
            return None
        cols = keys + [pricecol] + ([valuecol] if valuecol != "-" else [])
        prices, total, rows = {}, 0.0, 0
        for k in objs:
            t = pq.read_table(io.BytesIO(s3.get_object(Bucket=bucket, Key=k)["Body"].read()), columns=cols).to_pydict()
            n = len(t[pricecol])
            rows += n
            for i in range(n):
                p = t[pricecol][i]
                if valuecol != "-" and t[valuecol][i] is not None:
                    total += float(t[valuecol][i])
                if p is None:
                    continue
                prices[tuple(t[c][i] for c in keys)] = float(p)
        return prices, total, rows

    d0 = dt.date.fromisoformat(first)
    d1 = dt.date.fromisoformat(last)
    days = [d0 + dt.timedelta(days=i) for i in range((d1 - d0).days + 1)]
    data = {d: load(d.isoformat()) for d in days}
    print("%s/%s  keys %s  price %s" % (bucket, prefix, keys, pricecol))
    for a, b in zip(days, days[1:]):
        if data[a] is None or data[b] is None:
            print("  %s %s -> %s %s  %s" % (a.strftime("%a"), a, b.strftime("%a"), b,
                                            "ABSENT: " + ", ".join(str(x) for x in (a, b) if data[x] is None)))
            continue
        pa, pb = data[a][0], data[b][0]
        both = [k for k in pa if k in pb and pa[k] > 0 and pb[k] > 0]
        same = sum(1 for k in both if pa[k] == pb[k])
        pct = 100.0 * same / len(both) if both else float("nan")
        print("  %s %s -> %s %s  unchanged %6d of %6d (%5.1f%%)  rows %d -> %d  total value %s -> %s" % (
            a.strftime("%a"), a, b.strftime("%a"), b, same, len(both), pct, data[a][2], data[b][2],
            ("%.2f" % data[a][1]) if valuecol != "-" else "-", ("%.2f" % data[b][1]) if valuecol != "-" else "-"))


if __name__ == "__main__":
    main()
