#!/usr/bin/env python3
"""Which close does a partition dated D hold, over a source's WHOLE history? (CTO rulings batch 63 items 2-3; row IRPT_BCKEND-S245)

    python partition_close_history_sweep.py <bucket> <prefix> <key col,key col> <price col> [<first date> <last date>]

`partition_close_consecutive.py` reads a few days around a seam; this reads every DISCRIMINATING pair of consecutive calendar-day
partitions a source has, so a declared `partition_close` basis rests on the history and not on a sample, and a second seam nobody
looked for would show. A pair (D-1, D) discriminates when exactly one of the two days is a trading day:

  D is the first non-trading day after a trading day (a Saturday, a holiday):
      OWN_DATE          -> D repeats D-1 (no new close exists)        -> unchanged
      PRIOR_TRADING_DAY -> D is the first to hold D-1's close         -> changed
  D is the first trading day after a non-trading day (a Monday):
      OWN_DATE          -> D holds its own new close                  -> changed
      PRIOR_TRADING_DAY -> D repeats the weekend (still Friday's)     -> unchanged

"unchanged" = of the keys with a positive price in both partitions, the share carrying the same price: at least 99 percent reads as
a repeat, under 90 percent as a new close, between the two as AMBIGUOUS (printed, never classified). A pair with no priced key in
both is NO-PRICES; a pair missing a partition is ABSENT. Printed: the count per class, the runs of one basis with their date
ranges, and every pair that is not the basis of the run around it. The day axis is lib/trading_calendar.py. Read-only.
"""
from __future__ import annotations

import collections
import datetime as dt
import io
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import boto3
import pyarrow.parquet as pq
from botocore.config import Config

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "lib"))
import trading_calendar as tc  # noqa: E402

REPEAT, NEW_CLOSE = 0.99, 0.90


def classify(first_is_trading, unchanged_share):
    """The basis one discriminating pair shows. `first_is_trading`: D-1 is the trading day of the pair."""
    if unchanged_share is None:
        return "NO-PRICES"
    if unchanged_share >= REPEAT:
        return "OWN_DATE" if first_is_trading else "PRIOR_TRADING_DAY"
    if unchanged_share < NEW_CLOSE:
        return "PRIOR_TRADING_DAY" if first_is_trading else "OWN_DATE"
    return "AMBIGUOUS"


def self_test():
    assert classify(True, 1.0) == "OWN_DATE" and classify(True, 0.07) == "PRIOR_TRADING_DAY"
    assert classify(False, 1.0) == "PRIOR_TRADING_DAY" and classify(False, 0.09) == "OWN_DATE"
    assert classify(True, 0.95) == "AMBIGUOUS" and classify(False, None) == "NO-PRICES"
    print("self-test: 6 of 6")


def main() -> int:
    if sys.argv[1:] == ["--self-test"]:
        self_test()
        return 0
    if len(sys.argv) not in (5, 7):
        print(__doc__)
        return 2
    bucket, prefix, keycols, pricecol = sys.argv[1:5]
    keys = keycols.split(",")
    # A read that times out is retried by the client; a pair is never graded on a partial read (a failed read raises).
    s3 = boto3.client("s3", region_name="us-east-1",
                      config=Config(retries={"max_attempts": 8, "mode": "standard"}, read_timeout=120, max_pool_connections=16))
    listed = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=prefix, Delimiter="/"):
        for child in page.get("CommonPrefixes", []):
            token = child["Prefix"][len(prefix):].rstrip("/")
            if token.startswith("date="):
                listed.append(dt.date.fromisoformat(token[5:15]))
    have = set(listed)
    first = dt.date.fromisoformat(sys.argv[5]) if len(sys.argv) == 7 else min(have)
    last = dt.date.fromisoformat(sys.argv[6]) if len(sys.argv) == 7 else max(have)
    span = [first + dt.timedelta(days=i) for i in range((last - first).days + 1)]
    trading = {d: tc.is_trading_day(d) for d in [first - dt.timedelta(days=1)] + span}
    pairs = [(d - dt.timedelta(days=1), d) for d in span[1:] if trading[d] != trading[d - dt.timedelta(days=1)]]
    print("%s/%s  keys %s  price %s  calendar %s" % (bucket, prefix, keys, pricecol, tc.calendar_source()))
    print("partitions listed %d (%s .. %s); swept %s .. %s; discriminating pairs %d of %d consecutive calendar-day pairs"
          % (len(have), min(have), max(have), first, last, len(pairs), len(span) - 1))

    def load(day):
        resp = s3.list_objects_v2(Bucket=bucket, Prefix="%sdate=%s/" % (prefix, day))
        objs = [o["Key"] for o in resp.get("Contents", []) if o["Key"].endswith(".parquet")]
        prices = {}
        for k in objs:
            t = pq.read_table(io.BytesIO(s3.get_object(Bucket=bucket, Key=k)["Body"].read()), columns=keys + [pricecol]).to_pydict()
            for i, p in enumerate(t[pricecol]):
                if p is not None and float(p) > 0:
                    prices[tuple(t[c][i] for c in keys)] = float(p)
        return prices

    def grade(pair):
        a, b = pair
        if a not in have or b not in have:
            return pair, "ABSENT", None, 0
        for attempt in range(4):
            try:
                pa, pb = load(a), load(b)
                break
            except Exception:  # a body read that timed out mid-stream: re-read the pair, never grade a part
                if attempt == 3:
                    raise
        both = [k for k in pa if k in pb]
        share = (sum(1 for k in both if pa[k] == pb[k]) / len(both)) if both else None
        return pair, classify(trading[a], share), share, len(both)

    with ThreadPoolExecutor(8) as pool:
        graded = list(pool.map(grade, pairs))
    census = collections.Counter(g[1] for g in graded)
    print("class census over %d pairs: %s" % (len(graded), dict(sorted(census.items()))))
    runs = []
    for (a, b), cls, share, n in graded:
        if cls not in ("OWN_DATE", "PRIOR_TRADING_DAY"):
            continue
        if runs and runs[-1][0] == cls:
            runs[-1][2], runs[-1][3] = b, runs[-1][3] + 1
        else:
            runs.append([cls, b, b, 1])
    print("runs of one basis, by the pair's second partition date (%d run(s)):" % len(runs))
    for cls, start, end, n in runs:
        print("  %-18s %s .. %s  %4d pair(s)" % (cls, start, end, n))
    odd = [g for g in graded if g[1] not in ("OWN_DATE", "PRIOR_TRADING_DAY")]
    print("pairs with no basis reading: %d" % len(odd))
    by_cls = collections.defaultdict(list)
    for (a, b), cls, share, n in odd:
        by_cls[cls].append((a, b, share, n))
    for cls, rows in sorted(by_cls.items()):
        print("  %s: %d pair(s), %s .. %s" % (cls, len(rows), rows[0][1], rows[-1][1]))
        for a, b, share, n in (rows if cls == "AMBIGUOUS" else rows[:3] + rows[-3:] if len(rows) > 6 else rows):
            print("     %s %s -> %s %s  unchanged %s of %d keys priced in both"
                  % (a.strftime("%a"), a, b.strftime("%a"), b, ("%.1f%%" % (100 * share)) if share is not None else "-", n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
