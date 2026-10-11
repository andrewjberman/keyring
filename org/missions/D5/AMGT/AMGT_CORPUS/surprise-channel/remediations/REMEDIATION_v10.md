# AMGT_CORPUS -- round 47 remediations (dell1)

<sweep_watermark>2026-10-11T21:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T21:20:00Z. Graduated at ADJUDICATION_v62: 2 rows, both INERT.

```json
[
  {
    "id": "AMGT_CORPUS-D1-S7",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The round-46 period-header test took the EQY_FUND_YEAR row as the header on CLX, ML FP and BABA, so 177 rows that carry figures are served (the /12 objects, live on DEV) as headings with no value. The /13 write carries the correction; the live function still serves /12.",
    "evidence": [
      "investigation row AMGT_CORPUS-D1-S7",
      "adjudication rows AMGT_CORPUS-D1-C-S54, D1-C-S55"
    ],
    "remedy": "Serve the /13 objects (AMGT_RESAPP round 98's redeploy). Close when: the live census after the redeploy reads, for CLX, ML FP and BABA, the /13 classes (those 177 rows FIGURE, each with a figure or a why) and each name's team_sheet equal to its stored /13 field.",
    "owner": "2.0.0_SA_COO~C1",
    "round": "v47",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C1",
      "round": "v47"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~C1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_CORPUS-D1-S6",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "50 of the 106 field-code labels are FactSet data-item codes no estate source describes (702 of 1,348 code-labelled FIGURE rows); they render 'FactSet line' with the code and why in the title (1,343 rendered rows in the round-47 prediction). ADDENDUM E's DEC names only a Bloomberg field code's label.",
    "evidence": [
      "investigation row AMGT_CORPUS-D1-S6",
      "adjudication row AMGT_CORPUS-D1-C-S56"
    ],
    "remedy": "A ruling on how a FactSet code's row is labelled (a cited description entry in factset_descriptions.json, or 'FactSet line' accepted on the record). Close when: the ruling is on the record and the rendered census prints the FactSet rows' labels in the ruled form.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v47",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v47"
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
