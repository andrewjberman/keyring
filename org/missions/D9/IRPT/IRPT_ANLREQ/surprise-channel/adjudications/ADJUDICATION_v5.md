# IRPT_ANLREQ: CVO adjudication, round 3 (workstream Y), slug

<sweep_watermark>2026-10-11T09:50Z</sweep_watermark>

By `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T09:50:52Z. Input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_ADDENDUM_1_20261011.md @81b38e28a5 (msg 4612)`. 2 rows dismissed below.
7 rows graduate OPEN in `remediations/REMEDIATION_v3.md`.

```json
[
  {
    "id": "IRPT_ANLREQ-C-S5",
    "project": "IRPT_ANLREQ",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-11T09:50:52Z",
    "one_line": "Round 3 (Y) slug: dismissed, D2-S36 (a build from the source map carried no retained_ref; ruled by the CTO, msg 4572, and the entry is re-pinned to one commit, read by this seat as 42 of 42) and this seat's read row D2-S40. Seven rows graduate: D2-W66-S1, D2-W52-S4, D2-W52-S3, D2-S33, D2-S34, D2-S35, D2-S38.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_ANLREQ-D2-S36",
      "IRPT_ANLREQ-D2-S40"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "No IRPT_ANLREQ order is open (to-check). No row is ARMED.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation rows D2-S36, D2-S40",
        "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND3_Y_L8_COMPILE_ADDENDUM_1_20261011.md @81b38e28a5 (msg 4612)",
        "this seat's reads 2026-10-11T09:50:52Z: the source map's irpt-status entry holds 42 staged_from rows, 42 of them at ee3fd7c5e5; owned_report.py at ee3fd7c5e5 holds 7 lines naming retained_ref; live irpt-status CodeSha256 is still 6idtFvAm..., LastModified 2026-10-11T04:44:47Z; portal ff41894759 is an ancestor of origin/DEV, which reads ff41894759 (positive control f74706add3 also an ancestor); the entry's deployed_code_sha256, last_deployed_commit and last_deployed_at still describe 2026-10-05"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A ruled defect whose remedy is read in place, and a read row."
  }
]
```
