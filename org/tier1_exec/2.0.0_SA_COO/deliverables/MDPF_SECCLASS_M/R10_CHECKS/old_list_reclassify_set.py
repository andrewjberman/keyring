#!/usr/bin/env python3
"""old_list_reclassify_set.py -- MDPF_SECCLASS round 8, cell SC-e-32 (FWD-17, FWD-15): build the old list's reclassification set.

READ-ONLY against AWS (consistent paginated DynamoDB scans of bd-securities and etf-classifications) and against the
Holdings producer's local per-firm parquet builds. NO table write, NO model call. Writes one local file:
  org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_RECLASSIFY_SET_20261007.tsv
tab-separated, header
  old_key  shared_key  held  route  asset_class  sub_asset_class  clean_name
one line per bd-securities key (denominator printed).

shared_key -- the key the row would carry in the shared list, ONLY as the contract (org/standards/MDPF_SECCLASS_CONTRACT.json
              0.5.0, `identifier_namespace`) declares:
                ticker-shaped old key        -> the ticker as itself
                9-character CUSIP-shaped key -> CUSIP:<9>
                NAME::<anything>             -> NAME::<slug>, slug = name upper-cased, every run outside A-Z 0-9 - replaced by ONE
                                                space, trimmed, first 80 characters; an EMPTY slug yields no key (blank)
                any other form               -> itself only when the shared list ALREADY holds it under that key (a present key is
                                                never re-keyed); otherwise blank (no declared form fits it)
route       -- PRESENT      shared_key is already a key of etf-classifications (a present key is never touched)
               DIRECT       the direct-match plan (etf_classification_scheduled.classify_asset_class, rule (i): the old row's value
                            as INPUT, only when its class and its sub-class are already members of the shared list's own
                            vocabulary restricted to the six classes; a fold is never a match) places it
               AI           the plan leaves it UNRESOLVED; class and sub-class BLANK here, decided by SC-e-31's path at the write act
               UNPLACED-KEY shared_key is blank
held        -- the census partition's own definition (OLD_LIST_CENSUS: the old key equals a held SECURITY node's symbol,
               CUSIP:<cusip> or NAME::<80-char slug of its description>), over the same local producer builds; claim: inferred
order       -- non-PRESENT rows first, held=true before held=false (then keys already in their declared form, then old_key);
               PRESENT rows last.
clean_name  -- security_name.clean_name(the old row's name), SC-e-30.

Usage (repo root):  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_reclassify_set.py [--held-root DIR]
"""
from __future__ import annotations

import argparse
import collections
import csv
import importlib.util
import sys
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]
OUT = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_RECLASSIFY_SET_20261007.tsv"
SHARED = ROOT / "infra/aws/lambda/v2_portal/_shared"
COLS = ["old_key", "shared_key", "held", "route", "asset_class", "sub_asset_class", "clean_name"]
SIX = frozenset({"cash", "fixed_income", "equity", "structured", "alternatives", "commodities"})
REGION = "us-east-1"
NAME_PREFIX = "NAME::"
CUSIP_PREFIX = "CUSIP:"


