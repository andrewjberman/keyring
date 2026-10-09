#!/usr/bin/env python3
"""e71_reseed_verify.py -- MDPF_SECCLASS SC-e-71 release (the one re-seed): leg G of the CTO half @d6c99a32d5, condition 3.

READ-ONLY (consistent get_item of the 15 snapshot rows). For each row of E71_SEED_ROWS_SNAPSHOT_20261009.json:
  - asset_class and sub_asset_class equal the snapshot (no class moves);
  - updated_by reads 'seed-script';
  - for the 12 seed-source keys, name equals ETF_NAME_OVERRIDES at the repo's HEAD bytes (git show, never the working tree).
Prints E71-RESEED ok=<bool> rows=<n> names_ok=<k>/12 class_moved=[...] by_wrong=[...] name_miss=[...]. Run from the repo root.
The second-dry-run limb (0 of 197) is the seed script's own output, read beside this check.
"""
import json
import subprocess
import sys
import types
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
SNAP = HERE.parent / "E71_SEED_ROWS_SNAPSHOT_20261009.json"
SRC = "infra/aws/lambda/v2_portal/_shared/etf_classification.py"
NAMES = ("AAETX", "AMECX", "CAIBX", "CFIHX", "CLBAX", "FBALX", "FKIQX", "FTYPX", "KAGIX", "MDLOX", "SGIIX", "VTTHX")


def head_overrides():
    src = subprocess.run(["git", "show", "HEAD:" + SRC], capture_output=True, check=True).stdout.decode("utf-8")
    mod = types.ModuleType("etf_classification_head")
    exec(compile(src, SRC, "exec"), mod.__dict__)  # noqa: S102 -- the repo's own module at HEAD, read-only use
    return mod.ETF_NAME_OVERRIDES


def main():
    snap = json.load(open(SNAP, encoding="utf-8"))["rows"]
    want = head_overrides()
    table = boto3.resource("dynamodb", region_name="us-east-1").Table("etf-classifications")
    moved, by_wrong, miss, names_ok = [], [], [], 0
    for key, before in sorted(snap.items()):
        row = table.get_item(Key={"ticker": key}, ConsistentRead=True).get("Item") or {}
        for f in ("asset_class", "sub_asset_class"):
            if row.get(f) != before.get(f):
                moved.append((key, f, before.get(f), row.get(f)))
        if row.get("updated_by") != "seed-script":
            by_wrong.append((key, row.get("updated_by")))
        if key in NAMES:
            if row.get("name") == want.get(key):
                names_ok += 1
            else:
                miss.append((key, row.get("name"), want.get(key)))
    ok = len(snap) == 15 and not moved and not by_wrong and names_ok == len(NAMES)
    print(f"E71-RESEED ok={ok} rows={len(snap)} names_ok={names_ok}/{len(NAMES)} class_moved={moved} "
          f"by_wrong={by_wrong} name_miss={miss}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
