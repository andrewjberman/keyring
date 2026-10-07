#!/usr/bin/env python3
"""sc_e56_newly_placed_check.py -- MDPF_SECCLASS round 9, cell SC-e-56 (S27, folded R8 SC-e-39): the securities the Holdings
producer newly places by its CUSIP fallback, listed before the change ships, are true against the table.

READ-ONLY. Reads the newest org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/HOLDINGS_CUSIP_NEWLY_PLACED_<yyyymmdd>.json:
  {"source": "<how the held set was read>", "as_of": "<date>",
   "firms": {"49financial": [{"symbol": .., "cusip": .., "market_value": ..}, ..], "cottonwood": [..], "inflection": [..]}}
and checks against etf-classifications (consistent reads only):
  - all three firms are present (an empty list is allowed for a firm, an absent key is not);
  - every entry: its symbol is ABSENT from the table (or empty), and `CUSIP:<cusip>` is PRESENT -- a newly placed security is
    exactly a symbol miss that the CUSIP key answers;
  - at least one entry overall (round 8 held 187; a zero list is not evidence);
  - POSITIVE CONTROL: AAETX reads present, so an absent read is not a broken client.
Prints SC-E56-NEWLY ok=<bool> firms=<n of 3> listed=<n> false_entries=<n> control=<present|ABSENT>. Run from the repo root.
"""
import glob
import json
import os
import sys

import boto3

HOME = os.path.join("org", "tier1_exec", "2.0.0_SA_COO", "deliverables", "MDPF_SECCLASS_M")
FIRMS = ("49financial", "cottonwood", "inflection")
TABLE = "etf-classifications"


def present(ddb, key):
    if not key:
        return False
    return "Item" in ddb.get_item(TableName=TABLE, Key={"ticker": {"S": key}}, ConsistentRead=True,
                                  ProjectionExpression="ticker")


def main():
    hits = sorted(glob.glob(os.path.join(HOME, "HOLDINGS_CUSIP_NEWLY_PLACED_*.json")))
    if not hits:
        print("SC-E56-NEWLY ok=False firms=0 of 3 listed=0 false_entries=0 control=unread reason=no HOLDINGS_CUSIP_NEWLY_PLACED_*.json")
        return 1
    with open(hits[-1], encoding="utf-8") as fh:
        doc = json.load(fh)
    ddb = boto3.client("dynamodb", region_name="us-east-1")
    control = "present" if present(ddb, "AAETX") else "ABSENT"
    firms = doc.get("firms", {})
    nfirms = sum(1 for f in FIRMS if f in firms)
    listed, false = 0, 0
    for f in FIRMS:
        for e in firms.get(f, []):
            listed += 1
            sym = str(e.get("symbol") or "").strip().upper()
            cusip = str(e.get("cusip") or "").strip().upper()
            if present(ddb, sym) or not cusip or not present(ddb, "CUSIP:" + cusip):
                false += 1
    ok = nfirms == 3 and listed >= 1 and false == 0 and control == "present"
    print(f"SC-E56-NEWLY ok={ok} firms={nfirms} of 3 listed={listed} false_entries={false} control={control} "
          f"file={os.path.basename(hits[-1])}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
