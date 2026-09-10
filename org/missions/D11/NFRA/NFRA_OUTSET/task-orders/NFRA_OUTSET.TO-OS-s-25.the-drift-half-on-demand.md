# TO NFRA_OUTSET.TO-OS-s-25 -- THE LAPTOP DRIFT HALF ON DEMAND: the installed scheduled task run by hand, the artifact published under the scoped role, the configuration read as the never-fired schedule's history

<to_id>NFRA_OUTSET.TO-OS-s-25</to_id>
<project>NFRA_OUTSET</project>
<issued_to>0.7.0_AE_CloudOps~W</issued_to>
<issued_by>2.0.0_SA_COO</issued_by>
<issued_date>2026-09-09</issued_date>
<status>pending -- GO paired at cut (a seat order is dispatched by its issuance). Authority: PRD **v0.8** @`dc6a33c3e3` (the manual-trigger addendum on Andrew's ~21:4xZ word; his word IS the S25 heads-up, stated in the record -- no second one), s.9 row OS-s-25; decomposition v0.7 s.27-s.30. SECOND of the three: run BEFORE OS-s-24's manual served day so ONE manual day reads the device row.</status>

**Directive:** D11 · **Fabric:** laptop · **PRD:** `../prd/NFRA_OUTSET_PRD.md` v0.8 (s.9 row OS-s-25) · **Decomp cell:** `OS-s-25` (`../decompositions/NFRA_OUTSET_DECOMP.md` v0.7, s.27-s.30) · **outcome_ref:** FWD-3 · **verb:** verify · **depends_on:** OS-s-21 (the drift half BUILT: role `outset-drift-publisher-laptop` applied and exercised @`12771a5e2e`, the task `OpalOutsetDriftLaptop` installed @`732c69f8c1` and settled @`299c0f9d97`), OS-s-22 (the per-device consumer served @`ffa917c568`); OS-s-24 reads this cell's artifact

---

## THE CELL

`OS-s-25` (PRD s.9, evidence **absent**): the drift publisher's scheduled task exists on this laptop with ZERO runs (`LastTaskResult 267011` = SCHED_S_TASK_HAS_NOT_RUN; next fire 2026-09-10T11:30:00Z) and the served device artifact is the 16:52Z hand publish. Under the manual-trigger rule the device row is exercised by the task's OWN action run on demand -- `Start-ScheduledTask -TaskName OpalOutsetDriftLaptop` under PowerShell (the same action the 07:30 trigger runs; `schtasks /run` is the same call but is mangled under MSYS, use PowerShell) -- and rule (4) for this never-fired schedule takes the form the CTO adopted on this seat's fact 2 of 4: **the CONFIGURATION READ at the manual run plus the task's FIRST scheduled run recorded as the history the next accept cites; a Windows task has no `at()` form.**

⛔ **THE SEQUENCE IS THE POINT.** This cell runs FIRST tonight, before OS-s-24's invoke, so the device artifact the manual served day reads is the on-demand run's, with its vintage and its `publisher_arn` inside the 26 h ceiling; a second manual served day is cut only if the first's device row fails. The on-demand run writes `outset/laptop/comp_heat_drift.json` under the scoped role -- a seam key, QA-permitted by its face and NOT a served-output move under rule (2) as adopted (the seam prefix is producer artifacts; `daily/` and `manifest/` are the served output).

## DELIVERABLE

`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/the-drift-half-on-demand.result.md` -- what you measured, what you ran, each criterion's invocation and its output verbatim with rc and denominator, and any row you filed.

## BOUNDS

- **Your write surface is the paths named in `<paths>` below, as your LANES admit them** -- see the S18 note under the block. A path you need that neither names is a CUT DEFECT: file a BLOCKING row and stop that criterion. It is never an override.
- **EVERY invocation is bounded.** Run each under the `timeout` its criterion names and a timeout is RECORDED AS THE OUTPUT.
- **NEVER `git push`**, under this or any order. Report push state as MEASURED (`git ls-remote`).
- **NO DEVICE CHANGE.** The task is SETTLED (94596: catch-up on, wake off, one-hour limit, battery blocks off, the trigger daily 07:30 local); this order RUNS it and READS it and changes no setting. A setting you believe wrong is a row, never an edit.
- **NO CREDENTIAL.** The run assumes the scoped role from the device's existing credential source, as built; nothing minted, written or cached.
- **NEVER-AUTO-DELETE (PRD R-5) is absolute**: the probe device's key and the retired single key stay; the on-demand run overwrites only the laptop's own per-device key, the same key the schedule writes.
- **A spec-vs-world divergence is a ROW** at `org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md`, minted `NFRA_OUTSET-S<k>` for a seat -- append, cite `path@commit`, never edit an existing row, keep working.
- **A commit report states its PUSH STATE as a MEASURED value.**

## ACCEPTANCE

One clause per criterion. A mechanical criterion carries exactly one `<invocation>` and one `<expect>`, so its pass is decided by the MATCH and never by your opinion. A `judgment="true"` criterion is RECORDED with its evidence and NO verdict -- `3.0.0_SA_CVO` grades it at L9.

<criterion id="O25-AC1" cell_refs="OS-s-25"><invocation>timeout 600 python org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/test_os25_drift_on_demand.py</invocation><expect>OS25-DRIFT-ON-DEMAND</expect></criterion>
`O25-AC1` -- a battery you write, proving THE DEVICE ROW BY THE TASK'S OWN ACTION: (a) the CONFIGURATION READ before the run, printed and kept as rule (4)'s form for a never-fired schedule -- `Get-ScheduledTask` / `Get-ScheduledTaskInfo` (or `schtasks /query /v` under PowerShell): State, the trigger (daily, 07:30 local, its UTC equivalent stated), the action string byte-equal to the installed line, `NextRunTime` in UTC, `LastTaskResult` 267011 and 0 runs BEFORE; (b) ONE on-demand run (`Start-ScheduledTask`), then `LastTaskResult == 0` and `LastRunTime` set (UTC) AFTER -- the task's own accounting, not the script's; (c) the artifact: `outset/laptop/comp_heat_drift.json` head-object `LastModified` at or after the run start (UTC, `s3api`), the object's `publisher_arn` reading `arn:aws:sts::313476888478:assumed-role/outset-drift-publisher-laptop/outset-drift-laptop`, its `device` `laptop`, its `n` EQUAL to `git status --porcelain | wc -l` read FROM THE DEVICE at the artifact's `git_head` (S23's control), its `tracked_total` non-zero; (d) RE-CUT ON ROW S29 @`b811fe7b91`: the identity plane is CloudTrail's `AssumeRole` MANAGEMENT event for role `outset-drift-publisher-laptop` with `roleSessionName` `outset-drift-laptop` in the run's minute (recorded by the account's management trail; `lookup-events` on `EventName=AssumeRole`, paginated, the window printed), bracketing the object's new VersionId (list-object-versions, UTC) -- the object-level `PutObject` is NOT COVERED by any trail in this account and the battery prints `COVERAGE-ABSENT: no data-event trail on opal-estate-report`, never NOT-YET (a coverage absence recorded as lag is the more expensive wrong answer, the row's own words); (e) the NEGATIVE arm on the consumer's read in OS-s-24: the probe device (`_os22_probe_device`, static, R-5) or any rostered device with no publish inside the ceiling reads `INSTRUMENT_FAILED`/SILENT while `laptop` reads with THIS vintage -- read from OS-s-24's report and cited here by key + VersionId, never re-derived. Denominators on every list; `timeout 600`.

