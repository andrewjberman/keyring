#!/usr/bin/env python3
"""clean_name_row_set.py -- MDPF_SECCLASS round 8, cell SC-e-34 (FWD-14): the clean-name row set.

READ-ONLY. One consistent scan of DynamoDB etf-classifications, then writes
  org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_20261007.tsv
tab-separated, header  key  classified_by  current_name  clean_name  action , one line per row whose `name` is non-blank:
  clean_name = security_name.clean_name(current_name)   (the one function, SC-e-30)
  action     = UNCHANGED when equal, else SEED-SOURCE for a `seed` row (the seed source owns the correction), else WRITE.
A row with no name has no source name in the table and is outside the set; its count is printed.
"""
import csv
import sys
from collections import Counter
from pathlib import Path

_REPO = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(_REPO / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"))
OUT = _REPO / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_20261007.tsv"
COLS = ["key", "classified_by", "current_name", "clean_name", "action"]


def scan():
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
    from security_name import clean_name
    live = scan()
    rows, bad = [], []
    for key in sorted(live):
        name, by = live[key]
        if not name or not name.strip():
            continue
        if "\t" in name or "\n" in name or "\r" in name:
            bad.append(key)
        clean = clean_name(name)
        action = "UNCHANGED" if clean == name else ("SEED-SOURCE" if by == "seed" else "WRITE")
        rows.append([key, by, name, clean, action])
    if bad:
        print("REFUSED: a name holds a tab or newline (set would be ambiguous): " + ",".join(bad[:10]))
        return 1
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, quotechar=None, escapechar=None)
        w.writerow(COLS)
        w.writerows(rows)
    c = Counter(r[4] for r in rows)
    print(f"CLEAN-NAME-ROW-SET rows_scanned={len(live)} named={len(rows)} unnamed={len(live) - len(rows)} "
          f'write={c["WRITE"]} seed_source={c["SEED-SOURCE"]} unchanged={c["UNCHANGED"]} -> {OUT.name}')
    return 0


if __name__ == "__main__":
    sys.exit(main())
