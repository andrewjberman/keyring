#!/usr/bin/env python3
"""clean_name_write.py -- MDPF_SECCLASS round 8, cell SC-e-34 (FWD-14): the clean-name writer for etf-classifications.

Reads CLEAN_NAME_ROW_SET_20261007.tsv (clean_name_row_set.py). Only action WRITE rows are ever touched; SEED-SOURCE rows are
listed for the seed source's owner (a seed row always wins; the correction is made in the seed source) and UNCHANGED rows need nothing.

DRY RUN by default: a consistent get-item per WRITE key, no write of any kind. The client is wrapped with a counter of every
mutating call and the run asserts puts=0. Prints
  CLEAN-NAME-DRY-RUN write=<n> seed_source=<n> unchanged=<n> refused_stale=<n> puts=0
`--write` requires `--half <path>` (refuses unless the `## COO half` and `## CTO half` headings both read SIGNED) and
`--snapshot <path>` (the pre-state of every WRITE key, consistent reads, written before the first update). Each WRITE is ONE
conditional UpdateItem: SET #n = :clean, updated_by = :by with CONDITION #n = :cur (#n is the attribute `name`) -- a row that
moved since the set was built is refused (reported, never overwritten); the rest continue.
`--rollback <snapshot> [--write]`: per key, a conditional update back to the snapshot name (and the snapshot's updated_by, or
REMOVE it if the row had none), only where the row still reads updated_by = this run's value and name = the clean name.

  python .../clean_name_write.py                                    # dry run
  python .../clean_name_write.py --write --half <half.md> --snapshot <snapshot.json>
  python .../clean_name_write.py --rollback <snapshot.json> [--write]
"""
from __future__ import annotations

import argparse
import csv
import datetime
import json
import re
import sys
from pathlib import Path

TABLE = "etf-classifications"
HERE = Path(__file__).resolve().parent
SET_FILE = HERE.parent / "CLEAN_NAME_ROW_SET_20261007.tsv"
COLS = ["key", "classified_by", "current_name", "clean_name", "action"]
UPDATED_BY = "mdpf-secclass-clean-names"
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


def read_set():
    with SET_FILE.open(encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE)
        assert rd.fieldnames == COLS, f"set header {rd.fieldnames!r}"
        return list(rd)


def s(item, k):
    return (item.get(k) or {}).get("S")


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
    rows = read_set()
    seed_source = [r for r in rows if r["action"] == "SEED-SOURCE"]
    unchanged = [r for r in rows if r["action"] == "UNCHANGED"]
    todo = [r for r in rows if r["action"] == "WRITE"]
    assert len(seed_source) + len(unchanged) + len(todo) == len(rows), "unknown action in the set"
    plan, stale = [], []
    for r in todo:
        item = ddb.get_item(TableName=TABLE, Key={"ticker": {"S": r["key"]}}, ConsistentRead=True).get("Item", {})
        if s(item, "name") == r["current_name"]:
            plan.append((r, item))
        else:
            stale.append(r["key"])
            print(f'REFUSED_STALE {r["key"]} set={r["current_name"]!r} live={s(item, "name")!r}')
    if not write:
        assert ddb.puts == 0, f"dry run made {ddb.puts} mutating calls"
        print(f"CLEAN-NAME-DRY-RUN write={len(plan)} seed_source={len(seed_source)} unchanged={len(unchanged)} "
              f"refused_stale={len(stale)} puts={ddb.puts}")
        return 0 if not stale else 1
    ok, why = half_signed(half) if half else (False, "no --half named")
    print("PRECONDITION half:", "MET" if ok else "NOT MET", "-", why)
    if not ok:
        print("REFUSED: nothing written")
        return 4
    Path(snapshot).write_text(json.dumps({"taken_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "table": TABLE,
                                          "updated_by": UPDATED_BY, "rows": {r["key"]: item for r, item in plan},
                                          "clean": {r["key"]: r["clean_name"] for r, _i in plan}}, indent=1, sort_keys=True), encoding="utf-8")
    print("SNAPSHOT written:", snapshot, f"({len(plan)} rows)")
    written = failed = 0
    for r, _item in plan:
        try:
            ddb.update_item(TableName=TABLE, Key={"ticker": {"S": r["key"]}},
                            UpdateExpression="SET #n = :clean, updated_by = :by", ConditionExpression="#n = :cur",
                            ExpressionAttributeNames={"#n": "name"},
                            ExpressionAttributeValues={":clean": {"S": r["clean_name"]}, ":by": {"S": UPDATED_BY}, ":cur": {"S": r["current_name"]}})
            written += 1
        except ddb.exceptions.ConditionalCheckFailedException:
            failed += 1
            print(f'   CONDITION FAILED at write: {r["key"]} moved between the read and the write')
    print(f"WROTE {written} of {len(plan)}; condition failures {failed}; stale refused at read {len(stale)}")
    return 0 if failed == 0 and not stale else 1


def rollback(path, write):
    import boto3
    ddb = CountingClient(boto3.client("dynamodb", region_name="us-east-1"), allow_mutation=write)
    snap = json.loads(Path(path).read_text(encoding="utf-8"))
    by = snap.get("updated_by", UPDATED_BY)
    done = skipped = 0
    for key, old in sorted(snap["rows"].items()):
        cur = ddb.get_item(TableName=TABLE, Key={"ticker": {"S": key}}, ConsistentRead=True).get("Item", {})
        if s(cur, "updated_by") != by or s(cur, "name") != snap["clean"][key]:
            skipped += 1
            print(f"SKIP {key} (not at this run's value)")
            continue
        print("RESTORE", key)
        if not write:
            continue
        vals = {":old": {"S": s(old, "name")}, ":by": {"S": by}, ":clean": {"S": snap["clean"][key]}}
        if s(old, "updated_by") is not None:
            expr = "SET #n = :old, updated_by = :oby"
            vals[":oby"] = {"S": s(old, "updated_by")}
        else:
            expr = "SET #n = :old REMOVE updated_by"
        try:
            ddb.update_item(TableName=TABLE, Key={"ticker": {"S": key}}, UpdateExpression=expr,
                            ConditionExpression="#n = :clean AND updated_by = :by", ExpressionAttributeNames={"#n": "name"},
                            ExpressionAttributeValues=vals)
            done += 1
        except ddb.exceptions.ConditionalCheckFailedException:
            skipped += 1
            print(f"   CONDITION FAILED at rollback: {key} moved")
    print(f"ROLLED BACK {done}, skipped {skipped}" if write else f"DRY RUN (rollback) skipped={skipped}")
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
