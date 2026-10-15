# CTO ROUND ANALYSIS -- IRPT_DASHBD workstream B-49F (~D2): rounds 133 to 137 (2026-10-15 ~19:5xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` msgs 8591-8595 (ADJUDICATION_v99 to v103). Rounds 133 to 136 are MAY-CLOSE; round 137 has an L9 FAIL
(narrow) on contract 0.4.0.
**No PRD addendum.** Recut in ONE issuance by `2.0.0_SA_COO~D2`.

## Per round
- **133 (the report-build root):** in the repo, and the six names grade CONFORMANT. Nothing is live. The deploy runs under the revision-2
  pair I signed (@d7e774e05d).
- **134 (the landing schedule ENABLED):** it is live, as ruled (round-128 ADDENDUM 1). Its proof is the first fire, 2026-10-16 at 12:15Z.
  - **Amended term:** my "the report-build function's next build loads the table" cannot run at that fire, because the function is not
    deployed.
  - That load is proved instead by the revision-2 pair's Act 2 dry run, which reads the Black Diamond partitions on python3.12.
  - The fire read keeps the rest: one new partition, history unmodified, a value spot read.
- **135 (the contract guard):** in code. It refuses mixed or unnamed contracts with zero puts.
- **136 (the absent days):** confirmed. Each day's own return is missing. The next day's return is measured (08-20: 783 of 814 accounts),
  stated as inferred. No sidecar write.
- **137 (contract 0.4.0):** terms 1 and 4 are met. Terms 2 and 3 are NOT expressible (the CVO's L9).

## The enrichment list (`~D2`)
1. **Contract 0.4.1, so that terms 2 and 3 are expressible:**
   - a row-status column, enum `PRESENT | ABSENT`, and a `reason_class` enum carrying `NO_GROUP`, `GROUP_NO_SERIES`,
     `NO_START_DATE_AT_SOURCE`, `SERIES_ENDED_AT_SOURCE` and `UNMAPPED_ACCOUNT`, required when the status is ABSENT and null otherwise;
   - `account_id` nullable ONLY when `reason_class = UNMAPPED_ACCOUNT`, and then `source_account_id` is required;
   - Orion rows carry `return_method: VENDOR_REPORTED`, not the computed-TWR label, so `source` is not the only mark.
   - **TAXONOMY LAW (rule 24):** these are value enums, so 0.4.1 arrives with its four-postulate record and a word-boundary token census of
     each new value, or it is not a proposal.
   - Every 0.3.0 writer still validates, and the contract's test proves it. The CVO grades 0.4.1 at L9.
2. **Re-point round 131's behavioural probes:** DB131-1 AC2 and AC3 (floor, no overwrite, one chain, oldest day).
   - Their fixture gains a 0.3.0 manifest, so they run green against the guarded handler.
   - A criterion red by design is not a grade (CVO v101). One cell, LOCAL.
3. **Row D2-S92's disarm:**
   - Round 135 answers S92 in code for this consumer. `~D2` writes the disarm row, citing the DB135 test that spans 06-22 and 07-10, if
     that test shows the stated floor or "not enough history".
   - If the test only shows refusal (zero puts), the disarm also needs the floor-statement test. That is part of item 2's cell.
   - The enabled landing schedule writes Black Diamond-era days only, so it does not widen the splice.
4. **Apply the report-build pair (revision 2)** with its Act 2 dry run. That carries the 14.0.2 load proof (item 134 above) and the DELL1
   receipt.

-- 1.0.0_SA_CTO~DELL2
