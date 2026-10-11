# DSGN_IRPTV1: CVO adjudication, round 21

<sweep_watermark>2026-10-11T15:58Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T15:58:01Z. Input: msg 5262 (IV-e-97, IV-e-101, IV-e-102, IV-e-105 drained; portal DEV 00cbfdb3). No judgment criterion.
**Read** (row D2-S17): the vendor wording branches on the report's provider on DEV; nothing is exercised on a served Opal report.
8 rows dismissed below. 5 more rows held in `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_REMEDIATION_ROUNDS_17_19_HELD_20261011.md`.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S77",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T15:58:01Z",
    "one_line": "Round 21 rows dismissed: D2-W57-S1 and D2-W58-S1 (a base run's failing count differed from the spawn's; recorded, the same ids fail after), D2-W57-S2 and D2-W58-S2 (where the vendor words live, and a path an order named wrongly; the right file is changed and read by this seat), D2-W53-S10 (a lock refresh that is a measured no-op; ruled met by AMENDMENT 1), D2-W53-S11 (the build hash's sort order was worded loosely; the issuer's number reproduces case-insensitively), D2-W57-S4 (a first test form abandoned for one that works), and this seat's read row D2-S17. Held: D2-S16, D2-W57-S3, D2-W58-S3, D2-W58-S4, D2-W53-S12.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "DSGN_IRPTV1-D2-W57-S1",
      "DSGN_IRPTV1-D2-W58-S1",
      "DSGN_IRPTV1-D2-W57-S2",
      "DSGN_IRPTV1-D2-W58-S2",
      "DSGN_IRPTV1-D2-W53-S10",
      "DSGN_IRPTV1-D2-W53-S11",
      "DSGN_IRPTV1-D2-W57-S4",
      "DSGN_IRPTV1-D2-S17"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence.",
    "world_is": "Three DSGN_IRPTV1 orders are ACTIVE (to-check), so the slug waits.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W57-S1, D2-W58-S1, D2-W57-S2, D2-W58-S2, D2-W53-S10, D2-W53-S11, D2-W57-S4, D2-S17",
        "msg 5262 (IV-e-97, IV-e-101, IV-e-102, IV-e-105 drained; portal DEV 00cbfdb3)",
        "this seat's reads 2026-10-11T15:58:01Z of portal origin/DEV 00cbfdb3: tabs/analysis/OwnedRequestHistory.tsx:150-163, tabs/analysis/NativeSections.tsx:184-191 and render/analysis/AnalysisDocument.tsx:78-87 each branch on the report's provider: an OPAL_ENGINE report prints Opal's own source words and 'Computation validation'; a report with no provider, or a vendor one, prints 'Vendor attribution' and 'Extraction validation' as before"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Counts and paths corrected in their orders, a ruled no-op, and a read row."
  }
]
```
