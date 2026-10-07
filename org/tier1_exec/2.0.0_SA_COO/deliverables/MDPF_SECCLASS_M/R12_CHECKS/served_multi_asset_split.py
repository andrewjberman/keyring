#!/usr/bin/env python3
"""served_multi_asset_split.py -- MDPF_SECCLASS: split the served `multi_asset` hits (census, CTO msg 437) into keys written AFTER the
six-class switch (a producer still emits it) and keys last written BEFORE it (stale history the remap predates).

READ-ONLY (list + get, 16 threads). For each bucket given (default opal-data-bd opal-data-cot), every `platinum/**.json` key is read;
a key with any JSON string equal to "multi_asset" (value or key) is a hit, recorded with LastModified, the body's `data_as_of` (when
present) and the file name. The cut is CUT_UTC, the six-class switch: Andrew-direct 2026-10-07 ~00:4xZ; its module landed in both
firm buckets 04:15Z / 07:09Z (rows S51/S52). A hit with LastModified >= CUT is POST-SWITCH (a live producer); before it is PRE-SWITCH.
Prints per bucket: listed, hits, post, pre, and per file name the post count with up to 3 example keys. Writes JSON to argv[1].
"""
import json
import sys
from concurrent.futures import ThreadPoolExecutor
from datetime import datetime, timezone

import boto3

TOKEN = "multi_asset"
CUT_UTC = datetime(2026, 10, 7, 7, 10, tzinfo=timezone.utc)


def hits(node):
    if isinstance(node, dict):
        return sum((k == TOKEN) + hits(v) for k, v in node.items())
    if isinstance(node, list):
        return sum(hits(v) for v in node)
    return int(node == TOKEN)


def read_one(s3, bucket, obj):
    body = s3.get_object(Bucket=bucket, Key=obj["Key"])["Body"].read()
    if b"multi_asset" not in body:
        return None
    try:
        doc = json.loads(body)
        n = hits(doc)
        asof = doc.get("data_as_of") if isinstance(doc, dict) else None
    except ValueError:
        n, asof = body.count(b'"multi_asset"'), None
    if not n:
        return None
    return {"key": obj["Key"], "hits": n, "last_modified": obj["LastModified"].isoformat(), "data_as_of": asof,
            "post_switch": obj["LastModified"] >= CUT_UTC}


def scan(bucket):
    s3 = boto3.client("s3", region_name="us-east-1")
    objs = [o for p in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix="platinum/")
            for o in p.get("Contents", []) if o["Key"].endswith(".json")]
    with ThreadPoolExecutor(16) as ex:
        found = [r for r in ex.map(lambda o: read_one(s3, bucket, o), objs) if r]
    return {"bucket": bucket, "listed": len(objs), "hit_keys": found}


def main(argv):
    out_path = argv[1] if len(argv) > 1 else None
    buckets = argv[2:] or ["opal-data-bd", "opal-data-cot"]
    res = []
    for b in buckets:
        r = scan(b)
        res.append(r)
        post = [h for h in r["hit_keys"] if h["post_switch"]]
        print(f"{b}: listed={r['listed']} hit_keys={len(r['hit_keys'])} post_switch={len(post)} "
              f"pre_switch={len(r['hit_keys']) - len(post)}")
        by = {}
        for h in post:
            by.setdefault(h["key"].rsplit("/", 1)[-1], []).append(h)
        for name, hs in sorted(by.items(), key=lambda kv: -len(kv[1])):
            print(f"  POST {name}: {len(hs)} e.g. {[h['key'] + ' @' + h['last_modified'][:16] for h in hs[:3]]}")
    if out_path:
        with open(out_path, "w", encoding="utf-8") as fh:
            json.dump({"token": TOKEN, "cut_utc": CUT_UTC.isoformat(), "buckets": res}, fh, indent=1)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
