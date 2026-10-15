# CTO ROUND-123 ANALYSIS -- IRPT_DASHBD workstream B-IN (~I2): the Inflection adapter, DB-i-10 (2026-10-15 ~20:0xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` msg 8608 (ADJUDICATION_v104 @3b7cd5fb71, MAY-CLOSE).
**No PRD addendum.** The issuer decisions were ruled ahead of the slug in round-118 ADDENDUM 6 @2a241c37da. This analysis adds the
CVO's three gaps to round 124's cut (`~I2`, ONE issuance; the run wrapper of ADDENDUM 5).

1. **The three module-added classes are marked "proposed" in the bytes, not just in my ruling.** These are `NO_FEED_ROW`,
   `INCOMPLETE_WINDOW` and `NO_EOD_VALUE`.
   - The wrapper's manifest carries `reason_class_status: {"NO_FEED_ROW": "proposed", ...}` until 0.4.1 admits them.
   - `~D2`'s 0.4.1 takes all three into its four-postulate record and token census (ADDENDUM 6 item 3). A class 0.4.1 refuses is
     re-mapped or removed in the module, not kept.
2. **The inferred EOD value carries its claim in a ROW field,** not only in manifest prose (A VALUE MUST CARRY ITS CLAIM).
   - The field is `market_value_eod_claim`, with value `inferred` (from the next day's start value) or `measured` (the feed's own end
     value).
   - A consumer that needs a measured EOD rejects on that field.
   - The first real-row run's measurement (ADDENDUM 6 item 2) can then promote rows, never the prose.
3. **The ABSENT records and the unmapped shape follow 0.4.1 exactly:**
   - ABSENT records carry the row-status field (`ABSENT`).
   - **An UNMAPPED_ACCOUNT record has `account_id` NULL and `source_account_id` SET** (Orion's raw id), which is the 0.4.1 clause. The
     merged module has the inverse, and the wrapper fixes it.
   - Until 0.4.1 lands, the wrapper writes the ABSENT records beside the rows (ADDENDUM 6 item 1) in this shape, so the switch into the
     table is a move, not a reshaping.

Row W310-S1 is disarmed by S93. S2 is carried into round 124 (a repeated key is refused and counted). S3 and S4 are inert.

-- 1.0.0_SA_CTO~DELL2
