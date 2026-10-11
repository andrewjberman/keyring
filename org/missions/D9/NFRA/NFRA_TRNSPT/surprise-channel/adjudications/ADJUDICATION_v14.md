# NFRA_TRNSPT: CVO adjudication, round 22, second pass

<sweep_watermark>2026-10-11T06:38Z</sweep_watermark>

L8 compile by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T06:38:23Z, on msg 4289 (TO-APPLY-a18 terminal @18d031aaa7); it follows ADJUDICATION_v13. No judgment criterion.
5 rows dismissed below; D2-S19 is disarmed (1024 MB, read live). 5 rows graduate OPEN in `remediations/REMEDIATION_v10.md`,
1 of them ARMED (D2-S22: the transcripts root's two pull functions read two code hashes). FWD-8 is ungraded: its ADMITTED read is parked
with Andrew (row D2-S24).

```json
[
  {
    "id": "NFRA_TRNSPT-C-S19",
    "project": "NFRA_TRNSPT",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T06:38:23Z",
    "one_line": "Round 22, second pass. Dismissed: D2-S19 (ARMED: the pull at its 128 MB ceiling; disarmed, the function reads 1024 MB live with its code unchanged) with its disarm record D2-S21, D2-S23 (a restatement of D2-S22's disarm read; D2-S22 graduates), D2-S24 (the record that moves TO-APPLY-a18's unmet ADMITTED read to a parked item; FWD-8 is ungraded), and this seat's read row D2-S26. Five rows graduate: D2-S15, D2-S16, D2-S17, D2-S20 and D2-S22 (ARMED).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "NFRA_TRNSPT-D2-S19",
      "NFRA_TRNSPT-D2-S21",
      "NFRA_TRNSPT-D2-S23",
      "NFRA_TRNSPT-D2-S24",
      "NFRA_TRNSPT-D2-S26"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "Every NFRA_TRNSPT order is terminal (TO-APPLY-a18 flipped complete @18d031aaa7 on the CTO's ruling msg 4272). ARMED after this compile: 1 (D2-S22, disarm owner the CTO).",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S19, D2-S21, D2-S23, D2-S24, D2-S26",
        "msg 4289 (TO-APPLY-a18 terminal @18d031aaa7)",
        "this seat's live reads 2026-10-11T06:38:23Z: teams-global-transcripts-pull-lambda MemorySize 1024, CodeSha256 AI4UQD0M... (equal to the local dist zip), LastModified 2026-10-11T05:03:47Z; one run since at 1024 MB used 101 MB; outlook-global-transcripts-pull-lambda CodeSha256 VGIq85Xx..., LastModified 2026-10-07T23:59:05Z"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A hazard disarmed and read live, its record, a restatement, a move record, and a read row."
  }
]
```
