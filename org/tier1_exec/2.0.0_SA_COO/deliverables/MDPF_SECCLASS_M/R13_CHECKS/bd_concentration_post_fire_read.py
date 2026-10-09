#!/usr/bin/env python3
"""bd_concentration_post_fire_read.py -- MDPF_SECCLASS post-fire read over every BD client concentration file (read-only).

Two legs in one pass over opal-data-bd platinum/clients/*/concentration.json:
  - e75 leg G: count of keys and holdings still carrying the retired class `multi_asset` (denominator printed);
  - e77 leg F (CTO condition 3): for each REMAP key of S11_ROW_SET_20261008.tsv, the held dollars and served asset_class on each
    file's LATEST dated entry, summed over relationships.
Prints one E75-CONC line and one E77-REMAP line, and writes JSON to argv[1].
"""
import csv
import json
import sys
from collections import defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

import boto3

BUCKET = "opal-data-bd"
HERE = Path(__file__).resolve().parent
SET = HERE.parent / "S11_ROW_SET_20261008.tsv"


def holdings_of(doc):
    """(latest date, holdings list) from a concentration file in either served shape."""
    conc = doc.get("concentration", doc) if isinstance(doc, dict) else doc
    if isinstance(conc, list) and conc and isinstance(conc[0], dict) and "date" in conc[0]:
        last = max(conc, key=lambda e: e.get("date") or "")
        return last.get("date"), last.get("holdings") or []
    if isinstance(conc, dict):
        return doc.get("data_as_of"), conc.get("holdings") or conc.get("items") or []
    return None, []


def count_token(node, token="multi_asset"):
    if isinstance(node, dict):
        return sum((v == token) + count_token(v, token) for v in node.values())
    if isinstance(node, list):
        return sum(count_token(v, token) for v in node)
    return 0


def main(argv):
    remap = {r["key"]: r for r in csv.DictReader(open(SET, encoding="utf-8"), delimiter="\t") if r["action"] == "REMAP"}
    s3 = boto3.client("s3", region_name="us-east-1")
    keys = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix="platinum/clients/"):
        keys += [o["Key"] for o in page.get("Contents", []) if o["Key"].endswith("/concentration.json")]

    def read(k):
        return k, json.loads(s3.get_object(Bucket=BUCKET, Key=k)["Body"].read())

    ma_keys, ma_vals = 0, 0
    held = defaultdict(lambda: {"market_value": 0.0, "relationships": 0, "classes": defaultdict(float)})
    with ThreadPoolExecutor(16) as pool:
        for k, doc in pool.map(read, keys):
            n = count_token(doc)
            ma_keys += n > 0
            ma_vals += n
            _, hs = holdings_of(doc)
            for h in hs:
                t = h.get("ticker") or h.get("key")
                if t in remap:
                    mv = float(h.get("market_value") or 0)
                    held[t]["market_value"] += mv
                    held[t]["relationships"] += 1
                    held[t]["classes"][h.get("asset_class")] += mv
    total = sum(v["market_value"] for v in held.values())
    by_class = defaultdict(float)
    for v in held.values():
        for c, mv in v["classes"].items():
            by_class[c] += mv
    print(f"E75-CONC keys={len(keys)} keys_with_multi_asset={ma_keys} multi_asset_values={ma_vals}")
    print(f"E77-REMAP remap_keys={len(remap)} held_keys={len(held)} held_dollars={total:,.2f} "
          f"by_served_class={ {c: round(v, 2) for c, v in sorted(by_class.items(), key=lambda x: str(x[0]))} }")
    out = {"keys": len(keys), "keys_with_multi_asset": ma_keys, "multi_asset_values": ma_vals,
           "remap": {t: {"market_value": v["market_value"], "relationships": v["relationships"], "classes": dict(v["classes"])}
                     for t, v in sorted(held.items())}}
    if len(argv) > 1:
        json.dump(out, open(argv[1], "w", encoding="utf-8"), indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
