"""e49 DIRECT leg L2 verify: every planned key reads its plan row live (ConsistentRead), inside the contract bound.

  python e49_direct_verify.py <E49_DIRECT_SNAPSHOT.json>
"""
import json
import sys
from pathlib import Path

import boto3

ROOT = Path(__file__).resolve().parents[6]
snap = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
contract = json.loads((ROOT / "org/standards/MDPF_SECCLASS_CONTRACT.json").read_text(encoding="utf-8"))
closed = {c: set(v) for c, v in contract["fields"]["sub_asset_class"]["values_by_class"].items()}
c = boto3.client("dynamodb", region_name="us-east-1")
ok = miss = oob = 0
for r in snap["planned"]:
    it = c.get_item(TableName=snap["table"], Key={"ticker": {"S": r["ticker"]}}, ConsistentRead=True).get("Item", {})
    got = {k: (it.get(k) or {}).get("S") for k in ("asset_class", "sub_asset_class", "classified_by", "updated_by", "name")}
    if got["sub_asset_class"] not in closed.get(got["asset_class"], set()):
        oob += 1
    if all(got[k] == r[k] for k in got):
        ok += 1
    else:
        miss += 1
        print("MISS", r["ticker"], got)
print(f"E49-DIRECT-VERIFY rows={len(snap['planned'])} match={ok} miss={miss} outside_contract={oob}")
