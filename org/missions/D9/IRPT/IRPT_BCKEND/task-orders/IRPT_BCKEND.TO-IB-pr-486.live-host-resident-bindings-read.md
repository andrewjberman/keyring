# TO IRPT_BCKEND.TO-IB-pr-486 -- READ ONLY: does the installed `resident_bindings.json` on the live YCharts host carry `commentary_ready_queue_url`

<to_id>IRPT_BCKEND.TO-IB-pr-486</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-12</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>167</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** `1.0.0_SA_CTO~DELL2` msg 6517 (PRD ADDENDUM v0.51 section 2 item 4; ROUND-166 ANALYSIS section 3a: "ONE read first ... whether the installed `resident_bindings.json` on the live host carries `commentary_ready_queue_url` today") | **Decomp cell:** `IB-pr-486` (decomposition section 159) | **outcome_ref:** FWD-8

---

## WORKER FACE

**Why.** The resident runtime (`infra/aws/lambda/investor-reporting/reports/resident_installed.py`) treats `commentary_ready_queue_url` as an OPTIONAL binding (about line 50), and `build_resident_runtime` (about lines 345-346) imports `opal_packager` (`ycharts/research/opal_packager.py`) when the bindings carry it. The resident PACKAGE does not stage `ycharts/research` today
(`reports/build_resident_package.py` `DIRS`; a separate order in this round adds it). If the installed bindings on the live host ALREADY carry the queue URL, the live resident cannot have imported the packager; if they do not, nothing is broken live and the fix rides the next resident release. You answer which, by reading the file on the host.

**HARD BOUNDS -- this cell reads and does nothing else.**
- NO sign-in is attempted, by you or caused by you. You do not run `run-ycharts-session.sh` or `ycharts_session.js`, do not submit a request, do not send, receive or delete a queue message, do not start, stop or restart any unit, do not touch the browser profile.
- NO secret VALUE is read: never `get-secret-value`.
- NO write on the host: no redirection to a host path, no temp file, no `tee`, no `cp`, `mv`, `rm` or `sed -i`. Each command is one pass that prints to stdout, as the earlier host reads did (`deliverables/0.7.0_AE_CloudOps~IB2/IB129-1_capture_failure_read.json` is the model; its host commands are listed verbatim there).
- NO vendor call. NO queue URL is printed or recorded: it carries the account id. The file is read ON the host by a command that prints only whether the key is present and non-empty, and (if present) the queue NAME, which is the last path segment of the URL and nothing before it.

**Read (the host is instance `i-0167fd745ad906a66`; the resident unit is `irpt-analysis-resident.service`; its root at the last read was `/opt/irpt-resident/<pin>-st<n>` -- confirm each from the unit before relying on it):**
1. **Where the bindings file is.** Read the repo first: `reports/resident_installed.py` (how `bindings_path` is resolved, the file name and the optional keys), `reports/build_resident_package.py` (what it writes as `resident_bindings.json`) and `infra/aws/ec2/investor-reporting-ycharts/README.md`. Establish the installed path on the host from the unit's `WorkingDirectory` or `Environment` (read with `systemctl show -p WorkingDirectory -p Environment irpt-analysis-resident.service`, which reads the unit and starts nothing). Print only variable NAMES from the environment, never values.
2. **The key.** With ONE read-only SSM command (`AWS-RunShellScript` through `.tools/aws`; each script is one you would be content to see run twice), print: whether the file exists (`test -f`), its modification time (`stat -c %y`), and whether `commentary_ready_queue_url` is present and non-empty (a one-line `python3 -c` that prints `BOUND` or `UNBOUND`, plus the queue name only when bound). Read the command's result with `get-command-invocation`; a CommandId alone proves only that SSM accepted it.
3. **The state of the unit** (a read): `systemctl is-active irpt-analysis-resident.service`, and the installed package's root directory name (the pin), by `ls` of the parent directory.
4. **What follows.** If BOUND: the live resident cannot have imported `opal_packager` from a package that lacks `ycharts/research`; look in the unit's recent journal (`journalctl -u irpt-analysis-resident.service --since '<24 hours ago, in the host time zone you state>' | grep -c ImportError`, a count only) for the import failure and report the count and the first and last time; FILE A ROW with that state (class OBSERVATION; hazard ARMED if the count is above zero, with `disarm_owner` `2.0.0_SA_COO~P2`). If UNBOUND: say so; nothing is broken live.

