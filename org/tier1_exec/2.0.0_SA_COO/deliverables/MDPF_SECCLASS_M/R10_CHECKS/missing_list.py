#!/usr/bin/env python3
"""missing_list.py -- MDPF_SECCLASS round 8, cell SC-e-33 (FWD-15): the missing list on demand.

For each of 49financial, cottonwood, inflection: the held securities with no entry in the shared list
(DynamoDB etf-classifications, us-east-1) and their total. READ-ONLY against AWS (BatchGetItem, ConsistentRead).
Writes exactly three local files:
  org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/MISSING_LIST_<firm>_<yyyymmdd>.json   (today's UTC date)
  {"firm", "as_of", "source", "held_count", "missing": [{"key", "name", "cusip" (when known), "amount" (when served)}], "total"}

Held set (AMENDMENT 1 of the task order): the per-firm firm buckets deny this device's principal, so the held set is the Holdings
producer's own build (data/assets/scripts/gold/investor_reporting/holdings_snapshot.py, run WITHOUT --upload, --as-of AS_OF),
one parquet per firm under <held-root>/hb_<firm>/. The source string says so and the claim is `inferred`. If a firm's parquet is
absent, `--build` runs the producer for it (about 4-15 minutes each; not part of the 120 s pull).

Definitions
  held         distinct SECURITY nodes of the build, by identity key = display.symbol (upper, not NONE/NAN), else
               "CUSIP:"+security_id.value when its namespace is CUSIP, else "NAME::"+slug(display.description).
  excluded     the producer's own cash line (classify_security: ticker CASH and description CASH): never a security,
               never counted in held_count. Non-SECURITY nodes (ACCOUNT, CATEGORY, MODEL_LEAF) are not held securities.
  no entry     the producer's lookup is canonical_lookup(display.symbol) -> etf-classifications get_item(ticker=<SYMBOL>)
               (holdings_snapshot.py _NarrowedClassifier.canonical_lookup ~line 880). The task order adds the CUSIP key: a
               security is missing when NEITHER its symbol key NOR "CUSIP:"+cusip exists in the table (its own identity key is
               read as well, so the list can never name a key the table holds).
  amount       sum of the SECURITY nodes' amount.value (USD) for the identity, when served.
"""
from __future__ import annotations

import argparse
import datetime
import glob
import json
import subprocess
import sys
from pathlib import Path

import boto3

ROOT = Path(__file__).resolve().parents[6]
OUT_DIR = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M"
PRODUCER_DIR = ROOT / "data/assets/scripts/gold/investor_reporting"
FIRMS = ("49financial", "cottonwood", "inflection")
AS_OF = "2026-10-05"
TABLE = "etf-classifications"


def slug(name):
    n = "".join(c if c.isalnum() or c == "-" else " " for c in str(name).upper())
    return " ".join(n.split())[:80]


def present(client, keys):
    found = set()
    keys = list(dict.fromkeys(keys))
    for i in range(0, len(keys), 100):
        req = {TABLE: {"Keys": [{"ticker": {"S": k}} for k in keys[i:i + 100]], "ConsistentRead": True,
                       "ProjectionExpression": "ticker"}}
        while req:
            resp = client.batch_get_item(RequestItems=req)
            for it in resp.get("Responses", {}).get(TABLE, []):
                found.add(it["ticker"]["S"])
            req = resp.get("UnprocessedKeys") or None
    return found


def build_firm(firm, root):
    out = Path(root)
    out.mkdir(parents=True, exist_ok=True)
    cmd = [sys.executable, "holdings_snapshot.py", "--firms", firm, "--as-of", AS_OF, "--local-out", str(out)]
    run = subprocess.run(cmd, cwd=str(PRODUCER_DIR), capture_output=True, text=True, timeout=3000, check=False)
    if run.returncode != 0:
        raise SystemExit(f"ERROR: producer build for {firm} rc={run.returncode}: {run.stderr.strip()[-400:]}")


