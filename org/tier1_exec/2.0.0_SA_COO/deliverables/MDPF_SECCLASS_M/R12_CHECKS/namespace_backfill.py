#!/usr/bin/env python3
"""namespace_backfill.py -- MDPF_SECCLASS round 12, cell SC-e-69 (W26-S5): the identifier_namespace backfill for etf-classifications.

The writer change (classify-residual-model.py landing_row) stamps the namespace on new AI-runner rows. This is the conditional
backfill of the rows that already exist without one: a `CUSIP:`-keyed row gets CUSIP and a `NAME::`-keyed row gets NAME (contract
fields.identifier_namespace.definitions). A bare-key row is NOT touched: an absent value already reads TICKER (CTO RULING 103140),
so there is nothing to stamp. A `BBG:` row is not planned here (the task order names CUSIP: and NAME:: only).

DRY RUN by default: one paginated, ConsistentRead scan (projection ticker, identifier_namespace), a plan, no write of any kind.
The client is wrapped with a counter of every mutating call and the run asserts puts=0. Prints
  NAMESPACE-BACKFILL-DRY-RUN rows=<n> missing_cusip=<n> missing_name=<n> puts=0
`--write` requires `--half <path>` (refuses unless the `## COO half` and `## CTO half` headings both read SIGNED) and
`--snapshot <path>` (the pre-state of every planned key, consistent reads, written before the first update). Each planned key is
ONE conditional UpdateItem: SET identifier_namespace = :ns with CONDITION attribute_exists(ticker) AND
attribute_not_exists(identifier_namespace) -- a row that gained a namespace since the scan is refused (reported, never
overwritten), a deleted row is never re-created; the rest continue. No other attribute (not updated_by, not last_updated) is touched.
`--rollback <snapshot> [--write]`: per snapshot key, REMOVE identifier_namespace only where the row still reads the value this run set.

  python .../namespace_backfill.py                                    # dry run
  python .../namespace_backfill.py --write --half <half.md> --snapshot <snapshot.json>
  python .../namespace_backfill.py --rollback <snapshot.json> [--write]
"""
from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
from pathlib import Path

TABLE = "etf-classifications"
REGION = "us-east-1"
PREFIX_NS = (("CUSIP:", "CUSIP"), ("NAME::", "NAME"))
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


def namespace_for(key):
    for prefix, ns in PREFIX_NS:
        if key.startswith(prefix):
            return ns
    return None


def scan_all(ddb):
    """Every row, paginated, ConsistentRead. Returns (rows, pages)."""
    rows, pages, kw = [], 0, {}
    while True:
        page = ddb.scan(TableName=TABLE, ConsistentRead=True, ProjectionExpression="ticker, identifier_namespace",
                        **kw)
        pages += 1
        rows.extend(page.get("Items", []))
        if "LastEvaluatedKey" not in page:
            return rows, pages
        kw = {"ExclusiveStartKey": page["LastEvaluatedKey"]}


def plan_of(rows):
    """[(key, namespace)] for each CUSIP:/NAME:: keyed row that lacks identifier_namespace (attribute absent)."""
    out = []
    for it in rows:
        key = s(it, "ticker")
        ns = namespace_for(key or "")
        if ns and "identifier_namespace" not in it:
            out.append((key, ns))
    return sorted(out)


def half_signed(path):
    text = Path(path).read_text(encoding="utf-8")
    for who in ("COO", "CTO"):
        m = re.search(r"^## " + who + r" half\b[^\n]*$", text, re.MULTILINE)
        if not m or not re.search(r"\bSIGNED\b", m.group(0).upper()) or re.search(r"NOT SIGNED|PENDING|UNSIGNED|WITHDRAWN", m.group(0).upper()):
            return False, f"{who} half is not SIGNED: " + (m.group(0) if m else "no heading")
    return True, "both halves read SIGNED"


def run(write, half, snapshot):
    import boto3
    ddb = CountingClient(boto3.client("dynamodb", region_name=REGION), allow_mutation=write)
    rows, pages = scan_all(ddb)
    plan = plan_of(rows)
    n_cusip = sum(1 for _k, ns in plan if ns == "CUSIP")
    n_name = sum(1 for _k, ns in plan if ns == "NAME")
    if not write:
        assert ddb.puts == 0, f"dry run made {ddb.puts} mutating calls"
        print(f"NAMESPACE-BACKFILL-DRY-RUN rows={len(rows)} missing_cusip={n_cusip} missing_name={n_name} puts={ddb.puts}")
        print(f"(scan pages={pages}, ConsistentRead; planned={len(plan)}; bare-key rows untouched: an absent value reads TICKER)")
        return 0
    ok, why = half_signed(half) if half else (False, "no --half named")
    print("PRECONDITION half:", "MET" if ok else "NOT MET", "-", why)
    if not ok:
        print("REFUSED: nothing written")
        return 4
    pre = {}
    for key, _ns in plan:
        pre[key] = ddb.get_item(TableName=TABLE, Key={"ticker": {"S": key}}, ConsistentRead=True).get("Item", {})
    Path(snapshot).write_text(json.dumps({"taken_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "table": TABLE,
                                          "rows": pre, "set": dict(plan)}, indent=1, sort_keys=True), encoding="utf-8")
    print("SNAPSHOT written:", snapshot, f"({len(plan)} rows)")
    written = failed = 0
    for key, ns in plan:
        try:
            ddb.update_item(TableName=TABLE, Key={"ticker": {"S": key}}, UpdateExpression="SET identifier_namespace = :ns",
                            ConditionExpression="attribute_exists(ticker) AND attribute_not_exists(identifier_namespace)",
                            ExpressionAttributeValues={":ns": {"S": ns}})
            written += 1
        except ddb.exceptions.ConditionalCheckFailedException:
            failed += 1
            print(f"   CONDITION FAILED at write: {key} moved between the read and the write")
    print(f"WROTE {written} of {len(plan)}; condition failures {failed}")
    return 0 if failed == 0 else 1


def rollback(path, write):
    import boto3
    ddb = CountingClient(boto3.client("dynamodb", region_name=REGION), allow_mutation=write)
    snap = json.loads(Path(path).read_text(encoding="utf-8"))
    done = skipped = 0
    for key, ns in sorted(snap["set"].items()):
        cur = ddb.get_item(TableName=TABLE, Key={"ticker": {"S": key}}, ConsistentRead=True).get("Item", {})
        if s(cur, "identifier_namespace") != ns:
            skipped += 1
            print(f"SKIP {key} (not at this run's value)")
            continue
        print("RESTORE (REMOVE identifier_namespace)", key)
        if not write:
            continue
        try:
            ddb.update_item(TableName=TABLE, Key={"ticker": {"S": key}}, UpdateExpression="REMOVE identifier_namespace",
                            ConditionExpression="identifier_namespace = :ns", ExpressionAttributeValues={":ns": {"S": ns}})
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
