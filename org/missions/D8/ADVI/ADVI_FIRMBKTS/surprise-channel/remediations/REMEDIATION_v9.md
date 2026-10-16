# ADVI_FIRMBKTS -- round 8 remediations (dell1)

<sweep_watermark>2026-10-16T17:16:04Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-16T17:16:04Z. Graduated at ADJUDICATION_v9 (C-S58): 2 rows, INERT, owner 2.0.0_SA_COO~B1.

```json
[
  {
    "id": "ADVI_FIRMBKTS-D1-S59",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The Cottonwood silver run (SSM document opal-cot-silver-run) never merges account_attributes, so silver stopped at 2026-08-20 and gold/dimensions/accounts_dimension_latest.parquet joins a 2026-08-19 partition.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S59",
      "adjudication row ADVI_FIRMBKTS-D1-C-S58 (ADJUDICATION_v9)"
    ],
    "remedy": "Routed to the Cottonwood silver pipeline's owner: the run merges account_attributes, or the dimension's staleness is ruled. Close when: a silver account_attributes partition newer than 2026-08-20 is read, or the ruling names the row.",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v8"
    },
    "closed": false
  },
  {
    "id": "ADVI_FIRMBKTS-D1-S60",
    "project": "ADVI_FIRMBKTS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The secret opal/bd/cottonwood/credentials is live, declared by no Terraform, readable by 0 of 304 roles and unread since 2026-05-26.",
    "evidence": [
      "investigation row ADVI_FIRMBKTS-D1-S60",
      "adjudication row ADVI_FIRMBKTS-D1-C-S58 (ADJUDICATION_v9)"
    ],
    "remedy": "The Cottonwood plan lists it as a retire candidate (a delete needs a human confirmation), or it is declared with an owner. Close when: the plan or a ruling names it.",
    "owner": "2.0.0_SA_COO~B1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~B1",
      "round": "v8"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
