#!/usr/bin/env python3
"""e84_cot_post_fire_read.py -- MDPF_SECCLASS SC-e-84 leg G: READ-ONLY post-fire read of Cottonwood after the NAME:: port ships.

Grades the COO half's conditions 2-3 and the CTO half's conditions 5-6
(NEVER_WIDEN_HALF_REQUEST_SECCLASS_COT_NAME_PORT_20261009.md; CTO_HALF_SECCLASS_SC_E84_COT_NAME_PORT_20261009.md):
  - fire: platinum/firm/mix_summary.json and gold/views/mix_daily_summary.json were rewritten after argv[1] (the ship time, ISO UTC);
  - name-placed set: COT's classify_position (the repo lib, which the ship check proved equals the served bytes) is run over the newest
    canonical holdings partition with and without asset_name; positions that move off 'unclassified' with rule 'table name' are the set;
  - census (CTO 5): the set counted by class; any class outside the six (multi_asset included) is a STOP;
  - served (COO 3): every set position's served class in platinum/clients/*/concentration.json (matched by asset_name on the latest
    date) equals its table class; mismatches are counted;
  - top ten (CTO 6): the ten largest name-placed positions (name, class, rule) printed beside the half's ten (COT_NAME_SHARE_20261009.json);
  - firm unclassified: served mix_summary unclassified market value, printed beside the SC-e-82 baseline.
Prints  E84-G ok=<bool> verdict=<PASS|NOT-YET|STOP> ...  and writes detail JSON to argv[2] if given.
ok = fire rebuilt AND census within the six AND served mismatches == 0. NOT-YET when the fire has not rewritten the mix after argv[1].
"""
import importlib.util
import io
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

import boto3
import pandas as pd

ROOT = Path(__file__).resolve().parents[6]
REC = Path(__file__).resolve().parent.parent / "COT_NAME_SHARE_20261009.json"
B = "opal-data-cot"
SIX = {"equity", "fixed_income", "alternatives", "commodities", "structured", "cash"}


def _s(v):
    return None if v is None or (not isinstance(v, str) and pd.isna(v)) else v


def main(argv) -> int:
    shipped = datetime.fromisoformat(argv[1].replace("Z", "+00:00"))
    s3 = boto3.client("s3")
    mix_head = s3.head_object(Bucket=B, Key="platinum/firm/mix_summary.json")
    view_head = s3.head_object(Bucket=B, Key="gold/views/mix_daily_summary.json")
    rebuilt = mix_head["LastModified"] > shipped and view_head["LastModified"] > shipped
    if not rebuilt:
        print(f"E84-G ok=False verdict=NOT-YET mix_summary={mix_head['LastModified'].isoformat()} shipped={argv[1]}")
        return 1
    spec = importlib.util.spec_from_file_location("cot_clf_g", ROOT / "data/cot/scripts/gold/lib/etf_classifier.py")
    mod = importlib.util.module_from_spec(spec)
    sys.modules["cot_clf_g"] = mod
    spec.loader.exec_module(mod)
    clf = mod.ETFClassifier.instance()
    keys = [o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="gold/canonical/holdings/")
            for o in pg.get("Contents", []) if o["Key"].endswith(".parquet")]
    part = sorted(keys)[-1]
    df = pd.read_parquet(io.BytesIO(s3.get_object(Bucket=B, Key=part)["Body"].read()))
    has_cusip = "cusip" in df.columns
    memo, placed = {}, []
    for r in df.itertuples(index=False):
        t = (_s(r.ticker), _s(getattr(r, "cusip", None)) if has_cusip else None, _s(r.cash_equivalent), _s(r.asset_name))
        if t not in memo:
            memo[t] = (clf.classify_position(t[0], t[1], t[2]), clf.classify_position(t[0], t[1], t[2], asset_name=t[3]))
        before, after = memo[t]
        if before[0] == clf.UNCLASSIFIED and after[1] == "table name":
            mv = 0.0 if pd.isna(r.market_value) else float(r.market_value)
            placed.append({"name": t[3], "class": after[0], "rule": after[1], "market_value": mv})
    census = Counter(p["class"] for p in placed)
    outside = sorted(c for c in census if c not in SIX)
    # served classes by name on each client's latest concentration date
    want = {p["name"]: p["class"] for p in placed}
    served_seen, mismatch = 0, []
    ckeys = [o["Key"] for pg in s3.get_paginator("list_objects_v2").paginate(Bucket=B, Prefix="platinum/clients/")
             for o in pg.get("Contents", []) if o["Key"].endswith("concentration.json")]
    for k in ckeys:
        doc = json.loads(s3.get_object(Bucket=B, Key=k)["Body"].read())
        last = (doc.get("concentration") or [{}])[-1]
        for h in last.get("holdings") or []:
            nm = h.get("asset_name")
            if nm in want:
                served_seen += 1
                if h.get("asset_class") != want[nm]:
                    mismatch.append({"key": k, "name": nm, "served": h.get("asset_class"), "table": want[nm]})
    mix = json.loads(s3.get_object(Bucket=B, Key="platinum/firm/mix_summary.json")["Body"].read())
    unc_now = (mix.get("mix", {}).get("unclassified") or {}).get("market_value")
    rec = json.loads(REC.read_text(encoding="utf-8"))
    top = sorted(placed, key=lambda p: -p["market_value"])[:10]
    ok = not outside and not mismatch
    verdict = "PASS" if ok else "STOP"
    print(f"E84-G ok={ok} verdict={verdict} partition={part.rsplit('/', 1)[-1]} placed={len(placed)} "
          f"placed_mv={sum(p['market_value'] for p in placed):.2f} census={dict(census)} outside_six={outside} "
          f"served_matched={served_seen} served_mismatch={len(mismatch)} firm_unclassified_now={unc_now} "
          f"baseline_unclassified_mv={rec['unclassified_mv']}")
    for i, p in enumerate(top):
        h = rec["top"][i] if i < len(rec["top"]) else {}
        print(f"  top{i + 1}: {p['name']} | {p['class']} | {p['rule']} | {p['market_value']:.2f}  || half: "
              f"{h.get('name')} | {h.get('class')} | {h.get('market_value')}")
    if len(argv) > 2:
        with open(argv[2], "w", encoding="utf-8") as fh:
            json.dump({"partition": part, "placed": len(placed), "census": census, "outside_six": outside,
                       "served_matched": served_seen, "served_mismatch": mismatch[:200], "top": top,
                       "firm_unclassified_now": unc_now}, fh, indent=2, default=str)
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv))
