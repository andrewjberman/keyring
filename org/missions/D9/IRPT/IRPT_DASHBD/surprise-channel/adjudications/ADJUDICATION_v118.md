# IRPT_DASHBD: CVO adjudication, round 116 (workstream F-SHIP, ~F2): the filled-report export wire in the server's names

<sweep_watermark>2026-10-16T00:58Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~IRPT`, 2026-10-16T00:58Z, on msg 8821 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R116_F.md` @dbf56b0a3d, blob b246bcd7ce), a packet written after the issuer's close at the CTO's round-119 ruling 5; graded by this lane under rule 5 of `CTO_RULING_DELL2_IRPT_DASHBD_FOUR_WORKSTREAMS_AT_ROUND_114_20261015.md` (CTO msg 8009). Not B-49F's or B-IN's round 116. One order, TO-DB-f-505 (LOCAL, direct act; worker ~505; issuance bdf27dff29, drained @50ffe7f3b6). No judgment criterion. Re-run: DBF116-1-AC1 and AC2 FAIL on the landed tree (the portal code is only on the candidate) and PASS on a scratch root with a detached portal worktree at the round's candidate head e23ddb8e34 (removed after). 2 of 2 PASS on the target tree; proof VALID; round-close MAY-CLOSE. No remediation row.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S55",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T00:58:00Z",
  "one_line": "Round 116 F-SHIP (~F2): the page's export sends filled_report_source {source_kind: filled_report, client_id} only, per the CTO's ruling on call f50a (the server pins at submit). 2 of 2 PASS on the candidate tree. NOTHING PROMOTED WHILE UNSEEN: the candidate heads of rounds 116-118 (portal e23ddb8e34, 0d58fe2c43, 65f2e5430b) are each NOT an ancestor of origin/DEV (d6fd0684) or origin/PROD (e0e69da7), and no remote ref contains them (git -C portal merge-base --is-ancestor; branch -r --contains; fetched 2026-10-16T00:5xZ). No client-facing page change reached DEV or PROD, so Andrew's word was never needed. D2-W505-S1 (BLOCKING: the server's parse_filled_report_source demanded version_id, sha256 and size and would refuse a client-only body) is DISPOSED BY THIS SEAT, resolved in REPO CODE. At HEAD, retained_export.freeze_filled_report calls server_pinned_body(body, reader) BEFORE parse_filled_report_source (retained_export.py:450-452), so the server fills the pin from its own read. The submit's PATH C calls freeze_filled_report (IB-pr-563 @608495b0ed, IB-pr-566 @c1b48c458a, ~P2's lane). Whether that server code is deployed is NOT read here; it is ~P2's apply. Until it is, a client-only export would still be refused by a server running older code. The round closed unseen by a CVO, and is graded here after the fact.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W505-S1"
  ],
  "spec_asserts": "Spine L9/L10: every terminal round is graded by the CVO before close; a criterion is re-run on the tree it targets; a client-facing page reaches PROD only on Andrew's word.",
  "world_is": "The page's client-only export wire is in an unpushed candidate. The server code that accepts it is in the repo, with its deployment not read here. FWD-21's export path is not live.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-16T00:5xZ: DBF116-1-AC1, AC2 FAIL on the landed tree; PASS on a detached portal worktree at e23ddb8e34; proof VALID (~505); round-close --round 116 --workstream ~F2 MAY-CLOSE",
    "git -C portal: e23ddb8e34 not in origin/DEV d6fd0684 nor origin/PROD e0e69da7; no remote ref contains it",
    "infra/aws/lambda/investor-reporting/export/retained_export.py:344-360 (parse), :443-452 (freeze calls server_pinned_body first); commits 608495b0ed, c1b48c458a",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/R116_CLOSE_F_SHIP.md line 11",
    "investigation row D2-W505-S1",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~F2/L8_PACKET_R116_F.md blob b246bcd7ce (msg 8821)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "The BLOCKING server-premise row is resolved in repo code by ~P2's server pin. Its deploy is ~P2's apply and is not graded here."
 }
]
```
