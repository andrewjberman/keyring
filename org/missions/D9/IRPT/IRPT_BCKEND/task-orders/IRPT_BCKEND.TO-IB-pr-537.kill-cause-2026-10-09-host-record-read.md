# TO IRPT_BCKEND.TO-IB-pr-537 -- READ the cause of 49financial's 2026-10-09 kill (exit 137) from the host's own record: OOM, not OOM, or unreadable (CTO round-193 analysis item 3 @e9dabffe7b; rows D2-S164, D2-W381-S1)

<to_id>IRPT_BCKEND.TO-IB-pr-537</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.7.0_AE_CloudOps~IB2</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-14</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>193</round>
<workstream>~P</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO's round-193 analysis (item 3: "the host's own record for that invocation's window (the kernel log or the journal for an OOM kill, and the instance's memory at the time, if retained). One line: OOM, or not, or unreadable. If it is OOM, the release's fire carries a memory read in its after-read.") | **Decomp cell:** `IB-pr-537` (decomposition section 185) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Cell `IB-pr-537` (inlined).** 49financial's scheduled holdings fire of 2026-10-09 ran `python holdings_snapshot.py --firms 49financial` under SSM `AWS-RunShellScript` and ended `Failed`: invocation and plugin status `TimedOut`, StatusDetails `ExecutionTimedOut`, response code 137, the shell reporting the python process `Killed`, after about 310 seconds of a 3600-second window (rows D2-S164 and D2-W381-S1). Nobody has read WHY the process died; an out-of-memory kill is the candidate. **This order reads the host's own record for that window and states ONE verdict: `OOM`, `NOT_OOM` or `UNREADABLE`. It changes nothing on the host.**

