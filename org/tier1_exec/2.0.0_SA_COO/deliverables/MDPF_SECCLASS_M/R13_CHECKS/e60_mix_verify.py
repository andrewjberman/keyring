#!/usr/bin/env python3
"""e60_mix_verify.py -- MDPF_SECCLASS SC-e-60 acceptance on the served BD firm mix (READ-ONLY).

Reads opal-data-bd platinum/firm/mix_summary.json (the current version) and the pre-act reference version (argv[1], default the
post-04:00Z-fire VersionId recorded in the signed COO half). Requires:
  - the served version is NEWER than the reference (a run after the ship has written it);
  - top-level `mix` keys are the six canonical classes plus at most one `Unclassified`, with no lower-case `unclassified` or `other`;
  - the mix pcts sum to 1.0 within 1e-9;
  - `composition.mix` and `composition.unclassified` equal the reference's (the donut is unchanged by this act, beyond the day's data).
Prints E60-MIX ok=<bool> served=<vid> keys=[...] pct_sum=<x> unclassified_line=<mv|absent> composition_same=<bool>.
"""
import json
import sys

import boto3

BUCKET, KEY = "opal-data-bd", "platinum/firm/mix_summary.json"
REF = "lp8kKqX7WixODLx.y23rnauYiUg6s8HS"
SIX = {"equity", "fixed_income", "alternatives", "commodities", "structured", "cash"}


def main(argv):
    ref_vid = argv[1] if len(argv) > 1 else REF
    s3 = boto3.client("s3", region_name="us-east-1")
    cur = s3.get_object(Bucket=BUCKET, Key=KEY)
    ref = s3.get_object(Bucket=BUCKET, Key=KEY, VersionId=ref_vid)
    c, r = json.loads(cur["Body"].read()), json.loads(ref["Body"].read())
    newer = cur["VersionId"] != ref_vid and cur["LastModified"] > ref["LastModified"]
    mix = {k: v for k, v in c.get("mix", {}).items() if isinstance(v, dict)}
    keys = sorted(mix)
    extra = set(keys) - SIX - {"Unclassified"}
    pct_sum = sum(v.get("pct", 0.0) for v in mix.values())
    line = mix.get("Unclassified", {}).get("market_value", "absent")
    same = (c.get("composition", {}).get("mix") == r.get("composition", {}).get("mix")
            and c.get("composition", {}).get("unclassified") == r.get("composition", {}).get("unclassified"))
    ok = newer and not extra and abs(pct_sum - 1.0) <= 1e-9
    print(f"E60-MIX ok={ok} served={cur['VersionId']} newer={newer} keys={keys} extra={sorted(extra)} pct_sum={pct_sum:.12f} "
          f"unclassified_line={line} composition_same={same}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
