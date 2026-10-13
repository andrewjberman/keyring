# TO IRPT_BCKEND.TO-IB-pr-497 -- ONE read-only count of leftover Tax-snapshot temp files on the host that runs the 49F builder (row D2-W345-S3, the host read)

<to_id>IRPT_BCKEND.TO-IB-pr-497</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-13</issued_date>
<status>parked</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>171</round>
<workstream>~P</workstream>

**PARKED (issuer, 2026-10-13T04:0xZ; IB2's STOP at step 3 was right, row IRPT_BCKEND-D2-S124):** the one runner host is stopped and absent from SSM, so the count was NOT ESTABLISHED. No start or stop of the host is granted (a stop is a human-confirm act; the start belongs to the daily runner's own schedule). The order is reissued, same read, for a window when the runner is up; owner 2.0.0_SA_COO~P2; the function whose variable names the runner is irpt-holdings-refresh-lambda (IRPT_HOLDINGS_RUNNER_INSTANCE_ID), not irpt-holdings.

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO ROUND-171 ANALYSIS (msg 6764) section 1, row D2-W345-S3: "One read of the host's temp space for files left by past builds, counts only, no contents; any found are listed for a human delete (a delete of client-bearing files is a person's act)" | **Decomp cell:** `IB-pr-497` (decomposition section 163) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-497` (inlined):** `holdings_snapshot.retained_capture` writes the Tax membership snapshot, which carries client account numbers, to a temp file ending `-taxsma_workbook_projected_snapshot.json` (`tempfile.mkstemp(suffix="-" + obj)`) on whatever host runs `holdings_49f.build_49f_meshed`, and never removes it. Nobody has measured whether any such file exists on that host. **One read, counts and ages only, no contents, no deletion.**

**Steps:**
1. Find the host(s) that run the 49 Financial holdings builder: read the runner instance id(s) from the configuration of the Lambda(s) that hand the build to a runner by SSM (`aws lambda get-function-configuration` on `irpt-holdings` and `irpt-directory-refresh`: environment variable NAMES that end in `RUNNER_INSTANCE_ID`; the instance ids are not client data). If no function names a runner for the holdings build, STOP and file a row saying so: do not guess a host.
2. For each such host, ONE read through SSM Run Command (`AWS-RunShellScript`) of ONE read-only command that prints ONLY the modification time (seconds since epoch) of each file, one per line, no names:
   `find /tmp /var/tmp "${TMPDIR:-/tmp}" -maxdepth 1 -type f -name '*-taxsma_workbook_projected_snapshot.json' -printf '%T@\n' 2>/dev/null; echo END`
   (`-printf` on the modification time only; no `-exec`, no `-delete`, no cat.) Poll the command to a terminal state; read its stdout; from it compute `files_matching` and the ages in whole days relative to now (`oldest_age_days`, `newest_age_days`; null when none).
3. If SSM Run Command is not permitted to your user, or the host is not Online in SSM, or the command ends in any state but Success: STOP, file a row with the error code (never a key or a path), write no record.
4. Write `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB171-2_host_tmp_read.json`: `{hosts_read: <int>, per_host: [{host_class: "runner", files_matching: <int>, oldest_age_days: <int|null>, newest_age_days: <int|null>}], contents_read: 0, files_deleted: 0, command_run: "<the exact command string you ran>", read_at_utc: "<date -u +%FT%TZ>", not_established: ["..."]}`. NO instance id, path, file name, account number or timestamp list in the record: counts and ages only.
5. If `files_matching` is above 0 on any host, say so in your report (a human deletes them; you delete NOTHING) and file ONE row, class BLOCKING, hazard standing ARMED, `disarm_owner` `2.0.0_SA_COO~P2`, counts only.

**Criteria (run each under `timeout 120` from the repo root, record the output and exit code verbatim):**

<criterion id="IB171-2-AC1" cell_refs="IB-pr-497"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-2-AC1</invocation><expect>IB171-2-AC1 PASS</expect></criterion>
<criterion id="IB171-2-AC2" cell_refs="IB-pr-497"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-2-AC2</invocation><expect>IB171-2-AC2 PASS</expect></criterion>
<criterion id="IB171-2-AC3" cell_refs="IB-pr-497"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r171/p171_cells.py" . IB171-2-AC3</invocation><expect>IB171-2-AC3 PASS</expect></criterion>

<expected_criteria>IB171-2-AC1, IB171-2-AC2, IB171-2-AC3</expected_criteria>

What the checks grade: AC1 the record's shape and arithmetic (one row per host; ages null when nothing matched; `contents_read` 0, `files_deleted` 0); AC2 the record carries no path, no temp file name, no instance id and no long digit run; AC3 the recorded command is a read-only `find`/`ls` (no rm, cat, tee, redirect, shred, mv, cp, `-exec`, `-delete`).

## BOUNDS

- **Grant:** the `paths` block and nothing else. READ-ONLY on the host: one `find` per host, nothing written, nothing deleted, no file opened. No other SSM command, no change to any role, document or instance. No client name or account number in any file or message.
- **Refusal clause:** STOP and file a row on any of: no function names a runner; SSM not permitted; the host not Online; a command state other than Success; any need to read a file's contents. Never improvise a second command.
- **Row ids** are `IRPT_BCKEND-D2-S<n>` (the next free number: check the id is free just before you commit); `surfaced_at` is `date -u +%FT%TZ` at filing.
- **Commit with** your own author line via `bash .tools/safe-commit.sh -F <msgfile>` (message file via the Write tool, outside the worktree; do NOT pre-`git add`); ASCII only. Report to `2.0.0_SA_COO~P2` in one message under 150 words: the counts and ages only and each criterion's last line.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-497.host-temp-space-read-counts-only.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 163 (round 171, workstream ~P), cell `IB-pr-497`.
<owned_cells>IB-pr-497</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB171-2-AC1, IB171-2-AC2, IB171-2-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-497.host-temp-space-read-counts-only.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- one SSM Run Command per runner host executing a read-only `find` that prints modification times (no names, no contents); no resource is created or changed. Class SERVED because the files, if any, hold client account numbers (never read). The CTO's ruling @3554eeb652 names this read; a delete of any file found is a person's act (Andrew's word if recursive), not this order's.
comp-iam: DECLARED-NOT-APPLICABLE -- no permission change; an SSM denial is a STOP, never a request for a grant.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p171_cells.py dry-run at base on dell2 2026-10-13 ~04:0xZ: IB171-2 AC1, AC2 and AC3 FAIL (no record). Not run: whether the executor's AWS user may send an SSM command (unmeasured; the order makes a denial a STOP).
lane: the paths block IS the grant; applied by 0.7.0_AE_CloudOps~IB2, IRPT_BCKEND only. Class SERVED.
</preflight>
