# MDPF_SECCLASS -- round 17 remediations

<sweep_watermark>2026-10-09T11:51Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T11:51:00Z. Graduated at ADJUDICATION_v13: 2 rows, both INERT.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-S24",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The COT twin of D1-S19: test_cot_etf_classifier_canonical.py::test_deploy_tool_ships_the_shared_modules_beside_cottonwoods_gold_files pins the retired ship-every-_shared-module rule and fails at HEAD (1 of 28 in the COT gold suite).",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S24",
      "org/tier1_exec/2.0.0_SA_COO/deliverables/MDPF_SECCLASS_M/L8_DRAIN_END_PACKET_R17_20261009.md @6e68c2d4ca Rows"
    ],
    "remedy": "Retire or rewrite both stale tests (D1-S19 BD, D1-S24 COT) to the named-file rule (safe_deploy_core.shipped_artifacts_for). Close when: both suites read green at HEAD",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v18",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v18"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "MDPF_SECCLASS-D1-S23",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "safe-deploy's seat-gates OPEN-CALL and OPEN-DEPLOY limbs match on the ROOT token (data/black_diamond), including inside referenced body documents, so a one-key deploy drew 4 STOP hits, none contending for its key.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S23"
    ],
    "remedy": "Key the limbs on the deploy's own write set (keys/files), not the root token or prose in referenced documents. Close when: a one-key ship on data/black_diamond reads 0 unrelated hits",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v18",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v18"
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
