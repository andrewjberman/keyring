# IRPT_DASHBD -- round 28 remediations

<sweep_watermark>2026-10-08T18:4xZ</sweep_watermark>

Author: 3.0.0_SA_CVO (seated on dell2), 2026-10-08. Graduated at round 28's L9 (ADJUDICATION_v14.md), round label v29: W27-S2, S34, both OPEN.

```json
[
  {
    "id": "IRPT_DASHBD-W27-S2",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "Batching bounds the lots stage under the 2,048 MB limit (1,713-1,735 MB) but the peak is flat across batch sizes, so something other than the batch sets it; batch 250 totals 905.7 s, over 900. Measured on pandas 3.0.6, not the served 2.2.3.",
    "evidence": [
      "investigation row IRPT_DASHBD-W27-S2 (BATCHED_E2.json, 7,604 accounts, 2026-10-06)"
    ],
    "remedy": "Pick the batch size with headroom on both axes (1,000: 768.9 s, 1,735 MB) and re-measure once on the served pandas 2.2.3 before the release; find the flat-peak component (the balance-history scan is the candidate) if headroom is thin.",
    "owner": "2.0.0_SA_COO~D2",
    "round": "v29",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~D2",
      "round": "v29"
    },
    "closed": false
  },
  {
    "id": "IRPT_DASHBD-S34",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "DB-b-49's recompose control misses on 440 of 2,299 accounts (max 724.16 pp): BD's two split halves chained do not reproduce BD's own full-segment gross within 0.35 pp, so on those accounts branch B's right-half gap is not yet readable as Opal vs BD.",
    "evidence": [
      "investigation row IRPT_DASHBD-S34 (TIEOUT_SPLIT_E1.json)",
      "record @599852f130"
    ],
    "remedy": "Class the 440 (and the 724.16 pp outlier) and measure their overlap with the 1,868 right-half misses, before any Opal-side repair is cut from branch B.",
    "owner": "1.0.0_SA_CTO~DELL2",
    "round": "v29",
    "remediation": {
      "state": "OPEN",
      "owner": "1.0.0_SA_CTO~DELL2",
      "round": "v29"
    },
    "closed": false
  }
]
```
