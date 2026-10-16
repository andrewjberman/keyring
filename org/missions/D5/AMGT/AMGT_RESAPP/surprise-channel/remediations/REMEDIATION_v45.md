# AMGT_RESAPP -- round 107 (~R1's keys) remediations (dell1)

<sweep_watermark>2026-10-16T00:43:06Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-16T00:43:06Z. Graduated at ADJUDICATION_v134 (C-S156): 4 rows, ARMED, owner and disarm owner 2.0.0_SA_COO~R1.
REMEDIATION_v44's SHOP CN rows (W441-S1, W443-S2, D1-S31, D1-S32) read met by the team mark on the bn-4 walk, and REMEDIATION_v43 (W419-S3, the team-row grid dash) reads met on ZURN SW's grid.
Closing those rows is a separate act, not done here.

```json
[
  {
    "id": "AMGT_RESAPP-D1-S35",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "On a withheld name with no team P/E (ZURN SW, 939 HK, ICT PM, 1299 HK), Key Figures renders no P/E row, so the withhold reason prints nowhere. What Changed prints ratio lines for the withheld years under 'a line this page has no name for yet'.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S35",
      "adjudication row AMGT_RESAPP-D1-C-S156 (ADJUDICATION_v134)"
    ],
    "remedy": "Key Figures shows a P/E row whose forecast cells print the served withhold reason where no team value exists, and the page prints no withheld ratio elsewhere (What Changed included). Close when: this seat reads both on the next walk's withheld names.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v107",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v107"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W474-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The worker's row for the same state as D1-S35 (four of five withheld drawn names show no P/E row).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W474-S1",
      "adjudication row AMGT_RESAPP-D1-C-S156 (ADJUDICATION_v134)"
    ],
    "remedy": "Closes with AMGT_RESAPP-D1-S35.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v107",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v107"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-S34",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "PBR US 2025's team range prints with no source mark, because the mark is keyed on a withheld column.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S34",
      "adjudication row AMGT_RESAPP-D1-C-S156 (ADJUDICATION_v134)"
    ],
    "remedy": "The CTO rules whether every team-filled Key Figures P/E cell carries the mark. Close when: the ruling is in the round-107 analysis and the page matches it on the next walk.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v107",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v107"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-C-S156",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "bn-4 AC6 NOT MET: change 3 does not show on withheld names with no team P/E.",
    "evidence": [
      "adjudication row AMGT_RESAPP-D1-C-S156",
      "adjudication row AMGT_RESAPP-D1-C-S156 (ADJUDICATION_v134)"
    ],
    "remedy": "Closes with AMGT_RESAPP-D1-S35.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v107",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v107"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
