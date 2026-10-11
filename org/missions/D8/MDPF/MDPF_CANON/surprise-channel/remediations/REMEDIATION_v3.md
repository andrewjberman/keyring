# MDPF_CANON -- round 3 remediations (dell1)

<sweep_watermark>2026-10-11T05:40Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T05:40:00Z. Graduated at ADJUDICATION_v3: 7 rows (3 ARMED, 4 INERT), every owner 1.0.0_SA_CTO~DELL1 for the
round-3 analysis (ARMED disarm owner as filed). The rows in REMEDIATION_v1 and v2 stay open with their owners, except C-S12, closed REMEDIATED at v3.

```json
[
  {
    "id": "MDPF_CANON-D1-S10",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The smartx value leg (fact_model_aum_daily) lands one trading day behind the T-1 frontier on every weekend partition (Sat/Sun end Thursday; Monday ends Friday), so a weekend gold fire's cross-axis gate (v) refuses global and cannot read both legs at the frontier.",
    "evidence": [
      "investigation row MDPF_CANON-D1-S10",
      "adjudication row MDPF_CANON-D1-C-S23"
    ],
    "remedy": "Rule whether weekend fires are expected to build global (and so need a calendar-aware gate or a skip) or whether Monday's fire is the first that can; state it in the D1-S9 close condition. Close when: the rule is written and the first fire it names is read",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-W8-S2",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Global by_model re-emits opal_growth_sma and opal_div_sma at 2026-10-08 with nonzero account counts (45, 40) frozen at 49financial's 2026-07-17 values and a moving model_value, while no firm scope holds either entry: min firms 0.",
    "evidence": [
      "investigation row MDPF_CANON-D1-W8-S2",
      "adjudication row MDPF_CANON-D1-C-S25"
    ],
    "remedy": "Route to the owner of data/mdpf/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py: drop or null an entry no firm holds at the date, or rule the carry. Close when: a scheduled global build emits no by_model entry with a nonzero count that no firm holds at the date",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-W8-S3",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Served global opal_aggregate_aua differs from model_aua + non_model_aua on 24 dates (2026-08-26..2026-10-08); this seat measured the gap equal to sma_additive_aua + tax_additive_aua on 24 of 24. The fold docstring (:2256-2257) still states the identity at every date and says the front end derives the non-model band as total minus model.",
    "evidence": [
      "investigation row MDPF_CANON-D1-W8-S3",
      "adjudication row MDPF_CANON-D1-C-S26"
    ],
    "remedy": "Fold owner: correct the docstring identity to the additive form, and read whether any front-end band is still derived as total minus model. Close when: the docstring matches the emitted composition and the band's derivation is read (not derived, or derived net of the additive components)",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-W8-S4",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The global account-distribution keyed 2026-10-08 composes the cottonwood object keyed 2026-10-07 (7 of 7 total_aum equal; 0 of 7 to the 2026-10-08-keyed cottonwood object, built a day later). The global snapshot carries a firm leg one key-date behind its own label.",
    "evidence": [
      "investigation row MDPF_CANON-D1-W8-S4",
      "adjudication row MDPF_CANON-D1-C-S27"
    ],
    "remedy": "Route to the account-distribution global producer: align the firm legs to the global object's key date, or label the vintage per leg. Close when: a global account-distribution's firm legs read equal to the same-key firm objects",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-W8-S5",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "infra/logic/06_CONFORMANCE_LEDGER.md carries X2 GRANTED (Andrew-direct 2026-09-15) on the round-2 basis; the round-3 basis (read back equal by this seat) shows by_model min firms 0 and non-model series min firms 1.",
    "evidence": [
      "investigation row MDPF_CANON-D1-W8-S5",
      "adjudication rows MDPF_CANON-D1-C-S20 and C-S28"
    ],
    "remedy": "The CTO puts the re-read of X2 against X2_GLOBAL_BASIS.md (round 3) to Andrew as an open call. Close when: Andrew's word on X2 is recorded on the ledger row",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-S11",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "LGIC_ENFORCE's round-2 fixed input check_en_r2.py reads three FAILs at box/dell1 HEAD independent of MDPF_CANON: header marks of three generated files do not hash scopes.json; an undeclared registry file (event_rules.json) moves data/firm_registry.json; generate differs.",
    "evidence": [
      "investigation row MDPF_CANON-D1-S11",
      "adjudication row MDPF_CANON-D1-C-S29"
    ],
    "remedy": "Rule whether the three generated files are regenerated at HEAD or the round-2 check is retired. Close when: the three subcommands pass at HEAD or the check is retired by ruling",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_CANON-D1-W9-S7",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Nothing in the repo writes s3://opal-data-mdpf/code/: the runner's scripts and config arrive by a hand copy (about 20 commits behind HEAD outside the three files synced 2026-10-11). The round-3 hand sync is done and measured.",
    "evidence": [
      "investigation rows MDPF_CANON-D1-W9-S7 and D1-S12",
      "adjudication rows MDPF_CANON-D1-C-S36 and C-S37"
    ],
    "remedy": "Rule whether the repo-to-code copy becomes a deploy step (CloudOps) or stays manual with a recorded owner. Close when: the ruling is written and code/ reads equal to the repo for data/mdpf/scripts and data/mdpf/config",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v4",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v4"
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
