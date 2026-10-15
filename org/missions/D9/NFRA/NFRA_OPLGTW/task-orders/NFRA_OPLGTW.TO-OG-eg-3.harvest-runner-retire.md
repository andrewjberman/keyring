# NFRA_OPLGTW task order -- `OG-eg-3` -- APPLY: the site Z harvest runner RETIRES (STOP, then Disable), and the two open runner ledgers close SUPERSEDED (PRD v3.11, CTO msg 34500)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-eg-3</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-eg-3</to_id>
<issued_to>0.7.0_AE_CloudOps~Z</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-APPLIER at the act (`comp-schedule --drift`): the act DISABLES the scheduled task "Opal Data Harvest - Continuous Cycle" (the CTO's PRD v3.11 ruling, on Andrew's word that all harvest operations move to dell1). No hold or moratorium names it; none is known at the cut.
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change.
comp-adversary: DECLARED-NOT-APPLICABLE -- the act is Andrew's word (~16:3xZ, relayed verbatim by 2.0.0_SA_COO~O msg 34493) as ruled by 1.0.0_SA_CTO~Z (PRD v3.11 @32b70d1b86, msg 34500) and accepted by 1.0.0_SA_CTO~DELL1 (relay 34508).
EGRESS CLASS, declared: this act STOPS a producer that reads and writes S3; it adds no egress.
</preflight>

## 1. THE CELL -- `OG-eg-3` (decomposition addendum R3-T.71, workstream HARVEST-RETIRE, FWD-22)

Andrew moved ALL harvest operations to dell1 (bbg, sa, wsj, barrons; FT to follow). Site Z's runner has stored `new 0` for every publisher since the 14:02Z Python outage, so retiring it opens no capture gap that is not already there. Dell1 runs the same E1+E2 code at pin `39ae28559b`.

