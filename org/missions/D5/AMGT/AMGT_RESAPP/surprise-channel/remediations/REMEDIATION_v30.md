# AMGT_RESAPP -- round 84 remediations (dell1)

<sweep_watermark>2026-10-09T11:59Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-09T11:59:00Z. Graduated at ADJUDICATION_v102: 1 row, INERT.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W337-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "r84_store's business-item regex also matches an Item 3.D risk heading containing 'our business', so NU reads 4 business locations where 3 are Item 4.B.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W337-S1",
      "packet s.2 (NU 4 of 39, 3 true 4.B)"
    ],
    "remedy": "Anchor the business match on the item label (4.B), not the phrase. Close when: NU reads 3 of 39 and a planted 3.D 'our business' heading reads 0",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v85",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v85"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  }
]
```
