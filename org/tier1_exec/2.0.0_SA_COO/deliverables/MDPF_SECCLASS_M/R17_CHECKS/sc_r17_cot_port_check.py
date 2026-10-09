"""sc_r17_cot_port_check.py -- MDPF_SECCLASS round 17, cell SC-e-84 (the COT NAME:: port). READ-ONLY.

Runs COT's classify_position (data/cot/scripts/gold/lib/etf_classifier.py, as it stands in the working tree) over the SAME
partition SC-e-82 measured (COT_NAME_SHARE_20261009.json `source`), once WITHOUT the name and once WITH it
(keyword `asset_name=`), over each distinct (ticker, cusip, cash_equivalent, asset_name) tuple.

ok=True when ALL hold:
  1. no position placed without the name (rule 'feed cash flag' / 'table ticker' / 'table cusip') changes class or rule with it;
  2. every position that moves out of 'unclassified' does so with rule 'table name';
  3. placed positions >= SC-e-82's name_placeable_positions (the measured floor; a NAME:: row added since can only raise it);
  4. a position the name does not place stays ('unclassified', 'none').
Prints: COT-PORT ok=<bool> positions=<n> placed=<n> placed_mv=<usd> floor=<n> overridden=<n> wrong_rule=<n> reason=<...>
"""
import importlib.util
import io
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
REC = Path(__file__).resolve().parent.parent / "COT_NAME_SHARE_20261009.json"
PLACED_RULES = ("feed cash flag", "table ticker", "table cusip")


def _load(name, rel):
    spec = importlib.util.spec_from_file_location(name, ROOT / rel)
    mod = importlib.util.module_from_spec(spec)
    sys.modules[name] = mod
    spec.loader.exec_module(mod)
    return mod


def _s(v):
    import pandas as pd
    return None if v is None or (not isinstance(v, str) and pd.isna(v)) else v


def main() -> int:
    import boto3
    import pandas as pd

    rec = json.loads(REC.read_text(encoding="utf-8"))
    bucket, key = rec["source"][len("s3://"):].split("/", 1)
    floor = int(rec["name_placeable_positions"])
    cot = _load("cot_etf_classifier_r17", "data/cot/scripts/gold/lib/etf_classifier.py")
    clf = cot.ETFClassifier.instance()
    df = pd.read_parquet(io.BytesIO(boto3.client("s3").get_object(Bucket=bucket, Key=key)["Body"].read()))
    has_cusip = "cusip" in df.columns

    def _tup(r):
        return (_s(r.ticker), _s(getattr(r, "cusip", None)) if has_cusip else None, _s(r.cash_equivalent), _s(r.asset_name))

    def _pair(t):
        return clf.classify_position(t[0], t[1], t[2]), clf.classify_position(t[0], t[1], t[2], asset_name=t[3])

    from concurrent.futures import ThreadPoolExecutor
    distinct = sorted({_tup(r) for r in df.itertuples(index=False)}, key=repr)
    try:
        with ThreadPoolExecutor(max_workers=16) as pool:  # table reads dominate; the bound keeps the run under 120 s
            memo = dict(zip(distinct, pool.map(_pair, distinct)))
    except TypeError as exc:
        print(f"COT-PORT ok=False positions={len(df)} placed=0 placed_mv=0 floor={floor} overridden=0 "
              f"wrong_rule=0 reason=classify_position-rejects-asset_name:{exc}")
        return 1
    placed = overridden = wrong_rule = stayed_bad = 0
    placed_mv = 0.0
    for r in df.itertuples(index=False):
        before, after = memo[_tup(r)]
        mv = 0.0 if pd.isna(r.market_value) else float(r.market_value)
        if before[1] in PLACED_RULES:
            overridden += int(after != before)
        elif after[0] != clf.UNCLASSIFIED:
            placed += 1
            placed_mv += mv
            wrong_rule += int(after[1] != "table name")
        else:
            stayed_bad += int(after != (clf.UNCLASSIFIED, "none"))
    reasons = []
    if overridden:
        reasons.append("overridden")
    if wrong_rule:
        reasons.append("wrong-rule")
    if placed < floor:
        reasons.append("below-floor")
    if stayed_bad:
        reasons.append(f"residue-not-none:{stayed_bad}")
    ok = not reasons
    print(f"COT-PORT ok={ok} positions={len(df)} placed={placed} placed_mv={placed_mv:.2f} floor={floor} "
          f"overridden={overridden} wrong_rule={wrong_rule} reason={','.join(reasons) or 'none'}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
