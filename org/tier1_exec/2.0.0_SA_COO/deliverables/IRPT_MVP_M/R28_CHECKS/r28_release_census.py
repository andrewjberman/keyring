"""Round 28 (~M) check IBM28-281-AC1: the Holdings release census, measured AFTER the MDPF_SECCLASS backfill.

Reads the cell's census JSON, written from REAL local Holdings builds at all three firms on the held chain
(IB-mr-251/261/271/272) against the live etf-classifications as it stands after release step 2 (ledger
mdpf-secclass-backfill-20260930 CLOSED @f13cddd058: 2,309 rows). Requires: the table row count read at build time is at
least 2,309 (so the census is not the stale pre-backfill one); per firm the build completed with zero refused and
zero guessed; the securities whose class MOVES against today's served snapshot listed with before and after; the
unclassified names listed; GLD, PHYS and VXX, where held, in their placed classes; the aggregates block valid.

Run from the repo (or worktree) root. Prints RELEASE-CENSUS <firm=moved/unclassified/securities ...> or
NOT-CENSUSED: <reason>.
"""
import json
import os
import sys

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R28_RELEASE_CENSUS_20260930.json"
FIRMS = ("49financial", "inflection", "cottonwood")
PLACED = {"GLD": ("commodities", "Metals"), "PHYS": ("commodities", "Metals"), "VXX": ("structured", "Hedge")}
MIN_TABLE_ROWS = 2309
NEED = ("firm", "as_of", "completed", "securities", "refused", "guessed", "moved", "moves", "unclassified",
        "unclassified_names", "placed", "aggregates_valid")


def main():
    if not os.path.exists(PATH):
        print("NOT-CENSUSED: %s absent" % PATH)
        return 1
    with open(PATH, encoding="utf-8") as fh:
        doc = json.load(fh)
    if int(doc.get("table_rows_at_build") or 0) < MIN_TABLE_ROWS:
        print("NOT-CENSUSED: table_rows_at_build %s < %d -- a pre-backfill census" % (
            doc.get("table_rows_at_build"), MIN_TABLE_ROWS))
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
        if f["moved"] != len(f["moves"]) or f["unclassified"] != len(f["unclassified_names"]):
            print("NOT-CENSUSED: %s counts disagree with their lists" % name)
            return 1
        if f["aggregates_valid"] is not True:
            print("NOT-CENSUSED: %s aggregates block not valid" % name)
            return 1
        for tick, cls in (f["placed"] or {}).items():
            want = PLACED.get(str(tick).upper())
            if want and tuple(cls) != want:
                print("NOT-CENSUSED: %s %s lands %s, placed %s" % (name, tick, cls, want))
                return 1
        out.append("%s=%d/%d/%d" % (name, f["moved"], f["unclassified"], f["securities"]))
    print("RELEASE-CENSUS " + " ".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
