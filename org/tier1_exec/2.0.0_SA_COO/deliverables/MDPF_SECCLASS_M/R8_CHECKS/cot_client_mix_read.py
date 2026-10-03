#!/usr/bin/env python3
"""cot_client_mix_read.py -- Cottonwood re-point leg R/S acceptance: every client mix a Cottonwood gold run rewrote sums to
one on its latest point, and which classes carry a share.

Reads opal-data-cot gold/entities/clients/*.json whose LastModified is at or after --since (UTC ISO), the latest `mix` point
of each (shares per class, `total_mv`). Read-only.

Run from the repo root:
  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R8_CHECKS/cot_client_mix_read.py --since 2026-10-02T17:59:00Z
"""
from __future__ import annotations

import argparse
import collections
import datetime
import json
import sys
from concurrent.futures import ThreadPoolExecutor

import boto3
from botocore.config import Config
from botocore.exceptions import ConnectionClosedError, ReadTimeoutError, ResponseStreamingError

BUCKET = "opal-data-cot"
PREFIX = "gold/entities/clients/"
s3 = boto3.client("s3", region_name="us-east-1",
                  config=Config(read_timeout=120, connect_timeout=30, retries={"max_attempts": 8, "mode": "adaptive"}))


def get(key):
    for attempt in range(10):   # a body-read timeout is not retried by botocore
        try:
            return json.loads(s3.get_object(Bucket=BUCKET, Key=key)["Body"].read())
        except (ReadTimeoutError, ResponseStreamingError, ConnectionClosedError):
            if attempt == 9:
                raise
    raise AssertionError("unreachable")


def one(key):
    last = (get(key).get("mix") or [{}])[-1]
    parts = {c: v for c, v in last.items() if c not in ("date", "total_mv") and isinstance(v, (int, float))}
    return key, last.get("date"), sum(parts.values()), sorted(c for c, v in parts.items() if v), last.get("total_mv")


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--since", required=True)
    since = datetime.datetime.fromisoformat(ap.parse_args().since.replace("Z", "+00:00"))
    keys, tok, total = [], None, 0
    while True:
        kw = {"Bucket": BUCKET, "Prefix": PREFIX}
        if tok:
            kw["ContinuationToken"] = tok
        page = s3.list_objects_v2(**kw)
        for o in page.get("Contents", []):
            total += 1
            if o["LastModified"] >= since and o["Key"].endswith(".json"):
                keys.append(o["Key"])
        if not page.get("IsTruncated"):
            break
        tok = page["NextContinuationToken"]
    print(f"client files {total}; rewritten at or after {since.isoformat()}: {len(keys)}", flush=True)
    with ThreadPoolExecutor(4) as pool:
        res = list(pool.map(one, keys))
    dates = collections.Counter(r[1] for r in res)
    zero = [r for r in res if not r[4]]
    off = [r for r in res if r[4] and abs(r[2] - 1) > 0.001]
    cls = collections.Counter(c for r in res for c in r[3])
    print(f"latest dates {dict(dates)}")
    print(f"latest point sums to 1 within 0.001: {len(res) - len(off) - len(zero)}; not summing: {len(off)}; zero total: {len(zero)}")
    for r in off[:5]:
        print("  NOT SUMMING", r[0], r[1], round(r[2], 6), r[3])
    print(f"clients with a non-zero share, per class: {dict(sorted(cls.items()))}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
