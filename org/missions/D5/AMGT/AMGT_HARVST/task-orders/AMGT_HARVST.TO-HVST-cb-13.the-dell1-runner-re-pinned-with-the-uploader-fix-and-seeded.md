# AMGT_HARVST task order -- `HVST-cb-13` -- ROUND 87, workstream RUNNER-REPIN2 (CTO addendum 3 `ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF_ADDENDUM_3_UPLOADER_REPIN.md`, condition C-d3, msg 6396; COO addendum 3 `deliverables/2.0.0_SA_COO_W1/round87/NEVER_WIDEN_HALF_COO_CB13_REPIN_FOR_UPLOADER.md` sha256 `80fb1e5a69a9606a723d7698846ea3dded77cff16d98ad8aaed5882f689aa85b`): THE DELL1 HARVEST RUNNER RE-PINNED TO A HEAD CARRYING THE UPLOADER FIX, SEEDED ONCE, FOR `wsj` AND `barrons`

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cb-13.the-dell1-runner-re-pinned-with-the-uploader-fix-and-seeded</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cb-13</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- the ONE task `Opal Data Harvest - Continuous Cycle` is re-registered. No other task is touched.
comp-iam: RUN at L5 -- an act on dell1's own task scheduler, its own worktrees and its own progress database. NO Secrets Manager call by this seat, NO sign-in by this seat, NO key sent to any window, NO process ended by name or PID. The seed command READS S3 once per table (`opal-data-harvest`, about 139 MiB for `wsj` and `barrons`) and writes only `<runtime>\progress.sqlite3` and `<runtime>\silver_known_seed.json`. The RUNNER's own jobs write bronze and silver to `opal-data-harvest` as before.
comp-adversary: RUN at L5 -- the adversary is a seed run while the runner is still writing (the snapshot would miss rows), a `check` window that opens BEFORE the seed (seeded parts counted as duplicates), a stop that cuts a live job, a pin that lacks the uploader fix or the seed command, and a start that precedes the seed (the first uploads would then append rows already in S3).
</preflight>

## 0. THE CELL

The dell1 runner runs `wsj,barrons` from pin `3c1e8bcdb1`. Since then `HVST-cb-12` (merge `c1df06b1ef`: the uploader appends without reading the target silver table, de-duplicating against a local `silver_known` table) and `HVST-cb-14` (merge `4d2a3e2187`: the lookup matches date keys; a one-off `seed` and `check` command, `lib/opal_data_harvest/seed_silver_known.py`) are merged. This cell re-registers the runner from a NEW pin **R** that carries both, seeds `silver_known` once while the runner is stopped (CTO C-d3), restarts it, reads it, and proves no row already in S3 was written again.

## 1. START CONDITIONS (all read at the start, not assumed; any false: DO NOT START, file one row, and the issuer reads it)

