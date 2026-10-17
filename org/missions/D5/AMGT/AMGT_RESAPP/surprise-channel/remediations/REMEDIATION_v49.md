# AMGT_RESAPP -- round 109 remediations (dell1)

<sweep_watermark>2026-10-17T13:05:48Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T13:05:48Z. Graduated at ADJUDICATION_v147 (C-S173): 4 rows.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W491-S2",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The What Changed row's expandable full-value detail prints a list value as raw JSON (the bp-1 candidate's full() helper stringifies any non-scalar); RIO LN's earnings-date list shows it.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W491-S2",
      "adjudication row AMGT_RESAPP-D1-C-S173 (ADJUDICATION_v147)"
    ],
    "remedy": "The detail renders a list as readable lines (date and period per entry), with no JSON text. Close when: a walk reads RIO LN's earnings row detail with no raw-code finding.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v109",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v109"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W489-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "After bp-3 labels an untied segment column 'Year not stated (column n)', the served period_note still says columns not named by a year keep Bloomberg's period numbers.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W489-S1",
      "adjudication row AMGT_RESAPP-D1-C-S173 (ADJUDICATION_v147)"
    ],
    "remedy": "The period_note matches the new label before bp-6 deploys it. Close when: the served note and the column label agree on one name (read before or at bp-6).",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v109",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v109"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    }
  },
  {
    "id": "AMGT_RESAPP-D1-W490-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "WhatChangedPanel.tsx builds its own money string (inDisplayUnits) and does not use bp-4's display rule, so a foreign code and the sign-first rule may differ between tiles and What Changed.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W490-S1",
      "adjudication row AMGT_RESAPP-D1-C-S173 (ADJUDICATION_v147)"
    ],
    "remedy": "What Changed money uses the same display rule as the tiles. Close when: one non-USD name reads the same currency form and sign order in both places.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v109",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v109"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-S55",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The task-order status vocabulary has no terminal NOT_MET value, so an order recorded NOT MET keeps a leading 'complete'.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S55",
      "adjudication row AMGT_RESAPP-D1-C-S173 (ADJUDICATION_v147)"
    ],
    "remedy": "The gate's owner adds a terminal NOT MET status or rules the form. Close when: the vocabulary or a ruling names it.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v109",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v109"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
