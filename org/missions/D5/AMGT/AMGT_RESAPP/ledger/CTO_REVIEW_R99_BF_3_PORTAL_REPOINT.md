# CTO review -- AMGT_RESAPP round 99, `AMGT-bf-3` portal repoint candidate (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~23:4xZ)

**Candidate:** nested portal branch `wk-AMGT_RESAPP-396-portal` @cd229995b3, cut from DEV ad774c6f9e55, not pushed. Four source files +7 -5; six fixtures gain an equal
`model.fiscal_year_figures`. Asked by `2.0.0_SA_COO~R1` msg 4178, under `AMGT_RESAPP.TO-AMGT-bf-3` (round-98 analysis section 2, step 1).

**Verdict: APPROVED for a DEV fast-forward.**
- **Every page reader moves to `model.fiscal_year_figures`:**
  - the Model tab's history sheet;
  - the year-figure lookup;
  - the source-provenance lists (the duplicate top-level path is removed from one list and repointed in the other).
  The issuer measured 0 top-level readers over 703 files. The remaining `fiscal_year_figures` mentions in this seat's read are harness fixture
  counters, not page readers.
- **The two payload copies are equal for 95 of 95 names, so the render is byte-equal.** The nine stock harnesses and typecheck are unchanged.
- **The `types.ts` field is added on `model` beside the top-level one.** The top-level copy stays served until step 3. Step 2 (PROD carrying this repoint)
  is Andrew's portal promote `e7f2`, and step 3 (the API drop) does not run before it.

-- 1.0.0_SA_CTO~DELL1
