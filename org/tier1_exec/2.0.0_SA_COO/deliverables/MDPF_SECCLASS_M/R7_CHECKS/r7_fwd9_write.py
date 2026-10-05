#!/usr/bin/env python3
"""
r7_fwd9_write.py -- the WRITER for the FWD-9 row set (MDPF_SECCLASS, cell SC-e-17; CTO rulings batch 257 item 6).

What it does, and nothing else:
  - reads the set file `r7_fwd9_row_set.py` wrote (`--set-file`, default FWD9_ROW_SET_20261005.tsv) and takes its
    `WRITE` lines only. A PRESENT-SAME, PRESENT-DIFFERS or OUT line is never written, never overwritten.
  - writes through `etf_classification_scheduled.write()`, the scheduled path's conditional put
    (`attribute_not_exists(ticker)`); this file issues no PutItem of its own and has NO overwrite and NO delete path.
  - the shared write() carries `security_bloomberg` and `listing_country` in its own attribute list (cell SC-e-17
    amendment 1), so this file has no table wrapper: the producer (SC-e-19) and this writer put through one path.
  - DRY RUN BY DEFAULT: it prints the plan and puts nothing.
  - `--write` REFUSES unless ALL of these hold (each printed):
      (a) R7_BBG_READER_CENSUS_20261005.json (cell SC-e-16) grades every reader TOLERATES or READ-ONLY, lists none
          uncensused, and any crashes / refuses / miskeys / fails_contract counter it carries is 0 (row W14-S4);
      (b) org/standards/MDPF_SECCLASS_CONTRACT.json lists BLOOMBERG in identifier_namespace values (contract 0.4.0,
          the CTO's carrier);
      (c) `--half <path>` names a half whose COO and CTO headings both read SIGNED for the branch written (`--namespace`);
          a run over every WRITE line needs both headings to read BOTH BRANCHES.

Usage:
  python r7_fwd9_write.py                       # dry run
  python r7_fwd9_write.py --write --half <path>
"""
from __future__ import annotations

import argparse
import collections
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
# SC-e-16 grades each reader with a verdict, not with counters (row W14-S4): a reader is clean only when its verdict is
# one of these. Any other verdict, an empty reader list or an uncensused file fails closed.
CLEAN_VERDICTS = ("TOLERATES", "READ-ONLY")


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
    """(ok, why). The census is clean when every reader's verdict is in CLEAN_VERDICTS, nothing is uncensused and any of the
    four counters it carries is 0. A counter the census does not carry is not read as 0; the verdicts carry the grade."""
    if not Path(path).exists():
        return False, "census %s is absent" % Path(path).name
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    readers = data.get("readers") or []
    if not readers:
        return False, "census lists no readers"
    bad = []
    verdicts = collections.Counter(str(r.get("verdict")) for r in readers)
    for verdict, n in sorted(verdicts.items()):
        if verdict not in CLEAN_VERDICTS:
            bad.append("verdict %s=%d" % (verdict, n))
    uncensused = (data.get("denominator") or {}).get("uncensused")
    if uncensused is None:
        bad.append("denominator.uncensused missing")
    elif (len(uncensused) if isinstance(uncensused, (list, dict)) else uncensused) != 0:
        bad.append("uncensused=%s" % (len(uncensused) if isinstance(uncensused, (list, dict)) else uncensused))
    for key in CENSUS_ZEROES:
        for value in _find_key(data, key):
            count = len(value) if isinstance(value, (list, dict)) else value
            if count != 0:
                bad.append("%s=%s" % (key, count))
    if bad:
        return False, "census not clean: %s" % ", ".join(bad)
    return True, "census clean: %d readers (%s), 0 uncensused" % (
        len(readers), ", ".join("%s %d" % kv for kv in sorted(verdicts.items())))


def check_contract(path=CONTRACT):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    spec = data.get("fields", {}).get("identifier_namespace", {})
    if "BLOOMBERG" in (spec.get("values") or []):
        return True, "contract lists BLOOMBERG in identifier_namespace"
    return False, "contract %s identifier_namespace values %s do not list BLOOMBERG (contract 0.4.0 not landed)" % (
        data.get("contract_version"), spec.get("values"))


