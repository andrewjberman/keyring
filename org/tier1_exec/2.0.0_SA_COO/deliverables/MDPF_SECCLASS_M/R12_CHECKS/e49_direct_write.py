"""e49_direct_write.py -- MDPF_SECCLASS SC-e-49, the DIRECT leg only: conditional puts of the re-planned DIRECT entries.

No model call. Input: the re-plan at contract 0.8.0 (R12_CHECKS/e49_replan/FWD15_AI_PLAN_<firm>_20261007.json). One row per
distinct shared key, the first (largest-amount) entry placing it. Each row goes through etf_classification_scheduled.write()
(`attribute_not_exists(ticker)`), classified_by=scheduled, updated_by=mdpf-secclass-fwd15-direct, name=clean_name(<plan name>).
Bound (CTO condition 2): every row's class/sub-class pair is in the contract's values_by_class, and 0 fixed_income/Cash; a row
outside the bound is refused before any put.

  python e49_direct_write.py                                          # dry run: reads the table, puts nothing
  python e49_direct_write.py --write --half <CTO half.md> --snapshot <snapshot.json>
  python e49_direct_write.py --rollback <snapshot.json> [--write]     # deletes only this act's rows (updated_by guard)
"""
from __future__ import annotations

import argparse
import datetime
import glob
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / "infra/aws/lambda/v2_portal/_shared"))
import etf_classification_scheduled as sched  # noqa: E402
from security_name import clean_name  # noqa: E402

HERE = Path(__file__).resolve().parent
PLAN_GLOB = str(HERE / "e49_replan" / "FWD15_AI_PLAN_*_20261007.json")
CONTRACT = ROOT / "org/standards/MDPF_SECCLASS_CONTRACT.json"
UPDATED_BY = "mdpf-secclass-fwd15-direct"


def load_rows():
    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    closed = {c: set(v) for c, v in contract["fields"]["sub_asset_class"]["values_by_class"].items()}
    entries = []
    for f in sorted(glob.glob(PLAN_GLOB)):
        p = json.loads(Path(f).read_text(encoding="utf-8"))
        entries += [dict(e, firm=p["firm"]) for e in p["entries"] if e["route"] == "DIRECT"]
    entries.sort(key=lambda e: -(e.get("amount") or 0.0))
    rows, seen, out_of_bound = [], set(), []
    for e in entries:
        key = e["shared_key"]
        if key in seen:
            continue
        seen.add(key)
        pair = (e["asset_class"], e["sub_asset_class"])
        if pair[1] not in closed.get(pair[0], set()) or pair == ("fixed_income", "Cash"):
            out_of_bound.append((key, pair))
            continue
        rows.append({"ticker": key, "asset_class": pair[0], "sub_asset_class": pair[1], "classified_by": sched.CLASSIFIED_BY,
                     "updated_by": UPDATED_BY, "name": clean_name(e.get("name") or key), "firm": e["firm"]})
    return contract.get("contract_version"), len(entries), rows, out_of_bound


def half_signed(path):
    text = Path(path).read_text(encoding="utf-8")
    return bool(re.search(r"^## VERDICT: SIGNED\b", text, re.MULTILINE))


def run(write, half, snapshot):
    import boto3
    ddb = boto3.client("dynamodb", region_name=sched.REGION)
    version, n_entries, rows, oob = load_rows()
    present = []
    for r in rows:
        if ddb.get_item(TableName=sched.TABLE_NAME, Key={"ticker": {"S": r["ticker"]}}, ConsistentRead=True).get("Item"):
            present.append(r["ticker"])
    plan = [r for r in rows if r["ticker"] not in set(present)]
    print(f"E49-DIRECT contract={version} entries={n_entries} keys={len(rows)} out_of_bound={len(oob)} present_now={len(present)} "
          f"to_put={len(plan)} write={write}")
    if oob:
        print("REFUSED: rows outside the contract bound", oob)
        return 3
    if not write:
        return 0
    if not (half and half_signed(half)):
        print("REFUSED: the CTO half does not read SIGNED; nothing written")
        return 4
    Path(snapshot).write_text(json.dumps({"taken_at": datetime.datetime.now(datetime.timezone.utc).isoformat(),
                                          "table": sched.TABLE_NAME, "updated_by": UPDATED_BY, "present_before": sorted(present),
                                          "planned": plan}, indent=1, sort_keys=True), encoding="utf-8")
    print("SNAPSHOT written:", snapshot, f"({len(plan)} planned, {len(present)} present before)")
    table = boto3.resource("dynamodb", region_name=sched.REGION).Table(sched.TABLE_NAME)
    res = sched.write([{k: v for k, v in r.items() if k != "firm"} for r in plan], table=table)
    written = sum(1 for _k, s in res if s == "written")
    refused = sum(1 for _k, s in res if s == "refused")
    print(f"WROTE {written} of {len(plan)}; refused (key landed first by another writer) {refused}")
    return 0


def rollback(path, write):
    import boto3
    snap = json.loads(Path(path).read_text(encoding="utf-8"))
    ddb = boto3.client("dynamodb", region_name=sched.REGION)
    deleted = skipped = 0
    for r in snap["planned"]:
        if not write:
            continue
        try:
            ddb.delete_item(TableName=snap["table"], Key={"ticker": {"S": r["ticker"]}},
                            ConditionExpression="attribute_exists(ticker) AND updated_by = :by",
                            ExpressionAttributeValues={":by": {"S": snap["updated_by"]}})
            deleted += 1
        except ddb.exceptions.ConditionalCheckFailedException:
            skipped += 1
    print(f"ROLLBACK planned={len(snap['planned'])} deleted={deleted} skipped_not_ours={skipped} write={write}")
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
        sys.exit("REFUSED: --write needs --snapshot")
    sys.exit(run(a.write, a.half, a.snapshot))
