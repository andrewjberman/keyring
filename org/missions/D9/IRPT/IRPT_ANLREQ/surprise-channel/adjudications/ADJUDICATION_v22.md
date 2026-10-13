# IRPT_ANLREQ: CVO adjudication, round 21 (workstreams Y and YR)

<sweep_watermark>2026-10-13T16:22Z</sweep_watermark>

L8 compile and L9 grades by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T16:22:00Z, on msg 7055 (`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND21_Y_L8_COMPILE_20261013.md`). The status rule is exercised live and works; the
allowlist reader r19.3 is built, and it closes this seat's backstop FAILs (probed). **L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_21_L9_GRADE_20261013.md`): AR221-y-AC3J PASS; AR-y-222's judgment
FAIL, superseded by AR-y-229 PASS; four AC2J PASS; R21E-AC1 and R21S-AC1 re-grades accepted. 22 rows dismissed below; nothing graduates.
Still ARMED where they stand: D2-W52-S33 and -S36 (released, not shown live), D2-W55-S5 (P2), D2-W55-S1 (the class line's limits).

```json
[
 {
  "id": "IRPT_ANLREQ-C-S22",
  "project": "IRPT_ANLREQ",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T16:22:00Z",
  "one_line": "Dismissed: Round 21 (Y, YR). Disarmed and closed: D2-W67-S1 (BLOCKING, ARMED; the allowlist against three tests, by amendment @21a3ea4299) with REMEDIATION_v13's D2-W64-S6 and D2-W61-S2 (ARMED) and D2-W69-S1 (BLOCKING; the false premise answered by the CTO half's choice (A)), all by the issuer's D2-S75; REMEDIATION_v13's D2-S73 (this seat's AR211 FAIL carrier; met by r19.3's allowlist, this seat's probe: 10 of 10 one-account neighbours unflagged, 8 of 8 two-account forms turned back) and D2-S71 (the ci script's false NOT VERIFIED; fixed by AR-y-229 and proved by TO-SCRATCH-R21b). Readings and limits, stated in their records: D2-W67-S2, -S3, D2-W68-S1, D2-W70-S1 to -S5, D2-W71-S1 to -S4, D2-W72-S1, -S2, D2-S74 (the 3 extra class lines placed on one other caller's invocation). Workstream YS's rows wait for YS's packet.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_ANLREQ-D2-S74",
   "IRPT_ANLREQ-D2-S75",
   "IRPT_ANLREQ-D2-W67-S1",
   "IRPT_ANLREQ-D2-W67-S2",
   "IRPT_ANLREQ-D2-W67-S3",
   "IRPT_ANLREQ-D2-W68-S1",
   "IRPT_ANLREQ-D2-W69-S1",
   "IRPT_ANLREQ-D2-W70-S1",
   "IRPT_ANLREQ-D2-W70-S2",
   "IRPT_ANLREQ-D2-W70-S3",
   "IRPT_ANLREQ-D2-W70-S4",
   "IRPT_ANLREQ-D2-W70-S5",
   "IRPT_ANLREQ-D2-W71-S1",
   "IRPT_ANLREQ-D2-W71-S2",
   "IRPT_ANLREQ-D2-W71-S3",
   "IRPT_ANLREQ-D2-W71-S4",
   "IRPT_ANLREQ-D2-W72-S1",
   "IRPT_ANLREQ-D2-W72-S2",
   "IRPT_ANLREQ-D2-W64-S6",
   "IRPT_ANLREQ-D2-W61-S2",
   "IRPT_ANLREQ-D2-S73",
   "IRPT_ANLREQ-D2-S71"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and judgment criteria are graded at L9, never self-graded.",
  "world_is": "All 11 round-21 orders are terminal (to-check.py --all: 0 active at 16:14Z). The status rule is EXERCISED live and works. Reader r19.3 is built, its two-leg pair signed, and its window closed on the R0d recount (kms:Decrypt on a Dell lane). irpt-ycharts-generate unchanged at hpNfkhLt (this seat's read). L9: AR221-y-AC3J PASS; AR-y-222's judgment FAIL, superseded by AR-y-229 PASS; four AC2J PASS; two mechanical re-grades accepted.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-S74, D2-S75, D2-W67-S1, D2-W67-S2, D2-W67-S3, D2-W68-S1, D2-W69-S1, D2-W70-S1, D2-W70-S2, D2-W70-S3, D2-W70-S4, D2-W70-S5, D2-W71-S1, D2-W71-S2, D2-W71-S3, D2-W71-S4, D2-W72-S1, D2-W72-S2, D2-W64-S6, D2-W61-S2, D2-S73, D2-S71",
    "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND21_Y_L8_COMPILE_20261013.md (837581576b, msg 7055)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_21_L9_GRADE_20261013.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Disarmed on the owner's record and by this seat's probe, a script fix proved on a real run, and readings."
 }
]
```
