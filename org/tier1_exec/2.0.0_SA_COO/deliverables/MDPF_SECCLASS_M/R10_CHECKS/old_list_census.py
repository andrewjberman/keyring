#!/usr/bin/env python3
"""old_list_census.py -- MDPF_SECCLASS round 8, cell SC-e-26 (FWD-17, FWD-15): the old Black Diamond list measured.

READ-ONLY against AWS (DynamoDB scans, consistent reads; S3 reads only through the producer below). Writes one local file:
org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/OLD_LIST_CENSUS_<YYYYMMDD>.json (UTC run date).

Reads
  old list     DynamoDB bd-securities (us-east-1), full paginated consistent scan -> denominator N.
  shared list  DynamoDB etf-classifications, full paginated consistent scan.
  held today   the Holdings producer's own per-firm build (data/assets/scripts/gold/investor_reporting/holdings_snapshot.py,
               run WITHOUT --upload, so nothing is published), one parquet per firm under <held-root>/hb_<firm>/ ; with --build the
               missing firms are built here (about 4-15 minutes each). Why a local build and not the served platinum object: the
               per-firm served buckets (opal-data-<firm>) answer AccessDenied (explicit resource-policy deny) to this device's
               agent identity; the producer reads the same upstream sources the scheduled fire reads and the file below names
               the as-of date and the producer's git HEAD, so the claim is `inferred` (same code, same sources, not the served bytes).

Rules stated (the issuer's check reads the shape; these are the definitions)
  key form     "NAME::" prefix | "CUSIP:" prefix | "ticker" = fullmatch [A-Z0-9]{1,6}([.-][A-Z0-9]{1,4})? | none_or_other = the rest.
  in_both      the old key K is in etf-classifications as K, or as "CUSIP:"+K when K is 9 alphanumerics (a bare CUSIP key).
  held         the old key equals a held SECURITY node's identity key: display.symbol (upper, not NONE/NAN), "CUSIP:"+security_id
               (namespace CUSIP), or "NAME::"+slug(display.description) with slug = upper, [^A-Z0-9-] -> space, collapse, 80 chars
               (the bd-securities writer's own rule, classify_bd_securities.normalize_key).
  partition    in_both_lists = in shared; held_today_not_in_shared = held and not in shared; rest = everything else. a+b+c == N.

Usage (repo root):  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R10_CHECKS/old_list_census.py [--build] [--held-root DIR]
"""
from __future__ import annotations

import argparse
import collections
import datetime
import glob
import json
import re
import subprocess
import sys
from pathlib import Path

import boto3

ROOT = Path(__file__).resolve().parents[6]
OUT_DIR = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M"
PRODUCER_DIR = ROOT / "data/assets/scripts/gold/investor_reporting"
FIRMS = ("cottonwood", "inflection", "49financial")
AS_OF = "2026-10-05"  # the issuer's held read used each firm's build of this date
TICKER_RE = re.compile(r"[A-Z0-9]{1,6}([.\-][A-Z0-9]{1,4})?")
CUSIP_RE = re.compile(r"[A-Z0-9]{9}")


def scan_keys(client, table):
    keys = []
    for page in client.get_paginator("scan").paginate(TableName=table, ConsistentRead=True, ProjectionExpression="#t",
                                                      ExpressionAttributeNames={"#t": "ticker"}):
        keys += [i["ticker"]["S"] for i in page["Items"]]
    assert len(keys) == len(set(keys)), f"duplicate hash keys in {table}"
    return keys


def key_form(k):
    if k.startswith("NAME::"):
        return "NAME::"
    if k.startswith("CUSIP:"):
        return "CUSIP:"
    if TICKER_RE.fullmatch(k):
        return "ticker"
    return "none_or_other"


def slug(name):
    n = "".join(c if c.isalnum() or c == "-" else " " for c in str(name).upper())
    return " ".join(n.split())[:80]


def in_shared(k, shared):
    return k in shared or (CUSIP_RE.fullmatch(k) is not None and "CUSIP:" + k in shared)


def build_firm(firm, root):
    out = Path(root)
    out.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, "holdings_snapshot.py", "--firms", firm, "--as-of", AS_OF, "--local-out", str(out)]
    run = subprocess.run(cmd, cwd=str(PRODUCER_DIR), capture_output=True, text=True, timeout=3000, check=False)
    if run.returncode != 0:
        raise SystemExit(f"ERROR: producer build for {firm} rc={run.returncode}: {run.stderr.strip()[-400:]}")


def held_nodes(firm, root):
    import pyarrow.parquet as pq
    files = glob.glob(str(Path(root) / "**" / "*.parquet"), recursive=True)
    if len(files) != 1:
        return None, files
    nodes = [json.loads(s) for s in pq.read_table(files[0], columns=["node_json"]).column("node_json").to_pylist()]
    return [n for n in nodes if n.get("node_kind") == "SECURITY"], files


