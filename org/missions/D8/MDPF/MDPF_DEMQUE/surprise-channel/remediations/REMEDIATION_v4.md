# MDPF_DEMQUE -- round 5 remediations

<sweep_watermark>2026-10-09T12:32Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T12:32:00Z. Graduated at ADJUDICATION_v5: 2 rows, both INERT.

```json
[
  {
    "id": "MDPF_DEMQUE-D1-W13-S1",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The history channel's reserve (40 cells) counts only the static producer names, while the ledger shows one day draws 5,858 history cells, so the quoted allowance overstates what a backfill may draw (FWD-3 reserve below production's real draw).",
    "evidence": [
      "investigation row MDPF_DEMQUE-D1-W13-S1"
    ],
    "remedy": "Seed the history reserve from the ledger's measured daily history draw plus a margin (C-RESERVE). Close when: the history reserve reads at or above the measured draw on the ledger",
    "owner": "2.0.0_SA_COO~Q1",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Q1",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Q1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "MDPF_DEMQUE-D1-S3",
    "project": "MDPF_DEMQUE",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Yahoo's dividend list misses some cash Bloomberg's total return carries (LNVGY, DIVZ, IDVZ: one payment each in the window), and Yahoo shows money-market funds at 0 total return where Bloomberg accrues daily.",
    "evidence": [
      "investigation row MDPF_DEMQUE-D1-S3",
      "org/missions/D8/MDPF/MDPF_DEMQUE/deliverables/0.9.0_WK_MDPF_DEMQUE~15/TR_COMPARISON.md Findings 2 and 5"
    ],
    "remedy": "Carry the TR method's two guards: flag a non-ex-date gap larger than rounding against Bloomberg's stored TR as a missing cash row, and source money-market TR from Bloomberg or an accrual. Close when: both guards are in the TR column's build",
    "owner": "2.0.0_SA_COO~Q1",
    "round": "v6",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~Q1",
      "round": "v6"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~Q1",
      "at": null
    },
    "closed": false
  }
]
```
