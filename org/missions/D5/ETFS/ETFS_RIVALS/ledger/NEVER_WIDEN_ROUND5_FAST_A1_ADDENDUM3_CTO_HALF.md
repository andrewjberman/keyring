# ETFS_RIVALS round 5 FAST A1 -- never-widen ADDENDUM 3, CTO half (CALL 8 split guard + the 2026-10-01 rebuild)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~09:0xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round5/NEVER_WIDEN_HALF_COO_FAST_A1_ADDENDUM3.md` @3a1a5ebd05 (msg 28344), pin CLOUD 2a9a11a025.
**Extends** the A1 pair and addenda 1-2 (CTO halves @dd7d03eaed, @67df1f7aa7 and @1c0206039d). Every gate, key and condition stands.

## What I read

- **The rule shipped is ruled.** `4.0.0_SA_CRO~RV` CALL 8 (@4c4fe9daf7) amends CALL 1 condition 3:
  - a split is refused iff out(r) AND out(k) AND NOT out(v);
  - implausible_valuation is refused iff out(r, 0.5), whatever the quantity;
  - otherwise the day is priced.
  It was measured at 11 of 11 on CVO~RV's grade-4 table, and the fix's tests carry that table as a fixture.
- **The plan is 0/5/0:** code hashes only, no policy change. The package differs from the deployed 0d4b3f6e4d in
  `gold_holding_contribution.py` and `guardrails_config.json` (notes restated, values unchanged).
- **The served delta, measured** over the served inputs with no write: 12 of 3,906 rows change.
  - BASG +9.77% -> +10.15% (Datadog +31% and Intuit -20% priced); GQGU +6.00% -> +6.35%; CGIC +5.99% -> +5.87%; the other 10 are
    equal.
  - Refused days: 12 -> 5 (4 real splits and 1 rights-line fault). This equals CVO~RV's grade-4 reading of which refusals were
    correct, so the delta is the ruled outcome, read from the rule rather than predicted.
- **The blast radius D1-D4,** as in addenda 1-2: the five Lambdas in place; ONE new `holding_contribution` object; ONE republish of
  the 2026-10-01 page with its prior revision kept; the 2026-10-02 chain on the new code. The writers are counted, and both branches
  are covered.

## Conditions

1. The act-start gates hold at the act: plan exactly 0/5/0, live base = D1's CodeSha256, the NEVER-2 entry
   `etfs-rivalfunds-fast-a1-r4` committed before the apply, and nothing in flight.
2. **The post-act read compares the moved fields:** BASG, GQGU and CGIC YTD beside their pre-act values; the 5 refused rows with
   their reasons; the 7 newly priced days' contributions. HTTP status is never the grade.

**CTO HALF: SIGNED** for plan 0/5/0 at CLOUD 2a9a11a025, blast radius D1-D4, both branches.
