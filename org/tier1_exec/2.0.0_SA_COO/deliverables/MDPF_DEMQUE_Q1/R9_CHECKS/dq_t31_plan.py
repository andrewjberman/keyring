"""MDPF_DEMQUE round 9, DQ-t-31 criterion AC2: the standing extension's PLAN on the REAL served price store (S3 read only, nothing written).
`extend_frontier.py --plan --today D` prints ONE JSON line {"frontier", "start", "end", "symbols", "cells", "finish_date", "request_id"}.
Checked: --today 2026-10-12 (a trading Monday) ends 2026-10-12; --today 2026-10-11 (a Sunday) ends 2026-10-09 (Friday is Monday's answer);
`symbols` equals this check's own count of CUSIP prefixes holding both prices.parquet and lock.json; `start` is the earliest valid_from.
XPLAN-OK n=<symbols>; else XPLAN-BAD <why>.
"""
from __future__ import annotations

import json
import os
import subprocess
import sys
from urllib.parse import urlparse

sys.path.insert(0, ".")
TOOL = os.path.join("data", "mdpf", "scripts", "demque", "extend_frontier.py")


def _bad(why):
    print("XPLAN-BAD " + why)
    return 1


def _plan(day):
    r = subprocess.run([sys.executable, TOOL, "--plan", "--today", day], capture_output=True, text=True, timeout=110, check=False)
    lines = [ln for ln in r.stdout.splitlines() if ln.strip().startswith("{")]
    if r.returncode != 0 or not lines:
        return None, "rc=%d %s" % (r.returncode, (r.stderr or r.stdout)[-300:].strip())
    return json.loads(lines[-1]), None


def main() -> int:
    if not os.path.isfile(TOOL):
        return _bad("no file " + TOOL)
    mon, e1 = _plan("2026-10-12")
    sun, e2 = _plan("2026-10-11")
    if e1 or e2:
        return _bad(e1 or e2)
    import boto3
    from lib.opal_naming import address
    p = urlparse(address("yahoo", "global", "silver", "price_history", "x").rsplit("/", 1)[0])
    bucket, prefix = p.netloc, p.path.strip("/") + "/"
    s3 = boto3.client("s3")
    n, starts = 0, []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=prefix, Delimiter="/"):
        for cp in page.get("CommonPrefixes", []):
            if not cp["Prefix"][len(prefix):].startswith("cusip="):
                continue
            try:
                s3.head_object(Bucket=bucket, Key=cp["Prefix"] + "prices.parquet")
                lk = json.loads(s3.get_object(Bucket=bucket, Key=cp["Prefix"] + "lock.json")["Body"].read())
            except Exception:
                continue
            n += 1
            starts.append(str(lk.get("valid_from"))[:10])
    print("independent: symbols=%d earliest_valid_from=%s" % (n, min(starts) if starts else None))
    print("monday: %s" % json.dumps(mon, sort_keys=True))
    print("sunday: %s" % json.dumps(sun, sort_keys=True))
    arms = {
        "monday_end": mon.get("end") == "2026-10-12" and mon.get("frontier") == "2026-10-12",
        "sunday_end": sun.get("end") == "2026-10-09" and sun.get("frontier") == "2026-10-09",
        "symbols": mon.get("symbols") == n == sun.get("symbols"),
        "start": mon.get("start") == (min(starts) if starts else None),
    }
    bad = [k for k, v in arms.items() if not v]
    if bad:
        return _bad("arms=" + ",".join(bad))
    print("XPLAN-OK n=%d" % n)
    return 0


if __name__ == "__main__":
    sys.exit(main())
