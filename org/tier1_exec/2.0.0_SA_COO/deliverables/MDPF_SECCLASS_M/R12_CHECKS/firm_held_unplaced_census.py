#!/usr/bin/env python3
"""firm_held_unplaced_census.py -- MDPF_SECCLASS round 12, cell SC-e-70 (AMENDMENT 1): READ-ONLY census of EVERY firm-held key
absent from etf-classifications (FWD-15's domain per the CTO ruling, commit ddd3eaac69).

READ-ONLY against AWS: S3 list/get on the firm's own bucket, DynamoDB consistent paginated scans of etf-classifications (the
absence test and the table vocabulary) and bd-securities (the direct-match plan's input, as in R11_CHECKS/fwd15_ai_plan.py).
No write, no model call, no invoke.

1. Held set, per firm, from the newest SERVED holdings snapshot in that firm's own bucket:
     49financial -> opal-data-49financial   irpt/49financial/gold/holdings/date=*/<hash>.parquet
     inflection  -> opal-data-inflection    irpt/inflection/gold/holdings/date=*/<hash>.parquet
     cottonwood  -> opal-data-cottonwood    irpt/cottonwood/gold/holdings/date=*/<hash>.parquet
   (the task order names opal-data-cot for cottonwood; that bucket carries no irpt/ holdings snapshot and an empty
   gold/holdings_lots/ -- the probe is printed into the output JSON; the served snapshot is the cottonwood-named bucket).
   Newest = greatest date partition, then greatest LastModified. Bucket, key, VersionId, LastModified, ETag are recorded.
   Held identity = the rule of R10_CHECKS/missing_list.py held_securities(): distinct SECURITY nodes, identity key =
   display.symbol (upper, not NONE/NAN), else CUSIP:<value> when the namespace is CUSIP, else NAME::<slug(description)>;
   the producer's own cash line (symbol CASH and description CASH) is excluded. amount = sum of the SECURITY nodes'
   amount.value across both bases (as missing_list did, so the numbers compare with the first census);
   amount_observed_usd = the OBSERVED-basis nodes only, recorded beside it.
2. Absent set: a held identity is PRESENT when any of its candidate keys is a `ticker` of an etf-classifications row:
   the symbol, the identity key, CUSIP:<cusip>, BLOOMBERG:<id> (security_id namespace BLOOMBERG), NAME::<slug(description)>,
   and the plan's derived shared key. Otherwise ABSENT.
3. Route of each ABSENT key: the rule of R11_CHECKS/fwd15_ai_plan.py, imported (derive_shared_key, load_runner, the
   classify_asset_class direct-match plan, the six classes and the contract's closed sub-class list): UNPLACED-KEY when no
   declared key form fits, DIRECT when the direct-match plan places it inside the contract, else AI.
4. Writes ../FIRM_HELD_UNPLACED_CENSUS_20261008.json.
5. Control: each of the 99 entries of ../UNPLACED_KEY_CENSUS_20261008.json (its source plan files) that is still held (identity in
   this run's held set) and still absent (the four match forms tested from the plan entry's own key, cusip and name, not through
   the widened set) must appear in the widened absent set. An entry now matched by a table row (e.g. a NAME:: row written after
   the plan) is PRESENT, not absent; the JSON counts those by the first form that matched.

Prints  FIRM-HELD-CENSUS ok=<bool> firms=<n> held=<per-firm n> absent=<per-firm n> usd=<per-firm sum>
        e70_still_absent=<n> missing_from_widened=<n>
Usage (repo root):  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R12_CHECKS/firm_held_unplaced_census.py
"""
from __future__ import annotations

import collections
import datetime
import importlib.util
import io
import json
import re
import sys
from pathlib import Path

import boto3

HERE = Path(__file__).resolve().parent
M = HERE.parent
PLAN_MODULE = M / "R11_CHECKS" / "fwd15_ai_plan.py"
PLAN_FILES = HERE / "e49_replan"
FIRST_CENSUS = M / "UNPLACED_KEY_CENSUS_20261008.json"
OUT = M / "FIRM_HELD_UNPLACED_CENSUS_20261008.json"
REGION = "us-east-1"
# firm -> (the served-holdings bucket, the order's named bucket)
FIRMS = {
    "cottonwood": ("opal-data-cottonwood", "opal-data-cot"),
    "49financial": ("opal-data-49financial", "opal-data-49financial"),
    "inflection": ("opal-data-inflection", "opal-data-inflection"),
}
ROUTES = ("DIRECT", "AI", "UNPLACED-KEY")


def load_plan_module():
    spec = importlib.util.spec_from_file_location("fwd15_ai_plan_rule", str(PLAN_MODULE))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def newest_artifact(s3, bucket, firm):
    prefix = f"irpt/{firm}/gold/holdings/"
    objs = []
    for page in s3.get_paginator("list_objects_v2").paginate(Bucket=bucket, Prefix=prefix):
        objs.extend(o for o in page.get("Contents", []) if o["Key"].endswith(".parquet"))
    if not objs:
        return None, 0
    best = max(objs, key=lambda o: (re.search(r"date=(\d{4}-\d{2}-\d{2})/", o["Key"]).group(1), o["LastModified"]))
    return best, len(objs)


