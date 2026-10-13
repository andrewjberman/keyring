# IRPT_BCKEND: remediations, round 169 (workstream ~P)

<sweep_watermark>2026-10-13T01:50Z</sweep_watermark>

Slug by `3.0.0_SA_CVO` (seated on dell2), 2026-10-13T01:50:00Z. Follows ADJUDICATION_v70. L8 input: `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_169_P_DRAIN_END_20261013.md` (blob cac527a019, msg 6733). No judgment criterion.
Graduated, round label v170: 2 rows, OPEN; ARMED 0.
- D2-S121 (owner `1.0.0_SA_CTO~DELL2`): the release's changed branch has not run live. The on-demand act now exists; run it again on another client,
  or record the branch as offline-proven only.
- D2-W341-S7 (owner `2.0.0_SA_COO~P2`, DISARMED): the walker's client-name redaction is unproven on a live page.

```json
[
 {
  "id": "IRPT_BCKEND-D2-W341-S7",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "BLOCKING",
  "hazard_standing": "INERT",
  "mechanism": "The walker's terminal output leaks a fragment of the walked client's name. Each STEP line prints a screenshot path whose slug is the step label cut to 60 characters, and the step label carries the first listed client's name; the --first-client redaction in log() matches only the full name string, so the slug passes through. The walk of 00:04:00 to 00:05:57 printed such fragments on the terminal. The walker contract says a client name is never printed, so any further --first-client run leaks the same way until the slug is covered by the redaction.",
  "evidence": [
   "investigation row D2-W341-S7",
   "row D2-S115 (disarm evidence)",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_169_P_DRAIN_END_20261013.md"
  ],
  "remedy": "The --first-client redaction (log, shot file name, step label) is proven by code read and the worker's three criteria, not on a live page. The next --first-client walk reads its terminal and shot names for any client-name fragment; 0 closes the row.",
  "owner": "2.0.0_SA_COO~P2",
  "round": "v170",
  "remediation": {
   "state": "OPEN",
   "owner": "2.0.0_SA_COO~P2",
   "round": "v170"
  },
  "closed": false,
  "disarm": {
   "state": "DISARMED",
   "owner": "2.0.0_SA_COO~P2",
   "at": "2026-10-13T01:50:00Z"
  }
 },
 {
  "id": "IRPT_BCKEND-D2-S121",
  "project": "IRPT_BCKEND",
  "fabric": "dell2",
  "class": "OBSERVATION",
  "hazard_standing": "INERT",
  "mechanism": "The round-168 release's CHANGED branch (claim inferred, days_with_return_left_out above 0) has still not run on a live answer: round 169's on-demand Inflection read computed twice and matched its prediction, but the account had 0 excluded days, so it exercised only the measured branch. The act that would reach the changed branch now exists (a walk that picks another client).",
  "evidence": [
   "investigation row D2-S121",
   "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/IRPT_BCKEND_ROUND_169_P_DRAIN_END_20261013.md"
  ],
  "remedy": "Either the walk is run again with another first letter until one Inflection account with a return-leaving-out excluded day computes, and its claim (inferred) and count (above 0) are read against the offline prediction; or the CTO records the left-out branch as offline-proven only (the 30,843-figure replay) with its reason. Branch B (the named rollback version) stays available.",
  "owner": "1.0.0_SA_CTO~DELL2",
  "round": "v170",
  "remediation": {
   "state": "OPEN",
   "owner": "1.0.0_SA_CTO~DELL2",
   "round": "v170"
  },
  "closed": false
 }
]
```
