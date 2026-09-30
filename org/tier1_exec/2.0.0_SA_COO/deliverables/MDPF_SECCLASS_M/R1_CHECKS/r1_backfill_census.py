"""MDPF_SECCLASS round 1 check SC1-k1-AC2: the scheduled-classification backfill census (dry run, no write).

Reads the cell's census JSON, written by the scheduled classification run in dry-run mode over each firm's latest held
securities. Requires, per firm: a held-ticker denominator; would-write rows only for tickers the table lacks; ZERO
overwrites of an existing row (Andrew-direct 2026-09-29 ~21:4xZ: the canonical table is not overwritten by anything in
bd-securities); zero outside-model calls (PRD C-VENDOR); every would-write row labelled classified_by=scheduled with the
input it came from, every bd-securities-sourced row listed; unresolved tickers listed by name. GLD, PHYS and VXX already
have rows, so none of them may appear as a would-write.

Amendment 1 (issuer, row MDPF_SECCLASS-W3-S1): a held ticker the SEED SOURCE already carries (e.g. PHYS, whose row
lands with SC-k-2's seed write) is the seed path's, never a scheduled write: the census counts it as seed_pending.

Run from the repo (or worktree) root. Prints BACKFILL-CENSUS <firm=would_write/held ...> or NOT-CENSUSED: <reason>.
"""
import json
import os
import sys

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BACKFILL_CENSUS_20260929.json"
NEED = ("firm", "as_of", "held_tickers", "already_present", "would_write", "unresolved", "overwrites",
        "vendor_calls", "rows")
PINNED = {"GLD", "PHYS", "VXX"}


def main():
    if not os.path.exists(PATH):
        print("NOT-CENSUSED: %s absent" % PATH)
        return 1
    with open(PATH, encoding="utf-8") as fh:
        doc = json.load(fh)
    firms = doc.get("firms") or []
    if not firms or "bd" not in {f.get("firm") for f in firms}:
        print("NOT-CENSUSED: firms %s (bd, the thread firm, is required)" % [f.get("firm") for f in firms])
        return 1
    if doc.get("overwrite_refused_control") is not True:
        print("NOT-CENSUSED: overwrite_refused_control is not true (the GLD overwrite attempt must be refused)")
        return 1
    out = []
    for f in firms:
        missing = [k for k in NEED if k not in f]
        if missing:
            print("NOT-CENSUSED: %s lacks %s" % (f.get("firm"), missing))
            return 1
        name = f["firm"]
        if f["overwrites"] or f["vendor_calls"]:
            print("NOT-CENSUSED: %s overwrites %s vendor_calls %s" % (name, f["overwrites"], f["vendor_calls"]))
            return 1
        seed_pending = int(f.get("seed_pending") or 0)
        if f["held_tickers"] != f["already_present"] + seed_pending + f["would_write"] + len(f["unresolved"]):
            print("NOT-CENSUSED: %s held %s != present %s + seed_pending %s + would_write %s + unresolved %s" % (
                name, f["held_tickers"], f["already_present"], seed_pending, f["would_write"], len(f["unresolved"])))
            return 1
        if len(f["rows"]) != f["would_write"]:
            print("NOT-CENSUSED: %s would_write %s but lists %d rows" % (name, f["would_write"], len(f["rows"])))
            return 1
        for r in f["rows"]:
            if r.get("classified_by") != "scheduled" or not r.get("input"):
                print("NOT-CENSUSED: %s row %s lacks classified_by=scheduled or its input" % (name, r.get("ticker")))
                return 1
            if str(r.get("ticker", "")).upper() in PINNED:
                print("NOT-CENSUSED: %s would write %s, which already has a row" % (name, r.get("ticker")))
                return 1
        out.append("%s=%d/%d" % (name, f["would_write"], f["held_tickers"]))
    print("BACKFILL-CENSUS " + " ".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