**Do, in this order (a number or a line is a MEASUREMENT with its source named in `reads`):**
1. **Find the fire.** `ssm list-commands` (paginated to the end; print the count) filtered client-side on the Comment prefix `irpt holdings refresh 49financial 2026-10-09`; then `ssm list-command-invocations --command-id <id> --details` for status fields, the instance id, and `ResponseStartDateTime`/`ResponseFinishDateTime` of the plugin. Record `fire` = `{"fire_date":"2026-10-09","response_code":137,"plugin_seconds":<n>}` (the instance id stays out of every tracked file).
2. **The instance's memory, if retained.** `ec2 describe-instances` for the instance type and memory size (class only, as text such as `16 GiB class`), then `cloudwatch list-metrics --namespace CWAgent --dimensions Name=InstanceId,Value=<id>` for a memory metric; if one exists, read `get-metric-statistics` (60 s periods, Maximum) over the plugin window plus ten minutes either side and record the peak percent. If none is retained, say so in `reads`.
3. **The host's own kernel record (AT MOST TWO read-only host commands).** Using SSM `AWS-RunShellScript` against that one instance, send at most two commands, each READ ONLY and each starting with `journalctl`, `dmesg` or `grep` (no `;`, `&`, `>`, backtick, `$(`, `sudo`, `systemctl`, `rm`, `kill` or pipe to a shell; pipes to `grep`/`head`/`wc` are allowed). The first is `journalctl -k` over the plugin window (a few minutes either side, in the host's own time zone as the host reports it) piped to `grep -ciE "out of memory|oom-kill|killed process"` (a COUNT) and, if the count is above 0, a second command that prints at most five of those lines with `head -5` (record only: the process NAME and whether it is python; never a pid or a path). If journald holds nothing for the window (not persisted), the second command is the `dmesg -T` equivalent. If the instance is not `Online` in SSM, or the window has rotated out, the verdict is `UNREADABLE`: record why, send nothing, work around nothing. Record the commands VERBATIM in `host_commands` and their count in `host_commands_sent`.
4. **The verdict.** `OOM` only if a kernel line names an out-of-memory kill of a python process inside the plugin window; `NOT_OOM` only if the kernel record for the whole window was read and holds no such line (and say what the memory metric read, if any); otherwise `UNREADABLE`. `verdict_basis` is one real line. `memory_read_for_release_fire` is true exactly when the verdict is `OOM` (the release fire's after-read then carries a memory read: the issuer tells IB-pr-535).
5. **Write** `deliverables/0.7.0_AE_CloudOps~IB2/IB193-3_kill_cause.json`: `{"fire":{...},"verdict":"OOM|NOT_OOM|UNREADABLE","verdict_basis":"..","reads":[{"source":"..","result":".."}],"memory_read_for_release_fire":bool,"host_commands":[{"command":"..","read_only":true}],"host_commands_sent":<n>,"notes":["what each fact rests on and what was not read"],"functions_invoked":0,"aws_writes_made":0,"files_deleted":0,"service_restarts":0,"host_state_changes":0}`. No instance id, no pid, no account number, no log body beyond the process name.
6. **Run the three criteria below from the repository root**, record each output and exit code verbatim in `IB193-3_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths. Do NOT edit this order file or the check; do not flip `<status>`. Report once, under 150 words.

**Criteria (run each under `timeout 120` from the repository root, record the output and exit code verbatim):**

<criterion id="IB193-3-AC1" cell_refs="IB-pr-537"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r193/p193_cells.py" . IB193-3-AC1</invocation><expect>IB193-3-AC1 PASS</expect></criterion>
<criterion id="IB193-3-AC2" cell_refs="IB-pr-537"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r193/p193_cells.py" . IB193-3-AC2</invocation><expect>IB193-3-AC2 PASS</expect></criterion>
<criterion id="IB193-3-AC3" cell_refs="IB-pr-537"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r193/p193_cells.py" . IB193-3-AC3</invocation><expect>IB193-3-AC3 PASS</expect></criterion>

<expected_criteria>IB193-3-AC1, IB193-3-AC2, IB193-3-AC3</expected_criteria>

What the checks grade: AC1 the fire (2026-10-09, response code 137), a verdict from the three words, a one-line basis, reads each with a source and a result, and the release memory-read flag true exactly when the verdict is OOM; AC2 at most two host commands, `host_commands_sent` equal to the list, each starting with a read-only verb with none of the forbidden characters or verbs; AC3 no long digit run, a note, and the five bound counters 0. Do not edit the checks.

## BOUNDS

- **Grant:** the paths below and a scratch directory outside the repository. READ ONLY except the at-most-two host commands of step 3. **Nothing is written, invoked, restarted, uploaded, applied or deleted:** no Lambda invoke, no S3 write, no terraform, no service restart, no change to the host's state, no vendor call. A denial is recorded, never worked around or widened.
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a command that is not read-only; a third host command; the instance not Online (then the verdict is UNREADABLE, recorded); an identifier of an instance, account or process in a tracked file; a figure you cannot source (say so; do not estimate). Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-IB2-S<k>` (the next free `k`); file a row for anything odd and keep working. **Report once, under 150 words.**

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 185 (round 193, workstream ~P), cell `IB-pr-537`.
<owned_cells>IB-pr-537</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB193-3-AC1, IB193-3-AC2, IB193-3-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.7.0_AE_CloudOps~IB2/IRPT_BCKEND.TO-IB-pr-537.kill-cause-2026-10-09-host-record-read.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order reads SSM command history (status fields), one instance's type and a memory metric, and sends at most two read-only commands (journal/dmesg greps) to the one runner host that ran the failed fire; it writes and changes nothing on the host, and the host also runs the other firms' fires, so the commands are read-only by an allowlist the check enforces.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the seat's existing identity sends the commands, as it does for its other SSM reads.
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched or created.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p193_cells.py IB193-3 dry-run at base on dell2 2026-10-14 ~12:5xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp root the run created itself (a synthetic record; removed): all three PASS; negatives, each failing its own arm: an OOM verdict with no release memory read, a destructive host command, three host commands, a long digit run, a counter above 0.
lane: the paths block IS the grant; seat `0.7.0_AE_CloudOps~IB2` (dell2; idle at the cut, no open task order of this project). Class SERVED (reads the live SSM history and one runner host). The premises are the CTO's round-193 analysis item 3 and my own reading of rows D2-S164 and D2-W381-S1 (the fire died about 310 s into a 3600 s window; the sender of the exit-137 kill was not read).
</preflight>
