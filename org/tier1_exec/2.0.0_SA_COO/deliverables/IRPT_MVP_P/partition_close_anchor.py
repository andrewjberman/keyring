#!/usr/bin/env python3
"""Which close does a holdings partition dated D hold -- D's own, or the prior trading day's? (CTO rulings batch 63 item 3(a))

    python partition_close_anchor.py <day> <prior trading day> [<day> <prior trading day> ...]

THE ANCHOR is the 49 Financial Schwab silver (schwab/08335338/silver/dim_position): its `closing_price` is the OWN-date close,
which this script re-reads each run from the column `secprice_lstupdte` (the price's own last-update date) rather than assuming.
For each day given, the securities whose Schwab close MOVED between the prior trading day and the day are the discriminating set.
A second source's partition for that day is then graded per security: equal to the own-date close, equal to the prior-day close,
or neither (relative 1e-4). Sources graded: Cottonwood's Black Diamond holdings (price = Market Value / Units, joined by CUSIP) and
Inflection's Orion positions (currentPrice, joined by ticker).

Why an anchor and not only a weekend test: the weekend test (does Saturday's partition repeat Friday's?) needs weekend
partitions, and neither the Schwab nor the Black Diamond silver has them. Read-only.
"""
from __future__ import annotations

import collections
import io
import sys

import boto3
import pyarrow.parquet as pq

BUCKET = "opal-data-assets"


def main() -> int:
    args = sys.argv[1:]
    if not args or len(args) % 2:
        print(__doc__)
        return 2
    pairs = list(zip(args[0::2], args[1::2]))
    s3 = boto3.client("s3", region_name="us-east-1")

    def table(prefix, day, cols):
        resp = s3.list_objects_v2(Bucket=BUCKET, Prefix="%sdate=%s/" % (prefix, day))
        keys = [o["Key"] for o in resp.get("Contents", []) if o["Key"].endswith(".parquet")]
        if not keys:
            return None
        return pq.read_table(io.BytesIO(s3.get_object(Bucket=BUCKET, Key=keys[0])["Body"].read()), columns=cols).to_pydict()

    def close(a, b):
        return abs(a - b) <= 1e-4 * max(abs(a), abs(b), 1e-9)

    schwab = {}
    for day in sorted({d for pair in pairs for d in pair}):
        t = table("schwab/08335338/silver/dim_position/", day, ["cusip", "ticker_symbol", "closing_price", "secprice_lstupdte"])
        if t is None:
            print("ERROR: the anchor has no partition for %s" % day)
            return 1
        by_cusip, by_ticker = {}, {}
        for c, tk, p in zip(t["cusip"], t["ticker_symbol"], t["closing_price"]):
            if p is None or float(p) <= 0:
                continue
            if c:
                by_cusip[c.strip()] = float(p)
            if tk:
                by_ticker[tk.strip().upper()] = float(p)
        updated = collections.Counter(str(x)[:10] for x in t["secprice_lstupdte"])
        print("anchor %s: %d rows; price last-update date equals the partition date on %d (own-date close)"
              % (day, len(t["closing_price"]), updated.get(day, 0)))
        schwab[day] = (by_cusip, by_ticker)

    def grade(name, prices, kind, day, prior):
        own, prev = schwab[day][kind], schwab[prior][kind]
        disc = [k for k in prices if k in own and k in prev and not close(own[k], prev[k])]
        m_own = sum(1 for k in disc if close(prices[k], own[k]))
        m_prev = sum(1 for k in disc if close(prices[k], prev[k]))
        print("  %-36s partition %s: %4d securities whose anchor close moved from %s | own-date close %4d | prior-day close %4d | neither %4d"
              % (name, day, len(disc), prior, m_own, m_prev, len(disc) - m_own - m_prev))

    for day, prior in pairs:
        t = table("blackdiamond/cottonwood/silver/fact_holdings/", day, ["CUSIP", "Market Value", "Units"])
        if t is None:
            print("  Cottonwood (Black Diamond): no partition for %s" % day)
        else:
            px = {}
            for c, mv, u in zip(t["CUSIP"], t["Market Value"], t["Units"]):
                try:
                    mv, u = float(mv), float(u)
                except (TypeError, ValueError):
                    continue
                if c and u > 0 and mv > 0:
                    px[c.strip()] = mv / u
            grade("Cottonwood (Black Diamond), by CUSIP", px, 0, day, prior)
        t = table("orion/inflection/silver/fact_positions/", day, ["ticker", "currentPrice"])
        if t is None:
            print("  Inflection (Orion): no partition for %s" % day)
        else:
            px = {}
            for tk, p in zip(t["ticker"], t["currentPrice"]):
                if tk and p is not None and float(p) > 0:
                    px[tk.strip().upper()] = float(p)
            grade("Inflection (Orion), by ticker", px, 1, day, prior)
    return 0


if __name__ == "__main__":
    sys.exit(main())
