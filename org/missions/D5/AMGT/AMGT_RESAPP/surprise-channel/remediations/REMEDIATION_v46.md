# AMGT_RESAPP -- FWD-41 read remediation (dell1)

<sweep_watermark>2026-10-16T00:43:06Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-16T04:44:25Z. Graduated at ADJUDICATION_v135 (C-S158): 1 row, ARMED, owner 2.0.0_SA_COO~R2.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S158",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "BLOCKING",
    "hazard_standing": "ARMED",
    "mechanism": "The AIFILL producer keeps a sentence as SUPPORTED when a quote covers only part of it (QXO team_view's $3bn, Apollo and Temasek clause), and it keeps a mgmt sentence that a newer source cited elsewhere on the same page contradicts (HSBA team_view's buyback pause against the 2026 interim buyback). One block prints a run-together word (NG/ 'Pettigrewafter').",
    "evidence": [
      "adjudication row AMGT_RESAPP-D1-C-S158 (ADJUDICATION_v135)"
    ],
    "remedy": "A sentence is SUPPORTED only when every stated fact is in the quote or the source text (a clause-level check), plus the round-107 item (g) cross-block recency rule, then a re-run of the affected names (never a hand edit). Close when: this seat reads five new names drawn by sha256 over that day's date and finds no unsupported or stale claim. The hold stays until then.",
    "owner": "2.0.0_SA_COO~R2",
    "round": "v107",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R2",
      "round": "v107"
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
