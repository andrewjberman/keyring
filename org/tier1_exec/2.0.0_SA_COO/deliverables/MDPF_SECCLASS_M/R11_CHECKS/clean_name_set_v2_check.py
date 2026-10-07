#!/usr/bin/env python3
"""clean_name_set_v2_check.py -- MDPF_SECCLASS round 9, cell SC-e-48 (FWD-14, analysis ruling 2.2): the issuer's check of the
regenerated clean-name row set. The worker does not edit this file. READ-ONLY: one consistent scan of etf-classifications.

Reads the newest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_V2_*.tsv, tab-separated, header
  key	classified_by	current_name	source_name	clean_name	action	source
and PASSES only if:
  - every live row whose `name` is non-blank appears exactly once with source `table`, current_name equal to the live name,
    clean_name == security_name.clean_name(current_name), and action UNCHANGED (equal) / SEED-SOURCE (a `seed` row) / WRITE;
  - every other line is a HELD row with no live name: source `custody:<firm>`, current_name empty, a non-empty source_name,
    clean_name == clean_name(source_name), action WRITE (or SEED-SOURCE for a seed row), and its key exists in the live table;
  - no key appears twice; at least one table row; no value holds a tab or newline.
Prints CLEAN-NAME-SET-V2 ok=True|False rows=<n> table=<n> custody=<n> write=<n> seed_source=<n> unchanged=<n>.
"""
import csv
import glob
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(_REPO / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"))
HOME = _REPO / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M"
COLS = ["key", "classified_by", "current_name", "source_name", "clean_name", "action", "source"]


def live_rows():
    import boto3
    d = boto3.client("dynamodb", region_name="us-east-1")
    out = {}
    for pg in d.get_paginator("scan").paginate(TableName="etf-classifications", ConsistentRead=True,
                                               ProjectionExpression="ticker, #n, classified_by",
                                               ExpressionAttributeNames={"#n": "name"}):
        for it in pg["Items"]:
            out[it["ticker"]["S"]] = ((it.get("name") or {}).get("S") or "", (it.get("classified_by") or {}).get("S") or "")
    return out


def main():
    files = sorted(glob.glob(str(HOME / "CLEAN_NAME_ROW_SET_V2_*.tsv")))
    if not files:
        print("CLEAN-NAME-SET-V2 ok=False missing=CLEAN_NAME_ROW_SET_V2_*.tsv")
        return 1
    try:
        from security_name import clean_name
    except Exception as exc:  # noqa: BLE001 -- any import failure is a FAIL with its type printed
        print(f"CLEAN-NAME-SET-V2 ok=False import_error={type(exc).__name__}")
        return 1
    with open(files[-1], encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t"))
    if not rows or list(rows[0].keys()) != COLS:
        print(f"CLEAN-NAME-SET-V2 ok=False header={list(rows[0].keys()) if rows else None}")
        return 1
    live = live_rows()
    named = {k for k, (n, _) in live.items() if n.strip()}
    seen, probs, cnt = set(), [], {"table": 0, "custody": 0, "WRITE": 0, "SEED-SOURCE": 0, "UNCHANGED": 0}
    for r in rows:
        k = r["key"]
        if k in seen:
            probs.append(f"dup:{k}")
        seen.add(k)
        if k not in live:
            probs.append(f"absent:{k}")
            continue
        lname, lcls = live[k]
        cnt[r["action"]] = cnt.get(r["action"], 0) + 1
        if r["source"] == "table":
            cnt["table"] += 1
            want = "UNCHANGED" if clean_name(lname) == lname else ("SEED-SOURCE" if lcls == "seed" else "WRITE")
            if r["current_name"] != lname or r["clean_name"] != clean_name(lname) or r["action"] != want:
                probs.append(f"table:{k}")
        elif r["source"].startswith("custody:"):
            cnt["custody"] += 1
            want = "SEED-SOURCE" if lcls == "seed" else "WRITE"
            if lname.strip() or r["current_name"] or not r["source_name"].strip() or \
                    r["clean_name"] != clean_name(r["source_name"]) or r["action"] != want:
                probs.append(f"custody:{k}")
        else:
            probs.append(f"source:{k}")
    missing = named - {r["key"] for r in rows if r["source"] == "table"}
    if missing:
        probs.append(f"named_not_listed={len(missing)}")
    ok = not probs and cnt["table"] > 0
    print(f"CLEAN-NAME-SET-V2 ok={ok} rows={len(rows)} table={cnt['table']} custody={cnt['custody']} write={cnt['WRITE']} "
          f"seed_source={cnt['SEED-SOURCE']} unchanged={cnt['UNCHANGED']} problems={probs[:3]}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
