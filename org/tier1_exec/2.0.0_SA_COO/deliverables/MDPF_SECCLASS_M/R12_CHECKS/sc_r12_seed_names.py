"""sc_r12_seed_names.py -- MDPF_SECCLASS round 12 cell SC-e-71 check: the 12 SEED-SOURCE names read clean_name()'s output.

READ-ONLY, no AWS. The 12 keys are the SEED-SOURCE rows of CLEAN_NAME_ROW_SET_V2_20261007.tsv (e48). A seed row always wins over the
table, so their names change only when the seed source does: _shared/etf_classification.py ETF_NAME_OVERRIDES.
For each key: ETF_NAME_OVERRIDES[key] must equal clean_name(<the set's current_name>), recomputed here with the tree's clean_name.
Run from the repo root you are grading.
Prints  SEED-NAMES ok=<bool> keys=12 match=<n> first_miss=[...]
"""
import csv
import sys
from pathlib import Path

ROOT = Path.cwd()
SHARED = ROOT / "infra/aws/lambda/v2_portal/_shared"
sys.path.insert(0, str(SHARED))
SET = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_V2_20261007.tsv"


def main():
    import etf_classification as seed
    from security_name import clean_name
    with SET.open(encoding="utf-8", newline="") as fh:
        rows = [r for r in csv.DictReader(fh, delimiter="\t", quoting=csv.QUOTE_NONE) if r["action"] == "SEED-SOURCE"]
    miss = []
    for r in rows:
        want = clean_name(r["current_name"])
        got = seed.ETF_NAME_OVERRIDES.get(r["key"])
        if got != want:
            miss.append((r["key"], got, want))
    ok = len(rows) == 12 and not miss
    print(f"SEED-NAMES ok={ok} keys={len(rows)} match={len(rows) - len(miss)} first_miss={miss[:3]}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
