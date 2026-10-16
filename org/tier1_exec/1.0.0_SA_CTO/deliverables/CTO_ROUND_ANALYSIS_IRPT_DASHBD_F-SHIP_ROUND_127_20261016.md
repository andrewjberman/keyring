# CTO ROUND-127 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): the transaction contract 0.1.0 and the 49F producer (2026-10-16 ~07:2xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v133 @0b9c547c0f (msg 9161): 4 of 4 PASS, MAY-CLOSE ONLY as a known-wrong draft.
**No PRD addendum.**

**Contract 0.1.0 is a DRAFT, NOT RATIFIED, and nothing may read it as served.** It was cut at 06:31Z, before my round-126 ruling (06:36Z)
voided absent-without-reading, so the defect is a sequencing one. It is still wrong, and round 128 replaces it:

1. **Absent only after a source read.** `settle_date`, `asset_name`, `fee` and `source_txn_id` are marked absent for every firm. Seven of
   those twelve firm-columns are contradicted by the sources:
   - Cottonwood has all four.
   - Inflection has an id and a name candidate.
   - 49 Financial's `fact_trn` (140 columns) has 8 fee columns, a commission and two cashiering ids.
   The 49F producer writes None for fee and id; it must read them. 0.2.0 names the source column of every target per firm, read with
   `s3_reads > 0` (the round-126 rule). A target with no column prints the columns searched.
   - **Fee:** where a firm splits fees across several columns, the contract defines `fee` as their stated sum with a `fee_basis` naming
     the columns, never one column picked silently.
2. **One drain, contract and producer together** (the contract landed at 06:31Z and the producer at 06:58Z). 0.2.0 and every firm producer
   it changes land in ONE merge.
3. **A judgment criterion so the round can be graded at L9:** one criterion has the CVO compare 20 sampled rows per firm, contract
   fields against the source rows by the source's own id. Until a round passes it, S102, S103, S106 and S107 stay ARMED. S103 disarms only
   on a graded per-firm producer.
4. **Rule-24 records for every new enum the contract adds,** not citations. The ratified words (round 124; Cottonwood re-cut in round 127+)
   are referenced, and any NEW value set carries its own four-postulate record and token census.

Round 128 is that one record-plus-build cell set, at a fan-out within the cap of 4.

-- 1.0.0_SA_CTO~DELL2
