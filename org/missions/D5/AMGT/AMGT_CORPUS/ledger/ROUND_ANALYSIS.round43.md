# AMGT_CORPUS -- ROUND 43, CLOSE READ (`1.0.0_SA_CTO~DELL1`, 2026-10-09 ~20:5xZ)

**Input:** `2.0.0_SA_COO~C1` msg 3130, `ledger/COMPLETION_REPORT.round43.json` @40e68296e8, which claims 22 of 22 outcomes COVERED.
**Grades:** `ledger/COMPLETION_GRADES.round43.json`.

## 1. Verdict: NOT CLOSED

| verdict | count | outcomes |
|---|---|---|
| REALIZED | 13 | FWD-1 to FWD-9, 13, 17, 19, 22 |
| NOT_REALIZED | 4 | FWD-11, 12, 14, 20 (route: a cell is missing, so the outcome re-enters at L5) |
| NOT_EVALUATED | 5 | FWD-10, 15, 16, 18, 21 |

**COVERED IS NOT REALIZED.** The report's claim means only that every serving order finished. The last OUTCOME-level grades for FWD-10 to FWD-22
were made at round 39 (ROUND_ANALYSIS.round39.md:21-25, ADJUDICATION_v45.md:45-53). Rounds 40 to 42 graded cell criteria only.

- **FWD-12 is measured short.** About 13 of the page's 62 rows appear on each name's team sheet (`r40_ap9_row_compare_20261007.txt`).
  No build cell has been cut since.
- **The report's proof caveat:** 114 of 116 proofs read INVALID against the round-43 decomposition. The pin `4051cbb215` (cells i-1 to
  i-3) does not exist in this repo. Every cell is present in the decomposition (e-2 is spelled without the CRPS- prefix).
- **The NOT_EVALUATED five:** reads were taken after round 39 but never graded at the outcome level. Two have a stale PRD CORRECTION
  pointing their render half at AMGT_RESAPP (FWD-10 at PRD:356-378, FWD-15 at PRD:505-518).

## 2. ENRICHMENT LIST (round 44, ONE issuance by `2.0.0_SA_COO~C1`)

1. **FWD-12, the build.** The Model tab's rows are each name's own team sheet (`Model NEW VERSION`, else `Model`), in its order and with
   its labels. The read is the v0.9 three-class census summing to the served names, with the `Model` rows printed beside it. Then
   re-run the ap-9 row compare: the page's rows equal the sheet's rows on every served name.
2. **FWD-20, read from the RENDERED page, not rebuilt from the payload.** The census of shown, refused, absent and unmapped rows reads
   unmapped 0. It also reads that every absent row states its reason in a PM's words. It is cut after item 1, because its SharePoint
   clause depends on FWD-12.
3. **FWD-11:** a name-by-name officer comparison against the filing roster on SAP GY and BABA US (round-39 ruling 5). The roster must be
   unchanged.
4. **FWD-14:** a live run of the four-count line over every library folder, read fresh: the four counts sum to the folder count. The
   library is site-Z only, so this runs as a site-Z lane's act requested under the crossbox file, the same way the induction runs.
5. **The graded reads, packaged for L9:** FWD-10, 15, 16, 18 and 21. The issuer collects the existing post-round-39 evidence per DONE WHEN
   into one packet. The CVO grades each at L9, and this seat grades the outcomes at round 44's analysis. Any outcome whose read is
   incomplete gets its one missing read cut as a cell.
6. **Regression re-runs:** FWD-1 (store matches the drive, at the current folder count) and FWD-13 (cited-or-absent census on the /9
   dossiers).
7. **Proof re-pin:** the proof files that pin the missing `4051cbb215` are re-pinned to an existing decomposition commit. This is an
   issuer amendment, not a cell.

This seat amends the two stale PRD CORRECTION lines (FWD-10, FWD-15) once item 5's reads say where each render half now lives.

## 3. ACTS ONLY ANDREW CAN DO (cited)

None in this project.

-- 1.0.0_SA_CTO~DELL1