def _load(path: Path, modname: str):
    spec = importlib.util.spec_from_file_location(modname, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def scan_items(table_name: str) -> list:
    table = boto3.resource("dynamodb", region_name=REGION).Table(table_name)
    items, kw = [], {"ConsistentRead": True}
    while True:
        resp = table.scan(**kw)
        items.extend(resp.get("Items", []))
        if "LastEvaluatedKey" not in resp:
            return items
        kw["ExclusiveStartKey"] = resp["LastEvaluatedKey"]


def derive_shared_key(old_key: str, shared_keys: set, census) -> str:
    """The shared-list key a row would carry, by the declared forms only; blank when none fits."""
    if old_key.startswith(NAME_PREFIX):
        slug = census.slug(old_key[len(NAME_PREFIX):])
        return NAME_PREFIX + slug if slug else ""
    if old_key.startswith(CUSIP_PREFIX):
        return old_key
    if census.TICKER_RE.fullmatch(old_key):
        return old_key
    if census.CUSIP_RE.fullmatch(old_key):
        return CUSIP_PREFIX + old_key
    return old_key if old_key in shared_keys else ""


def old_name(row: dict):
    return row.get("name") or row.get("asset_name_raw") or None


def main(argv=None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--held-root", default=str(ROOT / ".scratch"),
                    help="directory holding hb_<firm>/ producer builds (the census's own --held-root)")
    ap.add_argument("--out", default=str(OUT))
    a = ap.parse_args(argv)

    sys.path.insert(0, str(SHARED))
    census = _load(HERE / "old_list_census.py", "old_list_census_for_set")
    from etf_classification_scheduled import TableVocabulary, classify_asset_class
    from security_name import clean_name

    old_rows = scan_items("bd-securities")
    shared_rows = scan_items("etf-classifications")
    shared_keys = {r["ticker"] for r in shared_rows}
    old_by_key = {r["ticker"]: r for r in old_rows}
    assert len(old_by_key) == len(old_rows), "duplicate hash keys in bd-securities"
    print(f"DENOMINATOR old={len(old_rows)} shared={len(shared_keys)}", flush=True)

    # the shared list's own vocabulary, restricted to the six classes (the seed module's multi_asset, if any, never counts)
    live = TableVocabulary.from_live_table()
    vocab = TableVocabulary(
        asset_classes={c for c in live.asset_classes if c in SIX},
        sub_asset_classes={c: set(s) for c, s in live.sub_asset_classes.items() if c in SIX})

    # held today: the census definition, over the same local producer builds
    held_match = set()
    for firm in census.FIRMS:
        nodes, files = census.held_nodes(firm, Path(a.held_root) / ("hb_" + firm))
        if nodes is None:
            raise SystemExit(f"ERROR: held parquet for {firm} not found or ambiguous under {a.held_root} ({files})")
        for nd in nodes:
            _, keys = census.identity_keys(nd)
            held_match |= keys

    rows = []
    for key, row in old_by_key.items():
        sk = derive_shared_key(key, shared_keys, census)
        held = "true" if key in held_match else "false"
        nm = clean_name(old_name(row))
        if sk and sk in shared_keys:
            route, ac, sac = "PRESENT", "", ""
        elif not sk:
            route, ac, sac = "UNPLACED-KEY", "", ""
        else:
            got_ac, got_sac, _ = classify_asset_class(
                sk, vocab=vocab, bd_securities_lookup=lambda _k, _row=row: _row)
            if got_ac in SIX:
                route, ac, sac = "DIRECT", got_ac, got_sac or ""
            else:
                route, ac, sac = "AI", "", ""
        rows.append({"old_key": key, "shared_key": sk, "held": held, "route": route,
                     "asset_class": ac, "sub_asset_class": sac, "clean_name": nm or ""})

    def order(r):
        if r["route"] == "PRESENT":
            return (1, 0, 0, r["old_key"])
        return (0, 0 if r["held"] == "true" else 1, 0 if r["old_key"] == r["shared_key"] else 1, r["old_key"])

    rows.sort(key=order)
    out = Path(a.out)
    with out.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(COLS)
        for r in rows:
            w.writerow([r[c] for c in COLS])

    by_route = collections.Counter(r["route"] for r in rows)
    held_n = sum(1 for r in rows if r["held"] == "true")
    by_route_held = collections.Counter((r["route"], r["held"]) for r in rows)
    dup = collections.Counter(r["shared_key"] for r in rows if r["shared_key"] and r["route"] != "PRESENT")
    dup_keys = {k: n for k, n in dup.items() if n > 1}
    print("WROTE", out.relative_to(ROOT), f"rows={len(rows)}")
    print("by_route", dict(by_route), "sum", sum(by_route.values()))
    print("by_route_held", {f"{k[0]}|held={k[1]}": n for k, n in sorted(by_route_held.items())})
    print(f"held={held_n} distinct_shared_keys_to_write={sum(1 for k in dup)} shared_keys_with_more_than_one_old_row={len(dup_keys)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
