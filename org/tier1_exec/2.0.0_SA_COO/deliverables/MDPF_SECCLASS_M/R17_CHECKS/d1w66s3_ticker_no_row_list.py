#!/usr/bin/env python3
"""d1w66s3_ticker_no_row_list.py -- MDPF_SECCLASS row D1-W66-S3: the list of BD trace securities whose ticker has NO row today, each
marked as e79's NAME:: fallback resolving it (a live NAME:: row with a class) or listed unresolved. READ-ONLY (DynamoDB get-item).

Domain: every row of BD_UNCLASSIFIED_TRACE_D1S11_20261008.json (all why-groups) carrying a non-blank ticker. Written before the BD fire on
the e79 lib (CRO proposal, UB-20261009T124633Z-37ed act 2), so e79's leg-G read only confirms which of the list the fire resolved.
Prints  D1W66S3-LIST with_ticker=<n> ticker_no_row=<n> name_resolvable=<n> unresolved=<n> usd_resolvable=<..> usd_unresolved=<..>
and writes ../D1W66S3_TICKER_NO_ROW_LIST_20261009.json.
"""
import json
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
TRACE = HERE.parent / "BD_UNCLASSIFIED_TRACE_D1S11_20261008.json"
OUT = HERE.parent / "D1W66S3_TICKER_NO_ROW_LIST_20261009.json"


def main() -> int:
    table = boto3.resource("dynamodb", region_name="us-east-1").Table("etf-classifications")
    rows = [r for r in json.loads(TRACE.read_text(encoding="utf-8"))["rows"] if (r.get("ticker") or "").strip()]
    out = []
    for r in rows:
        tk = r["ticker"].strip().upper()
        if table.get_item(Key={"ticker": tk}, ConsistentRead=True).get("Item"):
            continue
        nrow = table.get_item(Key={"ticker": r["name_key"]}, ConsistentRead=True).get("Item") if r.get("name_key") else None
        cls = (nrow or {}).get("asset_class")
        out.append({"ticker": tk, "name": r.get("name"), "name_key": r.get("name_key"), "why_group": str(r.get("why", ""))[:2],
                    "market_value": r.get("market_value"), "name_row_class": cls,
                    "e79_expected": "resolves via NAME:: row" if cls else "listed unresolved (no NAME:: row)"})
    res = [o for o in out if o["name_row_class"]]
    unr = [o for o in out if not o["name_row_class"]]
    usd = lambda xs: round(sum(float(x["market_value"] or 0) for x in xs), 2)  # noqa: E731
    rec = {"claim": "measured: read-only list, live table read 2026-10-09; trace partition 2026-10-06", "source": TRACE.name,
           "with_ticker": len(rows), "ticker_no_row": len(out), "name_resolvable": len(res), "unresolved": len(unr),
           "usd_resolvable": usd(res), "usd_unresolved": usd(unr),
           "entries": sorted(out, key=lambda o: -float(o["market_value"] or 0))}
    OUT.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    print(f"D1W66S3-LIST with_ticker={len(rows)} ticker_no_row={len(out)} name_resolvable={len(res)} unresolved={len(unr)} "
          f"usd_resolvable={rec['usd_resolvable']} usd_unresolved={rec['usd_unresolved']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
