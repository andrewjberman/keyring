# ADVI_COTBKF: CVO adjudication

Round 1 L8 compile and L9 adjudication by `3.0.0_SA_CVO`, on 1.0.0_SA_CTO msg 105715 (your watermark is ABSENT; start L8).
Channel read at 0c24382325: 5 rows (S1, W1-S1, W2-S1, S2, S3), 0 ARMED. Round-1 orders TO-CB-a-1, a-2 and a-3 are all
`complete`, and none carries a JUDGMENT criterion, so L9 grades nothing beyond the rows. After this document, 0 rows are
undispositioned. Round 2 (TO-CB-b-1..4) was issued at 57c1676b89; its rows belong to the next compile.

```json
[
  {
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-06T20:30Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "ADVI_COTBKF-C-S1",
    "one_line": "ROUND-1 L9: three rows GRADUATED into PRD v0.4 and the round-2 issuance -- every delivered record kept (W2-S1, S3) and FWD-1 bounded by the delivery with FWD-9 added (S2).",
    "spec_asserts": "W2-S1: silver dropped 1,360 record-level repeats under the round-1 rule. S3: v0.4 first counted 1,416,500 lines, not 1,416,497 records. S2: no account spans 2013 to 2026, so FWD-1 as worded could not be exercised.",
    "world_is": "PRD v0.4 @51a7c07278: C-SILVER keeps every record, with the row count equal to the record count. FWD-1 reads \"as far back as Commonwealth recorded it\", and FWD-9 follows a client across a Commonwealth account change. Ratified-text half signed at current bytes (review @03c2d28c0e). Round-2 order TO-CB-b-1 (issuance 57c1676b89) expects rows_out=1416497 dropped_dup=0 records=1416497 rows_eq_records=True, citing W2-S1 and S3.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md@51a7c07278 (C-SILVER; FWD-1; FWD-9)",
        "org/missions/D8/ADVI/ADVI_COTBKF/task-orders/ADVI_COTBKF.TO-CB-b-1.transactions-every-record.md@57c1676b89 (criterion CB2b1-AC2 expect line)",
        "org/tier1_exec/3.0.0_SA_CVO/deliverables/ADVI_COTBKF_PRD_v0.1_RATIFIED_TEXT_REVIEW_20261006.md@03c2d28c0e"
      ]
    },
    "adjudicates": [
      "ADVI_COTBKF-W2-S1",
      "ADVI_COTBKF-S3",
      "ADVI_COTBKF-S2"
    ],
    "disposition": "GRADUATED"
  },
  {
    "project": "ADVI_COTBKF",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-06T20:30Z",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "id": "ADVI_COTBKF-C-S2",
    "one_line": "ROUND-1 L9: two rows are RECORDS needing no remedy -- one portfolio zip, not two (S1), and the naming scope read through lookup() with the same keys (W1-S1).",
    "spec_asserts": "S1: the thread named a transactions zip and a performance zip. W1-S1: the order typed the literal scope \"cottonwood\", which the LGIC naming gate refuses.",
    "world_is": "S1: the delivery has one portfolio-accounting zip; round 1 landed it, and its SHA-256 equals both the manifest and Andrew's Files.zip member (the CTO's own read in the v0.4 addendum). No outcome depends on two zips. W1-S1: lookup(\"cottonwood\")[\"long\"] returns the same value, so the keys are unchanged. The builder's opal-data-assets home for source commonwealth is C-HOMES; the firm bucket opal-data-cottonwood is only C-SENSITIVE's declared R20 exception for the CRM zip.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "org/missions/D8/ADVI/ADVI_COTBKF/prd/ADVI_COTBKF_PRD.md@51a7c07278 (v0.4 addendum: bronze SHA-256 a3a2772e... equal to manifest and Files.zip member; C-HOMES; C-SOURCE exception)"
      ]
    },
    "adjudicates": [
      "ADVI_COTBKF-S1",
      "ADVI_COTBKF-W1-S1"
    ],
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Both rows record a premise the world corrected inside the round, with no outcome changed. S1 is wording in the thread; W1-S1 is the gate doing its job, with identical keys."
  }
]
```
