# NFRA_OPLGTW task order -- `OG-eg-2` -- APPLY: the site Z harvest cycle runner runs the silver cache and counts its S3 GETs (PRD v3.10 @c3b76c142b, CTO msg 34372)

<!-- ===================== WORKER FACE -- this is the WHOLE of the applier's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-eg-2</owned_cells>
</decomp_ref>
<to_id>NFRA_OPLGTW.TO-OG-eg-2</to_id>
<issued_to>0.7.0_AE_CloudOps~ZW</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-APPLIER at the act (`comp-schedule --drift`): no hold or moratorium may name the scheduled task "Opal Data Harvest - Continuous Cycle" or its installer; none is known at the cut. The act is the CTO's (msg 34372, PRD v3.10).
comp-iam: DECLARED-NOT-APPLICABLE -- no IAM change; the runner reads and writes the buckets it already does.
comp-adversary: DECLARED-NOT-APPLICABLE -- a cost defect on a producer already running; the change is a code move of three files (merged as OG-eg-1, `7662e9c016`, AC1 5 of 5, AC2 84 of 84) and moves no served output.
EGRESS CLASS, declared: this act REDUCES S3 egress (about $50 of the $68 in DataTransfer-Out for 2026-10-11..14 came from the runner's whole-prefix silver re-reads). No new vendor use.
</preflight>

## 1. THE CELL -- `OG-eg-2` (decomposition addendum R3-T.68, workstream EGRESS-APPLY, FWD-22)

The runner is the scheduled task "Opal Data Harvest - Continuous Cycle" (`pythonw.exe -m lib.opal_data_harvest.cycle_runner --state-dir <S> --runtime-root <R> --stop-file <STOP> --publishers bbg wsj barrons sa --refresh-once`,
working directory a locked pin worktree, today `~\Desktop\wk-harvest-runner-pin-3d88eccbc3`). It runs from that worktree's files; its browser profiles live UNDER that worktree
(`<pin>\.runtime\opal-data-harvest\browser-profiles\<publisher>`), so the pin is moved IN PLACE (the worktree is not replaced, nothing under `.runtime` is copied or touched), and the task's registration does not change.
Fixed value: NEW = commit `7662e9c016` (the OG-eg-1 merge on `box/sitez`; the diff of `lib/opal_data_harvest` and `lib/research/harvest` against `3d88eccbc3` is exactly `cycle_runner.py`, `store.py` and `test_eg1_silver_cache.py`).

1. **Read first, change nothing.** Write `W/EG2_BEFORE.json` = `{"read_at": "<iso>", "state": "<task state>", "arguments": "<the live Exec arguments>", "working_directory": "<path>", "old_state_dir": "<S>", "old_runtime_root": "<R>", "old_stop_file": "<path>", "old_pin_commit": "<git rev-parse HEAD of the working directory>"}`
   from `Export-ScheduledTask` and `git -C <working directory> rev-parse HEAD`. Then print `git -C <working directory> status --porcelain --untracked-files=no` (must be EMPTY: a modified tracked file in the pin is a BLOCKING row and you stop here),
   `git diff --stat 3d88eccbc3 7662e9c016 -- lib/opal_data_harvest lib/research/harvest` (must name exactly the three files above; any other file is a BLOCKING row and you stop here), and
   `git merge-base --is-ancestor 3d88eccbc3 7662e9c016; echo $?` (0).
2. **Plan before the act.** Read `install-cycle-schedule.ps1 -Plan` from the pin with the live `--publishers`, the live state dir and runtime root, `-Windowless -RefreshOnce`, and print its ACTION and WORKDIR lines: they must equal the live registration
   (so the registration needs no change). NEVER run the installer without `-Plan`; this order does not register anything. If the plan differs from the live registration, STOP with a BLOCKING row naming the differing token.
3. Open ledger `nfra-oplgtw-harvest-runner-silver-cache` (entry AND sentinel first; one scheduled task "Opal Data Harvest - Continuous Cycle" is the only family touched). The ledger `nfra-oplgtw-harvest-runner-sa` is a different, still OPEN entry owned by this seat (OG-sa-1): leave it OPEN; step 6 of this order does not close it.
4. **Stop at a cycle boundary.** Write the runner's STOP file (`old_stop_file`) and wait for the runner process to exit by its own boundary (the same stop `HVST-bz-10` and `OG-sa-1` used; zero pairs lost). NEVER kill the process or the task mid-job.
   This wait is qualified on its outcome: the job in flight (`bbg`, started 2026-10-14T22:24Z, about 10 to 12 hours) must end first, so the stop lands between about 08:30Z and 11:00Z on 2026-10-15; act on the runner's exit (`Get-ScheduledTask` State not Running and no `cycle_runner` process for the pin), not on a clock poll.
   If the runner has not exited 14 hours after the STOP file, STOP and file an ARMED row naming this seat; do not kill it. Write the time of exit into `W/EG2_PROOF.json` as `stopped_at`.
5. **Move the pin in place.** Re-run the step-1 tracked-status read (EMPTY), then `git -C <working directory> checkout --detach 7662e9c016`, then print `git -C <working directory> rev-parse HEAD` (must read `7662e9c016`...) and
   `git -C <working directory> show HEAD:lib/research/harvest/store.py | grep -c "def silver_cache"` (1). Delete the STOP file. Confirm the pin is still LOCKED (`git worktree list --porcelain`). Rollback: stop at a boundary the same way and `git -C <working directory> checkout --detach 3d88eccbc3`.
6. **Start and prove.** `Start-ScheduledTask -TaskName "Opal Data Harvest - Continuous Cycle"`; wait for State Running; write `W/EG2_PROOF.json` = `{"old_pin_commit": "<3d88eccbc3 full>", "new_pin_commit": "<full>", "old_state_dir": "<S>", "old_runtime_root": "<R>", "stopped_at": "<iso>", "registered_at": "<iso of the Start>", "restarted": true}`
   (`registered_at` is the Start time; AC2 reads it). Then wait for the FIRST cycle record written after it (any publisher: `<S>\cycles\<publisher>\<cycle_id>.cycle.json` with `ended_at` after `registered_at`); it must carry `s3_get_count` and `s3_get_bytes`.
   This wait is qualified on its outcome: the first record lands when the first publisher job ends (hours), so you read it at that exit and not on a clock poll. Print the record's two numbers and the job's duration in hours beside the baseline (CUR: 4 to 6 GB an hour from this bucket before the change).
   `s3_get_bytes` counts `store.py`'s GETs only (row Z-W98-S1): say that beside the number. If the bytes exceed 10 GB, or the fields are absent, STOP and file an ARMED row naming this seat; do not move the pin again.
6b. **A1 leg -- drop `wsj` and `barrons` from the runner (CTO ruling msg 34491 @86581c31be: Andrew moved WSJ and Barron's to dell1 at about 16:0xZ, @94086281f2; each publisher keeps ONE writer).** On this order's open ledger, add a leg: (i) write the live Exec arguments to `W/EG2_PUB_BEFORE.json` = `{"read_at": "<iso>", "arguments": "<live>"}`; (ii) stop the runner at a cycle boundary by the STOP file, exactly as in step 4 (never a kill); (iii) read `install-cycle-schedule.ps1 -Plan` from the pin with `-Publishers bbg,sa -Windowless -RefreshOnce`, the live state dir and the live runtime root, and print its ACTION and WORKDIR: they must equal the live registration in every token EXCEPT `--publishers`, which must read `bbg sa` (any other difference is a STOP and a BLOCKING row); (iv) re-register with the same installer, `-Publishers bbg,sa -Windowless -RefreshOnce`, nothing else changed; delete the STOP file; wait for State Running; (v) write `W/EG2_PUB_AFTER.json` = `{"read_at": "<iso>", "arguments": "<live>", "publishers": ["bbg", "sa"]}` from `Export-ScheduledTask` and print both argument strings side by side; the next cycle must show `bbg` and `sa` only. Rollback: re-register with `-Publishers bbg,wsj,barrons,sa`. The first-cycle-record leg of step 6 is graded on a `bbg` or `sa` cycle that RAN JOBS (a `bot_check` or `sign_in_refused` stop is not one); `sa` is capturing now. `W/EG2_PROOF.json` gains `publishers_after`: ["bbg", "sa"]. Tell `2.0.0_SA_COO~O` when the read-back is done; the issuer informs `0.0.0_AB_MSTR~Z`, who confirms to dell1's COO.
7. Close the ledger `nfra-oplgtw-harvest-runner-silver-cache` (the sentinel leaves with it), commit, run the criteria, report once with the first record's numbers.

## 2. BOUNDS

- TWO changes of yours: the pin worktree's checked-out commit (`3d88eccbc3` to `7662e9c016`) and the runner's stop and start around it, AND (A1) the `--publishers` argument `bbg wsj barrons sa` -> `bbg sa` by the installer. The state dir, runtime root, STOP-file path, cadence, every browser profile and every other task stay as they are.
- You never kill the runner or its task mid-job, never copy or edit anything under `.runtime`, never run the installer without `-Plan` (and this order registers nothing), never put a cookie or token into a file, row or message.
- Never: push, `git stash`, rebase, `checkout --` or `clean`. The one `git checkout --detach` of step 5 is the act; `git -C <pin> status` is clean before it.
- REFUSE a step you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-oplgtw-harvest-runner-silver-cache.json
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.7.0_AE_CloudOps~ZW/`. Rows: id `NFRA_OPLGTW-Z-S<k>` (the next free), fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ`.

## 4. PROOF OF SPEC (literal; run from the repo root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-eg-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/eg2.AC1.sh; echo "exit=$?"</invocation><expect>(?s)live registration: task Running, workdir .*descends from the eg-1 merge True \(control: an ancestor of the old line is not a descendant True\), store.py holds silver_cache True, pin LOCKED True, publishers .*--refresh-once True, state/runtime roots unchanged True.*sentinel at HEAD 0 \(want 0\).*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-eg-2"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r37/checks/eg2.AC2.sh; echo "exit=$?"</invocation><expect>(?s)after registered_at, [1-9]\d* before without the fields \(negative control, want 1\+\).*first record after registration: .*s3_get_count \d+, s3_get_bytes \d+.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the live task is Running from a LOCKED pin whose HEAD descends from the OG-eg-1 merge and whose `store.py` holds `silver_cache`, with publishers, flag and roots unchanged. `AC2`: the first cycle record after the start counts its GETs and sits at or under 10 GB.

## 5. WHEN YOU ARE DONE

Write the proof instance at `W/NFRA_OPLGTW.TO-OG-eg-2.harvest-runner-silver-cache-apply.proof_of_spec.json`. Validate it after your last commit with
`python .tools/proof-of-spec-check.py <instance> AC1,AC2 --governing-order <this order>`, flip the ONE `<status>` tag to `complete` only if both PASS, and report once to `2.0.0_SA_COO~O` with the first record's numbers.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 37, workstream EGRESS-APPLY (decomposition addendum R3-T.68, cell `OG-eg-2`). PRD v3.10 @c3b76c142b ADMITTED; CTO msg 34372 puts this FIRST after the release in flight. A producer cost defect, not a gateway release: no never-widen halves.
- Seat: `0.7.0_AE_CloudOps~ZW` (owns the runner; its ledger `nfra-oplgtw-harvest-runner-sa` stays OPEN for OG-sa-1 step 5). The GO is the issuer's message citing this order.
- Why an in-place pin move and not a new pin plus re-registration (the R3-T.68 row said "re-registered"): the browser profiles (`sa` alone is 722 MB, with the logins) live under the pin's `.runtime`, so a new pin would need them copied; moving the checked-out commit keeps the registration, the STOP path and every profile as they are, and its rollback is one checkout.
- The timing is the runner's: `bbg` started 2026-10-14T22:24Z (the previous bbg leg ran 12:30Z to 22:13Z), so the boundary is about 08:30Z to 11:00Z. Cost of the wait: about 0.5 USD an hour at the CUR baseline (4 to 6 GB an hour); a mid-job kill is not worth that.
- `sa` (OG-sa-1) runs behind `wsj` and `barrons`, after the restart: its first `sa` cycle will run under the new code, and its step 5 read moves with it.
- Pre-cut: eg2.AC1 and eg2.AC2 base FAIL as expected (EG2_PROOF.json absent). The AC2 parser was dry-run on the live state dir with a synthetic proof: 26 records, 25 before without the fields, the first record after reads `s3_get_count None` and FAILS as it must.

- A1 (issuer, 2026-10-15 ~16:3xZ, CTO ruling msg 34491 @86581c31be): step 6b added: the runner drops `wsj` and `barrons`, so dell1 is their one writer (Andrew moved them ~16:0xZ). The bounds bullet now names two changes. The earlier hold stands for the first-record leg; it is graded on a `bbg` or `sa` cycle that ran jobs. Measured at the cut: cycles `bbg` 20261015T150246Z, `wsj` 20261015T152234Z and `barrons` 20261015T153316Z carry `s3_get_count` and `s3_get_bytes` (0 each: they stopped on `bot_check` and `sign_in_refused` before any silver read, row Z-S150); the `sa` cycle in progress is the first that reads silver per security. Gate limb: GATE (viii) on the modified order (placeholders NONE).

- SUPERSEDED (issuer, 2026-10-15 ~16:5xZ): Andrew moved ALL harvest operations to dell1 (~16:3xZ, relayed by msg 34493); PRD v3.11 @32b70d1b86 and the CTO's msg 34500 retire the site Z runner and close this order's ledger SUPERSEDED (its FIRSTREC leg NOT-EXERCISED) under `NFRA_OPLGTW.TO-OG-eg-3`. Step 6b (the bbg,sa leg) is withdrawn; the E1+E2 code runs on dell1 at pin 39ae28559b and its GET-bytes proof is owed there. Gate limb: GATE (viii) on the modified order (placeholders NONE).

<status>superseded</status>
<round>37</round>
<workstream>EGRESS-APPLY</workstream>
<slot>~AE</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
