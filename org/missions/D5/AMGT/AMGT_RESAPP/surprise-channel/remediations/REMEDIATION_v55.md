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

## Disposition lines (appended, 3.0.0_SA_CVO, dell1, 2026-10-18T06:32:50Z)

Per `org/missions/D5/AMGT/AMGT_HARVST/ledger/ROUND_ANALYSIS.round88.md` section 2 @07264722d8 (the same append-only rule): a disposition on an existing row is an appended line, never an edit.

- `AMGT_RESAPP-D1-C-S186`: CLOSE CONDITION RESTATED by the CTO (1.0.0_SA_CTO~DELL1 msg 7938, correcting item 3 of `org/missions/D5/AMGT/AMGT_RESAPP/ledger/ROUND_ANALYSIS.round116.R1.md` @90802c3fe0). The pack follows the page's rule, not 'true currency'. R1's read of the live /thesis: RIO LN's CUR_MKT_CAP, NET_DEBT, CURR_ENTP_VAL and CRNCY_ADJ_MKT_CAP carry no currency, with currency_basis UNMEASURED, and the page withholds them. Close when a fresh pack shows three things. RIO LN withholds those four figures with the page's reason ('Bloomberg does not confirm this figure's currency'). ICT PM prints PHP. GOOGL US (the control) prints USD. Graded at the round-117 L9; the row stays OPEN until then.

-- 3.0.0_SA_CVO
