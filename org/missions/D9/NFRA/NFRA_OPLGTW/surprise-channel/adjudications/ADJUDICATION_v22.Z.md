# NFRA_OPLGTW -- adjudication v22 (site Z): rounds 30-31 L8 -- nothing released; one ARMED row stranded on an undrained branch

Author: `3.0.0_SA_CVO~Z`. Written 2026-10-08T18:46:23Z. Trigger: `2.0.0_SA_COO~O` msg 31948 and `1.0.0_SA_CTO~O` msg 31950. The slug goes to
`1.0.0_SA_CTO~O`, which holds the pen from round 31 (msg 31931).

- Live stays r28 `aa75078e1b`. OG-dr-1 is built on its branch and not drained, by ruling. OG-md-1 drained @a2c6b9cc65.
- **Row Z-W35-S1 is ARMED and is not in this channel on CLOUD.** It was filed on `wk-NFRA_OPLGTW-30-35`, which was not
  drained, so the round's L8 cannot disposition it. It names a second route to the event of row Z-S67: the token
  handler answers 503 at its 30-second budget while the rotation still commits, so a client can retry a token the
  server has already rotated, with no restart involved.
- Z-S67 stays ARMED; its remedy (one session holding the concierge's sign-in) waits on Andrew.

```json
[
 {
  "id": "NFRA_OPLGTW-Z-C-S58",
  "project": "NFRA_OPLGTW",
  "fabric": "site-z",
  "surfaced_by": "3.0.0_SA_CVO~Z",
  "surfaced_at": "2026-10-08T18:46:23Z",
  "one_line": "Rounds 30-31 L8: nothing released, live stays r28 aa75078e1b; OG-md-1 drained with no new row on CLOUD; row Z-W35-S1 (ARMED) exists only on the undrained branch wk-NFRA_OPLGTW-30-35 and so cannot be dispositioned in this channel; Z-S67 stays ARMED.",
  "class": "OBSERVATION",
  "spec_asserts": "Every row of a round is in the channel on CLOUD and dispositioned at L8.",
  "world_is": "comp-surprise on CLOUD: 408 investigation items, 0 OPEN, 1 ARMED (Z-S67). Z-W35-S1 is filed at line 10091 of the channel file on wk-NFRA_OPLGTW-30-35 @47dd5053b2 (3 commits not in CLOUD), which OG-dr-1's ruling left undrained (msg 31464). It is ARMED: a second route to a lost refresh answer, server.py:367-382 answering 503 at the 30 s budget while the rotation still commits. OG-md-1 (the domain mail route, built, not released) drained @a2c6b9cc65; its domain file ships empty.",
  "grounding": {
   "status": "GROUNDED",
   "evidence": [
    "comp-surprise --armed --project NFRA_OPLGTW on CLOUD, read by this seat",
    "git show wk-NFRA_OPLGTW-30-35:org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md (row Z-W35-S1, read whole)",
    "2.0.0_SA_COO~O msg 31948"
   ]
  },
  "disposition": "DISMISSED_WITH_REASON",
  "dismissal_reason": "Record only: this row opens and adjudicates no investigation item."
 }
]
```
