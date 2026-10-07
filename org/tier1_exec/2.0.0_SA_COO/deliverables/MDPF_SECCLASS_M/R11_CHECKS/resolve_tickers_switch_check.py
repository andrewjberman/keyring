#!/usr/bin/env python3
"""resolve_tickers_switch_check.py -- MDPF_SECCLASS round 9, cell SC-e-43 (FWD-5): the resolve_tickers gap record.

READ-ONLY against AWS (DynamoDB scans of bd-securities and etf-classifications, us-east-1; no S3, no write, no vendor call).
Writes ONE local file: org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/RESOLVE_TICKERS_GAP_<yyyymmdd>.md

  OLD-LIST-ROWS     bd-securities rows carrying the attribute (non-empty), ConsistentRead scan.
  CANONICAL         whether etf-classifications carries the attribute: rows carrying it, from a full scan (today: none).
  USED-BY           the resolve_tickers.py methods that read the attribute, path:line, found by reading the file.
  CANONICAL-FIRST-HITS  distinct held names (normalized) the new canonical_name method resolves from the canonical table's
                    `name`. Held names: the Holdings producer's own LOCAL build (no --upload, --as-of 2026-10-05; row W25-S1),
                    one parquet per firm under <held-root>/hb_<firm>/, SECURITY nodes, cash line excluded; claim `inferred`.
                    The hit count calls the module's own _resolve_canonical_name (yfinance stubbed on import: no vendor call).
"""
from __future__ import annotations

import argparse
import datetime
import importlib.util
import re
import sys
import types
from pathlib import Path

import boto3

ROOT = Path(__file__).resolve().parents[6]
OUT_DIR = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M"
SCRIPT_REL = "data/black_diamond/scripts/classification/resolve_tickers.py"
FIRMS = ("49financial", "cottonwood", "inflection")
ATTRS = ("asset_name_raw", "name_aliases")


def load_missing_list():
    spec = importlib.util.spec_from_file_location("missing_list", OUT_DIR / "R10_CHECKS" / "missing_list.py")
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def load_resolver():
    sys.modules.setdefault("yfinance", types.ModuleType("yfinance"))  # imported at module load; never called here
    sys.path.insert(0, str(ROOT / "data/black_diamond/scripts/classification"))
    import resolve_tickers  # noqa: WPS433
    return resolve_tickers


def scan(table, projection, names=None):
    d = boto3.client("dynamodb", region_name="us-east-1")
    kw = {"TableName": table, "ConsistentRead": True, "ProjectionExpression": projection}
    if names:
        kw["ExpressionAttributeNames"] = names
    rows = []
    for pg in d.get_paginator("scan").paginate(**kw):
        rows.extend(pg["Items"])
    return rows


def carries(item, attr):
    v = item.get(attr)
    if v is None:
        return False
    if "S" in v:
        return bool(v["S"].strip())
    if "L" in v:
        return len(v["L"]) > 0
    if "SS" in v:
        return len(v["SS"]) > 0
    return True


def used_by(attr):
    """Method names + line numbers in resolve_tickers.py that read `attr` (item.get('<attr>' ...))."""
    lines = (ROOT / SCRIPT_REL).read_text(encoding="utf-8").splitlines()
    cur, hits = None, []
    for i, ln in enumerate(lines, 1):
        m = re.match(r"def (_resolve_\w+|\w+)\(", ln)
        if m:
            cur = m.group(1)
        if re.search(r"item\.get\(\s*'" + attr + "'", ln) and cur and cur.startswith("_resolve_"):
            hits.append(f"{cur} ({SCRIPT_REL}:{i})")
    return hits


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--held-root", default=str(ROOT / ".scratch"))
    a = ap.parse_args()
    ml = load_missing_list()
    rt = load_resolver()

    old = scan("bd-securities", "ticker, asset_name_raw, name_aliases")
    canon_attrs = scan("etf-classifications", "ticker, asset_name_raw, name_aliases")
    canon_named = scan("etf-classifications", "ticker, #n", {"#n": "name"})
    canon_items = [{"ticker": i["ticker"]["S"], "name": i["name"]["S"]} for i in canon_named
                   if "name" in i and "S" in i["name"] and "ticker" in i and "S" in i["ticker"]]

    held_names = {}  # normalized name -> raw
    per_firm = {}
    for firm in FIRMS:
        held, files, cash = ml.held_securities(Path(a.held_root) / ("hb_" + firm))
        if held is None:
            raise SystemExit(f"ERROR: held parquet for {firm} absent or ambiguous ({files})")
        per_firm[firm] = len(held)
        for h in held.values():
            n = rt.normalize_asset_name(h["name"])
            if n:
                held_names.setdefault(n, h["name"])
    hits = rt._resolve_canonical_name(set(held_names), canon_items)

    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d")
    out = []
    out.append("# resolve_tickers.py -- canonical-first switch: the gap record (SC-e-43, FWD-5)\n")
    out.append(f"Read-only scans of bd-securities ({len(old):,} rows) and etf-classifications ({len(canon_attrs):,} rows), "
               f"ConsistentRead, {today}. Script: org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/"
               "resolve_tickers_switch_check.py.\n")
    for attr in ATTRS:
        n_old = sum(carries(i, attr) for i in old)
        n_can = sum(carries(i, attr) for i in canon_attrs)
        ub = used_by(attr)
        out.append(f"## ATTRIBUTE: {attr}\n")
        out.append(f"OLD-LIST-ROWS: {n_old}")
        out.append(f"CANONICAL: {'yes' if n_can else 'no'} -- etf-classifications rows carrying {attr}: {n_can} of {len(canon_attrs):,}")
        out.append("USED-BY: " + ("; ".join(ub) if ub else "none found"))
        out.append("")
    out.append("## CANONICAL-FIRST HITS\n")
    out.append(f"CANONICAL-FIRST-HITS: {len(hits)}")
    out.append("")
    out.append("Claim `inferred` (row W25-S1): held names are the SECURITY nodes' descriptions of the Holdings producer's own local "
               "build, --as-of 2026-10-05, no --upload (the served per-firm objects are unreadable from this device); "
               f"distinct normalized names {len(held_names):,} across {', '.join(f'{k} {v:,}' for k, v in per_firm.items())} "
               f"held securities. Canonical rows carrying `name`: {len(canon_items):,} of {len(canon_attrs):,}; rows keyed "
               "NAME:: or CUSIP: and names two rows map to different tickers are not resolved by the new method.")
    out.append("")
    path = OUT_DIR / f"RESOLVE_TICKERS_GAP_{today}.md"
    path.write_text("\n".join(out), encoding="utf-8")
    print(f"GAP-RECORD wrote={path.relative_to(ROOT)} canonical_first_hits={len(hits)} held_distinct_names={len(held_names)}")


if __name__ == "__main__":
    main()
