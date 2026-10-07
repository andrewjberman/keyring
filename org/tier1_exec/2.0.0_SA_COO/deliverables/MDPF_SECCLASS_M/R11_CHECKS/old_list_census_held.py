#!/usr/bin/env python3
"""old_list_census_held.py -- MDPF_SECCLASS round 9, cell SC-e-50 (FWD-17, analysis rulings 2.4, 2.5, 2.9): the whole old list counted
under the HELD definition, and the reclassification set refreshed with the held column and re-planned under the contract bound.

READ-ONLY against AWS (consistent paginated DynamoDB scans of bd-securities and etf-classifications). NO table write, NO model call,
NO upload. Reads each firm's held set from the Holdings producer's own LOCAL build (holdings_snapshot.py, run WITHOUT --upload; the
parquet under <held-root>/hb_<firm>/), because the firm buckets deny this device's principal. Writes two local files:
  M/OLD_LIST_CENSUS_HELD_20261007.json
  M/OLD_LIST_RECLASSIFY_SET_V2_20261007.tsv     (header old_key shared_key held route asset_class sub_asset_class clean_name)

Held (ruling 2.4, quoted in the census): "'Held' means present with a non-zero market value in the latest served holdings partition of
any of the three firms on the census as-of." Here, the read is the local build of each firm's newest date the producer reaches
(custody_as_of on its nodes), so the claim is `inferred` and the served-bytes read is a laptop seat's act (`served_read`, ruling 2.9).
A security is held by a firm when the sum of its SECURITY nodes' amount.value (USD) is non-zero (|sum| >= 0.005) on that as-of; an old
key is held when it equals a held security's symbol, CUSIP:<cusip> or NAME::<80-char slug of its description> (round 8's match rule,
OLD_LIST_CENSUS). The producer's cash line (ticker CASH) is a SECURITY node with a market value and is counted, as the ruling reads.

Set rules: round 8's planner logic (R10_CHECKS/old_list_reclassify_set.py: derive_shared_key, PRESENT / UNPLACED-KEY / DIRECT / AI,
clean_name), with two changes, both ruling 2.5: the direct-match plan matches against the CONTRACT's closed sub-class list for each of
the six classes (fields.sub_asset_class.values_by_class, SC-e-54), not the values the live table happens to hold, so the old cash rows
are planned; and a DIRECT row must carry a sub-class that is a member of that list (an old row with a class but no sub-class is AI).

Usage (repo root):  python org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R11_CHECKS/old_list_census_held.py [--held-root DIR]
Prints  OLD-LIST-CENSUS-HELD denominator=<n> held=<n> not_held=<n> claim=inferred
"""
from __future__ import annotations

import argparse
import collections
import csv
import datetime
import importlib.util
import json
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
M = HERE.parent
ROOT = HERE.parents[5]
R10 = M / "R10_CHECKS"
SHARED = ROOT / "infra/aws/lambda/v2_portal/_shared"
CONTRACT = ROOT / "org/standards/MDPF_SECCLASS_CONTRACT.json"
DATE = "20261007"
FIRMS = ("49financial", "cottonwood", "inflection")
SIX = ("cash", "fixed_income", "equity", "structured", "alternatives", "commodities")
COLS = ["old_key", "shared_key", "held", "route", "asset_class", "sub_asset_class", "clean_name"]
RULING_24 = ("'Held' means present with a non-zero market value in the latest served holdings partition of any of the three firms "
             "on the census as-of.")


