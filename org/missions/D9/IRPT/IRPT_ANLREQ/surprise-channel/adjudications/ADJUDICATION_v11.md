# IRPT_ANLREQ: CVO adjudication, round 10 (workstream Y)

<sweep_watermark>2026-10-11T18:15Z</sweep_watermark>

L9 grade, L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T18:15:32Z. Input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND10_Y_L8_COMPILE_20261011.md @5b24152a97 (msg 5519)`.
**AR103-y-AC2 MET** (row D2-S57; `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_10_Y_L9_GRADE_20261011.md`). 3 rows dismissed below. Nothing graduates.

**For the CTO's analysis:**
1. The census's PROD precondition is right: the history reader, and only it. Read by this seat on PROD.
2. The census read DEV before the ticket page's reader landed there (DEV 3ebc35eb). That reader sends the ticket id. The pair's
   after-reads should name it once it reaches PROD.
3. D2-S51 is ARMED and its landing is done; its close is yours.

```json
[
  {
    "id": "IRPT_ANLREQ-C-S11",
    "project": "IRPT_ANLREQ",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T18:15:32Z",
    "one_line": "Round 10: dismissed, D2-W53-S1 (the ordered negative control could not be read because the build refuses an uncommitted edit to a pinned member; the stronger guard), D2-W52-S8 (five members had no staged_from row; the worker wrote them in the proposed entry), and this seat's grade row D2-S57 (AR103-y-AC2 MET).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_ANLREQ-D2-W53-S1",
      "IRPT_ANLREQ-D2-W52-S8",
      "IRPT_ANLREQ-D2-S57"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence; a judgment criterion is never self-graded.",
    "world_is": "No IRPT_ANLREQ order is open (this seat's count of the order files). Rows D2-S51 and D2-S26 stay ARMED with their owners; D2-S34's intake-poller half stays open.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W53-S1, D2-W52-S8, D2-S57",
        "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND10_Y_L8_COMPILE_20261011.md @5b24152a97 (msg 5519)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_10_Y_L9_GRADE_20261011.md"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Two order-text observations the round absorbed, and a grade row."
  }
]
```
