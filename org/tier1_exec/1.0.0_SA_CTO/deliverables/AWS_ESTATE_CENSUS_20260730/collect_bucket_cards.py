"""Per-bucket card facts: top-level paths + per-path approx last write + sample leaf.

Last-write heuristic: descend the lexicographically-LAST CommonPrefix at each level
(finds the newest partition in date-partitioned trees), then max(LastModified) of that
page. Labeled APPROX -- exact for date-partitioned layouts, first-page-weak for flat ones.
Usage: python collect_bucket_cards.py <bucket> [<bucket> ...] -> bucket_cards.json
"""
from __future__ import annotations

import json
import sys

import boto3

s3 = boto3.client("s3", region_name="us-east-1")


def descend_last_write(bucket: str, prefix: str):
    """Best (max_lastmod, sample_key) reachable by descending EVERY CommonPrefix level's
    max-prefix chain, folding in same-level objects at each step.

    FIXED 2026-07-30: v1 BROKE at a mixed level (objects + subdirs coexisting) and
    reported the level's own objects, never descending -- opal-data-inf silver/ holds one
    root parquet from 05-05 next to 12 subdirs writing TODAY, and v1 called the layer
    cold. Break-on-mixed-level specimen, recorded in RULINGS_LEDGER."""
    best = (None, None)
    for depth in range(10):
        r = s3.list_objects_v2(Bucket=bucket, Prefix=prefix, Delimiter="/", MaxKeys=1000)
        cps = [c["Prefix"] for c in r.get("CommonPrefixes", [])]
        objs = r.get("Contents", [])
        if objs:
            newest = max(objs, key=lambda o: o["LastModified"])
            iso = newest["LastModified"].isoformat()
            if best[0] is None or iso > best[0]:
                best = (iso, newest["Key"])
        if not cps:
            break
        prefix = max(cps)
    return best[0], best[1], depth


out = {}
for bucket in sys.argv[1:]:
    print(f"--- {bucket}", flush=True)
    card = {"prefixes": []}
    r = s3.list_objects_v2(Bucket=bucket, Delimiter="/", MaxKeys=1000)
    tops = [c["Prefix"] for c in r.get("CommonPrefixes", [])]
    root_objs = r.get("Contents", [])
    card["root_objects"] = len(root_objs)
    if root_objs:
        nr = max(root_objs, key=lambda o: o["LastModified"])
        card["root_last_write"] = nr["LastModified"].isoformat()
        card["root_sample"] = nr["Key"]
    card["top_prefix_count"] = len(tops)
    for p in tops[:12]:
        lw, sample, depth = descend_last_write(bucket, p)
        card["prefixes"].append(
            {"prefix": p, "approx_last_write": lw, "newest_leaf": sample})
        print(f"  {p:40s} {lw or 'EMPTY'}", flush=True)
    if len(tops) > 12:
        card["prefixes_truncated"] = len(tops) - 12
    out[bucket] = card

json.dump(out, open("bucket_cards.json", "w"), indent=1, default=str)
print("wrote bucket_cards.json")
