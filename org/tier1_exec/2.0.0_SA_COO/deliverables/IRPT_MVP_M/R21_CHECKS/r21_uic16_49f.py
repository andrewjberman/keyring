"""Round 21 (~M) check IBM21-213-AC2 (UIC-16 at 49F): 49F's account labels carry the full Schwab names from the
CTO's committed code table, and only the codes the table lacks print as unrecognised.

Reads the cell's summary of a REAL local 49F build. Prints SCHWAB-NAMED <labelled>/<accounts> or NOT-NAMED: <reason>.
Run from the repo (or worktree) root.
"""
import json
import os
import sys

TABLE = "org/tier1_exec/1.0.0_SA_CTO/deliverables/SCHWAB_ACCOUNT_CODES_BRIDGEFT_READ_20260929.json"
SUMMARY = "org/tier1_exec/2.0.0_SA_COO/deliverables/IRPT_MVP_M/R21_UIC16_49F_SUMMARY_20260929.json"


def main():
    for p in (TABLE, SUMMARY):
        if not os.path.exists(p):
            print("NOT-NAMED: %s absent" % p)
            return 1
    with open(TABLE, encoding="utf-8") as fh:
        table = json.load(fh)
    with open(SUMMARY, encoding="utf-8") as fh:
        s = json.load(fh)
    if s.get("table_source") != TABLE or s.get("source_url") != table.get("source_url"):
        print("NOT-NAMED: the summary must cite the committed table and its source_url")
        return 1
    known = set(table.get("acct_regis") or {}) | set(table.get("acct_type") or {})
    unrec = s.get("unrecognised") or {}
    if any(code in known for code in unrec):
        print("NOT-NAMED: codes the table names were printed as unrecognised: %s" % sorted(set(unrec) & known))
        return 1
    if not s.get("accounts") or s.get("labelled_full_name", 0) + sum(unrec.values()) != s["accounts"]:
        print("NOT-NAMED: labelled %s + unrecognised %s != accounts %s"
              % (s.get("labelled_full_name"), sum(unrec.values()), s.get("accounts")))
        return 1
    if s.get("guessed", 1) != 0:
        print("NOT-NAMED: guessed labels %s (must be 0)" % s.get("guessed"))
        return 1
    print("SCHWAB-NAMED %d/%d (unrecognised %s)" % (s["labelled_full_name"], s["accounts"], unrec))
    return 0


if __name__ == "__main__":
    sys.exit(main())
