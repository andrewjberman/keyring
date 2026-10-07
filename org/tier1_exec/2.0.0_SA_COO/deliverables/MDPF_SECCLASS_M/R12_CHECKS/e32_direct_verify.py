"""e32 V3 DIRECT leg verify: every DIRECT key of the V3 set reads its planned row live, and the snapshot's keys are untouched.

  python e32_direct_verify.py <OLD_LIST_V3_WRITE_SNAPSHOT.json>
Prints  E32-DIRECT-VERIFY keys=<n> match=<n> miss=<n> outside_contract=<n> table_rows=<n> snapshot_rows=<n> multi_asset=<n>
"""
import csv
import json
import sys
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
M = HERE.parent
ROOT = HERE.parents[5]
SET = M / "OLD_LIST_RECLASSIFY_SET_V3_20261007.tsv"
snap = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
before = set(snap["keys"])
contract = json.loads((ROOT / "org/standards/MDPF_SECCLASS_CONTRACT.json").read_text(encoding="utf-8"))
closed = {c: set(v) for c, v in contract["fields"]["sub_asset_class"]["values_by_class"].items()}
with SET.open(encoding="utf-8", newline="") as fh:
    rows = list(csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE))
direct = {}
for r in rows:
    if r["route"] == "DIRECT" and r["shared_key"] not in direct and r["shared_key"] not in before:
        direct[r["shared_key"]] = r


def scan_all(table):
    out, kw = [], {"ConsistentRead": True}
    while True:
        page = table.scan(**kw)
        out += page.get("Items", [])
        if "LastEvaluatedKey" not in page:
            return out
        kw["ExclusiveStartKey"] = page["LastEvaluatedKey"]


items = scan_all(boto3.resource("dynamodb", region_name="us-east-1").Table("etf-classifications"))
live = {i["ticker"]: i for i in items}
ok = miss = oob = 0
for k, r in direct.items():
    it = live.get(k, {})
    want = (r["asset_class"], r["sub_asset_class"] or None, "scheduled", "mdpf-secclass-old-list-reclassify", r["clean_name"] or k)
    got = (it.get("asset_class"), it.get("sub_asset_class"), it.get("classified_by"), it.get("updated_by"), it.get("name"))
    if got == want:
        ok += 1
    else:
        miss += 1
        if miss <= 5:
            print("MISS", k, got, want)
    if it and it.get("sub_asset_class") not in closed.get(it.get("asset_class"), set()):
        oob += 1
ma = sum(1 for i in items if i.get("asset_class") == "multi_asset")
print(f"E32-DIRECT-VERIFY keys={len(direct)} match={ok} miss={miss} outside_contract={oob} table_rows={len(items)} "
      f"snapshot_rows={len(before)} multi_asset={ma} snapshot_keys_present={len(before & set(live))}/{len(before)}")
