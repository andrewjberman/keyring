"""cot_name_share.py -- MDPF_SECCLASS round 16 cell SC-e-82 (row D1-W66-S2). READ-ONLY measure of how much of Cottonwood's
unclassified a canonical NAME:: row in etf-classifications would place. Reads S3 (opal-data-cot) and DynamoDB (batch_get_item) only."""
import importlib.util
import io
import json
import sys
from pathlib import Path

import boto3
import pandas as pd

ROOT = Path(__file__).resolve().parents[6]
OUT = Path(__file__).resolve().parent.parent / "COT_NAME_SHARE_20261009.json"
BUCKET, PREFIX, TABLE = "opal-data-cot", "gold/canonical/holdings/", "etf-classifications"
THRESHOLD = 0.5


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def main():
    cot = _load("cot_etf_classifier", "data/cot/scripts/gold/lib/etf_classifier.py")
    bd = _load("bd_etf_classifier", "data/black_diamond/scripts/gold/lib/etf_classifier.py")
    s3 = boto3.client("s3")
    keys = []
    for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=BUCKET, Prefix=PREFIX):
        keys += [o["Key"] for o in pg.get("Contents", []) if o["Key"].endswith(".parquet")]
    key = sorted(keys)[-1]
    df = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=BUCKET, Key=key)["Body"].read()))
    clf = cot.ETFClassifier.instance()
    unc = []
    total_mv = 0.0
    for r in df.itertuples(index=False):
        mv = 0.0 if pd.isna(r.market_value) else float(r.market_value)
        total_mv += mv
        cusip = getattr(r, "cusip", None)
        cls, _rule = clf.classify_position(None if pd.isna(r.ticker) else r.ticker,
                                           None if cusip is None or pd.isna(cusip) else cusip, r.cash_equivalent)
        if cls == clf.UNCLASSIFIED:
            name = "" if pd.isna(r.asset_name) else str(r.asset_name)
            norm = bd.ETFClassifier.normalize_name(name) if name else ""
            unc.append((name, "NAME::" + norm if norm else "", mv))
    uniq = sorted({k for _, k, _ in unc if k})
    ddb = boto3.client("dynamodb", region_name="us-east-1")
    found = {}
    for i in range(0, len(uniq), 100):
        req = {TABLE: {"Keys": [{"ticker": {"S": k}} for k in uniq[i:i + 100]], "ConsistentRead": True}}
        while req:
            resp = ddb.batch_get_item(RequestItems=req)
            for it in resp["Responses"].get(TABLE, []):
                ac = it.get("asset_class", {}).get("S")
                if ac:
                    found[it["ticker"]["S"]] = ac
            req = resp.get("UnprocessedKeys") or None
    placeable = [(n, k, found[k], mv) for n, k, mv in unc if k in found]
    unc_mv = sum(mv for _, _, mv in unc)
    pl_mv = sum(p[3] for p in placeable)
    pct = 100.0 * pl_mv / total_mv if total_mv else 0.0
    top = sorted(placeable, key=lambda p: -p[3])[:10]
    rec = {
        "as_of": Path(key).stem, "source": f"s3://{BUCKET}/{key}", "positions": int(len(df)),
        "unclassified_positions": len(unc), "unclassified_mv": round(unc_mv, 2), "total_mv": round(total_mv, 2),
        "name_placeable_positions": len(placeable), "name_placeable_mv": round(pl_mv, 2),
        "threshold_pct": THRESHOLD, "material": bool(pct >= THRESHOLD),
        "method": "COT classify_position on every position of the newest canonical holdings partition; each unclassified one's "
                  "NAME::<BD normalize_name(asset_name)> key read from etf-classifications via batch_get_item, counted when a row with an asset_class exists.",
        "top": [{"name": n, "name_key": k, "class": c, "market_value": round(m, 2)} for n, k, c, m in top],
    }
    OUT.write_text(json.dumps(rec, indent=2) + "\n", encoding="utf-8")
    print(f"wrote {OUT.name} pct={pct:.4f} material={rec['material']}")


if __name__ == "__main__":
    main()
