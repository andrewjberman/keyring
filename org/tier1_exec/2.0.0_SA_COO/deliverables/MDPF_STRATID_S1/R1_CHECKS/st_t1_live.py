"""MDPF_STRATID round 1, ST-t-1 criterion AC3: the seam probe against the REAL neighbour (read-only S3).

Calls `build_cottonwood_mdpf_slice.measure_sma_overlap(s3, value_date)` for the served slice's last date and requires a
PFDE row: {"pfde": {"sleeve_accounts": int >= 1, "overlap_accounts": int >= 0, "overlap_dollars": float >= 0}}, with
overlap_accounts <= sleeve_accounts. Writes nothing. LIVE-OK, else LIVE-BAD naming what failed.
"""
from __future__ import annotations

import json
import os
import sys

GOLD = os.path.join("data", "assets", "scripts", "gold")
SILVER = os.path.join("data", "assets", "scripts", "silver")
MDPF = os.path.join("data", "mdpf", "scripts", "gold")

if __name__ == "__main__":
    for p in (GOLD, SILVER, MDPF):
        sys.path.insert(0, os.path.abspath(p))
    import boto3
    import build_cottonwood_mdpf_slice as sl

    if not hasattr(sl, "measure_sma_overlap"):
        print("LIVE-BAD no measure_sma_overlap in build_cottonwood_mdpf_slice")
        sys.exit(1)
    s3 = boto3.client("s3")
    cot = json.loads(s3.get_object(Bucket="opal-data-assets",
                                   Key="gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json")["Body"].read())
    d = cot["dates"][-1]
    got = sl.measure_sma_overlap(s3, d)
    print("date=%s result=%s" % (d, json.dumps(got, default=str)))
    p = (got or {}).get("pfde")
    if not isinstance(p, dict):
        print("LIVE-BAD no pfde row")
        sys.exit(1)
    sa, oa, od = p.get("sleeve_accounts"), p.get("overlap_accounts"), p.get("overlap_dollars")
    if not (isinstance(sa, int) and sa >= 1 and isinstance(oa, int) and 0 <= oa <= sa
            and isinstance(od, (int, float)) and od >= 0):
        print("LIVE-BAD pfde row malformed: %r" % (p,))
        sys.exit(1)
    print("LIVE-OK")
    sys.exit(0)