def held_securities(root):
    """identity key -> {"name", "symbol", "cusip", "amount", "nodes"} over the build's SECURITY nodes, cash line excluded."""
    import pyarrow.parquet as pq
    files = glob.glob(str(Path(root) / "**" / "*.parquet"), recursive=True)
    if len(files) != 1:
        return None, files, 0
    nodes = [json.loads(s) for s in pq.read_table(files[0], columns=["node_json"]).column("node_json").to_pylist()]
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
        cusip = str(sid.get("value") or "").strip().upper() if sid.get("namespace") == "CUSIP" else ""
        name = desc or str(disp.get("label") or "")
        ident = sym or ("CUSIP:" + cusip if cusip else ("NAME::" + slug(name) if slug(name) else ""))
        if not ident:
            continue
        h = held.setdefault(ident, {"name": name, "symbol": sym, "cusip": cusip, "amount": None, "nodes": 0})
        h["nodes"] += 1
        val = (n.get("amount") or {}).get("value")
        if isinstance(val, (int, float)):
            h["amount"] = round((h["amount"] or 0.0) + float(val), 2)
        if not h["cusip"] and cusip:
            h["cusip"] = cusip
    return held, files, cash


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--build", action="store_true", help="run the producer for any firm whose held parquet is absent")
    ap.add_argument("--held-root", default=str(ROOT / ".scratch"))
    a = ap.parse_args()
    head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                          check=False).stdout.strip()
    today = datetime.datetime.now(datetime.timezone.utc).strftime("%Y%m%d")
    client = boto3.client("dynamodb", region_name="us-east-1")
    total_all = 0
    for firm in FIRMS:
        root = Path(a.held_root) / ("hb_" + firm)
        held, files, cash = held_securities(root)
        if held is None and a.build and not files:
            build_firm(firm, root)
            held, files, cash = held_securities(root)
        if held is None:
            raise SystemExit(f"ERROR: held parquet for {firm} not found or ambiguous ({files}); run with --build")
        lookup = []
        for ident, h in held.items():
            lookup += [k for k in (h["symbol"], "CUSIP:" + h["cusip"] if h["cusip"] else "", ident) if k]
        hit = present(client, lookup)
        missing = []
        for ident, h in sorted(held.items()):
            if any(k in hit for k in (h["symbol"], "CUSIP:" + h["cusip"] if h["cusip"] else "", ident) if k):
                continue
            row = {"key": ident, "name": h["name"]}
            if h["cusip"]:
                row["cusip"] = h["cusip"]
            if h["amount"] is not None:
                row["amount"] = h["amount"]
            missing.append(row)
        amount = round(sum(m.get("amount", 0.0) for m in missing), 2)
        doc = {
            "firm": firm, "as_of": AS_OF,
            "source": f"local producer build as-of {AS_OF} @{head}, inferred (not the served bytes)",
            "claim": "inferred",
            "source_detail": ("holdings_snapshot.py run without --upload for this firm only; parquet "
                              + (str(Path(files[0]).relative_to(ROOT)) if str(files[0]).startswith(str(ROOT)) else str(files[0]))
                              + "; served opal-data-<firm> bucket not readable by this device's principal"),
            "excluded": f"{cash} cash-line SECURITY node(s) (ticker CASH, description CASH) and all non-SECURITY nodes",
            "held_count": len(held), "missing_amount_usd": amount,
            "missing": missing, "total": len(missing),
        }
        assert doc["total"] == len(doc["missing"])
        path = OUT_DIR / f"MISSING_LIST_{firm}_{today}.json"
        path.write_text(json.dumps(doc, indent=1), encoding="utf-8")
        total_all += len(missing)
        print(f"FIRM {firm} held={len(held)} missing={len(missing)} amount_usd={amount} wrote={path.relative_to(ROOT)}",
              flush=True)
    print(f"MISSING-LIST-PULL firms=3 total={total_all}")


if __name__ == "__main__":
    main()
