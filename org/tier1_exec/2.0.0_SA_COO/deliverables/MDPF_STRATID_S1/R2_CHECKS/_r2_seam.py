"""MDPF_STRATID round 2 (workstream 1): shared read-only seam inputs for ST-u-1 and ST-u-2.

Reads, live and read-only: the served Global aggregate timeseries (latest dated key under portal/gold/mdpf/global/) and the
Cottonwood slice the fold consumes. Rebuilds Global's PRE-SLEEVE-FOLD doc from the served one (the served doc already carries
round 1's PFDE fold): opal_aggregate_aua minus sma_additive_aua per date, the additive firm-sleeve by_model entries dropped,
sma_additive_aua all-None, sma_additive_withheld []. Writes nothing.
"""
from __future__ import annotations

import copy
import json
import os
import sys

BUCKET = "opal-data-assets"
GOLD = os.path.join("data", "mdpf", "scripts", "gold")
COT_KEY = "gold/mdpf_revamp/cottonwood/aggregate_aua_timeseries.json"


def load():
    sys.path.insert(0, os.path.abspath(GOLD))
    import boto3

    s3 = boto3.client("s3")
    keys = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix="portal/gold/mdpf/global/aggregate-aua-timeseries/"):
        keys += [o["Key"] for o in page.get("Contents", []) if o["Key"].endswith(".json")]
    if not keys:
        raise SystemExit("SEAM-BAD arm=input no served Global key")
    gkey = sorted(keys)[-1]
    g = json.loads(s3.get_object(Bucket=BUCKET, Key=gkey)["Body"].read())
    cot = json.loads(s3.get_object(Bucket=BUCKET, Key=COT_KEY)["Body"].read())
    print("inputs: %s (%d dates) | %s (last %s)" % (gkey, len(g["dates"]), COT_KEY, cot["dates"][-1]))
    return g, cot


def pre_fold(g: dict) -> dict:
    """The served Global doc with round 1's sleeve fold taken back out (Tax untouched)."""
    p = copy.deepcopy(g)
    add = p.get("sma_additive_aua") or [None] * len(p["dates"])
    p["opal_aggregate_aua"] = [None if t is None else round(t - (a or 0.0), 2) for t, a in zip(p["opal_aggregate_aua"], add)]
    p["by_model"] = {k: v for k, v in p["by_model"].items()
                     if not (v.get("source_basis") == "additive" and v.get("firms"))}
    p["sma_additive_aua"] = [None] * len(p["dates"])
    p["sma_additive_withheld"] = []
    return p


def cot_at(cot: dict, member: str, day: str):
    """(value, overlap) of a Cottonwood sma member on a Global date, or (None, None)."""
    if day not in cot["dates"] or member not in cot["by_model"]:
        return None, None
    i = cot["dates"].index(day)
    e = cot["by_model"][member]
    ov = e.get("overlap_model_value")
    return e["model_value"][i], (ov[i] if ov else None)
