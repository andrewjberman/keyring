#!/usr/bin/env python3
"""clean_name_row_set_v2.py -- MDPF_SECCLASS round 9, cell SC-e-48 (FWD-14, analysis ruling 2.2): the clean-name row set v2.

READ-ONLY. One consistent scan of DynamoDB etf-classifications plus the per-firm held sets, then writes
  org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_V2_20261007.tsv
tab-separated, header  key  classified_by  current_name  source_name  clean_name  action  source :
  - one line per row with a non-blank live `name`: source `table`, source_name empty, clean_name = clean_name(current_name),
    action UNCHANGED (equal) / SEED-SOURCE (a `seed` row) / WRITE;
  - one line per HELD key with no live name whose custody name is non-blank: source `custody:<firm>` (the first firm, in the
    order 49financial, cottonwood, inflection, that holds the key with a non-blank custody name), current_name empty,
    source_name = the custody name, clean_name = clean_name(source_name), action WRITE (SEED-SOURCE for a seed row).
    An AI-made row (classified_by `model`) is never in the custody group: FWD-11 names it.

Held set: `inferred`. The firm buckets deny this device's principal (row W25-S1), so the held set is the Holdings producer's own
per-firm build (data/assets/scripts/gold/investor_reporting/holdings_snapshot.py, run WITHOUT --upload, --as-of 2026-10-05), one
parquet per firm under <held-root>/hb_<firm>/ (built by R10_CHECKS/old_list_census.py build_firm; reused here if present, built
here with --build). Custody security name = the SECURITY node's display.description (display.label is "<SYMBOL> -- <description>",
so it is not a name). A held security reaches the table by the producer's own lookups: its symbol, "CUSIP:"+cusip, or its
identity key; every one of those keys that exists in the table with no name receives the custody name.
  python .../clean_name_row_set_v2.py [--build] [--held-root DIR]
"""
from __future__ import annotations

import argparse
import collections
import csv
import glob
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[6]
sys.path.insert(0, str(ROOT / "infra" / "aws" / "lambda" / "v2_portal" / "_shared"))
sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "R10_CHECKS"))
OUT = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/CLEAN_NAME_ROW_SET_V2_20261007.tsv"
COLS = ["key", "classified_by", "current_name", "source_name", "clean_name", "action", "source"]
FIRMS = ("49financial", "cottonwood", "inflection")
TABLE = "etf-classifications"


def slug(name):
    n = "".join(c if c.isalnum() or c == "-" else " " for c in str(name).upper())
    return " ".join(n.split())[:80]


def scan():
    import boto3
    d = boto3.client("dynamodb", region_name="us-east-1")
    out = {}
    for pg in d.get_paginator("scan").paginate(TableName=TABLE, ConsistentRead=True, ProjectionExpression="ticker,#n,classified_by",
                                               ExpressionAttributeNames={"#n": "name"}):
        for it in pg["Items"]:
            out[it["ticker"]["S"]] = ((it.get("name") or {}).get("S") or "", (it.get("classified_by") or {}).get("S") or "")
    return out


def held(root):
    """identity key -> {"keys": table keys it can reach, "name": custody name} over the build's SECURITY nodes, cash excluded."""
    import pyarrow.parquet as pq
    files = glob.glob(str(Path(root) / "**" / "*.parquet"), recursive=True)
    if len(files) != 1:
        return None, files, 0
    nodes = [json.loads(s) for s in pq.read_table(files[0], columns=["node_json"]).column("node_json").to_pylist()]
    acc, cash = {}, 0
    for n in nodes:
        if n.get("node_kind") != "SECURITY":
            continue
        disp = n.get("display") or {}
        desc = " ".join(str(disp.get("description") or "").split())
        sym = str(disp.get("symbol") or "").strip().upper()
        if sym == "CASH" and desc.upper() == "CASH":
            cash += 1
            continue
        sym = sym if sym and sym not in ("NONE", "NAN") else ""
        sid = n.get("security_id") or {}
        cusip = str(sid.get("value") or "").strip().upper() if sid.get("namespace") == "CUSIP" else ""
        ident = sym or ("CUSIP:" + cusip if cusip else ("NAME::" + slug(desc) if slug(desc) else ""))
        if not ident:
            continue
        h = acc.setdefault(ident, {"keys": set(), "names": collections.Counter()})
        h["keys"].update(k for k in (sym, "CUSIP:" + cusip if cusip else "", ident) if k)
        if desc:
            h["names"][desc] += 1
    for h in acc.values():
        # the most common non-blank description; ties broken by the string, so the choice is deterministic
        h["name"] = sorted(h["names"].items(), key=lambda kv: (-kv[1], kv[0]))[0][0] if h["names"] else ""
    return acc, files, cash


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true")
    ap.add_argument("--held-root", default=str(ROOT / ".scratch"))
    a = ap.parse_args()
    from security_name import clean_name
    live = scan()
    rows, bad = [], []
    for key in sorted(live):
        name, by = live[key]
        if not name.strip():
            continue
        if any(c in name for c in "\t\n\r"):
            bad.append(key)
        clean = clean_name(name)
        rows.append([key, by, name, "", clean, "UNCHANGED" if clean == name else ("SEED-SOURCE" if by == "seed" else "WRITE"), "table"])
    named = len(rows)
    custody, per_firm, conflicts = {}, {}, 0
    for firm in FIRMS:
        root = Path(a.held_root) / ("hb_" + firm)
        acc, files, cash = held(root)
        if acc is None and a.build and not files:
            from old_list_census import build_firm
            build_firm(firm, root)
            acc, files, cash = held(root)
        if acc is None:
            raise SystemExit(f"ERROR: held parquet for {firm} not found or ambiguous ({files}); run with --build")
        reached = 0
        for ident, h in sorted(acc.items()):
            for k in sorted(h["keys"]):
                if k not in live or live[k][0].strip() or live[k][1] == "model" or not h["name"]:
                    continue
                if k in custody:
                    conflicts += custody[k][0] != h["name"]
                    continue
                custody[k] = (h["name"], firm)
                reached += 1
        per_firm[firm] = {"held": len(acc), "cash_lines": cash, "keys_taken": reached, "parquet": str(Path(files[0]).name)}
    for k in sorted(custody):
        sname, firm = custody[k]
        if any(c in sname for c in "\t\n\r"):
            bad.append(k)
        by = live[k][1]
        rows.append([k, by, "", sname, clean_name(sname), "SEED-SOURCE" if by == "seed" else "WRITE", "custody:" + firm])
    if bad:
        print("REFUSED: a name holds a tab or newline (set would be ambiguous): " + ",".join(bad[:10]))
        return 1
    with OUT.open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n", quoting=csv.QUOTE_NONE, quotechar=None, escapechar=None)
        w.writerow(COLS)
        w.writerows(rows)
    c = collections.Counter((r[6].split(":")[0], r[5]) for r in rows)
    head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], capture_output=True, text=True, check=False).stdout.strip()
    print(f"CLEAN-NAME-ROW-SET-V2 rows_scanned={len(live)} named={named} unnamed={len(live) - named} lines={len(rows)} "
          f"custody={len(custody)} cross_firm_name_conflicts={conflicts} head={head}")
    for (src, act), n in sorted(c.items()):
        print(f"  source={src} action={act} n={n}")
    for f, d in per_firm.items():
        print(f"  firm {f} {d}")
    print("wrote", OUT.name)
    return 0


if __name__ == "__main__":
    sys.exit(main())
