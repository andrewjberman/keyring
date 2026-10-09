"""MDPF_STRATID workstream 2, W2-2 criterion AC2 (SEAM, real neighbour): over every distinct name in Cottonwood's Rebalancer
silver on its latest date (fact_model_roster.model_name + fact_model_definition model_name/sleeve_name/component_name), the new
matcher built from the repo ETF list gives the SAME member as today's rules (frozen below, copied from
rebalancer_schemas.py:218-223 at f3cc1552bf), except where it names a member today's rules did not (printed, counted, allowed only
for a full-name or data-rule hit). Read-only S3. W22-SEAM-OK, else W22-SEAM-BAD. Run from the repo (worktree) root."""
from __future__ import annotations

import io
import json
import re
import sys

TODAY = (
    (re.compile(r"(?<![A-Za-z0-9])DIVZ(?![A-Za-z0-9])", re.I), "divz"),
    (re.compile(r"(?<![A-Za-z0-9])IDVZ(?![A-Za-z0-9])", re.I), "idvz"),
    (re.compile(r"(?<![A-Za-z0-9])PFDE(?![A-Za-z0-9])|Pathfinder\s+Disciplined", re.I), "pfde"),
    (re.compile(r"(?<![A-Za-z0-9])PFOE(?![A-Za-z0-9])|Pathfinder\s+Focused\s+Opportunit", re.I), "pfoe"),
)
BUCKET = "opal-data-assets"
SILVER = "blackdiamond/cottonwood/silver/"


def today(name):
    hits = sorted({m for rx, m in TODAY if rx.search(name)})
    return hits[0] if len(hits) == 1 else ("RAISE" if hits else None)


def main() -> int:
    sys.path.insert(0, "data/assets/scripts/silver")
    try:
        import opal_strategy_matcher as osm  # noqa: PLC0415
    except Exception as exc:  # noqa: BLE001
        print("W22-SEAM-BAD matcher not importable: %s" % exc)
        return 1
    import boto3  # noqa: PLC0415
    import pyarrow.parquet as pq  # noqa: PLC0415
    with open("infra/aws/etfs/config/etf_universe.json", encoding="utf-8") as f:
        m = osm.StrategyMatcher(json.load(f))
    s3 = boto3.client("s3", region_name="us-east-1")
    names, src = set(), []
    for table, cols in (("fact_model_roster", ["model_name"]),
                        ("fact_model_definition", ["model_name", "sleeve_name", "component_name"])):
        keys = []
        for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=SILVER + table + "/date="):
            keys += [o["Key"] for o in page.get("Contents", []) if o["Key"].endswith(".parquet")]
        key = max(keys)
        src.append(key)
        t = pq.read_table(io.BytesIO(s3.get_object(Bucket=BUCKET, Key=key)["Body"].read()), columns=cols).to_pandas()
        for c in cols:
            names |= {str(v) for v in t[c].dropna().unique()}
    diff, gained = [], []
    for n in sorted(names):
        old = today(n)
        try:
            new = m.member_of(n)
        except ValueError:
            new = "RAISE"
        if old == new:
            continue
        (gained if old is None and new not in (None, "RAISE") else diff).append((n, old, new))
    print("SOURCE: %s" % ", ".join(src))
    print("DENOMINATOR: %d distinct names" % len(names))
    print("same: %d; gained (new member where today's rules had none): %d; changed: %d"
          % (len(names) - len(diff) - len(gained), len(gained), len(diff)))
    for row in gained + diff:
        print("   ", row)
    if diff:
        print("W22-SEAM-BAD %d name(s) changed member" % len(diff))
        return 1
    print("W22-SEAM-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