1. **Read, change nothing.** Write `W/EG3_BEFORE.json` = `{"read_at": "<iso>", "state": "<task state>", "arguments": "<live Exec arguments>", "working_directory": "<path>", "stop_file": "<the --stop-file path from the arguments>", "runner_processes": N}` from `Export-ScheduledTask` and a census of `cycle_runner` processes (a PowerShell `Get-CimInstance Win32_Process` filtered on the command line; print the denominator).
2. Open ledger `nfra-oplgtw-harvest-runner-retire` (entry AND sentinel first), legs: `stop`, `disable`, `pins-locked`, `ledgers-superseded`.
3. **STOP at a job boundary.** Write the runner's STOP file (`stop_file`); wait until no `cycle_runner` process remains. NEVER kill the process or the task. This wait is qualified on its outcome: the runner ends at its next job boundary (minutes); act on its exit and not on a clock poll. If it has not exited 2 hours after the STOP file, STOP and file an ARMED row naming this seat; do not kill it.
4. **Disable, unregister nothing.** `Disable-ScheduledTask -TaskName "Opal Data Harvest - Continuous Cycle"`, then read the state back as Disabled (`Get-ScheduledTask`), and census again: no `cycle_runner` process. Leave the STOP file IN PLACE. Rollback (one act, in this order): delete the STOP file, `Enable-ScheduledTask`, `Start-ScheduledTask`.
5. **The pin worktrees stay LOCKED** (`wk-harvest-runner-pin-3d88eccbc3`, `-995adcaeaa`, `-1c69fa35a3`, `-c1be67f53c`, `-b5a7a3a4b6`): read `git worktree list --porcelain`, print each pin with its `locked` line (a positional cut of that census misses the last one: read the whole list). They are the rollback source until dell1 reports a productive cycle per publisher; unlocking them is `0.0.0_AB_MSTR~Z`'s act afterwards, not yours.
6. **Close the two open runner ledgers SUPERSEDED** (the CTO's ruling, PRD v3.11): `nfra-oplgtw-harvest-runner-silver-cache` (OG-eg-2: its FIRSTREC leg recorded NOT-EXERCISED because no site Z cycle ran jobs after the start; leg 6b withdrawn; the E1/E2 GET-bytes proof is owed on dell1) and `nfra-oplgtw-harvest-runner-sa` (OG-sa-1: its WINDOW leg recorded NOT-EXERCISED). Say in each close line that it is closed SUPERSEDED by this order. Then close your own ledger `nfra-oplgtw-harvest-runner-retire`.
7. Write `W/EG3_PROOF.json` = `{"stopped_at": "<iso of the last runner exit>", "disabled_at": "<iso>", "state": "Disabled", "runner_processes": 0, "pins_locked": 5, "firstrec_not_exercised": true, "window_not_exercised": true}`, commit, run the criteria, and report once. The read-back (stopped, Disabled) is what `0.0.0_AB_MSTR~Z` carries to dell1's COO.

## 2. BOUNDS

- Your changes: the STOP file, the task's Enabled state (to Disabled), and the ledgers. The task registration, its arguments, the state dir, the runtime root, every browser profile, every pin worktree and every other task stay as they are. No object is written to or deleted from any bucket.
- Never: unregister the task, kill a process, delete a pin worktree or unlock one, push, `git stash`, rebase, `checkout --` or `clean`; put a cookie or token into a file, row or message.
- REFUSE a step you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-harvest-runner-retire.json
org/critical_paths/.open_deploys/nfra-oplgtw-harvest-runner-silver-cache.json
org/critical_paths/.open_deploys/nfra-oplgtw-harvest-runner-sa.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~Z/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free; a correction is a NEW row citing the old id, never an edit), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-eg-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/eg3.AC1.sh; echo "exit=$?"</invocation><expect>(?s)task state Disabled; cycle_runner processes 0; STOP file present yes; pins locked 5 of 5.*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-eg-3"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/eg3.AC2.sh; echo "exit=$?"</invocation><expect>(?s)ledgers closed 3 of 3; sentinels at HEAD 0; superseded closes 2 of 2; proof legs not-exercised yes.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the live task is Disabled, no `cycle_runner` process runs, the STOP file is in place and the five pin worktrees are still locked. `AC2`: the three ledgers are closed with their sentinels gone, the two earlier ledgers read SUPERSEDED, and the proof records FIRSTREC and WINDOW as NOT-EXERCISED.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-eg-3.harvest-runner-retire.proof_of_spec.json`. Validate it after your last commit with `python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once to `2.0.0_SA_COO~O` with the read-back (stopped, Disabled).

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream HARVEST-RETIRE (decomposition addendum R3-T.71). PRD v3.11 @32b70d1b86 ADMITTED; CTO msg 34500; dell1's CTO accepted all four publishers (relay 34508, ADDENDUM_4_Z_RETIRES_ALL @e6eb813524). Not a gateway release: no never-widen halves.
- Seat: `0.7.0_AE_CloudOps~ZW` (owns the runner). The GO is the issuer's message citing this order. `OG-eg-2` and `OG-sa-1` become `superseded` in the same commit as this order (their ledgers close SUPERSEDED here).
- Pre-cut: eg3.AC1 and eg3.AC2 base FAIL as expected (the task is Running, the ledgers are open, the proof is absent).

- A1 (issuer, 2026-10-15 ~17:4xZ): the order is REASSIGNED from `0.7.0_AE_CloudOps~ZW` to `0.7.0_AE_CloudOps~Z`. ~ZW stopped at a weekly usage-limit dialog (resets Oct 18, 9am ET; screen read 17:39Z, 8 unread files, no inbox watcher) and has not read the GO of 16:56Z; `0.0.0_AB_MSTR~Z` declined to seat another instance (msg 34523: the same model policy meets the same limit) and left the reassignment to the issuer. Everything else stands: the CTO's ruling (PRD v3.11, msg 34500), the steps, the bounds and the criteria. `W` is now `~Z`'s deliverables folder, so `EG3_BEFORE.json` and `EG3_PROOF.json` are written there (eg3.AC1 and AC2 read it). The two older runner ledgers `nfra-oplgtw-harvest-runner-silver-cache` and `nfra-oplgtw-harvest-runner-sa` were OPENED by `~ZW` and are closed SUPERSEDED here by `~Z` from the measured state (the CTO's ruling names that close); say so in each close line. The surface paths are unchanged. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>pending</status>
<round>37</round>
<workstream>HARVEST-RETIRE</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
