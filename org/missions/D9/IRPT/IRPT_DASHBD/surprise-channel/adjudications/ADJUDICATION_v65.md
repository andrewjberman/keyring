# IRPT_DASHBD: CVO adjudication, round 105

<sweep_watermark>2026-10-14T14:12Z</sweep_watermark>

L8 compile and L9 grade by `3.0.0_SA_CVO~DELL2`, 2026-10-14T14:12Z, on msg 7679 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND105_B_DRAIN_END_20261014.md`, blob 94d5e1d21e). **L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_105_L9_GRADE_20261014.md`): DB105-2-J1 FAIL. Round 104's counts 2 and 3 are fixed, and count 1 is fixed on the Activity Summary. It remains on p.7, where the household Net Gain for 4 windows reads "needs more history" while p.4 prints it. A second instance this seat missed in round 104: allocation charts claim "needs more history" while their values print. Orientation is met. DB105-1..3-AC1 re-run here: 3 of 3 PASS. 13 rows dismissed below; 4 ARMED rows among them leave ARMED on their owners' disarm rows. Held: D2-W167-S4..S7 (for the remedy cell and the candidate), D2-W164-S3, D2-W165-S1..S2, D2-W166-S2, -S4 (the applies), D2-S30 and round 98's rows (DB-b-183 APPLIED 12:08:39Z; leg L3's read is open), D2-W149-S2, -S3, D2-W155-S10 (ARMED). No remediation row while round 98 runs.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S2",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-14T14:12:00Z",
  "one_line": "Round 105. L9: DB105-2-J1 FAIL. (1) p.7: the household Net Gain for 4 windows reads 'needs more history' while p.4 prints all 4 and p.5 prints the 12-month one; the cross-table rule's 6 pairs do not include this one. (2) p.2 and p.5: the allocation charts claim 'needs more history' while p.7 prints the class allocation and p.5 the account values (missed by this seat in round 104). Fixed: the Activity Summary is filled and reconciles; notes name their account; slot names are client words; no asterisk prints. Orientation MET. Dismissed (13): D2-W158-S1, -S4, -S6 (ARMED; disarmed by their owner in D2-S29: contract 0.4.1/0.4.2 percent points, kind written at 42 sites, the fee-basis line follows its member) and D2-S29; D2-W167-S3 (ARMED; the issuer's ruling D2-S31, no fourth kind) and D2-S31; D2-W167-S1 (a structurally-zero counter in the record, read), -S2 (the sample's reference date moved, read), -S8 (ruled in D2-S31: digits masked, checker amended @07f8c57528), -S9 (5 portal suite failures, identical at base); D2-W168-S1 (the calendar's fallback table on this box, read); D2-W164-S1 (the market_topic_daily route removed by DB-b-204), -S2 (data_as_of moved, read).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W158-S1",
   "IRPT_DASHBD-D2-W158-S4",
   "IRPT_DASHBD-D2-W158-S6",
   "IRPT_DASHBD-D2-S29",
   "IRPT_DASHBD-D2-W167-S3",
   "IRPT_DASHBD-D2-S31",
   "IRPT_DASHBD-D2-W167-S1",
   "IRPT_DASHBD-D2-W167-S2",
   "IRPT_DASHBD-D2-W167-S8",
   "IRPT_DASHBD-D2-W167-S9",
   "IRPT_DASHBD-D2-W168-S1",
   "IRPT_DASHBD-D2-W164-S1",
   "IRPT_DASHBD-D2-W164-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): judgment criteria are graded at L9, never self-graded; every ARMED row leaves ARMED only on its owner's disarm or a measured read.",
  "world_is": "All round-105 orders complete and the direct act recorded (disclosure NOT FOUND; Andrew's call a252). Everything LOCAL: renders private, portal branches unpushed, nothing written to AWS. The view now reads the builder's kind. One cross-table pair and the allocation-chart reason remain wrong in client words.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's read of 15 of 15 pages, fwd21_sample_r105/pages/r105_3/ (private; no figure copied)",
    "this seat's re-run 2026-10-14T14:0xZ: DB105-1-AC1, DB105-2-AC1, DB105-3-AC1 PASS",
    "investigation rows D2-S29, D2-S31 (owner disarms and rulings), D2-W158-S1, -S4, -S6, D2-W164-S1..S3, D2-W167-S1..S9, D2-W168-S1",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND105_B_DRAIN_END_20261014.md blob 94d5e1d21e (msg 7679)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_DASHBD_ROUND_105_L9_GRADE_20261014.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Four ARMED rows disarmed by their owners' rows, those rows themselves, a ruled masking row, a removed route, and readings. Rows that shape the remedy cell, the candidate or the applies are held."
 }
]
```
