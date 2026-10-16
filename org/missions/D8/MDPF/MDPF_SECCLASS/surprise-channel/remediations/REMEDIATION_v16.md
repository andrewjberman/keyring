# MDPF_SECCLASS -- round 26 remediations (dell1)

<sweep_watermark>2026-10-16T04:12:29Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-16T04:12:29Z. Graduated at ADJUDICATION_v26 (C-S29): W93-S2, ARMED, owner 2.0.0_SA_COO~M1.
REMEDIATED here: W92-S4 (REMEDIATION_v15), met in round 26.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-W93-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "E_18 writes the canonical row for a bd-only ticker with an asset_class taken from the old list; repointing the lookup yields None, so the input can only be removed.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-W93-S2",
      "adjudication row MDPF_SECCLASS-D1-C-S29 (ADJUDICATION_v26)"
    ],
    "remedy": "Measure how many bd-only tickers a nightly E_18 run writes with an old-list class, then the round-27 build removes the input with a stated consequence. Close when: this seat reads the measurement and the merged build.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v26",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v26"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
