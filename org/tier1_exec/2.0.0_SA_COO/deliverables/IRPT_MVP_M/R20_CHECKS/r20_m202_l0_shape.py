"""Round 20 (~M) check IBM20-202-AC2: the L0 category shape holds on a REAL local build at every firm.

Reads the per-firm summary the cell writes from its local candidates. Every ACCOUNT's children are CATEGORY nodes
named only Models / SMAs / Client, the L0 amounts sum to the account amount within $0.01, no MODEL_WRAPPER node
remains, and the candidate's node-amount total equals the pre-change candidate's (no dollars created or lost).

Run from the repo (or worktree) root. Prints L0-SHAPED <firm=accounts...> or NOT-SHAPED: <reason>.
"""
import json
import os
import sys

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_L0_SHAPE_SUMMARY_20260929.json"
FIRMS = ("49financial", "inflection", "cottonwood")
FIELDS = ("accounts", "accounts_with_non_category_child", "accounts_l0_sum_mismatch", "model_wrapper_nodes",
          "category_names", "security_amount_total_before", "security_amount_total_after", "candidate_sha256")


def main():
    if not os.path.exists(PATH):
        print("NOT-SHAPED: %s absent" % PATH)
        return 1
    with open(PATH, encoding="utf-8") as fh:
        firms = {f.get("firm"): f for f in json.load(fh).get("firms") or []}
    if set(firms) != set(FIRMS):
        print("NOT-SHAPED: firms %s" % sorted(firms))
        return 1
    out = []
    for name in FIRMS:
        f = firms[name]
        gaps = [k for k in FIELDS if k not in f]
        if gaps:
            print("NOT-SHAPED: %s lacks %s" % (name, gaps))
            return 1
        if not f["accounts"] or f["accounts_with_non_category_child"] or f["accounts_l0_sum_mismatch"] or f["model_wrapper_nodes"]:
            print("NOT-SHAPED: %s %s" % (name, {k: f[k] for k in FIELDS[:4]}))
            return 1
        if not set(f["category_names"]) <= {"Models", "SMAs", "Client"}:
            print("NOT-SHAPED: %s category names %s" % (name, f["category_names"]))
            return 1
        if abs(float(f["security_amount_total_before"]) - float(f["security_amount_total_after"])) > 0.01:
            print("NOT-SHAPED: %s totals moved %s -> %s" % (name, f["security_amount_total_before"], f["security_amount_total_after"]))
            return 1
        out.append("%s=%d" % (name, f["accounts"]))
    print("L0-SHAPED " + " ".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
