#!/usr/bin/env python3
"""sc_e65_cash_token.py -- MDPF_SECCLASS round 11 SC-e-65 (PRD v0.15 C-CASH-TOKEN): the scheduled producer's direct plan places
a security whose ticker or name carries CASH as a whole token in the table as cash/Cash.

READ-ONLY, no AWS. Calls plan_rows() of infra/aws/lambda/v2_portal/_shared/etf_classification_scheduled.py with no lookups, an
empty table and an empty seed set, over three held securities:
- BDCASHIN ("BD Cash In") and FCASH ("Fidelity Cash"), which must be planned cash/Cash;
- CASHMERE ("Cashmere Valley Bank"), the difference control, which must NOT be planned cash/Cash (cash is not a whole token there);
- amendment 3 (row S63): a NAME:: key is a name, not a ticker. NAME::CASH ("Cash") is still planned cash/Cash by the whole-name
  leg; NAME::FT UNIT ... MONTHLY CASH and NAME::VICTORYSHARES SMALL CAP FREE CASH FLOW ETF must NOT be (the ticker leg no longer
  reads a NAME:: key's words).
Prints SC-E65 ok=<bool> with each outcome. Run from the repo root you are grading.
"""
import sys
from pathlib import Path

ROOT = Path.cwd()  # the repo root the worker runs from (its own worktree), never this file's tree
SHARED = ROOT / "infra/aws/lambda/v2_portal/_shared"
if str(SHARED) not in sys.path:
    sys.path.insert(0, str(SHARED))

FT_UNIT = "NAME::FT UNIT 9273 INT RATE HEDGE PORT SER 135 MONTHLY CASH"
VICTORY = "NAME::VICTORYSHARES SMALL CAP FREE CASH FLOW ETF"
HELD = [("BDCASHIN", "BD Cash In"), ("FCASH", "Fidelity Cash"), ("CASHMERE", "Cashmere Valley Bank"), ("NAME::CASH", "Cash"),
        (FT_UNIT, "FT Unit 9273 Int Rate Hedge Port Ser 135 Monthly Cash"), (VICTORY, "VictoryShares Small Cap Free Cash Flow ETF")]
IN = ("BDCASHIN", "FCASH", "NAME::CASH")
OUT = ("CASHMERE", FT_UNIT, VICTORY)


def main():
    import etf_classification_scheduled as sched  # noqa: E402 -- path set above

    vocab = sched.TableVocabulary(asset_classes={"cash", "equity", "fixed_income", "alternatives", "structured", "commodities"},
                                  sub_asset_classes={"cash": {"Cash", "Money Market", "T-Bill"}})
    rows, unresolved, _ = sched.plan_rows(HELD, vocab=vocab, existing_tickers=set(), seed_source_tickers=set())
    got = {r["ticker"]: (r.get("asset_class"), r.get("sub_asset_class")) for r in rows}
    ins = all(got.get(t) == ("cash", "Cash") for t in IN)
    out = all(got.get(t) != ("cash", "Cash") for t in OUT)
    ok = ins and out
    print(f"SC-E65 ok={ok} " + " ".join(f"{t.replace(' ', '_')[:22]}={got.get(t)}" for t in IN + OUT)
          + f" unresolved={len(unresolved)}")
    return 0 if ok else 1


if __name__ == "__main__":
    sys.exit(main())
