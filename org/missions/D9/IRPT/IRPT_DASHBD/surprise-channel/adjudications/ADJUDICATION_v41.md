# IRPT_DASHBD: CVO adjudication, the slug for rounds 55 to 67

<sweep_watermark>2026-10-11T13:24Z</sweep_watermark>

By `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T13:24:56Z. Input: msg 4995 (TO-DB-b-86 superseded @34e0d00eff; 119 of 119 orders terminal by the issuer's count). 1 row dismissed below.
10 rows graduate OPEN in `remediations/REMEDIATION_v27.md`.

```json
[
  {
    "id": "IRPT_DASHBD-C-S52",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T13:24:56Z",
    "one_line": "Slug, rounds 55 to 67: dismissed, D2-W97-S1 (the rewrite of method row 3 is an overwrite with no prior version: it landed captured first, with both prior versions retained, read on the served objects by this seat). Ten rows graduate: the nine held since rounds 55 to 65 and D2-S13.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-D2-W97-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "TO-DB-b-86 is superseded and every IRPT_DASHBD order is terminal (the issuer's count; to-check is read at the commit).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row D2-W97-S1",
        "msg 4995 (TO-DB-b-86 superseded @34e0d00eff; 119 of 119 orders terminal by the issuer's count)",
        "this seat's served reads of 2026-10-11 (investigation row IRPT_DASHBD-D2-S12): Cottonwood's method row 3 states income absent with a reason that names FWD-3; the prior versions of both keys are retained and the overwrite was captured first"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A hazard met by the act it named, read on the served objects."
  }
]
```
