# IRPT_BCKEND: CVO adjudication, round 189 (workstream ~P)

<sweep_watermark>2026-10-14T03:42:08Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-14T03:42:08Z, on msg 7496 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_189_P_DRAIN_END_20261014.md`). Two orders, 3 of 3 PASS each, no judgment
criterion; nothing applied. This seat re-ran IB189-1-AC1 to AC3: all PASS. 7 rows dismissed below; nothing graduates while IB-pr-497 is
parked. For the CTO: the cash rule's blast radius is 844 nodes, and a fallback-served cash fund stays Fixed Income (cross-page).

```json
[
 {
  "id": "IRPT_BCKEND-C-S373",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-14T03:42:08Z",
  "one_line": "Round 189 (~P), no judgment criterion. Dismissed: D2-S161 (FDRXX resolves on the canonical branch: 757 nodes on Inflection's 2026-10-12 snapshot), D2-S160 (the read of Cottonwood's lost account: missing from the allocations feed since 2026-10-09, not closed, not re-keyed; carried by D2-S158, ARMED with the CTO, and the directory-exemption repair the CTO puts in round 190), D2-S162 (the dispositions), D2-W375-S1 to -S4 (Branch A named code not yet in the tree; fallback identifiers withheld by shape; 101 symbol-less nodes, none a mover; the producer's deploy and schedule NOT read: the next round's census cell before either half is signed). HELD with their owners, not adjudicated: D2-S158 (ARMED, the CTO: Cottonwood's IR holdings stale) and D2-W374-S1 (ARMED, the box manager: the commit-time client-data check is ABSENT on dell2; this seat's own commits print the same WARN). Stay open with the issuer: D2-S152, D2-S155, D2-S156, D2-S145 to -S147, D2-S150, D2-S153.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-S160",
   "IRPT_BCKEND-D2-S161",
   "IRPT_BCKEND-D2-S162",
   "IRPT_BCKEND-D2-W375-S1",
   "IRPT_BCKEND-D2-W375-S2",
   "IRPT_BCKEND-D2-W375-S3",
   "IRPT_BCKEND-D2-W375-S4"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "TO-IB-pr-527 and TO-IB-pr-528 are complete (order files read). The IR cash rule is BUILT, canonical-only, fallback untouched; the release packet is written with both halves UNSIGNED. Blast radius 844 nodes (49F 32, COT 38, INF 774). Cross-page fact for the CTO: a cash fund served by the fallback layer stays Fixed Income while the canonical branch serves Cash. The catalogue ledger is CLOSED; the export person-read is still owed. IB-pr-497 parked; IB-pr-456 waits on Andrew's PROD execution ID.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S160, D2-S161, D2-S162, D2-W375-S1, D2-W375-S2, D2-W375-S3, D2-W375-S4",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_189_P_DRAIN_END_20261014.md (msg 7496)",
    "this seat's run 2026-10-14T03:42 of IB189-1-AC1 to AC3 from TO-IB-pr-527: all PASS (107 tests pass and the change is confined; the rule acts on the canonical branch only, on a Cash sub only; one definition, one call); merges dff35d95da and e09575dde1 on HEAD. This seat's own commits on dell2 print the same client-data WARN W374-S1 names (the hashed account-id list absent)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Readings carried to the CTO's rulings and the next census cell; two ARMED rows held with their owners."
 }
]
```
