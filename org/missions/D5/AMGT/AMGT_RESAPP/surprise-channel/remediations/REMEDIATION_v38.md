# AMGT_RESAPP -- round 94 remediations (dell1)

<sweep_watermark>2026-10-11T15:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T15:55:00Z. Graduated at ADJUDICATION_v114: 2 rows, both ARMED.

```json
[
  {
    "id": "AMGT_RESAPP-D1-S24",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "analyze.reverify_stored_thesis_driver re-derives each stored point from its `value`, which AMGT-ff-3 stores rescaled (SAP 2023 = 13.745 for a printed 13,745 million); the excerpt does not print the rescaled figure, so a second re-verification of SAP's already rescaled object keeps 1 of 3 points. Nothing re-verifies SAP today (the ff-5 ledger leg L8 says no operator may).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S24",
      "adjudication row AMGT_RESAPP-D1-C-S76",
      "RA1 finding AMGT_RESAPP.TO-AMGT-ff-5.RESCALED_OBJECT_DEGRADES_ON_REVERIFY.md"
    ],
    "remedy": "The CTO's round-95 first cell: locate a point by its `stated_value` when the stored point carries one (and `held_uncited` the same). Close when: a re-verification of an already rescaled object keeps its 3 of 3 byte-equal, beside a negative arm where a stored value no excerpt prints is held.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v94",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v94"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-11T18:50:00Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-S26",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The classification lookup keys etf-classifications by the bare ticker: CSL AU is served the row for `CSL` (Carlisle Cos Inc: sub_asset_class 'US Large Cap', sector null), and the rank timeseries asked for CSL AU by ticker still names it 'Carlisle Cos Inc' (D1-S25's residual). SAN FP's row (bare `SAN`) reads Health Care; whether that row is Sanofi's or a coincidence is unread.",
    "evidence": [
      "investigation rows AMGT_RESAPP-D1-S26, D1-S25",
      "adjudication rows AMGT_RESAPP-D1-C-S77, D1-C-S78"
    ],
    "remedy": "The CTO's round-95 second cell: when the registered name disagrees with the table row's name for the bare ticker, no field of that row is served for the security and the page says why. Close when: CSL AU serves no Carlisle field on the overlay, the ranked join or the rank timeseries asked by ticker, and SAN FP's classification row is read and shown to be Sanofi's, beside a control whose classification is unchanged.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v94",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v94"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-11T18:50:00Z"
    },
    "closed": true
  }
]
```
