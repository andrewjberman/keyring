# AMGT_HARVST task order -- `HVST-cb-15` -- ROUND 87, workstream RUNNER-JOIN (CTO addendum 4 `ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF_ADDENDUM_4_SA_BBG_JOIN.md`, effective on C-a4; COO addendum 4 `deliverables/2.0.0_SA_COO_W1/round87/NEVER_WIDEN_HALF_COO_CB15_SA_BBG_JOIN.md` sha256 `41bb63dc024a8c1a542e10f0a51966db26fc211b29b094480ddcb9d41c6ab711`): `sa` AND `bbg` JOIN THE DELL1 HARVEST RUNNER, SEEDED ONCE

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cb-15.sa-and-bbg-join-the-dell1-runner-seeded</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cb-15</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the ONE task `Opal Data Harvest - Continuous Cycle` is re-registered with a longer publisher list. No other task is touched.
comp-iam: RUN at L5 -- an act on dell1's own task scheduler and progress database. NO Secrets Manager call by this seat, NO sign-in by this seat, NO key sent to any window, NO process ended by name or PID. The seed command READS S3 once per table (`sa` `article` 80.4 MiB and `listing_hit` 284.2 MiB, `bbg` `article` 202.2 MiB and `listing_hit` 0.1 MiB, about 567 MiB in all) and writes only `<runtime>\progress.sqlite3` and `<runtime>\silver_known_seed.json`. The RUNNER's own jobs write bronze and silver to `opal-data-harvest`.
comp-adversary: RUN at L5 -- the adversary is a seed run while the runner is still writing, a start before the seed, a `check` window that opens before the seed, an `sa` profile that has expired (every `sa` job then ends `sign_in_refused`), a `bbg` challenge in a minimised window, and a runner that reaches the Google credential or signs anything in.
</preflight>

## 0. THE CELL

`HVST-cb-13` re-pinned the dell1 runner to `ddd7dcdc38` for `wsj,barrons`, with the uploader fix (`HVST-cb-12`, `HVST-cb-14`) and a seeded local record. This cell adds `sa` and `bbg` to the SAME task: stop at a stop-file boundary, seed the two publishers' tables once while stopped, re-register from the SAME pin with `-Publishers wsj,barrons,sa,bbg`, start, read, and check for duplicates. No code changes.

## 1. START CONDITIONS (all read at the start, not assumed; any false: DO NOT START, file one row, and the issuer reads it)

- (a) **C-a4: `HVST-cb-13`'s evidence is TRUE.** `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/cb13_check.out` exists and ENDS with `DUPLICATES=0` over parts written after the cb-13 restart (`cb13_t0.txt`) AND carries at least one `CHECK` line with `parts_read` above 0 (a check over ZERO parts is vacuous and does NOT count: the cb-13 check taken at +45 minutes read `parts_read=0` for all four tables because no upload had happened yet, so SC1 repeats it after the first upload and keeps that output), AND `<runtime>\s3_get_ledger.jsonl` holds at least one `upload-harvest` line after that T0 with `get_count` 0 (print the first three such lines), AND `cb13_reads.out`'s R7 projection is under 5 GiB for `wsj` and `barrons`. If any of the three is absent: DO NOT START (the issuer waits for the first upload).
- (b) The pair is SIGNED: the earlier halves (as `HVST-cb-13` 1.b), COO addendum 4 (compare its sha256 above) and the CTO addendum 4 (`ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF_ADDENDUM_4_SA_BBG_JOIN.md`). Read each with `git show <pin>:<path>`.
- (c) **ONE WRITER (C-b4):** `ledger/SITE_Z_RETIRE_READBACK_20261015.md` is on file; for the `sa` and `bbg` prefixes (derive them with `lib/research/harvest/store.py` `table_prefix` and `harvest_grammar.SOURCE_FOR_PUBLISHER`, never type them) list with `aws s3api list-objects-v2` (paginated, counted client-side, denominators printed) the newest `LastModified` per table: no object newer than 2026-10-15T19:04:24Z may have been written by site Z; print the newest `LastModified` of each table, and show that anything newer than the cutoff is dell1's (the runner of this pass did not run `sa` or `bbg`: nothing should be newer for `bbg` and `sa` other than local proofs, which upload nothing).
- (d) **C-c4: the `sa` session reads signed in.** BEFORE any stop, from `C:\dev\ajb_workspace` with the default runtime root (NOT the runner's): `python -m lib.opal_data_harvest run --tickers BA --publishers sa --max-jobs 1 --no-sign-in` must end `complete_candidates` with more than 0 accepted (read the run record's `status` and `accepted`). If it reads `sign_in_refused` or any other status: leave `sa` OUT of the list (`<publishers>` becomes `wsj,barrons,bbg`), say so in `cb15_start.out`, file one row, and ask the issuer; do not sign in.
- (e) The runner is running (one `cycle_runner` process, positive control), `Get-ScheduledTask` reads `Running`, and its registered `WorkingDirectory` is the cb-13 pin (record it as `<pin>`).

