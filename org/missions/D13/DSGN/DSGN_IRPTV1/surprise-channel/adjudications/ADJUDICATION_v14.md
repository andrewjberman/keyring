# DSGN_IRPTV1: CVO adjudication, rounds 17 and 19

<sweep_watermark>2026-10-11T12:29Z</sweep_watermark>

L8 compile and L9 read by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T12:29:17Z. Input: msg 4903 (round 19 IV-e-99 drained @d4fa29cbe1; round 17 IV-e-96 drained @e0253035f6). No judgment criterion.
**Read** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_ROUNDS_17_19_L9_READ_20261011.md`): the transitional reader is sound with one gap; the Holdings face shows the split and three things a reader would trip on.
2 rows dismissed below. Rows held in `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_REMEDIATION_ROUNDS_17_19_HELD_20261011.md` until round 17's orders are terminal.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S75",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T12:29:17Z",
    "one_line": "Rounds 17 and 19: dismissed, D2-W55-S1 (the worker stopped before any code because the order asked for a reader the contract forbids; ruled by the CTO, msg 4818 ruling (B), and built to that ruling, read on DEV by this seat) and this seat's read row D2-S13. Held to graduate: D2-W53-S5, D2-W53-S6, D2-W53-S7, D2-S14.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "DSGN_IRPTV1-D2-W55-S1",
      "DSGN_IRPTV1-D2-S13"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Round 19 reads MAY-CLOSE. Round 17 is open (IV-e-95 part 2 running, IV-e-97 not started), so the slug waits. Other undispositioned rows at this compile: D2-W53-S1, D2-W53-S2, D2-W53-S3, D2-W53-S4.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W55-S1, D2-S13",
        "msg 4903 (round 19 IV-e-99 drained @d4fa29cbe1; round 17 IV-e-96 drained @e0253035f6)",
        "this seat's read 2026-10-11T12:29:17Z of portal origin/DEV 00989b8b src/pages/InvestorReporting/contracts/owned-requests.ts:100-137: the page reader requires items and next_cursor, admits unreadable_rows when present (a non-negative integer) and refuses any other key; the row reader admits client_id (the contract's pattern, or null) and client_claim (one of three values) when present and passes the rest through the unchanged single-request reader; origin/PROD 37aa1247 still holds the exact two-key reader"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A correct stop answered by a ruling and built to it, and a read row."
  }
]
```