def held_from_snapshot(table):
    """identity key -> {name, symbol, cusip, bloomberg, amount, amount_observed, nodes}; cash line excluded."""
    nodes = [json.loads(s) for s in table.column("node_json").to_pylist()]
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
        ns = sid.get("namespace")
        cusip = str(sid.get("value") or "").strip().upper() if ns == "CUSIP" else ""
        bbg = str(sid.get("value") or "").strip() if ns == "BLOOMBERG" else ""
        name = desc or str(disp.get("label") or "")
        ident = sym or ("CUSIP:" + cusip if cusip else ("NAME::" + slug(name) if slug(name) else ""))
        if not ident:
            continue
        h = held.setdefault(ident, {"name": name, "symbol": sym, "cusip": cusip, "bloomberg": bbg, "amount": None,
                                    "amount_observed": None, "nodes": 0})
        h["nodes"] += 1
        val = (n.get("amount") or {}).get("value")
        if isinstance(val, (int, float)):
            h["amount"] = round((h["amount"] or 0.0) + float(val), 2)
            if n.get("basis") == "OBSERVED":
                h["amount_observed"] = round((h["amount_observed"] or 0.0) + float(val), 2)
        if not h["cusip"] and cusip:
            h["cusip"] = cusip
        if not h["bloomberg"] and bbg:
            h["bloomberg"] = bbg
    return held, cash


def slug(name):
    n = "".join(c if c.isalnum() or c == "-" else " " for c in str(name).upper())
    return " ".join(n.split())[:80]


