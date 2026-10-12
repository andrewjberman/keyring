# IRPT_ANLREQ: CVO adjudication -- row D2-S59 disarmed

<sweep_watermark>2026-10-11T20:18Z</sweep_watermark>

By `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T20:18:57Z. Row D2-S60, by the disarm owner, disarms D2-S59.

```json
[
  {
    "id": "IRPT_ANLREQ-C-S14",
    "project": "IRPT_ANLREQ",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T20:18:57Z",
    "one_line": "Row D2-S60 is dismissed as a disarm record: the branch that removed the ticket page's fallback is withdrawn as a candidate and the removal is re-cut after release 5's after-reads, as the CTO ruled (msg 5646). Row D2-S59's clocks are advanced in REMEDIATION_v6 by this commit.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_ANLREQ-D2-S60"
    ],
    "spec_asserts": "CLAUDE.md section 2: an ARMED hazard disarms via the row's disarm owner.",
    "world_is": "The disarm is the owner's statement in row D2-S60, filed by 2.0.0_SA_COO~Y2; this seat did not read the portal branch's state.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row D2-S60",
        "CTO msg 5646"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm record by the row's disarm owner."
  }
]
```
