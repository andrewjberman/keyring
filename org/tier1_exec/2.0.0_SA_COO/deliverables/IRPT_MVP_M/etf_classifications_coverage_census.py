"""Coverage of the canonical classification table over served holdings (Andrew-direct, CTO 102302; IRPT_BCKEND-S173).

Andrew: "The only classification table that matters is whatever ETFClassifier is connected to, the DDB table and
associated infra that feeds into the Positioning POSN page ... THat is the canonical table." That table is DynamoDB
`etf-classifications` (HASH ticker). This reads, read-only:
- the latest canonical/holdings partition of COT (opal-data-cot) and BD (opal-data-bd), positive market value;
- every item of etf-classifications (and of bd-securities, for the comparison only);
and prints, per firm, how many distinct tickers and served dollars the canonical table covers, the largest uncovered
tickers by dollars, and, for covered tickers, where the two tables disagree on the class.

Usage: python etf_classifications_coverage_census.py [--out <json>]
"""
import argparse
import json
import sys
from io import BytesIO
from pathlib import Path

import boto3
import pandas as pd

FIRMS = (("cot", "opal-data-cot"), ("bd", "opal-data-bd"))


def scan(table, fields):
    t = boto3.resource("dynamodb").Table(table)
    out, kw = {}, {}
    while True:
        r = t.scan(ProjectionExpression=", ".join(fields), **kw)
        for item in r["Items"]:
            out[str(item["ticker"]).upper()] = item
        if "LastEvaluatedKey" not in r:
            return out
        kw = {"ExclusiveStartKey": r["LastEvaluatedKey"]}


def latest(s3, bucket):
    keys = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix="gold/canonical/holdings/"):
        keys += [o["Key"] for o in page.get("Contents", []) if o["Key"].endswith(".parquet")]
    return sorted(keys)[-1]


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--out")
    a = ap.parse_args()
    s3 = boto3.client("s3")
    etf = scan("etf-classifications", ["ticker", "asset_class"])
    bds = scan("bd-securities", ["ticker", "asset_class"])
    res = {"etf_classifications_items": len(etf), "bd_securities_items": len(bds), "firms": {}}
    for firm, bucket in FIRMS:
        key = latest(s3, bucket)
        p = pd.read_parquet(BytesIO(s3.get_object(Bucket=bucket, Key=key)["Body"].read()),
                            columns=["ticker", "asset_name", "market_value"])
        p["market_value"] = pd.to_numeric(p["market_value"], errors="coerce")
        p = p[p["market_value"] > 0].copy()
        p["t"] = p["ticker"].fillna("").astype(str).str.strip().str.upper()
        g = p.groupby("t").agg(mv=("market_value", "sum"), name=("asset_name", "first")).reset_index()
        g = g[~g["t"].isin(["", "NONE", "NAN"])]
        no_ticker_mv = float(p.loc[p["t"].isin(["", "NONE", "NAN"]), "market_value"].sum())
        g["in_etf"] = g["t"].isin(etf.keys())
        g["in_bds"] = g["t"].isin(bds.keys())
        total = float(p["market_value"].sum())
        cov = g[g["in_etf"]]
        unc = g[~g["in_etf"]].sort_values("mv", ascending=False)
        disagree = []
        for _, r in cov.iterrows():
            e, b = etf[r["t"]].get("asset_class"), (bds.get(r["t"]) or {}).get("asset_class")
            if b is not None and e != b:
                disagree.append({"ticker": r["t"], "etf": e, "bd_securities": b, "mv": round(float(r["mv"]), 2)})
        res["firms"][firm] = {
            "partition": key, "served_total": round(total, 2), "no_ticker_mv": round(no_ticker_mv, 2),
            "tickers": int(len(g)), "tickers_in_etf": int(len(cov)),
            "mv_in_etf": round(float(cov["mv"].sum()), 2), "mv_in_etf_pct": round(float(cov["mv"].sum()) / total, 4),
            "tickers_in_bd_securities": int(g["in_bds"].sum()),
            "mv_in_bd_securities_pct": round(float(g.loc[g["in_bds"], "mv"].sum()) / total, 4),
            "top_uncovered": [{"ticker": r["t"], "name": str(r["name"])[:40], "mv": round(float(r["mv"]), 2),
                               "in_bd_securities": bool(r["in_bds"])} for _, r in unc.head(25).iterrows()],
            "class_disagreements": sorted(disagree, key=lambda d: -d["mv"])[:25],
            "class_disagreement_count": len(disagree),
        }
    text = json.dumps(res, indent=1)
    if a.out:
        Path(a.out).write_text(text + "\n", encoding="utf-8")
    for firm, r in res["firms"].items():
        print(firm, r["partition"], "total $%.1fM" % (r["served_total"] / 1e6),
              "| tickers %d, in etf-classifications %d ($ %.1f%%)" % (r["tickers"], r["tickers_in_etf"], 100 * r["mv_in_etf_pct"]),
              "| in bd-securities %d ($ %.1f%%)" % (r["tickers_in_bd_securities"], 100 * r["mv_in_bd_securities_pct"]),
              "| no-ticker $%.1fM" % (r["no_ticker_mv"] / 1e6), "| class disagreements %d" % r["class_disagreement_count"])
    return 0


if __name__ == "__main__":
    sys.exit(main())
