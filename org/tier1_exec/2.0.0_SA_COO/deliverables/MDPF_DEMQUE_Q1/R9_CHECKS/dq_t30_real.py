"""MDPF_DEMQUE round 9, DQ-t-30 criterion AC2: `lock.py --partition` on the REAL transactions store (S3 read only). It prints ONE JSON line
{"partition": "date=...", "trades_through": "YYYY-MM-DD", "partitions": N}. This check lists the store's date= partitions itself, takes the
greatest one that holds a parquet file, reads that partition's largest Trade_Date, and requires the tool to agree on all three.
LP-REAL-OK partition=<p> trades_through=<d>; else LP-REAL-BAD <why>. (2026-10-11 read: one partition, date=2026-06-23, trades through 2026-06-22.)
"""
from __future__ import annotations

import io
import json
import os
import subprocess
import sys
from urllib.parse import urlparse

sys.path.insert(0, ".")
TOOL = os.path.join("data", "mdpf", "scripts", "demque", "lock.py")


def _bad(why):
    print("LP-REAL-BAD " + why)
    return 1


def main() -> int:
    r = subprocess.run([sys.executable, TOOL, "--partition"], capture_output=True, text=True, timeout=110, check=False)
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    if r.returncode != 0 or not lines:
        return _bad("tool rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip()))
    got = json.loads(lines[-1])
    import boto3
    import pyarrow.compute as pc
    import pyarrow.parquet as pq
    from lib.opal_naming import address
    p = urlparse(address("commonwealth", "cottonwood", "silver", "transactions", "date=2026-01-01"))
    bucket, key = p.netloc, p.path.strip("/")
    parent = key.rsplit("/", 1)[0] + "/"
    s3 = boto3.client("s3")
    parts = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=parent, Delimiter="/"):
        parts += [c["Prefix"] for c in page.get("CommonPrefixes", [])]
    held = []
    for pre in sorted(x for x in parts if x.rstrip("/").rsplit("/", 1)[-1].startswith("date=")):
        objs = [o["Key"] for o in s3.list_objects_v2(Bucket=bucket, Prefix=pre).get("Contents", []) if o["Key"].endswith(".parquet")]
        if objs:
            held.append((pre, objs))
    if not held:
        return _bad("no date= partition holds a parquet file under " + parent)
    pre, objs = held[-1]
    mx = None
    for k in objs:
        t = pq.read_table(io.BytesIO(s3.get_object(Bucket=bucket, Key=k)["Body"].read()), columns=["Trade_Date"])
        m = pc.max(t["Trade_Date"]).as_py()
        mx = m if mx is None or m > mx else mx
    want = {"partition": pre.rstrip("/").rsplit("/", 1)[-1], "trades_through": str(mx)[:10], "partitions": len(held)}
    print("independent: %s | tool: %s" % (want, got))
    if any(got.get(k) != v for k, v in want.items()):
        return _bad("tool and independent read differ")
    print("LP-REAL-OK partition=%s trades_through=%s" % (want["partition"], want["trades_through"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
