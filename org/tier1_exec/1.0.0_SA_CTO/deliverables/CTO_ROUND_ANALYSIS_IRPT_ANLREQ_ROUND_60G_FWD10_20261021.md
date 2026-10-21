# CTO round-N analysis: IRPT_ANLREQ round 60 G (FWD-10 Core), 2026-10-21 ~09:3xZ, 1.0.0_SA_CTO~DELL2

**Answers:** the L10 slug from `3.0.0_SA_CVO~DELL2`, msg 11976, ADJUDICATION_v30 @b173905c09.
- The judgment (ACCEPT) is MET: the CVO read PDF pages 59-60, sha 2fc0ad5f8726.
- **FWD-10 is NOT REALIZED.** The approved DONE WHEN names "two Opal models and one ETF", and the live comparison catalogue holds the five Opal models only.

## Grades read (not re-derived)
- **Run 7K (r34s):**
  - packager ATTACHED; audit AUDIT_WRITTEN;
  - the portfolio row reproduces within 0.0012 pt (G2's independent read, msg 11967);
  - the model rows are exact.
- **Run 7J:** wrong portfolio drift. Superseded by 7K, and kept under its own name for comparison.

## The call, ruled
**Realize as written. No ENDPOINT addendum.** Andrew approved the ETF in the text on 2026-10-20, and dropping it would shrink an outcome he worded.
- **The road:** Andrew's 10-20 walk put an "Other ETFs" chip field on the form.
- **The enrichment cell for G2 first measures (read-only, r34s):** does an ETF typed in that field reach `_compare_stage` as a comparable, priced from prices Opal holds?
  - **Yes:** run 7M is one live Multi-Comp with two Opal models and one typed ETF, the same independent read, and an L8 packet to the CVO.
  - **No:** one cell wires the typed-ETF comparable through the existing comparables path, with a failing-first test, in the next resident release. Then 7M.
- **Guard:** ETF prices come from what Opal already holds (C-SWAP / etf-classifications). No new vendor call is made.

## Enrichment list for the next round
1. **FWD-10 ETF leg:** the measurement above, then 7M (owner `2.0.0_SA_COO~G2`).
2. **Page 60 as-of date:** each model row prints its own positioning date (2026-10-08 and 2026-08-18), not one "as of 2026-10-19" (owner G2). It ships in the same release as item 1 when a release is needed.
3. **S220** (unknown ticker): settled by run 7L, now in flight (Y2 GO 09:29Z). Its answer is graded either way.
4. **FWD-3 sheet shape** (carried from TCKT_VNEXT ADDENDUM 6; this seat decides here). **Decided:** it stays a contract with no outcome. The filer is Opal staff (Andrew-direct 2026-10-14, Opal-only Ticket Center), and C-STOREDINPUT and the reader's door checks turn a multi-account sheet or a totals row back at upload, proven by those checks' own tests. No FWD is minted. If a client filer is ever admitted, it becomes an outcome then.

## Close state
- **Round 60 G:** analysed. FWD-10 is NOT REALIZED pending the ETF leg.
- **Other FWDs:**
  - FWD-9 (Overview package) is graded at its own L9.
  - C-AUDIT-RECORD is proven live on 7J and 7K.
  - FWD-13..15 await Andrew's DONE WHEN confirmation.

-- 1.0.0_SA_CTO~DELL2
