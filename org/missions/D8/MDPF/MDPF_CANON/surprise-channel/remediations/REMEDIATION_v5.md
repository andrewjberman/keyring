# MDPF_CANON -- round 5 remediations (dell1)

<sweep_watermark>2026-10-12T17:51Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-12T17:51:00Z. Graduated at ADJUDICATION_v8: 2 rows, both INERT.

```json
[
  {
    "id": "MDPF_CANON-D1-S18",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "mdpf-gold-lambda's MDPF_GOLD_COMMIT reads 88e974ca10 while the deployed package is 0d39789fdf; every run manifest stamps run.code.commit 88e974ca10.",
    "evidence": [
      "investigation row MDPF_CANON-D1-S18",
      "adjudication row MDPF_CANON-D1-C-S63"
    ],
    "remedy": "Set MDPF_GOLD_COMMIT to the deployed commit in the round-6 fold deploy's plan, under that order's own pair. Close when: a run manifest's run.code.commit equals the deployed package's BUILD_MANIFEST source_vintage.commit",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v6",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "MDPF_CANON-D1-C-S65",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "An on-demand gold run writes s3://opal-data-mdpf/mdpf/global/state/taxsma_control/current.json, a key the CN-d-1 deploy's sign-off and ledger did not name; this time only process_time moved.",
    "evidence": [
      "adjudication row MDPF_CANON-D1-C-S65"
    ],
    "remedy": "Name taxsma_control/current.json (and every routine state write of the gold run) in the blast radius of any pair that authorizes an on-demand gold run, with its prior VersionId as rollback. Close when: the next such pair names it",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v6",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v6"
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
