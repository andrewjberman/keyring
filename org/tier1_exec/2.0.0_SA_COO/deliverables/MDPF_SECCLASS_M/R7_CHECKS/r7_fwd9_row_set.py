#!/usr/bin/env python3
"""
r7_fwd9_row_set.py -- the FWD-9 universe row set (MDPF_SECCLASS, cell SC-e-17; CTO rulings batch 257).

READS ONLY. It reads Rival Funds' served canonical_shape (column-pruned, newest revision of each day), maps every
distinct security through the shared module `rivalfunds_classification.classify_canonical_row`, reads each key from
`etf-classifications` with a consistent get, and writes ONE tab-separated line per security to the set file:

    action <TAB> key <TAB> security_bloomberg <TAB> name <TAB> item JSON

Actions:
  WRITE          no row for the key: the writer may put it (on absence).
  PRESENT-SAME   a row exists with the same asset_class and sub_asset_class. Left as it is.
  PRESENT-DIFFERS a row exists with another class or sub-class. NEVER overwritten; listed for the CTO. Its item JSON
                 holds {"planned": ..., "existing": ...}.
  OUT            not in the domain (Q4: not Equity, a cash line, or no parseable Bloomberg identifier).

Prints: FWD9-ROW-SET securities=<n> write=<n> present_same=<n> present_differs=<n> out=<n>

A security is taken as its NEWEST record in the window (a class can resolve later). Nothing here writes to S3 or to
DynamoDB, apart from the local set file.

Usage: python r7_fwd9_row_set.py [--out <tsv>] [--cache <pickle>]
  --cache: a pickle of [(date, [record, ...]), ...] from an earlier read of the same input (development only; the
  default reads S3).
"""
from __future__ import annotations

import argparse
import collections
import json
import pickle
import sys
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]  # R7_CHECKS -> MDPF_SECCLASS_M -> deliverables -> 2.0.0_SA_COO -> tier1_exec -> org -> root
_SHARED = ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"
if str(_SHARED) not in sys.path:
    sys.path.insert(0, str(_SHARED))

from rivalfunds_classification import classify_canonical_row  # noqa: E402

REGION = "us-east-1"
TABLE = "etf-classifications"
BASE = "opal-data-etfs/rivalfunds/etfs/gold/canonical_shape"
COLUMNS = ["security_bloomberg", "security_ticker", "security_name", "security_cusip", "provider_security_type",
           "position_type", "is_cash_line", "asset_class", "gics_sector", "gics_status"]
DEFAULT_OUT = Path(__file__).resolve().parent / "FWD9_ROW_SET_20261005.tsv"


def _retry(call, tries=12):
    """Run call(fresh) until it returns; `fresh` is True on a retry so the caller can build a new client."""
    for attempt in range(tries):
        try:
            return call(attempt > 0)
        except OSError:
            if attempt == tries - 1:
                raise
            time.sleep(3 + 3 * attempt)


def read_universe():
    """[(date, [record, ...])] for the newest revision of each day, column-pruned, 16 threads.

    The laptop link drops requests now and then (a body, a listing), so every S3 call retries with a fresh client.
    """
    import pyarrow.fs as pf
    import pyarrow.parquet as pq

    def client(fresh=False):
        return pf.S3FileSystem(region=REGION)

    fs = client()
    days = sorted(i.path for i in _retry(lambda fresh: (client() if fresh else fs).get_file_info(pf.FileSelector(BASE)))
                  if i.type == pf.FileType.Directory)

    def newest(day):
        for attempt in range(4):  # a listing can miss a partition that is being re-landed; retry, then say so
            infos = _retry(lambda fresh: (client() if fresh else fs).get_file_info(
                pf.FileSelector(day, allow_not_found=True)))
            files = [f.path for f in infos if f.path.endswith(".parquet")]
            if files:
                return max(files)  # the revision stamp is in the file name, so the max name is the newest
            time.sleep(2 * (attempt + 1))
        print("WARN: no parquet under %s after 4 listings; day skipped" % day, file=sys.stderr)
        return None

    done = []

    def read(path):
        table = _retry(lambda fresh: pq.read_table(path, columns=COLUMNS, filesystem=client() if fresh else fs))
        done.append(path)
        if len(done) % 50 == 0:
            print("read %d files" % len(done), file=sys.stderr, flush=True)
        return path.split("date=")[1].split("/")[0], table.to_pylist()

    with ThreadPoolExecutor(16) as pool:
        files = [f for f in pool.map(newest, days) if f]
        print("days listed=%d with a parquet=%d" % (len(days), len(files)))
        return list(pool.map(read, files))


def distinct_securities(universe):
    """{identifier: (record to grade, days seen)} over the window.

    The identifier is `security_bloomberg`, or `NOBBG:<ticker|cusip|name>` for a record that carries none. The
    record graded is the newest one the shared module places IN the domain (Q4); a security that is never in
    the domain is graded on its newest record, which then reads OUT. An empty `security_name` is filled from the
    newest record of the same security that has one. A record with no identifier at all is not a security.
    """
    newest, in_domain, name_of = {}, {}, {}
    seen_days = collections.Counter()
    for day, records in sorted(universe, key=lambda x: x[0]):
        today = set()
        for rec in records:
            ident = rec.get("security_bloomberg")
            if not ident:
                tag = rec.get("security_ticker") or rec.get("security_cusip") or rec.get("security_name")
                if not tag:
                    continue
                ident = "NOBBG:%s" % tag
            newest[ident] = rec  # sorted by date, so the last write is the newest day
            if classify_canonical_row(rec) is not None:
                in_domain[ident] = rec
            if (rec.get("security_name") or "").strip():
                name_of[ident] = rec["security_name"]
            today.add(ident)
        seen_days.update(today)
    graded = {}
    for ident, rec in newest.items():
        rec = dict(in_domain.get(ident, rec))
        if not (rec.get("security_name") or "").strip() and ident in name_of:
            rec["security_name"] = name_of[ident]
        graded[ident] = (rec, seen_days[ident])
    return graded


