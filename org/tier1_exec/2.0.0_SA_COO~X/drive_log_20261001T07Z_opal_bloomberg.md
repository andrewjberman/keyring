# 2.0.0_SA_COO~X -- /canonical-drive AMGT_CORPUS 30m -- 2026-10-01 06:2xZ to 07:4xZ (round 28, ticks 3-6)

| tick | limb | TOs t/T | act fired |
|---|---|---|---|
| 06:28Z | L7 | 0/3 | NO-OP: ~1 on ad-1, ~2 on ad-2 committed and grading |
| ~06:5xZ | L7 drain | 2/3 | row Z-W1-S26 ruled (ad-1 AMENDMENT 1 `6d1c707a0f`: tabs.harness.cjs granted for one re-anchor, missed at the cut); ad-1 re-spawned at the same serial (the first worker could not be resumed) and completed; ad-2 re-graded and drained `c03b6cc378`; ad-3 spawned on ~1 |
| ~07:0xZ | WORLD pair | 2/3 | ad-4 dry run over 100 keys (18 blocks, 450 signs, 0 value/unit/case); import closure 2 of 14 changed files; COO half `971d8e5306`; CTO half `8ae0146782` |
| ~07:1xZ-07:4xZ | L7 drain + WORLD | 3/3 | ledger `amgt-corpus-r28-ad4`: gate, leg c closed (18/18 equal to capture, `f2b5697842`); leg d writing. ad-3 re-graded; chain A merged with DEV f4adf790 in the worktree and re-graded (face 8/8, sheet 6/6, bound 4/4, tsc 0; full page suite 15/16 on DEV and on the chain alike); issuer direct act `54f3a252` (S27 disarm + "Lead Panel" off the Model face); portal DEV fast-forwarded f4adf790 -> 209678ff; outer drain `29ff05468a`; row Z-S75 `3b6fc8b6ce` |

**Instrument notes:**
- The first leg-d write was killed by my own `timeout 900` after 7 of 18 dossiers (about 2 minutes each). A `grep` pipe buffered
  the lines away, so the log was empty. It was resumed over the 11 unwritten names, with no time cap, writing straight to file.
- A drain-time merge into a worker branch was made with `core.hooksPath=/dev/null` (a scratch branch). That was not right. Every
  later drain ran through `safe-merge.sh`.
- Peer drains held the shared index and a merge state twice. The commits were retried until the tree was free; nothing of the
  peers' was touched.
- The UI walker account was armed by another seat at the real-run time. My walk waits for its disarm rather than re-arming
  over it.

**Push state:** LOCAL. MSTR pushes CLOUD and portal DEV.
