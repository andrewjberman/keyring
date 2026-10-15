# MDPF_CANON -- rounds 7 and 9 remediations (dell1)

<sweep_watermark>2026-10-15T14:12Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-15T14:20:00Z. Graduated at ADJUDICATION_v15 D1-C-S86: 3 rows.

```json
[
  {
    "id": "MDPF_CANON-D1-S27",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "/api/general/mdpf/* was rewritten to platinum/mdpf/* behind the JWT check alone, so any login could read another firm's per-firm leaf.",
    "evidence": [
      "investigation row MDPF_CANON-D1-S27",
      "adjudication row MDPF_CANON-D1-C-S86 (ADJUDICATION_v15)"
    ],
    "remedy": "CN-q-1: auth-validator-edge v24 admits a per-firm MDPF leaf only to the claim's own firm (internal sessions pass). Live on 27 of 27 associations. Limit: a live foreign-firm 403 is unproven (no partner login); the deployed-bundle replay with a v23 negative control stands in.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v8",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": "2026-10-15T14:10:00Z"
    },
    "closed": true
  },
  {
    "id": "MDPF_CANON-D1-S25",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "On Model Portfolios (Global, as-of 2026-10-13) the Client card reads $292.26M while its drill-down reads $341.10M.",
    "evidence": [
      "investigation row MDPF_CANON-D1-S25",
      "adjudication row MDPF_CANON-D1-C-S86 (ADJUDICATION_v15)"
    ],
    "remedy": "One definition of Client on both surfaces, or each labels what it sums; read on the page after CN-p-2.",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-S26",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "round-close-check sorts ADJUDICATION_v*.md as strings and returns the first CVO verdict, so a later re-grade cannot replace an earlier one.",
    "evidence": [
      "investigation row MDPF_CANON-D1-S26",
      "adjudication row MDPF_CANON-D1-C-S86 (ADJUDICATION_v15)"
    ],
    "remedy": "Sort the files numerically and take the newest verdict per criterion.",
    "owner": "0.0.0_AB_MSTR~DELL1",
    "round": "v8",
    "remediation": {
      "state": "OPEN",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "round": "v8"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR~DELL1",
      "at": null
    },
    "closed": false
  }
]
```
