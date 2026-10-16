# AMGT_HARVST task order -- `HVST-cb-9` (with `HVST-cb-7`) -- ROUND 87, workstream RUNNER-REREGISTER (CTO addendum 2 `ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF_ADDENDUM_2_REPIN.md` @21dc90d6b5; COO addendum 2 `deliverables/2.0.0_SA_COO_W1/round87/NEVER_WIDEN_HALF_COO_CB9_REPIN_AND_JOIN.md`): THE DELL1 HARVEST RUNNER RE-REGISTERED FROM THE CB-8 HEAD FOR FOUR PUBLISHERS

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cb-9.the-dell1-runner-re-registered-from-the-cb-8-head-with-four-publishers</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cb-9</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the ONE task `Opal Data Harvest - Continuous Cycle` is re-registered. No other task is touched.
comp-iam: RUN at L5 -- an act on dell1's own task scheduler, its own worktrees and the deletion of two copied files. NO Secrets Manager call by this seat, NO sign-in by this seat, NO key sent to any window, NO process ended by name or PID. The RUNNER's own jobs read `dowjones/credentials`, `bloomberg/session` and `seeking-alpha/session` by name and write bronze and silver to `s3://opal-data-harvest` as the existing harvester does.
comp-adversary: RUN at L5 -- the adversary is a stop that cuts a live cycle, a pin that lacks the cb-8 merge (the seed is then still needed), deleting the seeded copies before a job proved `browser_profile`, a re-registration that changes the state dir, runtime root or stop file, an `sa` leg that signs in by itself, and a second writer for a publisher.
</preflight>

## 0. THE CELL

