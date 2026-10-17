# AMGT_RESAPP -- round 110 remediations (dell1)

<sweep_watermark>2026-10-17T17:28:16Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T17:28:16Z. Graduated at ADJUDICATION_v148 (C-S175): 2 rows.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W492-S3",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "WhatChangedPanel.tsx listReading returns JSON.stringify(value) for any non-list object, so a changed row whose served value is an object prints braces and quotes in its visible before and after cells; no harness check grades the visible object cell.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W492-S3",
      "adjudication row AMGT_RESAPP-D1-C-S175 (ADJUDICATION_v148)"
    ],
    "remedy": "Object values render as readable text in the visible cells, with a harness check on the visible cell. Close when: the check passes and a walk reads no raw-code finding on What Changed.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v110",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v110"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-S57",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The approval register has no fold-back verb: a PROD-into-DEV fold-back counts every DEV-only commit as overlap, so the bq-2 fold-back needed a one-time named waiver (106 shas).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S57",
      "adjudication row AMGT_RESAPP-D1-C-S175 (ADJUDICATION_v148)"
    ],
    "remedy": "A fold-back verb, or a ruling on how fold-backs register. Close when: either is on the record.",
    "owner": "portal manager (named by 1.0.0_SA_CTO~DELL1)",
    "round": "v110",
    "remediation": {
      "state": "OPEN",
      "owner": "portal manager (named by 1.0.0_SA_CTO~DELL1)",
      "round": "v110"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
