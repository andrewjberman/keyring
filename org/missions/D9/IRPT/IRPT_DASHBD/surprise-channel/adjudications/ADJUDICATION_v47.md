# IRPT_DASHBD: CVO adjudication, round 75

<sweep_watermark>2026-10-11T20:02Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T20:02:47Z. Input: msg 5720 (IRPT_DASHBD round 75 fully drained @fc42bbcab0; orders DB-b-141 and DB-b-142). No judgment criterion.
1 row dismissed below. 1 graduates OPEN in `remediations/REMEDIATION_v32.md`.

```json
[
  {
    "id": "IRPT_DASHBD-C-S58",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T20:02:47Z",
    "one_line": "Round 75, no judgment criterion: dismissed, D2-W115-S1 (at the cent 50 of 51 differing days reproduce by counting each transaction id once; the 51st holds an administrative expense the method keeps inside the return, confirmed by this seat in the code). Its one limit, that the shared code table's class for that row was not read, is carried on row D2-W113-S3, which stays OPEN. Graduates: D2-W114-S1.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-D2-W115-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "No IRPT_DASHBD order is open (this seat's count of the order files). Rows D2-W113-S2 and D2-W113-S3 stay OPEN in REMEDIATION_v31.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row D2-W115-S1",
        "msg 5720 (IRPT_DASHBD round 75 fully drained @fc42bbcab0; orders DB-b-141 and DB-b-142)",
        "this seat's read 2026-10-11T20:02:47Z of data/assets/scripts/gold/irpt_reporting/account_return_daily.py lines 698 to 717: the comment at 706 says an administrative fee is an expense of the account and stays inside the return, and the flow term at 713 to 717 takes EXTERNAL, FEE-MANAGEMENT and the two cross-account provenances only"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A result whose one limit is carried on an open row."
  }
]
```
