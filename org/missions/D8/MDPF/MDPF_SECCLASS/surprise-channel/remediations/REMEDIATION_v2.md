# MDPF_SECCLASS -- rounds 2 and 3 remediations

<sweep_watermark>2026-09-30T06:25Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-09-30. Graduated at rounds 2-3's L9 (ADJUDICATION_v2.md).

```json
[
  {
    "id": "MDPF_SECCLASS-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The SC-t-1 drain removed the BD classifier's private _ticker_map/_name_map, which IRPT_BCKEND's Holdings producer still reads (holdings_snapshot.py:837, 845, 847 at HEAD); CLOUD's investor_reporting suite reads 30 failed / 16 errors and a Holdings re-mint from CLOUD would fail. Served Holdings are unaffected (minted 09-29 16:21Z from the pre-thread library).",
    "evidence": [
      "data/assets/scripts/gold/investor_reporting/holdings_snapshot.py:837,845,847 at CLOUD HEAD read clf._ticker_map and clf._name_map (printed by this seat 07:1xZ)",
      "investigation row MDPF_SECCLASS-S3 (2.0.0_SA_COO~M): r27_suite_whole.py SUITE-BROKEN at 874ab56b33",
      "IRPT_BCKEND.TO-IB-m29-291 reads pending at HEAD (the disarm cell)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R2_R3_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "P0: IB-mr-291 lands Holdings canonical-first with its own declared bd-securities fallback and no import of the BD library; disarm when the investor_reporting suite reads 0 failed / 0 errors on CLOUD. Until then no Holdings package is minted from CLOUD. Drain hygiene for every issuer: a drain that changes a shared module re-runs every suite that imports it.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~M",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": "2026-09-30T17:50Z"
    },
    "closed": true
  },
  {
    "id": "MDPF_SECCLASS-W6-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The live unconditional bd-securities PutItem for bd-exporter-ec2-role is granted by shared-infra/main.tf aws_iam_policy.bd_securities_access (Scan/GetItem/PutItem/UpdateItem/BatchWriteItem on BOTH bd-securities and etf-classifications), also attached to partners-lambda-role; SC-e7's step 2 named bd-pipeline/iam.tf, which carries no such grant. The E18_IAM half's 'bd-securities PutItem removed' is not true of the principal.",
    "evidence": [
      "infra/aws/terraform/shared-infra/main.tf:402-407 at HEAD (printed by this seat): the Action list and both table ARNs; last commit 4cd7f74e57 (2026-06-16)",
      "investigation row MDPF_SECCLASS-W6-S2 (0.9.0_WK_MDPF_SECCLASS~6)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R2_R3_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "P1: a follow-on order scoped to infra/aws/terraform/shared-infra/main.tf drops bd-securities from bd_securities_access (or splits the policy per principal), with its own never-widen half because partners-lambda-role shares it; AE lane, Terraform only. The E18_IAM half is not signed as 'removed' until then.",
    "owner": "2.0.0_SA_COO~M",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M",
      "round": "v4"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~M",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-W5-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "This device's CLOUD and origin/CLOUD have diverged: at 07:1xZ origin is 1,460 commits ahead of local CLOUD and local is 260 ahead of origin; 8757ce95eb (site Z's seed-etf-constituents.py union) is not on local CLOUD. A cell told to build on it cannot see it, and every CVO commit since 2026-09-29 19:54Z is LOCAL.",
    "evidence": [
      "git rev-list --count CLOUD..origin/CLOUD = 1460 and origin/CLOUD..CLOUD = 260, after git fetch at 04:11Z, read by this seat 07:1xZ",
      "git merge-base --is-ancestor 8757ce95eb CLOUD: not an ancestor",
      "investigation row MDPF_SECCLASS-W5-S3 (0.9.0_WK_MDPF_SECCLASS~5)",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R2_R3_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "P0: 0.0.0_AB_MSTR reconciles the two trunks (/integrate: pull-merge, never rebase, on Andrew's word), then pushes; until then no cell is cut against an origin-only commit. Disarm when origin/CLOUD..CLOUD reads 0.",
    "owner": "0.0.0_AB_MSTR",
    "round": "v4",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "0.0.0_AB_MSTR",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "0.0.0_AB_MSTR",
      "at": "2026-09-30T17:35Z"
    },
    "closed": true
  },
  {
    "id": "MDPF_SECCLASS-W5-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "identifier_namespace now names two enums on two schemas: {TICKER, CUSIP} on etf-classifications and {TICKER, CUSIP, ISIN, CASH, MODEL, UNMATCHED} on IRPT_BCKEND's AnalysisRequest wire contract. No reader reads both today.",
    "evidence": [
      "investigation row MDPF_SECCLASS-W5-S2 (0.9.0_WK_MDPF_SECCLASS~5): comp-find census, 8 hits all in the IRPT tree, 0 in the classification code",
      "CTO RULING 103140 named the field and its values",
      "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R2_R3_REVIEW_20260930.md (co-committed)"
    ],
    "remedy": "P3: 1.0.0_SA_CTO records whether the narrower enum is a declared subset of the wider one (one vocabulary) or an unrelated field that should carry a distinct name; rule 24 (iii) intent coherence.",
    "owner": "1.0.0_SA_CTO",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    },
    "closed": false
  }
]
```
