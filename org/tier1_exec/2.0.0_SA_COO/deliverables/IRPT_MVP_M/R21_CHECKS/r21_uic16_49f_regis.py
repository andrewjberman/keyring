"""Round 21 (~M) check IBM21-213-AC2 after amendment 1 (CTO refusal @05b9abe572): 49F's account labels carry the
REGISTRATION type (Schwab acct_regis) in full from the CTO's committed code table, never the product code (acct_type).

Reads the cell's summary of a REAL local 49F build. Prints SCHWAB-REGIS-NAMED <labelled>/<accounts> or NOT-NAMED: <reason>.
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
    if s.get("field") != "acct_regis":
        print("NOT-NAMED: the summary's field is %r, want 'acct_regis' (the registration type)" % s.get("field"))
        return 1
    if s.get("table_source") != TABLE or s.get("source_url") != table.get("source_url"):
        print("NOT-NAMED: the summary must cite the committed table and its source_url")
        return 1
    known = set(table.get("acct_regis") or {})
    unrec = s.get("unrecognised") or {}
    if any(code in known for code in unrec):
        print("NOT-NAMED: registration codes the table names were printed as unrecognised: %s"
              % sorted(set(unrec) & known))
        return 1
    if not s.get("accounts") or s.get("labelled_full_name", 0) + sum(unrec.values()) != s["accounts"]:
        print("NOT-NAMED: labelled %s + unrecognised %s != accounts %s"
              % (s.get("labelled_full_name"), sum(unrec.values()), s.get("accounts")))
        return 1
    if s.get("guessed", 1) != 0:
        print("NOT-NAMED: guessed labels %s (must be 0)" % s.get("guessed"))
        return 1
    print("SCHWAB-REGIS-NAMED %d/%d (unrecognised %s)" % (s["labelled_full_name"], s["accounts"], unrec))
    return 0


if __name__ == "__main__":
    sys.exit(main())
