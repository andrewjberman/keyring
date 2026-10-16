# CTO ROUND-129 ANALYSIS -- IRPT_DASHBD workstream B-IN (~I2): DB-i-16 (2026-10-16 ~00:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v115 @32e0cacb2f: MAY-CLOSE. The run script is not exercised on real data.
**No PRD addendum.**

- **A grading gap was disclosed by both seats and is accepted:**
  - round 125's wrapper refuses the feed's real silver, because the feed partitions by day and stamps every row with the pull date
    (48 rows refused on a feed-shaped fixture);
  - v110 passed it on fixtures that were not feed-shaped.

  **The rule from here: every B-IN fixture that stands in for the feed is BUILT FROM THE FEED'S OWN WRITER** (the feed script's output
  schema and partitioning, as `pull_inflection_scope_account_returns.py` writes it), never hand-shaped. The first round that touches a
  fixture carries that as a criterion.
- **Round 130** (DB-i-17, a direct act on the issuer's own finding) is the fix. **The first real run waits on it**, and on the feed's first
  scheduled silver.
- **Round 128 (DB-i-15) has drained but has NO packet. `~I2` owes it.** A drained round with no packet is invisible to L8.
- W316 rows are inert.

-- 1.0.0_SA_CTO~DELL2
