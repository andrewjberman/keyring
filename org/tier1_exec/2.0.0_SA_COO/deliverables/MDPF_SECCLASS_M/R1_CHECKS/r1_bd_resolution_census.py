"""MDPF_SECCLASS round 1 check SC1-t1-AC2: the BD classifier's resolution census, before and after (thread hop 1).

Reads the cell's census JSON, written from the BD chain's latest real holdings (opal-data-bd) classified by the library
before (bd-securities scan, name aliases, pattern and ticker-shape guesses) and after (etf-classifications through the one
client). Requires: after, zero bd-securities reads and zero guessed classes (a holding the table lacks is unclassified,
by name); GLD, PHYS and VXX, where held, land commodities/Metals, commodities/Metals, structured/Hedge; every moved
holding listed with before and after; every reader of the library named.

Run from the repo (or worktree) root. Prints BD-CENSUS holdings=n moved=m unclassified=u or NOT-CENSUSED: <reason>.
"""
import json
import os
import sys

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/R1_BD_RESOLUTION_CENSUS_20260929.json"
PLACED = {"GLD": ("commodities", "Metals"), "PHYS": ("commodities", "Metals"), "VXX": ("structured", "Hedge")}


def main():
    if not os.path.exists(PATH):
        print("NOT-CENSUSED: %s absent" % PATH)
        return 1
    with open(PATH, encoding="utf-8") as fh:
        d = json.load(fh)
    for k in ("as_of", "holdings", "before_layers", "after_layers", "moved", "moves", "unclassified",
              "bd_securities_reads_after", "guessed_after", "readers"):
        if k not in d:
            print("NOT-CENSUSED: census lacks %s" % k)
            return 1
    if d["bd_securities_reads_after"] or d["guessed_after"]:
        print("NOT-CENSUSED: after reads bd-securities %s times, guesses %s" % (d["bd_securities_reads_after"],
                                                                              d["guessed_after"]))
        return 1
    if d["moved"] != len(d["moves"]):
        print("NOT-CENSUSED: moved %s but lists %d" % (d["moved"], len(d["moves"])))
        return 1
    for m in d["moves"]:
        want = PLACED.get(str(m.get("ticker", "")).upper())
        if want and (m.get("after", {}).get("asset_class"), m.get("after", {}).get("sub_asset")) != want:
            print("NOT-CENSUSED: %s lands %s, placed %s" % (m.get("ticker"), m.get("after"), want))
            return 1
    if len(d["readers"]) < 5:
        print("NOT-CENSUSED: %d readers named; the library has at least five (assets dim, C_06, D_03, D_04, E_25)"
              % len(d["readers"]))
        return 1
    print("BD-CENSUS holdings=%d moved=%d unclassified=%d" % (d["holdings"], d["moved"], d["unclassified"]))
    return 0


if __name__ == "__main__":
    sys.exit(main())
