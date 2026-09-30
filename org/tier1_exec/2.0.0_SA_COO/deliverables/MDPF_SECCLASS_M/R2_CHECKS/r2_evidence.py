"""MDPF_SECCLASS round 2 checks: one evidence reader per cell, each with its own rule.

Usage: r2_evidence.py <cell>, where <cell> is one of label, kind, thread, cot, positions, fwd3, e18, unresolved.
Each reads its cell's JSON under org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/ and prints
<TOKEN> <summary> on success or NOT-MET: <reason> on failure. The rules are the ones the round-2 faces state. Every
evidence file carries `table_rows_at_build`, which must be at least 2,309 (after release step 2), so no pre-backfill
evidence passes.

Run from the repo (or worktree) root.
"""
import json
import os
import sys

BASE = "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/"
MIN_ROWS = 2309
FILES = {
    "label": "R2_LABEL_CENSUS_20260930.json",
    "kind": "R2_KIND_CENSUS_20260930.json",
    "thread": "R2_THREAD_CENSUS_20260930.json",
    "cot": "R2_COT_CALLER_CENSUS_20260930.json",
    "positions": "R2_POSITIONS_CENSUS_20260930.json",
    "fwd3": "R2_FWD3_PLAN_20260930.json",
    "e18": "R2_E18_IAM_20260930.json",
    "unresolved": "R2_UNRESOLVED_REVIEW_20260930.json",
}


def need(d, keys):
    missing = [k for k in keys if k not in d]
    return "lacks %s" % missing if missing else None


def check_label(d):
    err = need(d, ("contract_version", "classified_by_values", "unlabelled_rows", "would_label",
                   "other_attributes_touched", "overwrites"))
    if err:
        return err
    if d["contract_version"] != "0.2.0":
        return "contract_version %r, want 0.2.0" % d["contract_version"]
    if sorted(d["classified_by_values"]) != ["constituents", "legacy", "scheduled", "seed"]:
        return "classified_by values %s" % d["classified_by_values"]
    if d["would_label"] != d["unlabelled_rows"] or d["other_attributes_touched"] or d["overwrites"]:
        return "would_label %s of %s, other attributes %s, overwrites %s" % (
            d["would_label"], d["unlabelled_rows"], d["other_attributes_touched"], d["overwrites"])
    return "LABEL-CENSUS would_label=%d" % d["would_label"]


def check_kind(d):
    err = need(d, ("source_named", "rows_absent_kind", "would_set", "defaulted", "from_bd_securities", "rows"))
    if err:
        return err
    if not str(d["source_named"]).strip():
        return "no input source named"
    if d["defaulted"]:
        return "defaulted %s" % d["defaulted"]
    if d["would_set"] != len(d["rows"]):
        return "would_set %s but lists %d" % (d["would_set"], len(d["rows"]))
    return "KIND-CENSUS would_set=%d of %d absent (source: %s)" % (d["would_set"], d["rows_absent_kind"],
                                                                     d["source_named"])


def check_thread(d):
    for stage in ("resolution", "silver", "gold"):
        s = d.get(stage) or {}
        err = need(s, ("rows", "unclassified", "unclassified_names", "moved", "moves", "guessed"))
        if err:
            return "%s %s" % (stage, err)
        if s["guessed"] or s["unclassified"] != len(s["unclassified_names"]) or s["moved"] != len(s["moves"]):
            return "%s counts disagree or guessed" % stage
    if d.get("bd_securities_reads"):
        return "bd_securities_reads %s" % d["bd_securities_reads"]
    return "THREAD-CENSUS gold rows=%d unclassified=%d" % (d["gold"]["rows"], d["gold"]["unclassified"])


def check_cot(d):
    err = need(d, ("firm", "source", "held_tickers", "already_present", "seed_pending", "would_write", "unresolved",
                   "overwrites", "vendor_calls"))
    if err:
        return err
    if d["firm"] != "cottonwood" or not d["held_tickers"]:
        return "firm %s held %s -- a ticker-keyed cottonwood source must hold tickers" % (d["firm"],
                                                                                          d["held_tickers"])
    if d["overwrites"] or d["vendor_calls"]:
        return "overwrites %s vendor_calls %s" % (d["overwrites"], d["vendor_calls"])
    total = d["already_present"] + d["seed_pending"] + d["would_write"] + len(d["unresolved"])
    if total != d["held_tickers"]:
        return "held %s != %s" % (d["held_tickers"], total)
    return "COT-CALLER held=%d would_write=%d" % (d["held_tickers"], d["would_write"])


def check_positions(d):
    err = need(d, ("rows", "class_sources", "guessed", "unclassified", "unclassified_names", "contract_additive"))
    if err:
        return err
    foreign = {s: n for s, n in d["class_sources"].items() if s not in ("etf-classifications", "unclassified") and n}
    if foreign or d["guessed"] or d["unclassified"] != len(d["unclassified_names"]):
        return "foreign %s guessed %s or unclassified list mismatch" % (foreign, d["guessed"])
    if d["contract_additive"] is not True:
        return "the positions.json change is not additive to its wire contract"
    return "POSITIONS-CENSUS rows=%d unclassified=%d" % (d["rows"], d["unclassified"])


