#!/usr/bin/env python3
"""move_multi_asset_rows.py -- MDPF_SECCLASS batch 183 ONE packet: the 7 MOVES of existing `scheduled` rows to `multi_asset`.

The seed script cannot move them: its merge rule returns a CONFLICT wherever the table and the module both know a value and
disagree, and its caller refuses on any conflict. So each move is ONE conditional UpdateItem (compare-and-set): it lands only
if the row still reads exactly as recorded in the row set (asset_class, sub_asset_class, classified_by), and sets
asset_class = multi_asset, sub_asset_class = the set's sub class, classified_by = seed (a curated correction outranks a
scheduled row, MDPF_SECCLASS_CONTRACT.json), updated_by = mdpf-secclass-multi-asset, last_updated = now. Nothing else on the
row is touched.

Default is a DRY RUN: it reads each row (consistent get-item) and prints whether the condition holds -- MOVE (would land),
ALREADY (the row already reads the target), or REFUSED (the row moved since the set was read). --write performs the updates;
a ConditionalCheckFailed on any row is reported and the rest continue (each move is independent and individually reversible).

Run from the repo root:
  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/move_multi_asset_rows.py [--write]
"""
from __future__ import annotations

import argparse
import datetime
import sys
from pathlib import Path

import boto3

TABLE = "etf-classifications"
HERE = Path(__file__).resolve().parent
ROW_SET = HERE / "MULTI_ASSET_ROW_SET_20261003.tsv"
UPDATED_BY = "mdpf-secclass-multi-asset"


def moves():
    """[(ticker, (class, sub, classified_by) today, (class, sub) target)] from the row set's MOVE lines."""
    out = []
    for line in ROW_SET.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        f = line.split("\t")
        if f[0] != "MOVE":
            continue
        today = tuple(part.strip() for part in f[3].split("/"))
        out.append((f[1], today, (f[4], f[5])))
    return out


def main(write: bool) -> int:
    ddb = boto3.client("dynamodb", region_name="us-east-1")
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    rows = moves()
    assert len(rows) == 7, "the row set names %d MOVE lines, 7 expected" % len(rows)
    counts = {"MOVE": 0, "ALREADY": 0, "REFUSED": 0, "WRITTEN": 0, "FAILED": 0}
    for ticker, (cls, sub, by), (tcls, tsub) in rows:
        item = ddb.get_item(TableName=TABLE, Key={"ticker": {"S": ticker}}, ConsistentRead=True).get("Item", {})
        got = tuple((item.get(k) or {}).get("S") for k in ("asset_class", "sub_asset_class", "classified_by"))
        if got[:2] == (tcls, tsub):
            state = "ALREADY"
        elif got == (cls, sub, by):
            state = "MOVE"
        else:
            state = "REFUSED"
        counts[state] += 1
        print("%-8s %-6s today=%s target=%s" % (state, ticker, "/".join(map(str, got)), "/".join((tcls, tsub))))
        if write and state == "MOVE":
            try:
                ddb.update_item(
                    TableName=TABLE, Key={"ticker": {"S": ticker}},
                    UpdateExpression="SET asset_class = :tc, sub_asset_class = :ts, classified_by = :seed, "
                                     "updated_by = :by, last_updated = :now",
                    ConditionExpression="asset_class = :oc AND sub_asset_class = :os AND classified_by = :ob",
                    ExpressionAttributeValues={":tc": {"S": tcls}, ":ts": {"S": tsub}, ":seed": {"S": "seed"},
                                               ":by": {"S": UPDATED_BY}, ":now": {"S": now},
                                               ":oc": {"S": cls}, ":os": {"S": sub}, ":ob": {"S": by}})
                counts["WRITTEN"] += 1
            except ddb.exceptions.ConditionalCheckFailedException:
                counts["FAILED"] += 1
                print("   CONDITION FAILED at write: %s moved between the read and the write" % ticker)
    print(("WROTE" if write else "DRY RUN"), counts)
    return 0 if counts["REFUSED"] == 0 and counts["FAILED"] == 0 else 1


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    sys.exit(main(ap.parse_args().write))
