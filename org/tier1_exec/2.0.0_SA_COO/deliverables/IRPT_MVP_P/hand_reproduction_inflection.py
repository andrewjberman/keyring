#!/usr/bin/env python3
"""One Inflection account's holdings return reproduced BY HAND from the two silver partitions that hold each close, and compared
with the rebuilt gold row (1.0.0_SA_CTO rulings batch 63 item 3(d); batch 80 item 7: one reproduction spans a gap).

    python hand_reproduction_inflection.py [<account id>]

INDEPENDENT OF THE PRODUCER: this file imports none of its code and does not read sources.json. The partition that holds each
close is written out below by hand, from the measured record (HOLDINGS_SOURCE_DATE_BASIS_READ_20261001.md), so a wrong
declaration and a wrong hand table cannot agree by sharing a line of code.

THE METHOD, restated from the PRD (v0.19 rulings 2-5, v0.20 rulings 13-16), for one account and one row:
    for every holding at the START close (keyed by ticker; value = currentValue, price = currentPrice):
        in the basket if it is custodial cash, or it has a positive price at BOTH closes; and its value is not negative
        contribution = value_start * (price_end / price_start - 1)       (zero for an unpriced cash line)
    return = sum(contributions) / sum(value_start over the basket)
No flow term. The end price of a security is its price in the END partition on any account.

THE THREE REPRODUCTIONS
  1. BEFORE THE SEAM  2026-04-30: own-date partitions, start close in date=2026-04-29, end close in date=2026-04-30.
  2. THE SEAM DAY     2026-05-05: start close (Mon 05-04) in date=2026-05-04, its own partition; end close (Tue 05-05) in
                      date=2026-05-06, the first partition on the prior-day basis that holds it.
  3. A WINDOW ACROSS A GAP  2026-05-07 .. 2026-05-13: four rows. Monday 05-11's close is in no partition (date=2026-05-12 holds no
                      single close), so 05-11 has no row and 05-12 is ONE row from Friday's close (date=2026-05-11) to Tuesday's
                      (date=2026-05-13), span 2. The window's return is the product of the four rows.
Reads only.
"""
from __future__ import annotations

import io
import json
import sys

import boto3
import pyarrow.parquet as pq

SILVER = ("opal-data-assets", "orion/inflection/silver/fact_positions/date=%s/data.parquet")
GOLD = ("opal-data-inflection", "irpt/inflection/gold/holdings_performance_daily/date=%s/data.parquet")
MANIFEST = ("opal-data-inflection", "irpt/inflection/gold/holdings_performance_manifest/date=%s/manifest.json")

# (label, gold row date, start close day, partition holding the start close, partition holding the end close, span)
ROWS = [
    ("1 before the seam", "2026-04-30", "2026-04-29", "2026-04-29", "2026-04-30", 1),
    ("2 the seam day", "2026-05-05", "2026-05-04", "2026-05-04", "2026-05-06", 1),
    ("3 window: Thu", "2026-05-07", "2026-05-06", "2026-05-07", "2026-05-08", 1),
    ("3 window: Fri", "2026-05-08", "2026-05-07", "2026-05-08", "2026-05-11", 1),
    ("3 window: Tue, LINKED over Mon", "2026-05-12", "2026-05-08", "2026-05-11", "2026-05-13", 2),
    ("3 window: Wed", "2026-05-13", "2026-05-12", "2026-05-13", "2026-05-14", 1),
]
WINDOW = ["2026-05-07", "2026-05-08", "2026-05-12", "2026-05-13"]

s3 = boto3.client("s3", region_name="us-east-1")
_cache = {}


def table(spec, day):
    key = spec[1] % day
    if key not in _cache:
        for attempt in range(4):
            try:
                _cache[key] = pq.read_table(io.BytesIO(s3.get_object(Bucket=spec[0], Key=key)["Body"].read())).to_pylist()
                break
            except s3.exceptions.NoSuchKey:
                _cache[key] = None
                break
            except Exception:
                if attempt == 3:
                    raise
    return _cache[key]


