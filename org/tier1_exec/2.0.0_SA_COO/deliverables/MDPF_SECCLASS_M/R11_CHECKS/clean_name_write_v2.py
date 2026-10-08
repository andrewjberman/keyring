#!/usr/bin/env python3
"""clean_name_write_v2.py -- MDPF_SECCLASS round 9, cell SC-e-48 (FWD-14): the clean-name writer v2 for etf-classifications.

Reads CLEAN_NAME_ROW_SET_V2_20261007.tsv (clean_name_row_set_v2.py). Only action WRITE lines are ever touched; SEED-SOURCE lines are
listed for the seed source's owner (a seed row is corrected in the seed source, never in the table; C-WRITER) and UNCHANGED lines
need nothing. A WRITE line is one of two kinds, by its `source`:
  table      the row has a live name: conditional update SET #n = :clean, updated_by = :by  WITH CONDITION #n = :cur
  custody:*  a held row with no name: conditional update SET #n = :clean, updated_by = :by  WITH CONDITION attribute_not_exists(#n)
(#n is the attribute `name`). A row that moved since the set was built is refused (reported, never overwritten); the rest continue.

DRY RUN by default: a consistent get-item per WRITE key, no write of any kind. The client is wrapped with a counter of every
mutating call and the run asserts puts=0. Prints
  CLEAN-NAME-V2-DRY-RUN write=<n> custody=<n> seed_source=<n> unchanged=<n> refused_stale=<n> puts=0
`--write` requires `--half <path>` (refuses unless the `## COO half` and `## CTO half` headings both read SIGNED) and
`--snapshot <path>` (the pre-state of every WRITE key, consistent reads, written before the first update).
`--rollback <snapshot> [--write]`: per key, a conditional update back to the snapshot (a table row: its old name and updated_by, or
REMOVE updated_by if it had none; a custody row: REMOVE name, and updated_by restored or removed), only where the row still reads
updated_by = this run's value and name = the clean name.

  python .../clean_name_write_v2.py                                    # dry run
  python .../clean_name_write_v2.py --set <rows.tsv>                   # dry run over another set (same columns); default is the V2 set
  python .../clean_name_write_v2.py --write --half <half.md> --snapshot <snapshot.json>
  python .../clean_name_write_v2.py --rollback <snapshot.json> [--write]
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
SET_FILE = HERE.parent / "CLEAN_NAME_ROW_SET_V2_20261007.tsv"
COLS = ["key", "classified_by", "current_name", "source_name", "clean_name", "action", "source"]
UPDATED_BY = "mdpf-secclass-clean-names-v2"
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


def is_custody(r):
    return r["source"].startswith("custody:")


def still_as_built(r, item):
    """A table row must still read its current name; a custody row must still have no `name` attribute."""
    return ("name" not in item) if is_custody(r) else (s(item, "name") == r["current_name"])


def run(write, half, snapshot, set_file=None):
    import boto3
    ddb = CountingClient(boto3.client("dynamodb", region_name="us-east-1"), allow_mutation=write)
    rows = read_set(set_file)
    seed_source = [r for r in rows if r["action"] == "SEED-SOURCE"]
    unchanged = [r for r in rows if r["action"] == "UNCHANGED"]
    todo = [r for r in rows if r["action"] == "WRITE"]
    assert len(seed_source) + len(unchanged) + len(todo) == len(rows), "unknown action in the set"
    assert len({r["key"] for r in rows}) == len(rows), "a key appears twice in the set"
    plan, stale = [], []
    for r in todo:
        item = ddb.get_item(TableName=TABLE, Key={"ticker": {"S": r["key"]}}, ConsistentRead=True).get("Item", {})
        if item and still_as_built(r, item) and s(item, "classified_by") != "model" and s(item, "classified_by") != "seed":
            plan.append((r, item))
        else:
            stale.append(r["key"])
            print(f'REFUSED_STALE {r["key"]} source={r["source"]} set={r["current_name"]!r} live={s(item, "name")!r} '
                  f'by={s(item, "classified_by")!r}')
    n_custody = sum(1 for r, _i in plan if is_custody(r))
    if not write:
        assert ddb.puts == 0, f"dry run made {ddb.puts} mutating calls"
        print(f"CLEAN-NAME-V2-DRY-RUN write={len(plan) - n_custody} custody={n_custody} seed_source={len(seed_source)} "
              f"unchanged={len(unchanged)} refused_stale={len(stale)} puts={ddb.puts}")
        return 0 if not stale else 1
    ok, why = half_signed(half) if half else (False, "no --half named")
    print("PRECONDITION half:", "MET" if ok else "NOT MET", "-", why)
    if not ok:
        print("REFUSED: nothing written")
        return 4
    Path(snapshot).write_text(json.dumps({"taken_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "table": TABLE,
                                          "updated_by": UPDATED_BY, "rows": {r["key"]: item for r, item in plan},
                                          "clean": {r["key"]: r["clean_name"] for r, _i in plan},
                                          "custody": sorted(r["key"] for r, _i in plan if is_custody(r))},
                                         indent=1, sort_keys=True), encoding="utf-8")
    print("SNAPSHOT written:", snapshot, f"({len(plan)} rows)")
    written = failed = 0
    for r, _item in plan:
        vals = {":clean": {"S": r["clean_name"]}, ":by": {"S": UPDATED_BY}}
        if is_custody(r):
            cond = "attribute_not_exists(#n)"
        else:
            cond = "#n = :cur"
            vals[":cur"] = {"S": r["current_name"]}
        try:
            ddb.update_item(TableName=TABLE, Key={"ticker": {"S": r["key"]}},
                            UpdateExpression="SET #n = :clean, updated_by = :by", ConditionExpression=cond,
                            ExpressionAttributeNames={"#n": "name"}, ExpressionAttributeValues=vals)
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
    custody = set(snap.get("custody", []))
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
        vals = {":by": {"S": by}, ":clean": {"S": snap["clean"][key]}}
        sets, removes = [], []
        if key in custody:
            removes.append("#n")
        else:
            sets.append("#n = :old")
            vals[":old"] = {"S": s(old, "name")}
        if s(old, "updated_by") is not None:
            sets.append("updated_by = :oby")
            vals[":oby"] = {"S": s(old, "updated_by")}
        else:
            removes.append("updated_by")
        expr = ("SET " + ", ".join(sets) if sets else "") + (" REMOVE " + ", ".join(removes) if removes else "")
        try:
            ddb.update_item(TableName=TABLE, Key={"ticker": {"S": key}}, UpdateExpression=expr.strip(),
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
    ap.add_argument("--set", dest="set_file", help="row-set TSV with the V2 columns; default CLEAN_NAME_ROW_SET_V2_20261007.tsv")
    a = ap.parse_args()
    if a.rollback:
        sys.exit(rollback(a.rollback, a.write))
    if a.write and not (a.half and a.snapshot):
        sys.exit("REFUSED: --write needs --half <path> and --snapshot <path>")
    sys.exit(run(a.write, a.half, a.snapshot, a.set_file))
