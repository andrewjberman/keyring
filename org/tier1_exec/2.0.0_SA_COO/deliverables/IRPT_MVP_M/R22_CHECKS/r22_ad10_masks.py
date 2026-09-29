"""Round 22 (~M) check IBM22-221-AC2 (AD-10): every directory entry carries each ACCOUNT's own mask.

Reads the per-firm summary the cell writes from REAL local directory builds, and the committed DirectoryEntry
contract. Every account in every entry has its own mask; no mask carries more than the last 4 digits; at least one
multi-account entry per firm that has one shows more than one distinct tail (the head-row mask would show one).

Run from the repo (or worktree) root. Prints AD10-MASKED <firm=accounts...> or NOT-MASKED: <reason>.
"""
import json
import os
import sys

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R22_AD10_ACCOUNT_MASKS_SUMMARY_20260929.json"
SCHEMA = "docs/contracts/investor-reporting/v1/DirectoryEntry.schema.json"
FIRMS = ("49financial", "inflection", "cottonwood")
FIELDS = ("entries", "accounts", "accounts_with_own_mask", "masks_with_more_than_4_digits",
          "multi_account_entries", "multi_account_entries_with_distinct_tails", "sample")


def main():
    for p in (PATH, SCHEMA):
        if not os.path.exists(p):
            print("NOT-MASKED: %s absent" % p)
            return 1
    with open(SCHEMA, encoding="utf-8") as fh:
        props = json.load(fh).get("properties") or {}
    if "account_masks" not in props:
        print("NOT-MASKED: DirectoryEntry.schema.json has no account_masks property")
        return 1
    with open(PATH, encoding="utf-8") as fh:
        firms = {f.get("firm"): f for f in json.load(fh).get("firms") or []}
    if set(firms) != set(FIRMS):
        print("NOT-MASKED: firms %s" % sorted(firms))
        return 1
    out = []
    for name in FIRMS:
        f = firms[name]
        gaps = [k for k in FIELDS if k not in f]
        if gaps:
            print("NOT-MASKED: %s lacks %s" % (name, gaps))
            return 1
        if not f["accounts"] or f["accounts_with_own_mask"] != f["accounts"]:
            print("NOT-MASKED: %s own masks %s of %s accounts" % (name, f["accounts_with_own_mask"], f["accounts"]))
            return 1
        if f["masks_with_more_than_4_digits"]:
            print("NOT-MASKED: %s %d masks carry more than 4 digits" % (name, f["masks_with_more_than_4_digits"]))
            return 1
        if f["multi_account_entries"] and not f["multi_account_entries_with_distinct_tails"]:
            print("NOT-MASKED: %s has %d multi-account entries and none shows distinct tails"
                  % (name, f["multi_account_entries"]))
            return 1
        out.append("%s=%d" % (name, f["accounts"]))
    print("AD10-MASKED " + " ".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
