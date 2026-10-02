#!/usr/bin/env python3
"""holdings_publication_row_read.py -- legs S of the MDPF_SECCLASS row acts: does the served Holdings publication carry each
written row's class?

For every firm's newest served irpt-holdings publication (irpt/<firm>/platinum/holdings/current/manifest.json), every SECURITY
node whose display.symbol is one of a written set's tickers is compared with that ticker's live etf-classifications row
(asset_class, sub_asset_class). Read-only: S3 get-object and one paginated DynamoDB scan; nothing is written.

Sets (each a ledger's written tickers, derived from the commit or set file that wrote them, never typed here):
  cot-seed-19       ETF_CLASSIFICATIONS keys added by 15a9717715 (secclass-cot-seed-rows-m-20261001)
  cot-pattern-3     ETF_CLASSIFICATIONS keys added by 3e10c3d4e2 (secclass-cot-name-pattern-rows-m-20261002)
  bd-first-act-16   ETF_CLASSIFICATIONS keys added by 23c8e4c798 (secclass-bd-first-act-seed-m-20261002)
  bd-mapped-67      BD_MAPPED_WRITE_SET_20261002.tsv (secclass-bd-mapped-rows-m-20261002)

Run from the repo root: python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R8_CHECKS/holdings_publication_row_read.py
"""
from __future__ import annotations

import csv
import hashlib
import io
import json
import re
import subprocess
import sys
from collections import defaultdict
from pathlib import Path

import boto3
import pyarrow.parquet as pq
from botocore.config import Config
from botocore.exceptions import ConnectionClosedError, ReadTimeoutError, ResponseStreamingError

HERE = Path(__file__).resolve().parent
SEED = "infra/aws/lambda/v2_portal/_shared/etf_classification.py"
FIRMS = {"49financial": "opal-data-49financial", "inflection": "opal-data-inflection", "cottonwood": "opal-data-cottonwood"}
TABLE = "etf-classifications"
s3 = boto3.client("s3", region_name="us-east-1",
                  config=Config(read_timeout=300, connect_timeout=30, retries={"max_attempts": 8, "mode": "adaptive"}))


def added_seed_keys(commit: str) -> list:
    """Keys of ETF_CLASSIFICATIONS added by `commit`: added lines '"TICKER": "<class>",' -- only that dict's values are
    class names (the sub class, style and sector dicts carry other words)."""
    diff = subprocess.run(["git", "show", "--format=", "-U0", commit, "--", SEED], capture_output=True, text=True,
                          encoding="utf-8", check=True).stdout
    keys = []
    for line in diff.splitlines():
        m = re.match(r'''^\+\s*["']([A-Z0-9.\-]+)["']:\s*["']([a-z_]+)["']''', line)
        if m and m.group(2) in ("equity", "fixed_income", "alternatives", "commodities", "structured", "cash", "hedge"):
            keys.append(m.group(1))
    return sorted(set(keys))


def mapped_set() -> list:
    # '#' header lines, then rows: ticker, asset_class, sub_asset_class, name, bd-securities pair, disposition (no header row).
    with open(HERE.parent / "BD_MAPPED_WRITE_SET_20261002.tsv", encoding="utf-8", newline="") as f:
        return sorted({r[0] for r in csv.reader(f, delimiter="\t") if r and not r[0].startswith("#")})


def table_rows() -> dict:
    ddb = boto3.client("dynamodb", region_name="us-east-1")
    rows, kw = {}, {"TableName": TABLE, "ProjectionExpression": "ticker, asset_class, sub_asset_class"}
    while True:
        page = ddb.scan(**kw)
        for it in page["Items"]:
            rows[it["ticker"]["S"]] = (it.get("asset_class", {}).get("S"), it.get("sub_asset_class", {}).get("S"))
        if "LastEvaluatedKey" not in page:
            return rows
        kw["ExclusiveStartKey"] = page["LastEvaluatedKey"]


def get(bucket, key, ver=None):
    kw = {"Bucket": bucket, "Key": key}
    if ver:
        kw["VersionId"] = ver
    for attempt in range(10):   # a body-read timeout is not retried by botocore; retry the whole get
        try:
            return json.loads(s3.get_object(**kw)["Body"].read())
        except (ReadTimeoutError, ResponseStreamingError, ConnectionClosedError):
            if attempt == 9:
                raise
            print(f"  RETRY {attempt + 1} {key}", flush=True)
    raise AssertionError("unreachable")


