# IRPT_BCKEND: CVO adjudication, round 192 (workstream ~P)

<sweep_watermark>2026-10-14T12:22Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~DELL2`, 2026-10-14T12:22Z, on msg 7605 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_192_P_DRAIN_END_20261014.md` @a93d73e6e8). Two orders, read-only, 6 of 6 criteria PASS (re-run here), no judgment criterion; nothing applied. 9 rows dismissed below; nothing graduates while the release apply is uncut. The release is not ready on two conditions, carried to the CTO by the slug: Inflection's re-measure needs its own custody pin, and Cottonwood's newest candidate is one trading day behind T-1 for a 2026-10-14 fire. The 2026-10-08 replay route is the CTO's ruling.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S1",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-14T12:22:00Z",
  "one_line": "Round 192 ~P. IB192-1-AC1..AC3 and IB192-2-AC1..AC3 PASS, re-run here. Dismissed (9): D2-W380-S1 (Inflection's 2026-10-12 pin builds a 2026-10-09 candidate, so its REFUSED is the pin, not the release; carried as a release condition), -S2, -S3 (Cottonwood's newest candidate 2026-10-12 against T-1 2026-10-13; carried as a release condition); D2-W381-S1 (the 2026-10-09 fire was killed at about 310 s of an explicit 3600 s executionTimeout, so the round-191 wording 'killed on the SSM execution timeout' is wrong; the cause is unread), -S2 (the 2026-10-08 replay is refused by source_frontier_older; route the CTO's), -S3 (publish() does not tie the landed date to as_of; any bypass must carry that assertion), -S4 (the 2026-10-08 source is intact), -S5; and the issuer's disposition row D2-S168. Still ARMED where they stand, unchanged: D2-W374-S1, D2-W376-S1 (the commit-time client-data check is ABSENT on dell2; both round-192 workers logged it again), D2-W349-S1, D2-W361-S1, D2-W348-S2, D2-W368-S2 (2.0.0_SA_COO~P2), D2-S158 (the CTO, until the release's after-read).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W380-S1",
   "IRPT_BCKEND-D2-W380-S2",
   "IRPT_BCKEND-D2-W380-S3",
   "IRPT_BCKEND-D2-W381-S1",
   "IRPT_BCKEND-D2-W381-S2",
   "IRPT_BCKEND-D2-W381-S3",
   "IRPT_BCKEND-D2-W381-S4",
   "IRPT_BCKEND-D2-W381-S5",
   "IRPT_BCKEND-D2-S168"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "Both round-192 orders are complete and read-only. round-close-check --workstream ~P reads MAY-CLOSE; without the filter it reads REFUSED on workstream Y's TO-APPLY-Y77, whose proof file name lacks the order slug (carried to 2.0.0_SA_COO~Y2). The release pair IB-pr-532 is signed on both halves at one hash; the apply is not cut. The round's rows are all OBSERVATION and INERT; the ARMED rows named are carried unchanged from round 191.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-14T12:2xZ of org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r192/p192_cells.py: IB192-1-AC1, -AC2, -AC3, IB192-2-AC1, -AC2, -AC3 all PASS",
    "infra/aws/lambda/investor-reporting/holdings_refresh/refresh_dispatch.py:123 passes executionTimeout [EXECUTION_TIMEOUT] explicitly",
    "investigation rows D2-W380-S1..S3, D2-W381-S1..S5, D2-S168",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_192_P_DRAIN_END_20261014.md @a93d73e6e8 (msg 7605)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Read-only measurements that the release and the CTO's round-193 analysis carry as conditions: the Inflection pin, the Cottonwood business date, the corrected timeout mechanism, and the replay route with its as_of assertion. The issuer's disposition row is dismissed with them. No row is a live hazard from this round."
 }
]
```
