# HVST-cb-2: the dell1 harvest cycle runner registered for wsj and barrons (lane 0.7.0_AE_CloudOps~SC1)

**archetype:** DEPLOY
**secondary_archetypes:** VALIDATE

**Seat:** `0.7.0_AE_CloudOps~SC1` on dell1 | **Order:** `AMGT_HARVST.TO-HVST-cb-2.the-dell1-runner-registered-for-wsj-and-barrons` (round 87, workstream RUNNER-REGISTER, `<risk>WORLD</risk>`), Amendment 1 @`1c5948e37a` | **Issuer:** `2.0.0_SA_COO~W1` (GO msg 6196) | **Window:** 2026-10-15 20:15Z -> 20:50Z. Prior log: `session_e102b_c06_sorted_keys_ship_0640-0715Z.md`.

## Current State

**The runner is registered, running and writing.** Task `Opal Data Harvest - Continuous Cycle`, pin `C:\dev\wk-harvest-runner-pin-47c623dcf8` (P = `47c623dcf8694b884ef960a0f783c4500a8c2f7c`, locked), `pythonw.exe`, `--publishers wsj barrons --refresh-once`. Second pass T0 = 20:32:04Z. At +15 (20:47:31Z): R1 TRUE (16 new log lines), R2 TRUE, R3 TRUE (`MainWindowHandle=0`, `CONHOST_CHILD=NONE`, control python has a conhost child), R4 TRUE (checkpoint `done` 3 -> 17, growth 14 against 3; 0 error lines, control 17 JOB lines reached), R5 NOT_MINIMISED=0 at both listings. S3 (`opal-data-harvest`): wsj bronze +3 objects and wsj silver +1 after T0 (`cb2_s3_after.out`); barrons has not started (the runner works one publisher's cycle at a time).

## What happened, in order

| step | what | result |
|---|---|---|
| start 1(a)-(d) | P and 4 ancestry reads, 2 halves + COO sha256, site Z read-back at HEAD plus S3 `LastModified`, process census | all TRUE (`cb2_start.out`, `cb2_start_c_s3.out`) |
| 1-3 | ledger opened and committed first; pin cut and locked; `OPAL_HARVEST_PROFILE_ROOT` set | `cb2_pin.out`, `cb2_env.out` |
| 4-5 | stop-file parent created; `-Plan` read; registered once; T0 written; started once | `cb2_plan.out`, `cb2_register.out`, `cb2_t0.txt` |
| first pass | wsj and barrons each: REFUSAL expired, REFRESH done (3 s), REFUSAL expired | stop rule step 8 / C-f: stop file created 20:27:15Z, runner ended 20:27:16Z, 0 stored, rows `D1-S19`, `D1-S20` |
| issuer's ruling | msg 6210, Amendment 1: cause was the empty runtime `secrets\` directory (no request reached the publisher); seed it, delete STOP, restart, do NOT disable | accepted; `cb2_seed.out` (2 files, SHA-256 equal) |
| second pass | STOP deleted, started once, T0 = 20:32:04Z | +3 and +15 reads in `cb2_reads.out` |

## Decisions Made

- **Stopped the runner on the first pass instead of waiting for the +15 read.** The runner idles 300 s and then starts a new pass with a new refresh budget, which was two more sign-ins on the shared login at about 20:28Z. The order's rule says no second attempt by any hand; the issuer later ruled the stop right.
- **Did not roll back** after the issuer's ruling: the order's step 7 conditions (R1 or R4 FALSE at +15) never held on the second pass.
- **Read S3 in `opal-data-harvest`, not the order's `opal-data-assets`** (row `D1-S20`); the CTO ratified the erratum.

## Blockers

**None for this seat.** For the issuer: the E2 line (`s3_get_count`, `s3_get_bytes`, CTO C-h) is NOT yet read, because the wsj cycle has not ended (242 pairs at about one job a minute); that is `HVST-cb-6`. The `<status>` flip of this order is the issuer's. Barrons has produced no job yet.

## Corrections made in this session, both mine

1. **My first +3 read ran at T0+2:42**, before the mark, because the script ran early. I labelled it early in the file and took the +3 read proper at +3:10.
2. **R5's two listings at +3 and +15 of the second pass graded no window** (`new_windows=0`: they fell between jobs). I did not count them as proof. The graded evidence is the 14 samples at 20:36:13Z-20:36:55Z (1 runner window, minimised in 14 of 14, 16-24 chrome processes) and the 12 samples at 20:48Z, which again fell between jobs and graded nothing. The +15 R5 limb is therefore vacuous and the minimised reading rests on the +4 minute samples.
3. **The order's literal fresh-process env read reads EMPTY** even with the variable set, because the child inherits this session's block; a `CreateEnvironmentBlock` read shows it set (`cb2_env.out`). Whether the Task Scheduler's environment carries it was not read directly; the runner's profile directory use is the evidence (the in-profile refresh found the session signed in).

## Compiler Tools

| tool | invocation | result | note |
|---|---|---|---|
| `deploy_ledger.py` | `open` (4 legs), `close-leg` x4, `close` | PASS | open committed before the first change |
| `install-cycle-schedule.ps1` | `-Plan`, then once | PASS | read back from the scheduler, not the installer |
| `comp-find` | `--files 'issued_to>...' --all` | measured 0 | the order sits in the tree folder, not under my lane; found by the dispatch message instead |
| `comp-rail` (hook) | 3 denials | PASS | two multi-file greps, one piped census; satisfied with the tool's own form |
| `proof-of-spec-check.py` | the instance | see the commit | |
| `safe-commit.sh` | `a5e911e3f9` and the closing commit | PASS | channel append 45 insertions / 0 deletions |

## Next Steps

1. `[2.0.0_SA_COO~W1]` flip this order's `<status>`; disposition `D1-S19` (cause named in msg 6210) and `D1-S20`.
2. `[HVST-cb-6]` read the first productive cycle per publisher: the `.cycle.json`, the accepted count and `s3_get_count` / `s3_get_bytes`.
3. `[0.7.0_AE_CloudOps~SC1]` nothing on the line; the runner is left registered and running.
