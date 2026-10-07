"""e48 L2 verify: every row the clean-name write v2 wrote reads its clean name live (ConsistentRead).

  python e48_l2_live_verify.py <CLEAN_NAME_WRITE_V2_SNAPSHOT.json>
"""
import json
import sys

import boto3

snap = json.load(open(sys.argv[1], encoding="utf-8"))
c = boto3.client("dynamodb", region_name="us-east-1")
ok = bad = 0
for k, clean in snap["clean"].items():
    it = c.get_item(TableName=snap["table"], Key={"ticker": {"S": k}}, ConsistentRead=True).get("Item", {})
    if (it.get("name") or {}).get("S") == clean and (it.get("updated_by") or {}).get("S") == snap["updated_by"]:
        ok += 1
    else:
        bad += 1
        print("MISS", k, repr((it.get("name") or {}).get("S")), repr(clean))
print(f"E48-L2-VERIFY rows={len(snap['clean'])} match={ok} miss={bad}")
