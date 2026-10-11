"""MDPF_DEMQUE round 9, DQ-t-32 criterion AC3: `hold_lock_records.py --dry-run` on the REAL served store (S3 read only, nothing written).
It prints ONE JSON line {"planned": [{"cusip", "symbol", "claim_before", "claim_after", "claim_reason"}, ...]} for every name whose
prices.parquet still carries exactly the three original columns. This check reads those names itself from the parquet footers and requires
the planned set to equal them, every `claim_after` "held", and every reason to carry "cause under measurement" and "90 pct".
HOLD-OK n=<names>; else HOLD-BAD <why>.
"""
from __future__ import annotations

import io
import json
import os
import subprocess
import sys
from urllib.parse import urlparse

sys.path.insert(0, ".")
TOOL = os.path.join("data", "mdpf", "scripts", "demque", "hold_lock_records.py")
ORIGINAL = ["date", "close_served", "as_traded_close"]


def _bad(why):
    print("HOLD-BAD " + why)
    return 1


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    r = subprocess.run([sys.executable, TOOL, "--dry-run"], capture_output=True, text=True, timeout=115, check=False)
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    if r.returncode != 0 or not lines:
        return _bad("tool rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip()))
    planned = json.loads(lines[-1]).get("planned", [])
    import boto3
    import pyarrow.parquet as pq
    from lib.opal_naming import address
    p = urlparse(address("yahoo", "global", "silver", "price_history", "x").rsplit("/", 1)[0])
    bucket, prefix = p.netloc, p.path.strip("/") + "/"
    s3 = boto3.client("s3")
    stale = set()
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=prefix, Delimiter="/"):
        for cp in page.get("CommonPrefixes", []):
            nm = cp["Prefix"][len(prefix):].strip("/")
            if not nm.startswith("cusip="):
                continue
            try:
                body = s3.get_object(Bucket=bucket, Key=cp["Prefix"] + "prices.parquet")["Body"].read()
            except s3.exceptions.NoSuchKey:
                continue
            if list(pq.ParquetFile(io.BytesIO(body)).schema_arrow.names) == ORIGINAL:
                stale.add(nm[len("cusip="):])
    got = {x.get("cusip") for x in planned}
    print("independent: %d three-column names; tool planned %d" % (len(stale), len(got)))
    if got != stale or not stale:
        return _bad("planned set differs (only-tool=%s only-check=%s)" % (sorted(got - stale)[:5], sorted(stale - got)[:5]))
    for x in planned:
        if x.get("claim_after") != "held" or "cause under measurement" not in str(x.get("claim_reason")) or "90 pct" not in str(x.get("claim_reason")):
            return _bad("a planned row is not held with the stated reason: %s" % x)
    print("HOLD-OK n=%d" % len(stale))
    return 0


if __name__ == "__main__":
    sys.exit(main())
