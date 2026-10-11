# DSGN_IRPTV1: CVO adjudication, rounds 18 and 20 and IV-e-95

<sweep_watermark>2026-10-11T13:35Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T13:35:10Z. Input: msg 5015 (IV-e-95 drained @85b3758e3f; round 20 IV-e-100 @7914dec2a5; round 18 IV-e-98 @9a574656d7). No judgment criterion.
**Read** (row D2-S15): the deletion of five hand-added types is sound, re-run by this seat. 9 rows dismissed below.
5 more rows held in `org/tier1_exec/3.0.0_SA_CVO/deliverables/DSGN_IRPTV1_REMEDIATION_ROUNDS_17_19_HELD_20261011.md`.

```json
[
  {
    "id": "DSGN_IRPTV1-C-S76",
    "project": "DSGN_IRPTV1",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T13:35:10Z",
    "one_line": "Rounds 18 and 20 and IV-e-95, rows dismissed: D2-W53-S1, S3 and S4 (three correct stops, each on a count the order had wrong; answered by its amendments, the smoke map lands at 17 of 22 with five named excuses), D2-W53-S9 (one extra failing id is a timeout that passes alone), D2-W54-S2 (18 type errors, not 13; all fixed, typecheck 0 by the worker), D2-W54-S3 (the three exports deleted on a zero-consumer count; re-run by this seat and sound), D2-W54-S4 (the suite leaves the tree clean), D2-W56-S1 (an order's premise about the sections reader was false; the reader already branches on provider), and this seat's read row D2-S15. Held: D2-W53-S2, D2-W53-S8, D2-W54-S1, D2-W56-S2, D2-W56-S3.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "DSGN_IRPTV1-D2-W53-S1",
      "DSGN_IRPTV1-D2-W53-S3",
      "DSGN_IRPTV1-D2-W53-S4",
      "DSGN_IRPTV1-D2-W53-S9",
      "DSGN_IRPTV1-D2-W54-S2",
      "DSGN_IRPTV1-D2-W54-S3",
      "DSGN_IRPTV1-D2-W54-S4",
      "DSGN_IRPTV1-D2-W56-S1",
      "DSGN_IRPTV1-D2-S15"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Rounds 18 and 20 read MAY-CLOSE. Round 17 is open and three orders are ACTIVE (to-check), so the slug waits.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-W53-S1, D2-W53-S3, D2-W53-S4, D2-W53-S9, D2-W54-S2, D2-W54-S3, D2-W54-S4, D2-W56-S1, D2-S15",
        "msg 5015 (IV-e-95 drained @85b3758e3f; round 20 IV-e-100 @7914dec2a5; round 18 IV-e-98 @9a574656d7)",
        "this seat's reads 2026-10-11T13:35:10Z: portal origin/DEV is 1f0b1d68, the wire-folder candidate, so it HAS landed since the issuer's send; word-boundary search on it: the three exported names (AnalysisReportResponseDataWire, AnalysisReportOpalResponseDataWire, WIRE_CONSUMED_OPAL_FIELDS) occur in 0 files; the two aliases occur only as local type declarations in contracts/adapt.ts:929-930 and one test; at the base 73806e29 the only file outside the wire folder naming any of the five was one test, in a comment (fe-s-47/no-status-reason.test.ts:152); positive control: OwnedAnalysisRequestWire is named by 9 files outside the folder"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "Correct stops answered by amendment, counts corrected and fixed in the order, a deletion re-checked, and a read row."
  }
]
```
