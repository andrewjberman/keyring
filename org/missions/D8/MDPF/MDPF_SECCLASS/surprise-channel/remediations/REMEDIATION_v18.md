# MDPF_SECCLASS -- round 28 remediations (dell1)

<sweep_watermark>2026-10-18T01:53:27Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T01:53:27Z. Graduated at ADJUDICATION_v29 (C-S34): 2 rows, owner 2.0.0_SA_COO~M1.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-W100-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "A NAME:: classification row for LORD ABBETT CONVERTIBLE I classes it cash, while the ruled class for its ticker LCFYX is fixed_income.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-W100-S3",
      "adjudication row MDPF_SECCLASS-D1-C-S34 (ADJUDICATION_v29)"
    ],
    "remedy": "The NAME:: row agrees with the ruled ticker class, or is retired. Close when: one read of the classification table shows the two agree.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v28",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v28"
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S52",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "E_18 skips a holdings name found in gold/dimensions/ticker_resolution.parquet (one version, 2026-04-07T21:54:55Z, writer classification/resolve_tickers.py), so the nine held-out names stay invisible to it as 'already resolved'.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S52",
      "adjudication row MDPF_SECCLASS-D1-C-S34 (ADJUDICATION_v29)"
    ],
    "remedy": "Refresh or re-key the resolution table, or have E_18 not treat an April resolution as current. Close when: E_18's own output names the nine held-out tickers as candidates or rules them out by class.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v28",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v28"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
