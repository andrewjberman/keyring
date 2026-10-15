# AMGT_HARVST task order -- `HVST-cb-2` -- ROUND 87, workstream RUNNER-REGISTER (`1.0.0_SA_CTO~DELL1` addenda 3 and 4, CTO half `ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF.md` @5e75337456): THE DELL1 HARVEST CYCLE RUNNER REGISTERED FOR `wsj` AND `barrons`

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-cb-2.the-dell1-runner-registered-for-wsj-and-barrons</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-cb-2</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~SC1</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- ONE scheduled task is registered on dell1, `Opal Data Harvest - Continuous Cycle`, which does not exist on this box today. No other task is touched.
comp-iam: RUN at L5 -- an act on dell1's own task scheduler, its own worktrees and ONE user-level environment variable. NO Secrets Manager call by this seat, NO sign-in by this seat, NO key sent to any window, NO process ended by name or PID. The RUNNER's own jobs read `dowjones/credentials` by name and write bronze and silver to `s3://opal-data-assets` as the existing harvester does.
comp-adversary: RUN at L5 -- the adversary is a runner started while site Z still writes the same publisher (two writers), a registration whose profile root follows the pin (every re-pin starts logged out), a stop that cuts a live cycle, a runner that registers but never spawns, and a visible Chrome window left on the desktop.
</preflight>

## 0. THE CELL

Andrew moved all harvest operations to dell1. Site Z's runner is stopped and its formal Disabled read-back is owed (see 1.c). This cell registers the ONE scheduled runner on dell1 for the two Dow Jones publishers from pin **P**, reads it at +3 and +15 minutes, and nothing else. `bbg`, `sa` and `ft` are not in this cell: they join by a re-registration under their own addendum to the pair.
The runner is the production writer from its first cycle. It runs one pair after another (`--no-sign-in` jobs), uploads after each job that left something pending, and with `--refresh-once` renews a refused publisher's profile at most ONCE per publisher per cycle (`verification.renew`, merged `d0c48b3946`).

## 1. START CONDITIONS (all read at the start, not assumed; any false: DO NOT START, file one row, and the issuer reads it)

- (a) P is the head of `box/dell1` at the start (`git rev-parse HEAD` in the main tree, recorded). After `git fetch origin box/dell1`, each of `39ae28559b` (NFRA_OPLGTW E1+E2), `d0c48b3946` (HVST-ca-1), `08c80a8f75` (HVST-cb-1) and `e6649b1250` (HVST-cb-5) passes `git merge-base --is-ancestor <c> P`; read the reverse for `e6649b1250` (P is not an ancestor of it) as the negative control. Nothing here pushes.
- (b) BOTH never-widen halves are on file and read SIGNED: COO half `org/missions/D5/AMGT/AMGT_HARVST/deliverables/2.0.0_SA_COO_W1/round87/NEVER_WIDEN_HALF_COO_CB2_DELL1_RUNNER.md` @5271f99a66 and CTO half `org/missions/D5/AMGT/AMGT_HARVST/ledger/NEVER_WIDEN_ROUND87_CB2_CTO_HALF.md` @5e75337456. Read each with `git show <pin>:<path>`, and the COO half's sha256 must equal `167561c11747ed9e2d0a51ac93024cc9e69baf625e3815933a40d87e4cb6d50b`.
- (c) **ONE WRITER (CTO C-g):** the file `org/missions/D5/AMGT/AMGT_HARVST/ledger/SITE_Z_RETIRE_READBACK_20261015.md` exists at HEAD and quotes site Z's FORMAL read-back (the task `Opal Data Harvest - Continuous Cycle` Disabled, a process census with a positive control). The issuer writes it when MSTR relays it; if it is absent: DO NOT START. Then read S3 yourself: for the `wsj` and `barrons` bronze and silver prefixes under `s3://opal-data-assets` (derive them with `lib/research/harvest/store.py` `table_prefix`, never type them), list with `aws s3api list-objects-v2` (paginated, counted client-side, denominators printed) and record the newest `LastModified` per prefix: each must be OLDER than the read-back's time. A prefix written after it: DO NOT START, file a row.
- (d) No `cycle_runner` or `backfill_driver` python process is running on dell1 (a census over ALL processes with a positive control), and `Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle'` finds none.

## 2. THE ACT (dell1, once)

