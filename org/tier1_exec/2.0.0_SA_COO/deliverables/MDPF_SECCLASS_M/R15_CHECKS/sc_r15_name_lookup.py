"""sc_r15_name_lookup.py -- MDPF_SECCLASS round 15 cell SC-e-76 check: BD's classify_with_identity reads the NAME:: row for a
blank-ticker position the identity chain cannot place.

READ-ONLY (DynamoDB get-item on etf-classifications through the BD lib's own client). Inputs: the group-A securities of
BD_UNCLASSIFIED_TRACE_D1S11_20261008.json (row D1-S11): blank ticker, a canonical NAME:: row present, unclassified today.
For each: ETFClassifier.classify_with_identity('', name, <its one CUSIP or None>) from the tree's
data/black_diamond/scripts/gold/lib/etf_classifier.py must return a non-empty class equal to that NAME:: row's class.
ok when at least 99 pct of group A resolves (rows written or changed after the trace may move a handful).
Run from the repo root you are grading.
Prints  NAME-LOOKUP ok=<bool> group_a=<n> resolved=<n> mismatch=<n> first_miss=[...]
"""
import json
import sys
from pathlib import Path

ROOT = Path.cwd()
sys.path.insert(0, str(ROOT / "data/black_diamond/scripts/gold/lib"))
sys.path.insert(0, str(ROOT / "data/black_diamond/scripts/gold"))
TRACE = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/BD_UNCLASSIFIED_TRACE_D1S11_20261008.json"


def main():
    from etf_classifier import ETFClassifier
    clf = ETFClassifier.instance()
    rows = [r for r in json.loads(TRACE.read_text(encoding="utf-8"))["rows"] if str(r.get("why", "")).startswith("A:")]
    resolved, miss = 0, []
    for r in rows:
        cusips = r.get("cusips") or []
        want = (r.get("canonical_now") or {}).get("by_NAME_key")
        got = clf.classify_with_identity("", r["name"], cusips[0] if len(cusips) == 1 else None)
        if got[0] and got[0] == want:
            resolved += 1
        else:
            miss.append((r["name"][:40], got[0], got[3], want))
    ok = bool(rows) and resolved >= 0.99 * len(rows)
    print(f"NAME-LOOKUP ok={ok} group_a={len(rows)} resolved={resolved} mismatch={len(miss)} first_miss={miss[:3]}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
