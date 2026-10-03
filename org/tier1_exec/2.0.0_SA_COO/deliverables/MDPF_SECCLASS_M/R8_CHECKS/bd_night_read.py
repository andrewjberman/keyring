#!/usr/bin/env python3
"""bd_night_read.py -- MDPF_SECCLASS, the Black Diamond scheduled-fire reads of 2026-10-02 (read-only).

  silver   the 22:10Z silver fire (CTO batch 129): silver/bd_assets_dim.parquet's class counts, newest version vs the one
           before it -- the r3 silver builder must class as the old library did (any class count moving = roll it back).
  gold     the 23:00Z gold fire: ledger secclass-bd-thread-r4-reland-m-20261002 leg S (platinum/firm/mix_summary.json lists
           every class, sums to 1, unclassified <= 5.0 pct; z08327149 carries VXX structured / Hedge and ties) and ledger
           secclass-cot-seed-rows-m-20261001 leg G (the newest holdings_lots carry SPYI, PSLV, FPNIX with the rows' classes).

Run from the repo root:  python .../R8_CHECKS/bd_night_read.py silver|gold
"""
from __future__ import annotations

import collections
import io
import json
import sys

import boto3
import pyarrow.parquet as pq

BUCKET = "opal-data-bd"
s3 = boto3.client("s3", region_name="us-east-1")


def versions(key, n=2):
    vs = [v for v in s3.list_object_versions(Bucket=BUCKET, Prefix=key, MaxKeys=10).get("Versions", []) if v["Key"] == key]
    return sorted(vs, key=lambda v: v["LastModified"], reverse=True)[:n]


def body(key, version_id=None):
    kw = {"Bucket": BUCKET, "Key": key}
    if version_id:
        kw["VersionId"] = version_id
    return s3.get_object(**kw)["Body"].read()


def silver() -> int:
    """Per asset_id, newest version vs the one before: which assets changed blend / opal class, and whether each changed
    asset's ticker carries a row written in the last 26 hours (a ruled row act) -- any other change is unexplained."""
    key = "silver/bd_assets_dim.parquet"
    cols = ["asset_id", "ticker", "asset_super_class_blend", "super_class_source", "opal_asset_class"]
    vs = versions(key)
    frames = []
    for v in vs:
        df = pq.read_table(io.BytesIO(body(key, v["VersionId"])), columns=cols).to_pandas().set_index("asset_id")
        frames.append(df)
        print(f"{key} {v['VersionId']} {v['LastModified'].isoformat()} rows {len(df)} opal_asset_class "
              f"{dict(collections.Counter(df['opal_asset_class']))}")
    if len(frames) < 2:
        return 0
    new, old = frames
    both = new.index.intersection(old.index)
    moved = [a for a in both if (new.at[a, "asset_super_class_blend"], new.at[a, "opal_asset_class"])
             != (old.at[a, "asset_super_class_blend"], old.at[a, "opal_asset_class"])]
    ddb = boto3.client("dynamodb", region_name="us-east-1")
    import datetime
    since = (datetime.datetime.now(datetime.timezone.utc) - datetime.timedelta(hours=26)).isoformat()
    explained, unexplained = [], []
    for a in moved:
        tk = str(new.at[a, "ticker"] or "").upper()
        item = ddb.get_item(TableName="etf-classifications", Key={"ticker": {"S": tk}}).get("Item") if tk else None
        fresh = bool(item) and item.get("last_updated", {}).get("S", "") >= since
        (explained if fresh else unexplained).append((a, tk, old.at[a, "opal_asset_class"], new.at[a, "opal_asset_class"],
                                                      old.at[a, "asset_super_class_blend"], new.at[a, "asset_super_class_blend"]))
    print(f"assets in both {len(both)}, new assets {len(new.index.difference(old.index))}, changed class {len(moved)}: "
          f"{len(explained)} on a row written in the last 26 h, {len(unexplained)} otherwise")
    for r in unexplained[:20]:
        print("   UNEXPLAINED", r)
    for r in explained[:10]:
        print("   by a row", r)
    return 0


def gold() -> int:
    key = "platinum/firm/mix_summary.json"
    v = versions(key, 1)[0]
    d = json.loads(body(key, v["VersionId"]))
    mix = d["mix"]
    print(f"{key} {v['VersionId']} {v['LastModified'].isoformat()} data_as_of {d.get('data_as_of')}")
    for k, x in mix.items():
        print("   %-13s %8.4f pct %18.2f" % (k, 100 * x["pct"], x["market_value"]))
    print("   pct sum %.9f, mix value %.2f, composition total %.2f, unclassified %.4f pct" % (
        sum(x["pct"] for x in mix.values()), sum(x["market_value"] for x in mix.values()),
        d["composition"]["total_market_value"], 100 * mix.get("unclassified", {}).get("pct", 0)))
    zkey = "platinum/clients/z08327149/composition.json"
    zv = versions(zkey, 1)[0]
    z = json.loads(body(zkey, zv["VersionId"]))
    tot = sum(x["market_value"] for x in z["mix"])
    vxx = [(x["asset_class"], t.get("sub_asset_class_canonical"), t["market_value"]) for x in z["mix"]
           for t in x.get("top_holdings", []) if t.get("key") == "VXX"]
    print(f"{zkey} {zv['VersionId']} {zv['LastModified'].isoformat()} mix sum %.2f total %s VXX %s" % (tot, z.get("total_market_value"), vxx))
    lots_prefix = "gold/timeseries/holdings_lots/"
    page = s3.list_objects_v2(Bucket=BUCKET, Prefix=lots_prefix)
    objs = page.get("Contents", [])
    while page.get("IsTruncated"):
        page = s3.list_objects_v2(Bucket=BUCKET, Prefix=lots_prefix, ContinuationToken=page["NextContinuationToken"])
        objs += page.get("Contents", [])
    newest = max(objs, key=lambda o: o["LastModified"])
    t = pq.read_table(io.BytesIO(body(newest["Key"])))
    print(f"{newest['Key']} {newest['LastModified'].isoformat()} rows {t.num_rows} columns {t.schema.names}")
    cols = [c for c in ("ticker", "asset_class", "sub_asset_class", "asset_class_canonical", "sub_asset_class_canonical",
                        "class_source") if c in t.schema.names]
    df = t.select(cols).to_pandas()
    for sym in ("SPYI", "PSLV", "FPNIX"):
        sub = df[df["ticker"].astype(str).str.upper() == sym]
        print(f"   {sym}: {len(sub)} lots; " + "; ".join(f"{c}={sorted(set(map(str, sub[c])))}" for c in cols if c != "ticker"))
    return 0


if __name__ == "__main__":
    sys.exit({"silver": silver, "gold": gold}[sys.argv[1]]())
