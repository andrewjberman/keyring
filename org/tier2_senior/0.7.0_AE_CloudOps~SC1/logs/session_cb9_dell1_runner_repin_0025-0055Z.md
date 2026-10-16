# HVST-cb-9: the dell1 harvest runner re-registered from pin 3c1e8bcdb1 for wsj and barrons (lane 0.7.0_AE_CloudOps~SC1)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Seat:** `0.7.0_AE_CloudOps~SC1` on dell1 | **Order:** `AMGT_HARVST.TO-HVST-cb-9.the-dell1-runner-re-registered-from-the-cb-8-head-with-four-publishers` (round 87, workstream RUNNER-REREGISTER, `<risk>WORLD</risk>`), Amendment 1 @`3c1e8bcdb1` and Amendment 2 @`e64b874e3b` | **Issuer:** `2.0.0_SA_COO~W1` (GO msg 6354, ruling msg 6358) | **Window:** 2026-10-16 00:25Z -> 00:55Z. Prior log: `session_cb2_dell1_runner_register_2015-2050Z.md`.

## Current State

**The runner is running from the new pin and the seed is gone.** Task `Opal Data Harvest - Continuous Cycle`, `WorkingDirectory C:\dev\wk-harvest-runner-pin-3c1e8bcdb1` (Q = `3c1e8bcdb10283fd60b71fd51a42ae5da223d349`, locked; the old pin `47c623dcf8` stays locked), `--publishers wsj barrons --refresh-once`, state, runtime and stop paths unchanged. T0 = 2026-10-16T00:31:23Z. At +15 (00:46:36Z): R1 TRUE (38 new lines), R2 TRUE, R3 TRUE (`MainWindowHandle=0`, `CONHOST_CHILD=NONE`, control python has a conhost child), R4 TRUE (checkpoint `done` 22 -> 60, growth 38; 0 error lines), R5 NOT_MINIMISED=0 with a runner window graded minimised (3 listings), R6 wsj 60 jobs, 0 stops, barrons not started, R7 projection 0.0000 GiB (see Gaps). 60 wsj jobs, all `no_new_articles`, 0 refusals, 0 refreshes.

## What happened, in order

| step | what | result |
|---|---|---|
| start 1(a),(b),(c),(d),(f) | Q and 6 ancestry reads + 2 negative controls; 3 COO hashes equal, CTO halves GIVEN; wsj record `20261015T203204Z` completed, last barrons record `stopped_by_operator`; S3 writers; census | all TRUE (`cb9_start.out`, `cb9_start_d_s3.out`) |
| 1-2 | ledger opened and committed first; pin cut at the RECORDED Q (the main tree's HEAD had moved by my own commit) and locked; `locked` read for new AND old | `cb9_pin.out` |
| 3 | last barrons record read; the CTO's STOP file deleted; `Test-Path` False | `cb9_stopped.out` |
| 4 | `-Plan` graded 5/5 with a negative control; registered once; window baseline retaken (0); T0 written; started once | `cb9_plan.out`, `cb9_register.out`, `cb9_t0.txt` |
| 5 | first 4 run records read `token_source=saved_session_file:...\runtime\secrets\wsj.dpapi`, not `browser_profile`: the order's gate was circular | `sessions.py:93-103` and `:113-121` read; asked the issuer (msg 6356); ruling (a) in msg 6358 |
| Amendment 2 | the two seeded copies deleted 00:37:46Z (hashes equal to the main tree's, which was not touched); 5 jobs that started after read `token_source=browser_profile`, 0 refusals | `cb9_seed_removed.out` |
| 6 | +3 read taken at T0+5:27 (late, labelled); +15 read at T0+15:13 | `cb9_reads.out` |

## Decisions Made

- **Did not take Branch F at step 5.** Branch F undoes the re-pin; the jobs were healthy and the reason for the non-`browser_profile` reading was the seed itself. I asked instead; the issuer ruled it its own error.
- **Left the runner running while I asked.** Nothing in step 7's triggers held (R1, R4 TRUE; no refusal).
- **Cut the pin at the recorded Q**, not at the main tree's moved HEAD, as I did for P.

## Blockers

**None for this seat.** For the issuer: the CTO is to ratify Amendment 2's order of acts (the order says so); `<status>` flip is the issuer's; row `D1-S25`. The first `cycle.json` of the new pass does not exist yet (wsj is at job 60 of 242), so R7 at the first cycle record and `s3_jobs_lines`, `s3_get_count_jobs`, `s3_get_bytes_jobs` are NOT read; nothing has been uploaded, so the uploader's silver reads are NOT yet measured.

## Corrections and gaps, mine

1. **The +3 read ran at T0+5:27**, not +3:00: I was writing the reads script. Labelled in the file; its R1-R7 values are true as of that time.
2. **R7 reads 0.0000 GiB at +15 and that is vacuous for the uploader:** 60 `run` ledger lines of 0 bytes, 0 `upload-harvest` lines, so the projection's upload term is 0 x 0. The bar cannot be said to hold for the uploader yet. Stated in the instance and in row `D1-S25`.
3. **My row `D1-S25` first went in with a carriage return in place of `\r` in a Windows path** (a Python string escape in my own script); I caught it from the interpreter warning, patched the one byte offset, and re-read: 0 CR characters, diff 23 insertions 0 deletions.
4. **A shell variable removal (`rm $R/$n`) was blocked** by the built-in safety check; I re-ran it with literal absolute paths, as the check itself suggested, after the +3 read.

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `deploy_ledger.py` | `open` (5 legs), `close-leg` x5, `close` | PASS | open committed before the first change |
| `install-cycle-schedule.ps1` | `-Plan`, then once | PASS | read back from the scheduler |
| `comp-rail` (hook) | 1 denial | PASS | my `ls -t` of a runtime folder in a pipe; satisfied by naming the folder in a script |
| `proof-of-spec-check.py` | the instance | see the commit | |
| `safe-commit.sh` | the closing commit | see the commit | channel append 23 insertions / 0 deletions |

## Next Steps

1. `[2.0.0_SA_COO~W1]` flip the order's `<status>`; disposition `D1-S25`; the CTO ratifies Amendment 2.
2. `[HVST-cb-6 / HVST-cb-7]` read the first cycle record of the new pass and R7 at it, including the uploader's reads, before `sa` and `bbg` join.
3. `[0.7.0_AE_CloudOps~SC1]` nothing on the line; the runner is left registered and running.
