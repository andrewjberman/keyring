#!/usr/bin/env python3
"""issuer_check_sc_e44.py -- MDPF_SECCLASS round 9 issuer check for cell SC-e-44 (FWD-5, FWD-7, FWD-10): the producer's new input.

Reads the newest M/PRODUCER_INPUT_DRY_RUN_*.json the worker writes: {"as_of", "held_source": "<...> inferred", "planned": [{"key",
"input": <name of the non-old-list input>, "asset_class"}, ...], "old_list_reads": <int>}. It passes only when planned is non-empty, no
planned row names an input containing 'bd-securities' or 'old', old_list_reads is 0, every planned asset_class is one of the six classes,
and every planned key is ABSENT from etf-classifications on a fresh consistent read (the producer plans only keys the table lacks; a
present one is a double write). Positive control: AAETX reads present. Prints SC-E44-INPUT ok=<bool> planned=<n> present=<n>
off_class=<n> old_list_reads=<n> control=<present|ABSENT>. Read-only. Run from the repo root.
"""
import glob
import json
import os
import sys

import boto3

M = os.path.join("org", "tier1_exec", "2.0.0_SA_COO", "deliverables", "MDPF_SECCLASS_M")
TABLE = "etf-classifications"
SIX = {"cash", "fixed_income", "equity", "structured", "alternatives", "commodities"}


def present(client, keys):
    found = set()
    keys = list(dict.fromkeys(keys))
    for i in range(0, len(keys), 100):
        req = {TABLE: {"Keys": [{"ticker": {"S": k}} for k in keys[i:i + 100]], "ConsistentRead": True,
                       "ProjectionExpression": "ticker"}}
        while req:
            resp = client.batch_get_item(RequestItems=req)
            found.update(it["ticker"]["S"] for it in resp.get("Responses", {}).get(TABLE, []))
            req = resp.get("UnprocessedKeys") or None
    return found


def main():
    hits = sorted(glob.glob(os.path.join(M, "PRODUCER_INPUT_DRY_RUN_*.json")))
    if not hits:
        print("SC-E44-INPUT ok=False no PRODUCER_INPUT_DRY_RUN_*.json")
        return 1
    with open(hits[-1], encoding="utf-8") as fh:
        doc = json.load(fh)
    planned = doc.get("planned", [])
    if not planned:
        print("SC-E44-INPUT ok=False planned is empty")
        return 1
    bad_input = [p for p in planned if "bd-securities" in str(p.get("input", "")) or "old" in str(p.get("input", "")).lower()]
    off = [p for p in planned if p.get("asset_class") not in SIX]
    client = boto3.client("dynamodb", region_name="us-east-1")
    found = present(client, [p["key"] for p in planned] + ["AAETX"])
    pres = [p["key"] for p in planned if p["key"] in found]
    control = "present" if "AAETX" in found else "ABSENT"
    ok = not bad_input and not off and not pres and doc.get("old_list_reads") == 0 and control == "present"
    print(f"SC-E44-INPUT ok={ok} planned={len(planned)} present={len(pres)} off_class={len(off)} "
          f"old_list_reads={doc.get('old_list_reads')} control={control}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
