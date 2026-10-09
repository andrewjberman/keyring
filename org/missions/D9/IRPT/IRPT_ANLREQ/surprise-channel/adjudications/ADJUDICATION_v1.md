# IRPT_ANLREQ -- round 1 L8 adjudication (FWD-1, the thread)

<sweep_watermark>2026-10-09T07:06Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~07:1xZ. The channel's first compile. L8 inputs: org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND1_L8_COMPILE.md @afef75b757 (2.0.0_SA_COO~Y2 msg 2753); TICKET packet L8_PACKET.TICKET.R1.md @5d3b1a6616 (msg 2706).
9 of 9 orders complete, 0 judgment criteria, MAY-CLOSE. 17 rows dismissed below; 13 graduate OPEN in `remediations/REMEDIATION_v1.md`,
two of them ARMED (D2-W41-S1 and D2-W11-S1), each with its disarm owner. TO-APPLY-V12's AC2 grade is owed when its after-reads land.

**For the round-1 analysis:**
1. **The thread is code-complete and not live.** Four releases are owed, in order: ~Y2 irpt-status (with the stale packaged schema,
   W1-S2), ~V2 opal-ticket-api, ~T2 commentary.tf (I3, I4, and the zip's keys.py closure, W41-S1/W41-S9), then ~G2's resident release
   with the packager mint (W62-S1/S2).
2. **Hop 9 is partial:** only the Report opens from the ticket; the branded PDF has a server reader and no portal reader (D2-S1).
3. **A durability gap at hop 5** (W61-S1): a crash between the READY write and the I3 send loses the send, and the redelivery path
   treats READY as done. FWD-4 ('never silently stops') needs that closed.
4. **Retention now admits one service writer** (svc-commentary, ANALYSIS_COMMENTARY, tenant-bound) @3fc99be70f. It is served only at
   ~T2's release; its pair should name it.

```json
[
  {
    "id": "IRPT_ANLREQ-C-S1",
    "project": "IRPT_ANLREQ",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T07:06:20Z",
    "one_line": "Round 1 rows dismissed: D2-S2 with its disposition D2-S3 (two READY triggers: H1 withdrawn by CTO @19c5067e12, hop 4b is I3 alone); D2-W1-S1 (the request schema admits ticket_id, AMENDMENT 1 @5be2acd7cc); D2-W41-S3/S4 (owner never read; the one-argument test reader kept green -- both as built, proofs ok); D2-W41-S6/S7/S8 with their dispositions S12/S13/S14 (retention admits the one named writer, the package reader entry, the store-backed queue test -- all landed @3fc99be70f, measured an ancestor of HEAD; the packet's 'asked of the CTO' for S6 is stale); D2-W41-S10 (the DRAFT's bytes shape is now written); D2-W41-S11/S16 with S15 (the AR-t-13 cell id, registered by AMENDMENT 7; round-close now reads proof_ok 9 of 9); D2-W11-S3 (gen-wire root resolution from a linked worktree: tooling); D2-W63-S1 (order wording against poll_once, resolved as built).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_ANLREQ-D2-S2",
      "IRPT_ANLREQ-D2-S3",
      "IRPT_ANLREQ-D2-W1-S1",
      "IRPT_ANLREQ-D2-W41-S3",
      "IRPT_ANLREQ-D2-W41-S4",
      "IRPT_ANLREQ-D2-W41-S6",
      "IRPT_ANLREQ-D2-W41-S7",
      "IRPT_ANLREQ-D2-W41-S8",
      "IRPT_ANLREQ-D2-W41-S10",
      "IRPT_ANLREQ-D2-W41-S11",
      "IRPT_ANLREQ-D2-W41-S12",
      "IRPT_ANLREQ-D2-W41-S13",
      "IRPT_ANLREQ-D2-W41-S14",
      "IRPT_ANLREQ-D2-W41-S15",
      "IRPT_ANLREQ-D2-W41-S16",
      "IRPT_ANLREQ-D2-W11-S3",
      "IRPT_ANLREQ-D2-W63-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "9 of 9 orders complete; the thread is NOT live (four releases owed through 0.7.0_AE_CloudOps~DELL2). this seat's reads ~07:1xZ: round-close-check --round 1 MAY-CLOSE (9 orders, proof_ok 9); 3fc99be70f (retention admits svc-commentary on reserve only, family ANALYSIS_COMMENTARY, tenant-bound, negative control fails at retention.py:97 on the old bytes) is an ancestor of box/dell2 HEAD.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S2, D2-S3, D2-W1-S1, D2-W41-S3, D2-W41-S4, D2-W41-S6, D2-W41-S7, D2-W41-S8, D2-W41-S10, D2-W41-S11, D2-W41-S12, D2-W41-S13, D2-W41-S14, D2-W41-S15, D2-W41-S16, D2-W11-S3, D2-W63-S1",
        "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND1_L8_COMPILE.md @afef75b757 (2.0.0_SA_COO~Y2 msg 2753); TICKET packet L8_PACKET.TICKET.R1.md @5d3b1a6616 (msg 2706)",
        "this seat's reads ~07:1xZ: round-close-check --round 1 MAY-CLOSE (9 orders, proof_ok 9); 3fc99be70f (retention admits svc-commentary on reserve only, family ANALYSIS_COMMENTARY, tenant-bound, negative control fails at retention.py:97 on the old bytes) is an ancestor of box/dell2 HEAD"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Resolved by amendment or landed commit (measured), as built with proofs ok, a disposition record, or tooling."
  }
]
```
