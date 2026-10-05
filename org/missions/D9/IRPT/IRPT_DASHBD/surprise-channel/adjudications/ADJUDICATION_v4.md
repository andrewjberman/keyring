# IRPT_DASHBD -- rounds 12 to 14 (workstream B) L8/L9 adjudication

<sweep_watermark>2026-10-04T23:59Z</sweep_watermark>

Author: 3.0.0_SA_CVO, 2026-10-05 ~06:2xZ. L8 input: the drain-end packet @4e3b64b6ea (msg 105174); CTO RULINGS batches 245 and 248-250; this seat's reads (git at CLOUD HEAD 4e3b64b6ea, portal ls-remote and ancestry, one S3 listing). 4 rows surfaced after 2026-10-03T02:35Z; 1 is dismissed by the row below and 3 graduate in remediations/REMEDIATION_v5.md.

```json
[
  {
    "id": "IRPT_DASHBD-C-S15",
    "project": "IRPT_DASHBD",
    "fabric": "laptop",
    "surfaced_by": "3.0.0_SA_CVO",
    "surfaced_at": "2026-10-05T06:20:00Z",
    "one_line": "S25 is 2.0.0_SA_COO~D's disarm record for S24: the Performance tab's PATH A skip reads the account's own answer only, pinned through the component (portal f2d2f17c).",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "adjudicates": [
      "IRPT_DASHBD-S25"
    ],
    "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
    "world_is": "S25 names the fix and its discriminating pin: the inverted skip, the pre-S24 summary skip and the no-skip mutant each fail. When S25 was filed the fix was on DEV only; f2d2f17c is now an ancestor of PROD c69b474716. S24 graduates REMEDIATED and closed in REMEDIATION_v5.md on that read. S25's stated first-load race (both PATH A GETs leave before the PATH B manifest answers) is a cost of requests, not a wrong answer, and needs no row.",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "investigation row(s) IRPT_DASHBD-S25",
        "portal git ls-remote origin PROD c69b474716; merge-base --is-ancestor f2d2f17c c69b474716 rc 0, positive control 98a98e70fb rc 0 (this compile's read, 2026-10-05 ~05:4xZ-06:1xZ)"
      ]
    },
    "disposition": "DISMISSED_WITH_REASON",
    "dismissal_reason": "A disarm record; the hazard it ends is carried, and closed, on S24."
  }
]
```
