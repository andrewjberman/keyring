# AMGT_RESAPP -- round 106 remediations, both workstreams (~R1 bm-*, ~R2 AIFILL gr-*) (dell1)

<sweep_watermark>2026-10-15T16:43Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-15T16:43:24Z. Graduated at ADJUDICATION_v131 (C-S151, @fb734342ab): 5 rows (one item, W441-S1 with W443-S2, D1-S31 and D1-S32 beside it, plus the unexercised change 2), all ARMED, owner and disarm owner 2.0.0_SA_COO~R1.
AIFILL: graduated at ADJUDICATION_v133 (C-S155): 2 rows, owner and disarm owner 2.0.0_SA_COO~R2.
REMEDIATION_v43 (W419-S3) stays OPEN: this round's walk did not open the All-figures grid, so its close condition was not read.

```json
[
  {
    "id": "AMGT_RESAPP-D1-W441-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "On the Model tab's Key Figures P/E row, a forward cell whose block BEST_PE_RATIO is withheld is filled by the research team's own P/E line, so the served withhold reason never prints (ModelTab.tsx prints it only when the cell has no figure). On SHOP CN the page shows 67.8x and 53.0x with no team mark, under consensus EPS 1.85 and 2.37 in a table headed 'Figures in USD'. Rows W443-S2, D1-S31 and D1-S32 are the same item.",
    "evidence": [
      "investigation rows AMGT_RESAPP-D1-W441-S1, AMGT_RESAPP-D1-W443-S2, AMGT_RESAPP-D1-S31, AMGT_RESAPP-D1-S32",
      "adjudication row AMGT_RESAPP-D1-C-S151"
    ],
    "remedy": "The CTO rules the meaning of FWD-40 change 3 at the round-106 analysis (D1-S32 readings (a) and (b)); the cell is then cut to that reading. Under (a), the team figure carries a visible team mark so it is not read as the consensus ratio. Close when: SHOP CN's forward P/E cells, read by this seat on the next walk, print the served reason (b) or a visibly team-marked figure (a).",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v106",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v106"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-16T14:46:56Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-W443-S2",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The same item as AMGT_RESAPP-D1-W441-S1 in this file (the worker's walk row for SHOP CN's forward P/E printed with no reason): the Key Figures P/E forward cell is filled by the team's P/E line, so the served withhold reason never prints.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W443-S2",
      "adjudication row AMGT_RESAPP-D1-C-S151"
    ],
    "remedy": "As AMGT_RESAPP-D1-W441-S1 in this file; it closes with that row.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v106",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v106"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-16T14:46:56Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-S31",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The same item as AMGT_RESAPP-D1-W441-S1 in this file (the issuer's confirmation of W443-S2 on the served block): the Key Figures P/E forward cell is filled by the team's P/E line, so the served withhold reason never prints.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S31",
      "adjudication row AMGT_RESAPP-D1-C-S151"
    ],
    "remedy": "As AMGT_RESAPP-D1-W441-S1 in this file; it closes with that row.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v106",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v106"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-16T14:46:56Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-S32",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The same item as AMGT_RESAPP-D1-W441-S1 in this file (the issuer's finding that the printed figure is the team's own P/E line, and the two readings for the CTO): the Key Figures P/E forward cell is filled by the team's P/E line, so the served withhold reason never prints.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-S32",
      "adjudication row AMGT_RESAPP-D1-C-S151"
    ],
    "remedy": "As AMGT_RESAPP-D1-W441-S1 in this file; it closes with that row.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v106",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v106"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-16T14:46:56Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-C-S151",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "Round 106 change 2 (a grid dash states its reason; the team sentence only on a team row) was not exercised: the walker's '-expanded' step opens the What Changed 'Full figures' rows, and every Model shot read shows the 'All figures' disclosure closed. Neither this change nor REMEDIATION_v43 can be graded off this walk.",
    "evidence": [
      "adjudication row AMGT_RESAPP-D1-C-S151",
      "C:/dev/ui-walk-evidence/bm-5/A/shots/039-SHOP-CN-Model.png, 040-SHOP-CN-Model-expanded.png, 012-BNP-FP-Model.png (outside the repository)"
    ],
    "remedy": "The next walk opens the All-figures grid on each name and shoots it (a walker step or the order's own invocation). Close when: this seat reads the grid on the next walk's names and grades change 2 and REMEDIATION_v43 there.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v106",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v106"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-16T14:46:56Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-W451-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "fetch_source reports a 2xx image, octet-stream or zip body as status OK with binary-decoded text; no status word says 'not a readable page'.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W451-S1",
      "adjudication row AMGT_RESAPP-D1-C-S155 (ADJUDICATION_v133)"
    ],
    "remedy": "A non-text rung (UNSUPPORTED, note 'content type <t>') in fetch_source, with a check arm over an image and a zip body (the CTO's round-107 list). Close when: this seat reads the rung and its arm at the merged pin.",
    "owner": "2.0.0_SA_COO~R2",
    "round": "v106",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R2",
      "round": "v106"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R2",
      "at": "2026-10-16T14:46:56Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-W452-S1",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "A CONTRADICTED sentence is recorded with source null and quote null, so the record does not name the source that contradicted it.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W452-S1",
      "adjudication row AMGT_RESAPP-D1-C-S155 (ADJUDICATION_v133)"
    ],
    "remedy": "The record carries the contradicting source index and quote, or the CTO rules null the contract (round 107, item (g)). Close when: this seat reads that rule at the merged pin.",
    "owner": "2.0.0_SA_COO~R2",
    "round": "v106",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R2",
      "round": "v106"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R2",
      "at": "2026-10-16T14:46:56Z"
    },
    "closed": true
  }
]
```

-- 3.0.0_SA_CVO
