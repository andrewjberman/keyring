"""sc_r16_ticker_no_row.py -- MDPF_SECCLASS round 16 cell SC-e-79 check (row D1-W66-S3): BD's classify_with_identity falls back to the
NAME:: row when a position carries a ticker that has NO row, and serves the match source.

READ-ONLY (DynamoDB get-item on etf-classifications). Inputs: the group-A securities of BD_UNCLASSIFIED_TRACE_D1S11_20261008.json that
carry a non-blank ticker. For each one whose ticker has no row in the live table today (the ticker-no-row hop), it calls
ETFClassifier.classify_with_identity(ticker, name, <its one CUSIP or None>) from the tree's data/black_diamond/scripts/gold/lib/etf_classifier.py.
The result's class must equal the live NAME:: row's class, and its hop (index 3) must name the name key (contain "name").
ok when every such security resolves this way and the set is not empty. Run from the repo root you are grading.
Prints  TICKER-NO-ROW ok=<bool> with_ticker=<n> ticker_no_row=<n> resolved=<n> first_miss=[...]
"""
import json
import sys
from pathlib import Path

import boto3

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / "data/black_diamond/scripts/gold/lib"))
sys.path.insert(0, str(ROOT / "data/black_diamond/scripts/gold"))
TRACE = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_UNCLASSIFIED_TRACE_D1S11_20261008.json"


def main():
    from etf_classifier import ETFClassifier
    clf = ETFClassifier.instance()
    table = boto3.resource("dynamodb", region_name="us-east-1").Table("etf-classifications")
    rows = [r for r in json.loads(TRACE.read_text(encoding="utf-8"))["rows"]
            if str(r.get("why", "")).startswith("A:") and (r.get("ticker") or "").strip()]
    tnr, resolved, miss = 0, 0, []
    for r in rows:
        tk = r["ticker"].strip().upper()
        if table.get_item(Key={"ticker": tk}, ConsistentRead=True).get("Item"):
            continue  # the ticker has a row today: not the ticker-no-row hop
        name_row = table.get_item(Key={"ticker": r["name_key"]}, ConsistentRead=True).get("Item") or {}
        want = name_row.get("asset_class")
        if not want:
            continue  # no NAME:: row today: nothing to fall back to
        tnr += 1
        cusips = r.get("cusips") or []
        got = clf.classify_with_identity(tk, r["name"], cusips[0] if len(cusips) == 1 else None)
        if got[0] == want and "name" in str(got[3]).lower():
            resolved += 1
        else:
            miss.append((tk, got[0], got[3], want))
    ok = tnr > 0 and resolved == tnr
    print(f"TICKER-NO-ROW ok={ok} with_ticker={len(rows)} ticker_no_row={tnr} resolved={resolved} first_miss={miss[:3]}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
