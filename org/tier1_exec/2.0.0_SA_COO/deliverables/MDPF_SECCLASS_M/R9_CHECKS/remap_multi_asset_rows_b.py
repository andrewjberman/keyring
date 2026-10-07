#!/usr/bin/env python3
"""remap_multi_asset_rows_b.py -- MDPF_SECCLASS: remap the 33 `multi_asset` rows of etf-classifications into the six classes (Andrew-direct
2026-10-07: no multi-asset class; "I like B": target-date, balanced and allocation funds to equity, income-oriented funds to fixed income).

One CONDITIONAL UpdateItem per row (compare-and-set), the same shape as move_multi_asset_rows.py: it lands only if the row still reads
exactly as the set file recorded (asset_class multi_asset, the old sub-class, the old classified_by). It sets asset_class to the target,
updated_by = mdpf-secclass-remap-b, last_updated = now; the sub-class is RESTORED where the set names one (the five rows that read the
same class before batch 183) and otherwise REMOVED with low_confidence = true. classified_by and every other attribute are untouched.

DRY RUN by default (consistent get-item per row: MOVE / ALREADY / REFUSED). `--write` needs `--half <path>` whose `## COO half` and `## CTO half`
headings both read SIGNED, and it first writes the full pre-state of every row to `--snapshot <path>` (the rollback source). A condition failure on
one row is reported and the rest continue (each move is independent and individually reversible).

  python .../remap_multi_asset_rows_b.py                         # dry run
  python .../remap_multi_asset_rows_b.py --write --half <half.md> --snapshot <rollback.json>
  python .../remap_multi_asset_rows_b.py --rollback <rollback.json> [--write]   # put each row back exactly as snapshotted (conditional on the remapped state)
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

import boto3

TABLE = "etf-classifications"
HERE = Path(__file__).resolve().parent
SET_FILE = HERE / "MULTI_ASSET_REMAP_B_SET_20261007.tsv"
UPDATED_BY = "mdpf-secclass-remap-b"
SIX = {"cash", "fixed_income", "equity", "structured", "alternatives", "commodities"}


def read_set():
    rows = []
    for line in SET_FILE.read_text(encoding="utf-8").splitlines():
        if not line or line.startswith("#"):
            continue
        f = line.split("\t")
        key, name, osub, oby, tcls, tsub = f[:6]
        assert tcls in SIX, "target class %r is not one of the six (row %s)" % (tcls, key)
        rows.append({"key": key, "name": name, "old_sub": osub, "old_by": oby, "tcls": tcls, "tsub": None if tsub == "-" else tsub})
    return rows


def s(item, k):
    return (item.get(k) or {}).get("S")


def half_signed(path):
    text = Path(path).read_text(encoding="utf-8")
    for who in ("COO", "CTO"):
        m = re.search(r"^## %s half\b[^\n]*$" % who, text, re.MULTILINE)
        if not m or not re.search(r"\bSIGNED\b", m.group(0).upper()) or re.search(r"NOT SIGNED|PENDING|UNSIGNED|WITHDRAWN", m.group(0).upper()):
            return False, "%s half is not SIGNED: %s" % (who, m.group(0) if m else "no heading")
    return True, "both halves read SIGNED"


def remap(write, half, snapshot):
    ddb = boto3.client("dynamodb", region_name="us-east-1")
    rows = read_set()
    print("SET: %d rows (equity %d, fixed_income %d)" % (len(rows), sum(r["tcls"] == "equity" for r in rows), sum(r["tcls"] == "fixed_income" for r in rows)))
    plan = []
    counts = {"MOVE": 0, "ALREADY": 0, "REFUSED": 0}
    for r in rows:
        item = ddb.get_item(TableName=TABLE, Key={"ticker": {"S": r["key"]}}, ConsistentRead=True).get("Item", {})
        got = (s(item, "asset_class"), s(item, "sub_asset_class"), s(item, "classified_by"))
        if got[0] == r["tcls"] and got[1] == r["tsub"]:
            state = "ALREADY"
        elif got == ("multi_asset", r["old_sub"], r["old_by"]):
            state = "MOVE"
        else:
            state = "REFUSED"
        counts[state] += 1
        plan.append((r, state, item))
        print("%-8s %-16s today=%s target=%s/%s" % (state, r["key"], "/".join(map(str, got)), r["tcls"], r["tsub"] or "(cleared)"))
    print("DRY RUN" if not write else "PLAN", counts)
    if not write:
        return 0 if counts["REFUSED"] == 0 else 1
    ok, why = half_signed(half) if half else (False, "no --half named")
    print("PRECONDITION half:", "MET" if ok else "NOT MET", "-", why)
    if not ok or counts["REFUSED"]:
        print("REFUSED: nothing written")
        return 4
    Path(snapshot).write_text(json.dumps({"taken_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "table": TABLE,
                                          "rows": {r["key"]: item for r, _s, item in plan}}, indent=1, sort_keys=True), encoding="utf-8")
    print("SNAPSHOT written:", snapshot, "(%d rows)" % len(plan))
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    written = failed = 0
    for r, state, _item in plan:
        if state != "MOVE":
            continue
        vals = {":tc": {"S": r["tcls"]}, ":by": {"S": UPDATED_BY}, ":now": {"S": now},
                ":oc": {"S": "multi_asset"}, ":os": {"S": r["old_sub"]}, ":ob": {"S": r["old_by"]}}
        if r["tsub"]:
            expr = "SET asset_class = :tc, sub_asset_class = :ts, updated_by = :by, last_updated = :now"
            vals[":ts"] = {"S": r["tsub"]}
        else:
            expr = "SET asset_class = :tc, updated_by = :by, last_updated = :now, low_confidence = :lc REMOVE sub_asset_class"
            vals[":lc"] = {"BOOL": True}
        try:
            ddb.update_item(TableName=TABLE, Key={"ticker": {"S": r["key"]}}, UpdateExpression=expr,
                            ConditionExpression="asset_class = :oc AND sub_asset_class = :os AND classified_by = :ob", ExpressionAttributeValues=vals)
            written += 1
        except ddb.exceptions.ConditionalCheckFailedException:
            failed += 1
            print("   CONDITION FAILED at write: %s moved between the read and the write" % r["key"])
    print("WROTE %d of %d; condition failures %d" % (written, counts["MOVE"], failed))
    return 0 if failed == 0 else 1


def rollback(path, write):
    """Put each remapped row back exactly as snapshotted (a full put of the snapshotted item), only where it still reads as remapped by this script."""
    ddb = boto3.client("dynamodb", region_name="us-east-1")
    snap = json.loads(Path(path).read_text(encoding="utf-8"))
    done = 0
    for key, old in sorted(snap["rows"].items()):
        cur = ddb.get_item(TableName=TABLE, Key={"ticker": {"S": key}}, ConsistentRead=True).get("Item", {})
        state = "RESTORE" if s(cur, "updated_by") == UPDATED_BY else "SKIP(not remapped by this script)"
        print("%-8s %s" % (state.split("(")[0], key))
        if write and state == "RESTORE":
            ddb.put_item(TableName=TABLE, Item=old, ConditionExpression="updated_by = :by", ExpressionAttributeValues={":by": {"S": UPDATED_BY}})
            done += 1
    print(("RESTORED %d" % done) if write else "DRY RUN (rollback)")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--half")
    ap.add_argument("--snapshot")
    ap.add_argument("--rollback")
    a = ap.parse_args()
    if a.rollback:
        sys.exit(rollback(a.rollback, a.write))
    if a.write and not a.snapshot:
        sys.exit("REFUSED: --write needs --snapshot <path>")
    sys.exit(remap(a.write, a.half, a.snapshot))
