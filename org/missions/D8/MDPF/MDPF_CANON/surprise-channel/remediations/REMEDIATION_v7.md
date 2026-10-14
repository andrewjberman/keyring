# MDPF_CANON -- round 7 remediations (dell1)

<sweep_watermark>2026-10-14T16:05Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T16:05:00Z. Graduated at ADJUDICATION_v10 D1-C-S74: 4 rows.

```json
[
  {
    "id": "MDPF_CANON-D1-W18-S7",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The Trend draws Client Unsupervised in #f97316, the locked Ultra-Short Term hex, in the same legend and stack.",
    "evidence": [
      "investigation row MDPF_CANON-D1-W18-S7",
      "adjudication row MDPF_CANON-D1-C-S74 (ADJUDICATION_v10)"
    ],
    "remedy": "Give the Client series colours at least 10 dE00 from every ladder rung (DESIGN.md C4), on the candidate before it lands.",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v7"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "MDPF_CANON-D1-W18-S1",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "renderTrendTooltip renders every series entry including nulls, as $0 rows.",
    "evidence": [
      "investigation row MDPF_CANON-D1-W18-S1",
      "adjudication row MDPF_CANON-D1-C-S74 (ADJUDICATION_v10)"
    ],
    "remedy": "Filter null entries before building the tooltip rows; a render with a hover on dates C and D shows no Client row.",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v7"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "MDPF_CANON-D1-W18-S3",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The Trend stack meets opal_aggregate_aua to the cent on 24 of 487 dates; the 'rounding gap' class holds a worst residual reported in billions.",
    "evidence": [
      "investigation row MDPF_CANON-D1-W18-S3",
      "adjudication row MDPF_CANON-D1-C-S74 (ADJUDICATION_v10)"
    ],
    "remedy": "Name the residual's cause and its largest date before FWD-9 (6) is graded.",
    "owner": "2.0.0_SA_COO~D1",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~D1",
      "round": "v7"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~D1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "MDPF_CANON-D1-W17-S2",
    "project": "MDPF_CANON",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "test_global_fold_flag2.py replaces the module-level loader with a stub and never restores it.",
    "evidence": [
      "investigation row MDPF_CANON-D1-W17-S2",
      "adjudication row MDPF_CANON-D1-C-S74 (ADJUDICATION_v10)"
    ],
    "remedy": "Restore the loader (fixture or monkeypatch) so later tests read the real one.",
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
