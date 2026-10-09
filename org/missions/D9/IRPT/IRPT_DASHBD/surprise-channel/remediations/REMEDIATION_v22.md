# IRPT_DASHBD -- round 46 remediations

<sweep_watermark>2026-10-09T14:00Z</sweep_watermark>

Graduated at round 46's L8 (ADJUDICATION_v28.md), round label v47: D2-W69-S2, OPEN.

```json
[
  {
    "id": "IRPT_DASHBD-D2-W69-S2",
    "project": "IRPT_DASHBD",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The DB-b-91 status record is dropped only by a scheduled fire that lands the day; an explicit backfill that lands a refused lots day leaves its statement in the object, so Branch A's 'the status record drops that day' holds on the scheduled path only.",
    "evidence": [
      "investigation row IRPT_DASHBD-D2-W69-S2",
      "IRPT_DASHBD round 46 drain-end (2.0.0_SA_COO~D2 msg 3404; DB-b-94 drained @caaf9b5cc7; packet deliverables/0.9.0_WK_IRPT_DASHBD~69/NEVER_WIDEN_PACKET_R44_RELEASE.md)"
    ],
    "remedy": "Drop the lots_not_computed status record on ANY successful landing of the day (scheduled fire or explicit backfill), and test the backfill branch, before the R44 release.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v47",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v47"
    },
    "closed": false
  }
]
```
