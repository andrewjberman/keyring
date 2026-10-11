# AMGT_RESAPP -- round 91 remediations (dell1)

<sweep_watermark>2026-10-11T08:20Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T08:20:00Z. Graduated at ADJUDICATION_v111: 2 rows, both ARMED.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S55",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "On the LIVE opal-amgt-scoped-api (CodeSha256 l8egBo/rf.., LastModified 2026-10-11T07:50:33Z, the base after pp-6's rollback), GET /security/<S>/peers over every subject under s3://opal-data-harvest/peers/v1/ (245 listed, 244 served 200, 2242 members, 163 serving a price_currency): 13 member rows, 5 distinct securities, serve the minor-unit code GBp beside a price in POUNDS -- Imperial Brands 24.24, Rio Tinto 69.54, SSE 24.73, BP 5.571, AstraZeneca 120.32 -- each with price_currency_claim null. Read as GBp the label states the price 100x too small. These are numeric-ticker members (AMGT-av-5) whose key reaches a held record whose CRNCY is GBp while the scanner price is in pounds; pp-6 would have added 24 more (GBp 12) and was rolled back for it. Pre-existing, not made by round 91.",
    "evidence": [
      "3.0.0_SA_CVO ran org/tier1_exec/3.0.0_SA_CVO/deliverables/checks/amgt_minor_unit_census.py 2026-10-11T08:1xZ against l8egBo/rf..",
      "adjudication row AMGT_RESAPP-D1-C-S55",
      "ledger/NEVER_WIDEN_ROUND91_REDEPLOY_CTO_HALF.md ADDENDUM 2"
    ],
    "remedy": "A unit-aware currency guard: a minor-unit code (GBp, ZAc, ILA) is never served beside a major-unit price, then one redeploy (CTO ADDENDUM 2). Close when: org/tier1_exec/3.0.0_SA_CVO/deliverables/checks/amgt_minor_unit_census.py run against the live function reads 0 member rows serving a minor-unit code beside a pound price, with a control member that still serves its correct major-unit code.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v91",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v91"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-11T10:15:00Z"
    },
    "closed": true
  },
  {
    "id": "AMGT_RESAPP-D1-W372-S3",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "mechanism": "verify_points_against_excerpt (lib/research/filings/analyze.py) sets a period's block from its label to the next located label or to len(excerpt), so a figure stated for another period later in the excerpt verifies for the last-located period (synthetic: '$21.05 billion in 2025 (2024: $18.08 billion).' verifies 2025 = 18.08). Pre-existing; pp-2 did not widen it.",
    "evidence": [
      "investigation row AMGT_RESAPP-D1-W372-S3",
      "adjudication row AMGT_RESAPP-D1-C-S57"
    ],
    "remedy": "Bound a last-located period's block, with a refusal arm on the synthetic excerpt (packet section 6 item 5). Close when: the synthetic 2025 = 18.08 point is refused, beside a control point stated for its own period that still verifies.",
    "owner": "2.0.0_SA_COO~R1",
    "round": "v91",
    "remediation": {
      "state": "REMEDIATED",
      "owner": "2.0.0_SA_COO~R1",
      "round": "v91"
    },
    "disarm": {
      "state": "DISARMED",
      "owner": "2.0.0_SA_COO~R1",
      "at": "2026-10-11T10:15:00Z"
    },
    "closed": true
  }
]
```
