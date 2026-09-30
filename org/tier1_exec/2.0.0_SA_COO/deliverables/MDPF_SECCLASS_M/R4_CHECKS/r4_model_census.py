"""Round 4 (~M) check SC4-e10-AC2: the Kimi K3 residual classification census (Andrew-direct @6a861c4e18).

Reads the cell's census JSON. The denominator is the E8 residual: every entry of R2_UNRESOLVED_REVIEW_20260930.json
that carries no proposed_class. Requires:
- table_rows_at_build >= 2309 and model == "kimi-k3";
- input_fields a subset of {name, ticker} (the standing word covers names and tickers only);
- one result per residual entry, no more and no fewer;
- each result: asset_class in the table vocabulary or null with a reason; confidence a number in [0, 1];
  low_confidence == (confidence < threshold) with threshold 0.80;
- overwrites 0 (a would-write row is a conditional put on absence), and the keyed, cusip_only and name_only counts
  sum to the results.

Run from the repo (or worktree) root. Prints MODEL-CENSUS classified=<c> flagged=<f> of <n> ... or NOT-CENSUSED:
<reason>.
"""
import json
import os
import sys

BASE = "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/"
PATH = BASE + "R4_MODEL_CLASSIFY_CENSUS_20260930.json"
E8 = BASE + "R2_UNRESOLVED_REVIEW_20260930.json"
VOCAB = {"equity", "fixed_income", "alternatives", "commodities", "structured"}
THRESHOLD = 0.80


def main():
    if not os.path.exists(PATH):
        print("NOT-CENSUSED: %s absent" % PATH)
        return 1
    with open(E8, encoding="utf-8") as fh:
        residual = [e for e in json.load(fh)["entries"] if not e.get("proposed_class")]
    with open(PATH, encoding="utf-8") as fh:
        doc = json.load(fh)
    if int(doc.get("table_rows_at_build") or 0) < 2309:
        print("NOT-CENSUSED: table_rows_at_build %s < 2309" % doc.get("table_rows_at_build"))
        return 1
    if doc.get("model") != "kimi-k3":
        print("NOT-CENSUSED: model %r, want kimi-k3" % doc.get("model"))
        return 1
    extra = set(doc.get("input_fields") or []) - {"name", "ticker"}
    if extra or not doc.get("input_fields"):
        print("NOT-CENSUSED: input_fields %s outside {name, ticker}" % doc.get("input_fields"))
        return 1
    if doc.get("threshold") != THRESHOLD:
        print("NOT-CENSUSED: threshold %s, want %s" % (doc.get("threshold"), THRESHOLD))
        return 1
    results = doc.get("results") or []
    if len(results) != len(residual):
        print("NOT-CENSUSED: %d results for %d residual entries" % (len(results), len(residual)))
        return 1
    classified = flagged = 0
    for r in results:
        ac, conf = r.get("asset_class"), r.get("confidence")
        if ac is None:
            if not r.get("reason"):
                print("NOT-CENSUSED: null class without a reason: %s" % r.get("name"))
                return 1
            continue
        if ac not in VOCAB:
            print("NOT-CENSUSED: %s class %r outside the vocabulary" % (r.get("name"), ac))
            return 1
        if not isinstance(conf, (int, float)) or not 0 <= conf <= 1:
            print("NOT-CENSUSED: %s confidence %r" % (r.get("name"), conf))
            return 1
        if r.get("low_confidence") is not (conf < THRESHOLD):
            print("NOT-CENSUSED: %s low_confidence %r at confidence %s" % (r.get("name"), r.get("low_confidence"), conf))
            return 1
        classified += 1
        flagged += bool(r["low_confidence"])
    if doc.get("overwrites") != 0:
        print("NOT-CENSUSED: overwrites %r, must be 0" % doc.get("overwrites"))
        return 1
    parts = [doc.get(k) for k in ("keyed", "cusip_only", "name_only")]
    if any(not isinstance(p, int) for p in parts) or sum(parts) != len(results):
        print("NOT-CENSUSED: keyed/cusip_only/name_only %s do not sum to %d" % (parts, len(results)))
        return 1
    print("MODEL-CENSUS classified=%d flagged=%d of %d (keyed=%d cusip_only=%d name_only=%d, overwrites 0)" % (
        classified, flagged, len(results), parts[0], parts[1], parts[2]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
