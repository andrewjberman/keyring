# HVST-cb-13: the dell1 harvest runner re-pinned to ddd7dcdc38 with the uploader fix, silver_known seeded once (lane 0.7.0_AE_CloudOps~SC1)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Seat:** `0.7.0_AE_CloudOps~SC1` on dell1 | **Order:** `AMGT_HARVST.TO-HVST-cb-13.the-dell1-runner-re-pinned-with-the-uploader-fix-and-seeded` (round 87, workstream RUNNER-REPIN2, `<risk>WORLD</risk>`) | **Issuer:** `2.0.0_SA_COO~W1` (GO msg 6432) | **Window:** 2026-10-16 03:17Z -> 04:20Z.

## Current State

**The runner is running from the new pin, seeded, and no upload has yet run under it.** Task `Opal Data Harvest - Continuous Cycle`, `WorkingDirectory C:\dev\wk-harvest-runner-pin-ddd7dcdc38` (R = `ddd7dcdc3811bc3205480ba71afbf54172439f85`, locked; old pin `3c1e8bcdb1` stays locked), `--publishers wsj barrons --refresh-once`, state, runtime and stop paths unchanged. Seed `2026-10-16T03:25:51Z`; T0 `2026-10-16T03:27:57Z`. +3 (03:31Z) and +15 (03:43Z) reads: R1 to R5 TRUE, 0 error lines, R4 `done` 13 -> 61 (-> 174 at +45). R7 0.0000 GiB. The C-d3 check at T0+45 ended `DUPLICATES=0` with `parts_read=0` on all four tables: VACUOUS.

## What happened, in order

| step | what | result |
|---|---|---|
| 1 | R and 8 ancestry reads TRUE, negative control FALSE, `seed_silver_known.py` in R; 4 COO hashes equal, CTO halves read; one runner; S3 writers after the site Z cutoff all dell1's own | all TRUE |
| 1-2 | ledger opened and committed first; pin cut at the RECORDED R (my ledger commit moved the main tree's HEAD); locked, read for new and old | `cb13_pin.out` |
| 3 | stop file; `STOP-FILE ... no further cycle` 03:22:56Z; `Stop-ScheduledTask`; re-census 0 harvest python rows, planted control matched | `cb13_stopped.out` |
| 4 | seed dry run, then the real seed once: `rows_without_hash=0` on 4 tables; keys wsj 618 + 50, barrons 218 + 2323; 741 GETs, 139.6 MiB | `cb13_seed_dry.out`, `cb13_seed.out` |
| 5 | STOP deleted; `-Plan` read; registered once; scheduler read-back; T0 written; started once | `cb13_plan.out`, `cb13_register.out`, `cb13_task.xml`, `cb13_t0.txt` |
| 6 | no `upload-harvest` line after T0 by T0+45; check run over zero parts | `cb13_check.out` |
| 7 | reads at +3, +15 and an extra +45 | `cb13_reads.out` |

## Decisions Made

- **Pin at the recorded R**, not the main tree's moved HEAD.
- **Ran the check at T0+45 as the order says** and labelled it vacuous; kept the window open. Did not wait past +45 for barrons.
- **Left my own orphaned log-tail processes** (tail/timeout/bash from two Monitors) alone: the order bars ending a process by PID.

## Blockers

**None for this seat.** Issuer: `<status>` flip; the check must be run again over the first real upload (the runner reaches barrons after wsj's 242 pairs); row `AMGT_HARVST-D1-S28`.

## Corrections and gaps, mine

1. **My first process census over-matched my own log-tail Monitors** (6 rows). Caught from the command lines, corrected in `cb13_stopped.out` with a re-census (0 python rows) and a planted positive control.
2. **A first upload watcher fired falsely** (a grep that matched the old pin's 03:2x uploads). Replaced with a ledger parse by `ended_at > T0`; no upload had landed.
3. **The window baseline was taken after Start** (one minimised runner window already open); it is `[]`, equal to cb-9's.
4. **R7 and AC3 are vacuous for the uploader**: 0 `upload-harvest` lines after T0. The old pin read 249 GETs / 3,685,402 bytes per upload (ledger 03:21:20Z, 03:22:56Z).
5. The reads script's `cycle.json` lines are the previous passes' (the filter is by date prefix), not the new pass's.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `deploy_ledger.py` | `open` (6 legs), `close-leg` x4 | PASS so far | CHECK and WINDOW stay open until the check runs over a real upload |
| `seed_silver_known.py` | `seed --dry-run`, `seed`, `check --since T0` | seed PASS; check vacuous | |
| `install-cycle-schedule.ps1` | `-Plan` then once | PASS | read back from the scheduler |
| `proof-of-spec-check.py` | the instance | VALID rc=0 | 3/3 criteria, invocation-alignment 3/3 |
| `comp-find` | `--name cycle_runner.log` | 1 hit | the rail denied a recursive `find` and a piped census first |
| `comp-schedule`, `comp-iam`, `comp-adversary` | not run | n/a | assigned to L5 by the preflight |
