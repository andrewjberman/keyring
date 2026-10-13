# AMGT_HARVST task order -- `HVST-bz-10` -- ROUND 85, workstream REFRESH-SITEZ (`1.0.0_SA_CTO~DELL1` msg 5209, `ledger/ROUND_ANALYSIS.round84.md` section 2 item 1, row `AMGT_HARVST-Z-S119`, ruling (A) msg 5143): THE SITE Z CYCLE RUNNER RE-REGISTERED WITH `--refresh-once` AT A CYCLE BOUNDARY

<!-- ===================== WORKER FACE -- this is the WHOLE of the seat's context ===================== -->

<to_id>AMGT_HARVST.TO-HVST-bz-10.site-z-runner-registered-with-refresh-once</to_id>
<decomp_ref>
<decomp_doc>org/missions/D5/AMGT/AMGT_HARVST/decompositions/AMGT_HARVST_DECOMP.md</decomp_doc>
<owned_cells>HVST-bz-10</owned_cells>
</decomp_ref>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
<issued_by>2.0.0_SA_COO~W1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN at L5 (--drift) -- one scheduled task is re-registered, `Opal Data Harvest - Continuous Cycle`, the one HVST-bz-4 registered windowless. No other task is touched.
comp-iam: RUN at L5 -- an act on the site Z box's own task scheduler and its own worktrees. NO S3 write, NO Secrets Manager call by this seat, NO sign-in by this seat, NO key sent to any window, NO process ended by name or PID. The RUNNER's own refresh, once the flag is on, reads `dowjones/credentials` by name as the existing harvester does.
comp-adversary: RUN at L5 -- the adversary is a stop that cuts a live cycle, a re-registration that changes the state dir, the runtime root or the publishers, a refresh that fires more than once per publisher per cycle on the shared Dow Jones account (a lock), and a runner that registers but never spawns.
</preflight>

## 0. THE CELL

On 2026-10-13 both Dow Jones publishers ended their cycle `sign_in_refused` (row Z-S119): `wsj` after 35 pairs and 69 minutes, `barrons` on its first key. The runner runs every pair `--no-sign-in`, so an expired session has no repair. `HVST-bz-9`
(merged `44aadb7f1d`) and `HVST-bz-12` (merged `3d88eccbc3`), producer changes under signed pairs, add `--refresh-once`, OFF by default: a `wsj` or `barrons` refusal the response shows to be expiry gets ONE `SessionManager.refresh` per publisher per cycle (no other publisher is ever refreshed; row D1-S16) and the same pair is replayed once; every refusal is recorded with its class in the
cycle log (`REFUSAL` lines) and the cycle checkpoint (`refusals`, `refreshes`). This cell re-registers the task from pin **P = `3d88eccbc3`** with `-Windowless -RefreshOnce`, and nothing else. Today the runner runs windowless from `wk-harvest-runner-pin-995adcaeaa`;
`<old>` below is that pin and it stays locked as the rollback.

## 1. START CONDITIONS (all four read at the start, not assumed; any false: DO NOT START, file one row, and the issuer reads it)

- (a) After `git fetch origin CLOUD`, `git cat-file -e 3d88eccbc3` and `git merge-base --is-ancestor 3d88eccbc3 origin/CLOUD` both succeed. Read the reverse (`origin/CLOUD` is not an ancestor of P) as the negative control. If P is not on origin/CLOUD, nothing here pushes it.
- (b) BOTH never-widen halves are on file and read SIGNED at their pins: COO half `deliverables/2.0.0_SA_COO_W1/round85/NEVER_WIDEN_HALF_COO_BZ10_REFRESH_REPIN.md` and CTO half `ledger/NEVER_WIDEN_ROUND85_BZ10_CTO_HALF.md`.
  Read each with `git show <pin>:<path>`; the issuer states the pins in the crossbox line.
- (c) **The runner is PROGRESSING:** `cycle_runner.log`'s last write is less than 15 minutes old. If not, STOP: that is a different failure and this order does not take it.
- (d) **The account is not mid-use:** no sign-in of `wsj` or `barrons` by anyone is in progress on the box (no `dowjones_harvest_session.py` process; `query user` names the desktop session of `Opal Bloomberg`, because the refresh opens a real Chrome window there).

## 2. BEFORE THE STOP (as in HVST-bz-4)

The runner may be mid-cycle. Do not kill it:
- (i) Read the stop-file path from the task's own arguments (`--stop-file "<path>"`) and create that file. The runner finishes its current pair, writes the cycle record and exits.
- (ii) Wait until the cycle's `.cycle.json` exists reading `stopped_by_operator` (or `completed true`). Record the path, `ended_at` and `stopped` in `bz10_stopped.out`. **If 15 minutes after the stop file the log carries no `STOP-FILE` line and the record does not exist: STOP, file a row, and do nothing else**
  (no key, no kill, no `Stop-ScheduledTask`).
