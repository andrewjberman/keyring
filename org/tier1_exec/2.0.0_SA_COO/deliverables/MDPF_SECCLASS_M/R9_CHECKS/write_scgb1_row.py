#!/usr/bin/env python3
"""write_scgb1_row.py -- the ONE `SCGB1` ticker row of etf-classifications (MDPF_SECCLASS row S27; CTO batch 266 (a)).

The row mirrors the existing `CUSIP:808516306` row (multi_asset / Fixed Mix, name BALANCED FUND): a Schwab node carrying
display.symbol SCGB1 never reaches the CUSIP row, because the producer reads display.symbol only.

Dry run by default; `--write` puts the row through etf_classification_scheduled.write() (attribute_not_exists(ticker)),
so an existing row is left exactly as it is. It reads the mirrored CUSIP row live and refuses to write if its class
differs from the batch's `multi_asset` / `Fixed Mix`.
"""
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"))
import boto3  # noqa: E402
import etf_classification_scheduled as scheduled  # noqa: E402

KEY, SOURCE = "SCGB1", "CUSIP:808516306"
table = boto3.resource("dynamodb", region_name="us-east-1").Table("etf-classifications")
src = table.get_item(Key={"ticker": SOURCE}, ConsistentRead=True).get("Item")
have = table.get_item(Key={"ticker": KEY}, ConsistentRead=True).get("Item")
print("SCGB1-ROW source=%s found=%s target_present=%s" % (SOURCE, bool(src), bool(have)))
if not src or (src.get("asset_class"), src.get("sub_asset_class")) != ("multi_asset", "Fixed Mix"):
    print("REFUSED: the mirrored row is absent or is not multi_asset / Fixed Mix: %r" % src)
    sys.exit(3)
row = {"ticker": KEY, "asset_class": src["asset_class"], "sub_asset_class": src["sub_asset_class"],
       "name": src["name"], "classified_by": "scheduled", "updated_by": "mdpf-secclass-cusip-rows"}
print("PLAN     %s %s / %s %s" % (KEY, row["asset_class"], row["sub_asset_class"], row["name"]))
if have:
    print("PRESENT  %s already has a row; left as it is" % KEY)
    sys.exit(0)
if "--write" not in sys.argv:
    print("DRY RUN: nothing written. Re-run with --write to land the plan.")
    sys.exit(0)
print("RESULT", scheduled.write([row]))
back = table.get_item(Key={"ticker": KEY}, ConsistentRead=True).get("Item")
print("READBACK", back)
