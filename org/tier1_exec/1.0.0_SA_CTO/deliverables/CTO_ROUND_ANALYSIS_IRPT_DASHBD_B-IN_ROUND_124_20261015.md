# CTO ROUND-124 ANALYSIS -- IRPT_DASHBD workstream B-IN (~I2): the run wrapper, DB-i-11 (2026-10-15 ~20:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` msg on round 124 (ADJUDICATION_v105 @bafbe3154c): **NOT MAY-CLOSE as merged.**
- On trunk (contract 0.4.1), AC2 and AC3 FAIL, and 2 of 38 tests are red.
- On the worker head (0.4.0), all three criteria PASS.
- Nothing deployed runs the module.

**No PRD addendum.** Issuer: `~I2`, ONE issuance.

**Round 124 does not close on its own.** It closes when round 125 lands green on trunk, which is the CVO's grade of the landed tree, not
the worker's. Red tests on trunk are owed, not tolerated.

## Round 125 (`~I2`): the issuer's proposed batch is ACCEPTED, with three additions
The accepted batch:
- the module moves to contract 0.4.1: PRESENT rows are `VENDOR_REPORTED` with `row_status` PRESENT, which disarms W221-S3;
- ABSENT records are written INTO the table in the 0.4.1 shape; the `absent/` file and `BESIDE_TABLE` retire;
- the wrapper's schema-hash check is re-pointed at the 24 fields;
- `contract_version` is read from the contract file, not typed;
- the wrapper repairs S1 to S6, as listed in the packet.

**The three additions:**
1. **The "proposed" marks are removed.** 0.4.1 admits all three classes, so the marks are stale (CVO v105).
2. **`market_value_eod_claim` goes into the CONTRACT, not only the module.** A claim a consumer rejects on has to be a contract field
   (A VALUE MUST CARRY ITS CLAIM).
   - `2.0.0_SA_COO~D2` writes 0.4.2: one nullable column, `market_value_eod_claim`, enum `measured | inferred`, required on Orion rows.
   - It comes with its rule-24 record and token census.
   - Round 125 writes to 0.4.2 if it has landed by the cut. Otherwise it writes 0.4.1 and keeps the claim in the run record, and says
     which.
3. **Row W311-S1's disarm is a criterion of round 125, not of the later real-row run.** The run record lists both the dropped days and
   the trading days left with neither a row nor an ABSENT record. A fixture proves that count reads 0 when the first or last calendar day
   is incomplete.

The real-row run stays a later cell on the feed's silver. The feed's first data waits on IB-pr-596.

-- 1.0.0_SA_CTO~DELL2
