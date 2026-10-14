# IRPT_BCKEND: CVO adjudication, round 194 (workstream ~P)

<sweep_watermark>2026-10-14T14:28Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~DELL2`, 2026-10-14T14:28Z, on msg 7684 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_194_P_DRAIN_END_20261014.md`). One order (IB-pr-538, packet v2 of the release as the full pin mint), read-only, 3 of 3 PASS re-run here on HEAD; no judgment criterion; nothing minted or signed. 3 rows dismissed below. Kept OPEN, load-bearing for the signing: D2-W383-S2, -S3 (the live holdings_snapshot.py matches no commit and differs per firm, so the signed counts measure the cash rule alone) and D2-S170 (the release carrier). D2-S172 (this seat's AC3 instrument row) stays open with the issuer. ARMED unchanged: D2-W349-S1, D2-W361-S1, D2-W348-S2, D2-W368-S2, D2-S158.

```json
[
 {
  "id": "IRPT_BCKEND-D2-C-S3",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-14T14:28:00Z",
  "one_line": "Round 194 ~P. IB194-1-AC1..AC3 PASS re-run here. Packet v2 characterizes 73 moved members (24/25/24); the trading calendar's holidays over 2026-10-01..2027-12-31 and the next three T-1 dates are identical (round 193's '3.5 months old' is the code, not the dates); write addresses are equal; the pin re-measure equals the signed counts. Not signable as is: the live producer matches no commit, so a full pin mint moves the producer beyond the two signed changes, and the signed counts do not measure the served-output delta of live code against the pin. Dismissed (3): D2-W383-S1 (BLOCKING: the issuer's check read the stop evidence's flat path lists as pairs; repaired @90a0952879; the re-grade @7b46d4a24d changes 3 leaves of 86, all in the AC1 row, verified here), D2-W383-S4 (rows_written means data rows, confirmed), and the issuer's disposition row D2-S173. Kept OPEN: D2-W383-S2, -S3, D2-S170.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W383-S1",
   "IRPT_BCKEND-D2-W383-S4",
   "IRPT_BCKEND-D2-S173"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row of the round is dispositioned before the slug; never-widen signs a measured blast radius, not a static reading.",
  "world_is": "IB-pr-538 is complete; packet v2 exists with both halves UNSIGNED. The issuer runs a live-against-pin differential on the same pinned inputs before signing the COO half, and recommends it as a round-195 cell with its own check. The release apply is not cut.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-14T14:2xZ on box/dell2 HEAD: the three IB-pr-538 invocations print IB194-1-AC1 PASS, IB194-1-AC2 PASS, IB194-1-AC3 PASS",
    "semantic diff of the IB-pr-538 proof instance across 7b46d4a24d: 3 changed leaves of 86 (acceptance[0] output_evidence, status, status_reason)",
    "investigation rows D2-W383-S1..S4, D2-S173, D2-S170",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_194_P_DRAIN_END_20261014.md (msg 7684)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A BLOCKING check defect repaired and its re-grade verified as limited to its row; a confirmed meaning; and the issuer's disposition record. The signing finding stays open."
 }
]
```
