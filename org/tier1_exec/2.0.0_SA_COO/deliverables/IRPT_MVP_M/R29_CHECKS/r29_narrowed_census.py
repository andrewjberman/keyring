"""Round 29 (~M) check IBM29-291-AC2: the NARROWED Holdings class release census (CTO 103169).

The Holdings producer reads a security's class from etf-classifications where the table holds it, and falls back to
the declared bd-securities exception otherwise (FWD-6; owner 2.0.0_SA_COO~M; sunset MDPF_SECCLASS E8+E9). Reads the
cell's census JSON from REAL local builds at all three firms against TODAY's served snapshot. Requires, per firm:
- the build completed, with nothing refused and nothing guessed;
- the count moving from a class to unclassified reads 0, with its denominator;
- every class change is listed with its weight;
- GLD, PHYS and VXX, where held, read from the TABLE (class_source etf-classifications) in their placed classes;
- the fallback count is printed.

Run from the repo (or worktree) root. Prints NARROWED-CENSUS <firm=moved/fallback/securities ...> or
NOT-CENSUSED: <reason>.
"""
import json
import os
import sys

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R29_NARROWED_CENSUS_20260930.json"
FIRMS = ("49financial", "inflection", "cottonwood")
PLACED = {"GLD": ("commodities", "Metals"), "PHYS": ("commodities", "Metals"), "VXX": ("structured", "Hedge")}
NEED = ("firm", "as_of", "completed", "securities", "refused", "guessed", "to_unclassified", "denominator",
        "moved", "moves", "fallback", "placed")


def main():
    if not os.path.exists(PATH):
        print("NOT-CENSUSED: %s absent" % PATH)
        return 1
    with open(PATH, encoding="utf-8") as fh:
        doc = json.load(fh)
    if int(doc.get("table_rows_at_build") or 0) < 2309:
        print("NOT-CENSUSED: table_rows_at_build %s < 2309" % doc.get("table_rows_at_build"))
        return 1
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
        if f["completed"] is not True or f["refused"] or f["guessed"]:
            print("NOT-CENSUSED: %s completed=%s refused=%s guessed=%s" % (name, f["completed"], f["refused"],
                                                                         f["guessed"]))
            return 1
        if f["to_unclassified"] != 0 or not f["denominator"]:
            print("NOT-CENSUSED: %s to_unclassified=%s of %s -- must be 0 with a denominator" % (
                name, f["to_unclassified"], f["denominator"]))
            return 1
        if f["moved"] != len(f["moves"]) or any("weight" not in m for m in f["moves"]):
            print("NOT-CENSUSED: %s moves list or weights incomplete" % name)
            return 1
        for tick, rec in (f["placed"] or {}).items():
            want = PLACED.get(str(tick).upper())
            if want and ((rec.get("asset_class"), rec.get("sub_asset_class")) != want
                         or rec.get("class_source") != "etf-classifications"):
                print("NOT-CENSUSED: %s %s reads %s, placed %s from the table" % (name, tick, rec, want))
                return 1
        out.append("%s=%d/%d/%d" % (name, f["moved"], f["fallback"], f["securities"]))
    print("NARROWED-CENSUS " + " ".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
