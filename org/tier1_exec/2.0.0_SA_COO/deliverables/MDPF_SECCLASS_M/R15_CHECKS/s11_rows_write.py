#!/usr/bin/env python3
"""s11_rows_write.py -- MDPF_SECCLASS round 15, cell SC-e-77 (FWD-16, FWD-17): the writer of the D1-S11 row set for etf-classifications.

Reads S11_ROW_SET_20261008.tsv (columns key, name, action, asset_class, sub_asset_class, current_class, rule, evidence).
  NEW    a row to create:  put_item conditioned on attribute_not_exists(ticker); the key is a ticker (group B) or a NAME:: key (group D).
         The item: ticker, asset_class, sub_asset_class (only when the set names one), classified_by `scheduled`, updated_by
         UPDATED_BY, name = clean_name(<set name>), identifier_namespace NAME for a NAME:: key (absent for a ticker, which reads
         TICKER), last_updated.
  REMAP  an existing AI-landed row whose class breaks Andrew's alternatives rule (Andrew-direct 2026-10-08 ~19:0xZ):
         update_item SET asset_class, sub_asset_class (REMOVE when the set names none), updated_by, last_updated, conditioned on
         attribute_exists(ticker) AND asset_class = <current_class>.
Every asset_class must be one of the six; a non-empty sub_asset_class must be in the contract's closed list for its class
(org/standards/MDPF_SECCLASS_CONTRACT.json values_by_class); a line outside either is refused before any call.

DRY RUN by default: one consistent get_item per line, no write of any kind. The client is wrapped with a counter of every mutating
call (a mutating call in a dry run raises), and the run asserts puts=0. Prints
  S11-ROWS-DRY-RUN new=<n> remap=<n> refused_present=<n> refused_stale=<n> puts=0
`--write` requires `--half <path>` (refuses unless the `## COO half` and `## CTO half` headings both read SIGNED) and
`--snapshot <path>` (must not exist yet; the pre-state of every REMAP key and the NEW key list, written before the first call).
`--rollback <snapshot> [--write]`: a NEW key is deleted only while it still reads updated_by = this run's value AND the class this
run put; a REMAP key is restored (class, sub-class, updated_by, last_updated, each as the snapshot holds it) only while it still reads
updated_by = this run's value and the class this run set. Without --write a rollback only lists what it would do.

  python .../s11_rows_write.py                                         # dry run
  python .../s11_rows_write.py --write --half <half.md> --snapshot <snapshot.json>
  python .../s11_rows_write.py --rollback <snapshot.json> [--write]
"""
from __future__ import annotations

import argparse
import csv
import datetime
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / "infra/aws/lambda/v2_portal/_shared"))
from security_name import clean_name  # noqa: E402

REGION = "us-east-1"
TABLE = "etf-classifications"
SET_FILE = HERE.parent / "S11_ROW_SET_20261008.tsv"
CONTRACT = ROOT / "org/standards/MDPF_SECCLASS_CONTRACT.json"
COLS = ["key", "name", "action", "asset_class", "sub_asset_class", "current_class", "rule", "evidence"]
SIX = frozenset({"equity", "fixed_income", "cash", "alternatives", "structured", "commodities"})
UPDATED_BY = "mdpf-secclass-s11-rows"
CLASSIFIED_BY = "scheduled"
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


def read_set(set_file=None):
    with Path(set_file or SET_FILE).open(encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE)
        assert rd.fieldnames == COLS, f"set header {rd.fieldnames!r}"
        rows = list(rd)
    assert len({r["key"] for r in rows}) == len(rows), "a key appears twice in the set"
    assert all(r["action"] in ("NEW", "REMAP") for r in rows), "unknown action in the set"
    return rows


def closed_lists():
    c = json.loads(CONTRACT.read_text(encoding="utf-8"))
    return {k: set(v) for k, v in c["fields"]["sub_asset_class"]["values_by_class"].items() if k in SIX}


def out_of_bound(rows):
    closed, bad = closed_lists(), []
    for r in rows:
        ac, sub = r["asset_class"], r["sub_asset_class"]
        if ac not in SIX or (sub and sub not in closed.get(ac, set())):
            bad.append((r["key"], ac, sub))
        if r["action"] == "REMAP" and not r["current_class"]:
            bad.append((r["key"], "no current_class", ""))
    return bad


def s(item, k):
    return (item.get(k) or {}).get("S")


