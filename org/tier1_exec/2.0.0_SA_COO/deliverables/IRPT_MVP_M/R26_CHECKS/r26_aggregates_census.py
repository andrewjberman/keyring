"""Round 26 (~M) check IBM26-261-AC2 (CTO 103025: W2-11 and W2-15 are served by the producer): the aggregates census.

Reads the cell's census JSON, written from REAL local Holdings builds at all three firms with the new producer-served
blocks. Requires, per firm: the built document validates against the contract at the cell's branch; it carries one
security aggregate per security identity (no identity twice); the security aggregates' weights and the class totals'
weights each sum to the scope total within 0.0001 of 1 (or the census names the held-out remainder that makes up the
difference); the class totals' amounts sum to the custody total within one cent; and the grain the aggregates are
served at is named.

Run from the repo (or worktree) root. Prints AGG-CENSUS <firm=securities/classes ...> or NOT-CENSUSED: <reason>.
"""
import json
import os
import sys

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R26_AGGREGATES_CENSUS_20260929.json"
FIRMS = ("49financial", "inflection", "cottonwood")
NEED = ("valid", "grain", "security_aggregates", "distinct_identities", "security_weight_sum",
        "class_totals", "class_weight_sum", "class_amount_sum", "custody_total", "held_out_weight")


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
        if f["valid"] is not True:
            print("NOT-CENSUSED: %s built document does not validate against the contract" % name)
            return 1
        if not str(f["grain"]).strip():
            print("NOT-CENSUSED: %s names no grain" % name)
            return 1
        if f["security_aggregates"] != f["distinct_identities"]:
            print("NOT-CENSUSED: %s %s aggregates for %s identities" % (name, f["security_aggregates"],
                                                                     f["distinct_identities"]))
            return 1
        held = float(f["held_out_weight"] or 0)
        for k in ("security_weight_sum", "class_weight_sum"):
            if abs(float(f[k]) + held - 1.0) > 0.0001:
                print("NOT-CENSUSED: %s %s %s + held-out %s != 1" % (name, k, f[k], held))
                return 1
        if abs(float(f["class_amount_sum"]) - float(f["custody_total"])) > 0.01:
            print("NOT-CENSUSED: %s class amounts %s vs custody %s" % (name, f["class_amount_sum"],
                                                                    f["custody_total"]))
            return 1
        out.append("%s=%d/%d" % (name, f["security_aggregates"], f["class_totals"]))
    print("AGG-CENSUS " + " ".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
