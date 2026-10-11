# ADVI_FIRMBKTS round 4 -- THE WINDOW RUNBOOK (acts 2, 3, 4, 4b, 4c), written by `2.0.0_SA_COO~B1`, 2026-10-11 ~16:3xZ

One page the executors read. It orders the acts; it changes no pair. Where this page and a signed half differ, the half wins.

## 0. State as of this page (each read from a file at HEAD)

| prerequisite | state |
|---|---|
| act 0 (producers' grant), its Delete addendum (`FB-f-16` @2658e9ff96) | APPLIED |
| act 1 (advTenant, `FB-f-8`) | APPLIED, complete |
| act 3b (readers' admission, `FB-f-14` @0acccf7d8e) | APPLIED; close simulation `FB-f-15` re-run owed by ~FBL (XB-b717) |
| act 3c (exec-summary fence row, `FB-f-17`) | pair SIGNED; apply pending (`0.7.0_AE_CloudOps~FB1`) |
| act 4b identity policy (`FB-f-18`) | pair SIGNED; apply pending (FB1) |
| dormant builds: `FB-g-1`..`FB-g-29` | merged and graded; `FB-g-29` (census) in flight |
| pairs: act 2 (ADDENDA 1-4), act 3, act 4 (+ ADDENDA 1, 2), 4b/4c, 3b, 3c | SIGNED in both halves |
| the one value (`routed` of the 49financial alias) | NOT flipped (act 4) |

## 1. Timing (read, not assumed)

- The producers' scheduled chain runs about 04:00Z and its window closes about 06:15Z (act 2 order, ISSUER NOTES). Sunday has no
  23:00Z fallback; Monday to Saturday does. The exec-summary generator runs `cron(30 4 * * ? *)` daily.
- The window opens AFTER a scheduled chain has ended and a read confirms it (exit 0; no run in progress), and every act of it
  lands before the NEXT scheduled chain, or act 2 rolls back (act-2 CTO half ADDENDUM 3 condition 2). Earliest opening:
  Monday 2026-10-12 about 06:30Z. **Act 4 (the flip) is timed INSIDE US TRADING HOURS** (CTO act-4 ADDENDUM 3, msg 3984): the
  first hour of real origin responses is its live read, so it flips at about 13:45Z or later on a trading day and is read for
  an hour. Acts 2 and 3 therefore run in the morning (about 06:30Z to 12:30Z); the legacy home sits frozen at that morning's
  chain output, which is the freshest data, until the flip.
- Act 4b lands after act 2 and before the next 04:30Z run, or act 2 waits a day (ADDENDUM 11 condition 2).

## 2. The order, with owners

| # | act | owner | gate to start | read at the end |
|---|---|---|---|---|
| 0 | GO read: chain ended, no run straddles, every row above reads as stated, no hand ownership-map change | `2.0.0_SA_COO~B1` | the checks below all green | the GO is a commit on `FB-f-9` naming `MOVE_TS` |
| 1 | act 2: ship the 19 `.py` objects and `gold_dispatch.sh`, record `MOVE_TS` | `0.7.0_AE_CloudOps~FB1` (`FB-f-9` phase B) | GO | `r3_act2_reads.py deployed-equal` 20 of 20 |
| 2 | act 3: the delta copy against a FRESH manifest | FB1 (`FB-f-10`) | act 2 `MOVE_TS` recorded; old home quiet | `r3_f7.py compare`: `DEST-VS-MANIFEST: EQUAL` |
| 3 | act 4 prep: build the three edge artifacts and the eight IRPT artifacts from the flip commit (on a branch, not yet integrated) | COO and workers | act 3 EQUAL | each artifact's hash printed |
| 4 | act 4: the ONE value commit; the edge units (laptop, crossbox ORDER) and the eight IRPT roots (dell1) | `0.7.0_AE_CloudOps~FBL`, FB1 (`FB-f-11`) | steps 0-3 | `r4_flip.py`, `r4_dormant.py`, object-level equality, the sample |
| 4a | BEFORE the flip: the router oracle's nine bucket/key pairs, a HEAD of each key at the new home, and the OAI Allow byte-equal (principal and action) to the OAI statement serving opal-data-bd today (a positive control); a difference is a STOP | COO and FBL | act 3 EQUAL | the printed pairs and the equality |
| 5 | the real sample: one invocation per IRPT function and the validator (census `FB-g-29`); AFTER the flip, the router behaviors' real origin responses over the first hour (an origin 403 or 404 is Branch B) | FB1 and FBL | act 4 applied | any AccessDenied is Branch B WITH act 2's rollback |
| 6 | acts 4b and 4c: the code version and `BD_PLATINUM_MODE=canonical` of each Lambda | FB1 (`FB-f-13` phases B, C) | act 3c and 3b complete | each pair's Branch A |
| 7 | close: L8 packet, the CTO's read, the L10 slug | COO | all of the above | the CTO's analysis |

## 3. Rollback, as the pairs state it (one page)

- Act 4's Branch B rolls back act 4 AND act 2 in the same hour: the previous edge versions re-associated, the eight IRPT
  functions' previous versions, the registry commit reverted and regenerated, and `gold_dispatch.sh` re-deployed from its recorded
  prior version (CTO half condition 1). The legacy home is untouched by acts 3 and 4; after act 2 it is frozen until the mode
  returns to `legacy`.
- Acts 4b and 4c roll back by the previous Lambda version and the removed environment value, the same hour.
- Act 3's guard never overwrites a newer destination key; its per-key rollback is the destination's prior version (versioning
  `Enabled`).

## 4. What this page does not decide

The GO itself (the issuer's amendment commit, with its window time); whether the nine OAI reads are made by a session or by the
oracle (ruled: the oracle's pairs before, real origin responses for an hour after; Andrew's staff session is offered in the entry, not a gate); the partners API's cache TTL (to be read and named in act 4c's entry, CTO msg 3974).