def _load(path: Path, modname: str):
    spec = importlib.util.spec_from_file_location(modname, str(path))
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def firm_held(census, firm, root):
    """(per-firm held key set, detail). A security is held when the sum of its SECURITY nodes' amount.value is non-zero."""
    nodes, files = census.held_nodes(firm, Path(root) / ("hb_" + firm))
    if nodes is None:
        raise SystemExit(f"ERROR: held parquet for {firm} not found or ambiguous under {root} ({files})")
    by_ident = {}
    dates = collections.Counter()
    for nd in nodes:
        ident, keys = census.identity_keys(nd)
        dates[(nd.get("clocks") or {}).get("custody_as_of")] += 1
        if not ident:
            continue
        rec = by_ident.setdefault(ident, {"sum": 0.0, "any_nonzero": False, "keys": set()})
        v = float(((nd.get("amount") or {}).get("value")) or 0.0)
        rec["sum"] += v
        rec["any_nonzero"] = rec["any_nonzero"] or abs(v) >= 0.005
        rec["keys"] |= keys
    held_keys = set()
    n_held = 0
    for rec in by_ident.values():
        if abs(rec["sum"]) >= 0.005:
            n_held += 1
            held_keys |= rec["keys"]
    detail = {
        "custody_as_of": sorted(dates)[-1], "custody_as_of_counts": dict(dates),
        "security_nodes": len(nodes), "distinct_securities": len(by_ident), "securities_non_zero_value": n_held,
        "securities_zero_value": len(by_ident) - n_held,
        "securities_nonzero_node_but_net_zero": sum(1 for r in by_ident.values() if r["any_nonzero"] and abs(r["sum"]) < 0.005),
        "parquet_name": Path(files[0]).name,
    }
    return held_keys, detail


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--held-root", default=str(ROOT / ".scratch"),
                    help="directory holding hb_<firm>/ producer builds")
    ap.add_argument("--out-dir", default=str(M))
    a = ap.parse_args(argv)
    out_dir = Path(a.out_dir)

    sys.path.insert(0, str(SHARED))
    census = _load(R10 / "old_list_census.py", "old_list_census_r11")
    r8 = _load(R10 / "old_list_reclassify_set.py", "old_list_reclassify_set_r11")
    from etf_classification_scheduled import TableVocabulary, classify_asset_class
    from security_name import clean_name

    contract = json.loads(CONTRACT.read_text(encoding="utf-8"))
    closed = {c: list(v) for c, v in contract["fields"]["sub_asset_class"]["values_by_class"].items()}
    assert set(closed) == set(SIX), sorted(closed)

    old_rows = r8.scan_items("bd-securities")
    shared_rows = r8.scan_items("etf-classifications")
    shared_keys = {r["ticker"] for r in shared_rows}
    old_by_key = {r["ticker"]: r for r in old_rows}
    assert len(old_by_key) == len(old_rows), "duplicate hash keys in bd-securities"
    n = len(old_rows)
    print(f"DENOMINATOR old={n} shared={len(shared_keys)} contract={contract.get('contract_version')}", flush=True)

    # ---- the census under the held definition
    held_by_firm, detail = {}, {}
    for firm in FIRMS:
        held_by_firm[firm], detail[firm] = firm_held(census, firm, a.held_root)
    held_union = set().union(*held_by_firm.values())
    per_firm = {f: sum(1 for k in old_by_key if k in held_by_firm[f]) for f in FIRMS}
    held_n = sum(1 for k in old_by_key if k in held_union)
    as_of = max(d["custody_as_of"] for d in detail.values())
    head = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "--short", "HEAD"], capture_output=True, text=True,
                          check=False).stdout.strip()
    doc = {
        "scanned_at": datetime.datetime.now(datetime.timezone.utc).isoformat(), "table": "bd-securities",
        "as_of": as_of, "as_of_by_firm": {f: detail[f]["custody_as_of"] for f in FIRMS},
        "held_definition": RULING_24 + " Read here as: the sum of a security's SECURITY nodes' amount.value (USD) is non-zero "
                           "(|sum| >= 0.005) on each firm's newest as-of the local producer build reaches; an old key is held when it "
                           "equals a held security's symbol, CUSIP:<cusip> or NAME::<80-char slug of its description>.",
        "ruling": "CTO_ROUND_ANALYSIS_MDPF_SECCLASS_ROUND_8_20261007.md 2.4 (whole old list, held or not), 2.9 (dell1 grades inferred)",
        "claim": "inferred",
        "claim_basis": "the held sets are local runs of the Holdings producer (holdings_snapshot.py, no --upload) at as-of per firm "
                       f"{ {f: detail[f]['custody_as_of'] for f in FIRMS} }; the firm buckets opal-data-<firm> deny this device's "
                       "principal; the three parquet files were copied from a sibling worker's scratch (byte-identical in two siblings, "
                       "same names as per_firm_detail.parquet_name) rather than rebuilt; repo HEAD at this run " + head,
        "served_read": "NOT DONE HERE. The grade that needs the served holdings partition (latest served platinum object per firm) is a "
                       "laptop seat's act, filed as a row (ruling 2.9); this census does not stand in for it.",
        "denominator": n, "held": held_n, "not_held": n - held_n, "per_firm": per_firm,
        "per_firm_detail": detail,
        "shared_rows": len(shared_keys),
        "round_8_for_comparison": {"old_rows_held_today": 3152, "definition": "any SECURITY node, zero value included (OLD_LIST_CENSUS_20261007.json)"},
    }

    # ---- the set, v2: round 8's logic, planned under the contract's closed list (ruling 2.5)
    vocab = TableVocabulary(asset_classes=set(SIX), sub_asset_classes={c: set(v) for c, v in closed.items()})
    rows, demoted_no_sub = [], 0
    for key, row in old_by_key.items():
        sk = r8.derive_shared_key(key, shared_keys, census)
        held = "true" if key in held_union else "false"
        nm = clean_name(r8.old_name(row))
        if sk and sk in shared_keys:
            route, ac, sac = "PRESENT", "", ""
        elif not sk:
            route, ac, sac = "UNPLACED-KEY", "", ""
        else:
            got_ac, got_sac, _ = classify_asset_class(sk, vocab=vocab, bd_securities_lookup=lambda _k, _row=row: _row)
            if got_ac in SIX and got_sac and got_sac in closed[got_ac]:
                route, ac, sac = "DIRECT", got_ac, got_sac
            else:
                if got_ac in SIX:
                    demoted_no_sub += 1  # a class with no sub-class is not a verdict inside the bound: the model decides
                route, ac, sac = "AI", "", ""
        rows.append({"old_key": key, "shared_key": sk, "held": held, "route": route,
                     "asset_class": ac, "sub_asset_class": sac, "clean_name": nm or ""})

    def order(r):
        if r["route"] == "PRESENT":
            return (1, 0, 0, r["old_key"])
        return (0, 0 if r["held"] == "true" else 1, 0 if r["old_key"] == r["shared_key"] else 1, r["old_key"])

    rows.sort(key=order)
    by_route = collections.Counter(r["route"] for r in rows)
    by_route_held = collections.Counter((r["route"], r["held"]) for r in rows)
    cash_rows = [r for r in rows if r["route"] == "DIRECT" and r["asset_class"] == "cash"]
    old_cash = [k for k, r in old_by_key.items() if str(r.get("asset_class")) == "cash"]
    doc["set_v2"] = {
        "rows": len(rows), "by_route": dict(by_route),
        "by_route_held": {f"{k[0]}|held={k[1]}": c for k, c in sorted(by_route_held.items())},
        "direct_by_class": dict(collections.Counter(r["asset_class"] for r in rows if r["route"] == "DIRECT")),
        "cash_rows_planned": [{"old_key": r["old_key"], "shared_key": r["shared_key"], "sub_asset_class": r["sub_asset_class"],
                               "held": r["held"]} for r in cash_rows],
        "old_rows_with_class_cash": len(old_cash), "class_without_sub_class_planned_ai": demoted_no_sub,
        "round_8_for_comparison": {"present": 2381, "direct": 5796, "ai": 2785, "unplaced_key": 3},
        "bound": "every DIRECT row's sub_asset_class is a member of contract fields.sub_asset_class.values_by_class[asset_class]; "
                 "AI rows carry no class or sub-class here (decided by the model at the write act)",
    }
    (out_dir / f"OLD_LIST_CENSUS_HELD_{DATE}.json").write_text(json.dumps(doc, indent=1, sort_keys=True, ensure_ascii=True) + "\n",
                                                               encoding="ascii")
    # old keys are exact DynamoDB keys (a few carry non-ASCII, as round 8's set does); row W36-S5
    with (out_dir / f"OLD_LIST_RECLASSIFY_SET_V2_{DATE}.tsv").open("w", encoding="utf-8", newline="") as fh:
        w = csv.writer(fh, delimiter="\t", lineterminator="\n")
        w.writerow(COLS)
        for r in rows:
            w.writerow([r[c] for c in COLS])
    print("SET-V2 rows=%d by_route=%s direct_by_class=%s cash_planned=%d of old_cash=%d class_without_sub_to_ai=%d" % (
        len(rows), dict(by_route), doc["set_v2"]["direct_by_class"], len(cash_rows), len(old_cash), demoted_no_sub))
    print("PER-FIRM as_of=%s old_keys_held=%s" % (doc["as_of_by_firm"], per_firm))
    print(f"OLD-LIST-CENSUS-HELD denominator={n} held={held_n} not_held={n - held_n} claim=inferred")
    return 0


if __name__ == "__main__":
    sys.exit(main())
