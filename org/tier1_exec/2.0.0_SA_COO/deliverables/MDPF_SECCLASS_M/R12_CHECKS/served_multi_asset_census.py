#!/usr/bin/env python3
"""served_multi_asset_census.py -- MDPF_SECCLASS: count `multi_asset` in the served composition artifacts the Advisor Intelligence
page reads, for every firm bucket that serves a `platinum/` tree (laptop 1.0.0_SA_CTO review 106245 of cand-dell1-secclass-e53-r9).

READ-ONLY (list + get). For each opal-data-* bucket, every key under `platinum/` ending in `.json` is read, and every JSON string
equal to "multi_asset" (as a value or a key) is counted. Per bucket it prints: keys listed, keys read, keys with a hit, total hits,
or UNREAD with the error (a denied bucket is a value, never a zero). Prints MULTI-ASSET-CENSUS ok=<bool>, where ok means every
bucket that holds a platinum tree was read in full and the total is 0. Writes the per-bucket table as JSON to argv[1] if given.
"""
import json
import sys

import boto3
from botocore.exceptions import ClientError

TOKEN = "multi_asset"


def hits(node):
    if isinstance(node, dict):
        return sum((k == TOKEN) + hits(v) for k, v in node.items())
    if isinstance(node, list):
        return sum(hits(v) for v in node)
    return int(node == TOKEN)


def census(s3, bucket):
    row = {"bucket": bucket, "listed": 0, "read": 0, "keys_with_hit": 0, "hits": 0, "examples": []}
    try:
        for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix="platinum/"):
            for obj in page.get("Contents", []):
                if not obj["Key"].endswith(".json"):
                    continue
                row["listed"] += 1
                body = s3.get_object(Bucket=bucket, Key=obj["Key"])["Body"].read()
                row["read"] += 1
                try:
                    n = hits(json.loads(body))
                except ValueError:
                    n = body.count(b'"multi_asset"')
                if n:
                    row["keys_with_hit"] += 1
                    row["hits"] += n
                    if len(row["examples"]) < 5:
                        row["examples"].append(obj["Key"])
    except ClientError as e:
        row["unread"] = e.response.get("Error", {}).get("Code", "ClientError")
    return row


def main(argv):
    s3 = boto3.client("s3", region_name="us-east-1")
    buckets = sorted(b["Name"] for b in s3.list_buckets()["Buckets"] if b["Name"].startswith("opal-data-"))
    rows = [census(s3, b) for b in buckets]
    for r in rows:
        if r.get("unread"):
            print(f"  {r['bucket']}: UNREAD {r['unread']}")
        elif r["listed"]:
            print(f"  {r['bucket']}: listed={r['listed']} read={r['read']} keys_with_hit={r['keys_with_hit']} hits={r['hits']} "
                  f"examples={r['examples']}")
    served = [r for r in rows if r["listed"] or r.get("unread")]
    total = sum(r["hits"] for r in served)
    complete = all(not r.get("unread") and r["read"] == r["listed"] for r in served)
    print(f"MULTI-ASSET-CENSUS ok={complete and total == 0} buckets_scanned={len(buckets)} with_platinum={len(served)} "
          f"unread={sum(1 for r in served if r.get('unread'))} keys_read={sum(r['read'] for r in served)} hits={total}")
    if len(argv) > 1:
        with open(argv[1], "w", encoding="utf-8") as fh:
            json.dump({"token": TOKEN, "buckets": rows}, fh, indent=2)
    return 0 if complete and total == 0 else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
