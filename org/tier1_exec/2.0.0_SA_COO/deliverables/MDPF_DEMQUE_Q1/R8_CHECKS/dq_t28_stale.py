"""MDPF_DEMQUE round 8, DQ-t-28 criterion AC2: the stale-file list on the REAL served price store (S3 read only, nothing written).
`redraw_stale.py --list` prints one JSON line {"total": N, "stale": [{"cusip","symbol","start","end"}, ...]}. This check counts the
files whose prices.parquet carries exactly the three original columns (date, close_served, as_traded_close) by its own read of the
parquet footers and requires the tool's stale CUSIP set to equal it, with total equal to the CUSIP prefixes holding a
prices.parquet. STALE-OK n=<stale> of <total>; else STALE-BAD <why>. (2026-10-11 04:xxZ read: 32 of 141.)
"""
from __future__ import annotations

import io
import json
import os
import subprocess
import sys
from urllib.parse import urlparse

sys.path.insert(0, ".")
TOOL = os.path.join("data", "mdpf", "scripts", "demque", "redraw_stale.py")
ORIGINAL = ["date", "close_served", "as_traded_close"]


def _bad(why):
    print("STALE-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    r = subprocess.run([sys.executable, TOOL, "--list"], capture_output=True, text=True, timeout=110, check=False)
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    if r.returncode != 0 or not lines:
        return _bad("tool rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip()))
    got = json.loads(lines[-1])
    import boto3
    import pyarrow.parquet as pq
    from lib.opal_naming import address
    p = urlparse(address("yahoo", "global", "silver", "price_history", "x").rsplit("/", 1)[0])
    bucket, prefix = p.netloc, p.path.strip("/") + "/"
    s3 = boto3.client("s3")
    total, stale = 0, set()
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=prefix, Delimiter="/"):
        for cp in page.get("CommonPrefixes", []):
            name = cp["Prefix"][len(prefix):].strip("/")
            if not name.startswith("cusip="):
                continue
            try:
                body = s3.get_object(Bucket=bucket, Key=cp["Prefix"] + "prices.parquet")["Body"].read()
            except s3.exceptions.NoSuchKey:
                continue
            total += 1
            if list(pq.ParquetFile(io.BytesIO(body)).schema_arrow.names) == ORIGINAL:
                stale.add(name[len("cusip="):])
    tool_set = {s.get("cusip") for s in got.get("stale", [])}
    print("independent: stale=%d of %d; tool: stale=%d of %s" % (len(stale), total, len(tool_set), got.get("total")))
    if got.get("total") != total or tool_set != stale:
        return _bad("tool and independent read differ (only-tool=%s only-check=%s)" % (
            sorted(tool_set - stale)[:5], sorted(stale - tool_set)[:5]))
    if any(not (s.get("symbol") and s.get("start") and s.get("end")) for s in got["stale"]):
        return _bad("a stale row lacks symbol/start/end")
    print("STALE-OK n=%d of %d" % (len(stale), total))
    return 0


if __name__ == "__main__":
    sys.exit(main())
