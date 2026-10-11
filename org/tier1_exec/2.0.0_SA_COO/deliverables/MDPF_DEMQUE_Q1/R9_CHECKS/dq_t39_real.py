"""MDPF_DEMQUE round 9, DQ-t-39 criterion AC2 (REAL served bytes, S3 read only; the write goes to a LOCAL scratch root): take one real served
name (the first CUSIP of the store holding a prices.parquet and a lock.json), copy its four files to a scratch root, then call
`price_store.write(scratch, lock_row, result)` twice with a result built from the served prices:
(a) the stored splits PLUS one split row dated after the stored end -> `written` False, a reason naming "split", and every scratch file
byte-identical to the served copy; (b) the stored splits unchanged and one extra price row dated after the stored end -> `written` True,
the scratch prices.parquet max(date) advanced to that row. SPLIT-REAL-OK; else SPLIT-REAL-BAD <why>.
"""
from __future__ import annotations

import hashlib
import json
import os
import sys
import tempfile
from urllib.parse import urlparse

sys.path.insert(0, ".")
sys.path.insert(0, os.path.join("data", "mdpf", "scripts", "demque"))


def _bad(why):
    print("SPLIT-REAL-BAD " + why)
    return 1


def main() -> int:
    import boto3
    import pandas as pd
    import price_store as ps
    import yahoo_pull as yp
    from lib.opal_naming import address
    p = urlparse(address("yahoo", "global", "silver", "price_history", "x").rsplit("/", 1)[0])
    bucket, prefix = p.netloc, p.path.strip("/") + "/"
    s3 = boto3.client("s3")
    pick = None
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=prefix, Delimiter="/"):
        for cp in page.get("CommonPrefixes", []):
            if cp["Prefix"][len(prefix):].startswith("cusip="):
                pick = cp["Prefix"]
                break
        if pick:
            break
    if not pick:
        return _bad("no cusip prefix in the store")
    cusip = pick[len(prefix):].strip("/")[len("cusip="):]
    tmp = tempfile.mkdtemp(prefix="split_hold_")
    base = os.path.join(tmp, "cusip=" + cusip)
    os.makedirs(base)
    names = ("prices.parquet", "splits.parquet", "dividends.parquet", "lock.json")
    for n in names:
        body = s3.get_object(Bucket=bucket, Key=pick + n)["Body"].read()
        with open(os.path.join(base, n), "wb") as fh:
            fh.write(body)
    h0 = {n: hashlib.sha256(open(os.path.join(base, n), "rb").read()).hexdigest() for n in names}
    lock_row = json.load(open(os.path.join(base, "lock.json"), encoding="utf-8"))
    px = pd.read_parquet(os.path.join(base, "prices.parquet"))
    sp = pd.read_parquet(os.path.join(base, "splits.parquet"))
    dv = pd.read_parquet(os.path.join(base, "dividends.parquet"))
    end = pd.to_datetime(px["date"]).max()
    new_day = end + pd.Timedelta(days=3)
    lock_row = dict(lock_row, valid_to=new_day.date().isoformat(), state="LOCKED")

    def result(prices, splits):
        last = prices.iloc[-1]
        extra = pd.DataFrame({"date": [new_day], "close_served": [float(last["close_served"])], "as_traded_close": [float(last["as_traded_close"])]})
        pr = pd.concat([prices[["date", "close_served", "as_traded_close"]], extra], ignore_index=True)
        return yp.PullResult(symbol=lock_row.get("yahoo_symbol") or "X", status="OK", http_status=200, prices=pr, splits=splits,
                             dividends=dv[["date", "amount"]] if len(dv) and "amount" in dv.columns else yp._empty_divs(), cells=len(pr))

    gain = pd.concat([sp[["date", "ratio"]], pd.DataFrame({"date": [new_day], "ratio": [2.0]})], ignore_index=True)
    out_a = ps.write(tmp, lock_row, result(px, gain))
    h1 = {n: hashlib.sha256(open(os.path.join(base, n), "rb").read()).hexdigest() for n in names}
    print("a: %s identical=%s" % (json.dumps(out_a, default=str)[:200], h1 == h0))
    out_b = ps.write(tmp, lock_row, result(px, sp[["date", "ratio"]]))
    px2 = pd.read_parquet(os.path.join(base, "prices.parquet"))
    print("b: %s max_date=%s" % (json.dumps(out_b, default=str)[:160], pd.to_datetime(px2["date"]).max().date()))
    arms = {
        "a_not_written": out_a.get("written") is False and "split" in str(out_a.get("reason")).lower(),
        "a_bytes_identical": h1 == h0,
        "b_written": out_b.get("written") is True,
        "b_advanced": pd.to_datetime(px2["date"]).max() == new_day,
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arms=" + ",".join(bad))
    print("SPLIT-REAL-OK a gained split row holds the name untouched; no new split row writes the extension (CUSIP %s)" % cusip)
    return 0


if __name__ == "__main__":
    sys.exit(main())
