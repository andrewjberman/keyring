# AMGT_RESAPP -- round 113 remediations (dell1)

<sweep_watermark>2026-10-17T22:22:35Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-17T22:22:35Z. Graduated at ADJUDICATION_v151 (C-S181): 3 rows.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W502-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "PeersTab.tsx passes the served PX_LAST currency to formatStatValue for the subject price cell outside priceCurrency.ts, so bt-3's trim does not reach it.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W502-S1",
      "adjudication row AMGT_RESAPP-D1-C-S181 (ADJUDICATION_v151)"
    ],
    "remedy": "The subject price cell reads the shared helper. Close when: a padded-currency harness case renders the subject cell trimmed (this also closes REMEDIATION_v52 W497-S2).",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v113",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v113"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W503-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "bt-6 opens the last min(12, floor(N/2)) rows' tooltips upward; on a grid under about 20 rows an upward bubble can still clip at the scroller's top (arithmetic, unmeasured).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W503-S1",
      "adjudication row AMGT_RESAPP-D1-C-S181 (ADJUDICATION_v151)"
    ],
    "remedy": "A short-grid case measured on a built page. Close when: a walk of a name with under 20 figure rows reads no occluded-popover finding, or the bound is changed and so graded.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v113",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v113"
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-S60",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "mechanism": "The walker's layout:clipped check counts every horizontally scrolling container in headless Chromium, so a scrolling overflow-x-auto grid reads as clipped text (ruled not clipped by the CTO, msg 7741).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S60",
      "adjudication row AMGT_RESAPP-D1-C-S181 (ADJUDICATION_v151)"
    ],
    "remedy": "The probe excludes a scrolling container from layout:clipped. Close when: a walk of RIO LN's grid reads no layout:clipped finding for it.",
    "owner": "the ui-walk walker's owner",
    "round": "v113",
    "remediation": {
      "state": "OPEN",
      "owner": "the ui-walk walker's owner",
      "round": "v113"
    },
    "closed": false
  }
]
```

-- 3.0.0_SA_CVO
