# IRPT_DASHBD: remediations, round 83 (workstream B)

<sweep_watermark>2026-10-11T23:24Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T23:24:29Z. Input: msgs 6039 and 6093 (IRPT_DASHBD round 83 closed @6d8691758d, 4 of 4; orders DB-b-158 to DB-b-161).
Graduated, round label v84: 2 rows, OPEN, INERT. This seat made no read of its own; every figure below is a worker's.

**For the CTO's analysis:**
1. **The yardstick is Black Diamond's return, not the custodian's** (row D2-W130-S1). This seat's last slug repeated 'the
   custodian's' and is corrected in row D2-S18. It changes the method question: the served end-of-day convention disagrees with
   Black Diamond on all 51, and two other timings agree with it; that says what Black Diamond does, not what is right.
2. **A change of convention is large and it moves the guard.** About 98,700 account-days change either way; about 3,000 by more
   than 10 bp under one timing and 1,500 under the other. And about 2,590 served returns would become nulls under one, 1,260
   under the other, because the unreconciled-flow flag moves with the timing.
3. **Neither system publishes when a flow counts.** Method help is behind a login nobody used.
4. **The contract's guard clause and the code differ** (row D2-W129-S1): the clause says a flagged day falls back to the price
   return; the code serves a null. The clause is the stale one, by the worker's reading of an earlier ruling.
5. Limits the issuer states: the flag thresholds were inferred by bracketing, not read; the restated end-of-day build differs from
   served on 6 days of the guard read and 19 of 2,596,311 in the size read.

```json
[
 {
  "id": "IRPT_DASHBD-D2-W129-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-160: a flagged day does not fall back to the price return in the code; FLOW_UNRECONCILED serves a null return, LARGE_FLOW keeps the TWR return; the PRD C-GUARD clause and the order wording still say fallback.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W129-S1",
   "msgs 6039 and 6093 (IRPT_DASHBD round 83 closed @6d8691758d, 4 of 4; orders DB-b-158 to DB-b-161)"
  ],
  "remedy": "The contract's guard clause is brought to what the code does, or the code to the clause, by an addendum: a day flagged as unreconciled is served as a null, not as a price return.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v84",
  "remediation": {
   "state": "REMEDIATED",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v84"
  },
  "closed": true
 },
 {
  "id": "IRPT_DASHBD-D2-W130-S1",
  "project": "IRPT_DASHBD",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "DB-b-161: the order and the round-83 analysis speak of 'the custodian's' time-weighted return the 51 segments were scored against, but the project's records show the oracle is Black Diamond's reporting_performance pull; the custodian (Schwab) supplies Opal's side, so two parties were read and the 51 are recorded as scored against Black Diamond.",
  "evidence": [
   "investigation row IRPT_DASHBD-D2-W130-S1",
   "msgs 6039 and 6093 (IRPT_DASHBD round 83 closed @6d8691758d, 4 of 4; orders DB-b-158 to DB-b-161)"
  ],
  "remedy": "Every record and analysis that says the 51 were scored against the custodian's return says Black Diamond's; the method question is then put as it is: which timing matches Black Diamond, and whether matching it is the aim.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v84",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v84"
  },
  "closed": false
 }
]
```
