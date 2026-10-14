# AMGT_RESAPP -- round 104 (~R1's keys) remediations (dell1)

<sweep_watermark>2026-10-14T02:00Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-14T02:00:00Z. Graduated at ADJUDICATION_v128: 4 rows, ARMED, owner and disarm owner 2.0.0_SA_COO~R1.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S142",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "Two broken values the walker's classes do not catch: PBR US team-model rows print a dollar sign on BRL figures under 'Figures in BRL'; BATS LN's segment tables carry an empty column headed 'Period 4' with no reason.",
    "evidence": [
      "adjudication rows AMGT_RESAPP-D1-C-S137, D1-C-S142",
      "C:/dev/ui-walk-evidence/bk-5/{A,B,C} (outside the repository; never committed)"
    ],
    "remedy": "The team-model rows print the currency their section states (or none); a segment period with no label or values is dropped or states its reason. Close when: the next ten-name walk, read by this seat, shows none of it.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v104",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v104"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W418-S2",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "PBR US prints forward P/E 5.2x and 6.3x beside a USD price and BRL EPS with no currency note; the printed figures do not reproduce them.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W418-S2",
      "adjudication row AMGT_RESAPP-D1-C-S139"
    ],
    "remedy": "The P/E row states its basis (currency conversion and the ADR ratio) or is withheld with a reason, as bk-4 does for cross-currency fiscal P/E. Close when: the next ten-name walk, read by this seat, shows none of it.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v104",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v104"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W418-S3",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The historical 2025 P/E is FY-end price over EPS but the FY-end price is not printed, so a reader recomputes another figure (GOOGL US 28.7x against 32.2x; ISP IM 11.2x against 11.7x).",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W418-S3",
      "adjudication row AMGT_RESAPP-D1-C-S139"
    ],
    "remedy": "The historical P/E prints its price basis (the FY-end price and date). Close when: the next ten-name walk, read by this seat, shows none of it.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v104",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v104"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  },
  {
    "id": "AMGT_RESAPP-D1-W418-S4",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "The Model tab's Key Figures table prints '--' with no reason on all ten names (forward margins, EV/EBITDA, ROE, debt; current-year P/E on non-December fiscal years), though the full table beside it footnotes the same gaps.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W418-S4",
      "adjudication row AMGT_RESAPP-D1-C-S139"
    ],
    "remedy": "Every Key Figures dash shows its reason in words, as the header tiles now do. Close when: the next ten-name walk, read by this seat, shows none of it.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v104",
    "remediation": {
      "state": "OPEN",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v104"
    },
    "disarm": {
      "state": "ARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": null
    },
    "closed": false
  }
]
```
