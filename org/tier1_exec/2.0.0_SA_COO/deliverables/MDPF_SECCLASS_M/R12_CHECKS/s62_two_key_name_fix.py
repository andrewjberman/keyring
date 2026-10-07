"""Row S62 remedy (a): rewrite the two non-ASCII names the e48 write landed, to clean_name()'s ASCII-only output (R12c).

A literal two-key act. Each update is conditioned on the live name still reading what the e48 snapshot wrote.
  python s62_two_key_name_fix.py                 # dry run: prints each key's live name and target
  python s62_two_key_name_fix.py --write
  python s62_two_key_name_fix.py --rollback      # puts back the e48-written value, conditioned on the target
Prints  S62-FIX write=<bool> keys=2 ok=<n> already=<n> moved=<n>
"""
import json
import sys
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / "infra/aws/lambda/v2_portal/_shared"))
from security_name import clean_name  # noqa: E402

SNAP = HERE.parent / "CLEAN_NAME_WRITE_V2_SNAPSHOT_20261007.json"
KEYS = ("VWUAX", "CUSIP:025083882")
UPDATED_BY = "mdpf-secclass-s62-ascii-names"

snap = json.loads(SNAP.read_text(encoding="utf-8"))
c = boto3.client("dynamodb", region_name="us-east-1")
write, back = "--write" in sys.argv, "--rollback" in sys.argv
ok = already = moved = 0
for k in KEYS:
    written = snap["clean"][k]
    target = clean_name(written)
    assert target.isascii() and target != written, (k, target)
    frm, to = (target, written) if back else (written, target)
    live = (c.get_item(TableName=snap["table"], Key={"ticker": {"S": k}}, ConsistentRead=True).get("Item", {}).get("name") or {}).get("S")
    print(f"{k}: live={live!a} from={frm!a} to={to!a}")
    if live == to:
        already += 1
        continue
    if live != frm:
        moved += 1
        continue
    if write or back:
        c.update_item(TableName=snap["table"], Key={"ticker": {"S": k}}, UpdateExpression="SET #n = :to, updated_by = :by",
                      ConditionExpression="#n = :from", ExpressionAttributeNames={"#n": "name"},
                      ExpressionAttributeValues={":to": {"S": to}, ":from": {"S": frm},
                                                 ":by": {"S": snap["updated_by"] if back else UPDATED_BY}})
    ok += 1
print(f"S62-FIX write={write or back} rollback={back} keys={len(KEYS)} ok={ok} already={already} moved={moved}")
sys.exit(0 if moved == 0 else 1)