def consistent_gets(keys):
    import boto3

    table = boto3.resource("dynamodb", region_name=REGION).Table(TABLE)

    def get(key):
        return key, table.get_item(Key={"ticker": key}, ConsistentRead=True).get("Item")

    with ThreadPoolExecutor(8) as pool:
        return dict(pool.map(get, keys))


def _plain(value):
    try:
        from decimal import Decimal
        if isinstance(value, Decimal):
            return int(value) if value == value.to_integral_value() else float(value)
    except ImportError:
        pass
    return value


def out_reason(rec):
    if rec.get("provider_security_type") != "Equity":
        return "provider_security_type=%s (Q4 needs Equity); asset_class=%s" % (rec.get("provider_security_type"),
                                                                            rec.get("asset_class"))
    if (str(rec.get("position_type") or "").lower() == "cash") or rec.get("is_cash_line") is True:
        return "cash line"
    return "no parseable Bloomberg identifier"


def main(argv=None):
    parser = argparse.ArgumentParser(description="FWD-9 universe row set (reads only)")
    parser.add_argument("--out", default=str(DEFAULT_OUT))
    parser.add_argument("--cache", default=None)
    args = parser.parse_args(argv)

    if args.cache:
        with open(args.cache, "rb") as fh:
            universe = pickle.load(fh)
    else:
        universe = read_universe()
    securities = distinct_securities(universe)

    planned = {}   # ident -> planned row
    outs = {}      # ident -> reason
    for ident, (rec, _days) in securities.items():
        row = classify_canonical_row(rec)
        if row is None:
            outs[ident] = out_reason(rec)
        else:
            planned[ident] = row

    keys = sorted({row["ticker"] for row in planned.values()})
    existing = consistent_gets(keys)

    lines = []
    counts = collections.Counter()
    claimed = {}
    for ident in sorted(securities):
        rec, days = securities[ident]
        name = (rec.get("security_name") or "").replace("\t", " ").replace("\n", " ")
        if ident in outs:
            lines.append(("OUT", ident, rec.get("security_bloomberg") or "", name,
                          json.dumps({"reason": outs[ident], "days": days}, sort_keys=True)))
            counts["OUT"] += 1
            continue
        row = planned[ident]
        key = row["ticker"]
        if key in claimed:
            raise SystemExit("REFUSED: two securities map to key %s (%s, %s)" % (key, claimed[key], ident))
        claimed[key] = ident
        row = dict(row)
        row["days"] = days
        have = existing.get(key)
        if have is None:
            action, item = "WRITE", row
        else:
            same = (have.get("asset_class") == row["asset_class"]
                    and have.get("sub_asset_class") == row.get("sub_asset_class"))
            if same:
                action, item = "PRESENT-SAME", row
            else:
                action = "PRESENT-DIFFERS"
                item = {"planned": row, "existing": {k: _plain(v) for k, v in have.items()
                                                      if k in ("ticker", "asset_class", "sub_asset_class",
                                                               "instrument_kind", "classified_by", "name")}}
        counts[action] += 1
        lines.append((action, key, rec.get("security_bloomberg") or "", name, json.dumps(item, sort_keys=True)))

    with open(args.out, "w", encoding="utf-8", newline="\n") as fh:
        for line in lines:
            fh.write("\t".join(line) + "\n")

    inputs = collections.Counter(r["input"] for r in planned.values())
    print("by sub-class input: %s; low_confidence=%d; non-US=%d; non-ASCII names=%d"
          % (dict(inputs), sum(1 for r in planned.values() if r.get("low_confidence")),
             sum(1 for r in planned.values() if r["ticker"].startswith("BBG:")),
             sum(1 for r in planned.values() if not r["name"].isascii())))
    kinds = collections.Counter()
    for line in lines:
        if line[0] == "PRESENT-DIFFERS":
            item = json.loads(line[4])
            planned_row, have = item["planned"], item["existing"]
            if have.get("asset_class") != planned_row["asset_class"]:
                kinds["asset_class differs"] += 1
            elif not planned_row.get("sub_asset_class"):
                kinds["planned has no sub-class (low_confidence); existing has %s" % ("one" if have.get("sub_asset_class") else "none")] += 1
            elif not have.get("sub_asset_class"):
                kinds["existing has no sub-class; planned has one"] += 1
            else:
                kinds["both have a sub-class and they differ"] += 1
    print("PRESENT-DIFFERS by kind: %s" % dict(kinds))
    print("PRESENT-DIFFERS keys: %s" % " ".join(line[1] for line in lines if line[0] == "PRESENT-DIFFERS"))
    outs_by = collections.Counter(json.loads(line[4])["reason"].split(";")[0] for line in lines if line[0] == "OUT")
    print("OUT by reason: %s" % dict(outs_by))
    print("FWD9-ROW-SET securities=%d write=%d present_same=%d present_differs=%d out=%d"
          % (len(lines), counts["WRITE"], counts["PRESENT-SAME"], counts["PRESENT-DIFFERS"], counts["OUT"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
