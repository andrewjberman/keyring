# IRPT_ANLREQ: CVO adjudication, round 16 (workstream Y)

<sweep_watermark>2026-10-12T22:22Z</sweep_watermark>

L8 compile and L9 grades by `3.0.0_SA_CVO` (seated on dell2), 2026-10-12T22:22:00Z, on msg 6633 (`org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND16_Y_L8_COMPILE_20261012.md`). In scope by fc10 addendum 2 (msg 6612).
**L9** (`org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_16_L9_GRADE_20261012.md`): AR161-y-AC2J PASS; **AR162-y-AC3J FAIL** on its first clause (the account-header rule misses two plain spellings of
the account number and turns back attribute columns); AR164-y-AC2J PASS. The reader is built, not released, so the fail costs nothing live.
7 rows dismissed below; 3 graduate in `remediations/REMEDIATION_v9.md`. Workstream YS's six rows wait for YS's close (TO-RUN-YS1 pending).

```json
[
 {
  "id": "IRPT_ANLREQ-C-S17",
  "project": "IRPT_ANLREQ",
  "fabric": "laptop",
  "surfaced_by": "3.0.0_SA_CVO",
  "surfaced_at": "2026-10-12T22:22:00Z",
  "one_line": "Round 16 (workstream Y). Dismissed: Round 16 (Y) rows that are records or readings: D2-W51-S9 (the commentary-sent handler differs from the face in four places and the page follows the code; the 403 follow-up is owed per the packet's section 5 item 3), D2-W54-S3 (no other-firm request reaches the owner comparison; a read result, and arm F2 confirmed the refusals live), D2-W52-S16 (the script reads two more retained objects than the face listed; all reads, same table and bucket), D2-W52-S17 (the version member rides the reader's result into the frozen document; met), D2-W52-S19 (where a test serves altered bytes), D2-W52-S21 (the imperative words; this seat grades the words clause PASS), D2-W52-S22 (a non-deterministic xlsx timestamp in a test helper, restamped). Workstream YS's rows (D2-W53-S11 to S16) are left for YS's own close; TO-RUN-YS1 is pending.",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "adjudicates": [
   "IRPT_ANLREQ-D2-W51-S9",
   "IRPT_ANLREQ-D2-W54-S3",
   "IRPT_ANLREQ-D2-W52-S16",
   "IRPT_ANLREQ-D2-W52-S17",
   "IRPT_ANLREQ-D2-W52-S19",
   "IRPT_ANLREQ-D2-W52-S21",
   "IRPT_ANLREQ-D2-W52-S22"
  ],
  "spec_asserts": "Spine L9/L10 (CLAUDE.md rule 27): every item is dispositioned on grounded evidence, and judgment criteria are graded at L9, never self-graded.",
  "world_is": "Every workstream-Y order of round 16 is complete (five cells plus TO-READS-Y7 and -Y8). L9: AR161-y-AC2J PASS, AR162-y-AC3J FAIL (clause 1), AR164-y-AC2J PASS. ARMED on the project: 3, none of this round's (D2-S26, D2-W41-S1, D2-S29), unchanged by this compile.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "investigation rows D2-W51-S9, D2-W54-S3, D2-W52-S16, D2-W52-S17, D2-W52-S19, D2-W52-S21, D2-W52-S22",
    "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND16_Y_L8_COMPILE_20261012.md (msg 6633)",
    "org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_16_L9_GRADE_20261012.md"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Records and readings; the two that carry owed work are named in the packet's section 5."
 }
]
```