- (a) **R** is the head of `box/dell1` at the start (`git rev-parse HEAD` in `C:\dev\ajb_workspace`, recorded). Each of `4d2a3e2187`, `c1df06b1ef`, `02d4090763`, `62fcc1978e`, `a879d12881`, `e6649b1250`, `d0c48b3946` and `39ae28559b` passes `git merge-base --is-ancestor <c> R`; the negative control is the reverse for `4d2a3e2187`. `lib/opal_data_harvest/seed_silver_known.py` exists in R (`git cat-file -e R:lib/opal_data_harvest/seed_silver_known.py`).
- (b) The pair is SIGNED: the earlier halves and addenda (as in `HVST-cb-9`'s 1.b), COO addendum 3 above (compare the sha256) and the CTO addendum 3 (`ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF_ADDENDUM_3_UPLOADER_REPIN.md`, with C-d3). Read each with `git show <pin>:<path>`.
- (c) The runner is running (one `cycle_runner` process, positive control) and `Get-ScheduledTask` reads `Running`; print the last three lines of `cycle_runner.log`.
- (d) **ONE WRITER:** the site Z read-back file `org/missions/D5/AMGT/AMGT_HARVST/ledger/SITE_Z_RETIRE_READBACK_20261015.md` is on file; the newest `LastModified` of the `wsj` and `barrons` prefixes is written by dell1's own runner (it started 00:31:23Z).

## 2. THE ACT (dell1, once)

`<main>` is `C:\dev\ajb_workspace`. `<old>` is `C:\dev\wk-harvest-runner-pin-3c1e8bcdb1`, `<new>` is `C:\dev\wk-harvest-runner-pin-<R first 10 hex>`. `<state>`, `<runtime>` and `<stop>` are exactly as in the registered task's own arguments (read them from `schtasks /query /xml`): do not change them.
1. Open the ledger before any change: `python .tools/deploy_ledger.py open --slug harvst-cb13-repin-uploader-20261016 ...` with legs `PIN`, `STOP`, `SEED`, `ARM`, `CHECK`, `WINDOW`. `WINDOW` closes on the reads of step 7.
2. `git worktree add --detach "<new>" <R>`; `git -C "<new>" rev-parse HEAD` must read R; `<old>` reads `3c1e8bcdb1` (positive control). Lock `<new>` with `git worktree lock --reason "AMGT_HARVST live cycle runner pin (HVST-cb-13); govern GC must not remove"`; show `locked` for `<new>` AND `<old>`. `cb13_pin.out`.
3. **Stop by the stop file, never a kill:** create `<stop>`; wait for the log's `STOP-FILE ... no further cycle` line (the running job may be long: a `barrons` job that rejects dozens of candidate articles runs 15 minutes or more) and record the cycle record path and its `stopped` in `cb13_stopped.out`. **If 30 minutes after the stop file the log carries no `STOP-FILE ... no further cycle` line: STOP, file a row, change nothing else** (no key, no kill, no `Stop-ScheduledTask`). Then `Stop-ScheduledTask` and a process census over ALL processes: no `cycle_runner` and no `backfill_driver` and no `lib.opal_data_harvest` process (positive control). Leave `<stop>` in place for now.
4. **THE SEED, with the runner stopped (CTO C-d3), from `<new>`:** `python -m lib.opal_data_harvest.seed_silver_known seed --runtime-root "<runtime>" --publishers wsj barrons --dry-run` first and read it (the `SEED` lines: keys per table, `rows_without_hash` expected 0, `s3_gets`, `s3_bytes`; nothing is written); then the same command WITHOUT `--dry-run`, once. Save both outputs to `cb13_seed_dry.out` and `cb13_seed.out`; read that `<runtime>\silver_known_seed.json` exists and print its `seeded_at` and each table's `keys`. The seed's own S3 reads are the only reads of S3 tables this act makes; print their total. **If the seed raises, or any table prints `rows_without_hash` above 0, or the snapshot is missing: DO NOT START the runner; restore nothing; file a row.**
5. Delete `<stop>` (read `Test-Path` False). `powershell -NoProfile -ExecutionPolicy Bypass -File "<new>\lib\opal_data_harvest\install-cycle-schedule.ps1" -RepoRoot "<new>" -Publishers wsj,barrons -StateDir "<state>" -RuntimeRoot "<runtime>" -StopFile "<stop>" -Windowless -RefreshOnce -Plan` first and read it (the interpreter ends `pythonw.exe`, `--refresh-once`, `--publishers wsj barrons`, the SAME `--state-dir` and `--runtime-root`, `WORKDIR` `<new>`); then once without `-Plan`. `cb13_plan.out`, `cb13_register.out`. Just before `Start-ScheduledTask`, write `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/cb13_t0.txt` with ONE line `T0=<UTC ISO ending Z>`; this T0 is AFTER the seed. Then `Start-ScheduledTask` once.
6. **THE CHECK (C-d3):** after the first `upload-harvest` line of the new pass appears in `<runtime>\s3_get_ledger.jsonl` (and again at +30 minutes if the pass is still running), run `python -m lib.opal_data_harvest.seed_silver_known check --runtime-root "<runtime>" --publishers wsj barrons --since <the T0 of step 5>` from `<new>`. It must end with `DUPLICATES=0` (exit 0); save every output to `cb13_check.out`. **A duplicate (exit 1) is Branch F.** If no upload has appeared by +45 minutes, say so in `cb13_check.out` (the check is then vacuous: it ran over zero new parts, print `parts_read`) and keep the window open: the issuer reads it again.
7. **THE READS, at +3 and +15 minutes, in `cb13_reads.out`** (each with its control), the same as `HVST-cb-9`'s: R1 log fresh, R2 task XML (`pythonw.exe`, `--refresh-once`, the exact publisher list, `WorkingDirectory` `<new>`), R3 no console window, R4 checkpoint `done` grows by at least 3 between +3 and +15, R5 every runner Chrome window minimised (`deliverables/2.0.0_SA_COO_W1/round87/cb5_window_probe.py` `chrome_windows()`), plus **R7 (the bar)**: from `<runtime>\s3_get_ledger.jsonl` lines whose `ended_at` is after T0, per `command` (`run`, `upload-harvest`) the line count, the sum of `get_count` and of `get_bytes`, and the average bytes per line; print the projection of a 242-pair cycle in GiB. **If it exceeds 5 GiB: create `<stop>`, wait for the cycle record, do NOT re-register, and tell the issuer at once.** The expected reading for `upload-harvest` is ZERO GETs per line (the old pin read about 3 MiB per upload).
8. **ROLLBACK (Branch F), signed:** if R1 or R4 reads FALSE at +15, or an upload ends with an error that did not occur at `3c1e8bcdb1`, or R7 reads MORE per upload than before, or the check reads a duplicate: create `<stop>`, wait for the `STOP-FILE` line, `Stop-ScheduledTask`, delete `<stop>`, re-register from `<old>` with `-Publishers wsj,barrons` and the same flags, start once, file one row, and say so in `cb13_reads.out`. The `silver_known` table and the snapshot stay (inert at the old pin). R2, R3 or R5 FALSE with R1 and R4 TRUE is NOT a rollback: file the row and leave it running.
9. **THE ACCOUNT STOP RULE (as in `HVST-cb-9`):** a `REFRESH <publisher>: FAILED`, or two `REFUSAL` lines for one publisher after its refresh, WITH a request made: do not re-register and do not sign in by hand; file ONE row (publisher, class, `http_status`, `host`, `login_redirect`).
Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/`. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>` in the investigation file, then keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cb13-repin-uploader-20261016.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cb-13"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.WorkingDirectory"</invocation><expect>(?s)\A(?!.*3c1e8bcdb1).*wk-harvest-runner-pin-[0-9a-f]{10}</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cb-13"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/cb13_check.out</invocation><expect>(?s)DUPLICATES=0\s*\Z</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cb-13"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/cb13_reads.out</invocation><expect>(?s)upload-harvest.*get_count=0</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. At the base: AC1 reads the old pin (FAIL as expected); AC2's and AC3's files do not exist. `cb13_check.out` must END with the line `DUPLICATES=0` (the last output of the `check` run you keep); `cb13_reads.out` must carry an R7 line for the `upload-harvest` command with `get_count=0` in it (print the sum as `get_count=<n>`).
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cb-13.the-dell1-runner-re-pinned-with-the-uploader-fix-and-seeded.proof_of_spec.json` (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-cb-13.the-dell1-runner-re-pinned-with-the-uploader-fix-and-seeded` and `decomp_ref.to_ref` the path of THIS order file.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS.** Append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them (the runner writes `opal-data-harvest` harvest prefixes only).

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: CTO addendum 3 and C-d3 (msgs 6395 and 6396); Andrew-direct 2026-10-15 ~16:3xZ. The cb-12 merge `c1df06b1ef` plus the cb-14 merge `4d2a3e2187` carry the fix, the date-key lookup and the seed command.
- **The issuer's own dry run, read at 03:0xZ against the real bucket (read-only):** `seed --dry-run` for `barrons`: `article` 209 keys (65 GETs, 10,746,505 bytes), `listing_hit` 2,228 keys (245 GETs, 3,603,032 bytes), `rows_without_hash=0`, `keys_already_local=0`. The `wsj` seed (`article` 419 parts, 125.4 MiB) is NOT dry-run by the issuer; the executor reads it first (step 4).
- **Not covered, named:** `sa` and `bbg` (they join after this cell's R7 and the CTO's gate, a later order); a challenge repair in a minimised window; the vendor-side behaviour of the long Barron's jobs (a job that rejects dozens of candidates, 15 minutes or more).
- **SENT 2026-10-16 ~03:2xZ (status pending):** the CTO had no objection to cb-14 as the answer to C-d3 (msg 6396; none received in the 50 minutes since my message 6397).

- **COMPLETE 2026-10-16T05:22:21Z (issuer, 2.0.0_SA_COO~W1), WITH LIMITS:** SC1 report msg 6515 re-read: commit 314424bf21 in tree; proof VALID rc=0; task Running from pin ddd7dcdc38; seed rows_without_hash=0; R1-R5 TRUE at +3/+15, R7 0.0000 GiB. LIMIT: the C-d3 duplicate check read `parts_read=0` (VACUOUS) and R7's upload term covers 0 upload lines; no upload ran under the new pin. The uploader evidence is carried by HVST-cb-15 step 6b (C-a4', CTO msg 6513); row D1-S28 dispositioned by D1-S30.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>complete</status>
<round>87</round>
<workstream>RUNNER-REPIN2</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
