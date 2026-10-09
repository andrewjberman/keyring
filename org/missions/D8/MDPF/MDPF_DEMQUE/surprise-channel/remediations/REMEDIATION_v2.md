# MDPF_DEMQUE -- round 2 remediations

<sweep_watermark>2026-10-09T03:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T03:20:00Z. Graduated at ADJUDICATION_v2: 1 row, INERT.

```json
[
  {
    "id": "MDPF_DEMQUE-D1-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "lock.py locks a mapping as measured on min(3, available) agreeing trade dates with no agreement-rate floor: PONPX locks at 51 of 83 (61%).",
    "evidence": [
      "lock.py check() @8abd95ad3b; QA re-lock 2026-10-09T02:4xZ PONPX 51/83 LOCKED measured",
      "investigation row MDPF_DEMQUE-D1-S1 (2.0.0_SA_COO~Q1); CTO round-2 analysis msg 1520 ruling (2)"
    ],
    "remedy": "Build the CTO's floor: LOCK only when >= 90 pct of trade dates agree within 2 pct, otherwise the unresolved list. Close when: PONPX reads not-locked and on the unresolved list, and AMLP re-locks under the floor, on one scheduled draw",
    "owner": "2.0.0_SA_COO~Q1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Q1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Q1",
      "at": null
    },
    "closed": false
  }
]
```
