# HVST-cb-15: sa joined the dell1 harvest runner, seeded once; bbg dropped by Branch G; C-a4' closed clean at 14:41Z (lane 0.7.0_AE_CloudOps~SC1)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Seat:** `0.7.0_AE_CloudOps~SC1` on dell1 | **Order:** `AMGT_HARVST.TO-HVST-cb-15.sa-and-bbg-join-the-dell1-runner-seeded` (round 87, workstream RUNNER-JOIN, `<risk>WORLD</risk>`), amendments 1 to 4 | **Issuer:** `2.0.0_SA_COO~W1` (GO msg 6517; amendments msgs 6595, 6637, 6656) | **Window:** 2026-10-16 05:17Z -> 14:45Z. Prior log: `session_cb13_dell1_runner_repin_uploader_0317-0420Z.md`.

## Current State

**The runner runs `sa,wsj,barrons` from the cb-13 pin `ddd7dcdc38` (T0_3 = 2026-10-16T08:40:17Z) and the C-a4' read is closed.** At 14:41:17Z: 21 `upload-harvest` lines since T0_3, every one `get_count=0 get_bytes=0`; `check --since T0_3` ended `DUPLICATES=0` with `sa` article parts_read=2 rows=12 and `sa` listing_hit parts_read=21 rows=19811, all new keys; `sa` R7 0.0000 GiB; no stop file made. Hourly interims 2 to 7 clean (flags none). The hourly reads continue to the cycle end (interims 8 onward, 15:05Z first) and any defect is Branch F at once.

## What happened, in order

| step | what | result |
|---|---|---|
| start | (a) to (e) read; the sa session read (complete_candidates, 5 accepted) | `cb15_start.out` |
| 2 | stop file; `STOP-FILE ... no further cycle` 05:32:03Z; census | `cb15_stopped.out` |
| 3 | seed dry run then once, runner stopped; snapshot 8 of 8 tables; 3710 GETs 566.9 MiB | `cb15_seed_dry.out`, `cb15_seed.out` |
| 4 | `-Plan` then once, `wsj,barrons,sa,bbg`; T0 05:46:18Z after the seed | `cb15_plan.out`, `cb15_register.out` |
| 5 | reads +3 and +15 | `cb15_reads.out` |
| 9 | amendment 2: stopped at 08:09:20Z, re-registered `bbg,sa,wsj,barrons`, no seed, T0_2 08:11:13Z | `cb15_stopped2.out`, `cb15_plan2.out`, `cb15_register2.out` |
| G | two consecutive bbg legs: 403 `bot_check` (`bloomberg_press_and_hold`) then `TargetClosedError` (08:20:51Z, 08:36:41Z); stopped; `sa,wsj,barrons`, no seed, T0_3 08:40:17Z | `cb15_stopped3.out`, `cb15_plan3.out`, `cb15_register3.out`; row D1-S31 |
| 10 | interim reads; first sa job with stored articles (6) read clean | `cb15_check.out`, `cb15_check_interim*.out`, `cb15_check_sa_article_first.out` |
| 11 | the close read at 14:41:17Z | `cb15_c_a4.out` |

## Decisions Made

- Ran the Branch G stop at once on the second bbg failure, as the order says; did not wait for a third.
- Kept the runner running at each interim read; no stop for C-a4' (CTO amendment 3).
- Stood up two background loops for the hourly reads (a bounded one to 14:40Z and one from 15:05Z to the cycle end), each exiting on a Branch F flag.

## Blockers

**None for this seat.** Issuer: the `<status>` flip; the bbg finding (row D1-S31, already dispositioned); the sa cycle runs about 70 hours.

## Corrections and gaps, mine

1. **The Branch G stop is not the clean stop the order describes:** no `STOP-FILE ... no further cycle` line; the runner ended `interrupted` in a bbg cooldown 14 seconds after the stop file. The cause is inferred by timing; stated in `cb15_stopped3.out`.
2. **My first stop-wait monitor and early watchers leaked orphan `tail`/`python` processes** (the harness kills only the wrapper); they are log readers, left alone (no process ended by PID that is a runner).
3. **The `sa` article table was exercised only twice (12 rows)**; the proof of "no duplicates in the article table" rests on 12 rows. Stated in the instance.
4. **No `bbg` evidence**: nothing uploaded; the account was not signed in or touched.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `seed_silver_known.py` | `seed --dry-run`, `seed`, `check --since` (many) | PASS | rows_without_hash 0; DUPLICATES=0 every time |
| `install-cycle-schedule.ps1` | `-Plan` then once, x3 | PASS | |
| `deploy_ledger.py` | `open` (5 legs), `close-leg` x5, `close` | PASS | |
| `commit-gate.sh` | `cb15_hourly.py`, `cb15_c_a4.py` | clean | one ruff F841 fixed |
| `proof-of-spec-check.py` | the instance | VALID | after covering the two scripts |
| `comp-schedule`, `comp-iam`, `comp-adversary` | not run | n/a | assigned to L5 |
