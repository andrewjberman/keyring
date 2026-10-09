# NFRA_GATSCP -- round 3 remediations (dell1)

<sweep_watermark>2026-10-09T15:30Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T15:30:00Z. Graduated at ADJUDICATION_v4: 1 row, INERT.

```json
[
  {
    "id": "NFRA_GATSCP-D1-W13-S1",
    "project": "NFRA_GATSCP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "GS-f-6's refusal exempts a conflicted path resolved by keeping the first parent's bytes; a path reset in BOTH the index and the working copy (e.g. checkout HEAD -- path) reads as a keep-ours and is not caught, so one route to D1-S5's partial commit stays open.",
    "evidence": [
      "investigation row NFRA_GATSCP-D1-W13-S1",
      "org/missions/D0/NFRA/NFRA_GATSCP/deliverables/2.0.0_SA_COO~N1/TRACE_round3.md 'Defects on the way'"
    ],
    "remedy": "Rule whether the narrower case needs a guard (e.g. compare against the staged list recorded before resolution) or is accepted with the limit stated. Close when: the ruling is recorded",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  }
]
```
