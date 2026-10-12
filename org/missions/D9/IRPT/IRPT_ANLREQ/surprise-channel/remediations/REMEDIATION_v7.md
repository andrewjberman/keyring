# IRPT_ANLREQ: remediations, round 13 (workstream Y)

<sweep_watermark>2026-10-11T21:02Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-11T21:02:29Z. Input: `org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND13_Y_L8_COMPILE_20261011.md @6d2fa01d99 (msg 5839)`.
Graduated, round label v14: 3 rows, OPEN, INERT.

**For the CTO's analysis:**
1. **Both criteria MET.** Grade file: `org/tier1_exec/3.0.0_SA_CVO/deliverables/IRPT_ANLREQ_ROUND_13_Y_L9_GRADE_20261011.md`.
2. **The one-account check was aimed at the wrong file** (row D2-W52-S9): the form's door is the template reader, which reads two
   columns of the first sheet. Today it accepts a two-account sheet and merges it, and counts a totals row as a holding (row D2-W52-S10).
3. **Five questions for your ruling before the build,** the record's four and one of this seat's: whether a second holdings sheet is
   turned back. Built as an error it would refuse the repository's own one-account multi-sheet example.
4. A person sees a refusal only on a second press (row D2-W52-S11).
5. AR131's clause 'read from the ticket type's definition' cannot be met: no per-type definition exists.

```json
[
 {
  "id": "IRPT_ANLREQ-D2-W52-S9",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "TO-AR-y-132: the order and the earlier read (TCKT_VNEXT~20) name parse.py as the normalizer, but the door the form reaches does not use it: the deployed upload service refuses the parse.py lane by name (CSV_LANE_NOT_COMPOSED) and the form only sends the template lane, whose reader is template_reader.py reading columns A and B. A check built in parse.py would never run for a person filing in the Ticket Center.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-W52-S9",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND13_Y_L8_COMPILE_20261011.md @6d2fa01d99 (msg 5839)"
  ],
  "remedy": "Every order and read that names parse.py as the form's door is corrected to the template reader; the one-account check is cut there.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v14",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v14"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W52-S10",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "TO-AR-y-132: run through the door in process (offline provider stub), a two-account sheet with an Account column and a sheet ending in a 'Total' row are both ACCEPTED (NORMALIZED); the first merged two accounts' AAA rows into one holding (150), the second counted the total as a holding (600 on a 300 sheet). The live provider's answer for the symbol TOTAL was not run.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-W52-S10",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND13_Y_L8_COMPILE_20261011.md @6d2fa01d99 (msg 5839)"
  ],
  "remedy": "The door turns back a sheet with an account column of two or more distinct values and a sheet with a labelled totals row, each with words; the live provider's answer for a totals label is read once.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v14",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v14"
  },
  "closed": false
 },
 {
  "id": "IRPT_ANLREQ-D2-W52-S11",
  "project": "IRPT_ANLREQ",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "TO-AR-y-132: the door's first answer to every template upload (10 of 10 sheets run) is RESOLVING; the form then says 'submit again in a moment', so a person learns what to fix only after a second press even for a file that is plainly bad.",
  "evidence": [
   "investigation row IRPT_ANLREQ-D2-W52-S11",
   "org/missions/D9/IRPT/IRPT_ANLREQ/ledger/IRPT_ANLREQ_ROUND13_Y_L8_COMPILE_20261011.md @6d2fa01d99 (msg 5839)"
  ],
  "remedy": "A ruling on whether two presses are acceptable for FWD-3; if not, the form re-posts until the answer leaves RESOLVING and then shows the findings.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v14",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v14"
  },
  "closed": false
 }
]
```
