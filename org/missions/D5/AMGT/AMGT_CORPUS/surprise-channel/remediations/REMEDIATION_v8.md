# AMGT_CORPUS -- round 45 remediations (dell1)

<sweep_watermark>2026-10-11T12:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T12:15:00Z. Graduated at ADJUDICATION_v59 C-S36: 1 row, INERT.

```json
[
  {
    "id": "AMGT_CORPUS-D1-S3",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "With the team's own rows served, the Model-tab sheet builder (portal DEV ff418947 modelSheet.ts) renders every team-sheet label for the 32 names with an own workbook, and 3210 of 9233 rendered rows have no field behind them (236 distinct labels: section headers such as Financial Summary, column headers such as Year, control tokens such as BEST_FPERIOD_OVERRIDE). FWD-12 and FWD-20 read as conflicting until the rows are classed.",
    "evidence": [
      "investigation row AMGT_CORPUS-D1-S3",
      "adjudication row AMGT_CORPUS-D1-C-S29 (reproduced: unmapped 3210 of 9233)",
      "org/missions/D5/AMGT/AMGT_CORPUS/ledger/ROUND_ANALYSIS.round44.md:54-75 ADDENDUM 1 @161ccad473 (the ruling)"
    ],
    "remedy": "ADDENDUM 1's round-46 LOCAL reader cell: one FIGURE / HEADING / CONTROL classifier in team_sheet.py, tested on the three examples plus a FIGURE control, then the rendered re-read. Close when: the per-name census prints FIGURE, HEADING and CONTROL counts summing to the sheet's rows, unmapped reads 0 over FIGURE rows with the denominator printed, HEADING rows render with no value cell, and CONTROL rows are counted and not rendered.",
    "owner": "2.0.0_SA_COO~C1",
    "round": "v45",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~C1",
      "round": "v45"
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
