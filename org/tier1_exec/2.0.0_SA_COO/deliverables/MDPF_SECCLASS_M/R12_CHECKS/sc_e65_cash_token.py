#!/usr/bin/env python3
"""sc_e65_cash_token.py -- MDPF_SECCLASS round 11 SC-e-65 (PRD v0.15 C-CASH-TOKEN): the scheduled producer's direct plan places
a security whose ticker or name carries CASH as a whole token in the table as cash/Cash.

READ-ONLY, no AWS. Calls plan_rows() of infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py with no lookups, an
empty table and an empty seed set, over three held securities:
- BDCASHIN ("BD Cash In") and FCASH ("Fidelity Cash"), which must be planned cash/Cash;
- CASHMERE ("Cashmere Valley Bank"), the difference control, which must NOT be planned cash/Cash (cash is not a whole token there).
Prints SC-E65 ok=<bool> with each outcome. Run from the repo root you are grading.
"""
import sys
from pathlib import Path

ROOT = Path.cwd()  # the repo root the worker runs from (its own worktree), never this file's tree
SHARED = ROOT / "infra/aws/lambda/v2_portal/_shared"
if str(SHARED) not in sys.path:
    sys.path.insert(0, str(SHARED))

HELD = [("BDCASHIN", "BD Cash In"), ("FCASH", "Fidelity Cash"), ("CASHMERE", "Cashmere Valley Bank")]


def main():
    import etf_classification_scheduled as sched  # noqa: E402 -- path set above

    vocab = sched.TableVocabulary(asset_classes={"cash", "equity", "fixed_income", "alternatives", "structured", "commodities"},
                                  sub_asset_classes={"cash": {"Cash", "Money Market", "T-Bill"}})
    rows, unresolved, _ = sched.plan_rows(HELD, vocab=vocab, existing_tickers=set(), seed_source_tickers=set())
    got = {r["ticker"]: (r.get("asset_class"), r.get("sub_asset_class")) for r in rows}
    ins = all(got.get(t) == ("cash", "Cash") for t in ("BDCASHIN", "FCASH"))
    out = got.get("CASHMERE") != ("cash", "Cash")
    ok = ins and out
    print(f"SC-E65 ok={ok} BDCASHIN={got.get('BDCASHIN')} FCASH={got.get('FCASH')} CASHMERE={got.get('CASHMERE')} "
          f"unresolved={len(unresolved)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