The dell1 runner (registered by `HVST-cb-2`, from pin `C:\dev\wk-harvest-runner-pin-47c623dcf8`) runs `wsj` and `barrons`, with a seeded `<runtime>\secrets\` holding two copied `.dpapi` files (cb-2 amendment 1). `HVST-cb-8` (merged `a879d12881`) makes a profile-store publisher start a job without any saved bundle, and the CTO bound the seeded copies to be deleted when it lands. Andrew moved `sa` and `bbg` to dell1 too, and their local proofs are in (`ledger/ROUND87_LOCAL_PROOFS_20261015.md`).
This cell does ONE re-registration: new pin **Q**, publishers `wsj,barrons,sa,bbg`, the seeded copies deleted after the first job proves `browser_profile`, and nothing else.

## AMENDMENT 1 (issuer, 2026-10-16 ~00:3xZ; CTO msgs 6344 and 6353; GOVERNS wherever sections 1 and 2 below differ)

The first dell1 cycle showed that every collector job re-read the whole silver `article` prefix (about 29.6 GiB per `wsj` cycle), and the CTO stopped the runner at 00:01:34Z by its stop file. `HVST-cb-10` (per-process GET counters) and `HVST-cb-11` (a job's bound from local state, no silver S3 read) are merged. The CTO ruled: re-register `wsj` and `barrons` ONLY; `sa` and `bbg` join (a later order, `HVST-cb-7`) only after the first cycle on the new pin has recorded the UPLOADER's silver reads; the 5 GiB-per-cycle bar includes the uploader's reads. So, for this order:
- **`<publishers>` is `wsj,barrons`. `sa` and `bbg` are NOT started by this order.** The order's title and file name keep "four-publishers" because a file name does not change; the cell owned is `HVST-cb-9` only.
- **Q must also carry** `62fcc1978e` (cb-10) and `02d4090763` (cb-11), as well as `a879d12881`, `e6649b1250`, `d0c48b3946` and `39ae28559b`. Check each with `git merge-base --is-ancestor <c> Q`; the negative control is the reverse for `02d4090763`.
- **Start condition 1.c is replaced:** only the `wsj` cycle record `20261015T203204Z` (`completed: true`, written by the previous pin) must exist; print it. The `barrons` clause is WAIVED by the CTO (its cycle was cut by the stop file, record `20261015T234451Z`, `stopped_by_operator`).
- **Start condition 1.d lists the `wsj` and `barrons` prefixes only** (same method). **1.e is WITHDRAWN** (no `sa`). **1.f becomes:** the runner is NOT running (it was stopped at 00:01:34Z): a census over ALL processes finds no `cycle_runner` and no `backfill_driver` process (positive control), and `Get-ScheduledTask` reads `Ready`. If a runner process IS running: DO NOT START, file a row.
- **Step 3 (the stop) is already done:** `<stop>` EXISTS now. Do not wait for a record. Read that the last `barrons` cycle record is `stopped_by_operator`, then DELETE `<stop>` and read `Test-Path` False before the registration. Everything else in step 3 is skipped.
- **New read R7 (the bar):** at +15 minutes and again at the first `.cycle.json` of EITHER publisher, read `<runtime>\s3_get_ledger.jsonl` (lines whose `ended_at` is after T0): per `command` (`run`, `upload-harvest`) the line count, the sum of `get_count` and of `get_bytes`, and the average bytes per line; project a 242-pair cycle as (average `run` bytes per job + average `upload-harvest` bytes per upload x uploads per job) x 242 and print it in GiB. **If either projection exceeds 5 GiB: create `<stop>`, wait for the cycle record, do NOT re-register, and tell the issuer at once.** `cycle.json` also carries `s3_jobs_lines`, `s3_get_count_jobs`, `s3_get_bytes_jobs`: print them.
- **Proof criterion AC1 is replaced** (below). AC2 and AC3 stand; `cb9_seed_removed.out` still needs `token_source=browser_profile` read from a run record of the new pass (C-c2).

## 1. START CONDITIONS (all read at the start, not assumed; any false: DO NOT START, file one row, and the issuer reads it)

- (a) **Q** is the head of `box/dell1` at the start (`git rev-parse HEAD` in `C:\dev\ajb_workspace`, recorded). `a879d12881` (cb-8), `e6649b1250` (cb-5), `d0c48b3946` (ca-1) and `39ae28559b` (E1+E2) each pass `git merge-base --is-ancestor <c> Q`; the reverse of `a879d12881` is the negative control.
- (b) All SIGNED halves are on file and read at their pins: the first pair (COO `NEVER_WIDEN_HALF_COO_CB2_DELL1_RUNNER.md` @5271f99a66, sha256 `167561c11747ed9e2d0a51ac93024cc9e69baf625e3815933a40d87e4cb6d50b`; CTO `ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF.md`), addendum 1 (COO sha256 `0f811a062934a228436461b93ac1cdd8b405dc82ed82709806f6b4abf3ecc165`; CTO `ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF_ADDENDUM_1_SA_BBG.md` @4e7a011829) and addendum 2 (COO `deliverables/2.0.0_SA_COO_W1/round87/NEVER_WIDEN_HALF_COO_CB9_REPIN_AND_JOIN.md`, sha256 `3df7917cb98b4bd8872f56b3f0ba2d1f1d66e323da8101d74f2ef3af4c6edfbb`; CTO `ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF_ADDENDUM_2_REPIN.md` @21dc90d6b5). Read each with `git show <pin>:<path>` and compare every hash. The erratum (bucket `opal-data-harvest`) applies.
- (c) **THE FIRST COMPLETE CYCLES EXIST (C-b2):** under `C:\dev\ajb_workspace\.runtime\harvest-cycle\state\cycles\wsj\` and `...\barrons\` a `.cycle.json` with `"completed": true` and its `s3_get_count` and `s3_get_bytes` keys, written by the CURRENT pin's runner (`started_at` after 2026-10-15T20:32:04Z). Print both records' `cycle_id`, `started_at`, `ended_at`, `completed`, `failed`, `s3_get_count`, `s3_get_bytes`. If either is absent: DO NOT START; the issuer waits.
- (d) **ONE WRITER:** `ledger/SITE_Z_RETIRE_READBACK_20261015.md` is on file, and for ALL FOUR prefix pairs (`wsj`, `barrons`, `sa`, `bbg` under `HARVEST_BUCKET`; derive them with `lib/research/harvest/store.py` `table_prefix`, never type them; the bucket is `store.HARVEST_BUCKET`, read it, do not type it) you list with `aws s3api list-objects-v2` (paginated, counted client-side, denominators printed) and show NO object written after 2026-10-15T19:04:24Z by site Z: for `wsj` and `barrons` the objects after that time are dell1's own runner (it started 20:32Z; print the earliest `LastModified` after the cutoff and show it is not before 20:23Z); for `sa` and `bbg` NONE may be newer than the cutoff. A `sa` or `bbg` object newer than the cutoff: DO NOT START, file a row.
- (e) **`sa` still reads signed in (C-c1):** before any change, with the `sa` profile NOT in use by the runner (it is not yet in the runner's list), run `python -m lib.opal_data_harvest run --tickers BA --publishers sa --max-jobs 1 --no-sign-in` from `C:\dev\ajb_workspace`: the job must end `complete_candidates` with more than 0 accepted. Anything else: leave `sa` OUT of the list, say so in `cb9_start.out`, and file a row (the issuer asks Andrew to sign in again).
- (f) A dell1 runner is running and is the only one (a census over ALL processes of `pythonw` or `python` with `cycle_runner` in the command line: exactly 1, with a positive control).

## 2. THE ACT (dell1, once)

`<main>` is `C:\dev\ajb_workspace`. `<old>` is `C:\dev\wk-harvest-runner-pin-47c623dcf8`, `<new>` is `C:\dev\wk-harvest-runner-pin-<Q first 10 hex>`. `<state>`, `<runtime>` and `<stop>` are exactly as in the registered task's own arguments (read them from `schtasks /query /xml`): do not change them. `<publishers>` is `wsj,barrons,sa,bbg` (or `wsj,barrons,bbg` if 1.e failed).
1. Open the ledger before any change: `python .tools/deploy_ledger.py open --slug harvst-cb9-repin-four-20261015 ...` with legs `PIN`, `STOP`, `ARM`, `SEED`, `WINDOW`. `WINDOW` closes on the reads of step 6.
2. `git worktree add --detach "<new>" <Q>`; `git -C "<new>" rev-parse HEAD` must read Q, and `<old>` reads 47c623dcf8 (positive control). Lock `<new>` with `git worktree lock --reason "AMGT_HARVST live cycle runner pin (HVST-cb-9); govern GC must not remove"`; show `locked` for `<new>` AND `<old>`. `cb9_pin.out`.
3. **Stop by the stop file, never a kill:** create `<stop>`; wait until the running cycle's `.cycle.json` exists reading `stopped_by_operator` and the log carries `STOP-FILE ... no further cycle`; record the path and `ended_at` in `cb9_stopped.out`. **If 15 minutes after the stop file the log carries no `STOP-FILE` line: STOP, file a row, and do nothing else** (no key, no kill, no `Stop-ScheduledTask`). Then `Stop-ScheduledTask` and a process census: NONE (positive control). DELETE `<stop>` (read `Test-Path` False) before the next start.
4. `powershell -NoProfile -ExecutionPolicy Bypass -File "<new>\lib\opal_data_harvest\install-cycle-schedule.ps1" -RepoRoot "<new>" -Publishers <publishers> -StateDir "<state>" -RuntimeRoot "<runtime>" -StopFile "<stop>" -Windowless -RefreshOnce -Plan` first and read it: the `ACTION` interpreter ends `pythonw.exe`, the arguments contain `--refresh-once`, `--publishers` lists exactly `<publishers>` with spaces, `--state-dir` and `--runtime-root` are the same as before, `WORKDIR` is `<new>`. `cb9_plan.out`. Then the same without `-Plan`, once (`cb9_register.out`). Just before `Start-ScheduledTask`, write `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/cb9_t0.txt` with ONE line `T0=<UTC ISO ending Z>`, then `Start-ScheduledTask` once.
5. **THE SEED STAYS UNTIL A JOB PROVES `browser_profile` (C-c2).** Wait for the first `wsj` or `barrons` job of the new pass to end; open ITS run record under `<runtime>\runs\` (by the `JOB` line's `run_id`) and read `token_source`. Only if it reads `browser_profile` and the job did not end `sign_in_refused`: delete `<runtime>\secrets\wsj.dpapi` and `<runtime>\secrets\barrons.dpapi` (and the `secrets\` directory if empty), record names, sizes and the deletion (`Test-Path` False) in `cb9_seed_removed.out`. If `token_source` reads anything else: DO NOT delete, take Branch F (step 7), and file a row. Do not delete anything under `<main>\.runtime\opal-data-harvest\secrets\`.
6. **THE FIVE READS, at +3 and +15 minutes, in `cb9_reads.out`** (each with its control), the same as `HVST-cb-2` step 6 (R1 log fresh, R2 task XML `pythonw.exe` and `--refresh-once` and the exact publisher list, R3 no console window, R4 checkpoint `done` grows by at least 3 between +3 and +15, R5 every runner Chrome window minimised using `deliverables/2.0.0_SA_COO_W1/round87/cb5_window_probe.py` `chrome_windows()`), plus **R6**: for each publisher in the list, the count of its `JOB` lines and of `STOP <publisher>:` lines since T0 (a `bbg` stop of `bot_check` or `TargetClosedError` is CTO condition C-j: record it; on the SECOND consecutive one, take Branch G).
7. **ROLLBACK (Branch F), signed:** if R1 or R4 reads FALSE at +15, or a `wsj` or `barrons` job ends `sign_in_refused` with `token_source` None: stop by the stop file as in step 3, restore the two seeded copies (a COPY from `<main>\.runtime\opal-data-harvest\secrets\`, within one box and one user, never printed) if they were deleted, re-register from `<old>` with `-Publishers wsj,barrons` and the same flags, start once, file one row, and say so in `cb9_reads.out`. `<old>` stays locked until `HVST-cb-6` closes. R2, R3 or R5 FALSE with R1 and R4 TRUE is NOT a rollback: file the row and leave it running.
8. **Branch G (CTO C-j):** two consecutive `bbg` legs ending `bot_check` or `TargetClosedError` drop `bbg` by a re-registration without it (the same steps 3-4), with the finding to the issuer; do not touch the other publishers.
9. **THE ACCOUNT STOP RULE (as in `HVST-cb-2`):** a `REFRESH <publisher>: FAILED`, or two `REFUSAL` lines for one publisher after its refresh, WITH a request made (a run record with non-empty `request_attempts`): do not re-register and do not sign in by hand; file ONE row (publisher, class, `http_status`, `host`, `login_redirect`). The runner never signs `sa` or `bbg` in; an `expired` refusal for either is a recorded finding for the issuer, never a repair.
Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/`. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>`, then keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cb9-repin-four-20261015.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cb-9"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.WorkingDirectory"</invocation><expect>(?s)\A(?!.*47c623dcf8).*wk-harvest-runner-pin-[0-9a-f]{10}</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cb-9"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/cb9_seed_removed.out</invocation><expect>(?s)token_source=browser_profile.*Test-Path.*False</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cb-9"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/cb9_windows.out</invocation><expect>(?s)NOT_MINIMISED=0.*NOT_MINIMISED=0</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC1 is a scheduler read on dell1 (AMENDED: the working directory must be a runner pin that is NOT the old `47c623dcf8`); at the base it reads the old pin, so it FAILS as expected; AC2's and AC3's files do not exist. `cb9_seed_removed.out` must carry the literal text `token_source=browser_profile` (the run record's value) and a `Test-Path` line reading False. `cb9_windows.out` must carry a `NOT_MINIMISED=<n>` line per read.
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cb-9.the-dell1-runner-re-registered-from-the-cb-8-head-with-four-publishers.proof_of_spec.json` with `to_id` `AMGT_HARVST.TO-HVST-cb-9.the-dell1-runner-re-registered-from-the-cb-8-head-with-four-publishers` and `decomp_ref.to_ref` the path of THIS order file.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS.** Append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: CTO addendum 2 (msg 6234); Andrew-direct 2026-10-15 ~16:3xZ; the CTO's bound on the seeded copies (msg 6216).
- **SENT 2026-10-16 ~00:4xZ under AMENDMENT 1 (status pending).** Before the amendment it waited on 1.c (the first complete `wsj` and `barrons` cycles with the E2 line). The first wsj cycle began 20:32Z; its length is organic (about 242 pairs per publisher). The issuer reads the cycle records and sends this order on the GO of that read; the executor then reads 1.c itself.
- **The real-job proof of `HVST-cb-8` is step 5** (the first pass after the re-pin with the seed to be deleted): not a separate job, because the production runner holds the publisher profiles and a second Chrome on one would collide with it. The CTO's half rules the same.
- **Not covered, named:** `sa`'s expiry (a person's sign-in); a challenge repair in a minimised window; `ft` (Andrew's session, not yet provided).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>pending</status>
<round>87</round>
<workstream>RUNNER-REREGISTER</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
