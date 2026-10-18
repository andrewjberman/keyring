# AMGT_RESAPP -- round 115 remediations (dell1)

<sweep_watermark>2026-10-18T03:57:08Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-18T03:57:08Z. Graduated at ADJUDICATION_v153 (C-S185): 1 row, owner 2.0.0_SA_COO~R1.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S186",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The printed pack's header labels 'Market value, currency-adjusted' as USD and 'Market cap' with the trading currency, whatever the value's real unit: ICT PM prints a PHP value as 'USD 1,735,465.1 million', and RIO LN prints a USD value as 'GBp 115,578.9 million'.",
    "evidence": [
      "adjudication row AMGT_RESAPP-D1-C-S184 (ADJUDICATION_v153)",
      "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round115/packs/ICT_PM_Equity_pack.pdf page 1",
      "org/missions/D5/AMGT/AMGT_RESAPP/deliverables/2.0.0_SA_COO~R1/round115/packs/RIO_LN_Equity_pack.pdf page 1"
    ],
    "remedy": "Each pack figure carries the unit its source states (CRNCY_ADJ_MKT_CAP in the requested currency; market cap in the trading currency's units), with a census of every currency-labelled header field. Close when: a fresh ICT PM and RIO LN pack prints each market-value line in its true currency, and the census names no other mislabel.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v115",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v115"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