- (iii) **C-g:** the new pin keeps the old runtime root, so the same STOP file would end the new runner at once. DELETE it after (ii) and BEFORE `Start-ScheduledTask`. Record the delete (path, time, `Test-Path` reading False) in `bz10_stopped.out` and the ledger.

## 3. THE ACT (site Z box, once)

`<state>` is the state dir in the task's own `--state-dir` argument (`...\wk-harvest-runner-pin-c1be67f53c\.runtime\harvest-cycle\state`), which stays exactly as it is, and `<runtime>` its `--runtime-root`. `<new>` is `C:\Users\Opal Bloomberg\Desktop\wk-harvest-runner-pin-3d88eccbc3`.
1. Open the ledger before any change: `python .tools/deploy_ledger.py open --slug harvst-bz10-refresh-once-20261013 ...` with legs `PIN`, `LOCK`, `STOP`, `ARM`, `WINDOW`. `WINDOW` closes on the four reads of step 6.
2. `git worktree add --detach "<new>" 3d88eccbc3`, then `git -C "<new>" rev-parse HEAD` (must read 3d88eccbc3), with a positive control on `<old>` (it reads 995adcaeaa). `bz10_pin.out`.
3. **Lock it:** `git worktree lock --reason "AMGT_HARVST live cycle runner pin (HVST-bz-10); govern GC must not remove" "<new>"`. Then `git worktree list --porcelain` must show a `locked` line for EVERY harvest pin: `<new>`, `<old>`, `1c69fa35a3`, `c1be67f53c` and `b5a7a3a4b6`. `bz10_lock.out`.
4. `Stop-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle'` (only after step 2(ii)); census python processes whose command line holds `cycle_runner` or `backfill_driver`: NONE, over ALL processes of ANY exe, with a positive control. `bz10_census.out`.
5. `powershell -NoProfile -ExecutionPolicy Bypass -File "<new>\lib\opal_data_harvest\install-cycle-schedule.ps1" -RepoRoot "<new>" -Publishers bbg,wsj,barrons -StateDir "<state>" -RuntimeRoot "<runtime>" -Windowless -RefreshOnce -Plan` first and read it:
   the `ACTION` interpreter ends `pythonw.exe`, the arguments contain `--refresh-once`, `--state-dir` is `<state>`, `WORKDIR` is `<new>`, and the publishers are `bbg wsj barrons`. `bz10_plan.out`. Then the same command without `-Plan`, once (`bz10_register.out`). **Just before `Start-ScheduledTask`, write the file `deliverables/0.7.0_AE_CloudOps~ZW/round85/bz10_t0.txt` holding ONE line `T0=<the current UTC time, ISO, ending Z>`** (`HVST-bz-11` reads it as the cut), then `Start-ScheduledTask` once, and leave the box.
6. **THE FOUR READS, at start + 3 minutes and again at start + 15 minutes, in `bz10_reads.out`** (each with its control):
   - **R1** `cycle_runner.log`: the last write is under 5 minutes old at +3 and a NEW line exists at +15.
   - **R2** `schtasks /query /xml /tn "Opal Data Harvest - Continuous Cycle"`: the `<Command>` ends `pythonw.exe` and the `<Arguments>` contain `--refresh-once`. Save the XML as `bz10_task.xml`.
   - **R3** no console window: for the runner's PID, `MainWindowHandle` 0 and NO `conhost.exe` child (control: the same read on a console `python.exe` shows a `conhost.exe` child). `bz10_console.out` carries `MainWindowHandle=0` and `CONHOST_CHILD=NONE`.
   - **R4** the real collector spawn works: the new cycle's `.checkpoint.json` `done` length grows by at least 3 between +3 and +15, and `cycle_runner.log` carries no `AttributeError`, `OSError` or `WinError` line since the start.
7. `kill-maint.ps1` as a DRY RUN only (never `-Execute`), default age and the labelled exercise at `-MinAgeSeconds 0`, both printed (`bz10_gc_dryrun.out`); grade it as it reads, as HVST-bz-4 did.
8. **ROLLBACK, signed:** if R1 or R4 reads FALSE at +15, stop the task (`Stop-ScheduledTask`; the loss is at most the one in-flight pair, re-queued from the same state dir), re-run the installer with `-RepoRoot "<old>"` `-Windowless` and WITHOUT `-RefreshOnce`, the same state flags, start once, file one row naming the reading, and say so in
   `bz10_reads.out`. R2 or R3 FALSE with R1 and R4 TRUE is NOT a rollback: file the row and leave it running.
