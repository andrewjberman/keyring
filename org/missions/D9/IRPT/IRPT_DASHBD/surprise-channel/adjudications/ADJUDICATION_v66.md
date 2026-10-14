# IRPT_DASHBD: CVO adjudication, round 106

<sweep_watermark>2026-10-14T15:05Z</sweep_watermark>

L8 compile and L9 grade by `3.0.0_SA_CVO~DELL2`, 2026-10-14T15:05Z, on msg 7696 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND106_B_DRAIN_END_20261014.md`, blob 11c4a27f31). **L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_106_L9_GRADE_20261014.md`): DB106-2-J1 FAIL on two single lines. On p.5, the household chart note points to 'pages 5 and 8', but p.8 is an account. On p.6, the foot note calls the household allocation unavailable above a filled Allocation column. Every round-105 count is fixed, the dash means only 'not held', and orientation is met. DB106-1-AC1 and DB106-2-AC1 re-run here: 2 of 2 PASS. 6 rows dismissed below, 2 ARMED rows among them on their owner's disarm. Held: D2-W169-S3 (the private accessor; next round's cell), and everything round 105 held.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S3",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-14T15:05:00Z",
  "one_line": "Round 106. L9: DB106-2-J1 FAIL on two lines. (1) p.5: the chart note 'Ending value and net additions, last 12 months (household)' points to 'tables on pages 5 and 8'; p.8 is account 9269, and the household's net additions print on p.4. (2) p.6: the foot note says 'the household allocation: not available yet' under an Allocation column that prints the household's class shares. Met: the holdings household Net Gain is filled; chart notes claim no reason; the split columns state the true reason; the dash only in the 3 unheld cells; orientation; no slot name or asterisk. Dismissed (6): D2-W169-S1, -S4 (ARMED; disarmed by their owner in D2-S32: the retired 'dash' words remain only in the builder's reason text and one contract footnote, never visible) and D2-S32; D2-W169-S2 (the calendar fallback on this box, read), -S5 (5 pre-existing portal suite failures). Held: D2-W169-S3.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W169-S1",
   "IRPT_DASHBD-D2-W169-S4",
   "IRPT_DASHBD-D2-S32",
   "IRPT_DASHBD-D2-W169-S2",
   "IRPT_DASHBD-D2-W169-S5"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): judgment criteria are graded at L9, never self-graded; every ARMED row leaves ARMED only on its owner's disarm or a measured read.",
  "world_is": "Both round-106 orders complete; the chain's merge bfe336aef3 is on origin box/dell2; the portal commits are LOCAL and unpushed; nothing served moved. The whole-document rule finds 0 conflicts over 140 cell keys, but it covers non-chart cells, so a chart note's page pointer and a foot note's scope sit outside it. The disclosure release gate (Andrew's call a252) still holds every client render.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's read of 14 of 14 pages, fwd21_sample_r106/pages/r106_1/ (private; no figure copied)",
    "this seat's re-run 2026-10-14T15:0xZ: DB106-1-AC1, DB106-2-AC1 PASS",
    "investigation rows D2-W169-S1..S5, D2-S32",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND106_B_DRAIN_END_20261014.md blob 11c4a27f31 (msg 7696)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_106_L9_GRADE_20261014.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two ARMED rows disarmed by their owner's row with the disarm read stated, that row, and two readings. The accessor row is held for next round."
 }
]
```
