# MDPF_STRATID -- grading-pass remediations (dell1)

<sweep_watermark>2026-10-13T18:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-13T18:45:00Z. Graduated at ADJUDICATION_v6: 5 rows, all INERT.

```json
[
  {
    "id": "MDPF_STRATID-D1-S1",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Each MDPF run rewrites the prior frontier date's per-firm aggregate-aua values (Cottonwood's measured account count becomes None) with no restatement record.",
    "evidence": [
      "investigation row MDPF_STRATID-D1-S1",
      "adjudication row MDPF_STRATID-D1-C-S28"
    ],
    "remedy": "A restatement record per prior-date rewrite, or a freeze of measured prior-date fields. Close when: a run that rewrites a prior date writes a record naming each changed field, beside a date it leaves untouched.",
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
    "id": "MDPF_STRATID-D1-S3",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "s3://opal-data-etfs has never had versioning enabled; overwrites of config read by three ETFS producers have no version rollback.",
    "evidence": [
      "investigation row MDPF_STRATID-D1-S3",
      "adjudication row MDPF_STRATID-D1-C-S29"
    ],
    "remedy": "Enable versioning on opal-data-etfs (infra, under its own pair) or rule that writers preserve prior bytes. Close when: get-bucket-versioning reads Enabled, or the ruling's path is cited.",
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
    "id": "MDPF_STRATID-D1-S4",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The box push gate ships one file of an import-coupled pair and skips the other as a first-mint, so a deployed prefix can be left with an unresolvable import.",
    "evidence": [
      "investigation rows MDPF_STRATID-D1-S4, D1-S6",
      "adjudication row MDPF_STRATID-D1-C-S30"
    ],
    "remedy": "Make the push gate pair-aware (refuse to ship an importer whose import target is absent at the destination). Close when: a push of an importer without its module is refused, beside a control pair that ships.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_STRATID-D1-S5",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A deploy-ledger authorship handover updates the sentinel's author field while the OPEN-DEPLOY seat-gate reads a different carrier.",
    "evidence": [
      "investigation row MDPF_STRATID-D1-S5",
      "adjudication row MDPF_STRATID-D1-C-S31"
    ],
    "remedy": "One carrier for ledger authorship that both deploy_ledger.py and the seat-gate read. Close when: a handover clears the seat-gate under ENFORCE, beside a control with no handover that is refused.",
    "owner": "1.0.0_SA_CTO",
    "round": "v2",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO",
      "round": "v2"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_STRATID-D1-C-S18",
    "project": "MDPF_STRATID",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Opal_Muni_Sleeve recurs on the served unidentified list as RULE_NOT_COUNTED after Andrew ruled it is not Opal's Muni SMA (call 203a).",
    "evidence": [
      "adjudication row MDPF_STRATID-D1-C-S18",
      "CTO_CLOSE_DELL1_OPEN_CALLS_ON_ANDREW_DIRECT_20261011_032xZ.md:12"
    ],
    "remedy": "Record the person's exclusion with its reason as data so the sleeve leaves the unknowns (C-MUNI-VERIFY). Close when: a run's unidentified list omits it and a recorded-exclusions list names it with the ruling.",
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
