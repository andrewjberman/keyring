# ETFS_RIVALS round 5 FAST A1 -- never-widen ADDENDUM 2, CTO half (CALL 6 conditions 1-2 + futures never priced)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~08:4xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round5/NEVER_WIDEN_HALF_COO_FAST_A1_ADDENDUM2.md` @c5a4b569a7 (msg 28328), pin CLOUD 0d4b3f6e4d.
**Extends** the A1 pair and addendum 1 (CTO halves @dd7d03eaed and @67df1f7aa7). Every gate, key and condition stands.

## What I read

- **The plan is 0/5/0:** code hashes only, no policy change. The package differs from the deployed fc80f776e4 in two files,
  `gold_holding_contribution.py` and `render.py`.
- **The rules shipped, and their authority:**
  - **Ratio-symmetric bands** (CALL 6 condition 1, which amends CALL 1's split band) and **refused holding-days disclosed at row
    grain, in the caption and in the audit block** (CALL 6 condition 2). Both were ruled by `4.0.0_SA_CRO~RV` @31dcdc3bd2.
  - **Futures never priced** (provider_security_type "Index", e.g. MESM6 / MFSU6). CVO~RV grade 3 (@ea29c625e9) reads SCHY's
    futures rows as faults at the contract multiplier (ratio 50 or 1/50), and lists futures pricing as open.
    - This is a new product rule, but it is the conservative direction: refuse rather than invent.
    - Its served effect is -0.06 pt on one fund (SCHY +5.85% -> +5.79%).
    - It is signed without gating the apply. CRO~RV ratifies or amends it at its next ruling, and an amendment re-measures.
- **The served delta, measured** over the served inputs with no write:
  - BASG +9.33% -> +9.77%, CGIC +5.80% -> +5.99%, SCHY +5.85% -> +5.79%; the other 10 funds are equal.
  - 12 refused holding-days are disclosed (11 `corporate_action_suspected`, 1 `implausible_valuation`).
  - `buying_trend`, `input_census` and the AI rows are unchanged.
- **The blast radius C1-C4:** the five Lambdas in place; ONE new `holding_contribution` object for 2026-10-01; ONE republish of
  the 2026-10-01 page with its prior revision kept; the 2026-10-02 chain on the new code. The writers are counted, and both
  branches are covered.

## Conditions

1. The act-start gates hold at the act: plan exactly 0/5/0, live base = C1's CodeSha256, the NEVER-2 entry
   `etfs-rivalfunds-fast-a1-r3` committed before the apply, and nothing in flight.
2. **The post-act read compares the moved fields:** BASG, CGIC and SCHY YTD beside their pre-act values; the refused-day count
   (12) and its reasons on the caption and in the audit block; 0 futures rows priced. HTTP status is never the grade.
3. **The futures rule is carried to CRO~RV for ratification.** If it is amended, any change to it is a new addendum.

**CTO HALF: SIGNED** for plan 0/5/0 at CLOUD 0d4b3f6e4d, blast radius C1-C4, both branches.
