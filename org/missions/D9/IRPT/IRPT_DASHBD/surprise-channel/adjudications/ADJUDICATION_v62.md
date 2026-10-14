# IRPT_DASHBD: CVO adjudication, rounds 101 and 102

<sweep_watermark>2026-10-14T04:26:23Z</sweep_watermark>

L8 compile and L9 grade by `3.0.0_SA_CVO` (seated on dell2), 2026-10-14T04:26:23Z, on msg 7518 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND101_102_B_DRAIN_END_20261014.md @4404620f0a`). **L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_101_L9_GRADE_20261014.md`): DB101-5-J1 PASS, with a
placeholder 'Sample Firm' header to add to round 102's render fix. 39 rows dismissed below; three ARMED rows held with their owners;
round 98's rows wait for its packet. No remediation row while round 98 runs.

```json
[
 {
  "id": "IRPT_DASHBD-C-S73",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-14T04:26:23Z",
  "one_line": "Rounds 101 and 102 (benchmark read). L9: DB101-5-J1 PASS (this seat read 8 of the 14 page images against the record and the baseline; note: every page prints the placeholder 'Sample Firm' in the header where the baseline prints the firm's report title, a client-facing defect the ranked list omits: add it to round 102's render-fix cell). Dismissed (39): D2-W146-S4 and -S5 (fixed by DB-b-187: 14 sheets on 14 pages, charts draw from series), D2-W152-S1 (BLOCKING, ARMED: no rasteriser; the issuer's amendment added one and the pages were read, this seat among the readers), D2-W152-S2, -S4, the absent-member classification and builder rows (D2-W153-S1 to -S5, D2-W154-S1 to -S4), the gold census rows (D2-W155-S1 to -S8, -S11 to -S13, D2-S26), the section-check rows (D2-W156-S1 to -S8, the four display defects ruled into round 102's first cell), the benchmark rows (D2-W157-S1 to -S4, D2-S27, ruled by the CTO msg 7511). HELD with their owners: D2-W152-S3 (ARMED: sheet height inline 7.6in, print.css outside the grant), D2-W155-S9 (ARMED: the firm registry's bucket field disagrees with address() for Cottonwood and Inflection), D2-W155-S10 (ARMED: Cottonwood account_return_daily gold stale since 2026-06-22). Wait for round 98's packet (DB-b-183 pending): D2-S24, D2-W149-S1 to -S3.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-S26",
   "IRPT_DASHBD-D2-S27",
   "IRPT_DASHBD-D2-W146-S4",
   "IRPT_DASHBD-D2-W146-S5",
   "IRPT_DASHBD-D2-W152-S1",
   "IRPT_DASHBD-D2-W152-S2",
   "IRPT_DASHBD-D2-W152-S4",
   "IRPT_DASHBD-D2-W153-S1",
   "IRPT_DASHBD-D2-W153-S2",
   "IRPT_DASHBD-D2-W153-S3",
   "IRPT_DASHBD-D2-W153-S4",
   "IRPT_DASHBD-D2-W153-S5",
   "IRPT_DASHBD-D2-W154-S1",
   "IRPT_DASHBD-D2-W154-S2",
   "IRPT_DASHBD-D2-W154-S3",
   "IRPT_DASHBD-D2-W154-S4",
   "IRPT_DASHBD-D2-W155-S1",
   "IRPT_DASHBD-D2-W155-S11",
   "IRPT_DASHBD-D2-W155-S12",
   "IRPT_DASHBD-D2-W155-S13",
   "IRPT_DASHBD-D2-W155-S2",
   "IRPT_DASHBD-D2-W155-S3",
   "IRPT_DASHBD-D2-W155-S4",
   "IRPT_DASHBD-D2-W155-S5",
   "IRPT_DASHBD-D2-W155-S6",
   "IRPT_DASHBD-D2-W155-S7",
   "IRPT_DASHBD-D2-W155-S8",
   "IRPT_DASHBD-D2-W156-S1",
   "IRPT_DASHBD-D2-W156-S2",
   "IRPT_DASHBD-D2-W156-S3",
   "IRPT_DASHBD-D2-W156-S4",
   "IRPT_DASHBD-D2-W156-S5",
   "IRPT_DASHBD-D2-W156-S6",
   "IRPT_DASHBD-D2-W156-S7",
   "IRPT_DASHBD-D2-W156-S8",
   "IRPT_DASHBD-D2-W157-S1",
   "IRPT_DASHBD-D2-W157-S2",
   "IRPT_DASHBD-D2-W157-S3",
   "IRPT_DASHBD-D2-W157-S4"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and judgment criteria are graded at L9, never self-graded.",
  "world_is": "All six orders of rounds 101 and 102 are complete; round 98 is not terminal (DB-b-183 held on dell1's ledger SC-e-97), so no remediation row is written this compile. Everything LOCAL: renders and the sample in the private folder, portal branches unpushed, nothing served or deployed. 46 of 117 members filled; percent values print at 100x (this seat confirmed on p.8).",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S26, D2-S27, D2-W146-S4, D2-W146-S5, D2-W152-S1, D2-W152-S2, D2-W152-S4, D2-W153-S1, D2-W153-S2, D2-W153-S3, D2-W153-S4, D2-W153-S5, D2-W154-S1, D2-W154-S2, D2-W154-S3, D2-W154-S4, D2-W155-S1, D2-W155-S11, D2-W155-S12, D2-W155-S13, D2-W155-S2, D2-W155-S3, D2-W155-S4, D2-W155-S5, D2-W155-S6, D2-W155-S7, D2-W155-S8, D2-W156-S1, D2-W156-S2, D2-W156-S3, D2-W156-S4, D2-W156-S5, D2-W156-S6, D2-W156-S7, D2-W156-S8, D2-W157-S1, D2-W157-S2, D2-W157-S3, D2-W157-S4",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND101_102_B_DRAIN_END_20261014.md @4404620f0a (msg 7518)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_101_L9_GRADE_20261014.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Fixed by the round's cells, ruled into round 102, or readings stated in their records; three ARMED rows held with their owners."
 }
]
```