BRANCH_WORDS = {"BLOOMBERG": ("BRANCH 1", "BLOOMBERG"), "TICKER": ("BRANCH 2", "TICKER")}


def _section_signs(text, who, namespace):
    """(ok, why) for one `## <who> half` heading. It must read SIGNED (no PENDING / UNSIGNED / NOT SIGNED) and name the
    branch being written: `BRANCH 1` or `BLOOMBERG` for --namespace BLOOMBERG, `BRANCH 2` or `TICKER` for --namespace
    TICKER, `BOTH BRANCHES` for either or for a run over every WRITE line. A heading that names a branch as HELD does
    not sign it."""
    match = re.search(r"^## %s half\b[^\n]*$" % who, text, re.MULTILINE)
    if not match:
        return False, "half has no %s section" % who
    heading = match.group(0)
    upper = heading.upper()
    if not re.search(r"\bSIGNED\b", upper) or re.search(r"NOT SIGNED|PENDING|UNSIGNED", upper):
        return False, "%s section does not read SIGNED: %s" % (who, heading)
    if "BOTH BRANCHES" in upper:
        return True, "%s section signs both branches: %s" % (who, heading)
    if namespace is None:
        return False, "%s section signs one branch; a run over every WRITE line needs BOTH BRANCHES: %s" % (who, heading)
    for word in BRANCH_WORDS[namespace]:
        at = upper.find(word)
        if at >= 0 and "HELD" not in upper[at:at + len(word) + 12]:
            return True, "%s section signs %s: %s" % (who, namespace, heading)
    return False, "%s section does not sign %s: %s" % (who, namespace, heading)


def check_half(half, namespace=None):
    if not half:
        return False, "no --half named"
    path = Path(half)
    if not path.exists():
        return False, "half %s is absent" % half
    text = path.read_text(encoding="utf-8")
    whys = []
    for who in ("COO", "CTO"):
        ok, why = _section_signs(text, who, namespace)
        if not ok:
            return False, why
        whys.append(why)
    return True, "; ".join(whys)


def preconditions(half, namespace=None):
    results = [("a", check_census()), ("b", check_contract()), ("c", check_half(half, namespace))]
    return results, all(ok for _, (ok, _) in results)


def main(argv=None):
    parser = argparse.ArgumentParser(description="Write the FWD-9 row set (absent keys only; dry run by default)")
    parser.add_argument("--set-file", default=str(DEFAULT_SET))
    parser.add_argument("--write", action="store_true")
    parser.add_argument("--half", default=None)
    parser.add_argument("--namespace", choices=("BLOOMBERG", "TICKER"), default=None,
                        help="write only the WRITE lines of this identifier_namespace (the half signs one branch at a time)")
    args = parser.parse_args(argv)

    rows = read_write_lines(args.set_file)
    if args.namespace:
        rows = [row for row in rows if row.get("identifier_namespace", "TICKER") == args.namespace]
        print("NAMESPACE %s: %d WRITE line(s) selected" % (args.namespace, len(rows)))
    by_ns = {}
    for row in rows:
        by_ns[row.get("identifier_namespace", "TICKER")] = by_ns.get(row.get("identifier_namespace", "TICKER"), 0) + 1
    print("FWD9-WRITE plan=%d (%s) from %s" % (len(rows), ", ".join("%s=%d" % kv for kv in sorted(by_ns.items())),
                                              Path(args.set_file).name))
    if not all(str(row.get("name", "")).isascii() for row in rows):
        print("REFUSED: a WRITE row carries a non-ASCII name (a served-table name is ASCII).")
        return 3

    results, ok = preconditions(args.half, args.namespace)
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
    outcome = scheduled.write(rows, table=table)
    written = [k for k, s in outcome if s == "written"]
    left = [k for k, s in outcome if s != "written"]
    print("WRITTEN %d of %d" % (len(written), len(rows)))
    if left:
        print("WARN: %d row(s) appeared between the plan and the put and were left alone: %s" % (len(left), " ".join(left)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
