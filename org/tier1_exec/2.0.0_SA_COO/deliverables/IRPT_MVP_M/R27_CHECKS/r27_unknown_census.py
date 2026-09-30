"""Round 27 (~M) check IBM27-271-AC2: a Holdings build completes with every unknown security unclassified BY NAME.

Reads the cell's census JSON, written from REAL local Holdings builds at all three firms on the corrected classifier
(IB-mr-251 + IB-mr-261 + this cell). Requires, per firm: the build completed (no refusal); zero refused securities;
zero guessed classes; every unclassified security named; the no-ticker (non-TICKER identity) nodes counted; GLD, PHYS
and VXX, where held, in their placed classes.

Run from the repo (or worktree) root. Prints UNKNOWN-CENSUS <firm=unclassified/securities ...> or NOT-CENSUSED: <reason>.
"""
import json
import os
import sys

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R27_UNKNOWN_CENSUS_20260930.json"
FIRMS = ("49financial", "inflection", "cottonwood")
PLACED = {"GLD": ("commodities", "Metals"), "PHYS": ("commodities", "Metals"), "VXX": ("structured", "Hedge")}
NEED = ("firm", "as_of", "completed", "securities", "refused", "guessed", "unclassified", "unclassified_names",
        "no_ticker_nodes", "placed")


def main():
    if not os.path.exists(PATH):
        print("NOT-CENSUSED: %s absent" % PATH)
        return 1
    with open(PATH, encoding="utf-8") as fh:
        doc = json.load(fh)
    firms = {f.get("firm"): f for f in doc.get("firms") or []}
    if set(firms) != set(FIRMS):
        print("NOT-CENSUSED: firms %s" % sorted(firms))
        return 1
    out = []
    for name in FIRMS:
        f = firms[name]
        missing = [k for k in NEED if k not in f]
        if missing:
            print("NOT-CENSUSED: %s lacks %s" % (name, missing))
            return 1
        if f["completed"] is not True or f["refused"]:
            print("NOT-CENSUSED: %s completed=%s refused=%s" % (name, f["completed"], f["refused"]))
            return 1
        if f["guessed"]:
            print("NOT-CENSUSED: %s guessed %s" % (name, f["guessed"]))
            return 1
        if f["unclassified"] != len(f["unclassified_names"]):
            print("NOT-CENSUSED: %s unclassified %s but names %d" % (name, f["unclassified"],
                                                                  len(f["unclassified_names"])))
            return 1
        for tick, cls in (f["placed"] or {}).items():
            want = PLACED.get(str(tick).upper())
            if want and tuple(cls) != want:
                print("NOT-CENSUSED: %s %s lands %s, placed %s" % (name, tick, cls, want))
                return 1
        out.append("%s=%d/%d" % (name, f["unclassified"], f["securities"]))
    print("UNKNOWN-CENSUS " + " ".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
