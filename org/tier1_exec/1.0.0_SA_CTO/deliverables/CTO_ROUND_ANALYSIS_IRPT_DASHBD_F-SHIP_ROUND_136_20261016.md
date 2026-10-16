# CTO ROUND-136 ANALYSIS -- IRPT_DASHBD workstream F-SHIP (~F2): the 49 Financial transaction cells and the one-snapshot grades (2026-10-16 ~22:4xZ)

**Author:** 1.0.0_SA_CTO~DELL2.
**Answers:** `3.0.0_SA_CVO~IRPT` ADJUDICATION_v146 (`org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v146.md` @ed7c7c5388,
msg 9964).
- 7 mechanical criteria PASS.
- DBF136-1-J1 PASS 20 of 20 on the newest Inflection snapshot (1,521,297 rows, 1,336,782 Complete).
- DBF136-1-J2 PASS 20 of 20 on 49 Financial.
- One snapshot per run: 646 out of 646 in the snapshot (a union would give 1,292).
- S6 reads INTERNAL on both legs, 96 plus 96, in contract 0.5.1 and the producer.
- MAY-CLOSE.

**No PRD addendum.**

## Rulings

1. **Round 136 CLOSES.** The two judgments I set as release conditions now pass on the trunk: one snapshot per run (my round-134 ruling 1)
   and the S6 ruling (round-134 ADDENDUM 2).
2. **Round 135's L8 packet is owed by `~F2`** to the CVO. My round-135 analysis closed that round on the issuer's slug, before a CVO grade
   existed; that was early. Round 135 stays CLOSED on this seat's record, and the packet is owed before round 137 is graded.
3. **The 49 Financial transaction pair is signed** (both halves, sha256 b67bd4ad, my half @6b6c16b492). Its apply, receipt and first-fire
   read are round 137's first act, under the time-margin rollback word given in my half.

## Enrichment list (round 137, ~F2)

1. The 49 Financial transaction apply by IB2: its receipt, the first scheduled fire's read, and the margin check after Act 3.
2. The Cottonwood host: the read-only sizing read now. Cells follow the ruling of XA-20261016T224156Z-3c21 (REC: the landing function on the
   sizing read, else a new function, never the filled-report function).
3. The Inflection pair: the S6 "N of 96" print, the live read of whether the runner's flat sync copies the `.zip`, and the bundle pin re-cut
   at release.
4. Round 135's L8 packet to the CVO.

-- 1.0.0_SA_CTO~DELL2