def served(firm, bucket):
    cur = get(bucket, f"irpt/{firm}/platinum/holdings/current/manifest.json")
    date = cur["latest_date"]
    m = cur["dates"][date]["manifest"]
    man = get(bucket, m["key"], m["version_id"])
    # The manifest's gold parquet is the same revision's node set in ONE object (column node_json = the served node), so
    # one get per firm replaces hundreds of partition gets; its sha256 is checked against the manifest.
    g = man["gold"]
    for attempt in range(10):
        try:
            data = s3.get_object(Bucket=g["bucket"], Key=g["key"], VersionId=g["version_id"])["Body"].read()
            break
        except (ReadTimeoutError, ResponseStreamingError, ConnectionClosedError):
            if attempt == 9:
                raise
            print(f"  RETRY {attempt + 1} {g['key']}", flush=True)
    assert hashlib.sha256(data).hexdigest() == g["sha256"], "gold parquet sha256 differs from the manifest"
    nodes = [json.loads(s) for s in pq.read_table(io.BytesIO(data), columns=["node_json"]).column("node_json").to_pylist()]
    return date, man["revision"], man["clocks"]["as_of_timestamp"], nodes


def main() -> int:
    sets = {"cot-seed-19": added_seed_keys("15a9717715"), "cot-pattern-3": added_seed_keys("3e10c3d4e2"),
            "bd-first-act-16": added_seed_keys("23c8e4c798"), "bd-mapped-67": mapped_set()}
    for name, tickers in sets.items():
        print(f"SET {name}: {len(tickers)} tickers", flush=True)
    rows = table_rows()
    print(f"TABLE {TABLE}: {len(rows)} rows (one paginated scan)")
    want = {t for ts in sets.values() for t in ts}
    seen = defaultdict(list)   # ticker -> [(firm, served class, served sub, basis, value)]
    for firm, bucket in FIRMS.items():
        date, rev, as_of, nodes = served(firm, bucket)
        secs = [n for n in nodes if n.get("node_kind") == "SECURITY"]
        print(f"PUBLICATION {firm}: business_date {date} revision {rev[:12]} as_of {as_of} nodes {len(nodes)} securities {len(secs)}")
        for n in secs:
            sym = ((n.get("display") or {}).get("symbol") or "").upper()
            if sym in want:
                seen[sym].append((firm, n.get("asset_class"), n.get("sub_asset_class"), n.get("asset_class_basis"),
                                  n["amount"]["value"]))
    out = {}
    for name, tickers in sets.items():
        held = agree = disagree = 0
        detail = []
        for t in tickers:
            row = rows.get(t)
            by_firm = defaultdict(lambda: [0, 0.0, set()])
            for firm, cls, sub, basis, v in seen.get(t, []):
                by_firm[firm][0] += 1
                by_firm[firm][1] += v
                by_firm[firm][2].add((cls, sub, basis))
            if not by_firm:
                detail.append({"ticker": t, "row": row, "held": False})
                continue
            held += 1
            served_pairs = {(c, s) for f in by_firm.values() for c, s, _ in f[2]}
            ok = row is not None and served_pairs == {row}
            agree += ok
            disagree += not ok
            detail.append({"ticker": t, "row": row, "held": True, "agrees": ok,
                           "firms": {f: {"nodes": c, "value": round(v, 2), "served": sorted(map(list, s))}
                                     for f, (c, v, s) in sorted(by_firm.items())}})
        print(f"RESULT {name}: {len(tickers)} written, {held} held in a publication, {agree} served as the row, "
              f"{disagree} served otherwise, {len(tickers) - held} not held")
        for d in detail:
            if d["held"] and not d["agrees"]:
                print(f"  OTHERWISE {d['ticker']} row={d['row']} served={json.dumps(d['firms'])}")
        out[name] = detail
    dest = HERE / "HOLDINGS_PUBLICATION_ROW_READ_20261002.json"
    dest.write_text(json.dumps(out, indent=1, sort_keys=True, default=list), encoding="utf-8")
    print(f"WROTE {dest.relative_to(HERE.parents[4]) if len(HERE.parents) > 4 else dest}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
