# IRPT_ANLREQ: CVO adjudication, round 17 (workstream Y)

<sweep_watermark>2026-10-12T23:44Z</sweep_watermark>

L8 compile and L9 grades by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T23:44:00Z, on msg 6673 (`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND17_Y_L8_COMPILE_20261012.md`).
**L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_17_L9_GRADE_20261012.md`): all four PASS. AR171-y-AC3J carries a condition: the reader's release pair waits on the CTO's ruling on D2-W52-S24
(the closed vocabulary misses `Brokerage Account`, `IRA Account`, `Joint Account`, `Subaccount` and `Account Seq`).
6 rows dismissed below; 5 graduate in `remediations/REMEDIATION_v10.md`, 2 ARMED (owner `2.0.0_SA_COO~Y2`). Nothing of the round is released.

```json
[
 {
  "id": "IRPT_ANLREQ-C-S18",
  "project": "IRPT_ANLREQ",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-12T23:44:00Z",
  "one_line": "Round 17 (workstream Y). Dismissed: Round 17 (Y) records and readings: D2-W52-S23 (an account word followed by a non-identifier word reads as not an account header, the design note behind the closed list), D2-W52-S26 and D2-W52-S27 (a path relative to the wrong root, a drain not in the worker's history, the reader blob byte-identical at both), D2-W52-S30 (the round-14 census's refusal claim predates the stored-input contract; superseded by AR-y-174's runs), D2-W54-S8 (BLOCKING; answered by AMENDMENT 3, which reopened the order, and the fixtures are committed), D2-W54-S9 (under the rule-revert mutant 3 of the 5 named tests fail, which is right: the other two test admits that the old rule also admitted). Workstream YS's rows (D2-W53-S11 to S16) wait for YS's own packet.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_ANLREQ-D2-W52-S23",
   "IRPT_ANLREQ-D2-W52-S26",
   "IRPT_ANLREQ-D2-W52-S27",
   "IRPT_ANLREQ-D2-W52-S30",
   "IRPT_ANLREQ-D2-W54-S8",
   "IRPT_ANLREQ-D2-W54-S9"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and judgment criteria are graded at L9, never self-graded.",
  "world_is": "Every round-17 order and the run TO-RUN-C173 are complete (to-check.py --project IRPT_ANLREQ --all: 0 active at 23:37Z). L9: AR171-y-AC3J PASS with a condition on the release, AR172-y-AC3J PASS, AR173-y-AC2J PASS, AR174-y-AC2J PASS. Nothing of the round is released.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W52-S23, D2-W52-S26, D2-W52-S27, D2-W52-S30, D2-W54-S8, D2-W54-S9",
    "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND17_Y_L8_COMPILE_20261012.md (msg 6673)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_17_L9_GRADE_20261012.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Records and readings, and one stop answered by amendment."
 }
]
```
