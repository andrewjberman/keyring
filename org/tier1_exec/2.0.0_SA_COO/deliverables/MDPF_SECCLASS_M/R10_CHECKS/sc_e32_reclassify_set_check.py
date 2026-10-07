#!/usr/bin/env python3
"""sc_e32_reclassify_set_check.py -- MDPF_SECCLASS round 8, cell SC-e-32 (FWD-17, FWD-15): the issuer's check of the old
list's reclassification set. The worker does not edit this file. READ-ONLY: one scan each of DynamoDB bd-securities and
etf-classifications, no write.

Reads org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_RECLASSIFY_SET_20261007.tsv, tab-separated, header
  old_key	shared_key	held	route	asset_class	sub_asset_class	clean_name
and PASSES only if:
  - every bd-securities key appears exactly once as old_key, and no other old_key appears (denominator = the live old list);
  - held is `true` or `false`; route is one of PRESENT, DIRECT, AI, UNPLACED-KEY;
  - PRESENT  <=> shared_key is non-blank and already a key of etf-classifications;
  - DIRECT   : shared_key non-blank and NOT in etf-classifications; asset_class one of the six classes; sub_asset_class blank
               or a value the live table already carries for that asset_class (the value bound: nothing is minted);
  - AI       : shared_key non-blank and not in etf-classifications; asset_class and sub_asset_class blank (the AI path of
               SC-e-31 decides them at the issuer's write act, never in this set);
  - UNPLACED-KEY : shared_key blank (no key form the contract declares fits it);
  - no field anywhere holds `multi_asset`;
  - every held=true row of route DIRECT/AI/UNPLACED-KEY comes before every held=false row of those routes (held first).
Prints RECLASSIFY-SET ok=True|False old_rows=<n> present=<n> direct=<n> ai=<n> unplaced_key=<n> held=<n>.
"""
import collections
import csv
import sys
from pathlib import Path

_REPO = Path(__file__).resolve().parents[6]
SET = _REPO / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_RECLASSIFY_SET_20261007.tsv"
COLS = ["old_key", "shared_key", "held", "route", "asset_class", "sub_asset_class", "clean_name"]
SIX = {"cash", "fixed_income", "equity", "structured", "alternatives", "commodities"}
ROUTES = {"PRESENT", "DIRECT", "AI", "UNPLACED-KEY"}


def scan(table, proj):
    import boto3
    d = boto3.client("dynamodb", region_name="us-east-1")
    out = []
    for pg in d.get_paginator("scan").paginate(TableName=table, ProjectionExpression=proj):
        out.extend(pg["Items"])
    return out


def main():
    if not SET.exists():
        print(f"RECLASSIFY-SET ok=False missing={SET.name}")
        return 1
    with SET.open(encoding="utf-8", newline="") as fh:
        rd = csv.DictReader(fh, delimiter="\t")
        if rd.fieldnames != COLS:
            print(f"RECLASSIFY-SET ok=False header={rd.fieldnames}")
            return 1
        rows = list(rd)
    old_keys = {i["ticker"]["S"] for i in scan("bd-securities", "ticker")}
    shared = scan("etf-classifications", "ticker,asset_class,sub_asset_class")
    shared_keys = {i["ticker"]["S"] for i in shared}
    vocab = collections.defaultdict(set)
    for i in shared:
        if "sub_asset_class" in i and "asset_class" in i:
            vocab[i["asset_class"]["S"]].add(i["sub_asset_class"]["S"])
    fails, seen, counts = [], set(), collections.Counter()
    seen_unheld = False
    for n, r in enumerate(rows, 2):
        if any("multi_asset" in (v or "") for v in r.values()):
            fails.append(f"line{int(n)} multi_asset")
        k, sk, route = r["old_key"], r["shared_key"], r["route"]
        if k in seen:
            fails.append(f"dup:{k}")
        seen.add(k)
        if r["held"] not in ("true", "false"):
            fails.append(f"held:{k}")
        if route not in ROUTES:
            fails.append(f"route:{k}={route}")
            continue
        counts[route] += 1
        if route == "PRESENT":
            if not sk or sk not in shared_keys:
                fails.append(f"present_not_live:{k}")
        elif route == "UNPLACED-KEY":
            if sk:
                fails.append(f"unplaced_has_key:{k}")
        else:
            if not sk or sk in shared_keys:
                fails.append(f"{route.lower()}_key:{k}")
            if route == "DIRECT":
                if r["asset_class"] not in SIX:
                    fails.append("direct_class:{}={}".format(k, r["asset_class"]))
                elif r["sub_asset_class"] and r["sub_asset_class"] not in vocab[r["asset_class"]]:
                    fails.append("direct_sub_minted:{}={}".format(k, r["sub_asset_class"]))
            if route == "AI" and (r["asset_class"] or r["sub_asset_class"]):
                fails.append(f"ai_prefilled:{k}")
        if route != "PRESENT":
            if r["held"] == "false":
                seen_unheld = True
            elif r["held"] == "true" and seen_unheld:
                fails.append(f"held_after_unheld:{k}")
        if sk and route != "PRESENT" and sk in shared_keys:
            fails.append(f"would_overwrite:{k}")
    missing, extra = old_keys - seen, seen - old_keys
    if missing:
        fails.append(f"missing_old_keys={len(missing)}")
    if extra:
        fails.append(f"extra_old_keys={len(extra)}")
    for f in fails[:20]:
        print("FAIL " + f)
    held = sum(1 for r in rows if r["held"] == "true")
    print(f'RECLASSIFY-SET ok={not fails!s} old_rows={len(rows)} present={int(counts["PRESENT"])} direct={int(counts["DIRECT"])} ai={int(counts["AI"])} unplaced_key={int(counts["UNPLACED-KEY"])} held={int(held)} live_old={len(old_keys)} fails={len(fails)}')
    return 0 if not fails else 1


if __name__ == "__main__":
    sys.exit(main())
