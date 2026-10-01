#!/usr/bin/env python3
"""Which close does EACH trading-day partition of a source hold? Every day of a range, graded against the Schwab own-date closes.

    python partition_close_anchor_sweep.py <first trading day> <last trading day> [--source orion|blackdiamond]

WHY THIS EXISTS BESIDE THE OTHER TWO INSTRUMENTS (1.0.0_SA_CTO rulings batch 63 items 2-3; row IRPT_BCKEND-S245).
`partition_close_history_sweep.py` reads weekend and holiday pairs, so it sees a Monday and is blind to Tuesday through Friday;
`partition_close_anchor.py` grades the days it is given. The week of 2026-07-13 showed what falls between them: three weekday
partitions on the own-date basis and one holding no single close, inside a stretch every sampled day read as prior-day. A basis
declared for a span is MEASURED only when every trading-day partition in the span was graded; this grades every one.

THE ANCHOR is the 49 Financial Schwab silver (schwab/08335338/silver/dim_position, `closing_price`), an own-date close: the share
of rows whose `secprice_lstupdte` equals the partition date is printed for the range (minimum over the days read). For trading
day D with prior trading day P and the one before it PP, the DISCRIMINATING securities are those whose anchor close differs
between D and P (relative 1e-4). The source's partition dated D is graded per discriminating security: equal to the close of D
(own), of P (prior), of PP (two back, counted only when it is neither of the first two), or none. The partition reads

    OWN_DATE            at least 95 percent equal D's close
    PRIOR_TRADING_DAY   at least 95 percent equal P's close
    NO_SINGLE_CLOSE     neither share reaches 95 percent
    ABSENT              the source has no partition dated D
    NO-ANCHOR           the anchor lacks D or P (nothing can be said; never read as a basis)

Printed: one line per trading day, the class census with its denominator, and the runs of one class with their date ranges.
Reads only (S3 list and get).
"""
from __future__ import annotations

import collections
import io
import sys
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import boto3
import pyarrow.parquet as pq
from botocore.config import Config

sys.path.insert(0, str(Path(__file__).resolve().parents[5] / "lib"))
import trading_calendar as tc  # noqa: E402

BUCKET = "opal-data-assets"
ANCHOR = "schwab/08335338/silver/dim_position/"
SOURCES = {
    "orion": ("orion/inflection/silver/fact_positions/", ["ticker", "currentPrice"], "ticker"),
    "blackdiamond": ("blackdiamond/cottonwood/silver/fact_holdings/", ["CUSIP", "Market Value", "Units"], "cusip"),
}
SHARE = 0.95


def same(a, b):
    return abs(a - b) <= 1e-4 * max(abs(a), abs(b), 1e-9)


def classify(n, own, prior):
    """The class of one graded partition: n discriminating securities, of which `own` and `prior` matched."""
    if n == 0:
        return "NO-ANCHOR"
    if own >= SHARE * n:
        return "OWN_DATE"
    if prior >= SHARE * n:
        return "PRIOR_TRADING_DAY"
    return "NO_SINGLE_CLOSE"


def self_test():
    assert classify(156, 156, 0) == "OWN_DATE" and classify(159, 156, 3) == "OWN_DATE"
    assert classify(152, 0, 152) == "PRIOR_TRADING_DAY" and classify(128, 0, 127) == "PRIOR_TRADING_DAY"
    assert classify(156, 0, 39) == "NO_SINGLE_CLOSE" and classify(0, 0, 0) == "NO-ANCHOR"
    assert same(10.0, 10.0005) and not same(10.0, 10.01)
    print("self-test: 8 of 8")


