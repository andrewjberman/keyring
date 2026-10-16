# IRPT_DASHBD: CVO adjudication, round 117 (workstream F-SHIP, ~F2): the avs benchmark members read by_row, pinned by a test

<sweep_watermark>2026-10-16T00:58Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T00:58Z, on msg 8821 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R117_F.md` @dbf56b0a3d, blob 446e3ee09a), a packet written after the issuer's close at the CTO's round-119 ruling 5; graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Not B-49F's or B-IN's round 117. One order, TO-DB-f-506 (LOCAL, direct act; worker ~506; issuance c8794f1232, drained @1c3ea59e4b). No judgment criterion. Re-run: DBF117-1-AC1 and AC2 FAIL on the landed tree and PASS on the candidate head 0d58fe2c43 (scratch root, removed after). 2 of 2 PASS on the target tree; proof VALID; round-close MAY-CLOSE. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S56",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T00:58:00Z",
  "one_line": "Round 117 F-SHIP (~F2): a test pins that the report model reads the sixteen avs benchmark members by_row per account (no source change). 2 of 2 PASS on the candidate tree. NOTHING PROMOTED WHILE UNSEEN: the candidate heads of rounds 116-118 (portal e23ddb8e34, 0d58fe2c43, 65f2e5430b) are each NOT an ancestor of origin/DEV (d6fd0684) or origin/PROD (e0e69da7), and no remote ref contains them (git -C portal merge-base --is-ancestor; branch -r --contains; fetched 2026-10-16T00:5xZ). No client-facing page change reached DEV or PROD, so Andrew's word was never needed. D2-S64's disarm by D2-S67 was graded GROUNDED in v84 and is not re-graded. D2-W506-S1 was accepted in v84. D2-W506-S2 (test.todo is not in the portal's bun:test typings, so typecheck failed; the todo became a comment at 0d58fe2c) is inert and accepted. The scalar case stays unpinned, and round 118 pins it.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W506-S2"
  ],
  "spec_asserts": "Spine L9/L10: every terminal round is graded by the CVO before close; a criterion is re-run on the tree it targets; a client-facing page reaches PROD only on Andrew's word.",
  "world_is": "The by_row reading is pinned by a test in an unpushed candidate. Nothing is promoted.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T00:5xZ: DBF117-1-AC1, AC2 FAIL on the landed tree; PASS at 0d58fe2c43; proof VALID (~506); round-close --round 117 --workstream ~F2 MAY-CLOSE",
    "git -C portal: 0d58fe2c43 not in origin/DEV nor origin/PROD; no remote ref contains it",
    "ADJUDICATION_v84 (S67, W506-S1)",
    "investigation row D2-W506-S2",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R117_F.md blob 446e3ee09a (msg 8821)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "One inert worker row. The by_row disarm was already graded in v84."
 }
]
```
