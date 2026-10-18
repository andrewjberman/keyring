# AMGT_RESAPP -- round 114 remediations (dell1)

<sweep_watermark>2026-10-18T01:34:53Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T01:34:53Z. Graduated at ADJUDICATION_v152 (C-S183): 4 rows, owner 2.0.0_SA_COO~R1.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W505-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ModelTab's price basis line prints the served period_end_date / fiscal_period_end ISO day (a bypass deferred by bu-2).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W505-S1",
      "adjudication row AMGT_RESAPP-D1-C-S183 (ADJUDICATION_v152)"
    ],
    "remedy": "The line prints the day in the long form. Close when: a walk or harness reads the basis line's date in the long form.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v114",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v114"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-W505-S2",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "ModelTab's gap-reason notes and PeersTab's absent-peers and column reasons print served reason text that can carry an ISO day; reasonInWords passes it through (three deferred bypasses).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W505-S2",
      "adjudication row AMGT_RESAPP-D1-C-S183 (ADJUDICATION_v152)"
    ],
    "remedy": "The reason text's days print in the long form. Close when: a harness case with an ISO day in a served reason renders the long form on each site.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v114",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v114"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-W506-S4",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The format=rich export still prints ISO days (the vintages line, the as-of vintage).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W506-S4",
      "adjudication row AMGT_RESAPP-D1-C-S183 (ADJUDICATION_v152)"
    ],
    "remedy": "The rich export prints days in the long form, or a ruling keeps ISO there. Close when: a fresh rich export of one name reads no ISO day, or the ruling is on record.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v114",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v114"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-W506-S5",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The printed pack's wrap guard rewrites an ISO day inside any printed line, including a verbatim quoted source passage (latent: none of eight live packs had one).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W506-S5",
      "adjudication row AMGT_RESAPP-D1-C-S183 (ADJUDICATION_v152)"
    ],
    "remedy": "A census of verbatim-quote blocks, then the guard exempts them. Close when: a quote carrying an ISO day prints unchanged and drafted prose still prints the long form.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v114",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v114"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO
