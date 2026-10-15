# IRPT_DASHBD: CVO adjudication, round 112

<sweep_watermark>2026-10-14T22:58Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO~DELL2`, 2026-10-14T22:58Z, on msg 7873 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND112_B_DRAIN_END_20261014.md`, blob 3e49db4850). No judgment criterion (no render). DB112-1-AC1 and DB112-2-AC1 re-run here: 2 of 2 PASS. 4 rows dismissed below, 3 ARMED among them. No remediation row while round 98 runs.

```json
[
 {
  "id": "IRPT_DASHBD-D2-C-S9",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "surfaced_by": "3.0.0_SA_CVO~DELL2",
  "surfaced_at": "2026-10-14T22:58:00Z",
  "one_line": "Round 112 (the household SOURCE_BREAK rule, no imputation; the cause read). DB112-1-AC1, DB112-2-AC1 PASS re-run here. A window with an unmeasured account day prints words naming the account, never a figure; 49 Financial: a figure for 3814 / 2027 / 1765 / 1449 of 4013 households (QTD / YTD / 12m / since inception). The unmeasured days (56,311) all come from this project's own account_return_daily.py; one date, 2026-04-21, breaks 861 households' since-inception windows. Dismissed (4): D2-W183-S1 (ARMED; a household whose only day is as_of now reads INSUFFICIENT_HISTORY in words, not 0; disarmed by its owner in D2-S47), D2-W183-S2 and D2-W182-S1 (ARMED; the commit-time client-data check is WARN-only on dell2 by Andrew's record ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME, the same disposition as IRPT_BCKEND D2-W374-S1; the issuer's identifier scans stood in), D2-S47 (the issuer's dispositions).",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W183-S1",
   "IRPT_DASHBD-D2-W183-S2",
   "IRPT_DASHBD-D2-W182-S1",
   "IRPT_DASHBD-D2-S47"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every BLOCKING or ARMED row is dispositioned on grounded evidence or a recorded ruling before the slug.",
  "world_is": "Both round-112 orders complete; nothing served or written to AWS. The 49 Financial household return has a rule for what prints; the report contract still sources it ABSENT. The next useful act is a READ of 2026-04-21's NOT_MEASURABLE rows by cause, before any repair that would move served numbers under a never-widen pair.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "this seat's re-run 2026-10-14T22:5xZ: DB112-1-AC1 PASS, DB112-2-AC1 PASS",
    "investigation rows D2-W182-S1, D2-W183-S1, D2-W183-S2, D2-S47",
    "org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261009_192xZ_CLIENT_DATA_IN_PRIVATE_GIT_NOT_WORTH_TIME.md",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND112_B_DRAIN_END_20261014.md blob 3e49db4850 (msg 7873)"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "An owner-disarmed rule fix, two ARMED rows whose standing Andrew's record decides, and the issuer's disposition record."
 }
]
```
