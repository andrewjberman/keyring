# IRPT_DASHBD: CVO adjudication, round 108

<sweep_watermark>2026-10-14T16:55Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~DELL2`, 2026-10-14T16:55Z, on msg 7758 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND108_B_DRAIN_END_20261014.md`, blob 9705f1a715). No judgment criterion. DB108-1-AC1 and DB108-2-AC1 re-run here: 2 of 2 PASS. 6 rows dismissed below, 2 ARMED among them on their owner's row D2-S34. Held: D2-S34 (the carrier of the Orion client-grain fork, for the CTO), D2-W171-S3 (an Eclipse table 5 days behind its siblings) and D2-W171-S4 (the Orion backfill guard reads FAIL with four alien objects, backfill_complete false). The last two are upstream facts that any Inflection read must state.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S5",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-14T16:55:00Z",
  "one_line": "Round 108 (Inflection adapter first tables; two coverage reads). DB108-1-AC1, DB108-2-AC1 PASS re-run here. Dismissed (6): D2-W172-S1 (ARMED; Orion transactions and performance partitions are cumulative, read newest-only; disarmed by owner in D2-S34), D2-W172-S3 (ARMED; Orion performance is client-keyed; disarmed by owner in D2-S34, the fork carried by D2-S34), D2-W172-S2 (reinvested income classed Internal, a method note), D2-W171-S1 (no separate account roster, read), -S2 (client key equals household key for Inflection, read), -S5 (the naming gate refuses a typed prefix; the adapter derives its grant from the registry row, as the gate intends). Held: D2-S34, D2-W171-S3, D2-W171-S4.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W172-S1",
   "IRPT_DASHBD-D2-W172-S3",
   "IRPT_DASHBD-D2-W172-S2",
   "IRPT_DASHBD-D2-W171-S1",
   "IRPT_DASHBD-D2-W171-S2",
   "IRPT_DASHBD-D2-W171-S5"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row of the round is dispositioned on grounded evidence before the slug.",
  "world_is": "Both round-108 orders complete; both merges on origin box/dell2; nothing written to AWS. Inflection has an account dimension (980 accounts, 320 households) built in a private dry run, Orion returns include dividends, Eclipse lots are absent (NO_LOTS). No Inflection gold table is written and no account-grain return exists: Orion performance is client-keyed (the fork in D2-S34). FWD-2 and FWD-21 are not met.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-14T16:5xZ: DB108-1-AC1 PASS, DB108-2-AC1 PASS",
    "investigation rows D2-W171-S1..S5, D2-W172-S1..S3, D2-S34",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND108_B_DRAIN_END_20261014.md blob 9705f1a715 (msg 7758)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Two ARMED method facts disarmed by their owner and carried into the next order faces, one method note, and three readings. The design fork and two upstream data facts are held."
 }
]
```
