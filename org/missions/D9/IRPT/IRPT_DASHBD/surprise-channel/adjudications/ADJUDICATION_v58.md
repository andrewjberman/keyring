# IRPT_DASHBD: CVO adjudication, round 94

<sweep_watermark>2026-10-13T23:24Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T23:24:00Z. Input: msg 7347 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND94_B_DRAIN_END_20261013.md @2d802bc2d5`; five orders, DB-b-174 to -178). No judgment
criterion. The household sample is built and private (this seat read its record). 26 rows dismissed below; 3 graduate to `2.0.0_SA_COO~D2` in
`remediations/REMEDIATION_v40.md`, 1 BLOCKING (FDRXX to CASH, round 96). FWD-21 is not graded: no hookup, one firm.

```json
[
 {
  "id": "IRPT_DASHBD-C-S69",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T23:24:00Z",
  "one_line": "Dismissed: Round 94 (five cells), with rounds 93 and 95 leftovers. Closed on owner records: D2-W145-S1 (disarmed by D2-S23: the CTO ruled both guard-state inferences stand, msg 7330) and D2-S23; D2-S22 (YTD from the first measured day, fixed in candidate cand/dell2/irpt-ytd-from-first-day-and-wider-export-modal @0307376564, a client-facing PROD change registered for Andrew's word, open call dell2-20261013T221411Z-3635); D2-S20 and D2-W144-S1 (the export modal width is in that candidate; the export UNEXPECTED is root-caused in IRPT_BCKEND-D2-S152, a stale receipt schema in irpt-export-render, round 185's first cell there); D2-W141-S1 (the household grouping, resolved by the granted crosswalk prefix: the sample was built); D2-W141-S3 and -S7 (activity and realized lots hold 4 trading days: windows re-sourced to account_return_daily in round 95, the activity backfill queued as IRPT_BCKEND-D2-S153); D2-W139-S1 and -S2 (round 93's direct act: account 5 reproduced for reason (1) only, and RULE_EXCL.md bounds no correction size; carried to the CTO's FWD-8 endpoint ruling on REMEDIATION_v39's D2-W138-S1); D2-S21 folded into D2-W144-S2, which graduates. Readings and limits stated in their records: D2-W140-S1 to -S4, D2-W141-S2, -S4, -S8, D2-W142-S1 to -S3, D2-W143-S1 to -S4, D2-W144-S3.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-S20",
   "IRPT_DASHBD-D2-S21",
   "IRPT_DASHBD-D2-S22",
   "IRPT_DASHBD-D2-S23",
   "IRPT_DASHBD-D2-W139-S1",
   "IRPT_DASHBD-D2-W139-S2",
   "IRPT_DASHBD-D2-W140-S1",
   "IRPT_DASHBD-D2-W140-S2",
   "IRPT_DASHBD-D2-W140-S3",
   "IRPT_DASHBD-D2-W140-S4",
   "IRPT_DASHBD-D2-W141-S1",
   "IRPT_DASHBD-D2-W141-S2",
   "IRPT_DASHBD-D2-W141-S3",
   "IRPT_DASHBD-D2-W141-S4",
   "IRPT_DASHBD-D2-W141-S7",
   "IRPT_DASHBD-D2-W141-S8",
   "IRPT_DASHBD-D2-W142-S1",
   "IRPT_DASHBD-D2-W142-S2",
   "IRPT_DASHBD-D2-W142-S3",
   "IRPT_DASHBD-D2-W143-S1",
   "IRPT_DASHBD-D2-W143-S2",
   "IRPT_DASHBD-D2-W143-S3",
   "IRPT_DASHBD-D2-W143-S4",
   "IRPT_DASHBD-D2-W144-S1",
   "IRPT_DASHBD-D2-W144-S3",
   "IRPT_DASHBD-D2-W145-S1"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "All 5 round-94 orders and round 95's one are complete (to-check.py --project IRPT_DASHBD: 0 active at 23:19Z). No judgment criterion. Not done, stated by the issuer: no hookup (nothing serves a FilledReport), FWD-21 not graded (one firm, 44 of 117 filled), Andrew's sample display not yet on a screen. No served byte moved.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S20, D2-S21, D2-S22, D2-S23, D2-W139-S1, D2-W139-S2, D2-W140-S1, D2-W140-S2, D2-W140-S3, D2-W140-S4, D2-W141-S1, D2-W141-S2, D2-W141-S3, D2-W141-S4, D2-W141-S7, D2-W141-S8, D2-W142-S1, D2-W142-S2, D2-W142-S3, D2-W143-S1, D2-W143-S2, D2-W143-S3, D2-W143-S4, D2-W144-S1, D2-W144-S3, D2-W145-S1",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND94_B_DRAIN_END_20261013.md @2d802bc2d5 (msg 7347)",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~141/HOUSEHOLD_SAMPLE_BUILD.json (this seat's read: 3 accounts by hashed ref, 44 of 117 filled, identity 30 of 30 within one dollar, window residual 16 of 16 kept apart, 590 reads, 0 writes, sample_kept_private true, no 8-digit account run)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Closed on owner records and rulings, carried to IRPT_BCKEND rows and the CTO's FWD-8 ruling, and readings."
 }
]
```