def check_fwd3(d):
    err = need(d, ("ticker", "fork_value", "current_row", "seed_value", "surfaces"))
    if err:
        return err
    if d["current_row"].get("classified_by") != "scheduled":
        return "the chosen row is not a scheduled row"
    if d["fork_value"] == d["seed_value"]:
        return "the seed value equals the fork value -- not a correction"
    if len(d["surfaces"]) < 2:
        return "fewer than two surfaces named"
    return "FWD3-PLAN %s -> %s on %d surfaces" % (d["ticker"], d["seed_value"], len(d["surfaces"]))


def check_e18(d):
    err = need(d, ("principal", "putitem_etf_classifications", "putitem_bd_securities", "fmt_ok", "validate_ok",
                   "schedule"))
    if err:
        return err
    if not (d["putitem_etf_classifications"] and not d["putitem_bd_securities"] and d["fmt_ok"] and d["validate_ok"]):
        return "grant state %s" % {k: d[k] for k in ("putitem_etf_classifications", "putitem_bd_securities",
                                                     "fmt_ok", "validate_ok")}
    if not str(d["schedule"]).strip():
        return "no schedule named"
    return "E18-IAM-DESIRED principal=%s" % d["principal"]


def check_unresolved(d):
    err = need(d, ("denominator", "entries"))
    if err:
        return err
    if d["denominator"] != len(d["entries"]):
        return "denominator %s but %d entries" % (d["denominator"], len(d["entries"]))
    bad = [e.get("name") for e in d["entries"] if not (e.get("proposed_class") or e.get("reason"))]
    if bad:
        return "%d entries carry neither a class nor a reason: %s" % (len(bad), bad[:5])
    classed = sum(1 for e in d["entries"] if e.get("proposed_class"))
    return "REVIEW-COMPLETE %d of %d (classed %d)" % (len(d["entries"]), d["denominator"], classed)


def check_cusip(d):
    """Amendment 1 (E9, CTO 103140): CUSIP-keyed rows on a prefixed key, after a census of every scanning reader."""
    err = need(d, ("reader_denominator", "readers", "would_write", "rows", "overwrites", "guessed"))
    if err:
        return err
    if d["reader_denominator"] != len(d["readers"]) or not d["readers"]:
        return "reader_denominator %s but %d readers" % (d["reader_denominator"], len(d["readers"]))
    open_readers = [r.get("path") for r in d["readers"] if r.get("surfaces_cusip") and not r.get("guard")]
    if open_readers:
        return "readers that would surface a CUSIP key in a ticker list with no guard named: %s" % open_readers[:5]
    bad = [r.get("ticker") for r in d["rows"]
           if not str(r.get("ticker", "")).startswith("CUSIP:") or r.get("identifier_namespace") != "CUSIP"
           or len(str(r.get("ticker", ""))) != len("CUSIP:") + 9]
    if bad:
        return "rows not keyed CUSIP:<9 chars> with identifier_namespace CUSIP: %s" % bad[:5]
    if d["overwrites"] or d["guessed"] or d["would_write"] != len(d["rows"]):
        return "overwrites %s guessed %s would_write %s rows %d" % (d["overwrites"], d["guessed"], d["would_write"],
                                                                   len(d["rows"]))
    return "CUSIP-CENSUS readers=%d would_write=%d" % (d["reader_denominator"], d["would_write"])


FILES["cusip"] = "R2_CUSIP_CENSUS_20260930.json"
RULES = {"label": check_label, "kind": check_kind, "thread": check_thread, "cot": check_cot,
         "positions": check_positions, "fwd3": check_fwd3, "e18": check_e18, "unresolved": check_unresolved,
         "cusip": check_cusip}


def main():
    if len(sys.argv) != 2 or sys.argv[1] not in RULES:
        print("NOT-MET: usage r2_evidence.py <%s>" % "|".join(RULES))
        return 2
    path = BASE + FILES[sys.argv[1]]
    if not os.path.exists(path):
        print("NOT-MET: %s absent" % path)
        return 1
    with open(path, encoding="utf-8") as fh:
        d = json.load(fh)
    if int(d.get("table_rows_at_build") or 0) < MIN_ROWS:
        print("NOT-MET: table_rows_at_build %s < %d" % (d.get("table_rows_at_build"), MIN_ROWS))
        return 1
    res = RULES[sys.argv[1]](d)
    if res.split(" ")[0].isupper() and "-" in res.split(" ")[0]:
        print(res)
        return 0
    print("NOT-MET: %s" % res)
    return 1


if __name__ == "__main__":
    sys.exit(main())
