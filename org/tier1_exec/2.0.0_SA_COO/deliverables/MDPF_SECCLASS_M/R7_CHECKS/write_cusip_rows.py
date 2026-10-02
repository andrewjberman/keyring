#!/usr/bin/env python3
"""
write_cusip_rows.py -- the WRITER for operator-named `CUSIP:` rows (MDPF_SECCLASS; 1.0.0_SA_CTO rulings batch 93
item 2: "a no-ticker holding with a CUSIP is a table row under the existing `CUSIP:` namespace ... written each with
its ground under their own half").

Neither existing path writes these rows: the seed script skips `CUSIP:` keys, and a firm's scheduled detector plans
only what its own evidence resolves. This script REPLAYS a reviewed list as rows of `etf-classifications`.

What it does, and nothing else:
  - reads a set file the operator NAMES (`--set-file`), one row per line, tab-separated:
        <cusip> <TAB> <asset_class> <TAB> <sub_asset_class or empty> <TAB> <name>
    `#` starts a comment. No file, no run: it never derives its own plan.
  - plans one row per line: key `CUSIP:<cusip>`, `identifier_namespace: CUSIP`, `classified_by: scheduled` (the
    class the table's existing `CUSIP:` rows carry), the line's class, sub class and name.
  - DRY RUN BY DEFAULT: prints the plan, every key already present and every refusal. `--write` lands the plan.
  - writes through `etf_classification_scheduled.write()`, the scheduled path's conditional put
    (`attribute_not_exists(ticker)`); this file issues no PutItem of its own.

What it cannot do: it has NO overwrite path and NO delete path. A key that already has a row is reported and left
exactly as it is. A refused line (not a valid unmasked 9-character CUSIP, a class or sub class outside the table's
vocabulary, no name, a duplicate) stops `--write` before the first put, so a run lands the whole list or nothing.

Usage:
  python write_cusip_rows.py --set-file <path>            # dry run
  python write_cusip_rows.py --set-file <path> --write
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parents[6]  # R7_CHECKS -> MDPF_SECCLASS_M -> deliverables -> 2.0.0_SA_COO -> tier1_exec -> org -> root
_SHARED = ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

import etf_classification_scheduled as scheduled  # noqa: E402
from etf_classification_scheduled import (CUSIP_PREFIX, TableVocabulary, existing_tickers,  # noqa: E402
                                          is_valid_cusip)
from etf_classifications_dynamodb import ETFClassifier  # noqa: E402

CLASSIFIED_BY = "scheduled"
UPDATED_BY = "mdpf-secclass-cusip-rows"


def read_set(path: str) -> List[Tuple[int, List[str]]]:
    """[(line number, [cusip, asset_class, sub_asset_class, name])] for every non-comment line."""
    lines: List[Tuple[int, List[str]]] = []
    with open(path, encoding="utf-8") as fh:
        for number, line in enumerate(fh, start=1):
            text = line.split("#", 1)[0].rstrip("\r\n")
            if text.strip():
                lines.append((number, [field.strip() for field in text.split("\t")]))
    return lines


def plan_rows(lines: List[Tuple[int, List[str]]], vocab: TableVocabulary,
              existing: Set[str]) -> Tuple[List[dict], List[Tuple[str, str]], List[str]]:
    """(rows to write, [(line or key, refusal)], keys that already have a row)."""
    rows: List[dict] = []
    refused: List[Tuple[str, str]] = []
    present: List[str] = []
    seen: Set[str] = set()
    for number, fields in lines:
        where = "line %d" % number
        if len(fields) != 4:
            refused.append((where, "SHAPE: %d tab-separated fields, 4 expected" % len(fields)))
            continue
        cusip, asset_class, sub, name = fields
        if not is_valid_cusip(cusip):
            refused.append((where, "NOT-A-CUSIP: %r is not a valid unmasked 9-character CUSIP" % cusip))
            continue
        key = CUSIP_PREFIX + cusip
        if key in seen:
            refused.append((key, "DUPLICATE: named twice in the set"))
            continue
        seen.add(key)
        if asset_class not in vocab.asset_classes:
            refused.append((key, "CLASS-NOT-IN-VOCABULARY: %r" % asset_class))
            continue
        if sub and sub not in vocab.sub_asset_classes.get(asset_class, set()):
            refused.append((key, "SUB-CLASS-NOT-IN-VOCABULARY: %r under %r" % (sub, asset_class)))
            continue
        if not name:
            refused.append((key, "NO-NAME: the row's ground is its custody name"))
            continue
        if key in existing:
            present.append(key)
            continue
        rows.append({
            "ticker": key,
            "identifier_namespace": "CUSIP",
            "asset_class": asset_class,
            "sub_asset_class": sub or None,
            "name": name,
            "classified_by": CLASSIFIED_BY,
            "updated_by": UPDATED_BY,
        })
    return rows, refused, present


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Write operator-named CUSIP: rows (absent keys only)")
    parser.add_argument("--set-file", required=True,
                        help="tab-separated: cusip, asset_class, sub_asset_class (may be empty), name")
    parser.add_argument("--write", action="store_true",
                        help="land the plan (default is a DRY RUN: plan, present keys and refusals only)")
    args = parser.parse_args(argv)

    lines = read_set(args.set_file)
    if not lines:
        print("REFUSED: the set file names no row. This script never derives a plan.")
        return 2

    classifier = ETFClassifier()
    vocab = TableVocabulary.from_live_table(classifier)
    existing = existing_tickers(classifier)
    rows, refused, present = plan_rows(lines, vocab, existing)

    print("CUSIP-ROWS named=%d plan=%d already_present=%d refused=%d (table rows=%d)"
          % (len(lines), len(rows), len(present), len(refused), len(existing)))
    for row in rows:
        print("PLAN     %-16s %-13s %-18s %s" % (row["ticker"], row["asset_class"],
                                                row["sub_asset_class"] or "-", row["name"]))
    for key in present:
        print("PRESENT  %-16s already has a row; left as it is" % key)
    for where, reason in refused:
        print("REFUSED  %-16s %s" % (where, reason))

    if not args.write:
        print("DRY RUN: nothing written. Re-run with --write to land the plan.")
        return 0
    if refused:
        print("BLOCKED: %d line(s) refused; nothing written. Name only writable rows." % len(refused))
        return 3
    if not rows:
        print("OK: nothing to write (every named key already has a row).")
        return 0

    results = scheduled.write(rows)
    written = [key for key, status in results if status == "written"]
    left = [key for key, status in results if status != "written"]
    print("WRITTEN %d of %d: %s" % (len(written), len(rows), " ".join(written)))
    if left:
        print("WARN: %d row(s) appeared between the plan and the put and were left alone: %s"
              % (len(left), " ".join(left)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
