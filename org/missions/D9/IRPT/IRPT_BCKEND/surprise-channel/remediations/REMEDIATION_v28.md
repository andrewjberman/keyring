# IRPT_BCKEND -- project sweep 19 remediations

<sweep_watermark>2026-10-08T18:47Z</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-08. Graduated at sweep 19 (ADJUDICATION_v36.md), round label v81. 2 rows, both OPEN.

```json
[
  {
    "id": "IRPT_BCKEND-D2-W174-S3",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The on-behalf advisor lookup reads opal-partner-<firm>; irpt-ycharts-generate's role grants no read on any opal-partner table, so a deployed build refuses every on-behalf admit (fails closed) until an IAM grant lands.",
    "evidence": [
      "investigation rows IRPT_BCKEND-D2-W174-S3, D2-S5",
      "drain-end packet rounds 79-80 @2f7fa13324"
    ],
    "remedy": "The IAM read grant on opal-partner-<firm> lands under ~Y2's E6 release-2 pair (a laptop Terraform act), with an on-behalf admit as its after-read.",
    "owner": "2.0.0_SA_COO~Y2",
    "round": "v81",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Y2",
      "round": "v81"
    },
    "closed": false
  },
  {
    "id": "IRPT_BCKEND-D2-W175-S1",
    "project": "IRPT_BCKEND",
    "fabric": "dell2",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The repinned repository.py names CUSTODY_REPORT, but the active retention policy irpt-x10-v1 registers no CUSTODY_REPORT family, so an enforced repository refuses to retain or read a custody report (RetentionRefused).",
    "evidence": [
      "investigation rows IRPT_BCKEND-D2-W175-S1, D2-S5",
      "release-census irpt-export-render --pin a0d8d4943f: changed repository.py, retention.py (this compile)"
    ],
    "remedy": "A CUSTODY_REPORT retention family is registered (E8, ~M2) before the custody owner read can pass; E9 (IB-pr-369) carries the code.",
    "owner": "2.0.0_SA_COO~M2",
    "round": "v81",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M2",
      "round": "v81"
    },
    "closed": false
  }
]
```
