#!/usr/bin/env python3
"""
r7_fwd9_write.py -- the WRITER for the FWD-9 row set (MDPF_SECCLASS, cell SC-e-17; CTO rulings batch 257 item 6).

What it does, and nothing else:
  - reads the set file `r7_fwd9_row_set.py` wrote (`--set-file`, default FWD9_ROW_SET_20261005.tsv) and takes its
    `WRITE` lines only. A PRESENT-SAME, PRESENT-DIFFERS or OUT line is never written, never overwritten.
  - writes through `etf_classification_scheduled.write()`, the scheduled path's conditional put
    (`attribute_not_exists(ticker)`); this file issues no PutItem of its own and has NO overwrite and NO delete path.
  - the shared write() copies only its own attribute list, which does not name `security_bloomberg`. The ruling
    keeps that string in its own attribute, so a thin table wrapper below adds it to the item of the same put. It
    adds nothing else and changes no condition.
  - DRY RUN BY DEFAULT: it prints the plan and puts nothing.
  - `--write` REFUSES unless ALL of these hold (each printed):
      (a) R7_BBG_READER_CENSUS_20261005.json (cell SC-e-16) has crashes, refuses, miskeys and fails_contract all 0;
      (b) org/standards/MDPF_SECCLASS_CONTRACT.json lists BLOOMBERG in identifier_namespace values (contract 0.4.0,
          the CTO's carrier);
      (c) `--half <path>` names a half whose CTO section reads SIGNED.

Usage:
  python r7_fwd9_write.py                       # dry run
  python r7_fwd9_write.py --write --half <path>
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[5]  # MDPF_SECCLASS_M, deliverables, 2.0.0_SA_COO, tier1_exec, org, then the repo root
_SHARED = ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

DEFAULT_SET = HERE / "FWD9_ROW_SET_20261005.tsv"
CENSUS = HERE.parent / "R7_BBG_READER_CENSUS_20261005.json"
CONTRACT = ROOT / "org" / "standards" / "MDPF_SECCLASS_CONTRACT.json"
CENSUS_ZEROES = ("crashes", "refuses", "miskeys", "fails_contract")


def read_write_lines(path):
    """[planned row dict] for every WRITE line of the set file."""
    rows = []
    with open(path, encoding="utf-8") as fh:
        for number, line in enumerate(fh, start=1):
            fields = line.rstrip("\n").split("\t")
            if len(fields) != 5:
                raise SystemExit("REFUSED: line %d has %d fields, 5 expected" % (number, len(fields)))
            if fields[0] != "WRITE":
                continue
            row = json.loads(fields[4])
            row.pop("days", None)
            if row.get("ticker") != fields[1]:
                raise SystemExit("REFUSED: line %d key %r differs from its item's ticker" % (number, fields[1]))
            rows.append(row)
    return rows


def _find_key(obj, key):
    """All values stored under `key` anywhere in a nested JSON value."""
    found = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                found.append(v)
            found.extend(_find_key(v, key))
    elif isinstance(obj, list):
        for v in obj:
            found.extend(_find_key(v, key))
    return found


def check_census(path=CENSUS):
    if not Path(path).exists():
        return False, "census %s is absent" % Path(path).name
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    bad = []
    for key in CENSUS_ZEROES:
        values = _find_key(data, key)
        if not values:
            bad.append("%s missing" % key)
            continue
        for value in values:
            count = len(value) if isinstance(value, (list, dict)) else value
            if count != 0:
                bad.append("%s=%s" % (key, count))
    if bad:
        return False, "census not clean: %s" % ", ".join(bad)
    return True, "census clean: crashes, refuses, miskeys, fails_contract all 0"


def check_contract(path=CONTRACT):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    spec = data.get("fields", {}).get("identifier_namespace", {})
    if "BLOOMBERG" in (spec.get("values") or []):
        return True, "contract lists BLOOMBERG in identifier_namespace"
    return False, "contract %s identifier_namespace values %s do not list BLOOMBERG (contract 0.4.0 not landed)" % (
        data.get("contract_version"), spec.get("values"))


def check_half(half):
    if not half:
        return False, "no --half named"
    path = Path(half)
    if not path.exists():
        return False, "half %s is absent" % half
    text = path.read_text(encoding="utf-8")
    match = re.search(r"^## CTO half\b[^\n]*$", text, re.MULTILINE)
    if not match:
        return False, "half has no CTO section"
    heading = match.group(0)
    if re.search(r"\bSIGNED\b", heading) and not re.search(r"NOT SIGNED|PENDING|UNSIGNED", heading):
        return True, "CTO section reads SIGNED: %s" % heading
    return False, "CTO section does not read SIGNED: %s" % heading


def preconditions(half):
    results = [("a", check_census()), ("b", check_contract()), ("c", check_half(half))]
    return results, all(ok for _, (ok, _) in results)


class _BloombergTable:
    """Adds `security_bloomberg` to the item of the SAME conditional put; nothing else changes."""

    def __init__(self, table, bloomberg_by_key):
        self._table = table
        self._by_key = bloomberg_by_key

    def put_item(self, Item, **kw):
        verbatim = self._by_key.get(Item.get("ticker"))
        if verbatim:
            Item = dict(Item, security_bloomberg=verbatim)
        return self._table.put_item(Item=Item, **kw)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the FWD-9 row set (absent keys only; dry run by default)")
    parser.add_argument("--set-file", default=str(DEFAULT_SET))
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--half", default=None)
    args = parser.parse_args(argv)

    rows = read_write_lines(args.set_file)
    by_ns = {}
    for row in rows:
        by_ns[row.get("identifier_namespace", "TICKER")] = by_ns.get(row.get("identifier_namespace", "TICKER"), 0) + 1
    print("FWD9-WRITE plan=%d (%s) from %s" % (len(rows), ", ".join("%s=%d" % kv for kv in sorted(by_ns.items())),
                                              Path(args.set_file).name))
    if not all(str(row.get("name", "")).isascii() for row in rows):
        print("REFUSED: a WRITE row carries a non-ASCII name (a served-table name is ASCII).")
        return 3

    results, ok = preconditions(args.half)
    for letter, (passed, why) in results:
        print("PRECONDITION (%s) %s: %s" % (letter, "MET" if passed else "NOT MET", why))

    if not args.write:
        print("DRY RUN: nothing written. %d WRITE line(s) planned; --write refuses unless all three preconditions hold."
              % len(rows))
        return 0
    if not ok:
        print("REFUSED: --write needs all three preconditions; nothing written.")
        return 4

    import boto3
    import etf_classification_scheduled as scheduled

    table = boto3.resource("dynamodb", region_name=scheduled.REGION).Table(scheduled.TABLE_NAME)
    wrapped = _BloombergTable(table, {r["ticker"]: r.get("security_bloomberg") for r in rows})
    outcome = scheduled.write(rows, table=wrapped)
    written = [k for k, s in outcome if s == "written"]
    left = [k for k, s in outcome if s != "written"]
    print("WRITTEN %d of %d" % (len(written), len(rows)))
    if left:
        print("WARN: %d row(s) appeared between the plan and the put and were left alone: %s" % (len(left), " ".join(left)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
