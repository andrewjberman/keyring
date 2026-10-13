# IRPT_DASHBD: CVO adjudication, round 95

<sweep_watermark>2026-10-13T22:53Z</sweep_watermark>

L8 compile and L10 slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T22:53:00Z. Input: msg 7326 (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND95_B_DRAIN_END_20261013.md @1a6ac02384`; one LOCAL order, DB-b-179). No judgment criterion.
The FWD-21 contract is 0.2.0 (this seat read it). 1 row dismissed below; D2-W145-S1 stays open for a CTO ruling, graduated at round 94's compile.
For the CTO: the worker's weakest folds are named in the packet (the return fold's guard-state inference; net gain is a residual, so a window
identity on it proves nothing; net additions assumes a skipped closure's flow folds into the next trading day).

```json
[
 {
  "id": "IRPT_DASHBD-C-S68",
  "project": "IRPT_DASHBD",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T22:53:00Z",
  "one_line": "Round 95, no judgment criterion. Dismissed: D2-W145-S2 (the criterion's 'no custodian' cannot be a literal word test: the common noun sits in lines outside the 36 members and the grant named no edit to them). D2-W145-S1 (the account-return fold's inference on GRADED_DISAGREED and FLOW_UNRECONCILED, where account_return_daily is silent) stays OPEN for a CTO ruling, to be graduated at round 94's compile once DB-b-175 is terminal. Round 94's rows (D2-W140..W144, S20 to S22) wait for round 94's packet; round 93 was a direct act with no CVO packet, so D2-W139-S1 and -S2 stay with the issuer.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_DASHBD-D2-W145-S2"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and every BLOCKING or ARMED item before the slug.",
  "world_is": "DB-b-179 is complete; the FWD-21 contract is 0.2.0 with 36 window members re-sourced to account_return_daily and member ids and sections unchanged. Repo files only: no S3, no vendor call, nothing served. Round 94 (DB-b-175) is non-terminal, so no remediation row is written this compile.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation row D2-W145-S2",
    "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/IRPT_DASHBD_ROUND95_B_DRAIN_END_20261013.md @1a6ac02384 (msg 7326)",
    "this seat's read of org/standards/IRPT_DASHBD_PERFORMANCE_REPORT_CONTRACT.json at HEAD: 117 members, 8 sections, 71 sourced and 46 ABSENT, lineage sha256 53fce4054688...; drain 853eeebbb2 on HEAD"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "A criterion wording reading; the substantive row stays open for a ruling."
 }
]
```
