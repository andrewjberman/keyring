#!/usr/bin/env python3
"""holdings_cusip_newly_placed.py -- MDPF_SECCLASS round 9, cell SC-e-56 (S27, folds R8 SC-e-39): the securities the Holdings
producer newly places by its CUSIP fallback, listed BEFORE the change ships.

READ-ONLY against AWS (BatchGetItem, ConsistentRead, DynamoDB etf-classifications us-east-1). Writes one local file:
  org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/HOLDINGS_CUSIP_NEWLY_PLACED_<yyyymmdd>.json (today's UTC date)
  {"source", "claim": "inferred", "as_of", "firms": {<firm>: [{"symbol", "cusip", "market_value", "name",
   "cusip_row_asset_class", "cusip_row_sub_asset_class"}, ..]}, "by_firm": {<firm>: {...}}}

Held set: the firm buckets deny some devices' principals, so the held set is the Holdings producer's own LOCAL build
(holdings_snapshot.py run WITHOUT --upload, one parquet per firm under <held-root>/hb_<firm>/), the latest built date per firm. The
claim is `inferred`: a local build, not the served bytes. `--build` runs the producer for a firm whose parquet is absent.

NEWLY PLACED = a distinct SECURITY node (cash line excluded) whose producer lookup key (display.symbol, upper-cased, not NONE/NAN)
is ABSENT from the table or empty, whose security_id namespace is CUSIP, and whose `CUSIP:<value>` key is PRESENT: exactly the
symbol misses the CUSIP key answers. A security whose symbol is held is never listed (the producer never asks its CUSIP).
market_value = the sum of its SECURITY nodes' amount.value (USD).
"""
from __future__ import annotations

import argparse
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
FIRMS = ("49financial", "cottonwood", "inflection")
TABLE = "etf-classifications"


def latest_parquet(root):
    """(path, date) of the newest date=YYYY-MM-DD partition's parquet under root, else (None, None)."""
    best = None
    for f in glob.glob(str(Path(root) / "**" / "*.parquet"), recursive=True):
        m = re.search(r"date=(\d{4}-\d{2}-\d{2})", f.replace("\\", "/"))
        if m and (best is None or m.group(1) > best[1]):
            best = (f, m.group(1))
    return best if best else (None, None)


def build_firm(firm, root, as_of):
    out = Path(root)
    out.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, "holdings_snapshot.py", "--firms", firm, "--as-of", as_of, "--local-out", str(out)]
    run = subprocess.run(cmd, cwd=str(PRODUCER_DIR), capture_output=True, text=True, timeout=3000, check=False)
    if run.returncode != 0:
        raise SystemExit(f"ERROR: producer build for {firm} rc={run.returncode}: {run.stderr.strip()[-400:]}")


def held_securities(path):
    """list of {"symbol", "cusip", "name", "amount", "nodes"} over the build's SECURITY nodes, cash line excluded."""
    import pyarrow.parquet as pq
    nodes = [json.loads(s) for s in pq.read_table(path, columns=["node_json"]).column("node_json").to_pylist()]
    held, cash = {}, 0
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
        cusip = str(sid.get("value") or "").strip().upper() if str(sid.get("namespace") or "").upper() == "CUSIP" else ""
        name = desc or str(disp.get("label") or "")
        ident = sym or ("CUSIP:" + cusip if cusip else "NAME::" + " ".join(name.upper().split())[:80])
        h = held.setdefault((sym, cusip, ident), {"symbol": sym, "cusip": cusip, "name": name, "amount": 0.0, "nodes": 0})
        h["nodes"] += 1
        val = (n.get("amount") or {}).get("value")
        if isinstance(val, (int, float)):
            h["amount"] = round(h["amount"] + float(val), 2)
    return list(held.values()), cash


def get_rows(client, keys):
    """key -> item (ticker, asset_class, sub_asset_class) for each key the table holds; consistent batch reads."""
    found = {}
    keys = list(dict.fromkeys(k for k in keys if k))
    for i in range(0, len(keys), 100):
        req = {TABLE: {"Keys": [{"ticker": {"S": k}} for k in keys[i:i + 100]], "ConsistentRead": True,
                       "ProjectionExpression": "ticker, asset_class, sub_asset_class"}}
        while req:
            resp = client.batch_get_item(RequestItems=req)
            for it in resp.get("Responses", {}).get(TABLE, []):
                found[it["ticker"]["S"]] = it
            req = resp.get("UnprocessedKeys") or None
    return found


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true", help="run the producer for any firm whose held parquet is absent")
    ap.add_argument("--as-of", default="2026-10-05", help="build date used with --build")
    ap.add_argument("--held-root", default=str(ROOT / ".scratch"))
    a = ap.parse_args()
    head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                          check=False).stdout.strip()
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d")
    client = boto3.client("dynamodb", region_name="us-east-1")
    firms, by_firm, as_ofs, files_used = {}, {}, {}, {}
    for firm in FIRMS:
        root = Path(a.held_root) / ("hb_" + firm)
        path, date = latest_parquet(root)
        if path is None and a.build:
            build_firm(firm, root, a.as_of)
            path, date = latest_parquet(root)
        if path is None:
            raise SystemExit(f"ERROR: held parquet for {firm} not found under {root}; run with --build")
        held, cash = held_securities(path)
        rows = get_rows(client, [h["symbol"] for h in held] + ["CUSIP:" + h["cusip"] for h in held if h["cusip"]])
        listed = []
        for h in sorted(held, key=lambda x: (x["symbol"], x["cusip"])):
            if h["symbol"] in rows or not h["cusip"]:
                continue
            row = rows.get("CUSIP:" + h["cusip"])
            if row is None:
                continue
            listed.append({"symbol": h["symbol"], "cusip": h["cusip"], "market_value": h["amount"], "name": h["name"],
                           "cusip_row_asset_class": row.get("asset_class", {}).get("S"),
                           "cusip_row_sub_asset_class": row.get("sub_asset_class", {}).get("S")})
        firms[firm] = listed
        as_ofs[firm] = date
        files_used[firm] = str(Path(path).relative_to(ROOT)) if str(path).startswith(str(ROOT)) else str(path)
        by_class = {}
        for e in listed:
            c = e["cusip_row_asset_class"] or "none"
            by_class[c] = round(by_class.get(c, 0.0) + e["market_value"], 2)
        by_firm[firm] = {"held_securities": len(held), "cash_lines_excluded": cash, "newly_placed": len(listed),
                         "newly_placed_usd": round(sum(e["market_value"] for e in listed), 2),
                         "newly_placed_usd_by_cusip_row_class": by_class, "as_of": date}
        print(f"FIRM {firm} as_of={date} held={len(held)} newly_placed={len(listed)} "
              f"usd={by_firm[firm]['newly_placed_usd']}", flush=True)
    doc = {"source": f"local producer builds (holdings_snapshot.py without --upload), latest built date per firm, read at @{head}; "
                     "DynamoDB etf-classifications consistent reads; inferred (not the served bytes)",
           "claim": "inferred", "as_of": as_ofs, "held_files": files_used, "firms": firms, "by_firm": by_firm,
           "total_newly_placed": sum(len(v) for v in firms.values())}
    path = OUT_DIR / f"HOLDINGS_CUSIP_NEWLY_PLACED_{today}.json"
    path.write_text(json.dumps(doc, indent=1), encoding="utf-8")
    print(f"HOLDINGS-CUSIP-NEWLY firms=3 total={doc['total_newly_placed']} wrote={path.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
