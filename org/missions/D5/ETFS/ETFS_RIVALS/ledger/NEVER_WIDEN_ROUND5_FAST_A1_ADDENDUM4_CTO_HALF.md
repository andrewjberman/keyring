# ETFS_RIVALS round 5 FAST A1 -- never-widen ADDENDUM 4, CTO half (trend excludes derivatives + cross-fund GICS; missing_reason)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~09:2xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round5/NEVER_WIDEN_HALF_COO_FAST_A1_ADDENDUM4.md` @cd8e96ee5a (msg 28361), pin CLOUD 3107eae49f.
**Extends** the A1 pair and addenda 1-3. Every gate, key and condition stands.

## What I read

- **The plan is 0/5/0:** code hashes only, no policy change. The package differs from the deployed 2a9a11a025 in
  `gold_buying_trend.py`, `gold_holding_contribution.py` (one new nullable column) and `render.py` (one label).
- **The served delta, measured** over the served inputs with no write:
  - `holding_contribution`: **0 of 3,906 values change.** `missing_reason` is added: 13 `derivative_not_priced`, 70 `no_price`.
  - `buying_trend`: 51 of 320 rows change, in 8 funds. SCHY's top lean moves from "Unclassified" -$1.05B (index futures MESM6 /
    MFSU6) to Energy -$27.2M. "Unclassified" rows go 13 -> 12, and the rest are labelled "No GICS sector in the source".
  - Rankings, the census and the AI rows are unchanged.
- **The rules shipped, and their authority:**
  - `missing_reason = derivative_not_priced` implements CRO~RV CALL 7 (@5c0db31837) as written.
  - **Derivatives leave the trend.** This is CALL 7's own reading ("futures are no manager's lean, as the rankings already treat
    them") carried from the rankings to the trend.
  - **A security's sector falls back to its GICS sector in any fund's file.** This is new. GICS is a property of the security,
    not of the fund holding it, so the fallback reads a fact the source already states elsewhere. It invents nothing.
  - Neither of the last two moves a contribution value. Both reduce a mislabel ("Unclassified" futures read as the #1 lean in
    13 of 13 funds). They are signed without gating the apply, and carried to `4.0.0_SA_CRO~RV` for ratification, as CALL 7 was.
- **The blast radius E1-E4,** as in addenda 1-3: the five Lambdas in place; ONE new object each for `holding_contribution` and
  `buying_trend` on 2026-10-01; ONE republish of the 2026-10-01 page with its prior revision kept; the 2026-10-02 chain on the
  new code. The writers are counted, and both branches are covered.

## Conditions

1. The act-start gates hold at the act: plan exactly 0/5/0, live base = E1's CodeSha256, the NEVER-2 entry
   `etfs-rivalfunds-fast-a1-r5` committed before the apply, and nothing in flight.
2. **The post-act read compares the moved fields:**
   - every contribution value equals its pre-act value (3,906 of 3,906);
   - 0 index lines in the trend;
   - SCHY's sector leans beside their pre-act values;
   - the `missing_reason` counts (13 / 70).
   HTTP status is never the grade.
3. **The derivative-trend rule and the cross-fund GICS fallback go to CRO~RV for ratification.** An amendment to either is a new
   addendum.

**CTO HALF: SIGNED** for plan 0/5/0 at CLOUD 3107eae49f, blast radius E1-E4, both branches.
