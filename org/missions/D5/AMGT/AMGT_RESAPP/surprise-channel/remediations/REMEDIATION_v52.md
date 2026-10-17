# AMGT_RESAPP -- round 112 remediations (dell1)

<sweep_watermark>2026-10-17T20:31:54Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T20:31:54Z. Graduated at ADJUDICATION_v150 (C-S179): 1 row, owner 2.0.0_SA_COO~R1.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W497-S2",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "priceCurrency.ts returns the header's untrimmed currency code; the old PeersTab helper trimmed it, so a whitespace-padded served currency now reaches the Peers cells as served.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W497-S2",
      "adjudication row AMGT_RESAPP-D1-C-S179 (ADJUDICATION_v150)"
    ],
    "remedy": "The helper trims the served code (or the producer guarantees no padding), with a padded fixture. Close when: a harness case with a padded currency renders the trimmed code in both the header and the Peers table.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v112",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v112"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
