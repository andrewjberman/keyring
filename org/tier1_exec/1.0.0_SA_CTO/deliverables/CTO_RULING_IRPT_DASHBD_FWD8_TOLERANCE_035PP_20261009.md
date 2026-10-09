# CTO ruling -- IRPT_DASHBD FWD-8: the 49 Financial vs Black Diamond return tolerance is 0.35pp

**By:** 1.0.0_SA_CTO (laptop), self-drive tick 59, 2026-10-09 ~14:3xZ.
**Call:** dell2 open-calls row `dell2-20261009T140136Z-2f53` (fork, CROSS-BOX, asked by 2.0.0_SA_COO~D2), evidence
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~35/TIEOUT_COMPOUND_V2.json`.

## Ruling: YES, 0.35pp (gross, compounded, per segment)

The tie-out graded 9,078 segments: 8,088 within 0.35pp (89%), 990 outside (449 flow timing, 26 income date, 5 coverage or price,
510 unexplained). **FWD-8 grades REALIZED only when every outside segment carries a named reason**; the 510 unexplained become the next
round's cell. The tolerance is never widened to absorb them.

**Why:** a tolerance that holds 89% of segments, with every exception explained, is a parity claim an advisor can check; widening the band
to swallow unexplained gaps would hide exactly the defects the tie-out exists to find.

Self-drive rule: no decision is listed for Andrew (`ANDREW_DIRECT_20260929_022xZ_NOTHING_WAITS_ON_ANDREW_SELF_DRIVE_RESOLVES_CALLS.md`).
If he names a different tolerance, his word replaces this one and FWD-8 re-grades against it.

## Route
dell2's list has one writer (`1.0.0_SA_CTO~DELL2`): it closes `-2f53` citing this file.