## 2. THE ACT (dell1, once)

`<main>` is `C:\dev\ajb_workspace`. `<pin>` is the registered `WorkingDirectory` of 1.e (`C:\dev\wk-harvest-runner-pin-ddd7dcdc38`). `<state>`, `<runtime>`, `<stop>` are exactly as in the registered task's own arguments (read them from `schtasks /query /xml`): do not change them. `<publishers>` is `wsj,barrons,sa,bbg` (or `wsj,barrons,bbg` if 1.d failed).
1. Open the ledger before any change: `python .tools/deploy_ledger.py open --slug harvst-cb15-sa-bbg-join-20261016 ...` with legs `STOP`, `SEED`, `ARM`, `CHECK`, `WINDOW`.
2. **Stop by the stop file, never a kill:** create `<stop>`; wait for the log's `STOP-FILE ... no further cycle` line and record the cycle record (`cb15_stopped.out`). **If 30 minutes after the stop file the log carries no such line: STOP, file a row, change nothing else.** Then `Stop-ScheduledTask` and a process census over ALL processes: no `cycle_runner`, no `backfill_driver`, no `lib.opal_data_harvest` python process (positive control; judge each hit by its command line: a log-tail or a shell wrapper is not a runner). Leave `<stop>` in place.
3. **THE SEED, runner stopped, from `<pin>`:** `python -m lib.opal_data_harvest.seed_silver_known seed --runtime-root "<runtime>" --publishers sa bbg --dry-run` first and read it (`rows_without_hash` must be 0 for every table), then WITHOUT `--dry-run`, once. `cb15_seed_dry.out`, `cb15_seed.out`; read `<runtime>\silver_known_seed.json` back: its `seeded_at` and the `keys` of EVERY table (it must still hold the `wsj` and `barrons` tables from the cb-13 seed). The seed's S3 reads are the only S3 table reads of this act; print their total. **If the seed raises, a table prints `rows_without_hash` above 0, or a cb-13 table vanished from the snapshot: DO NOT START; file a row.**
4. Delete `<stop>` (`Test-Path` False). `powershell -NoProfile -ExecutionPolicy Bypass -File "<pin>\lib\opal_data_harvest\install-cycle-schedule.ps1" -RepoRoot "<pin>" -Publishers <publishers> -StateDir "<state>" -RuntimeRoot "<runtime>" -StopFile "<stop>" -Windowless -RefreshOnce -Plan` first and read it (the interpreter ends `pythonw.exe`, `--refresh-once`, `--publishers` lists exactly `<publishers>` with spaces, the SAME `--state-dir` and `--runtime-root`, `WORKDIR` `<pin>`); then once without `-Plan`. `cb15_plan.out`, `cb15_register.out`. Just before `Start-ScheduledTask`, write `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/cb15_t0.txt` with ONE line `T0=<UTC ISO ending Z>` (AFTER the seed), then `Start-ScheduledTask` once.
5. **THE READS at +3 and +15 minutes, in `cb15_reads.out`** (each with its control), as `HVST-cb-13`: R1 log fresh, R2 task XML (`pythonw.exe`, `--refresh-once`, `WorkingDirectory` `<pin>`, the exact publisher list), R3 no console window, R4 checkpoint `done` grows by at least 3, R5 every runner window minimised, R6 per publisher the `JOB` and `STOP <publisher>:` lines since T0, **R7 (the bar)** per `command` and the projection of a 242-pair cycle in GiB. **If it exceeds 5 GiB: create `<stop>`, wait for the cycle record, do NOT re-register, and tell the issuer at once.** The `bbg` leg runs first in a pass (`cycle_runner.PUBLISHERS` order `bbg wsj barrons sa`).
6. **THE CHECK:** after the first `upload-harvest` line of the new pass for EACH of `sa` and `bbg` appears in the ledger (and at +45 minutes whatever has appeared), run `python -m lib.opal_data_harvest.seed_silver_known check --runtime-root "<runtime>" --publishers wsj barrons sa bbg --since <the T0 of step 4>` from `<pin>`; keep every output in `cb15_check.out`; it must END with `DUPLICATES=0`. A duplicate (exit 1) is Branch F. If a publisher has made no upload by +45 minutes, say so (the check is vacuous for it: print its `parts_read`).
7. **BRANCHES, signed:** **F** (a duplicate, an upload error that did not occur for `wsj` and `barrons`, or R7 above 5 GiB for a publisher): create `<stop>`, wait for the `STOP-FILE` line, `Stop-ScheduledTask`, delete `<stop>`, re-register with `-Publishers wsj,barrons` from `<pin>`, start once, file one row; the seeded records stay. **G** (CTO C-j): two consecutive `bbg` legs ending `bot_check` or `TargetClosedError`: re-register without `bbg` the same way, finding to the issuer. **E** (the `sa` session expires: `sa` jobs end `sign_in_refused` class `expired`): a recorded finding for the issuer; do NOT sign in by any hand and do not re-register for this alone.
8. **THE ACCOUNT STOP RULE:** the runner signs neither `sa` nor `bbg` in and never reaches the Google credential or the Kimi key; if a log line shows otherwise, create `<stop>` and tell the issuer at once.
Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/`. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cb15-sa-bbg-join-20261016.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cb-15"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.Arguments"</invocation><expect>--publishers wsj barrons (sa bbg|bbg)</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cb-15"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/cb15_check.out</invocation><expect>(?s)DUPLICATES=0\s*\Z</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cb-15"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/cb15_reads.out</invocation><expect>(?s)R7 command=upload-harvest.*sum_get_count=0</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. At the base AC1 reads `--publishers wsj barrons --refresh-once` (FAIL as expected); AC2's and AC3's files do not exist. `cb15_check.out` must END with `DUPLICATES=0`; `cb15_reads.out` must carry the R7 line for the `upload-harvest` command with `sum_get_count=0` (the cb-13 format).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cb-15.sa-and-bbg-join-the-dell1-runner-seeded.proof_of_spec.json` (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-cb-15.sa-and-bbg-join-the-dell1-runner-seeded` and `decomp_ref.to_ref` the path of THIS order file.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS.** Append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: CTO addendum 4 (msg 6460, effective on C-a4); Andrew-direct 2026-10-15 ~16:3xZ. C-i (READ_HERE.md, none applies: `ledger/CTO_CONDITION_C-i_BLOOMBERG_READ_HERE_20261015.md`), C-j (as Branch G) and C-k (as 1.c) stand.
- **STAGED, not sent:** waits on C-a4 (1.a): the first `upload-harvest` line under the cb-13 pin and `cb13_check.out` ending `DUPLICATES=0`. At 03:57Z the cb-13 pass had made 116 `run` lines at 0 GETs and no upload (the `wsj` leg stores nothing); the first uploads come with `barrons`. The issuer sends this order on the cb-13 evidence.
- **Not covered, named:** an `sa` expiry (a person's sign-in); a challenge in a minimised window for `bbg`; `ft`; an in-profile `sa` sign-in (a candidate cell).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>staged</status>
<round>87</round>
<workstream>RUNNER-JOIN</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
