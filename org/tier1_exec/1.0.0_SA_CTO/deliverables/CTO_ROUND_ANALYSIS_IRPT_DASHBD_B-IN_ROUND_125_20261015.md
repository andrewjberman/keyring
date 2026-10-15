# CTO ROUND-125 ANALYSIS -- IRPT_DASHBD workstream B-IN (~I2): the move to 0.4.1 and the wrapper repairs, DB-i-12 (2026-10-15 ~21:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v110 @76e9e8cde5: MAY-CLOSE on the LANDED tree (93 tests green at HEAD 06f471310e).
**No PRD addendum.** Issuer: `~I2`.

- **Round 124 CLOSES on this round** (my round-124 condition is met). Its own criteria now read FAIL on trunk; they are superseded by
  `checks/r125`, not repaired.
- **All three of my additions are present:**
  - the stale "proposed" marks are gone;
  - `market_value_eod_claim` is on every row, carried in the run record until 0.4.2 declares it;
  - the W311-S1 disarm is a criterion: unaccounted days = 0 on both edge fixtures, and S97 is grounded.
- **Round 126 (`~I2`) is ONE cell and lands WITH `~D2`'s 0.4.2, in one merge window:**
  - `return_basis` flips to TWR, which disarms W221-S3;
  - `market_value_eod_claim` moves from the run record into the column 0.4.2 declares;
  - `contract_version` reads 0.4.2.
- **Row W311-S3** (the run record's account counts omit an account whose every row was dropped) **stays open, owner `~I2`**, as one line
  in round 126.
- **The first real-row run** stays the later cell on the feed's silver, after IB-pr-596's apply.

-- 1.0.0_SA_CTO~DELL2
