# IRPT_DASHBD: CVO adjudication, round 74

<sweep_watermark>2026-10-11T19:17Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T19:17:34Z. Input: msg 5629 (IRPT_DASHBD round 74 drained @f7b1cc4571, DB-b-140; record deliverables/0.9.0_WK_IRPT_DASHBD~113/UNREPRODUCED_18.json). No judgment criterion.
1 row dismissed below. 2 graduate OPEN in `remediations/REMEDIATION_v31.md`.

```json
[
  {
    "id": "IRPT_DASHBD-C-S57",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T19:17:34Z",
    "one_line": "Round 74, no judgment criterion: dismissed, D2-W113-S1 (the earlier downloads did not hold the fields needed, so one prefix was re-read by GETs only; the order allowed it). Graduate: D2-W113-S2 and D2-W113-S3. Row D2-W111-S1 stays OPEN: its cause is reported by one worker and was re-run by neither the issuer nor this seat.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-D2-W113-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "No IRPT_DASHBD order is open (this seat's count of the order files). This seat made no read of its own for this compile.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row D2-W113-S1",
        "msg 5629 (IRPT_DASHBD round 74 drained @f7b1cc4571, DB-b-140; record deliverables/0.9.0_WK_IRPT_DASHBD~113/UNREPRODUCED_18.json)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A read the order allowed."
  }
]
```
