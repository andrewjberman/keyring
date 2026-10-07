#!/usr/bin/env python3
"""sc_e62_holdings_enum_equal.py -- MDPF_SECCLASS round 10 SC-e-62 (SC-e-22, row W38-S6): the three HoldingsSnapshot schema
copies' asset-class enums are equal to each other and to the producer's ASSET_CLASS_VALUES, and none holds multi_asset.

READ-ONLY. Finds every enum list inside each schema that contains "equity" and "fixed_income" (the class enums), and reads
ASSET_CLASS_VALUES from holdings_snapshot.py by AST (no import). Prints SC-E62 ok=<bool> with each set.
"""
import ast
import json
import sys
from pathlib import Path

ROOT = Path.cwd()  # the repo root the worker runs from (its own worktree), never this file's tree
COPIES = ["docs/contracts/investor-reporting/v1/HoldingsSnapshot.schema.json",
          "infra/aws/lambda/investor-reporting/_contracts/HoldingsSnapshot.schema.json",
          "infra/aws/lambda/investor-reporting/holdings/contracts/HoldingsSnapshot.schema.json"]
PRODUCER = "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py"


def class_enums(node, out):
    if isinstance(node, dict):
        e = node.get("enum")
        if isinstance(e, list) and "equity" in e and "fixed_income" in e:
            out.append(frozenset(x for x in e if x is not None))
        for v in node.values():
            class_enums(v, out)
    elif isinstance(node, list):
        for v in node:
            class_enums(v, out)


def producer_values():
    tree = ast.parse((ROOT / PRODUCER).read_text(encoding="utf-8"))
    for n in tree.body:
        if isinstance(n, ast.Assign) and any(getattr(t, "id", "") == "ASSET_CLASS_VALUES" for t in n.targets):
            return frozenset(ast.literal_eval(n.value))
    return None


def main():
    sets = []
    for c in COPIES:
        found = []
        class_enums(json.loads((ROOT / c).read_text(encoding="utf-8")), found)
        if not found:
            print(f"SC-E62 ok=False reason=no class enum in {c}")
            return 1
        sets.extend(found)
    prod = producer_values()
    allsets = [*sets, prod]
    in_any = any(s is not None and "multi_asset" in s for s in allsets)
    ok = prod is not None and len(set(allsets)) == 1 and not in_any
    print(f"SC-E62 ok={ok} schema_enums={len(sets)} distinct={len(set(allsets))} producer={sorted(prod or [])} "
          f"multi_asset_in_any={in_any}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
