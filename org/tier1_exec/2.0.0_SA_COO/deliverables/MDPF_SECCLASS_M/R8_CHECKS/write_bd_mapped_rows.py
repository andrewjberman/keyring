#!/usr/bin/env python3
"""
write_bd_mapped_rows.py -- the one-act WRITER for MDPF_SECCLASS BD forward fix 2 (CTO rulings batch 117 item 4 (ii), batch 139).

Replays an operator-named set file of ticker rows mapped from bd-securities, each pair stated explicitly in the file (nothing
maps at run time). Same shape and the same put as R7_CHECKS/write_cusip_rows.py:
  - set file, tab-separated: ticker, asset_class, sub_asset_class (may be empty), name, bd-securities pair, disposition.
    `#` starts a comment. No file, no run.
  - plans one row per line: the line's class, sub class and name, `classified_by: scheduled`, `updated_by: mdpf-secclass-bd-mapped`.
  - DRY RUN BY DEFAULT; `--write` lands the plan through `etf_classification_scheduled.write()`, the conditional put
    (`attribute_not_exists(ticker)`); no PutItem of its own, no overwrite, no delete.
  - refuses (and so writes nothing under --write): a ticker that is blank, lower case, a `CUSIP:` key or longer than 12
    characters; a class or sub class outside the live table's vocabulary; a duplicate; no name; a malformed line.

Usage:
  python write_bd_mapped_rows.py --set-file <path>            # dry run
  python write_bd_mapped_rows.py --set-file <path> --write
"""
from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import List, Optional, Set, Tuple

ROOT = Path(__file__).resolve().parents[6]  # R8_CHECKS -> MDPF_SECCLASS_M -> deliverables -> 2.0.0_SA_COO -> tier1_exec -> org -> root
_SHARED = ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

import etf_classification_scheduled as scheduled  # noqa: E402
from etf_classification_scheduled import CUSIP_PREFIX, TableVocabulary, existing_tickers  # noqa: E402
from etf_classifications_dynamodb import ETFClassifier  # noqa: E402

CLASSIFIED_BY = "scheduled"
UPDATED_BY = "mdpf-secclass-bd-mapped"


def read_set(path: str) -> List[Tuple[int, List[str]]]:
    lines: List[Tuple[int, List[str]]] = []
    with open(path, encoding="utf-8") as fh:
        for number, line in enumerate(fh, start=1):
            text = line.split("#", 1)[0].rstrip("\r\n")
            if text.strip():
                lines.append((number, [field.strip() for field in text.split("\t")]))
    return lines


def _valid_ticker(t: str) -> bool:
    return bool(t) and t == t.upper() and not t.startswith(CUSIP_PREFIX) and len(t) <= 12 and " " not in t


def plan_rows(lines, vocab: TableVocabulary, existing: Set[str]):
    rows, refused, present, seen = [], [], [], set()
    for number, fields in lines:
        where = "line %d" % number
        if len(fields) != 6:
            refused.append((where, "SHAPE: %d tab-separated fields, 6 expected" % len(fields)))
            continue
        ticker, asset_class, sub, name, _pair, _disp = fields
        if not _valid_ticker(ticker):
            refused.append((where, "NOT-A-TICKER: %r" % ticker))
            continue
        if ticker in seen:
            refused.append((ticker, "DUPLICATE: named twice in the set"))
            continue
        seen.add(ticker)
        if asset_class not in vocab.asset_classes:
            refused.append((ticker, "CLASS-NOT-IN-VOCABULARY: %r" % asset_class))
            continue
        if sub and sub not in vocab.sub_asset_classes.get(asset_class, set()):
            refused.append((ticker, "SUB-CLASS-NOT-IN-VOCABULARY: %r under %r" % (sub, asset_class)))
            continue
        if not name:
            refused.append((ticker, "NO-NAME"))
            continue
        if ticker in existing:
            present.append(ticker)
            continue
        rows.append({"ticker": ticker, "asset_class": asset_class, "sub_asset_class": sub or None, "name": name,
                     "classified_by": CLASSIFIED_BY, "updated_by": UPDATED_BY})
    return rows, refused, present


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description="Write operator-named bd-securities-mapped rows (absent tickers only)")
    parser.add_argument("--set-file", required=True)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args(argv)
    lines = read_set(args.set_file)
    if not lines:
        print("REFUSED: the set file names no row. This script never derives a plan.")
        return 2
    classifier = ETFClassifier()
    vocab = TableVocabulary.from_live_table(classifier)
    existing = existing_tickers(classifier)
    rows, refused, present = plan_rows(lines, vocab, existing)
    print("BD-MAPPED-ROWS named=%d plan=%d already_present=%d refused=%d (table rows=%d)"
          % (len(lines), len(rows), len(present), len(refused), len(existing)))
    for row in rows:
        print("PLAN     %-8s %-13s %-22s %s" % (row["ticker"], row["asset_class"], row["sub_asset_class"] or "-", row["name"]))
    for t in present:
        print("PRESENT  %-8s already has a row; left as it is" % t)
    for where, reason in refused:
        print("REFUSED  %-8s %s" % (where, reason))
    if not args.write:
        print("DRY RUN: nothing written. Re-run with --write to land the plan.")
        return 0
    if refused:
        print("BLOCKED: %d line(s) refused; nothing written." % len(refused))
        return 3
    if not rows:
        print("OK: nothing to write (every named ticker already has a row).")
        return 0
    results = scheduled.write(rows)
    written = [t for t, status in results if status == "written"]
    left = [t for t, status in results if status != "written"]
    print("WRITTEN %d of %d: %s" % (len(written), len(rows), " ".join(written)))
    if left:
        print("WARN: %d row(s) appeared between the plan and the put and were left alone: %s" % (len(left), " ".join(left)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
