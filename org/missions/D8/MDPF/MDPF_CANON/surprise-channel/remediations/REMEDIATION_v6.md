# MDPF_CANON -- round 6 remediations (dell1)

<sweep_watermark>2026-10-14T14:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T14:05:00Z. Graduated at ADJUDICATION_v9: 7 rows (4 ARMED/BLOCKING at D1-C-S68, 3 INERT at D1-C-S69).

```json
[
  {
    "id": "MDPF_CANON-D1-W16-S1",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "On a one-firm as-of an unfolded Global category-views build would fail the registry's recon or serve an unbalanced Models node.",
    "evidence": [
      "investigation row MDPF_CANON-D1-W16-S1",
      "adjudication row MDPF_CANON-D1-C-S68 (ADJUDICATION_v9)"
    ],
    "remedy": "AMENDMENT 1's refusal (Global refused whole) is in place; the row closes on the first organic one-firm as-of read showing the prior Global VersionId unchanged (the CTO's third arm).",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v7"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-W16-S2",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "build_aum_metrics' _frontier fallback fills a None as-of fold line with its last pooled value.",
    "evidence": [
      "investigation row MDPF_CANON-D1-W16-S2",
      "adjudication row MDPF_CANON-D1-C-S68 (ADJUDICATION_v9)"
    ],
    "remedy": "With D1-W16-S4: a fold line's current value is honest-None on a suppressed as-of (no _frontier fill for the fold line).",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v7"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-W16-S4",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "On a no-pool as-of the Other Models card would show the last pooled dollars as current, with q-cells computed from them.",
    "evidence": [
      "investigation row MDPF_CANON-D1-W16-S4",
      "adjudication row MDPF_CANON-D1-C-S68 (ADJUDICATION_v9)"
    ],
    "remedy": "As D1-W16-S2; read on a planted no-pool fixture before any no-pool day serves.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v7"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-W16-S5",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The staged global aggregate is written before the fold guard, unfolded, on every run; its readers are unverified.",
    "evidence": [
      "investigation row MDPF_CANON-D1-W16-S5",
      "adjudication row MDPF_CANON-D1-C-S68 (ADJUDICATION_v9)"
    ],
    "remedy": "Rule whether the staged copy moves behind the guard; name its readers.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v7"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-S22",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The MDPF portal publisher role is denied s3:GetObject on platinum/mdpf/_manifests/latest.json, so it republishes every leaf daily.",
    "evidence": [
      "investigation row MDPF_CANON-D1-S22",
      "adjudication row MDPF_CANON-D1-C-S69 (ADJUDICATION_v9)"
    ],
    "remedy": "Grant the publisher role GetObject on its own pointer (one IAM line, Terraform).",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v7"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-S23",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": ".tools/mdpf-code-equality.py hashes working-tree bytes, so a CRLF checkout reads DIFFER against S3.",
    "evidence": [
      "investigation row MDPF_CANON-D1-S23",
      "adjudication row MDPF_CANON-D1-C-S69 (ADJUDICATION_v9)"
    ],
    "remedy": "The round-7 repair cell: hash the git blob.",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v7"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-S24",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-6 packet's card read Total Holdings on the wrong run date (delta 0 instead of -177).",
    "evidence": [
      "investigation row MDPF_CANON-D1-S24",
      "adjudication row MDPF_CANON-D1-C-S69 (ADJUDICATION_v9)"
    ],
    "remedy": "The card to Andrew carries the --date 2026-10-14 read (-177) and names the Other Models card.",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v7",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v7"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": false
  }
]
```
