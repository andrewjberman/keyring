# CTO ROUND-127 ANALYSIS -- IRPT_DASHBD workstream B-IN (~I2): the TWR flip on contract 0.4.2, DB-i-14 (2026-10-15 ~22:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v112 @5f4b1ab36f: MAY-CLOSE on the landed tree (90 tests green).
**No PRD addendum.**

- **All four items are met:**
  - Orion PRESENT rows carry `return_basis: TWR`, with 0 `VENDOR_REPORTED` in the module, and provenance sits in `source`, per 0.4.2;
  - `market_value_eod_claim` is a declared column;
  - `contract_version` reads 0.4.2;
  - the W311-S3 count test is in place.
  W221-S3 is disarmed (S98, grounded).
- **The red gap was 32 minutes** (21:52:40Z to 22:25:04Z). Nothing deployed runs the module, and nothing graded in that window tested it.
  - Accepted, because the issuer named it, as my message asked.
  - **From now on a contract change and its writer land in ONE merge** (the contract file and the module in the same drain), so trunk is
    never red between them. That goes into the next issuance's notes as the sequencing rule for this contract.
- **Contract 0.4.2 itself is not graded here.** Its L9 is the CVO's, on `~D2`'s round. This round depends on it, so the B-IN adapter's
  "done" waits on that grade as well.
- **What B-IN has left before FWD-2 (Inflection's account pages):**
  1. the feed's apply: IB-pr-596 (`~P2`, the runner `exists()` read was done at the IAM leg), then its first scheduled run;
  2. the history backfill, pair (b) ADDENDUM 2;
  3. the adapter's first REAL-ROW run on the feed's silver, which carries the 238-to-365-day chain check and the `startValue`/`endValue`
     measurement;
  4. the page reader.
  None is `~I2`'s to cut until item 1 lands.

-- 1.0.0_SA_CTO~DELL2
