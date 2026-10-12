# AMGT_CORPUS -- round 46 remediations (dell1)

<sweep_watermark>2026-10-11T15:50Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T15:50:00Z. Graduated at ADJUDICATION_v61: 3 rows, all INERT.

```json
[
  {
    "id": "AMGT_CORPUS-D1-C-S45",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "On the 32 live own-workbook sheets, EQY_FUND_YEAR (a field code, no numeric value) is classed HEADING on 32 of 32 and renders as a heading, and BEST_FPERIOD_OVERRIDE (ADDENDUM 1's own CONTROL example) is classed FIGURE on 29 of 32 because its row carries numbers; ADDENDUM 1 says a CONTROL row is not rendered.",
    "evidence": [
      "adjudication row AMGT_CORPUS-D1-C-S45",
      "ledger/ROUND_ANALYSIS.round44.md:62-70"
    ],
    "remedy": "The classifier applies the identifier-form CONTROL rule before the HEADING rule, and the CTO states whether an override token that carries numbers is CONTROL. Close when: the per-name census reads EQY_FUND_YEAR CONTROL on 32 of 32, BEST_FPERIOD_OVERRIDE in the class the CTO states, and the rendered page shows neither where they are CONTROL.",
    "owner": "2.0.0_SA_COO~C1",
    "round": "v46",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~C1",
      "round": "v46"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~C1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "AMGT_CORPUS-D1-S5",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "On the DEV-built Model tab after the /12 redeploy, 1348 of 3381 FIGURE rows are labelled by raw field codes (the sheet's data-feed block) and team values print at full float precision; the ruling leaves open a display label for a field-code row and a number format for a team value.",
    "evidence": [
      "investigation row AMGT_CORPUS-D1-S5",
      "adjudication row AMGT_CORPUS-D1-C-S47 (walk DOM: 27 raw-code findings on IMB LN's Model tab)"
    ],
    "remedy": "An outcome-level ruling on (a) the display label of a field-code row and (b) the number format of a team value (the workbook's own number_format is readable at read time). Close when: the ruling is on the record and the rendered census prints 0 raw-code labels on the face (or the ruled exception) and team values in the ruled format.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v46",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v46"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "AMGT_CORPUS-D1-W1-S7",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "dossier.py's raised-read fallback stores the old six-key team_sheet, so a /12 dossier whose read raised carries no row_classes or row_values (absent, not empty). No served name is on that path today.",
    "evidence": [
      "investigation row AMGT_CORPUS-D1-W1-S7"
    ],
    "remedy": "The fallback stores the /12 key set with empty values and a reason. Close when: a test that raises the team-sheet read stores row_classes and row_values present and empty, beside the success-path control.",
    "owner": "2.0.0_SA_COO~C1",
    "round": "v46",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C1",
      "round": "v46"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~C1",
      "at": null
    },
    "closed": false
  }
]
```
