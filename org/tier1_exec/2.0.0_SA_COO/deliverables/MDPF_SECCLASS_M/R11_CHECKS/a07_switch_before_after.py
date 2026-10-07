#!/usr/bin/env python3
"""a07_switch_before_after.py -- MDPF_SECCLASS round 9, cell SC-e-42 (FWD-5, FWD-2): a07 reads the canonical table first.

Runs a07's OWN build twice over the held population it reads (a local build, nothing uploaded, output under .scratch/):
  before  canonical=False  (the old-list-only port; its strict --parity-control must report ZERO mismatches)
  after   canonical=True   (the switch; its --parity-control reports the switch's deltas)
and writes M/A07_SWITCH_BEFORE_AFTER_<YYYYMMDD>.json:
  {"as_of", "held_source", "denominator", "rows": [{"key", "before_class", "after_class", "source"}]} plus counts, the changed keys with
  their dollars per firm, and whether --parity-control's changed set equals this file's changed set.
`key` is the identifier the class was read under: for source "canonical" the canonical table's own key (bare ticker, CUSIP:<9>,
BBG:<ticker>:<exch>) so the issuer's check can read it back; `security_key` is a07's dim key.
source: canonical (the switch took the class from etf-classifications) | old_list (no canonical row, an old-list map hit) |
unclassified (in neither table: a07's regex / ticker-shape fallback or UNCLASSIFIED-LOUD; `after_source` names which).
Dollars are the sum of each firm's own market-value column over the same latest partitions a07 reads (49F dim_position
market_value_settled_unsettled, INF positions_mv current_value, COT fact_holdings Market Value); the held set is `inferred`
(a07's population legs read here, not the served mix bytes, which the firm buckets deny this device -- row W25-S1).
READ-ONLY against AWS (S3 gets, DynamoDB scans). Usage (repo root): python <this file> [--as-of 2026-10-07]
"""
from __future__ import annotations

import argparse
import contextlib
import datetime as dt
import io
import json
import re
import sys
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[6]
OUT_DIR = ROOT / "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M"
GOLD = ROOT / "data/assets/scripts/gold/runners_49f"
sys.path.insert(0, str(GOLD))
import a07_dim_asset_classification as a07  # noqa: E402

FIRM_NAME = {"49f": "49financial", "inf": "inflection", "cot": "cottonwood"}


class Tee(io.StringIO):
    def write(self, s):
        sys.__stdout__.write(s)
        return super().write(s)


def run_build(as_of, root, parity, canonical):
    buf = Tee()
    exit_msg = None
    with contextlib.redirect_stdout(buf):
        try:
            a07.build(as_of, str(root), parity, False, canonical=canonical)
        except SystemExit as e:
            exit_msg = str(e)
    return buf.getvalue(), exit_msg


def norm_key(ticker, cusip, name):
    def clean(v):
        s = None if v is None else str(v)
        return None if s in (None, "None", "nan", "", "<NA>") else s
    t, c, n = clean(ticker), clean(cusip), clean(name)
    k = t.upper().strip() if t else None
    if not k:
        k = c
    if not k:
        k = "NAME:" + a07.normalize_name(n)
    return k


