#!/usr/bin/env python3
"""MDPF_SECCLASS round 8, cell SC-e-21 (criterion SC8-e21-AC2): the seed plan against the live table.

READ-ONLY. It imports the seed script's own merge rule (merge_item, item_differs) from the tree it runs in,
does ONE consistent paginated scan of etf-classifications, and plans every module ticker exactly as
`seed-etf-classifications.py --dry-run` would. It writes nothing: no put, no update, no file.

Prints one line:
  SEED-SIX-CLASS ok=<bool> module_tickers=<n> conflicts=<n> off_vocab=<n> remap_keys_moved=<n> multi_asset_tokens=<n>

ok=True only when:
  - conflicts == 0             (no field where the module and the table both carry a value and differ)
  - off_vocab == 0             (every module asset_class is one of the six classes)
  - remap_keys_moved == 0      (for every SEED key of the rule-B remap set, the planned asset_class and
                                sub_asset_class equal the live row's: the seed run would not undo the remap)
  - multi_asset_tokens == 0    (the token is gone from the seed module)
Each failing key is printed above the summary line, so the denominator and the reason travel together.
"""
import importlib.util
import sys
from pathlib import Path

import boto3

ROOT = Path(__file__).resolve().parents[6]
SHARED = ROOT / "infra/aws/lambda/v2_portal/_shared"
SEED = ROOT / "infra/aws/lambda/v2_portal/yang_pipeline/seed-etf-classifications.py"
MODULE = SHARED / "etf_classification.py"
REMAP_SET = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R9_CHECKS/MULTI_ASSET_REMAP_B_SET_20261007.tsv"
SIX = {"cash", "fixed_income", "equity", "structured", "alternatives", "commodities"}
TABLE = "etf-classifications"


def load_seed():
    sys.path.insert(0, str(SHARED))
    spec = importlib.util.spec_from_file_location("seed_etf_classifications", str(SEED))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def scan_live():
    table = boto3.resource("dynamodb", region_name="us-east-1").Table(TABLE)
    items, kwargs = {}, {"ConsistentRead": True}
    while True:
        resp = table.scan(**kwargs)
        for row in resp.get("Items", []):
            items[str(row["ticker"])] = dict(row)
        last = resp.get("LastEvaluatedKey")
        if not last:
            return items
        kwargs["ExclusiveStartKey"] = last


def remap_seed_keys():
    keys = []
    for line in REMAP_SET.read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        cols = line.split("\t")
        if len(cols) > 3 and cols[3] == "seed":
            keys.append(cols[0])
    return keys


def main():
    seed = load_seed()
    tickers = set()
    for name in ("ETF_CLASSIFICATIONS", "ETF_MANAGEMENT_STYLE", "ETF_SUB_ASSET_CLASS", "ETF_SECTOR_MAPPING"):
        tickers.update(getattr(seed, name).keys())
    live = scan_live()

    conflicts = []
    for t in sorted(tickers):
        _, _, c = seed.merge_item(t, live.get(t), "1970-01-01T00:00:00Z")
        conflicts.extend(c)
    for t, field, lv, mv in conflicts:
        print(f"CONFLICT {t} {field} table={lv!r} module={mv!r}")

    off_vocab = sorted(t for t, v in seed.ETF_CLASSIFICATIONS.items() if v not in SIX)
    for t in off_vocab:
        print(f"OFF-VOCAB {t} asset_class={seed.ETF_CLASSIFICATIONS[t]!r}")

    moved = []
    rk = remap_seed_keys()
    for t in rk:
        row = live.get(t)
        if row is None:
            moved.append((t, "absent-from-table", "", ""))
            continue
        item, _, _ = seed.merge_item(t, row, "1970-01-01T00:00:00Z")
        for field in ("asset_class", "sub_asset_class"):
            if str(item.get(field, "")) != str(row.get(field, "")):
                moved.append((t, field, row.get(field, ""), item.get(field, "")))
    for t, field, lv, pv in moved:
        print(f"REMAP-MOVED {t} {field} live={lv!r} planned={pv!r}")
    # INFORMATIONAL, not in ok: merge_item drops MODEL_ONLY_FIELDS (low_confidence) on every seed write, so a seed
    # run would strip the low_confidence flag the rule-B remap set on these keys. The issuer's seed-run half decides.
    lose_lc = sorted(t for t in rk if live.get(t, {}).get("low_confidence") is True)
    print(f"INFO low_confidence_would_drop={len(lose_lc)} keys={','.join(lose_lc)}")

    tokens = MODULE.read_text(encoding="utf-8").count("multi_asset")
    ok = not conflicts and not off_vocab and not moved and tokens == 0
    print(f"SEED-SIX-CLASS ok={ok} module_tickers={len(tickers)} live_rows={len(live)} remap_seed_keys={len(rk)} "
          f"conflicts={len(conflicts)} off_vocab={len(off_vocab)} remap_keys_moved={len(moved)} "
          f"multi_asset_tokens={tokens}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
