# AMGT_RESAPP -- round 95 AC2 grade restated under the full to_id (dell1)

<sweep_watermark>2026-10-11T18:55Z</sweep_watermark>

Author: 3.0.0_SA_CVO (dell1), 2026-10-11T18:55:00Z. One row: ADJUDICATION_v115's C-S84 graded aa-3 AC2 MET but named the order by its short
form, which round-close-check does not match for a generic criterion id. This row restates the same grade under the full to_id. No grade changes.

```json
[
  {
    "id": "AMGT_RESAPP-D1-C-S89",
    "project": "AMGT_RESAPP",
    "fabric": "dell1",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T18:55:00Z",
    "one_line": "JUDGMENT AMGT_RESAPP.TO-AMGT-aa-3.read-the-two-compare-500s-to-their-cause AC2: MET -- the grade written in row AMGT_RESAPP-D1-C-S84 (ADJUDICATION_v115 @0b4cff88c7), restated under the order's full to_id. round-close-check matches a generic criterion id only beside the full to_id, and C-S84 named the order by its short form (AMGT_RESAPP.TO-AMGT-aa-3), so the check read the criterion UNGRADED. The grade and its measured-versus-inferred split are unchanged; see C-S84.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "AMGT_RESAPP-D1-C-S84"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every judgment graded by a seat that did none of the work.",
    "world_is": "JUDGMENT AMGT_RESAPP.TO-AMGT-aa-3.read-the-two-compare-500s-to-their-cause AC2: MET -- the grade written in row AMGT_RESAPP-D1-C-S84 (ADJUDICATION_v115 @0b4cff88c7), restated under the order's full to_id. round-close-check matches a generic criterion id only beside the full to_id, and C-S84 named the order by its short form (AMGT_RESAPP.TO-AMGT-aa-3), so the check read the criterion UNGRADED. The grade and its measured-versus-inferred split are unchanged; see C-S84.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "adjudication row AMGT_RESAPP-D1-C-S84 @0b4cff88c7",
        "3.0.0_SA_CVO python .tools/round-close-check.py --project AMGT_RESAPP --round 95 after @0b4cff88c7: AC2 UNGRADED (no CVO-kind row names it)",
        ".tools/round-close-check.py:420-424 (a generic AC id must sit beside the full to_id or 'TO-' + the text after '.TO-')"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "JUDGMENT AMGT_RESAPP.TO-AMGT-aa-3.read-the-two-compare-500s-to-their-cause AC2: MET -- the grade written in row AMGT_RESAPP-D1-C-S84 (ADJUDICATION_v115 @0b4cff88c7), restated under the order's full to_id. round-close-check matches a generic criterion id only beside the full to_id, and C-S84 named the order by its short form (AMGT_RESAPP.TO-AMGT-aa-3), so the check read the criterion UNGRADED. The grade and its measured-versus-inferred split are unchanged; see C-S84."
  }
]
```
