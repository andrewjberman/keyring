# IRPT_BCKEND: CVO adjudication, round 180 (workstream ~P)

<sweep_watermark>2026-10-13T15:46Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T15:46:00Z, on msg 7033 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_180_P_DRAIN_END_20261013.md`). One read-only order, no judgment criterion. account_id is LIVE
end to end on the builder side (7,639 of 7,640 served ACCOUNT nodes; 0 before the release). 2 rows dismissed below; 1 graduates in
`remediations/REMEDIATION_v55.md`. Still ARMED where they stand: D2-W361-S1 (v53), D2-W348-S2 (v48).

```json
[
 {
  "id": "IRPT_BCKEND-C-S364",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T15:46:00Z",
  "one_line": "Round 180 (~P). Dismissed: D2-W364-S2 (ARMED; publication.py caps selected part reads at 64 and refuses a full-firm read of the 200-part 49F publication; ruled a design bound by the issuer, since the serving entry points read only the selected accounts' parts and no serving path makes a full-firm read; disarm recorded), D2-S137 (the issuer's disposition record). Graduates: D2-W364-S1 (the directory's two homes).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W364-S2",
   "IRPT_BCKEND-D2-S137"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "TO-IB-pr-514 is complete (order file read; merge ce0bb315af on HEAD). The served 49F snapshot built on the new package carries account_id on 7,639 of 7,640 ACCOUNT nodes, all in the landed directory; the pre-release snapshot carries it on 0 of 7,634. The account_id line is live end to end on the builder side.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W364-S2, D2-S137",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_180_P_DRAIN_END_20261013.md (msg 7033)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A read bound ruled by design, and a disposition record."
 }
]
```
