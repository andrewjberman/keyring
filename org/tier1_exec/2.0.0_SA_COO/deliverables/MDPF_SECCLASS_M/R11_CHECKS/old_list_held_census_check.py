#!/usr/bin/env python3
"""old_list_held_census_check.py -- MDPF_SECCLASS round 9, cell SC-e-50 (FWD-17, analysis rulings 2.4 and 2.5): the issuer's check.
The worker does not edit this file. READ-ONLY: one consistent scan of bd-securities (key only) and the contract file.

Modes (one verdict token each; run from the repo root):
  census -- the newest M/OLD_LIST_CENSUS_HELD_*.json (shape {"as_of", "held_definition", "claim", "denominator", "held",
            "not_held", "per_firm": {firm: n}}) has denominator == the live bd-securities row count, held + not_held ==
            denominator, a held_definition naming "non-zero market value", and claim `inferred` (ruling 2.9).
            Prints OLD-LIST-HELD-CENSUS ok=True|False.
  set    -- the newest M/OLD_LIST_RECLASSIFY_SET_V2_*.tsv (header old_key shared_key held route asset_class sub_asset_class
            clean_name) carries every live old key once; every DIRECT row carries a sub_asset_class that is a member of the
            contract's closed list for its asset_class (fields.sub_asset_class.values_by_class, SC-e-54), cash included; every AI
            row is BLANK in asset_class and sub_asset_class (no verdict exists before the model runs; the bound is graded on the
            AI path's output, after its half) -- AMENDMENT 1 (2.0.0_SA_COO~M1, row W36-S4); at least one cash row is planned.
            Prints OLD-LIST-SET-V2 ok=True|False with the per-route counts.
"""
import csv
import glob
import json
import sys
from pathlib import Path

HOME = Path(__file__).resolve().parents[1]
CONTRACT = "org/standards/MDPF_SECCLASS_CONTRACT.json"


def live_keys():
    import boto3
    d = boto3.client("dynamodb", region_name="us-east-1")
    keys = []
    for pg in d.get_paginator("scan").paginate(TableName="bd-securities", ConsistentRead=True):
        for it in pg["Items"]:
            k = next((v["S"] for v in it.values() if isinstance(v, dict) and "S" in v), None)
            keys.append(k)
    return len(keys)


def newest(pattern):
    hits = sorted(glob.glob(str(HOME / pattern)))
    return hits[-1] if hits else None


def census():
    f = newest("OLD_LIST_CENSUS_HELD_*.json")
    if not f:
        print("OLD-LIST-HELD-CENSUS ok=False missing=OLD_LIST_CENSUS_HELD_*.json")
        return 1
    with open(f, encoding="utf-8") as fh:
        c = json.load(fh)
    n = live_keys()
    probs = []
    if c.get("denominator") != n:
        probs.append(f"denominator {c.get('denominator')} != live {n}")
    if (c.get("held") or 0) + (c.get("not_held") or 0) != c.get("denominator"):
        probs.append("held+not_held != denominator")
    if "non-zero market value" not in str(c.get("held_definition", "")).lower():
        probs.append("held_definition")
    if c.get("claim") != "inferred":
        probs.append("claim")
    ok = not probs
    print(f"OLD-LIST-HELD-CENSUS ok={ok} live={n} held={c.get('held')} problems={probs[:3]}")
    return 0 if ok else 1


def rset():
    f = newest("OLD_LIST_RECLASSIFY_SET_V2_*.tsv")
    if not f:
        print("OLD-LIST-SET-V2 ok=False missing=OLD_LIST_RECLASSIFY_SET_V2_*.tsv")
        return 1
    with open(CONTRACT, encoding="utf-8") as fh:
        bound = ((json.load(fh).get("fields", {}).get("sub_asset_class") or {}).get("values_by_class")) or {}
    if not bound:
        print("OLD-LIST-SET-V2 ok=False contract has no sub_asset_class.values_by_class")
        return 1
    with open(f, encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    keys = [r["old_key"] for r in rows]
    n = live_keys()
    probs = []
    if len(keys) != n or len(set(keys)) != len(keys):
        probs.append(f"rows {len(keys)} vs live {n}")
    cash = direct = ai = 0
    for r in rows:
        if r["route"] == "DIRECT":
            direct += 1
            if r["sub_asset_class"] not in bound.get(r["asset_class"], []):
                probs.append(f"bound:{r['old_key']}")
            cash += r["asset_class"] == "cash"
        elif r["route"] == "AI":
            ai += 1
            if (r["asset_class"] or "").strip() or (r["sub_asset_class"] or "").strip():
                probs.append(f"ai_prefilled:{r['old_key']}")
    if cash == 0:
        probs.append("no cash row planned")
    ok = not probs
    print(f"OLD-LIST-SET-V2 ok={ok} rows={len(rows)} live={n} direct={direct} ai={ai} cash_planned={cash} problems={probs[:3]}")
    return 0 if ok else 1


if __name__ == "__main__":
    mode = sys.argv[1] if len(sys.argv) > 1 else ""
    sys.exit(census() if mode == "census" else rset() if mode == "set" else (print("usage: census|set") or 2))