`<main>` is `C:\dev\ajb_workspace`. `<pin>` is `C:\dev\wk-harvest-runner-pin-<P first 10 hex>`. `<state>` is `<main>\.runtime\harvest-cycle\state`, `<runtime>` is `<main>\.runtime\harvest-cycle\runtime`, `<stop>` is `<main>\.runtime\harvest-cycle\STOP`.
1. Open the ledger before any change: `python .tools/deploy_ledger.py open --slug harvst-cb2-dell1-runner-20261015 ...` with legs `PIN`, `ENV`, `ARM`, `WINDOW`. `WINDOW` closes on the reads of step 6.
2. `git worktree add --detach "<pin>" <P>`, then `git -C "<pin>" rev-parse HEAD` (must read P). Lock it: `git worktree lock --reason "AMGT_HARVST live cycle runner pin (HVST-cb-2); govern GC must not remove" "<pin>"`; `git worktree list --porcelain` shows the `locked` line. `cb2_pin.out`.
3. **The profile root survives a re-pin:** `[Environment]::SetEnvironmentVariable('OPAL_HARVEST_PROFILE_ROOT', '<main>\.runtime\opal-data-harvest\browser-profiles', 'User')`, then read it back from the registry AND from a FRESH process (`powershell -NoProfile -Command '$env:OPAL_HARVEST_PROFILE_ROOT'`). `cb2_env.out`. (Without it the profile root follows the pin's checkout and every re-pin starts logged out.)
4. Create the stop file's parent directory first: `New-Item -ItemType Directory -Force "<main>\.runtime\harvest-cycle"` (row `AMGT_HARVST-Z-S120`: nothing else creates it); `<stop>` itself must NOT exist.
5. `powershell -NoProfile -ExecutionPolicy Bypass -File "<pin>\lib\opal_data_harvest\install-cycle-schedule.ps1" -RepoRoot "<pin>" -Publishers wsj,barrons -StateDir "<state>" -RuntimeRoot "<runtime>" -StopFile "<stop>" -Windowless -RefreshOnce -Plan` first and read it: the `ACTION` interpreter ends `pythonw.exe`, the arguments contain `--refresh-once` and `--publishers wsj barrons`, `--state-dir` is `<state>`, `WORKDIR` is `<pin>`. `cb2_plan.out`. Then the same command without `-Plan`, once (`cb2_register.out`). **Just before `Start-ScheduledTask`, write `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/cb2_t0.txt` holding ONE line `T0=<the current UTC time, ISO, ending Z>`**, then `Start-ScheduledTask` once, and leave the box.
5b. **AMENDMENT 1 (issuer, 20:3xZ; applies to a RESTART after the first pass failed, read in `cb2_reads.out` and the runner log): seed the runner's saved-session directory.** The collector job (`--no-sign-in`) asks `TokenFirstSessions.get(publisher)` for a stored session BEFORE it opens the tab; the runner's runtime root `<runtime>` has no `secrets\` directory, so every job ended `sign_in_refused` with `token_source` None and no request made (run record `20261015T202310Z-wsj-23b255623f`), and the profile (the real session store) was never asked. Before starting again: create `<runtime>\secrets\` and copy `wsj.dpapi` and `barrons.dpapi` from `<main>\.runtime\opal-data-harvest\secrets\` into it (a copy within one box and one Windows user; never print or open the files; record names, sizes and SHA-256 in `cb2_seed.out`). The tab transport does not read the copied bundle for these two publishers (`seed_from_bundle` false); it only has to EXIST. Then delete `<stop>`, `Start-ScheduledTask` once, write a NEW `cb2_t0.txt` line `T0=...` and repeat the reads of step 6 at the new +3 and +15 minutes (keep the first pass's reads in the file, labelled). The account stop rule of step 8 applies afresh: the first pass's two refusals were the empty directory, not the account (no request reached the publisher); a refusal AFTER a refresh in the new pass, with a request made, is the rule.
6. **THE FIVE READS, at start + 3 minutes and again at start + 15 minutes, in `cb2_reads.out`** (each with its control):
   - **R1** `<state>\cycle_runner.log`: the last write is under 5 minutes old at +3 and a NEW line exists at +15.
   - **R2** `schtasks /query /xml /tn "Opal Data Harvest - Continuous Cycle"`: the `<Command>` ends `pythonw.exe` and the `<Arguments>` contain `--refresh-once`. Save the XML as `cb2_task.xml`.
   - **R3** no console window: for the runner's PID, `MainWindowHandle` 0 and NO `conhost.exe` child (control: the same read on a console `python.exe` shows a `conhost.exe` child). `cb2_console.out` carries `MainWindowHandle=0` and `CONHOST_CHILD=NONE`.
   - **R4** the real collector spawn works: the new cycle's `.checkpoint.json` `done` length grows by at least 3 between +3 and +15, and the log carries no `AttributeError`, `OSError` or `WinError` line since the start.
   - **R5 the windows:** with the issuer's `deliverables/2.0.0_SA_COO_W1/round87/cb5_window_probe.py` functions `chrome_windows()` (import it by path; do not run its `main`), list the visible Chrome windows twice, 10 seconds apart, at each read: every window that is not one the box had open BEFORE the start (record those first) must read minimised. `cb2_windows.out` carries a line `NOT_MINIMISED=<n>` per read and the control (a plain Chrome window read not minimised, then closed).
7. **ROLLBACK, signed:** if R1 or R4 reads FALSE at +15, stop by the stop file (create `<stop>`; the runner ends after its current pair; wait for the `.cycle.json`; then DELETE `<stop>`), then `Disable-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle'` (do NOT unregister), file one row naming the reading, and say so in `cb2_reads.out`. R2, R3 or R5 FALSE with R1 and R4 TRUE is NOT a rollback: file the row and leave it running.
8. **THE ACCOUNT STOP RULE:** from the start, read `cycle_runner.log` and the cycle checkpoint at each read for `REFRESH <publisher>: FAILED` or two `REFUSAL` lines for one publisher after its refresh. If a refresh FAILED, or a publisher refuses again after its one refresh, **do not re-register and do not sign in by hand**: file ONE row naming the lines (publisher, class, `http_status`, `host`, `login_redirect`) and keep working. The shared Dow Jones login can lock; a second attempt by any hand is the issuer's call.
Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/`. Anything odd: one row `AMGT_HARVST-D1-S<next free D1 number>` in the investigation file, then keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-cb2-dell1-runner-20261015.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on dell1)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-cb-2"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.WorkingDirectory"</invocation><expect>wk-harvest-runner-pin-</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-cb-2"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.Arguments"</invocation><expect>(?s)--publishers wsj barrons.*--refresh-once|--refresh-once.*--publishers wsj barrons</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-cb-2"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/round87/cb2_windows.out</invocation><expect>(?s)NOT_MINIMISED=0.*NOT_MINIMISED=0</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC1 and AC2 are reads of the scheduler on dell1; at the base no such task exists, so both FAIL as expected (`Get-ScheduledTask` finds none), and AC3's file does not exist.
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~SC1/AMGT_HARVST.TO-HVST-cb-2.the-dell1-runner-registered-for-wsj-and-barrons.proof_of_spec.json` (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-cb-2.the-dell1-runner-registered-for-wsj-and-barrons` and `decomp_ref.to_ref` the path of THIS order file.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS.** Append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Commit with `.tools/safe-commit.sh`. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them (the runner writes `opal-data-assets` harvest prefixes only).

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: CTO addenda 3 and 4; Andrew-direct 2026-10-15 ~16:3xZ. Pair: COO half @5271f99a66 + CTO half @5e75337456 (both GIVEN). CTO ruled: (c) minimise first (done: HVST-cb-5 merged `e6649b1250`, AC3 PASS `2657939237`), then (a) register and read the first cycle's effect on the terminals; if the registration shows a job failing minimised that passes headful, do not leave it registered headful, return the question to the CTO.
- **SENT 2026-10-15 ~20:2xZ (status pending):** site Z's formal read-back is filed (`ledger/SITE_Z_RETIRE_READBACK_20261015.md`, runner ended 18:33:06Z, task Disabled 19:04:24Z, site Z's read relayed by MSTR 6192 and CTO 6194). Before it was sent, the order waited on (c) above, site Z's formal Disabled read-back (CTO C-g), which `0.0.0_AB_MSTR~DELL1` relays and the issuer files as `ledger/SITE_Z_RETIRE_READBACK_20261015.md`. The 18:54Z STOPPED read is not enough for a 24/7 writer.
- Executor `0.7.0_AE_CloudOps~SC1`: live on dell1, idle, no open order at 19:5xZ. Delivered by the broker with this file's path; not crossbox.
- **The close read is `HVST-cb-6` (read only, cut at the registration):** the first productive cycle per publisher, with the `.cycle.json` record, the accepted count and `s3_get_count` / `s3_get_bytes` (CTO C-h, the E2 proof). It is organic and about a cycle length.
- **Not covered, named:** a challenge repair (Press and Hold, slider) in a minimised window (Barron's has `automatic_verification_enabled`): the first reads watch for it; `bbg` and `sa` are not in the runner.

- **Unmeasured, for the first reads (issuer, 20:1xZ):** a CHALLENGE repair in a minimised window. Bloomberg samples this seat took: minimised, with a Press and Hold challenge, 1 job ended `TargetClosedError`; the same job with the minimise call disabled solved the challenge and ended complete (5 accepted); a minimised job that met no challenge ended complete (5 accepted). Three samples cannot separate the window from chance. If a `barrons` or `wsj` job ends `TargetClosedError` or `challenge_failed` at a challenge, file the row with the job id and keep the runner as it is.

- **AMENDMENT 1 (issuer, 20:3xZ), from the first pass (SC1 msg 6206, rows `D1-S19`, `D1-S20`):** the stop rule fired correctly on two refusals after a refresh and the runner ended itself at 20:27:16Z, nothing stored. Cause read from the runner log and the job record, not guessed: `TokenFirstSessions.get()` demands a stored session even for a publisher whose tab never uses one, and the runner's runtime root has none (the manual jobs worked because `.runtime/opal-data-harvest/secrets/` holds the 16:1xZ bundles). The refresher's `done` in 3 s was the in-profile renew finding the profile already signed in. The seed (step 5b) is an operational unblock; the durable fix is `HVST-cb-8` (a code cell: `get()` returns a profile-store envelope for such a publisher), which lands by a re-pin under its own pair half. The first pass also proved: the registration, the pin, the env var, no console, the stop file.

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>pending</status>
<round>87</round>
<workstream>RUNNER-REGISTER</workstream>
<slot>dell1</slot>
<fabric>dell1</fabric>
