#!/usr/bin/env python3
"""cash_row_write.py -- MDPF_SECCLASS round 12, cell SC-e-68 (FWD-2, FWD-16): the canonical CASH row to cash/Cash.

ONE row of `etf-classifications`, key `CASH` (the NAV-residual cash line, name "Cash & Cash Equivalents"). It reads
fixed_income / Ultra Short Duration, classified_by legacy. PRD v0.14 ruling 2.4 (SC-e-64): Cash is a sub-class of cash only.
The act is ONE conditional update_item:

  SET asset_class = 'cash', sub_asset_class = 'Cash', updated_by = 'mdpf-secclass-cash-row-r12'
  CONDITION classified_by = 'legacy' AND asset_class = 'fixed_income' AND sub_asset_class = 'Ultra Short Duration'

No other attribute is touched (classified_by stays `legacy`, name and last_updated are not written). A row that moved since the
read is refused (reported, never overwritten).

DRY RUN by default: one consistent get-item, no write of any kind. The client is wrapped with a counter of every mutating call, a
mutating call in dry-run mode raises, and the run asserts puts=0. Prints
  CASH-ROW-DRY-RUN write=<0|1> current=<class>/<sub> classified_by=<v> puts=0
and exits 0 when the one write is planned (write=1), 1 when the condition would refuse (write=0).
`--write` requires `--half <path>` (refuses unless the `## COO half` and `## CTO half` headings both read SIGNED) and
`--snapshot <path>` (the pre-state item, a consistent read, written before the update).
`--rollback <snapshot> [--write]`: puts the snapshot's asset_class, sub_asset_class and updated_by (or REMOVE updated_by if the
row had none) back, only where the row still reads asset_class = cash AND sub_asset_class = Cash AND updated_by = this run's value.

  python .../cash_row_write.py                                           # dry run
  python .../cash_row_write.py --write --half <half.md> --snapshot <snapshot.json>
  python .../cash_row_write.py --rollback <snapshot.json> [--write]
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

TABLE = "etf-classifications"
KEY = "CASH"
CUR_CLASS, CUR_SUB, CUR_BY = "fixed_income", "Ultra Short Duration", "legacy"
NEW_CLASS, NEW_SUB = "cash", "Cash"
UPDATED_BY = "mdpf-secclass-cash-row-r12"
MUTATING = ("put_item", "update_item", "delete_item", "batch_write_item", "transact_write_items", "execute_statement",
            "execute_transaction", "batch_execute_statement")


class CountingClient:
    """Wraps a boto3 DynamoDB client and counts every mutating call. In dry-run mode a mutating call raises instead of running."""

    def __init__(self, client, allow_mutation):
        self._c, self._allow, self.puts = client, allow_mutation, 0

    @property
    def exceptions(self):
        return self._c.exceptions

    def __getattr__(self, name):
        attr = getattr(self._c, name)
        if name not in MUTATING:
            return attr

        def guarded(*a, **kw):
            self.puts += 1
            if not self._allow:
                raise RuntimeError("dry run: refused mutating call " + name)
            return attr(*a, **kw)
        return guarded


def s(item, k):
    return (item.get(k) or {}).get("S")


def read_row(ddb):
    return ddb.get_item(TableName=TABLE, Key={"ticker": {"S": KEY}}, ConsistentRead=True).get("Item", {})


def as_planned(item):
    """The row must still read what the cell measured: legacy, fixed_income, Ultra Short Duration."""
    return bool(item) and s(item, "classified_by") == CUR_BY and s(item, "asset_class") == CUR_CLASS \
        and s(item, "sub_asset_class") == CUR_SUB


def half_signed(path):
    text = Path(path).read_text(encoding="utf-8")
    for who in ("COO", "CTO"):
        m = re.search(r"^## " + who + r" half\b[^\n]*$", text, re.MULTILINE)
        if not m or not re.search(r"\bSIGNED\b", m.group(0).upper()) or re.search(r"NOT SIGNED|PENDING|UNSIGNED|WITHDRAWN", m.group(0).upper()):
            return False, f"{who} half is not SIGNED: " + (m.group(0) if m else "no heading")
    return True, "both halves read SIGNED"


def run(write, half, snapshot):
    import boto3
    ddb = CountingClient(boto3.client("dynamodb", region_name="us-east-1"), allow_mutation=write)
    item = read_row(ddb)
    planned = as_planned(item)
    cur = f'{s(item, "asset_class")}/{s(item, "sub_asset_class")}'
    if not write:
        assert ddb.puts == 0, f"dry run made {ddb.puts} mutating calls"
        print(f'CASH-ROW-DRY-RUN write={1 if planned else 0} current={cur} classified_by={s(item, "classified_by")} puts={ddb.puts}')
        if not planned:
            print(f"REFUSED_STALE {KEY}: the row no longer reads {CUR_CLASS}/{CUR_SUB} classified_by={CUR_BY}")
        return 0 if planned else 1
    ok, why = half_signed(half) if half else (False, "no --half named")
    print("PRECONDITION half:", "MET" if ok else "NOT MET", "-", why)
    if not ok:
        print("REFUSED: nothing written")
        return 4
    if not planned:
        print(f'REFUSED_STALE {KEY}: reads {cur} classified_by={s(item, "classified_by")}; nothing written')
        return 1
    Path(snapshot).write_text(json.dumps({"taken_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "table": TABLE,
                                          "key": KEY, "updated_by": UPDATED_BY, "new": {"asset_class": NEW_CLASS, "sub_asset_class": NEW_SUB},
                                          "row": item}, indent=1, sort_keys=True), encoding="utf-8")
    print("SNAPSHOT written:", snapshot)
    try:
        ddb.update_item(TableName=TABLE, Key={"ticker": {"S": KEY}},
                        UpdateExpression="SET #ac = :ac, #sac = :sac, #by = :by",
                        ConditionExpression="#cb = :cb AND #ac = :curac AND #sac = :cursac",
                        ExpressionAttributeNames={"#ac": "asset_class", "#sac": "sub_asset_class", "#by": "updated_by",
                                                  "#cb": "classified_by"},
                        ExpressionAttributeValues={":ac": {"S": NEW_CLASS}, ":sac": {"S": NEW_SUB}, ":by": {"S": UPDATED_BY},
                                                   ":cb": {"S": CUR_BY}, ":curac": {"S": CUR_CLASS}, ":cursac": {"S": CUR_SUB}})
    except ddb.exceptions.ConditionalCheckFailedException:
        print(f"   CONDITION FAILED at write: {KEY} moved between the read and the write")
        print("WROTE 0 of 1; condition failures 1")
        return 1
    print("WROTE 1 of 1; condition failures 0")
    return 0


def rollback(path, write):
    import boto3
    ddb = CountingClient(boto3.client("dynamodb", region_name="us-east-1"), allow_mutation=write)
    snap = json.loads(Path(path).read_text(encoding="utf-8"))
    by = snap.get("updated_by", UPDATED_BY)
    old = snap["row"]
    cur = read_row(ddb)
    if s(cur, "updated_by") != by or s(cur, "asset_class") != NEW_CLASS or s(cur, "sub_asset_class") != NEW_SUB:
        print(f"SKIP {KEY} (not at this run's value)")
        print("ROLLED BACK 0, skipped 1" if write else "DRY RUN (rollback) skipped=1")
        return 0
    print("RESTORE", KEY, f'-> {s(old, "asset_class")}/{s(old, "sub_asset_class")}')
    if not write:
        print("DRY RUN (rollback) skipped=0")
        return 0
    vals = {":by": {"S": by}, ":ac": {"S": NEW_CLASS}, ":sac": {"S": NEW_SUB},
            ":oac": {"S": s(old, "asset_class")}, ":osac": {"S": s(old, "sub_asset_class")}}
    sets = ["#ac = :oac", "#sac = :osac"]
    removes = []
    if s(old, "updated_by") is not None:
        sets.append("#by = :oby")
        vals[":oby"] = {"S": s(old, "updated_by")}
    else:
        removes.append("#by")
    expr = "SET " + ", ".join(sets) + ((" REMOVE " + ", ".join(removes)) if removes else "")
    try:
        ddb.update_item(TableName=TABLE, Key={"ticker": {"S": KEY}}, UpdateExpression=expr,
                        ConditionExpression="#ac = :ac AND #sac = :sac AND #by = :by",
                        ExpressionAttributeNames={"#ac": "asset_class", "#sac": "sub_asset_class", "#by": "updated_by"},
                        ExpressionAttributeValues=vals)
    except ddb.exceptions.ConditionalCheckFailedException:
        print(f"   CONDITION FAILED at rollback: {KEY} moved")
        print("ROLLED BACK 0, skipped 1")
        return 0
    print("ROLLED BACK 1, skipped 0")
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
    if a.write and not (a.half and a.snapshot):
        sys.exit("REFUSED: --write needs --half <path> and --snapshot <path>")
    sys.exit(run(a.write, a.half, a.snapshot))
