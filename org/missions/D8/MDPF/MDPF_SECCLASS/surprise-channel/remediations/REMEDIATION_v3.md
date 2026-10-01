# MDPF_SECCLASS -- rounds 4 and 5 remediations

<sweep_watermark>2026-09-30T14:39Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-09-30. S4 graduated at rounds 4-5's L9 (ADJUDICATION_v3.md). Closed IN PLACE in REMEDIATION_v2.md at the same compile, clocks only: S3 (DISARMED + REMEDIATED, suite 319 passed at CLOUD HEAD) and W5-S3 (DISARMED + REMEDIATED, 0 behind origin); evidence in the co-committed review. W6-S2 unchanged in its carrier; its remedy is the parked TO-SC-e12 (owner 0.7.0_AE_CloudOps, CTO 103327). Carried unchanged: S2 (REMEDIATION_v1, OPEN, not re-read this compile) and W5-S2 (REMEDIATION_v2, OPEN; the enum citation is not yet done per the round-5 packet).

```json
[
  {
    "id": "MDPF_SECCLASS-S4",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "label_row_if_unlabelled() and set_kind_if_absent() condition only on their one attribute being absent (ConditionExpression attribute_not_exists(<attr>)), so an update_item on a ticker with no row would mint a skeleton row carrying that attribute alone.",
    "evidence": [
      "infra/aws/lambda/v2_portal/yang_pipeline/label-legacy-classified-by.py:89 and set-instrument-kind.py:96 at CLOUD HEAD: ConditionExpression attribute_not_exists(%s) % _WRITTEN_ATTRIBUTE, no attribute_exists(ticker) (read by this seat ~17:4xZ)",
      "investigation row MDPF_SECCLASS-S4 (2.0.0_SA_COO~M): both CLIs refuse a live run; the issuer's pre-read dropped 0 of 238 and 0 of 156",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R4_R5_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "Add attribute_exists(ticker) to both ConditionExpressions (one clause each), with a test that an update on an absent key is refused. Round-6 hygiene; inert while both CLIs are blocked.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v6"
    },
    "closed": false
  }
]
```
