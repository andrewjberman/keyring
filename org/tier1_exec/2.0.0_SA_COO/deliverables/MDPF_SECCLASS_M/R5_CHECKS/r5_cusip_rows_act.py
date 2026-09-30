"""r5_cusip_rows_act.py -- the CUSIP_ROWS act (MDPF_SECCLASS, halves COO 5cc84b40f6 / CTO 1f4792c45a).

Writes the 349 planned CUSIP-keyed rows of R2_CUSIP_CENSUS_20260930.json into etf-classifications through the module's
own conditional writer (etf_classification_scheduled.write: put_item with attribute_not_exists(ticker)), and reads
them back. Nothing else in the table is touched: the write set is the census's literal key list.

  --pre-read   consistent get_item on every planned key; prints PRE-READ present=<n> of <d> and writes the item map
  --write      the conditional puts; prints WRITTEN written=<n> refused=<n> of <d> overwrites=0 and every refused key
  --read-back  consistent get_item on every planned key; prints READ-BACK equal=<n> missing=<n> differ=<n> of <d>
Every mode writes its JSON evidence beside the ledger under R5_CUSIP_ACT/. Exit 1 on any refusal or difference.
"""
from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path

import boto3

ROOT = Path(__file__).resolve().parents[6]  # R5_CHECKS -> MDPF_SECCLASS_M -> deliverables -> 2.0.0_SA_COO -> tier1_exec -> org -> root
sys.path.insert(0, str(ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"))
import etf_classification_scheduled as sched  # noqa: E402

CENSUS = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R2_CUSIP_CENSUS_20260930.json"
OUT_DIR = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R5_CUSIP_ACT"
TABLE = os.environ.get("ETF_CLASSIFICATIONS_TABLE", "etf-classifications")
COMPARE_FIELDS = ("ticker", "identifier_namespace", "asset_class", "sub_asset_class", "classified_by", "updated_by", "name")


def planned_rows():
    rows = json.load(open(CENSUS, encoding="utf-8"))["rows"]
    bad = [r for r in rows if not str(r.get("ticker", "")).startswith("CUSIP:")]
    if bad:
        raise SystemExit(f"REFUSED: {len(bad)} planned row(s) are not CUSIP:-keyed")
    return rows


def stamp():
    return datetime.now(timezone.utc).strftime("%Y%m%dT%H%M%SZ")


def get_all(table, rows):
    found = {}
    for r in rows:
        resp = table.get_item(Key={"ticker": r["ticker"]}, ConsistentRead=True)
        if "Item" in resp:
            found[r["ticker"]] = resp["Item"]
    return found


def main(argv):
    ap = argparse.ArgumentParser()
    ap.add_argument("--pre-read", action="store_true")
    ap.add_argument("--write", action="store_true")
    ap.add_argument("--read-back", action="store_true")
    a = ap.parse_args(argv)
    rows = planned_rows()
    d = len(rows)
    table = boto3.resource("dynamodb", region_name="us-east-1").Table(TABLE)
    OUT_DIR.mkdir(parents=True, exist_ok=True)
    rc = 0
    if a.pre_read:
        found = get_all(table, rows)
        p = OUT_DIR / f"PRE_READ_{stamp()}.json"
        json.dump({"table": TABLE, "planned": d, "present": len(found), "items": found}, open(p, "w", encoding="utf-8"), indent=1, default=str)
        print(f"PRE-READ table={TABLE} present={len(found)} of {d} saved={p.relative_to(ROOT)}")
        if found:
            rc = 1
    if a.write:
        results = sched.write(rows, table=table, table_name=TABLE)
        written = sum(1 for _, s in results if s == "written")
        refused = [t for t, s in results if s == "refused"]
        p = OUT_DIR / f"WRITE_{stamp()}.json"
        json.dump({"table": TABLE, "planned": d, "written": written, "refused": refused, "results": results}, open(p, "w", encoding="utf-8"), indent=1)
        print(f"WRITTEN written={written} refused={len(refused)} of {d} overwrites=0 saved={p.relative_to(ROOT)}")
        for t in refused:
            print(f"  REFUSED {t}")
        if refused or written != d:
            rc = 1
    if a.read_back:
        found = get_all(table, rows)
        equal = missing = differ = 0
        diffs = []
        for r in rows:
            item = found.get(r["ticker"])
            if item is None:
                missing += 1
                diffs.append({"ticker": r["ticker"], "missing": True})
                continue
            delta = {f: (r.get(f), item.get(f)) for f in COMPARE_FIELDS if (r.get(f) or None) != (item.get(f) or None)}
            if delta:
                differ += 1
                diffs.append({"ticker": r["ticker"], "delta": delta})
            else:
                equal += 1
        p = OUT_DIR / f"READ_BACK_{stamp()}.json"
        json.dump({"table": TABLE, "planned": d, "equal": equal, "missing": missing, "differ": differ, "diffs": diffs, "items": found},
                  open(p, "w", encoding="utf-8"), indent=1, default=str)
        print(f"READ-BACK equal={equal} missing={missing} differ={differ} of {d} saved={p.relative_to(ROOT)}")
        if missing or differ:
            rc = 1
    return rc


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
