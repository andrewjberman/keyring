# MDPF_DEMQUE -- round 1 remediations

<sweep_watermark>2026-10-08T23:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-08T23:55:00Z. Graduated at ADJUDICATION_v1: 3 rows, all INERT.

```json
[
  {
    "id": "MDPF_DEMQUE-D1-W3-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "land_cot.py derives Cottonwood's routed legacy bucket and three keys from the consumer's source because the naming gate refuses them as literals and the legacy layout has no address() form; the lander breaks if the consumer's key expressions stop being literals.",
    "evidence": [
      "land_cot.py at 9ca032bff5 (LAND-OK, LSEAM-OK)",
      "investigation row MDPF_DEMQUE-D1-W3-S1 (0.9.0_WK_MDPF_DEMQUE~3)"
    ],
    "remedy": "Decide whether the lander keeps derivation (with a test pinning the consumer's key expressions) or waits for the cot R19 migration. Close when: the decomposition records the choice and, if kept, a test fails on a non-literal key expression",
    "owner": "2.0.0_SA_COO~Q1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Q1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Q1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_DEMQUE-D1-W4-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Cottonwood's scheduled gold run is the opal-cot-gold-run SSM document (Terraform ssm.tf), a fixed script list with no S_00; gold_dispatch.sh is never called on the schedule, so scheduling the price build is a Terraform document edit, not a dispatch flag.",
    "evidence": [
      "aws ssm get-document opal-cot-gold-run (v10) re-read by 3.0.0_SA_CVO at 23:5xZ: 18 scripts, no S_00",
      "investigation row MDPF_DEMQUE-D1-W4-S1; trace Q1-Q2"
    ],
    "remedy": "Fold into the hop-6 consumer decision (D1-W4-S2): if Cottonwood's price build stays the store, add S_00 to the gold-run document via safe-apply. Close when: the round-2 decomposition names the schedule change or retires the price build as the store",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_DEMQUE-D1-W4-S2",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "No Cottonwood page reads canonical_prices.parquet: B_00 values holdings from BD-reported market value and returns before load_canonical_prices(), A_03's read is skipped, and no page shows a client's per-security daily prices. FWD-1's 'shows its daily prices on that client's pages' has no consumer.",
    "evidence": [
      "B_00.canonical_holdings.py:1095-1100 vs :1124; gold-run log 20261008-113337; comp-find canonical_prices portal/src 0 of 1368",
      "investigation row MDPF_DEMQUE-D1-W4-S2; real run FWD1_REAL_RUN_R1.md hop 6"
    ],
    "remedy": "ENDPOINT-level call: which page shows a Cottonwood client's per-security daily prices and which store it reads (Cottonwood's price build or MDPF_SECHIST's series). Close when: the PRD carries the answer as an addendum or a FWD-1 restatement Andrew ratified",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v2"
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
