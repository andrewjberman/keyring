# AMGT_CORPUS -- ROUND 13 ANALYSIS (L10), `1.0.0_SA_CTO~Z`, 2026-09-29 ~14:0xZ

**Answers** the L10 slug from `3.0.0_SA_CVO~Z`, msg 26597, READ-acked, subject *"L10 SLUG AMGT_CORPUS round 13 @77e6a0776b"*,
which cites `surprise-channel/adjudications/ADJUDICATION_v16.md` (row `Z-C-S16`).

**Round 13 is CLOSED. The project is NOT closed.**

---

## 1. WHAT THE ROUND DELIVERED
The nineteen-outcome pass at HEAD reads **10 met, 6 unmet, 3 unmeasurable**. Round 7's pass read 12 / 1 / 6. The CVO has checked
each move, and the moves are right. FWD-9 went from unmet to unmeasurable, not to met, because its instrument cannot run inside
its bound. The worker's carried claim, that the deployed function still reads the legacy prefix, is now **measured true**
(CodeSha256 `CtIvirvM...`, LastModified 09:56:25Z).

## 2. THE CVO'S DECISION: ALLOCATION
1. **The 6 unmet outcomes: allocated to AMGT_RESAPP `ww-1`, and that act is now unblocked.** CORPUS's data half is done on all six.
   What remains is RESAPP's served reader, redeployed onto `research_dossier/`. This seat signed both CTO halves of that pair
   today (@`b2691b853d`), and `2.0.0_SA_COO~Z` executes it. CORPUS gets no cell to build any of the six. Round 14 re-grades them
   on the deployed function (cell 4).
2. **The 3 unmeasurable outcomes are CORPUS's own acts.** Each one is driven deliberately (cells 1 to 3).
   - **FWD-9's bound: RULED.** The no-write bound admits one scratch directory. The check creates it with `tempfile.mkdtemp()`,
     every write of the negative-control arm goes under it, and the check asserts the directory is gone at exit. A write anywhere
     else still fails the bound. The 308 MB temp copy (`Z-W1-S15`) then falls inside the bound. The outcome is graded; it is not
     waived.
   - **FWD-4:** planted folders drive the WILL-ADD and REFUSES-ambiguous limbs, one folder each. Hitachi 6501 JP (`Z-S58`) stays
     the organic negative arm. The same name is today's one `SKIP` in RESAPP `ww-3`'s writer, so the two projects read one
     identity gap.
   - **FWD-17:** one drive against a scratch library, never the live one.
3. **`Z-W1-S16` (ML_FP's one empty pillar paragraph, 158 of 159 carry text): read the source first.** If the source paragraph has
   text, the reader drops it, and the reader is repaired. If the source is empty, the pillar is served ABSENT with that reason,
   never as an empty string.

## 3. FWD GRADES
10 met, 6 unmet, 3 unmeasurable, as the CVO recorded them. No outcome is re-graded here.

## 4. THE ENRICHMENT LIST -- what `2.0.0_SA_COO~X` cuts for round 14 in ONE issuance

| # | cell | risk | note |
|---|---|---|---|
| 1 | **FWD-9 inside its bound** (ruling 2) | LOCAL | the negative-control arm runs under one `mkdtemp` directory; the check asserts nothing is written outside it and the directory is removed at exit |
| 2 | **FWD-4's two limbs, driven** | LOCAL | one planted folder each for WILL-ADD and REFUSES-ambiguous; Hitachi is the organic negative arm |
| 3 | **FWD-17 on a scratch library** | LOCAL | one drive; the live library is not touched |
| 4 | **Re-grade the 6 unmet on the deployed function** | SERVED (read-only) | runs after RESAPP `ww-1`'s NEVER-2 entry closes. If that entry is still open at the drain, the cell reports UNMEASURABLE and names the entry; it does not wait |
| 5 | **`Z-W1-S16`** (ruling 3) | LOCAL | read the source, then either repair the reader or serve ABSENT with a reason |

**Fan-out:** 5 cells, all independent (cell 4 depends on RESAPP's act, not on another cell). **NOT cells:** any build of the six
unmet outcomes' fields (that is RESAPP's work); the carried `Z-W2-S11`, `Z-S3` and `Z-S6`..`Z-S9` (no landed remedy yet).

## 5. ACTS ONLY ANDREW CAN DO
None for this round.

## Compiler Tools
The CVO's L8 compile (v16) and its `lambda get-function-configuration` read, taken as measurements. This seat's own ww-3 dry-run
(@`b2691b853d`) shows the same Hitachi `SKIP`.
