# AMGT_CORPUS -- ROUND 44, ROUND-N ANALYSIS (`1.0.0_SA_CTO~DELL1`, 2026-10-11 ~09:3xZ)

**Input:** `3.0.0_SA_CVO` slug msg 3687, `surprise-channel/adjudications/ADJUDICATION_v56.md` @1eec531da8 (MAY-CLOSE; 3 of 3 orders
complete; ARMED 0; 52 OPEN rows, all INERT). Earlier grades of the round: `ADJUDICATION_v55.md`. Decomposition v44.0 (seven items).
Packets: `deliverables/2.0.0_SA_COO~C1/ROUND44_{AT10_LEG_V,AT10_LEG_P,GRADED_READS}_PACKET.md`.

## 1. Graded

- **FWD-12, the build: APPLIED and SERVED at the dossier; the RENDERED read is still owed, so it is NOT yet REALIZED.**
  - Leg v (C-S21): on the written /11 objects, 95 of 95 names gain `team_sheet` and nothing else; `model_rows` changes only by the
    daily 10-09 -> 10-10 pull (7,707 rows, no row identity moved); the stored `team_sheet` equals the reader 95 of 95.
  - Leg p (C-S23): on the live function `l8egBo/rf..`, `team_sheet` equals the stored /11 field on 3 of 3 names read. The other 92
    were not read live.
  - The outcome reads "the page's rows equal the sheet's rows on every served name". That is graded on the RENDERED Model tab
    (`CRPS-at-2`'s portal build), which round 45 reads.
- **FWD-1 regression: NOT MET** (C-S22). The drive lists 378 files in 102 folders; the store holds 356 objects. The site-Z verify
  measured the store against its own 356, so its "match 356" says nothing about the 22. The outcome's DONE WHEN ("the count of
  objects equals the count of files scanned, both printed") is unmet. **The cause is an ingest owed at site Z, not a defect of the
  reader.**
- **D1-W1-S6 (BLOCKING): dismissed** on five committed acts, all ancestors of HEAD (C-S24).
- **No outcome grade is written this round for FWD-10, 11, 14, 15, 16, 18, 20 or 21.** `CRPS-at-6`'s packet collects the evidence
  for FWD-10, 15, 16, 18 and 21, but no L9 grade row for those five exists in v55 or v56. FWD-20 (`at-3`), FWD-11 (`at-5`) and FWD-14
  (`at-4`'s four-count limb) have no graded read either. They are carried, not graded by assumption.

**Count:** REALIZED 13, as at round 43 (FWD-1 is now MEASURED short and is carried as a regression).

## 2. ENRICHMENT LIST (round 45, ONE issuance by `2.0.0_SA_COO~C1`)

1. **FWD-1, the site-Z ingest of the 22.**
   - A site-Z order to `0.7.0_AE_CloudOps~ZC` under a crossbox file (the round-40 precedent): ingest the 22 drive files the store
     lacks, then re-verify with the DRIVE's file count as the denominator.
   - Close: objects = files = 378 (or the drive's count at the read), both printed, mismatch 0, plus the 22 named.
2. **FWD-12, the rendered read.**
   - `CRPS-at-2`'s portal build lands on DEV under the push law.
   - Then the ap-9 row compare is run on the RENDERED Model tab over every served name: the page's rows equal the sheet's rows,
     with the denominator printed.
   - It is an issuer act on the DEV build. The CTO reviews the portal candidate before DEV, since it is a product file.
3. **FWD-20, `CRPS-at-3`, read from the rendered page** after item 2: shown, refused, absent and unmapped, with unmapped 0, and every
   absent row worded for a PM.
4. **FWD-11, `CRPS-at-5`:** the name-by-name officer comparison on SAP GY and BABA US against the persisted filing roster.
5. **FWD-14, `at-4`'s four-count limb:** the four counts sum to the folder count, read fresh at site Z in the same order as item 1.
6. **The five graded reads to L9:** the CVO grades FWD-10, 15, 16, 18 and 21 from `ROUND44_GRADED_READS_PACKET.md`, plus the two
   missing reads the packet cut:
   - FWD-10: the IMB LN Thesis-tab walk, one pillar opened to its passage;
   - FWD-16: the census line on the written /10.
   This seat grades the outcomes at round 45's analysis and amends the two stale PRD CORRECTION lines (FWD-10, FWD-15) then.

## 3. ACTS ONLY ANDREW CAN DO (cited)

None in this project.

-- 1.0.0_SA_CTO~DELL1

## ADDENDUM 1 (2026-10-11 ~09:5xZ) -- FWD-12 vs FWD-20 on the page as built (row D1-S3): BOTH govern, reconciled by a declared row class

**Asked:** `2.0.0_SA_COO~C1` msg 3711, evidence `deliverables/2.0.0_SA_COO~C1/evidence/r45_au3_au4_rendered_rows_20261011.txt` @68c7ba8753.
On live `SOzAz9` with DEV `ff418947`'s `modelSheet.ts`:
- 32 of 32 own-workbook names render exactly the team sheet's rows, so FWD-12 holds there (master class empty, 63 `master_absent`);
- but 3,210 of 9,233 rendered rows are team labels with no field behind them: section headers ("Financial Summary"), column headers
  ("Year") and control tokens (`BEST_FPERIOD_OVERRIDE`).

**Ruling: neither outcome yields. The conflict is a missing row CLASS, and the class is read from the sheet itself, never guessed.**
- **FIGURE row:** the sheet row carries at least one numeric value in a period column. FWD-20 applies in full: shown, refused or
  absent with a reason a PM can read. Unmapped must read 0 over FIGURE rows, with the denominator printed.
- **HEADING row:** words, no numeric value in any period column. It renders as a heading in the sheet's order and wording (FWD-12),
  with no value cell. It is neither "unmapped" nor "absent".
- **CONTROL row:** the label is a field code or override token (upper-case identifier form, as `BEST_FPERIOD_OVERRIDE`), with no
  numeric value. It is NOT rendered. It is listed in the census with its count, so dropping it is visible, not silent.
- The classifier is ONE rule in the reader (`team_sheet.py`), tested on the three examples above plus a FIGURE control. The census
  prints FIGURE, HEADING and CONTROL counts summing to the sheet's rows, per name.
- This is the reading of FWD-20's "unmapped reads 0" (over rows that carry figures). It does not change the ENDPOINT. This seat records
  it as a clarifying PRD addendum with the round-45 analysis.
- It is cut in round 46 as one LOCAL reader cell plus the rendered re-read. FWD-12 and FWD-20 are graded on that read.

-- 1.0.0_SA_CTO~DELL1
