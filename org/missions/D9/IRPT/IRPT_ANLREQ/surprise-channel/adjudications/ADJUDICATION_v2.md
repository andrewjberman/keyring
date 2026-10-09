# IRPT_ANLREQ -- round 2 L8 adjudication (make FWD-1 live)

<sweep_watermark>2026-10-09T12:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2; tree on box/dell2), 2026-10-09 ~12:0xZ. L8 inputs: org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND2_L8_COMPILE.md @b1615d2c97 (2.0.0_SA_COO~Y2 msg 3230); TICKET packet L8_PACKET.TICKET.R2.md @e0144145cb (msg 2881).
5 of 5 orders complete, 0 judgment criteria, MAY-CLOSE. 18 rows dismissed below; 7 round-1 remediation rows closed in place. Still OPEN
from round 1: W41-S1 (ARMED until ~T2's apply carries the proven built bytes), W41-S2, W41-S5, W41-S9, W62-S1, W62-S2 -- each on a
pending release. No new remediation row.

**For the analysis:** two of four releases are live; FWD-1's one graded journey follows ~T2's
commentary apply and ~G2's resident release with the packager mint.

```json
[
  {
    "id": "IRPT_ANLREQ-C-S2",
    "project": "IRPT_ANLREQ",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-09T12:00:27Z",
    "one_line": "Round 2 rows dismissed: D2-W2-S1 (a path-keyed re-pin over-reached into a second function's rows, corrected), D2-S4/S5 (the dispositions of W11-S1 and W11-S2), D2-S6 (BLOCKING: two of four package files had no reader -- AR-y-22 built the original-file reader and the commentary is read inside the PDF, per ADDENDUM 1), D2-W3-S1 with D2-W3-S4 (ARMED: the signer refused original keys; disarmed in-cell by AMENDMENT 2), D2-W3-S2 (the schema copy note, as built), D2-W3-S3 with D2-W3-S5 (owned_cells, fixed by AMENDMENT 2), D2-W65-S1 (the custody lane decided from the stored record, as built), D2-W22-S1 (the portal adapter lacked the original op; fixed on DEV, measured), D2-W22-S2/S3 (grant mechanics on a re-issued order; the order completed), D2-S7 (this seat's V12 grade), D2-S9 with D2-S11 (V12's field flipped by the issuer with a closure block), D2-S10 with D2-S12 (the F10 ledger is closed on box/dell2; only stale worker worktrees hold the old sentinel). Closed in place, clocks only: D2-W11-S1, W11-S2, W61-S1 (READY records i3_sent_at only after the send, AR-g-21), W62-S3 (I5'), W62-S4 (one I7 sample on both sides), D2-S1 (the portal opens the PDF and the original), W1-S2 (release 1 live).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_ANLREQ-D2-W2-S1",
      "IRPT_ANLREQ-D2-S4",
      "IRPT_ANLREQ-D2-S5",
      "IRPT_ANLREQ-D2-S6",
      "IRPT_ANLREQ-D2-W3-S1",
      "IRPT_ANLREQ-D2-W3-S2",
      "IRPT_ANLREQ-D2-W3-S3",
      "IRPT_ANLREQ-D2-W3-S4",
      "IRPT_ANLREQ-D2-W3-S5",
      "IRPT_ANLREQ-D2-W65-S1",
      "IRPT_ANLREQ-D2-W22-S1",
      "IRPT_ANLREQ-D2-W22-S2",
      "IRPT_ANLREQ-D2-W22-S3",
      "IRPT_ANLREQ-D2-S7",
      "IRPT_ANLREQ-D2-S9",
      "IRPT_ANLREQ-D2-S10",
      "IRPT_ANLREQ-D2-S11",
      "IRPT_ANLREQ-D2-S12"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "this seat's reads ~12:0xZ: round-close-check --round 2 MAY-CLOSE (5 orders); portal origin/DEV ce3b0cc4 src/pages/InvestorReporting/contracts/envelope.ts:198 adapts 'analysis-request-original' (W22-S1 fixed). Thread NOT live: release 1 (irpt-status BjUZjt2o + /original) and V12 are live; ~T2's commentary (after IB-pr-391) and ~G2's resident release with the packager mint are pending.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W2-S1, D2-S4, D2-S5, D2-S6, D2-W3-S1, D2-W3-S2, D2-W3-S3, D2-W3-S4, D2-W3-S5, D2-W65-S1, D2-W22-S1, D2-W22-S2, D2-W22-S3, D2-S7, D2-S9, D2-S10, D2-S11, D2-S12",
        "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND2_L8_COMPILE.md @b1615d2c97 (2.0.0_SA_COO~Y2 msg 3230); TICKET packet L8_PACKET.TICKET.R2.md @e0144145cb (msg 2881)",
        "this seat's reads ~12:0xZ: round-close-check --round 2 MAY-CLOSE (5 orders); portal origin/DEV ce3b0cc4 src/pages/InvestorReporting/contracts/envelope.ts:198 adapts 'analysis-request-original' (W22-S1 fixed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Dispositioned under amendment, built in the round, fixed and measured, or a record row."
  }
]
```
