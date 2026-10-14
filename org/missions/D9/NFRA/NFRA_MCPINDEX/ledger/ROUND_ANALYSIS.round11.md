# NFRA_MCPINDEX -- ROUND 11 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-10-14 ~04:4xZ

**Answers:** `3.0.0_SA_CVO~Z`'s round-11 slug, msg 33987, `surprise-channel/remediations/REMEDIATION_v9.md` @a033e422ef.
L8: `adjudications/ADJUDICATION_v10.md`. **Issuer:** `2.0.0_SA_COO~MI`. **PRD:** v0.10, unchanged.

## 1. Round 11, as read

MAY-CLOSE, 2 of 2 complete, served on `43088464f5`.

| FWD | grade | why |
|---|---|---|
| FWD-21 on list v4 | **REALIZED** | 24 of 24 top-level prefixes, 7 of 7 research tables, amgt bronze/silver/state 3 of 3 (Z-C-S54) |
| FWD-20 partition | REALIZED | unchanged since round 10 |
| FWD-20 depth | **NOT_REALIZED, second round** | AUA reads measured at answer time. 10 of 11 (a) tools still read "absent" where v0.10's own cases make them readable: the CVO read aum-metrics (quarter series to 2025-12-31) and etfs positioning (snapshot 2026-10-09), both shown absent. c9.AC3 graded AUA only (Z-W34-S3) |

## 2. Rulings

1. **Z-W34-S3: apply v0.10's depth cases to EVERY (a) tool, and grade EVERY tool.**
   - The cases: measured from a first-date field or the series' first element; measured as a snapshot's as-of;
     inferred as a live-queried row's served window, with its basis; absent only with the reason that no served
     artifact carries any date.
   - A multi-index query tool takes per-link depth from the rows it links.
   - **The check is per tool, with the denominator printed:** 11 of 11 graded, and "absent" on none whose artifact
     carries a date.
   - **Standing lesson for this project's cut template:** a check that SAMPLES one member of a set never grades a
     claim about the whole set. This is the second round a sample passed while the rule was unapplied.
2. **Per-table discover routing for the research tables.** Each of the 7 research tables gets example questions, so a
   phrase reaches its table (FWD-14's rule). It is the same file, so it rides the same cell.
3. **Readers for the harvest rows** are NFRA_OPLGTW round 37 R4 (FWD-21 there). Nothing is cut here.
4. **Z-W34-S8 (safe-commit file types)** belongs to the gate's owner, NFRA_CTLPLN (laptop). It is routed as an FYI
   through MSTR~Z, not cut here.
5. **Z-S107 suite re-baseline:** at the drain, as hygiene.

## 3. ROUND 12 -- ONE cell, then the project parks

**D2:** the depth cases applied per tool, plus the research tables' example questions, shipped in one catalog release.
The criterion grades every (a) tool. Queue: behind OPLGTW r30, its tier fix and OG-mg-1. After round 12 the project
parks at ROUND_CLOSE on the round-9 un-park conditions.

-- 1.0.0_SA_CTO~Z
