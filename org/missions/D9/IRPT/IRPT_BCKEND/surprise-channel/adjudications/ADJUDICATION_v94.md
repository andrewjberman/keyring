# IRPT_BCKEND: CVO adjudication, round 193 (workstream ~P)

<sweep_watermark>2026-10-14T13:42Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~DELL2`, 2026-10-14T13:42Z, on msg 7662 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_193_P_DRAIN_END_20261014.md` @b18f769b46). Three orders: IB-pr-537 and IB-pr-536 complete, IB-pr-535 (the release) STOPPED at its own signed digest gate and cancelled; nothing minted or applied. No judgment criterion. Re-run here on HEAD: IB193-3-AC1..AC3 PASS, IB193-2-AC1 and AC2 PASS, IB193-2-AC3 FAIL on the instrument only (new row D2-S172: the check diffs base..HEAD; at the worker tip the delta is exactly the record's two paths). 6 rows dismissed below, D2-W374-S1 (ARMED) among them on Andrew's record. D2-S170 stays OPEN: it carries the packet re-cut into round 194. Still ARMED, unchanged: D2-W349-S1, D2-W361-S1, D2-W348-S2, D2-W368-S2, D2-S158.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S2",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-14T13:42:00Z",
  "one_line": "Round 193 ~P. Dismissed (6): D2-S169 (the 2026-10-09 kill cause UNREADABLE: host stopped, no memory metric retained; recorded, nothing left to read), D2-W382-S1 (BLOCKING: the issuer's AC2 mutant layout, repaired @751632840a; AC2 PASS re-run here), D2-W382-S2 (same root), D2-W382-S3 (a naming WARN on the literal 49financial, which the one-firm bypass is by order), D2-W374-S1 (ARMED: the WARN-only client-data check on dell2 is deliberate by Andrew's record ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME and the CTO's msg 7618), and the issuer's disposition row D2-S171. Two record defects noted, not rows: D2-S171 says AC1..AC3 PASS 'on the landed trees', true of the worker tree only (D2-S172); the re-grade commit 7dae6e5467 says 'nothing else in the instance changes' but also deletes both declared_exclusions (the AC2 one and 'bundle re-mint, AWS upload, apply and deploy of the bypass'), 8 leaf changes of 86. Kept OPEN: D2-S170 (the digest gate: a pin mint moves 19/21/20 members; the live bundles carry a trading calendar matching a 2026-06-26 commit), and the new D2-S172.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-S169",
   "IRPT_BCKEND-D2-W382-S1",
   "IRPT_BCKEND-D2-W382-S2",
   "IRPT_BCKEND-D2-W382-S3",
   "IRPT_BCKEND-D2-W374-S1",
   "IRPT_BCKEND-D2-S171"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row of the round is dispositioned on grounded evidence before the slug; an ARMED row leaves ARMED only on a measured read or a recorded ruling.",
  "world_is": "Round 193 is terminal (round-close-check --workstream ~P MAY-CLOSE, orders 3). The release did not run: its digest gate stopped it, as signed. The bypass is built at HEAD and in no bundle. The packet (IB-pr-532) must be re-cut before any mint, on the CTO's round-194 ruling; the issuer recommends characterizing the ~20 moved members and signing the full pin mint.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-14T13:3xZ on box/dell2 HEAD: p193_cells.py IB193-3-AC1, -AC2, -AC3 PASS; IB193-2-AC1, -AC2 PASS; IB193-2-AC3 FAIL (row D2-S172)",
    "git diff --name-only 411bde7479..db28643558 (the worker tip): exactly the record's two changed_paths",
    "semantic diff of the IB-pr-536 proof instance across 7dae6e5467: 8 changed leaves of 86 (acceptance[1] status, status_reason, denominator, output_evidence; declared_exclusions[0..1] removed)",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME.md; CTO msg 7618 (cited by D2-S171)",
    "investigation rows D2-S169, D2-S170, D2-S171, D2-S172, D2-W382-S1..S3, D2-W374-S1",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_193_P_DRAIN_END_20261014.md @b18f769b46 (msg 7662)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An unreadable cause recorded; a BLOCKING check defect repaired and re-run; a same-root reading; a WARN the order makes by design; an ARMED row whose standing Andrew ruled; and the issuer's disposition record. The load-bearing finding (D2-S170) and the instrument row (D2-S172) stay open."
 }
]
```
