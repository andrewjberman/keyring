# IRPT_ANLREQ: CVO adjudication, round 20 (workstreams Y and YR)

<sweep_watermark>2026-10-13T14:32Z</sweep_watermark>

L8 compile and L9 grades by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T14:32:00Z, on msg 6974 (`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND20_Y_L8_COMPILE_20261013.md`). The status rule is LIVE in all eight packagers
(read by this seat), and the irpt-holdings artifact-key incident is restored with no function ever running a wrong version (read by this seat).
**L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_20_L9_GRADE_20261013.md`): **AR211-y-AC3J FAILS** clause 1 (Acct Cost Basis and Acct Gain with 8-digit integers are still turned back); five AC2J PASS
on a sampled read; the AR212/AR213-y-AC1 re-grades are accepted. 19 rows dismissed below; 6 graduate in
`remediations/REMEDIATION_v13.md`, 2 ARMED.

```json
[
 {
  "id": "IRPT_ANLREQ-C-S21",
  "project": "IRPT_ANLREQ",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T14:32:00Z",
  "one_line": "Dismissed: Round 20 (Y, YR). Disarmed on the issuer's records and closed: D2-S69 and D2-W64-S5 (ARMED; the irpt-holdings artifact key restored, by D2-S70, read by this seat: restore hfQkgY1L, then the release; no function ran a wrong version), D2-W61-S3 and REMEDIATION_v11's D2-W54-S5 (ARMED; by D2-S72: the status rule is in all eight packagers' bytes, read live by this seat), REMEDIATION_v12's D2-W55-S25 (ARMED; its remedy, the 24 words carried to irpt-status by the all-eight pair, is applied: irpt-status runs vlGh380Q). BLOCKING rows resolved: D2-W61-S4 (the calendar test fails identically with the original bytes), D2-W64-S1 and -S2 (suites repaired by AR-y-216). Readings: D2-W63-S2, D2-W61-S5, -S6, D2-W64-S3, -S4, D2-W65-S2, -S3, D2-W66-S2, -S3, and the records D2-S70, D2-S72. Workstream YS's rows wait for YS's packet.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_ANLREQ-D2-S69",
   "IRPT_ANLREQ-D2-S70",
   "IRPT_ANLREQ-D2-S72",
   "IRPT_ANLREQ-D2-W61-S3",
   "IRPT_ANLREQ-D2-W61-S4",
   "IRPT_ANLREQ-D2-W61-S5",
   "IRPT_ANLREQ-D2-W61-S6",
   "IRPT_ANLREQ-D2-W63-S2",
   "IRPT_ANLREQ-D2-W64-S1",
   "IRPT_ANLREQ-D2-W64-S2",
   "IRPT_ANLREQ-D2-W64-S3",
   "IRPT_ANLREQ-D2-W64-S4",
   "IRPT_ANLREQ-D2-W64-S5",
   "IRPT_ANLREQ-D2-W65-S2",
   "IRPT_ANLREQ-D2-W65-S3",
   "IRPT_ANLREQ-D2-W66-S2",
   "IRPT_ANLREQ-D2-W66-S3",
   "IRPT_ANLREQ-D2-W54-S5",
   "IRPT_ANLREQ-D2-W55-S25"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and judgment criteria are graded at L9, never self-graded.",
  "world_is": "All 100 IRPT_ANLREQ orders are terminal (to-check.py --all: 0 active at 14:25Z). The status rule is live in eight packagers; the r19.2 reader is built, not released. L9: AR211-y-AC3J FAILS clause 1; five AC2J PASS on a sampled read; AR212/AR213-y-AC1 re-grades accepted.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S69, D2-S70, D2-S72, D2-W61-S3, D2-W61-S4, D2-W61-S5, D2-W61-S6, D2-W63-S2, D2-W64-S1, D2-W64-S2, D2-W64-S3, D2-W64-S4, D2-W64-S5, D2-W65-S2, D2-W65-S3, D2-W66-S2, D2-W66-S3, D2-W54-S5, D2-W55-S25",
    "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND20_Y_L8_COMPILE_20261013.md (msg 6974)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_20_L9_GRADE_20261013.md",
    "this seat's live reads 2026-10-13T14:21Z: eight packagers at the signed CodeSha256 values; TypeError/Traceback/ImportError 0 in eight log groups since 12:30Z; irpt-holdings artifact key versions T1NEd9G., msFi8sD6, QCyspt0v (wrong), hfQkgY1L (restore, 11:24:26Z), YMQJgP4t (release, latest); irpt-holdings LastModified 12:47:20Z"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Disarmed on the owner's records with this seat's live reads, blocking rows resolved by a measured later cell, and readings."
 }
]
```