def main() -> int:
    args = sys.argv[1:]
    if args == ["--self-test"]:
        self_test()
        return 0
    source = "orion"
    if "--source" in args:
        i = args.index("--source")
        source = args[i + 1]
        del args[i:i + 2]
    if len(args) != 2 or source not in SOURCES:
        print(__doc__)
        return 2
    prefix, cols, kind = SOURCES[source]
    days = [d for d in tc.trading_days_between(args[0], args[1])]
    need = sorted({x for d in days for x in (d, tc.prev_trading_day(d), tc.prev_trading_day(tc.prev_trading_day(d)))})
    s3 = boto3.client("s3", region_name="us-east-1",
                      config=Config(retries={"max_attempts": 8, "mode": "standard"}, read_timeout=120, max_pool_connections=16))

    def table(pfx, day, columns):
        for attempt in range(4):
            try:
                resp = s3.list_objects_v2(Bucket=BUCKET, Prefix="%sdate=%s/" % (pfx, day))
                keys = sorted(o["Key"] for o in resp.get("Contents", []) if o["Key"].endswith(".parquet"))
                if not keys:
                    return None
                out = collections.defaultdict(list)
                for k in keys:
                    t = pq.read_table(io.BytesIO(s3.get_object(Bucket=BUCKET, Key=k)["Body"].read()), columns=columns).to_pydict()
                    for c in columns:
                        out[c] += t[c]
                return out
            except Exception:  # a body read that timed out: re-read the whole partition, never grade a part
                if attempt == 3:
                    raise
        return None

    def anchor(day):
        t = table(ANCHOR, day, ["cusip", "ticker_symbol", "closing_price", "secprice_lstupdte"])
        if t is None:
            return day, None
        by = {}
        for c, tk, p in zip(t["cusip"], t["ticker_symbol"], t["closing_price"]):
            if p is None or float(p) <= 0:
                continue
            key = (c or "").strip() if kind == "cusip" else (tk or "").strip().upper()
            if key:
                by[key] = float(p)
        fresh = sum(1 for x in t["secprice_lstupdte"] if str(x)[:10] == str(day))
        return day, (by, fresh, len(t["closing_price"]))

    def graded(day):
        t = table(prefix, day, cols)
        if t is None:
            return day, None
        px = {}
        if source == "orion":
            for tk, p in zip(t["ticker"], t["currentPrice"]):
                if tk and p is not None and float(p) > 0:
                    px[tk.strip().upper()] = float(p)
        else:
            for c, mv, u in zip(t["CUSIP"], t["Market Value"], t["Units"]):
                try:
                    mv, u = float(mv), float(u)
                except (TypeError, ValueError):
                    continue
                if c and u > 0 and mv > 0:
                    px[c.strip()] = mv / u
        return day, px

    with ThreadPoolExecutor(8) as pool:
        anchors = dict(pool.map(anchor, need))
        prices = dict(pool.map(graded, days))
    shares = [a[1] / a[2] for a in anchors.values() if a and a[2]]
    print("source %s (%s); anchor %s; calendar %s" % (source, prefix, ANCHOR, tc.calendar_source()))
    print("trading days in range %d (%s .. %s); anchor partitions read %d of %d needed; anchor rows whose price last-update date "
          "equals the partition date: minimum %.3f%% over the days read"
          % (len(days), days[0], days[-1], sum(1 for a in anchors.values() if a), len(need), 100 * min(shares) if shares else 0.0))
    rows = []
    for d in days:
        p = tc.prev_trading_day(d)
        pp = tc.prev_trading_day(p)
        if prices[d] is None:
            rows.append((d, "ABSENT", 0, 0, 0, 0))
            continue
        if not anchors.get(d) or not anchors.get(p):
            rows.append((d, "NO-ANCHOR", 0, 0, 0, 0))
            continue
        own, prev = anchors[d][0], anchors[p][0]
        back = anchors[pp][0] if anchors.get(pp) else {}
        disc = [k for k in prices[d] if k in own and k in prev and not same(own[k], prev[k])]
        n_own = sum(1 for k in disc if same(prices[d][k], own[k]))
        n_prior = sum(1 for k in disc if same(prices[d][k], prev[k]))
        n_back = sum(1 for k in disc if k in back and same(prices[d][k], back[k])
                     and not same(prices[d][k], own[k]) and not same(prices[d][k], prev[k]))
        rows.append((d, classify(len(disc), n_own, n_prior), len(disc), n_own, n_prior, n_back))
    for d, cls, n, n_own, n_prior, n_back in rows:
        print("  %s %s  %-18s discriminating %4d | own-date %4d | prior-day %4d | two back %4d | none %4d"
              % (d.strftime("%a"), d, cls, n, n_own, n_prior, n_back, n - n_own - n_prior - n_back))
    census = collections.Counter(r[1] for r in rows)
    print("class census over %d trading day(s): %s" % (len(rows), dict(sorted(census.items()))))
    runs = []
    for d, cls, *_ in rows:
        if runs and runs[-1][0] == cls:
            runs[-1][2], runs[-1][3] = d, runs[-1][3] + 1
        else:
            runs.append([cls, d, d, 1])
    print("runs (%d):" % len(runs))
    for cls, a, b, n in runs:
        print("  %-18s %s .. %s  %4d day(s)" % (cls, a, b, n))
    return 0


if __name__ == "__main__":
    sys.exit(main())
