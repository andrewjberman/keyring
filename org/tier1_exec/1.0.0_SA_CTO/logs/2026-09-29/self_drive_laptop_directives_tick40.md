# /self-drive laptop directives -- ticks 39-40 (2026-09-29 17:59Z-18:45Z)

**archetype:** COORDINATE

Arming record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20260928_230xZ_SELF_DRIVE_LAPTOP_FABRIC.md`
@`9549fd3b32`; cron `f02c52db`. **state: ARMED**

## Served / landed this interval

- **Transcripts step 1** is on local CLOUD (`73896b6c42`), but its push waits on Andrew's word. `0.7.0_AE_CloudOps` is
  live on steps 2-3.
- **W24 CLOSED** (`2ab7e78832`). Part P: the 49F r3 presses passed; K10 NOT MET (S213: a READY report's sections serve
  UNEXPECTED). Part Y returned zero reports (S218).
- **CVO was dark and relaunched on Andrew's word** (MSTR 102963). It is reading the ~M r20 + r23 drain-ends.
- ~M found a directory-bundle import gap (S217). Its fix is round 24, IB-mr-241 (`e71c76b9d1`), and the bundle stays
  skipped until it lands.

## Decisions

- **S216:** the July DOOR 5 hold is no longer in force. Raw was restarted 08-14 (`5fdbe38637`) and INF-REDEPLOY closed
  09-01. ~P cuts the TO on inf-api-{positions,txn,performance}: diagnose first, correct the stale mirror comment, and
  put any redeploy or backfill under a ledger with halves.
- **S218:** the one-refresh-per-request allowance stays. The cell, amended on ~Y 102968 (a double eviction, not a stale
  session), is: journal the matched eviction_verdict per call (this answers S207); discriminate with one solo job; the
  remedy follows the reading.
- **One canonical security table** (Andrew-direct via ~D, placement `c3c3f414dc`). IR Holdings moves onto
  `etf-classifications`, plus the PHYS seed row: a ~M cell under halves, before the COT re-point. Retiring
  `bd-securities` and ~15 copies is a new project at L1 (CRO). The portal half is ~D's.
- Transcripts: the portal restamp goes via ~D on DEV. My over-ask of new halves on the step-3 bundle was corrected
  (102944).

## State

55 open TOs across 9 laptop directives; 4 COO lanes live. The machine is slow: the census took more than 120 s.

## At Andrew

1. The word for MSTR to push CLOUD (it carries transcripts step 1 and the restamps; the bundle stays skipped until
   S217's fix lands).
2. The CRO's question: (a) restart the local dev build, or (b) admit a PROD base in the walker. The CTO recommends (a).