def main():
    import pyarrow.parquet as pq

    plan = load_plan_module()
    plan.load_runner()  # puts _shared on sys.path
    from etf_classification_scheduled import TableVocabulary, classify_asset_class  # noqa: E402

    contract = json.loads(plan.CONTRACT.read_text(encoding="utf-8"))
    closed = {c: set(v) for c, v in contract["fields"]["sub_asset_class"]["values_by_class"].items()}
    six = plan.SIX
    assert set(closed) == set(six), sorted(closed)

    s3 = boto3.client("s3", region_name=REGION)
    shared_rows = plan.scan_items("etf-classifications")
    shared_keys = {r["ticker"] for r in shared_rows}
    old_rows = plan.scan_items("bd-securities")
    old_by_key = {r["ticker"]: r for r in old_rows}
    live = TableVocabulary.from_live_table()
    vocab = TableVocabulary(
        asset_classes={c for c in live.asset_classes if c in six},
        sub_asset_classes={c: set(live.sub_asset_classes.get(c, set())) & closed[c] for c in six})

    def bd_lookup(k):
        for cand in (k, k[len(plan.CUSIP_PREFIX):] if k.startswith(plan.CUSIP_PREFIX) else None):
            if cand and cand in old_by_key:
                return old_by_key[cand]
        return None

    def route_of(ident, entry):
        sk, form = plan.derive_shared_key(ident, shared_keys)
        if not sk:
            return "UNPLACED-KEY", sk, form
        ac, sac, _ = classify_asset_class(sk, vocab=vocab, bd_securities_lookup=bd_lookup)
        if ac in six and (sac is None or sac in closed[ac]) and ac is not None:
            return "DIRECT", sk, form
        return "AI", sk, form

    firms_out, held_sets, absent_sets = {}, {}, {}
    all_read = True
    for firm, (bucket, ordered_bucket) in FIRMS.items():
        probe = {}
        if ordered_bucket != bucket:
            n_irpt = s3.list_objects_v2(Bucket=ordered_bucket, Prefix=f"irpt/{firm}/gold/holdings/").get("KeyCount", 0)
            n_lots = s3.list_objects_v2(Bucket=ordered_bucket, Prefix="gold/holdings_lots/").get("KeyCount", 0)
            probe = {"order_named_bucket": ordered_bucket, "irpt_holdings_objects": n_irpt, "gold_holdings_lots_objects": n_lots}
        best, n_objs = newest_artifact(s3, bucket, firm)
        if best is None:
            all_read = False
            firms_out[firm] = {"read_ok": False, "bucket": bucket}
            held_sets[firm], absent_sets[firm] = {}, {}
            continue
        got = s3.get_object(Bucket=bucket, Key=best["Key"], IfMatch=best["ETag"])
        body = got["Body"].read()
        table = pq.read_table(io.BytesIO(body), columns=["node_json"])
        held, cash = held_from_snapshot(table)
        prov = {"bucket": bucket, "key": best["Key"], "version_id": got.get("VersionId"),
                "last_modified": best["LastModified"].strftime("%Y-%m-%dT%H:%M:%SZ"), "etag": best["ETag"].strip('"'),
                "size_bytes": len(body), "objects_under_prefix": n_objs, "snapshot_nodes": table.num_rows,
                "cash_line_nodes_excluded": cash, "claim": "measured"}
        absent, by_route = {}, collections.Counter()
        for ident, h in sorted(held.items()):
            sk, form = plan.derive_shared_key(ident, shared_keys)
            cands = [k for k in (h["symbol"], ident, "CUSIP:" + h["cusip"] if h["cusip"] else "",
                                 "BLOOMBERG:" + h["bloomberg"] if h["bloomberg"] else "",
                                 "NAME::" + slug(h["name"]) if slug(h["name"]) else "", sk) if k]
            if any(k in shared_keys for k in cands):
                continue
            route, sk, form = route_of(ident, h)
            absent[ident] = {"key": ident, "name": h["name"], "cusip": h["cusip"] or None, "amount": h["amount"],
                             "amount_observed": h["amount_observed"], "route": route, "shared_key": sk or None, "key_form": form}
            by_route[route] += 1
        ents = sorted(absent.values(), key=lambda e: -abs(e["amount"] or 0.0))
        usd = round(sum(e["amount"] or 0.0 for e in ents), 2)
        usd_obs = round(sum(e["amount_observed"] or 0.0 for e in ents), 2)
        one_route = all(e["route"] in ROUTES for e in ents) and len({e["key"] for e in ents}) == len(ents)
        firms_out[firm] = {"read_ok": True, "provenance": prov, "order_bucket_probe": probe or None, "held_count": len(held),
                           "absent_count": len(ents), "absent_usd": usd, "absent_usd_observed_basis": usd_obs,
                           "route_counts": {r: by_route.get(r, 0) for r in ROUTES},
                           "route_usd": {r: round(sum(e["amount"] or 0.0 for e in ents if e["route"] == r), 2) for r in ROUTES},
                           "every_absent_key_one_route": one_route, "absent": ents}
        held_sets[firm], absent_sets[firm] = held, absent

    # control: the first census's 99 entries, from the plan files it was built from
    first = json.loads(FIRST_CENSUS.read_text(encoding="utf-8"))
    e70, still_abs, missing = [], [], []
    for src in first["sources"]:
        d = json.loads((PLAN_FILES / src).read_text(encoding="utf-8"))
        for e in d["entries"]:
            if e.get("route") == "UNPLACED-KEY":
                e70.append((d["firm"], e))
    by_form = collections.Counter()
    for firm, e in e70:
        held = held_sets.get(firm, {})
        k = e["key"]
        if k not in held:
            continue
        h = held[k]
        # the order's four match forms, tested from the plan entry's own key/cusip/name (not through the widened set)
        forms = [("ticker", k), ("ticker", h["symbol"]), ("CUSIP", "CUSIP:" + e["cusip"] if e.get("cusip") else ""),
                 ("NAME", "NAME::" + slug(e.get("name")) if slug(e.get("name")) else ""),
                 ("BLOOMBERG", "BLOOMBERG:" + h["bloomberg"] if h["bloomberg"] else "")]
        hit = [f for f, x in forms if x and x in shared_keys]
        if hit:
            by_form[hit[0]] += 1
            continue
        still_abs.append((firm, k))
        if k not in absent_sets.get(firm, {}):
            missing.append((firm, k))

    ok = bool(all_read and all(f.get("read_ok") and f["held_count"] > 0 and f["every_absent_key_one_route"] for f in firms_out.values())
              and len(firms_out) == 3)
    doc = {
        "claim": "measured: read-only census of every firm-held key absent from etf-classifications, from the newest served holdings snapshot per firm",
        "generated_at": datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "denominator": {"etf_classifications_rows": len(shared_rows), "etf_classifications_distinct_tickers": len(shared_keys),
                        "bd_securities_rows": len(old_rows)},
        "rules": {"held_identity": "R10_CHECKS/missing_list.py held_securities()", "route": "R11_CHECKS/fwd15_ai_plan.py (derive_shared_key + classify_asset_class)",
                  "present_candidates": "symbol, identity key, CUSIP:<cusip>, BLOOMBERG:<id>, NAME::<slug(description)>, derived shared key"},
        "control": {"first_census": FIRST_CENSUS.name, "first_census_entries": len(e70), "e70_still_held_and_absent": len(still_abs),
                    "missing_from_widened": len(missing), "missing": [list(x) for x in missing],
                    "e70_no_longer_held": sum(1 for f, e in e70 if e["key"] not in held_sets.get(f, {})),
                    "e70_now_present_by_first_matching_form": dict(by_form)},
        "firms": firms_out, "ok": ok,
    }
    OUT.write_text(json.dumps(doc, indent=1, ensure_ascii=True) + "\n", encoding="ascii")
    order = list(FIRMS)
    print("FIRM-HELD-CENSUS ok=%s firms=%d held=%s absent=%s usd=%s e70_still_absent=%d missing_from_widened=%d" % (
        ok, sum(1 for f in firms_out.values() if f.get("read_ok")),
        "/".join(str(firms_out[f].get("held_count", 0)) for f in order),
        "/".join(str(firms_out[f].get("absent_count", 0)) for f in order),
        "/".join("%.2f" % firms_out[f].get("absent_usd", 0.0) for f in order),
        len(still_abs), len(missing)))
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
