# MDPF_CANON -- ROUND 1, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~21:4xZ)

**Input:** `3.0.0_SA_CVO` slug msg 3230, `surprise-channel/adjudications/ADJUDICATION_v1.md` @a97585cd13. Issuer packet:
`deliverables/2.0.0_SA_COO~D1/round1/ROUND1_CLOSE.md`. PRD v2.9 @12adb87963.

## 1. Graded

- **CN-a-1, the per-firm gold writers: MET.** Three writer roles, each limited to its own firm's gold prefix. The live
  `DenyForeignFirmPrincipals` admits them with no edit, which was the CVO's L6 condition.
- **CN-a-3, the backfill: MET.** 540 partitions, 16 of 16 date sets equal to the legacy dated sources, values match, 0 mismatches.
- **CN-a-2, the one parquet writer: NOT MET YET.** No live daily write has been read. It closes on the scheduled 13:30Z fire on 2026-10-10.
  That fire is the producer's own clock, not a wait this seat can drive: the backfill already drove the writer on demand, and the daily
  path is its organic arm.
- **FWD-1 (the thread): PARTIAL.**
  - It works end to end on the backfilled tree. Asked for 49 Financial's total assets on 2026-09-15, the issuer named
    `mdpf/49financial/gold/aum_metrics/date=2026-09-15/data.parquet` from `address()` alone. Opening the file once confirmed the
    vintage.
  - It is REALIZED when the 10-10 daily write lands at its `address()` path and reads correctly.
- **Rows:** S3-S6 are disarmed (S7), and S4's synthetic partitions are deleted on Andrew's word. 5 rows graduated to REMEDIATION_v1.

## 2. Ruled here

- **W1-S1: the builder map is tier-blind.** The Terraform `opal_name` `scope_bucket["global"]` gives `opal-data-portal-v2`, while
  `address()` puts composite gold in `opal-data-mdpf`.
  - Under rule 30, a builder that cannot produce the right name is a missing registry row, never a hand-typed workaround.
  - Ruled: round 2 cuts the registry row (`infra/logic/registry/`) that makes the builder tier-aware for the global scope. The grant then
    moves from `local.mdpf_bucket` to builder output.
  - Until then, the existing local stands, because it is the measured-correct bucket.

## 3. ENRICHMENT LIST (round 2, ONE issuance by `2.0.0_SA_COO~D1`)

1. **Read the 10-10 13:30Z daily write** (CN-a-2 AC3 and FWD-1's REALIZED read). Read the four types for each of the four scopes at
   their `address()` paths:
   - each one is written;
   - prior partitions are unchanged;
   - the global partition is byte-identical to its legacy source's figures.

   The read runs the tick after the fire. It is an issuer act, not a cell.
2. **M1 (the census) and M7 (the global basis):** neither waits on anything.
3. **M5 (the publisher):** it runs python3.12 with no pyarrow layer (L5_FACTS section 4). Give it the layer, or rule it reads through
   the gold Lambda's writer.
4. **W1-S1 (the builder map):** the registry row and the grant re-pointed to builder output, as ruled in section 2.
5. **account_units forward:** the daily path writes 49financial, inflection and global from the folded figure from the 10-10 fire. The
   read confirms the first partition exists for each.

M3's full-history clause, M4, M6, M8 and M11-M17 follow the PRD's arc after this. M9 and M10 wait on ADVI_FIRMBKTS, now seated on dell1
(`2.0.0_SA_COO~F1`).

## 4. ACTS ONLY ANDREW CAN DO (cited)

None outstanding. S4's delete was done on his word (@991c4cae64).

-- 1.0.0_SA_CTO~DELL1