def identity_keys(node):
    """(identity key, every key the node can be matched on)."""
    disp = node.get("display") or {}
    sym = str(disp.get("symbol") or "").strip().upper()
    sym = sym if sym and sym not in ("NONE", "NAN") else ""
    sid = node.get("security_id") or {}
    cusip = str(sid.get("value") or "").strip().upper() if sid.get("namespace") == "CUSIP" else ""
    name = slug(disp.get("description") or disp.get("label") or "")
    keys = set()
    if sym:
        keys.add(sym)
    if cusip:
        keys.add("CUSIP:" + cusip)
    if name:
        keys.add("NAME::" + name)
    ident = sym or ("CUSIP:" + cusip if cusip else ("NAME::" + name if name else ""))
    return ident, keys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true", help="build any firm whose held parquet is absent")
    ap.add_argument("--held-root", default=str(ROOT / ".scratch"))
    a = ap.parse_args()
    root_for = {f: Path(a.held_root) / ("hb_" + f) for f in FIRMS}

    ddb = boto3.client("dynamodb", region_name="us-east-1")
    old = scan_keys(ddb, "bd-securities")
    shared = set(scan_keys(ddb, "etf-classifications"))
    n = len(old)
    print(f"DENOMINATOR old={n} shared={len(shared)}", flush=True)

    held_ident = collections.defaultdict(set)   # identity key -> firms
    held_match = collections.defaultdict(set)   # any matchable key -> firms
    per_firm, dates = {}, {}
    for f in FIRMS:
        nodes, files = held_nodes(f, root_for[f])
        if nodes is None and a.build and not files:
            build_firm(f, root_for[f])
            nodes, files = held_nodes(f, root_for[f])
        if nodes is None:
            raise SystemExit(f"ERROR: held parquet for {f} not found or ambiguous ({files}); run with --build")
        idents = set()
        for nd in nodes:
            ident, keys = identity_keys(nd)
            if ident:
                idents.add(ident)
                held_ident[ident].add(f)
            for k in keys:
                held_match[k].add(f)
            dates[f] = (nd.get("clocks") or {}).get("custody_as_of", dates.get(f))
        per_firm[f] = {"security_nodes": len(nodes), "distinct_securities": len(idents),
                       "in_shared": sum(1 for i in idents if in_shared(i, shared)),
                       "not_in_shared": sum(1 for i in idents if not in_shared(i, shared)),
                       "custody_as_of": dates.get(f), "parquet": str(Path(files[0]).relative_to(ROOT)) if str(files[0]).startswith(str(ROOT)) else files[0]}

    by_mem = collections.Counter()
    by_form = collections.Counter()
    cross = collections.defaultdict(collections.Counter)
    examples = collections.defaultdict(list)
    held_old_rows = 0
    for k in old:
        form = key_form(k)
        both = in_shared(k, shared)
        held = k in held_match
        held_old_rows += held
        mem = "in_both_lists" if both else ("held_today_not_in_shared" if held else "rest")
        by_mem[mem] += 1
        by_form[form] += 1
        cross[mem][form] += 1
        if len(examples[mem + "|" + form]) < 5:
            examples[mem + "|" + form].append(k)
    held_in_both = sum(1 for k in old if in_shared(k, shared) and k in held_match)

    # FWD-15: held securities (the three firms' served builds) with no shared entry, and whether the old list has a row for them
    old_set = set(old)
    held_not_shared = sorted(i for i in held_ident if not in_shared(i, shared))
    held_not_shared_no_old = [i for i in held_not_shared if i not in old_set]

    head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], capture_output=True, text=True, check=False).stdout.strip()
    clocks = ", ".join(f"{f}={dates.get(f)}" for f in FIRMS)
    held_source = ("local run of the Holdings producer (data/assets/scripts/gold/investor_reporting/holdings_snapshot.py at repo HEAD "
                   f"{head}, no --upload) for cottonwood, inflection, 49financial with --as-of {AS_OF}; custody_as_of {clocks}. "
                   "NOT the served platinum object: opal-data-<firm> answers AccessDenied (explicit resource-policy deny) to this "
                   "device's agent identity. Claim: inferred (same code and upstream sources as the scheduled fire, not the served bytes).")
    now = datetime.datetime.now(datetime.timezone.utc)
    doc = {
        "scanned_at": now.isoformat(), "table": "bd-securities", "denominator": n,
        "by_membership": {k: by_mem.get(k, 0) for k in ("in_both_lists", "held_today_not_in_shared", "rest")},
        "by_key_form": {k: by_form.get(k, 0) for k in ("ticker", "CUSIP:", "NAME::", "none_or_other")},
        "held_source": held_source, "held_claim": "inferred",
        "held_in_both": held_in_both, "old_rows_held_today": held_old_rows,
        "match_rules": {"in_both_lists": "old key K in etf-classifications as K, or as CUSIP:K when K is 9 alphanumerics",
                        "held": "old key equals a held SECURITY node's symbol, CUSIP:<cusip>, or NAME::<80-char slug of its description>",
                        "ticker_form": TICKER_RE.pattern},
        "shared_rows": len(shared),
        "cross": {m: dict(c) for m, c in cross.items()},
        "held_by_firm": per_firm,
        "held_securities_distinct_across_firms": len(held_ident),
        "held_securities_not_in_shared": len(held_not_shared),
        "held_not_in_shared_with_no_old_row": len(held_not_shared_no_old),
        "examples": dict(examples),
        "held_not_in_shared_keys": held_not_shared,
    }
    path = OUT_DIR / f"OLD_LIST_CENSUS_{now.strftime('%Y%m%d')}.json"
    path.write_text(json.dumps(doc, indent=1, sort_keys=True), encoding="utf-8")
    print("WROTE", path.relative_to(ROOT))
    print("by_membership", doc["by_membership"], "sum", sum(doc["by_membership"].values()))
    print("by_key_form", doc["by_key_form"], "sum", sum(doc["by_key_form"].values()))
    print(f"held distinct {len(held_ident)}; not in shared {len(held_not_shared)}; of those no old row {len(held_not_shared_no_old)}")


if __name__ == "__main__":
    main()