def by_hand(account, start_part, end_part, show):
    start = [r for r in table(SILVER, start_part) if str(r["accountId"]) == account]
    end_price = {}
    for r in table(SILVER, end_part):
        tk = (r["ticker"] or "").strip()
        if tk and tk not in end_price:
            end_price[tk] = r["currentPrice"]
    holdings = {}
    for r in start:
        tk = (r["ticker"] or "").strip() or (r["name"] or "").strip()
        h = holdings.setdefault(tk, {"value": 0.0, "price": r["currentPrice"], "cash": False})
        h["value"] += float(r["currentValue"] or 0.0)
        h["cash"] = h["cash"] or bool(r["isCustodialCash"])
    num = den = 0.0
    n_in = n_out = 0
    for tk in sorted(holdings):
        h = holdings[tk]
        p0, p1 = h["price"], end_price.get(tk)
        priced = bool(p0 and p0 > 0 and p1 and p1 > 0)
        member = (h["cash"] or priced) and h["value"] >= 0
        contrib = h["value"] * (p1 / p0 - 1.0) if (member and priced and h["value"] > 0) else 0.0
        if member:
            num, den, n_in = num + contrib, den + h["value"], n_in + 1
        else:
            n_out += 1
        if show and (member or h["value"] != 0.0):
            print("      %-16s value %14.2f  price %10.4f -> %10s  %s  contribution %12.4f"
                  % (tk[:16], h["value"], p0 or 0.0, ("%.4f" % p1) if p1 else "-", "cash  " if h["cash"] else ("basket" if member else "OUT   "), contrib))
    return (num / den if den > 0 else None), den, n_in, n_out


def gold_row(account, day):
    rows = table(GOLD, day)
    if rows is None:
        return None
    hit = [r for r in rows if str(r["account_id"]) == account]
    return hit[0] if hit else None


def pick_account():
    """The lowest account id that is OK on every reproduced day and holds 4 to 9 basket lines on the first of them."""
    need = [r[1] for r in ROWS]
    ok = None
    for day in need:
        ids = {str(r["account_id"]) for r in table(GOLD, day) if r["status"] == "OK"}
        ok = ids if ok is None else ok & ids
    first = {str(r["account_id"]): r["included_count"] for r in table(GOLD, need[0])}
    fit = sorted((a for a in ok if 4 <= first.get(a, 0) <= 9), key=lambda a: (len(a), a))
    print("accounts OK on all %d reproduced days: %d; of those with 4 to 9 basket lines on %s: %d" % (len(need), len(ok), need[0], len(fit)))
    return fit[0]


def main() -> int:
    account = sys.argv[1] if len(sys.argv) > 1 else pick_account()
    print("account %s (the Orion accountId as the gold carries it)" % account)
    results, chain_hand, chain_gold = [], 1.0, 1.0
    for label, day, start_day, start_part, end_part, span in ROWS:
        print("== %s | gold row %s | start close %s read from date=%s | end close read from date=%s" % (label, day, start_day, start_part, end_part))
        hand, den, n_in, n_out = by_hand(account, start_part, end_part, show=True)
        g = gold_row(account, day)
        man = json.loads(s3.get_object(Bucket=MANIFEST[0], Key=MANIFEST[1] % day)["Body"].read())
        read = man.get("partitions_read") or {}
        same = (g is not None and hand is not None and abs(hand - g["daily_return"]) <= 1e-12 and abs(den - g["account_value"]) <= 1e-6
                and g["prior_business_date"] == start_day and int(g["span_trading_days"]) == span and int(g["included_count"]) == n_in)
        print("   BY HAND  return %.12f  basket %.2f  lines in %d out %d" % (hand, den, n_in, n_out))
        print("   GOLD     return %.12f  basket %.2f  lines in %d  status %s  prior_business_date %s  span %s  (manifest: read date=%s and date=%s)"
              % (g["daily_return"], g["account_value"], g["included_count"], g["status"], g["prior_business_date"], g["span_trading_days"],
                 (read.get("prior_close") or {}).get("partition"), (read.get("day_close") or {}).get("partition")))
        print("   EQUAL to 1e-12, same start close, same span, same line count: %s" % same)
        results.append(same)
        if day in WINDOW:
            chain_hand *= 1.0 + hand
            chain_gold *= 1.0 + g["daily_return"]
    gap = gold_row(account, "2026-05-11")
    print("== 3 the window 2026-05-07 .. 2026-05-13: gold row for the gap day 2026-05-11: %s"
          % ("no row from this rebuild; a STALE row of the 2026-09-29 build (schema %s) is still in that partition and is NOT part "
             "of this window's product -- its disposition is the rebuild ledger's leg V1" % gap.get("schema_version")
             if gap is not None and str(gap.get("schema_version")) != "1.2"
             else "none" if gap is None else "PRESENT at schema %s" % gap.get("schema_version")))
    print("   window return BY HAND %.12f | product of the four gold rows %.12f | equal to 1e-12: %s"
          % (chain_hand - 1.0, chain_gold - 1.0, abs(chain_hand - chain_gold) <= 1e-12))
    ok = all(results) and abs(chain_hand - chain_gold) <= 1e-12
    print("RESULT: %d of %d rows equal; window equal %s" % (sum(results), len(results), abs(chain_hand - chain_gold) <= 1e-12))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
