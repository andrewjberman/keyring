# MDPF_SECCLASS -- round 29 remediations (dell1)

<sweep_watermark>2026-10-19T14:52:17Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-19T14:52:17Z. C-S37 is the disarm row for D1-S42. Graduated at ADJUDICATION_v30 (C-S36): W104-S2 (ARMED), S53, S55; owner 2.0.0_SA_COO~M1.

```json
[
  {
    "id": "MDPF_SECCLASS-D1-C-S37",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "D1-S42: E_18 silently held tickers out of classification (old-list-only, then the April name-to-ticker table). Since TO-SC-e116b (served 2026-10-18T06:46:32Z), E_18 prints 'Held out by the resolution table ...' with each ticker named on every scheduled fire.",
    "evidence": [
      "adjudication row MDPF_SECCLASS-D1-C-S35 (ADJUDICATION_v30)",
      "s3://opal-data-bd/gold/logs/chain_full_20261019_040119.log (E_18 at 2026-10-19T05:07:28Z, lines 4819-4847)",
      "remediation row MDPF_SECCLASS-D1-S42 (REMEDIATION_v17)"
    ],
    "remedy": "None further for the silence: the held-out names print on every fire. The classification half stays on REMEDIATION_v17 S42 and REMEDIATION_v19 S55. Close when: this seat has read the display on a scheduled fire, which is met.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v29",
    "disarms": [
      "MDPF_SECCLASS-D1-S42"
    ],
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": "2026-10-19T05:07:28Z"
    },
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v29"
    },
    "closed": true
  },
  {
    "id": "MDPF_SECCLASS-D1-W104-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The opal-partners-data classifier (etf_classifier.py classify(), lines 64-107) returns the matched table's asset_class verbatim, mapping only 'hedge' to 'alternatives'. The returnable set is wider than the round-28 pre-read's three classes plus empty, and a repoint to etf-classifications would add client-visible classes (Structured 527 keys, Commodities 164) and move cash from 15 to 396 keys.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-W104-S2",
      "adjudication row MDPF_SECCLASS-D1-C-S36 (ADJUDICATION_v30)"
    ],
    "remedy": "The round-30 repoint cell under its own pair: six canonical classes, no code fold (the CTO's ruling, msg 7959); the client-facing apply waits on Andrew's word. Close when: the repointed handler returns only the six classes on a full census of its keys, and the apply is on file with Andrew's word.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v29",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v29"
    },
    "closed": false,
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~M1",
      "at": null
    }
  },
  {
    "id": "MDPF_SECCLASS-D1-S53",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The served mix_daily_summary TOTAL rises by about $32k less than the canonical holdings on Monday to Thursday dates (residue -31,616.79 to -32,192.93) and by exactly as much on Friday to Sunday (residue 0.00), for 2026-10-01 to 2026-10-14. What C_06 leaves out of the TOTAL on weekdays is not read.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S53",
      "adjudication row MDPF_SECCLASS-D1-C-S36 (ADJUDICATION_v30)"
    ],
    "remedy": "Name the weekday-dependent term (a component C_06 adds or drops by day of week). Close when: the residue is 0.00 on every date of a 14-date reconciliation, or the term is named and ruled as intended.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v29",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v29"
    },
    "closed": false
  },
  {
    "id": "MDPF_SECCLASS-D1-S55",
    "project": "MDPF_SECCLASS",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The April name-to-ticker resolution table (rows from 2026-04-07) holds 14 real tickers out of scheduled classification (the nine plus FPE, TRRJX, VTTVX, WTM, XPMIX), because their ticker is absent from the canonical etf-classifications table; the set grows with the holdings.",
    "evidence": [
      "investigation row MDPF_SECCLASS-D1-S55",
      "adjudication row MDPF_SECCLASS-D1-C-S36 (ADJUDICATION_v30)"
    ],
    "remedy": "The CTO rules whether the table still gates candidacy once a ticker is absent from etf-classifications. Close when: E_18's held-out count reads 0 on a scheduled fire, or the ruling that keeps the gate is on file.",
    "owner": "2.0.0_SA_COO~M1",
    "round": "v29",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~M1",
      "round": "v29"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