def dollars(cache):
    """key -> {firm: usd} from the frames a07's load_population read (cache keyed by (bucket, key))."""
    out = {}

    def add(key, firm, v):
        if v is None or pd.isna(v):
            return
        out.setdefault(key, {}).setdefault(firm, 0.0)
        out[key][firm] += float(v)

    for (b, k), df in cache.items():
        if "schwab/08335338/silver/dim_position/" in k:
            nc = next((c for c in df.columns if "descr" in c.lower() or "security_name" in c.lower()), None)
            for r in df.itertuples(index=False):
                d = r._asdict()
                add(norm_key(d.get("ticker_symbol"), d.get("cusip"), d.get(nc) if nc else None), "49financial",
                    d.get("market_value_settled_unsettled"))
        elif "positions_mv" in k:
            nc = next((c for c in df.columns if "product" in c.lower() or "name" in c.lower()), None)
            for r in df.itertuples(index=False):
                d = r._asdict()
                add(norm_key(d.get("ticker"), None, d.get(nc) if nc else None), "inflection", d.get("current_value"))
        elif "cottonwood/silver/fact_holdings" in k:
            for _, d in df.iterrows():
                t = d.get("Ticker") if d.get("Ticker") is not None and d.get("Ticker") != "" else d.get("Symbol")
                add(norm_key(t, d.get("CUSIP"), d.get("Asset Name")), "cottonwood", d.get("Market Value"))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--as-of", default=dt.datetime.now(dt.timezone.utc).strftime("%Y-%m-%d"))
    ap.add_argument("--scratch", default=str(ROOT / ".scratch" / "a07_switch"))
    a = ap.parse_args()
    scratch = Path(a.scratch)

    cache = {}
    orig_read = a07._read_pq

    def cached(bucket, key):
        if (bucket, key) not in cache:
            cache[(bucket, key)] = orig_read(bucket, key)
        return cache[(bucket, key)]

    a07._read_pq = cached

    print("=== BEFORE: canonical off ===")
    run_build(a.as_of, scratch / "before", False, False)
    print("=== AFTER: canonical first ===")
    run_build(a.as_of, scratch / "after", False, True)
    # The parity control is a THIRD and FOURTH build (it raises SystemExit before writing when it finds a mismatch, so it cannot
    # be the build whose output is read): strict parity with the switch off, then parity with the switch on.
    print("=== PARITY, switch off (the original strict control) ===")
    strict_out, before_exit = run_build(a.as_of, scratch / "parity_strict", True, False)
    print("=== PARITY, switch on (the deltas) ===")
    after_out, after_exit = run_build(a.as_of, scratch / "parity_after", True, True)

    b = pd.read_parquet(scratch / "before" / a07.TABLE / f"date={a.as_of}" / "data.parquet")
    f = pd.read_parquet(scratch / "after" / a07.TABLE / f"date={a.as_of}" / "data.parquet")
    m = b[["security_key", "ticker", "cusip", "asset_name", "asset_class", "classification_source"]].merge(
        f[["security_key", "asset_class", "classification_source"]], on="security_key", suffixes=("_b", "_a"), how="outer",
        indicator=True)
    assert (m["_merge"] == "both").all(), "before/after key sets differ"

    canon = a07._load_canonical()
    pop_variants = {}
    pop = a07.load_population()
    for r in pop.itertuples(index=False):
        pop_variants.setdefault(r.security_key, set()).add((r.ticker, r.cusip, r.asset_name))

    usd = dollars(cache)
    rows = []
    for r in m.itertuples(index=False):
        src_after = r.classification_source_a
        if src_after.startswith("canonical-"):
            source = "canonical"
            # the canonical key actually read: replay the resolution on the representative, else on the variants
            hit = canon.resolve_with_key(r.ticker, r.cusip)
            if not hit or hit[0] != r.asset_class_a:
                hit = None
                for vt, vc, vn in sorted(pop_variants.get(r.security_key, []), key=str):
                    h = canon.resolve_with_key(vt, vc)
                    if h and h[0] == r.asset_class_a:
                        hit = h
                        break
            key = hit[2] if hit else r.security_key
        elif src_after.startswith("dynamodb-"):
            source, key = "old_list", r.security_key
        else:
            source, key = "unclassified", r.security_key
        row = {"key": key, "security_key": r.security_key, "before_class": r.asset_class_b, "after_class": r.asset_class_a,
               "source": source, "before_source": r.classification_source_b, "after_source": src_after}
        if r.asset_class_b != r.asset_class_a:
            row["changed"] = True
            row["usd_by_firm"] = {k: round(v, 2) for k, v in sorted(usd.get(r.security_key, {}).items())}
        rows.append(row)
    rows.sort(key=lambda x: (x["security_key"], x["key"]))

    changed = sorted(r["security_key"] for r in rows if r.get("changed"))
    mm = re.search(r"A5-A07-PARITY-SWITCH-DELTAS: (\d+) (\[.*\])", after_out)
    parity_deltas = sorted({d[0] for d in json.loads(mm.group(2))}) if mm else None
    # the parity compares the representative against the ORIGINAL lib and skips STEP-B rows; name each set difference
    only_parity = sorted(set(parity_deltas or []) - set(changed))
    only_ba = sorted(set(changed) - set(parity_deltas or []))
    counts = {s: sum(1 for r in rows if r["source"] == s) for s in ("canonical", "old_list", "unclassified")}
    per_class = {}
    for r in rows:
        if r.get("changed"):
            per_class[f"{r['before_class']} -> {r['after_class']}"] = per_class.get(f"{r['before_class']} -> {r['after_class']}", 0) + 1
    firm_usd = {}
    for r in rows:
        for fm, v in (r.get("usd_by_firm") or {}).items():
            firm_usd.setdefault(fm, {"changed_usd": 0.0})["changed_usd"] += v
    doc = {
        "as_of": a.as_of,
        "held_source": ("a07's own population legs (latest partitions: " + ", ".join(sorted(f"s3://{b}/{k}" for (b, k) in cache)) +
                        ") built locally with a07.build(canonical=False|True), nothing uploaded; NOT the served mix bytes "
                        "(firm buckets deny this device, row W25-S1) -- inferred"),
        "held_claim": "inferred",
        "denominator": len(rows),
        "counts_by_source": counts,
        "changed": len(changed),
        "changed_by_class_move": dict(sorted(per_class.items())),
        "changed_usd_by_firm": {k: round(v["changed_usd"], 2) for k, v in sorted(firm_usd.items())},
        "parity_before_strict": {"canonical": False, "exit": before_exit, "ok": before_exit is None,
                                 "line": (re.search(r"A5-A07-PARITY-VS-SERVED: .{0,160}", strict_out) or [None])[0]},
        "parity_after": {"exit": after_exit, "switch_deltas": len(parity_deltas or []),
                         "changed_set_equals_before_after": parity_deltas is not None and not only_parity and not only_ba,
                         "only_in_parity": only_parity, "only_in_before_after": only_ba},
        "rows": rows,
    }
    out = OUT_DIR / f"A07_SWITCH_BEFORE_AFTER_{a.as_of.replace('-', '')}.json"
    out.write_text(json.dumps(doc, indent=1, default=str), encoding="utf-8")
    print(f"WROTE {out} denominator={doc['denominator']} counts={counts} changed={len(changed)} "
          f"parity_equal={doc['parity_after']['changed_set_equals_before_after']} "
          f"only_parity={len(only_parity)} only_before_after={len(only_ba)} before_strict_ok={doc['parity_before_strict']['ok']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