def half_signed(path):
    text = Path(path).read_text(encoding="utf-8")
    for who in ("COO", "CTO"):
        m = re.search(r"^## " + who + r" half\b[^\n]*$", text, re.MULTILINE)
        if not m or not re.search(r"\bSIGNED\b", m.group(0).upper()) or re.search(r"NOT SIGNED|PENDING|UNSIGNED|WITHDRAWN", m.group(0).upper()):
            return False, f"{who} half is not SIGNED: " + (m.group(0) if m else "no heading")
    return True, "both halves read SIGNED"


def new_item(r, now):
    item = {"ticker": {"S": r["key"]}, "asset_class": {"S": r["asset_class"]}, "classified_by": {"S": CLASSIFIED_BY},
            "updated_by": {"S": UPDATED_BY}, "name": {"S": clean_name(r["name"]) or r["key"]}, "last_updated": {"S": now}}
    if r["sub_asset_class"]:
        item["sub_asset_class"] = {"S": r["sub_asset_class"]}
    if r["key"].startswith("NAME::"):
        item["identifier_namespace"] = {"S": "NAME"}
    return item


def run(write, half, snapshot, set_file=None):
    import boto3
    ddb = CountingClient(boto3.client("dynamodb", region_name=REGION), allow_mutation=write)
    rows = read_set(set_file)
    oob = out_of_bound(rows)
    if oob:
        print("REFUSED: lines outside the six classes / the contract's closed sub-class lists:", oob[:5])
        return 3
    plan_new, plan_remap, present, stale = [], [], [], []
    for r in rows:
        item = ddb.get_item(TableName=TABLE, Key={"ticker": {"S": r["key"]}}, ConsistentRead=True).get("Item", {})
        if r["action"] == "NEW":
            if item:
                present.append(r["key"])
                print(f'REFUSED_PRESENT {r["key"]} live={s(item, "asset_class")}/{s(item, "sub_asset_class")} by={s(item, "updated_by")!r}')
            else:
                plan_new.append(r)
        else:
            if item and s(item, "asset_class") == r["current_class"]:
                plan_remap.append((r, item))
            else:
                stale.append(r["key"])
                print(f'REFUSED_STALE {r["key"]} set_current={r["current_class"]!r} live={s(item, "asset_class")!r}')
    if not write:
        assert ddb.puts == 0, f"dry run made {ddb.puts} mutating calls"
        print(f"S11-ROWS-DRY-RUN new={len(plan_new)} remap={len(plan_remap)} refused_present={len(present)} "
              f"refused_stale={len(stale)} puts={ddb.puts}")
        return 0 if not present and not stale else 1
    ok, why = half_signed(half) if half else (False, "no --half named")
    print("PRECONDITION half:", "MET" if ok else "NOT MET", "-", why)
    if not ok:
        print("REFUSED: nothing written")
        return 4
    if Path(snapshot).exists():
        print("REFUSED: the snapshot path already exists; nothing written")
        return 4
    now = datetime.datetime.now(datetime.timezone.utc).isoformat()
    Path(snapshot).write_text(json.dumps({
        "taken_at": now, "table": TABLE, "updated_by": UPDATED_BY, "classified_by": CLASSIFIED_BY,
        "new": {r["key"]: r["asset_class"] for r in plan_new},
        "remap": {r["key"]: {"set_class": r["asset_class"], "set_sub": r["sub_asset_class"], "before": item} for r, item in plan_remap}},
        indent=1, sort_keys=True), encoding="utf-8")
    print("SNAPSHOT written:", snapshot, f"({len(plan_new)} new, {len(plan_remap)} remap)")
    put = upd = failed = 0
    for r in plan_new:
        try:
            ddb.put_item(TableName=TABLE, Item=new_item(r, now), ConditionExpression="attribute_not_exists(ticker)")
            put += 1
        except ddb.exceptions.ConditionalCheckFailedException:
            failed += 1
            print(f'   CONDITION FAILED at write: {r["key"]} landed between the read and the write (left as it is)')
    for r, _item in plan_remap:
        vals = {":ac": {"S": r["asset_class"]}, ":by": {"S": UPDATED_BY}, ":now": {"S": now}, ":cur": {"S": r["current_class"]}}
        expr = "SET asset_class = :ac, updated_by = :by, last_updated = :now"
        if r["sub_asset_class"]:
            expr += ", sub_asset_class = :sub"
            vals[":sub"] = {"S": r["sub_asset_class"]}
        else:
            expr += " REMOVE sub_asset_class"
        try:
            ddb.update_item(TableName=TABLE, Key={"ticker": {"S": r["key"]}}, UpdateExpression=expr,
                            ConditionExpression="attribute_exists(ticker) AND asset_class = :cur", ExpressionAttributeValues=vals)
            upd += 1
        except ddb.exceptions.ConditionalCheckFailedException:
            failed += 1
            print(f'   CONDITION FAILED at write: {r["key"]} moved between the read and the write (left as it is)')
    print(f"WROTE new={put} of {len(plan_new)}, remap={upd} of {len(plan_remap)}; condition failures {failed}; "
          f"refused at read: present {len(present)}, stale {len(stale)}")
    return 0 if failed == 0 and not present and not stale else 1


