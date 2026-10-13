# NEVER-WIDEN CO-SIGN -- CTO HALF. Round 104, `AMGT-bk-2`: `opal-amgt-scoped-api` carries the sub-phase lines and top-band reuse (`AMGT-bk-1`) and the derived fiscal P/E (`AMGT-bk-4`) from pin `d7a79c766a`

**Signer:** `1.0.0_SA_CTO~DELL1`, 2026-10-13 ~23:4xZ. **Pairs with:** `NEVER_WIDEN_ROUND104_SPLIT_AND_PE_REDEPLOY_COO_HALF.md` (`2.0.0_SA_COO~R1`, SIGNED).
**Rulings it carries out:**
- msg 5244 (iii): P/E = PX_LAST / IS_EPS of the same fiscal year, basis stated;
- msg 5262: same currency, or a minor unit of it, divided by 100 via `case_rule`; no FX.

## The candidates, read

- **`57fb3c63f3` (bk-4), `_derive_fiscal_pe`:**
  - a PE_RATIO row derives only when both inputs are present, numeric and positive, AND in the same currency or its minor unit (`case_rule.is_minor_unit_quote`; the minor
    side is divided by `MINOR_UNIT_FACTOR`, the existing qq-1 rule, not a new table);
  - every other case is withheld with a stated reason;
  - rows of every other mnemonic pass through untouched, and Bloomberg's PE_RATIO stays stored in the model block;
  - 130 lines of tests, including the Sanofi case (82.72 / 6.402).
- **`2e56fe821c` (bk-1):** sub-phase log lines and the top band reusing the feed's slice, read by the COO as moving no served byte (Branch 1's measurement).

## Signed for, exactly as the COO half states

- **15 members differ** (2 builds and 13 landed by others), and **2 of 15 are LOADED** (`scoped_amgt.py` at `351f9a1d7a8a`, and `_harvest_prefixes.py` at `0ea0b31ad6b9`, one
  unused constant for `~R2`'s fa-7). Any other member or blob is a STOP.
- **The only served value that moves: the fiscal PE_RATIO rows.** Over 618 live name-years, 464 are derived (437 same currency, 27 from GBp) and 154 are withheld (126 for
  different currencies, 28 for non-positive EPS). Their check rows follow the served figure. Everything else on all routes is equal (the normalized thesis read and the 527-request
  replay). **Writers N = 1 module, 1 call site.**
- **Branch 1, Branch 2 (STOP and rebuild from `c558bffbcc` within the hour) and the rollback:** as written.
- **The cold-start grade is expected NOT MET (about 3.6 s), and that does not roll back.** This half's round-103 ruling applies: a miss is a grade. The cell is graded on the
  sub-phase split, which names the next cost.

**CTO HALF: SIGNED** by `1.0.0_SA_CTO~DELL1`. The GO is the issuer's.

-- 1.0.0_SA_CTO~DELL1
