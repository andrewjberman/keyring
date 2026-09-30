"""Round 25 (~M) check IBM25-251-AC2 (CTO placement @c3c3f414dc): the Holdings class census from etf-classifications.

Reads the cell's census JSON, written from REAL local Holdings builds at all three firms before (bd-securities via
etf_classifier) and after (the etf-classifications table through the existing client) the change. Requires: the after
source is the table; every firm has a before/after count; every moved security is listed with its before and after
class; GLD, PHYS and VXX, where a firm holds them, land in their placed classes (GLD/PHYS commodities with sub-asset
Metals; VXX structured with sub-asset Hedge); nothing is guessed; the Positioning readers of a PHYS row are named.

Run from the repo (or worktree) root. Prints CLASS-CENSUS <firm=moved/securities ...> or NOT-CENSUSED: <reason>.
"""
import json
import os
import sys

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R25_ETF_CLASS_CENSUS_20260929.json"
FIRMS = ("49financial", "inflection", "cottonwood")
PLACED = {"GLD": ("commodities", "Metals"), "PHYS": ("commodities", "Metals"), "VXX": ("structured", "Hedge")}


def main():
    if not os.path.exists(PATH):
        print("NOT-CENSUSED: %s absent" % PATH)
        return 1
    with open(PATH, encoding="utf-8") as fh:
        doc = json.load(fh)
    if doc.get("after_source") != "etf-classifications":
        print("NOT-CENSUSED: after_source %r, want etf-classifications" % doc.get("after_source"))
        return 1
    if not doc.get("positioning_readers"):
        print("NOT-CENSUSED: no Positioning readers of a PHYS row named")
        return 1
    firms = {f.get("firm"): f for f in doc.get("firms") or []}
    if set(firms) != set(FIRMS):
        print("NOT-CENSUSED: firms %s" % sorted(firms))
        return 1
    out = []
    for name in FIRMS:
        f = firms[name]
        for k in ("securities", "moved", "moves", "guessed"):
            if k not in f:
                print("NOT-CENSUSED: %s lacks %s" % (name, k))
                return 1
        if f["guessed"]:
            print("NOT-CENSUSED: %s guessed %s classes" % (name, f["guessed"]))
            return 1
        if f["moved"] != len(f["moves"]):
            print("NOT-CENSUSED: %s moved %s but lists %d moves" % (name, f["moved"], len(f["moves"])))
            return 1
        for m in f["moves"]:
            if not {"symbol", "before", "after"} <= set(m):
                print("NOT-CENSUSED: %s move row lacks symbol/before/after: %s" % (name, m))
                return 1
            want = PLACED.get(str(m["symbol"]).upper())
            if want and (m["after"].get("asset_class"), m["after"].get("sub_asset")) != want:
                print("NOT-CENSUSED: %s %s lands %s, placed %s" % (name, m["symbol"], m["after"], want))
                return 1
        out.append("%s=%d/%d" % (name, f["moved"], f["securities"]))
    print("CLASS-CENSUS " + " ".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
