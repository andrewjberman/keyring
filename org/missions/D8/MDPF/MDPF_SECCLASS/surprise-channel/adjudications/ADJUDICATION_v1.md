# MDPF_SECCLASS -- round 1 L8/L9 adjudication

<sweep_watermark>2026-09-30T02:45Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-09-30 ~02:5xZ. L8 packet: 2.0.0_SA_COO~M 103107 (DRAIN_END_R1_20260930.md @ee54196616). Review: org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R1_REVIEW_20260930.md (co-committed). 9 rows: 5 dismissed by the 3 rows below, 4 graduated in remediations/REMEDIATION_v1.md. L9: no swept order carries a JUDGMENT criterion (0 of 6).

```json
[
  {
    "id": "MDPF_SECCLASS-C-S1",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-30T02:55:00Z",
    "one_line": "W3-S1 (PHYS had no canonical row) and W1-S1 (the order text said it did) are resolved: PHYS is a seed row.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W3-S1",
      "MDPF_SECCLASS-W1-S1"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "aws dynamodb get-item etf-classifications PHYS: commodities / Metals / classified_by seed / instrument_kind fund.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "live get-item by this seat 2026-09-30 02:4xZ (PHYS and GLD both seed, commodities/Metals, fund)",
        "release step 1 ledger mdpf-secclass-seed-fields-20260929 (ad921b0c47)",
        "investigation rows MDPF_SECCLASS-W3-S1 and MDPF_SECCLASS-W1-S1",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R1_REVIEW_20260930.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The row the checks assumed now exists, written by the seed path; the BLOCKING check defect was ruled at e31e302afc and fixed in t2. Nothing is left armed."
  },
  {
    "id": "MDPF_SECCLASS-C-S2",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-30T02:55:00Z",
    "one_line": "W3-S2 (a reader of the classifier's private maps) is fixed in t2.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W3-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "build_bd_assets_dim.py at HEAD carries no _ticker_map or _name_map read; lines 164-165 record the removal.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "data/black_diamond/scripts/silver/build_bd_assets_dim.py:164-165 at HEAD, bytes printed",
        "drain of TO-SC-t2 at ae7aa281b0 (2.0.0_SA_COO~M)",
        "investigation row MDPF_SECCLASS-W3-S2 (0.9.0_WK_MDPF_SECCLASS~3)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R1_REVIEW_20260930.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "The only external reader of the private attributes no longer reads them; the row's own disarm condition."
  },
  {
    "id": "MDPF_SECCLASS-C-S3",
    "project": "MDPF_SECCLASS",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-09-30T02:55:00Z",
    "one_line": "W2-S1 (the seed source is a physically copied module) and W2-S2 (three constituent tickers are not stocks) record correct decisions and leave nothing open.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "MDPF_SECCLASS-W2-S1",
      "MDPF_SECCLASS-W2-S2"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "W2-S1 chose a literal over a live import so the copies at yang-generate-etf-returns and opal-partners-data keep importing; those copies are PRD surface rows S12 and S13 under FWD-4. W2-S2 classified SALXX/FXFXX as fund and CASH as absent, per the contract's definitions, with two tests.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "PRD SURFACE MANIFEST S12, S13",
        "org/standards/MDPF_SECCLASS_CONTRACT.json instrument_kind definitions",
        "investigation rows MDPF_SECCLASS-W2-S1 and MDPF_SECCLASS-W2-S2",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/MDPF_SECCLASS_R1_REVIEW_20260930.md (co-committed)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Each is a design note whose remedy already has a home: the copies retire under FWD-4 (S12, S13), and the fund/absent classification is the contract's own rule."
  }
]
```
