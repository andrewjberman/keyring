"""MDPF_STRATID workstream 2, ST-w-6 criterion AC2 (SEAM, real S3): with no config set by the caller, rebalancer_schemas reads
the shared list from s3://opal-data-etfs/config/etf_universe.json on first use (module attribute STRATEGY_CONFIG_SOURCE names
it), and over the 361 real Cottonwood Rebalancer names opal_sma_member_of gives the same member as the matcher built from the
repo file (the S3 bytes equal the committed bytes, ledger mdpf-stratid-w2a-etf-universe-s3-dell1-20261009). W26-LIVE-OK,
else W26-LIVE-BAD. Read-only S3. Run from the repo (worktree) root."""
from __future__ import annotations

import io
import json
import sys

BUCKET = "opal-data-assets"
SILVER = "blackdiamond/cottonwood/silver/"


def main() -> int:
    sys.path.insert(0, "data/assets/scripts/silver")
    import importlib  # noqa: PLC0415
    rs = importlib.import_module("rebalancer_schemas")
    import opal_strategy_matcher as osm  # noqa: PLC0415
    rs.opal_sma_member_of("PFDE Sleeve")
    src = getattr(rs, "STRATEGY_CONFIG_SOURCE", None)
    if src != "s3://opal-data-etfs/config/etf_universe.json":
        print("W26-LIVE-BAD STRATEGY_CONFIG_SOURCE=%r (the default path does not read the S3 list)" % (src,))
        return 1
    import boto3  # noqa: PLC0415
    import pyarrow.parquet as pq  # noqa: PLC0415
    with open("infra/aws/etfs/config/etf_universe.json", encoding="utf-8") as f:
        repo = osm.StrategyMatcher(json.load(f))
    s3 = boto3.client("s3", region_name="us-east-1")
    names = set()
    for table, cols in (("fact_model_roster", ["model_name"]),
                        ("fact_model_definition", ["model_name", "sleeve_name", "component_name"])):
        keys = [o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=SILVER + table + "/date=")
                for o in pg.get("Contents", []) if o["Key"].endswith(".parquet")]
        t = pq.read_table(io.BytesIO(s3.get_object(Bucket=BUCKET, Key=max(keys))["Body"].read()), columns=cols).to_pandas()
        for c in cols:
            names |= {str(v) for v in t[c].dropna().unique()}
    diff = []
    for n in sorted(names):
        def m(fn):
            try:
                return fn(n)
            except ValueError:
                return "RAISE"
        a, b = m(rs.opal_sma_member_of), m(repo.member_of)
        if a != b:
            diff.append((n, a, b))
    print("SOURCE: %s; DENOMINATOR: %d names; differ: %d" % (src, len(names), len(diff)))
    for d in diff[:10]:
        print("   ", d)
    if diff:
        print("W26-LIVE-BAD")
        return 1
    print("W26-LIVE-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
