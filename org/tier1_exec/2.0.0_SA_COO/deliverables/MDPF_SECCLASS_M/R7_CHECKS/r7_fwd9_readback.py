#!/usr/bin/env python3
"""r7_fwd9_readback.py -- the FWD-9 rows half's acceptance read for one branch (READ-ONLY).

For every WRITE line of FWD9_ROW_SET_20261005.tsv in the named --namespace, a consistent get of its key on
`etf-classifications`, graded against the planned item:
  MATCH     the row carries the planned class, sub-class (or none), classified_by scheduled, updated_by
            rivalfunds-backfill, and for a BLOOMBERG row identifier_namespace BLOOMBERG, the verbatim
            security_bloomberg, the planned listing_country, and no name
  DIFFERS   the row exists and one of those fields differs (each named)
  ABSENT    no row
Then a consistent COUNT scan of the table. Prints
`FWD9-READBACK namespace=<ns> keys=<n> match=<n> differs=<n> absent=<n> table_count=<n>`.

Usage (repo root): python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R7_CHECKS/r7_fwd9_readback.py --namespace BLOOMBERG
"""
from __future__ import annotations

import argparse
import concurrent.futures
import json
from pathlib import Path

import boto3
from botocore.config import Config

HERE = Path(__file__).resolve().parent
SET_FILE = HERE / "FWD9_ROW_SET_20261005.tsv"
TABLE = "etf-classifications"
CHECKED = ("asset_class", "sub_asset_class", "instrument_kind", "classified_by", "updated_by", "identifier_namespace",
           "security_bloomberg", "listing_country", "low_confidence")


def planned(namespace):
    rows = {}
    for line in SET_FILE.read_text(encoding="utf-8").splitlines():
        f = line.split("\t")
        if len(f) == 5 and f[0] == "WRITE":
            item = json.loads(f[4])
            item.pop("days", None)
            if item.get("identifier_namespace", "TICKER") == namespace:
                rows[f[1]] = item
    return rows


def grade(want, got):
    if got is None:
        return "ABSENT", []
    diffs = [k for k in CHECKED if (want.get(k) if k != "low_confidence" else bool(want.get(k)))
             != (got.get(k) if k != "low_confidence" else bool(got.get(k)))]
    if want.get("identifier_namespace") == "BLOOMBERG" and "name" in got:
        diffs.append("name present")
    return ("DIFFERS" if diffs else "MATCH"), diffs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--namespace", choices=("BLOOMBERG", "TICKER"), required=True)
    a = ap.parse_args()
    table = boto3.resource("dynamodb", region_name="us-east-1",
                           config=Config(retries={"max_attempts": 10, "mode": "standard"})).Table(TABLE)
    want = planned(a.namespace)

    def get(key):
        return key, table.get_item(Key={"ticker": key}, ConsistentRead=True).get("Item")

    out = {"MATCH": [], "DIFFERS": {}, "ABSENT": []}
    with concurrent.futures.ThreadPoolExecutor(max_workers=8) as pool:
        for key, item in pool.map(get, sorted(want)):
            verdict, diffs = grade(want[key], item)
            if verdict == "DIFFERS":
                out["DIFFERS"][key] = diffs
            else:
                out[verdict].append(key)
    n, kw = 0, {"Select": "COUNT", "ConsistentRead": True}
    while True:
        r = table.scan(**kw)
        n += r["Count"]
        if "LastEvaluatedKey" not in r:
            break
        kw["ExclusiveStartKey"] = r["LastEvaluatedKey"]
    for key, diffs in sorted(out["DIFFERS"].items()):
        print("DIFFERS %s %s" % (key, ",".join(diffs)))
    for key in out["ABSENT"]:
        print("ABSENT %s" % key)
    print("FWD9-READBACK namespace=%s keys=%d match=%d differs=%d absent=%d table_count=%d" % (
        a.namespace, len(want), len(out["MATCH"]), len(out["DIFFERS"]), len(out["ABSENT"]), n))


if __name__ == "__main__":
    main()
