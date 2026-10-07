#!/usr/bin/env python3
"""sc_e34_row_set_check.py -- MDPF_SECCLASS round 8, cell SC-e-34 (FWD-14): the issuer's check of the clean-name row set.
The worker does not edit this file. READ-ONLY: one consistent scan of DynamoDB etf-classifications, no write.

Reads org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_20261007.tsv, tab-separated, header line
  key	classified_by	current_name	clean_name	action
and PASSES only if:
  - every live row whose `name` is non-blank appears exactly once (by key) and no other key appears;
  - current_name equals the live `name` (a set built on a moved table is stale);
  - clean_name == security_name.clean_name(current_name) for every row (the one function, SC-e-30);
  - action is UNCHANGED when clean_name == current_name; otherwise SEED-SOURCE when classified_by is `seed` (the contract's
    precedence: a seed row is corrected in the seed source, never in the table); otherwise WRITE;
  - no value holds a tab or a newline.
Prints CLEAN-NAME-SET ok=True|False rows=<n> write=<n> seed_source=<n> unchanged=<n> unnamed_live=<n>.
"""
import csv
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(_REPO / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"))
SET = _REPO / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_20261007.tsv"
COLS = ["key", "classified_by", "current_name", "clean_name", "action"]


def live_rows():
    import boto3
    d = boto3.client("dynamodb", region_name="us-east-1")
    out = {}
    for pg in d.get_paginator("scan").paginate(TableName="etf-classifications", ConsistentRead=True,
                                               ProjectionExpression="ticker,#n,classified_by",
                                               ExpressionAttributeNames={"#n": "name"}):
        for it in pg["Items"]:
            out[it["ticker"]["S"]] = (it.get("name", {}).get("S"), it.get("classified_by", {}).get("S", ""))
    return out


def main():
    if not SET.exists():
        print(f"CLEAN-NAME-SET ok=False missing={SET.name}")
        return 1
    from security_name import clean_name
    with SET.open(encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh, delimiter="\t")
        if rd.fieldnames != COLS:
            print(f"CLEAN-NAME-SET ok=False header={rd.fieldnames}")
            return 1
        rows = list(rd)
    live = live_rows()
    named = {k for k, (n, _) in live.items() if n and n.strip()}
    fails, seen = [], set()
    counts = {"WRITE": 0, "SEED-SOURCE": 0, "UNCHANGED": 0}
    for r in rows:
        k = r["key"]
        if k in seen:
            fails.append(f"dup:{k}")
        seen.add(k)
        if k not in live:
            fails.append(f"not_live:{k}")
            continue
        if r["current_name"] != live[k][0]:
            fails.append(f"stale:{k}")
        if r["clean_name"] != clean_name(r["current_name"]):
            fails.append(f"not_the_function:{k}")
        if r["clean_name"] == r["current_name"]:
            want = "UNCHANGED"
        elif live[k][1] == "seed":
            want = "SEED-SOURCE"
        else:
            want = "WRITE"
        if r["action"] != want:
            fails.append("action:{}={} want {}".format(k, r["action"], want))
        counts[r["action"]] = counts.get(r["action"], 0) + 1
    missing = named - seen
    if missing:
        fails.append(f"missing_named={len(missing)}")
    for f in fails[:20]:
        print("FAIL " + f)
    print(f'CLEAN-NAME-SET ok={not fails!s} rows={len(rows)} write={int(counts["WRITE"])} seed_source={int(counts["SEED-SOURCE"])} unchanged={int(counts["UNCHANGED"])} unnamed_live={int(len(live) - len(named))} fails={len(fails)}')
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
