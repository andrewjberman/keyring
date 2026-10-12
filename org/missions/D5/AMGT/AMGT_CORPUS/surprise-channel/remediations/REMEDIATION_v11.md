# AMGT_CORPUS -- round 48 remediations (dell1)

<sweep_watermark>2026-10-11T22:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T22:55:00Z. Graduated at ADJUDICATION_v63: 2 rows (1 ARMED, 1 INERT).

```json
[
  {
    "id": "AMGT_CORPUS-D1-C-S64",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "On 13 of 32 own workbooks, 62 FIGURE rows come from a side-by-side case block in the sheet's period columns (separators 'Multiple', 'Price', 'Return', 'Tgt', 'Average', 'EPS' between numbers); the reader aligns them to the sheet's one period header, so the page prints case values under history years (ROG SW 'Price $660.45' and 'Year 2027E' under 2016). DEV only; fires on the PROD promotion.",
    "evidence": [
      "adjudication rows AMGT_CORPUS-D1-C-S63, D1-C-S64"
    ],
    "remedy": "The reader recognises a case block (a row whose period cells carry text separators, or the block under a case header) and serves it as the team's case table with its own column labels, or does not align it to the period header. Close when: the 62 rows' census reads 0 case values under a history-year header on the 13 names, with ROG SW's case prices under their case-years, beside a control row that keeps its history alignment.",
    "owner": "2.0.0_SA_COO~C1",
    "round": "v48",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~C1",
      "round": "v48"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~C1",
      "at": "2026-10-12T05:30:00Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_CORPUS-D1-C-S65",
    "project": "AMGT_CORPUS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "4,403 text cells in the 32 own workbooks' FIGURE rows print '--' with no why: 2,452 are the team's own ranges ('22x-26.5x') and 1,457 are Excel error values (#N/A 759, #N/A N/A 391, #VALUE! 219, NA 76, #DIV/0! 12).",
    "evidence": [
      "adjudication row AMGT_CORPUS-D1-C-S65"
    ],
    "remedy": "A display ruling: a range shows as the team wrote it, and an Excel error says why in words (or '--' is accepted on the record). Close when: the ruling is on the record and the rendered census prints the range and error cells in the ruled form.",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v48",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v48"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  }
]
```
