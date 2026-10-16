# IRPT_DASHBD: CVO grade record, round 131 (workstream F-SHIP, ~F2): the two judgment criteria by their full ids

<sweep_watermark>2026-10-16T12:08Z</sweep_watermark>

A NEW item citing IRPT_DASHBD-D2-C-S75 (ADJUDICATION_v140.md @d8a70da54d), which stands unedited. That row graded both judgment criteria of round 131 but named them 'J1' and 'J2', not by their full ids, so the round-close gate read them as ungraded. This row restates the same two grades by full id; no grade, finding or held item changes.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S78",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~IRPT",
  "surfaced_at": "2026-10-16T12:08:00Z",
  "one_line": "Round 131 F-SHIP (~F2), the grades of IRPT_DASHBD-D2-C-S75 restated by full id. L9 DBF131-1-J1 PASS, 20 of 20 (Cottonwood, natural key, unique-key rows, census 37,478 rows in 18,501 non-unique keys reproduced). L9 DBF131-1-J2 PASS, 20 of 20 (Inflection, Complete rows, natural key, census 1,036,824 rows in 477,446 non-unique keys reproduced). The four held decisions and W1701-S6 stand as written in C-S75.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-C-S75"
  ],
  "spec_asserts": "Spine L9: a judgment criterion is graded by the CVO on the artifacts; a correction is a new row citing the old id, never an edit.",
  "world_is": "Both round-131 judgment criteria are graded PASS; the round's held decisions remain with the CTO.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/adjudications/ADJUDICATION_v140.md @d8a70da54d (row C-S75, the grading evidence)",
    "round-close-check --round 131 --workstream ~F2 read graded=0 against v140 alone"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A restatement of C-S75's grades by full id; nothing new to dispose."
 }
]
```