**Record** `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IB167-6_host_bindings_read.json`:
`{instance, unit, root, bindings_path, read_at_utc, commentary_ready_queue_url_bound: true|false|"NOT_ESTABLISHED", queue_name_when_bound: <name>|null, bindings_file_mtime, unit_active, import_error_count_24h: <int>|null, claim: "measured"|"inferred"|"held"|"absent" (measured when you read the file), in_words, host_commands:[{ssm_command_id, status, script}], sign_in_attempted:false, secret_values_read:0, host_writes:0, output_files:[...], not_established:[...]}`.
Every host command's script is recorded verbatim, and its status is read with `get-command-invocation`.

<criterion id="IB167-6-AC1" cell_refs="IB-pr-486"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-6-AC1</invocation><expect>IB167-6-AC1 PASS</expect></criterion>
<criterion id="IB167-6-AC2" cell_refs="IB-pr-486"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-6-AC2</invocation><expect>IB167-6-AC2 PASS</expect></criterion>
<criterion id="IB167-6-AC3" cell_refs="IB-pr-486"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r167/p167_cells.py" . IB167-6-AC3</invocation><expect>IB167-6-AC3 PASS</expect></criterion>

<expected_criteria>IB167-6-AC1, IB167-6-AC2, IB167-6-AC3</expected_criteria>

The checks grade shape and bounds only: AC1 the bound flag is true, false or NOT_ESTABLISHED with a claim (measured when the file was read), the instance, path and read time are stated, and no queue URL appears in the record; AC2 every host command is listed verbatim with an SSM command id and a terminal status, none matching a forbidden pattern (a unit start/stop/restart, the session runner, a secret read, a queue send/receive/delete, `curl`, `wget`, `kill`, `rm`, `mv`, `cp`, `sed -i`, `tee`, a redirection to a host path, a DynamoDB write);
AC3 `sign_in_attempted` false, `secret_values_read` 0, `host_writes` 0 and `not_established` a list. Whether the key is bound is UNMEASURED by the issuer.

## BOUNDS

- **Refusal clause:** if answering needs anything the HARD BOUNDS forbid (a secret value, a unit restart, a session run, a write on the host, printing the queue URL), STOP at that point, record what was read so far, file a row and report. If a criterion cannot be met as written, file a row and report; never weaken a check; do not edit `p167_cells.py`.
- AWS through `.tools/aws`. SSM `send-command` with `AWS-RunShellScript` is the read path.
- **Row ids** are `IRPT_BCKEND-D2-IB2-S<k>`; check the id is free just before you commit; `surfaced_at` is `date -u +%FT%TZ` at filing.
- Commit with `.tools/safe-commit.sh --author "0.7.0_AE_CloudOps~IB2 <0.7.0_AE_CloudOps~IB2@opal.agent>" -F <msgfile> -- <paths>`; the message file by a non-shell writer; no pre-`git add`; ASCII only. No deploy is made, so no change-management entry is opened.
- **Report** to `2.0.0_SA_COO~P2` in one message under 150 words: the record's path, bound or unbound with its claim, the import-error count if bound, each criterion's last line. Flip `<status>` to complete only when all three PASS and the proof is VALID.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-pr-486.live-host-resident-bindings-read.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 159 (round 167, workstream ~P), cell `IB-pr-486`.
<owned_cells>IB-pr-486</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB167-6-AC1, IB167-6-AC2, IB167-6-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-486.live-host-resident-bindings-read.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: the tool was not run by the issuer; the cell changes nothing: one host file read through SSM, a unit-state read and repo reads.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission change; the applier's existing SSM and describe rights are used, and a refusal is a row.
comp-routes: DECLARED-NOT-APPLICABLE -- no route change.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no CloudFront or cache surface is touched.
comp-adversary: RUN -- p167_cells.py dry-run at base box/dell2 on dell2 2026-10-12 ~20:4xZ: IB167-6 AC1 FAIL, AC2 FAIL, AC3 FAIL (no record); commit-gate clean. The expectations are shape and bounds; nothing about the host's state is fixed by the issuer, who has not read the host. The forbidden-pattern list is the one IB-pr-431's check used (with its two corrections) plus cp and sed -i.
lane: 0.7.0_AE_CloudOps~IB2 is IRPT_BCKEND's applier seat (live at the cut by get_live_agents); the resident package and the YCharts host are IRPT_BCKEND's by CTO msg 4916.
</preflight>
