# IRPT_ANLREQ: CVO adjudication, round 18 (workstream Y)

<sweep_watermark>2026-10-13T01:24Z</sweep_watermark>

L8 compile and L9 grades by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T01:24:00Z, on msg 6720 (`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND18_Y_L8_COMPILE_20261013.md`).
**L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_18_L9_GRADE_20261013.md`): five PASS. AR186-y-AC2J carries a condition: run the pinned pair (uploads.py f09b802cdc plus template_reader.py
3f29017cfc) in a scratch tree before the reader's pair is cut.
12 rows dismissed below (three of them round-17 rows this seat missed); 6 graduate in `remediations/REMEDIATION_v11.md`, 5 ARMED.

```json
[
 {
  "id": "IRPT_ANLREQ-C-S19",
  "project": "IRPT_ANLREQ",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-13T01:24:00Z",
  "one_line": "Round 18 (workstream Y). Dismissed: Round 18 (Y) rows, plus three round-17 rows this seat missed at its round-17 compile. D2-W54-S4 (BLOCKING; five _authz tests outside the grant, answered by round 17's AMENDMENT 1), D2-W54-S6 (the six arms read the default profile reader; fixed by AMENDMENT 2), D2-W55-S2 (a plain key=value line, not JSON; stated), D2-W55-S3 (folded into D2-W55-S1), D2-W51-S10 (an older worktree; the record read the shared head), D2-W51-S11 (the check verifies no pin; this seat read both pins itself, see the grade record), D2-W52-S34 (folded into D2-W52-S33), D2-W54-S10, D2-W54-S11 and D2-W54-S12 (test-wiring notes behind AR-y-183, whose tests this seat graded PASS), D2-S65 and REMEDIATION_v10's D2-W52-S24 (ARMED; disarmed: this seat's own run of the rule matches all six forms the row named). Workstream YS's rows (D2-W53-S11 to S16) wait for YS's packet.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_ANLREQ-D2-W54-S4",
   "IRPT_ANLREQ-D2-W54-S6",
   "IRPT_ANLREQ-D2-W55-S2",
   "IRPT_ANLREQ-D2-W55-S3",
   "IRPT_ANLREQ-D2-W51-S10",
   "IRPT_ANLREQ-D2-W51-S11",
   "IRPT_ANLREQ-D2-W52-S34",
   "IRPT_ANLREQ-D2-W54-S10",
   "IRPT_ANLREQ-D2-W54-S11",
   "IRPT_ANLREQ-D2-W54-S12",
   "IRPT_ANLREQ-D2-S65",
   "IRPT_ANLREQ-D2-W52-S24"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and judgment criteria are graded at L9, never self-graded.",
  "world_is": "Five worker orders complete; TO-READS-Y9 has run (result @62aa285551, validated by the issuer) and its status flip waits on the laptop's proof. L9: five PASS, AR186-y-AC2J with a condition. Nothing of the round is released. D2-W52-S33 is a LIVE hazard today (the Lambda's pinned reader), graduated ARMED.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W54-S4, D2-W54-S6, D2-W55-S2, D2-W55-S3, D2-W51-S10, D2-W51-S11, D2-W52-S34, D2-W54-S10, D2-W54-S11, D2-W54-S12, D2-S65, D2-W52-S24",
    "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND18_Y_L8_COMPILE_20261013.md (msg 6720)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_18_L9_GRADE_20261013.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Stops answered by amendment, readings, rows folded into graduating rows, and a disarm confirmed by this seat's run."
 }
]
```
