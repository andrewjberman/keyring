"""MDPF_STRATID ST-w-8 (row D1-S7 follow-on, CloudOps~DELL1 msg 3151): the key-set identity holds when the Cottonwood slice carries
unidentified_strategies. Read-only S3; writes nothing.

  CONTROL  the 4 served aggregate-aua-timeseries docs (global, 49financial, inflection, cottonwood; latest date) with Cottonwood given
           an `unidentified_strategies` block: assert_keyset_identity raises (the defect, reproduced).
  ARM      the same docs through apply_sma_sleeve_overlay(arts) first: every scope carries `unidentified_strategies` (Cottonwood's block
           unchanged, the others None), assert_keyset_identity passes, and no figure moves (opal_aggregate_aua per scope equal).
W28-KEYSET-OK when both hold; else W28-KEYSET-BAD naming the arm.
"""
from __future__ import annotations

import copy
import json
import os
import sys

B = "opal-data-assets"
SCOPES = ("global", "49financial", "inflection", "cottonwood")
BLOCK = {"as_of": "2026-10-08", "firm_id": "cottonwood", "names_scanned": 18, "config_source": "s3://opal-data-etfs/config/etf_universe.json",
         "rows": [{"firm_id": "cottonwood", "name": "Opal_Muni_Sleeve", "dollars": 550823.07, "reason": "RULE_NOT_COUNTED"}]}


def _bad(m):
    print("W28-KEYSET-BAD " + m)
    return 1


def main():
    sys.path.insert(0, os.path.abspath(os.path.join("data", "mdpf", "scripts", "gold")))
    import boto3
    import mdpf_gold_consolidator as gc

    s3 = boto3.client("s3")
    docs = {}
    for sc in SCOPES:
        keys = []
        for p in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="portal/gold/mdpf/%s/aggregate-aua-timeseries/" % sc):
            keys += [o["Key"] for o in p.get("Contents", []) if o["Key"].endswith(".json")]
        docs[sc] = json.loads(s3.get_object(Bucket=B, Key=sorted(keys)[-1])["Body"].read())
    docs["cottonwood"]["unidentified_strategies"] = copy.deepcopy(BLOCK)
    try:
        gc.assert_keyset_identity(copy.deepcopy(docs), "aggregate-aua-timeseries")
        return _bad("arm=control the defect does not reproduce (identity passed with the key on Cottonwood only)")
    except SystemExit:
        pass
    before = {s: d.get("opal_aggregate_aua", [None])[-1] for s, d in docs.items()}
    out = gc.apply_sma_sleeve_overlay(copy.deepcopy(docs))
    for sc in SCOPES:
        if "unidentified_strategies" not in out[sc]:
            return _bad("arm=pad scope %s lacks unidentified_strategies" % sc)
    if out["cottonwood"]["unidentified_strategies"] != BLOCK:
        return _bad("arm=pad Cottonwood's block changed")
    if any(out[s]["unidentified_strategies"] is not None for s in SCOPES if s != "cottonwood"):
        return _bad("arm=pad a non-Cottonwood scope carries a non-None block")
    try:
        gc.assert_keyset_identity(out, "aggregate-aua-timeseries")
    except SystemExit as e:
        return _bad("arm=identity still fails: %s" % str(e)[:300])
    after = {s: out[s].get("opal_aggregate_aua", [None])[-1] for s in SCOPES}
    if any(before[s] is not None and abs((after[s] or 0) - before[s]) > 0.01 for s in SCOPES if s != "global"):
        return _bad("arm=figures a per-firm total moved: %r -> %r" % (before, after))
    print("CONTROL identity fails with the key on Cottonwood only | ARM 4/4 scopes carry it (Cottonwood block, others None), identity PASS, per-firm totals unchanged")
    print("W28-KEYSET-OK")
    return 0


if __name__ == "__main__":
    sys.exit(main())
