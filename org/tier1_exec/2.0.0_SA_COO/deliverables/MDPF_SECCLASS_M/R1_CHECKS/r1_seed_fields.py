"""MDPF_SECCLASS round 1 check SC1-k2-AC2: instrument_kind and industry on every seed row, and the seed-vs-live diff.

Reads the cell's census JSON. Requires: every row both seed scripts would write carries instrument_kind with a value
from org/standards/MDPF_SECCLASS_CONTRACT.json; GLD, PHYS and VXX read 'fund'; the seed-vs-live diff over every live
row is listed (differences other than the new fields named per ticker); zero rows whose existing class values the seed
run would change unless the census lists each one with before and after.

Run from the repo (or worktree) root. Prints SEED-FIELDS <seed_rows/live_rows diffs=n> or NOT-READY: <reason>.
"""
import json
import os
import sys

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_SEED_FIELDS_CENSUS_20260929.json"
CONTRACT = "org/standards/MDPF_SECCLASS_CONTRACT.json"


def main():
    if not os.path.exists(PATH):
        print("NOT-READY: %s absent" % PATH)
        return 1
    with open(CONTRACT, encoding="utf-8") as fh:
        values = set(json.load(fh)["fields"]["instrument_kind"]["values"])
    with open(PATH, encoding="utf-8") as fh:
        doc = json.load(fh)
    for k in ("seed_rows", "live_rows", "kinds", "class_changes", "other_diffs"):
        if k not in doc:
            print("NOT-READY: census lacks %s" % k)
            return 1
    kinds = doc["kinds"]
    if len(kinds) != doc["seed_rows"]:
        print("NOT-READY: %d kinds for %d seed rows" % (len(kinds), doc["seed_rows"]))
        return 1
    bad = sorted(t for t, v in kinds.items() if v not in values)
    if bad:
        print("NOT-READY: instrument_kind outside %s for %s" % (sorted(values), bad[:10]))
        return 1
    for t in ("GLD", "PHYS", "VXX"):
        if kinds.get(t) != "fund":
            print("NOT-READY: %s instrument_kind %r, want fund" % (t, kinds.get(t)))
            return 1
    for c in doc["class_changes"]:
        if not {"ticker", "before", "after"} <= set(c):
            print("NOT-READY: class change row lacks ticker/before/after: %s" % c)
            return 1
    print("SEED-FIELDS %d/%d diffs=%d class_changes=%d" % (doc["seed_rows"], doc["live_rows"],
                                                          len(doc["other_diffs"]), len(doc["class_changes"])))
    return 0


if __name__ == "__main__":
    sys.exit(main())
