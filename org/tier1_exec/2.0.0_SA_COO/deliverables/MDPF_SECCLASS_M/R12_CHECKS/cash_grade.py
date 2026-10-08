"""cash_grade.py -- MDPF_SECCLASS round 12 SC-e-72: READ-ONLY cash grade of etf-classifications.

  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/cash_grade.py

Paginated ConsistentRead scan of etf-classifications (no write of any kind). Counts:
- rows with asset_class cash, by sub_asset_class and by classified_by;
- the V3 set's cash-planned keys (route DIRECT, asset_class cash; unique shared_key) present at their planned sub-class;
- legacy rows asset_class fixed_income with sub_asset_class Cash (must be 0).
ok = every V3 cash-planned key is present at its planned (cash, sub_asset_class) AND fixed_income_Cash is 0.
Keys not yet written (e32 legs pending) are absent, so ok is False until they land; v3_absent says how many.
Prints  CASH-GRADE ok=<bool> cash_rows=<n> by_classified_by=<dict> v3_planned=<n> v3_present_at_plan=<n> fixed_income_Cash=<n> ...
"""
import csv
import sys
from collections import Counter
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
SET = HERE.parent / "OLD_LIST_RECLASSIFY_SET_V3_20261007.tsv"


def scan_all(table):
    out, kw, pages = [], {"ConsistentRead": True}, 0
    while True:
        page = table.scan(**kw)
        pages += 1
        out += page.get("Items", [])
        if "LastEvaluatedKey" not in page:
            return out, pages
        kw["ExclusiveStartKey"] = page["LastEvaluatedKey"]


def main():
    with SET.open(encoding="utf-8", newline="") as fh:
        rows = list(csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE))
    planned = {}
    for r in rows:
        if r["route"] == "DIRECT" and r["asset_class"] == "cash" and r["shared_key"] not in planned:
            planned[r["shared_key"]] = r["sub_asset_class"]

    items, pages = scan_all(boto3.resource("dynamodb", region_name="us-east-1").Table("etf-classifications"))
    live = {i["ticker"]: i for i in items}

    cash = [i for i in items if i.get("asset_class") == "cash"]
    by_sub = Counter(i.get("sub_asset_class") for i in cash)
    by_cb = Counter(i.get("classified_by") for i in cash)
    fi_cash = sum(1 for i in items if i.get("asset_class") == "fixed_income" and i.get("sub_asset_class") == "Cash")
    case_variants = sum(1 for i in items if str(i.get("asset_class", "")).lower() == "cash" and i.get("asset_class") != "cash")

    at_plan = absent = wrong = 0
    for k, sub in planned.items():
        it = live.get(k)
        if it is None:
            absent += 1
        elif it.get("asset_class") == "cash" and it.get("sub_asset_class") == sub:
            at_plan += 1
        else:
            wrong += 1

    ok = at_plan == len(planned) and fi_cash == 0
    print(f"CASH-GRADE ok={ok} cash_rows={len(cash)} by_classified_by={dict(by_cb)} v3_planned={len(planned)} "
          f"v3_present_at_plan={at_plan} fixed_income_Cash={fi_cash} by_sub_asset_class={dict(by_sub)} "
          f"v3_absent={absent} v3_present_wrong={wrong} cash_case_variants={case_variants} "
          f"table_rows={len(items)} scan_pages={pages} v3_tsv_rows={len(rows)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
