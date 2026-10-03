# ETFS_RIVALS round 6 -- RFW-D01 on today's page, never-widen pair, CTO half (refresh_a1 republish of 2026-10-02, no code change)

**Signer:** `1.0.0_SA_CTO~Z`, 2026-10-02 ~15:0xZ. **COO half:**
`deliverables/2.0.0_SA_COO~RV/round6/NEVER_WIDEN_HALF_COO_RFW_D01_REFRESH.md` @c1bf9ac157 (branch `rv-fast`; msg 28544). PRD v0.12
lead item RFW-D01 (@afc2bed44f).

## What I read

- **The defect:** the served 10-02 page shows A1 tables built at 11:03-11:04Z. That was before the 11:11Z G1 refresh (7 funds' 10-01
  reports) and before G4 date=2026-10-01 landed (11:10Z). `produce_a1` skips a date that already holds an object. This act fixes
  today's page only; the structural fix is round-6 cell d1-1.
- **The act:** ONE `daily-lambda` publish-page with `refresh_a1` at the deployed 722f0db291. No deploy and no plan.
- **The delta, measured through each producer's `handler_entry`** over the current inputs:
  - `holding_contribution`: 1,440 of 3,778 rows change, in 10 funds, and seven YTD totals move (e.g. ETFT 0.56% -> 0.07%, INEQ 8.29%
    -> 6.51%).
  - `buying_trend`: 5 of 319 rows change.
  - `input_census`: 27 rows change.
  - The page census goes from holdings 2 -> 9 of 13 and prices/GICS 0 -> 79 of 763. The four still missing (IDVZ, BIDD, CGIC, SCHY)
    have no 10-01 report in G1, which is RFW-D07, true today.
  - KPIs are unchanged (13 of 13, 213 trades), and the AI accounts are unchanged.
- **Writers:** the daily Lambda's publish stage (one rule, `produce_a1`).

## Blast radius and rollback

- **P1:** ONE new object each for `holding_contribution`, `buying_trend` and `input_census` at date=2026-10-02. **The rollback is NOT
  an S3 delete:** it re-puts the prior objects' content (`holding_contribution-20261002T110325Z`, `buying_trend-20261002T110403Z`,
  `input_census-20261002T110406Z`) as a newer revision, which "newest wins" then serves, followed by one publish-page. A delete
  would need Andrew's confirmation (CLAUDE.md), and this rollback needs none.
- **P2:** ONE republish of the 10-02 page (batch rv-publish-1002g). The prior page is kept under `revisions/<ts>/`.
- **Unmoved:** code, IAM, G0-G6, the AI run objects, and every other day.

## Conditions

1. The act-start gates hold: nothing in flight; the served objects equal the three measured; the deployed CodeSha256 is the
   722f0db291 set.
2. **The post-act read comes from the SERVED objects and page:**
   - the three A1 objects are the rebuilt ones;
   - the seven YTD totals equal the table above;
   - the census reads 9 of 13 / 79 of 763 / 79 of 763;
   - KPIs and the AI accounts are byte-equal to their pre-act values.
   HTTP status is never the grade.
3. **Carried to round 6, not blocking today:** the AI accounts were graded against the 11:03Z rows, so their prose figures can
   now differ from the rebuilt tables beside them. The section already prints its run time (RFW-D08). Round 6 makes the AI section
   state the table vintage it was written against whenever that differs from the tables served. No AI re-run follows from this act
   (CALL 5: one run per page day).

**CTO HALF: SIGNED** for the one refresh_a1 publish of 2026-10-02 at the deployed 722f0db291, blast radius P1-P2, with the
re-put rollback.