9. **THE ACCOUNT STOP RULE (this order's own):** from the start, read `cycle_runner.log` and the cycle checkpoint at each of your reads for `REFRESH <publisher>: FAILED` or two `REFUSAL` lines for one publisher after its refresh. If a refresh FAILED, or a publisher refuses again after its one refresh, **do not re-register again and do not sign in by hand**:
   file ONE row naming the lines (publisher, class, `http_status`, `host`, `login_redirect`) and keep working. The shared Dow Jones login can lock; a second attempt by any hand is the issuer's call.
Write every file in `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round85/`. Anything odd: one row `AMGT_HARVST-Z-S<next free Z number>`, then keep working.

<paths>
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round85/
org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/
org/missions/D5/AMGT/AMGT_HARVST/surprise-channel/investigations/INVESTIGATION_v1.md
org/critical_paths/.open_deploys/harvst-bz10-refresh-once-20261013.json
org/critical_paths/change_management/
</paths>

## PROOF OF SPEC (each invocation LITERAL, on the site Z box)

<proof_of_spec>
  <criterion id="AC1" cell_refs="HVST-bz-10"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.WorkingDirectory"</invocation><expect>wk-harvest-runner-pin-3d88eccbc3</expect></criterion>
  <criterion id="AC2" cell_refs="HVST-bz-10"><invocation>powershell -NoProfile -Command "(Get-ScheduledTask -TaskName 'Opal Data Harvest - Continuous Cycle').Actions.Arguments"</invocation><expect>--refresh-once</expect></criterion>
  <criterion id="AC3" cell_refs="HVST-bz-10"><invocation>cat org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/round85/bz10_console.out</invocation><expect>(?s)MainWindowHandle=0.*CONHOST_CHILD=NONE</expect></criterion>
</proof_of_spec>

- The checker reads `<expect>` as a regular expression. AC1 and AC2 are site Z reads and cannot run from dell1. At the base AC1 reads `...pin-995adcaeaa` and AC2's arguments carry no `--refresh-once`, so both FAIL as expected, and AC3's file does not exist.
- INSTANCE NAMED EXACTLY `org/missions/D5/AMGT/AMGT_HARVST/deliverables/0.7.0_AE_CloudOps~ZW/AMGT_HARVST.TO-HVST-bz-10.site-z-runner-registered-with-refresh-once.proof_of_spec.json`
  (directly under your serial's folder) with `to_id` `AMGT_HARVST.TO-HVST-bz-10.site-z-runner-registered-with-refresh-once` and `decomp_ref.to_ref` the path of THIS order file.
- **THE CHANNEL FILE HAS MIXED LINE ENDINGS.** Append a row by BYTES and check the diff reads N insertions and 0 deletions.
- Commit and push box/sitez. Do not edit this order file: the issuer flips its status.

## STANDING CONDITIONS (every order to a 0.7.0_AE_CloudOps lane)

1. A send that writes a firm data bucket, or assumes the 49F principal outside the runner's own job, is told to the laptop FIRST.
2. Every send to mdpf-daily-runner is reported after the fact. 3. 49 Financial data never goes into another firm's tree.
This order touches none of them.

<!-- ===================== RECORD FACE -- does NOT travel to the seat ===================== -->

**ISSUER NOTES:**
- Authority: `1.0.0_SA_CTO~DELL1` msg 5209 and `ledger/ROUND_ANALYSIS.round84.md` section 2 item 1; ruling (A) msg 5143. Row `AMGT_HARVST-Z-S119` (BLOCKING, disarm owner this seat).
- **What this act turns on, named for the pair:** the first headful sign-in the RUNNER makes, on the one Dow Jones login that `wsj` and `barrons` share (`dowjones/credentials`; `wsj` and `barrons` are not separate accounts). Budget: at most ONE refresh per publisher per cycle, so at most two sign-ins per full pass of `wsj` then `barrons`;
  a failed refresh is never retried; the flag is a registration argument, reversed by re-registering without it. Who else signs in with that login (a person at Opal, another box) is NOT READ; the pairs say so.
- **The refresh needs the interactive desktop:** the task's principal is `LogonType Interactive` for `Opal Bloomberg`, so a Chrome window opens on that desktop for up to the script's 120 s wait. That is new for the runner (bz-6's mint was run by this seat). The first refresh is therefore also a read of whether it works under the windowless runner (`REFRESH ... done` or `FAILED`).
- **Why the stop is at a cycle boundary by the stop file, not a kill:** as bz-1 and bz-4 (zero pairs lost).
- Pair: COO half `deliverables/2.0.0_SA_COO_W1/round85/NEVER_WIDEN_HALF_COO_BZ10_REFRESH_REPIN.md`; CTO half `ledger/NEVER_WIDEN_ROUND85_BZ10_CTO_HALF.md` (owed). The act does not start without both on file, and the crossbox ORDER is delivered after both.
- The close read is `HVST-bz-11` (read only), cut with this order. It cannot be graded until a publisher cycle ends under the new pin: organic, about a cycle length.
- Delivered as a crossbox ORDER through MSTR (`python .tools/crossbox-call.py open --kind ORDER --to-device sitez`).

<risk>WORLD</risk>
<worker_class>seat</worker_class>
<status>issued</status>
<round>85</round>
<workstream>REFRESH-SITEZ</workstream>
<slot>site-z</slot>
<fabric>dell1</fabric>
