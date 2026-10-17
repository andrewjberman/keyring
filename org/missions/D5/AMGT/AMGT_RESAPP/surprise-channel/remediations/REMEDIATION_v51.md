# AMGT_RESAPP -- round 111 remediations (dell1)

<sweep_watermark>2026-10-17T18:55:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T18:55:45Z. Graduated at ADJUDICATION_v149 (C-S177): 3 rows, owner 2.0.0_SA_COO~R1.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W494-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The stored model-block 'unresolved' reasons that can reach the P/E not shown footer come from a producer not read at source; the footer's safety net replaces an unknown token with 'a vendor figure', unmeasured on a live stored row.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W494-S1",
      "adjudication row AMGT_RESAPP-D1-C-S177 (ADJUDICATION_v149)"
    ],
    "remedy": "Read the producer at source and list every token it can emit. Close when: each is mapped to plain words or shown not to reach the footer.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v111",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v111"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W495-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "On the rendered Peers tab, a USD-priced control's member Price cell prints '148.07 currency not stated'.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W495-S1",
      "adjudication row AMGT_RESAPP-D1-C-S177 (ADJUDICATION_v149)"
    ],
    "remedy": "A Price cell names its currency when the served figure carries one. Close when: a walk of the Peers tab on a USD name reads the currency, or a ruling says why it is not stated.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v111",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v111"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W495-S2",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "HeaderCards.tsx falls back to CRNCY when PX_LAST has no currency, while PeersTab.tsx reads PX_LAST only, so the header and the Peers table can name different price currencies on one name.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W495-S2",
      "adjudication row AMGT_RESAPP-D1-C-S177 (ADJUDICATION_v149)"
    ],
    "remedy": "One rule for the page's price currency, shared by the header and the Peers table. Close when: both read the same rule, with a test on a name whose PX_LAST has no currency.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v111",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v111"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
