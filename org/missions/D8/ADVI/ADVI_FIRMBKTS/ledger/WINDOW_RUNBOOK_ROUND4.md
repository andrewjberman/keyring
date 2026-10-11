# ADVI_FIRMBKTS round 4 -- THE WINDOW RUNBOOK (acts 2, 3, 4b, 4c, 4), written by `2.0.0_SA_COO~B1`, 2026-10-11 ~17:0xZ; REVISION 2

One page the executors read. It orders the acts; it changes no pair. Where this page and a signed half differ, the half wins.
Revision 2 folds in the CTO's read (`CTO_READ_WINDOW_RUNBOOK_ROUND4.md`, msg 4013): one order error corrected (4b and 4c run
BEFORE act 4) and eight conditions added to the steps they belong to.

## 0. State as of this page (each read from a file at HEAD)

| prerequisite | state |
|---|---|
| act 0 (producers' grant), its Delete addendum (`FB-f-16` @2658e9ff96) | APPLIED |
| act 1 (advTenant, `FB-f-8`) | APPLIED, complete |
| act 3b (readers' admission, `FB-f-14` @0acccf7d8e) | APPLIED; close simulation `FB-f-15` re-run owed by ~FBL (crossbox b717) |
| act 3c (exec-summary fence row, `FB-f-17` @5a8c78f135) and 4b's identity policy (`FB-f-18` @ee0fed864d) | APPLIED |
| dormant builds `FB-g-1`..`FB-g-29`, `FB-g-19`..`-28` | merged and graded |
| pairs: act 2 (ADDENDA 1-4), act 3, act 4 (+ ADDENDA 1-5), 4b/4c, 3b, 3c | SIGNED in both halves |
| the one value (`routed` of the 49financial alias) | NOT flipped (act 4) |

## 1. Timing (read, not assumed)

- The producers' scheduled chain runs about 04:00Z and its window closes about 06:15Z. Sunday has no 23:00Z fallback; Monday to
  Saturday does. The exec-summary generator runs `cron(30 4 * * ? *)` daily.
- The window opens AFTER a scheduled chain has ended and a read confirms it (exit 0, no run in progress), and every act of it lands
  before the NEXT scheduled chain, or act 2 rolls back (act-2 CTO half ADDENDUM 3 condition 2). Earliest opening: Monday
  2026-10-12 about 06:30Z. **Act 4 (the flip) is timed INSIDE US TRADING HOURS** (CTO act-4 ADDENDUM 3): it flips at about 13:45Z
  or later on a trading day and is read for an hour. Acts 2, 3, 4b and 4c therefore run in the morning (about 06:30Z to 12:30Z);
  the legacy home sits frozen at that morning's chain output, the freshest data there is, until the flip.
- Act 4b lands before Tuesday's 04:30Z run (it lands the same morning, well before).

## 2. The order, with owners

| # | step | owner | gate to start | read at the end |
|---|---|---|---|---|
| 0 | THE GO: act 4 is READY before act 2 opens (act-2 CTO ADDENDUM 3 condition 1): `FB-g-29` merged and graded; every reader's dormant proof read; the laptop leg CONFIRMED: `FB-f-19`'s crossbox ORDER ACKED by `0.7.0_AE_CloudOps~FBL` with the flip time stated; a chain has ended; the rows of section 0 read as stated; NO hand ownership-map change (it must hold from here through step 5) | `2.0.0_SA_COO~B1` | all of it | the GO commit on `FB-f-9` naming `MOVE_TS`'s window; without a confirmed laptop executor act 2 does NOT open |
| 1 | act 2: ship the 19 `.py` objects (verify; the push hook may have shipped them) and `gold_dispatch.sh`, record `MOVE_TS` | `0.7.0_AE_CloudOps~FB1` (`FB-f-9` phase B) | GO | `r3_act2_reads.py deployed-equal` 20 of 20; the legacy-quiet read `old-home --since MOVE_TS` NAMES `exec_summary.json` among the keys |
| 2 | act 3: the delta copy against a FRESH manifest | FB1 (`FB-f-10`) | `MOVE_TS` recorded; old home quiet | `r3_f7.py compare` reads `DEST-VS-MANIFEST: EQUAL`, the denominator printed, AND the ownership key printed BY NAME as `equal` or `kept-newer` with its `LastModified` |
| 3 | acts 4b and 4c: the Lambda code version and `BD_PLATINUM_MODE=canonical` of each; the partners API's cache TTL read and named | FB1 (`FB-f-13` phases B, C) | step 2 EQUAL; acts 3b and 3c complete (3c before 4b, 3b before 4c) | each pair's Branch A; the exec-summary's own read is Tuesday 04:30Z (step 9) |
| 4 | act 4 prep: the flip commit (`FB-g-30`) and the eight re-pins (`FB-g-31`), merged and integrated to CLOUD; `r4_flipcommit.py --verify` 4 of 4, `r4_repin.py` 3 of 3; the `data/mdpf/config/bronze_homes.json` diff PRINTED and equal to its `_generated` mark line alone (v1.4 check d; a feed or value line changing is a STOP) | COO and workers | step 3 complete | the full commit hashes printed |
| 5 | BEFORE the flip: (a) the router oracle's nine bucket/key pairs, a HEAD of each key and the OAI Allow byte-equal to the legacy one (`r4_oai.py` 3 of 3); (b) the CloudFront behaviors' TTL read and NAMED (the CTO is asked if it exceeds one session); (c) the authorization sample BEFORE (granted and refused, through the validator path and one IRPT consumer; `SAMPLE_BEFORE.json`); (d) the MDPF gold fire of 13:30Z READ: its run has ended, or its end time is named (the flip commit regenerates `bronze_homes.json`; CTO msg 108377 chain item 3), never waited on beyond the first hour; its write as `mdpf-49f-gold-writer-role` into `opal-data-49financial` reads no `AccessDenied` (v1.4 check a; one is a BLOCKING row BEFORE the flip) | FB1 and FBL | step 4; a trading day, 13:45Z or later | a STOP on any difference |
| 6 | act 4: the edge units (`FB-f-19`, FBL) and the eight IRPT consumers (`FB-f-11`, FB1), begun the same minute; each side prints the FIRST and LAST unit's association or apply time; a split that cannot close rolls back EVERY unit already moved | FBL, FB1 | step 5 green | `r4_act4.py` irpt 8 of 8 and edge 6 of 6 |
| 7 | AFTER the flip: the same sample (`r4_sample_eq.py` all EQUAL; `irpt-ycharts-generate` reads the SAME answers, its added `load_directory` guard refusing a previously served request is Branch B); the performance adapter invoked once and its evidence artifact KEY named (never under a served class); the validator's log groups read in EVERY edge region with the denominator printed; the router behaviors' real origin responses over the first hour (a 403 or 404 is Branch B) | FB1, FBL | step 6 | every line printed; any `AccessDenied` is Branch B WITH act 2's rollback |
| 8 | close: the entry closed on both sides; D1-S17 disarmed by act 4's read and NAMED; the flip receipt carries one OWNERSHIP-PASS line per shared file (`shared-advisor-router`, the guard, the CloudFront behaviours, `bronze_homes.json`, `firm-config.mjs`, the portal-auth WAF rider: the CTO's R2, msg 108377); the L8 packet | COO | step 7 clean | the CTO's read |
| 9 | the next day: the exec-summary generator's 04:30Z run read at the object at the canonical home (a failure is a BLOCKING row, fixed forward, not a cutover rollback; the one-day-stale summary is its named cost) | FB1 | Tuesday 04:30Z has run | the object's `LastModified` and a count |

## 3. Rollback, as the pairs state it (one page)

- Act 4's Branch B rolls back act 4 AND act 2 in the same hour: the previous edge versions re-associated, the eight IRPT
  functions' previous versions, the registry commit reverted and regenerated, the eight pins reverted, and `gold_dispatch.sh`
  re-deployed from its recorded prior version (CTO half condition 1). Acts 4b and 4c roll back by the previous Lambda version and
  the removed environment value, the same hour. The legacy home is untouched by acts 3 and 4; after act 2 it is frozen until
  the mode returns to `legacy`.
- Act 3's guard never overwrites a newer destination key; its per-key rollback is the destination's prior version (versioning
  `Enabled`).

## 4. What this page does not decide

The GO itself (the issuer's amendment commit, with its window time); whether the nine OAI reads are made by a session (ruled: the
oracle's pairs before and real origin responses for an hour after; Andrew's staff session is offered in the entry, not a gate).

## Rev 3 (2026-10-11 ~18:3xZ)

Rows 5 and 8 amended for the CTO's R1-R5 (msg 108377, record section 5 @7a7e9b47c6): the 13:30Z MDPF fire is read before the flip (5d); the flip receipt names who owns each shared file after the flip (8). R3 (the `mdpf/{firm}/platinum/*` serving grant as a named FIRMBKTS cell before CANON M9) is a round-5 cell: the CTO carries it as an L10 addendum and it needs its own never-widen pair; nothing of it runs Monday.

## Rev 3b (~18:4xZ)

PRD v1.4 @1e5dcef9cb (L10 addendum R1-R5) bound two window checks, both added above. Check (d) was rehearsed in a scratch worktree at HEAD: the flip commit changes 16 files (registry 1, value-changing 2, mark-line only 13), and `bronze_homes.json` differs by its `_generated` mark line alone (1 line changed; its one feed, `orion_model_composition` on `opal-data-assets`, is untouched). The MDPF runner's read of `investor-reporting/directory/` through `opal-data-bd` (D1-S24's second reader) is not moved by the flip: the alias keeps serving that class.
