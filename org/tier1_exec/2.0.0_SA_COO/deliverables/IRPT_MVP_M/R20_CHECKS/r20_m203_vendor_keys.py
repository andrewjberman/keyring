"""Round 20 (~M) check IBM20-203-AC2: every firm's real local candidate carries its source vendor keys, and each key
is a registry vendor key (not a function name, not free text).

Reads the per-firm summary the cell writes. Prints VENDOR-KEYED <firm=keys...> or NOT-KEYED: <reason>.
Run from the repo (or worktree) root.
"""
import json
import os
import sys

PATH = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R20_UIC14_VENDOR_KEYS_SUMMARY_20260929.json"
FIRMS = ("49financial", "inflection", "cottonwood")


def main():
    if not os.path.exists(PATH):
        print("NOT-KEYED: %s absent" % PATH)
        return 1
    with open(PATH, encoding="utf-8") as fh:
        data = json.load(fh)
    registry = set(data.get("registry_vendor_keys") or [])
    if not registry or not data.get("registry_source"):
        print("NOT-KEYED: the summary must name registry_source and list registry_vendor_keys")
        return 1
    firms = {f.get("firm"): f for f in data.get("firms") or []}
    if set(firms) != set(FIRMS):
        print("NOT-KEYED: firms %s" % sorted(firms))
        return 1
    out = []
    for name in FIRMS:
        keys = firms[name].get("vendor_keys") or []
        if not keys or not set(keys) <= registry or not firms[name].get("output_field"):
            print("NOT-KEYED: %s keys %s (registry %d keys), output_field %r"
                  % (name, keys, len(registry), firms[name].get("output_field")))
            return 1
        out.append("%s=%s" % (name, "+".join(sorted(keys))))
    print("VENDOR-KEYED " + " ".join(out))
    return 0


if __name__ == "__main__":
    sys.exit(main())
