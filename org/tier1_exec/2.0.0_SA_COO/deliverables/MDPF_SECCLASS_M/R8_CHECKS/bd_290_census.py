"""bd_290_census.py -- MDPF_SECCLASS BD forward fix 2 (CTO rulings batch 117 item 4 (ii)): the tickers Black Diamond holds that
etf-classifications has no row for, and what bd-securities says each one is. Read-only.

Input: BD_NOTFOUND_TICKERS_20261002_0400Z.tsv -- every distinct ticker with a 'Classification not found' line in the 2026-10-02
04:00Z Black Diamond gold fire's log (290; the line count beside each). Dollars: gold/holdings_lots/<latest>.parquet, open lots.
For each ticker: does the live table have it now (a row may have landed since 04:00Z); the bd-securities row (asset_class,
sub_asset_class, name, classified_by, confidence); whether the scheduled path's own direct-match rule
(etf_classification_scheduled._direct_match against the live table's vocabulary) accepts that pair as is.

Output: R8_BD_290_CENSUS_<stamp>.json beside this file, plus a summary on stdout.
"""
from __future__ import annotations

import io
import json
import sys
from collections import defaultdict
from datetime import datetime, timezone
from pathlib import Path

import boto3
import pandas as pd

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
sys.path.insert(0, str(ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"))
import etf_classification_scheduled as sched  # noqa: E402
from etf_classifications_dynamodb import ETFClassifier  # noqa: E402

BD_BUCKET = "opal-data-bd"
BD_SECURITIES_TABLE = "bd-securities"  # the retiring fork's own name, as E_18.detect_new_securities.py:44 holds it


def latest_lots_key(s3) -> str:
    keys = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=BD_BUCKET, Prefix="gold/holdings_lots/"):
        keys += [o["Key"] for o in page.get("Contents", []) if o["Key"].endswith(".parquet")]
    return sorted(keys)[-1]


def main() -> int:
    tickers = []
    for line in (HERE / "BD_NOTFOUND_TICKERS_20261002_0400Z.tsv").read_text(encoding="utf-8").splitlines():
        t, n = line.split("\t")
        tickers.append((t.strip().upper(), int(n)))
    s3 = boto3.client("s3", region_name="us-east-1")
    lots_key = latest_lots_key(s3)
    lots = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=BD_BUCKET, Key=lots_key)["Body"].read()),
                           columns=["ticker", "asset_name", "market_value", "is_open", "account_id"])
    lots = lots[lots["is_open"].astype(bool)]
    lots["T"] = lots["ticker"].astype(str).str.strip().str.upper()
    mv = lots.groupby("T")["market_value"].sum()
    accts = lots.groupby("T")["account_id"].nunique()
    names = lots.groupby("T")["asset_name"].first()

    classifier = ETFClassifier()
    vocab = sched.TableVocabulary.from_live_table(classifier)
    existing = sched.existing_tickers(classifier)
    bd = boto3.resource("dynamodb", region_name="us-east-1").Table(BD_SECURITIES_TABLE)

    rows = []
    for t, misses in tickers:
        item = bd.get_item(Key={"ticker": t}).get("Item") or {}
        ac, sac = item.get("asset_class"), item.get("sub_asset_class")
        direct = bool(item) and sched._direct_match(ac, sac, vocab)
        rows.append({
            "ticker": t, "miss_lines": misses, "open_mv": round(float(mv.get(t, 0.0)), 2),
            "accounts": int(accts.get(t, 0)), "holding_name": str(names.get(t, "")),
            "in_table_now": t in existing,
            "bd_row": bool(item), "bd_asset_class": ac, "bd_sub_asset_class": sac,
            "bd_name": item.get("name") or item.get("security_name"), "bd_classified_by": item.get("classified_by"),
            "bd_confidence": float(item["confidence"]) if item.get("confidence") is not None else None,
            "direct_match": direct,
        })

    def agg(sel):
        return {"tickers": len(sel), "open_mv": round(sum(r["open_mv"] for r in sel), 2)}
    pairs = defaultdict(list)
    for r in rows:
        if r["bd_row"] and not r["direct_match"] and not r["in_table_now"]:
            pairs[(r["bd_asset_class"], r["bd_sub_asset_class"])].append(r)
    summary = {
        "lots_key": lots_key, "table_rows": len(existing),
        "all": agg(rows),
        "in_table_now": agg([r for r in rows if r["in_table_now"]]),
        "no_bd_row": agg([r for r in rows if not r["bd_row"] and not r["in_table_now"]]),
        "direct_match": agg([r for r in rows if r["direct_match"] and not r["in_table_now"]]),
        "bd_row_needs_mapping": agg([r for r in rows if r["bd_row"] and not r["direct_match"] and not r["in_table_now"]]),
        "unmatched_pairs": sorted(({"bd_asset_class": k[0], "bd_sub_asset_class": k[1], **agg(v),
                                    "examples": [x["ticker"] for x in sorted(v, key=lambda x: -x["open_mv"])[:5]]}
                                   for k, v in pairs.items()), key=lambda d: -d["open_mv"]),
        "vocabulary": {k: sorted(v) for k, v in vocab.sub_asset_classes.items()},
    }
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    out = HERE / ("R8_BD_290_CENSUS_%s.json" % stamp)
    out.write_text(json.dumps({"summary": summary, "rows": rows}, indent=1, default=str), encoding="utf-8")
    print(json.dumps({k: v for k, v in summary.items() if k not in ("unmatched_pairs", "vocabulary")}, indent=1))
    for p in summary["unmatched_pairs"][:25]:
        print("UNMATCHED %-14s %-28s tickers=%3d mv=%14.2f e.g. %s" % (p["bd_asset_class"], p["bd_sub_asset_class"],
                                                                       p["tickers"], p["open_mv"], ",".join(p["examples"])))
    print("written", out.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
