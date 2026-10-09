# LGIC_BLANKFIX -- round 14 remediations (dell1)

<sweep_watermark>2026-10-09T14:47Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T14:47:00Z. Graduated at ADJUDICATION_v12: 2 rows, both INERT.

```json
[
  {
    "id": "LGIC_BLANKFIX-D1-W2-S9",
    "project": "LGIC_BLANKFIX",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A firm-bearing schedule passes the live naming gate only in the opal_name module form, where the gate grades 0 strings; the literal the list prints is refused 31 of 31 as a hand-kept firm-token carrier. 'gate_pass=31' therefore means 'no refusal', not 'graded and right'.",
    "evidence": [
      "investigation row LGIC_BLANKFIX-D1-W2-S9"
    ],
    "remedy": "Rule whether FWD-4 accepts module-form names as graded, or the gate learns to grade a builder call's resolved name. Close when: the ruling is recorded in the round-14 analysis",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v15"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "LGIC_BLANKFIX-D1-W2-S12",
    "project": "LGIC_BLANKFIX",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "place() now returns PATTERN for the 14 per-firm stored names; the gate self-test passes but the commit-gate's behaviour on a real PATTERN name is unmeasured.",
    "evidence": [
      "investigation row LGIC_BLANKFIX-D1-W2-S12"
    ],
    "remedy": "Exercise one commit carrying a per-firm PATTERN name through the live gate. Close when: that commit's gate output is recorded",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v15",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v15"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  }
]
```
