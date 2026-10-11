# MDPF_DEMQUE -- round 6 remediations

<sweep_watermark>2026-10-09T13:15Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T13:15:00Z. Graduated at ADJUDICATION_v6: 2 rows, both INERT.

```json
[
  {
    "id": "MDPF_DEMQUE-D1-W17-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The history ceiling is a held floor (5858, the largest ledger day) and the reserve is measured from the same day x 1.25 (7322), so the history allowance per day is -1464 and no history backfill can be quoted a finish date.",
    "evidence": [
      "investigation row MDPF_DEMQUE-D1-W17-S1",
      "bbg_allowance.json history 5858/7322; quote DEMQUE-TR-COMPARISON-DIVIDEND-PAYERS finish_date null"
    ],
    "remedy": "Measure the history channel's real capacity (the ceiling), not the production day, or rule how a backfill draws when the measured ceiling is unknown (a spend is Andrew's). Close when: a history quote reads a finish date on a ceiling with claim measured",
    "owner": "1.0.0_SA_CTO~DELL1",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "round": "v7"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "1.0.0_SA_CTO~DELL1",
      "at": null
    },
    "closed": true
  },
  {
    "id": "MDPF_DEMQUE-D1-S4",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "quote_vs_actual.py --all raises KeyError 'finish_date' on a frozen quote of an older shape (MDPF_SECHIST-CARD-A-COT-BBG-HISTORY.quote.json), so the all-requests read stops at the first such file.",
    "evidence": [
      "investigation row MDPF_DEMQUE-D1-S4"
    ],
    "remedy": "Read an older-shape quote as 'no finish date quoted' instead of raising. Close when: quote_vs_actual.py --all reads all four quote files",
    "owner": "2.0.0_SA_COO~Q1",
    "round": "v7",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~Q1",
      "round": "v7"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Q1",
      "at": null
    },
    "closed": true
  }
]
```
