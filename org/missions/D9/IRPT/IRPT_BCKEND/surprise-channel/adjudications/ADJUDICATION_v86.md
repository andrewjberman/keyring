# IRPT_BCKEND: CVO adjudication, round 185 (workstream ~P)

<sweep_watermark>2026-10-13T23:42Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T23:42:00Z, on msg 7354 (`org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_185_P_DRAIN_END_20261013.md @a47c87446b`). Two orders, 3 of 3 PASS each, no judgment
criterion. WORLD act landed: irpt-ycharts-generate live at the new digest (this seat's read); the person-read of the catalogue is owed
(ledger open). 6 rows dismissed below; nothing graduates while IB-pr-497 is parked. The export-receipt release is built; its pair is unsigned.

```json
[
 {
  "id": "IRPT_BCKEND-C-S369",
  "project": "IRPT_BCKEND",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T23:42:00Z",
  "one_line": "Round 185 (~P), no judgment criterion. Dismissed: D2-W368-S1 (BLOCKING; the issuer's 0-mismatch rule written without reading the live zip, which already carries one; amended to the attribute rule @07380ba777); D2-W368-S2 (ARMED: served.py _handle_prospect passes profile_reader= to a constructor that takes none, latent in irpt-export-render because its operations never route to CREATE_INPUT, entry.py:447-455) and D2-S154 (ARMED, its disposition record): the same stale served.py pin class as D2-W349-S1, which stays ARMED with the issuer; folded there, and the issuer names that the same stale pin pair sits in other live functions that stage both files, not censused; D2-W368-S3 and -S5 (a source-map ledger that never names the function; one listed worktree absent, 54 of 55 read); D2-W368-S4 (the backfill premise: the store holds one receipt, it carries the field, branch none_needed). Stay open with the issuer: D2-S152 (the export-receipt root cause; its release IB-pr-519 is built and its pair UNSIGNED, the apply a later order), D2-S145 to -S147, D2-S150, D2-S153.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_BCKEND-D2-W368-S1",
   "IRPT_BCKEND-D2-W368-S2",
   "IRPT_BCKEND-D2-W368-S3",
   "IRPT_BCKEND-D2-W368-S4",
   "IRPT_BCKEND-D2-W368-S5",
   "IRPT_BCKEND-D2-S154"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "TO-IB-pr-519 and TO-IB-pr-520 are complete (order files read); apply bb381c308f, merges 85cd9597a4 and 295d98d389, COO half b667f38d96 and amendment 07380ba777 on HEAD. WORLD act landed: irpt-ycharts-generate live at the new digest (this seat's read). The served read is OWED: ledger irpt-ycg-catalogue-ultrashort-20261013 stays OPEN for a person's read; IB2's health proof shows 0 invocations since the apply, so it shows nothing broke, not that the new bytes served. The form's model checkboxes reorder for every firm. IB-pr-497 parked; IB-pr-456 waits on Andrew's PROD execution ID. Still ARMED with the issuer: W349-S1 (now carrying W368-S2), W361-S1, W348-S2.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W368-S1, D2-W368-S2, D2-W368-S3, D2-W368-S4, D2-W368-S5, D2-S154",
    "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_185_P_DRAIN_END_20261013.md @a47c87446b (msg 7354)",
    "this seat's read 2026-10-13T23:4xZ: lambda get-function-configuration irpt-ycharts-generate reads CodeSha256 xP47NQDnZNZ8Lui1XQKUxUtTMTasR8Cj/A1sQnRDZYY= (the signed digest per the packet), LastModified 2026-10-13T22:48:27Z"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An amended issuer rule, a latent ARMED defect folded into its own class's ARMED row, and readings."
 }
]
```
