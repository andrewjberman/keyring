#!/usr/bin/env python3
"""issuer_check_sc_e42.py -- MDPF_SECCLASS round 9 issuer check for cell SC-e-42 (FWD-5, FWD-2): a07 reads canonical first.

Reads the newest M/A07_SWITCH_BEFORE_AFTER_*.json the worker writes: {"as_of", "denominator": <int>, "rows": [{"key", "before_class",
"after_class", "source": "canonical"|"old_list"|"unclassified"}, ...]}. It passes only when the rows number the denominator (> 0), every
row's source is one of the three, and every row whose source is "canonical" carries an after_class equal to that key's asset_class in
etf-classifications on a fresh consistent read (batch_get_item, 100 keys a call). Positive control: AAETX reads present. Prints
SC-E42-SWITCH ok=<bool> rows=<n> canonical=<n> old_list=<n> unclassified=<n> mismatches=<n> control=<present|ABSENT>.
Read-only. Run from the repo root.
"""
import glob
import json
import os
import sys

import boto3

M = os.path.join("org", "tier1_exec", "2.0.0_SA_COO", "deliverables", "MDPF_SECCLASS_M")
TABLE = "etf-classifications"
SOURCES = ("canonical", "old_list", "unclassified")


def live_classes(client, keys):
    out = {}
    keys = list(dict.fromkeys(keys))
    for i in range(0, len(keys), 100):
        req = {TABLE: {"Keys": [{"ticker": {"S": k}} for k in keys[i:i + 100]], "ConsistentRead": True,
                       "ProjectionExpression": "ticker, asset_class"}}
        while req:
            resp = client.batch_get_item(RequestItems=req)
            for it in resp.get("Responses", {}).get(TABLE, []):
                out[it["ticker"]["S"]] = it.get("asset_class", {}).get("S")
            req = resp.get("UnprocessedKeys") or None
    return out


def main():
    hits = sorted(glob.glob(os.path.join(M, "A07_SWITCH_BEFORE_AFTER_*.json")))
    if not hits:
        print("SC-E42-SWITCH ok=False no A07_SWITCH_BEFORE_AFTER_*.json")
        return 1
    with open(hits[-1], encoding="utf-8") as fh:
        doc = json.load(fh)
    rows = doc.get("rows", [])
    if not rows or doc.get("denominator") != len(rows):
        print(f"SC-E42-SWITCH ok=False rows={len(rows)} denominator={doc.get('denominator')}")
        return 1
    bad_src = [r for r in rows if r.get("source") not in SOURCES]
    client = boto3.client("dynamodb", region_name="us-east-1")
    canon = [r for r in rows if r.get("source") == "canonical"]
    live = live_classes(client, [r["key"] for r in canon] + ["AAETX"])
    mism = [r["key"] for r in canon if live.get(r["key"]) != r.get("after_class")]
    control = "present" if "AAETX" in live else "ABSENT"
    counts = {s: sum(1 for r in rows if r.get("source") == s) for s in SOURCES}
    ok = not bad_src and not mism and control == "present"
    print(f"SC-E42-SWITCH ok={ok} rows={len(rows)} canonical={counts['canonical']} old_list={counts['old_list']} "
          f"unclassified={counts['unclassified']} mismatches={len(mism)} control={control}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
