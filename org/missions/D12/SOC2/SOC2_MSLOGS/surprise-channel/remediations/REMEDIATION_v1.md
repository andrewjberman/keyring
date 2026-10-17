# SOC2_MSLOGS -- round 1 remediations (dell1)

<sweep_watermark>2026-10-17T06:08:31Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T06:08:31Z. Graduated at ADJUDICATION_v1 (C-S3): 4 rows, owner 2.0.0_SA_COO~S1.

```json
[
  {
    "id": "SOC2_MSLOGS-D1-W2-S3",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The door's bronze audit_records prefixes are hand-typed in handler.py, and the naming gate WARNs on them.",
    "evidence": [
      "investigation row SOC2_MSLOGS-D1-W2-S3",
      "adjudication row SOC2_MSLOGS-D1-C-S3 (ADJUDICATION_v1)"
    ],
    "remedy": "The prefixes come from lib/opal_naming address() output (rule 30). Close when: handler.py holds no hand-typed bronze prefix and the naming gate reads clean on it.",
    "owner": "2.0.0_SA_COO~S1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~S1",
      "round": "v1"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~S1",
      "at": null
    }
  },
  {
    "id": "SOC2_MSLOGS-D1-W1-S1",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "data/m365_metadata/README.md still describes filter.py and population.json, which round 1 deleted.",
    "evidence": [
      "investigation row SOC2_MSLOGS-D1-W1-S1",
      "adjudication row SOC2_MSLOGS-D1-C-S3 (ADJUDICATION_v1)"
    ],
    "remedy": "The README describes the raw, every-account collector. Close when: the README names neither deleted file.",
    "owner": "2.0.0_SA_COO~S1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~S1",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "SOC2_MSLOGS-D1-W5-S1",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "population.json references and main.tf comments still say eight accounts.",
    "evidence": [
      "investigation row SOC2_MSLOGS-D1-W5-S1",
      "adjudication row SOC2_MSLOGS-D1-C-S3 (ADJUDICATION_v1)"
    ],
    "remedy": "The text says every account in the tenant. Close when: no eight-account statement remains in the project's live text.",
    "owner": "2.0.0_SA_COO~S1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~S1",
      "round": "v1"
    },
    "closed": false
  },
  {
    "id": "SOC2_MSLOGS-D1-W7-S1",
    "project": "SOC2_MSLOGS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "data/m365_metadata/scripts/app/RUNBOOK.md says the Entra sign-in feed is not subscribed; it is.",
    "evidence": [
      "investigation row SOC2_MSLOGS-D1-W7-S1",
      "adjudication row SOC2_MSLOGS-D1-C-S3 (ADJUDICATION_v1)"
    ],
    "remedy": "The RUNBOOK names the four subscribed content types. Close when: the RUNBOOK matches the live subscription list.",
    "owner": "2.0.0_SA_COO~S1",
    "round": "v1",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~S1",
      "round": "v1"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