def rollback(path, write):
    import boto3
    ddb = CountingClient(boto3.client("dynamodb", region_name=REGION), allow_mutation=write)
    snap = json.loads(Path(path).read_text(encoding="utf-8"))
    by = snap["updated_by"]
    deleted = restored = skipped = 0
    for key, ac in sorted(snap["new"].items()):
        cur = ddb.get_item(TableName=TABLE, Key={"ticker": {"S": key}}, ConsistentRead=True).get("Item", {})
        if s(cur, "updated_by") != by or s(cur, "asset_class") != ac:
            skipped += 1
            print(f"SKIP {key} (not at this run's value)")
            continue
        print("DELETE", key)
        if not write:
            continue
        try:
            ddb.delete_item(TableName=TABLE, Key={"ticker": {"S": key}}, ConditionExpression="updated_by = :by AND asset_class = :ac",
                            ExpressionAttributeValues={":by": {"S": by}, ":ac": {"S": ac}})
            deleted += 1
        except ddb.exceptions.ConditionalCheckFailedException:
            skipped += 1
            print(f"   CONDITION FAILED at rollback: {key} moved")
    for key, rec in sorted(snap["remap"].items()):
        before = rec["before"]
        cur = ddb.get_item(TableName=TABLE, Key={"ticker": {"S": key}}, ConsistentRead=True).get("Item", {})
        if s(cur, "updated_by") != by or s(cur, "asset_class") != rec["set_class"]:
            skipped += 1
            print(f"SKIP {key} (not at this run's value)")
            continue
        print("RESTORE", key)
        if not write:
            continue
        vals = {":by": {"S": by}, ":set": {"S": rec["set_class"]}, ":ac": {"S": s(before, "asset_class")}}
        sets, removes = ["asset_class = :ac"], []
        for attr, ph in (("sub_asset_class", ":sub"), ("updated_by", ":oby"), ("last_updated", ":olu")):
            if s(before, attr) is not None:
                sets.append(f"{attr} = {ph}")
                vals[ph] = {"S": s(before, attr)}
            else:
                removes.append(attr)
        expr = "SET " + ", ".join(sets) + (" REMOVE " + ", ".join(removes) if removes else "")
        try:
            ddb.update_item(TableName=TABLE, Key={"ticker": {"S": key}}, UpdateExpression=expr,
                            ConditionExpression="updated_by = :by AND asset_class = :set", ExpressionAttributeValues=vals)
            restored += 1
        except ddb.exceptions.ConditionalCheckFailedException:
            skipped += 1
            print(f"   CONDITION FAILED at rollback: {key} moved")
    if write:
        print(f"ROLLED BACK deleted={deleted} restored={restored} skipped={skipped}")
    else:
        assert ddb.puts == 0, f"dry rollback made {ddb.puts} mutating calls"
        print(f"S11-ROWS-ROLLBACK-DRY-RUN skipped={skipped} puts={ddb.puts}")
    return 0


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--half")
    ap.add_argument("--snapshot")
    ap.add_argument("--rollback")
    ap.add_argument("--set", dest="set_file", help="row-set TSV with the S11 columns; default S11_ROW_SET_20261008.tsv")
    a = ap.parse_args()
    if a.rollback:
        sys.exit(rollback(a.rollback, a.write))
    if a.write and not (a.half and a.snapshot):
        sys.exit("REFUSED: --write needs --half <path> and --snapshot <path>")
    sys.exit(run(a.write, a.half, a.snapshot, a.set_file))