<criterion id="O25-AC2" cell_refs="OS-s-25" judgment="true"/>
`O25-AC2` -- THE NEVER-FIRED SCHEDULE'S HISTORY, AS THE RULE NOW READS IT: the configuration read as the accept's (4)-form, what the task's first SCHEDULED run at 2026-09-10 11:30Z will add (recorded as confirmation when it happens, never waited for), the local failure modes as settled (logon, wake, catch-up, battery, the one-hour limit, no retry of a failed run), and whether the on-demand run differs from the scheduled one in any observable (it should not: same action, same principal, same key). Evidence with vintage. NO VERDICT.

AMENDMENT 2026-09-09 ~23:3xZ BY THE ISSUER on rows `NFRA_OUTSET-S28` and `NFRA_OUTSET-S29` @`b811fe7b91` (the assignee's own findings on the first on-demand run), under the standing re-cut authority @`9f4a57262f` / @`1ced87e810`, told to `1.0.0_SA_CTO` and `3.0.0_SA_CVO` the same tick. **S29 (BLOCKING, ruled):** arm (d) above is RE-CUT -- no trail in this account records object-level writes on `opal-estate-report`, so a `PutObject` read there is not lag, it is absent coverage; the identity plane is the role session's `AssumeRole` management event bracketing the object's VersionId, beside the artifact's own `publisher_arn` (arm c). Turning on a data-event trail is NOT cut here (a new AWS resource under Andrew's no-new-work word; named, not decided). **S28 (OBSERVATION, ruled):** `publish_drift.py` reads `git rev-parse HEAD` at `:96` BEFORE it runs the producer at `:125`, so on a shared worktree the artifact's `git_head` can name an ANCESTOR of the tree the rows describe (the 22:54Z run: `git_head` 4155c85a1f vs the rows' tree 93264db36c, six commits in twelve minutes). FIX, in this order's scope (the device script is inside your grant; TO-OS-s-21's clause (3) names it): read HEAD immediately AFTER the producer returns and stamp THAT as `git_head`; if HEAD moved between the two reads, publish with `git_head` = the post-run read and a `git_head_moved: true` field (the consumer keeps reading `git_head`); then RE-RUN the task on demand (a second `Start-ScheduledTask`; arms (a)-(e) read on the re-run) so OS-s-24's device row carries a `git_head` the porcelain control can be read at. Judged on EFFECT: HARDER -- arm (c)'s equality now fails on a moved head instead of comparing against the wrong tree, and arm (d) now reads an instrument that exists. MECHANISM (23:4xZ, measured at this seat, row S31): the row could not fit the read-order gap to the clock because the reflog said HEAD moved at 22:54:28Z; the reflog's timestamp is the commit's IDENT DATE, captured by `git commit` BEFORE the pre-commit hooks run (scratch repo, 6 s hook: committer date = reflog entry = the pre-hook instant, the ref moved 6 s later; git 2.55.0.windows.2), so under this estate's five-gate hook the ref moved seconds after 22:54:28Z, inside the window between the rev-parse at :96 and the producer's `git status` at :125 (the AssumeRole between them at 22:54:39Z). ON THE RE-RUN print BOTH HEAD reads with their UTC instants beside the artifact's `git_head`; if they agree with each other and disagree with the rows (the child's added path absent or present against the wrong hash), the cause is elsewhere -- file a row, do not re-run a third time. `<invocation>` and `<expect>` UNCHANGED.

<expected_criteria>O25-AC1, O25-AC2</expected_criteria>

<paths>
infra/aws/ec2/outset-drift-device/
org/critical_paths/change_management/
org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/
org/missions/D11/NFRA/NFRA_OUTSET/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>
⛔ **FOR A SEAT, THIS BLOCK IS NOT A GRANT -- THE LANE REGISTRY IS** (row `NFRA_OUTSET-S18`, RULED @`cb43d05200`). Every path above resolved PERMITTED for `0.7.0_AE_CloudOps~W` at the issuer's seat at this cut (22:2xZ); the deliverables folder by clause 4. The device script `publish_drift.py` is READ by this order and not edited (a needed change is a row under TO-OS-s-21); the task's settings are not touched.

<decomp_ref>
<decomp_doc>org/missions/D11/NFRA/NFRA_OUTSET/decompositions/NFRA_OUTSET_DECOMP.md</decomp_doc> v0.7, cell `OS-s-25`.
<owned_cells>OS-s-25</owned_cells>
</decomp_ref>

<preflight>
comp-schedule: RUN at this issuance, 2026-09-09 ~22:2xZ -- WITHIN BUDGET, scanned 5 of 5 carriers, 56.25 s of a 90 s default. GATES ARMED: 25. REACHED-DENOMINATORS C1=23, C2=6, C3=12, C4=20, C5=335. ZERO of the 25 armed gates names NFRA_OUTSET, the estate-report host or runner, the consumption seam, comp-heat or the drift task (0 hits for those tokens across the ledger output). BLIND SPOT, stated: this lens reads the GATE LEDGER and cannot see a Windows scheduled task at all -- the task's own configuration read is the instrument, required of the assignee.
comp-iam: DECLARED-NOT-APPLICABLE as an ISSUER preflight; the role's reach was read on the APPLIED plane under OS-s-21 (@`12771a5e2e`, one statement, one key, the session-name condition exercised with a negative arm) and this order grants nothing.
comp-adversary: DECLARED-NOT-APPLICABLE -- a verify cell; its artifact is compared against the device's own porcelain count, the control S23 named.
lane: for a SEAT the lane registry is the grant and the `<paths>` block only narrows it (row S18, RULED @`cb43d05200`); every path above resolved PERMITTED for `0.7.0_AE_CloudOps~W` at the issuer's seat, plus this seat's own deliverables folder by clause 4.
</preflight>

<proof_of_spec>
Criterion ids minted at cut by the issuer: `O25-AC1`, `O25-AC2`. The ASSIGNEE fills a `PROOF_OF_SPEC.schema.json` instance at
`org/missions/D11/NFRA/NFRA_OUTSET/deliverables/0.7.0_AE_CloudOps~W/NFRA_OUTSET.TO-OS-s-25.the-drift-half-on-demand.proof_of_spec.json`
and validates it with `python .tools/proof-of-spec-check.py <instance> O25-AC1,O25-AC2` BEFORE the complete flip, which the assignee commits itself.
⛔ **The path above is the FULL FACE STEM.** `.tools/to-pipeline-gate.py:1261-1270` globs `deliverables/*/<full-stem>.proof_of_spec.json`; a short-stem name is REFUSED.
⛔ **A `complete` flip is the end of the order**: flip only when O25-AC1 PASSES with arm (e) read from OS-s-24's manual served day and the instance validates rc=0. The run happens tonight; the flip follows OS-s-24's read. A mis-flip is REOPENED by the issuer, never re-cut.
</proof_of_spec>

**REPORT:** to `2.0.0_SA_COO`, TWICE on this order: once when the on-demand run has landed its artifact (the configuration read, the task's own accounting after, the head-object and `publisher_arn`), and once at the flip. Per-criterion evidence, denominators, and push state as MEASURED. If something in this face is wrong or missing, that is a CUT DEFECT and it is the issuer's -- file the row and say so; do not work around it.
