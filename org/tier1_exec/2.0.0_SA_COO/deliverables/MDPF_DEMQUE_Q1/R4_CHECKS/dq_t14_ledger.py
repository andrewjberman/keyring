"""MDPF_DEMQUE round 4, DQ-t-14 criterion AC2: the uploader's FIRST real run at site Z landed rows. Usage:
`python dq_t14_ledger.py [YYYY-MM-DD]` -- with no day, the latest dt= partition holding an object. Lists the builder ledger home
lib.opal_naming.address("bloomberg","global","bronze","demand_ledger","dt=<day>") (read-only), reads every JSON-lines object there, and
requires >= 1 row, every row carrying date, vendor "bloomberg", channel, mode, rows (int), cells (int or null) and claim
(measured|held|absent), with cells null exactly when claim is absent. LEDGER-OK <rows> <cells>; else LEDGER-BAD <reason>.
"""
from __future__ import annotations

import json
import os
import sys

sys.path.insert(0, os.getcwd())

if __name__ == "__main__":
    import boto3
    from lib.opal_naming import address
    day = sys.argv[1] if len(sys.argv) > 1 else None
    if day is None:
        root = str(address("bloomberg", "global", "bronze", "demand_ledger", "dt=x")).rsplit("/", 1)[0]
        b, _, p = root[len("s3://"):].partition("/")
        cps = boto3.client("s3").list_objects_v2(Bucket=b, Prefix=p + "/", Delimiter="/").get("CommonPrefixes", [])
        days = sorted(c["Prefix"].rstrip("/").rsplit("dt=", 1)[-1] for c in cps if "dt=" in c["Prefix"])
        if not days:
            print("LEDGER-BAD 0 rows: no dt= partition under %s" % root)
            sys.exit(1)
        day = days[-1]
    uri = str(address("bloomberg", "global", "bronze", "demand_ledger", "dt=%s" % day))
    bucket, _, prefix = uri[len("s3://"):].partition("/")
    s3 = boto3.client("s3")
    keys = [o["Key"] for o in s3.list_objects_v2(Bucket=bucket, Prefix=prefix.rstrip("/") + "/").get("Contents", [])]
    rows = []
    for k in keys:
        for ln in s3.get_object(Bucket=bucket, Key=k)["Body"].read().decode("utf-8").splitlines():
            if ln.strip():
                rows.append(json.loads(ln))
    if not rows:
        print("LEDGER-BAD 0 rows under %s (%d objects)" % (uri, len(keys)))
        sys.exit(1)
    need = ("date", "vendor", "channel", "mode", "rows", "cells", "claim")
    for r in rows:
        if any(k not in r for k in need) or r["vendor"] != "bloomberg" or r["claim"] not in ("measured", "held", "absent")                 or not isinstance(r["rows"], int) or ((r["cells"] is None) != (r["claim"] == "absent")):
            print("LEDGER-BAD bad row %r" % (r,))
            sys.exit(1)
    print("LEDGER-OK rows=%d cells=%d under %s" % (len(rows), sum(r["cells"] or 0 for r in rows), uri))
    sys.exit(0)
