# NFRA_OPLGTW task order -- `OG-en-1` -- the list-only run for the Tax SMA master 08403355, beside its control (PRD v2.0 item 5(a), FWD-13)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D9/NFRA/NFRA_OPLGTW/decompositions/NFRA_OPLGTW_DECOMP.md</decomp_doc>
<owned_cells>OG-en-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_OPLGTW~39</issued_to>
<issued_by>2.0.0_SA_COO~O</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: RUN-BY-ISSUER at the cut -- the two live daily-pull rules read cron(45 9,21 * * ? *) (08335338) and cron(15 10,22 * * ? *) (08242234), ENABLED; this cell's runs start outside [09:15,11:05) and [21:15,23:05) UTC. No cron, alarm or monitor is created.
comp-iam: DECLARED-NOT-APPLICABLE the acts run under the operator's IAM user (arn:aws:iam::313476888478:user/Andrew_Berman): one SSM RunPowerShellScript command per master to i-0f3d57a97f14727af, SSM invocation reads and two S3 heads; no service role, policy or resource policy is read for a decision or changed.
comp-adversary: DECLARED-NOT-APPLICABLE -- the ask is Andrew-direct 2026-10-08 ~17:4xZ answer 1 (org/tier1_exec/4.0.0_SA_CRO~Z/deliverables/ANDREW_DIRECT_20261008_174xZ_GATEWAY_SCHWAB_FOUR_CALLS_ANSWERED.md @116d52009d) on the assessment @139c8d018e section 5, and round-31 analysis item 3 (@e43ee663be).
EGRESS CLASS, declared: VENDOR (Schwab SDD) FROM THE SI2 BOX ONLY, two list requests (one per master), on Andrew's answer 1 ("Yes, rec approved") for 08403355 and as the control the scheduled job already makes twice a day for 08335338. No egress from the workstation.
</preflight>

## 1. THE CELL -- `OG-en-1` (decomposition addendum R3-T.30, round 32 item 3)

Alyssa needs the Tax SMA master `08403355`; it is not pulled at all today. The daily Schwab puller
(`infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`, 568 lines) is a REST client on the SI2 box
`i-0f3d57a97f14727af`; the master is a request parameter (`$req.MasterAccount`, line 323). What stops `08403355` is
ours: `[ValidateSet('08242234','08335338')]` on `-Master` (line 31). `-Mode enumerate` (lines 361-368) runs the ONE
wide search over the last `-LookbackDays` (default 30), logs per-type counts, and exits 0 BEFORE any download or S3
write. A search that enumerates zero files over a window containing trading days `Die 2`s (line 341ff).

This cell answers one question with one run per master: does Schwab return files for `08403355` to the login the box
holds, and are they the same file types and the same vendor filename grammar as the control master `08335338` over the
same window? It changes nothing that lands or runs.

**How the box runs the puller (read `infra/aws/terraform/canonical-schwab-ec2/monolith-daily-schedule.tf` lines 58-150
first; copy its proven pattern).** SSM runs as SYSTEM, whose credential vault is EMPTY; the SDD token lives in
Administrator's vault. So SSM only REGISTERS and STARTS a Windows Scheduled Task that runs as
`/RU Administrator /IT /RL HIGHEST`, proves it started, waits for it, prints the log, and unregisters it. A task that
never starts means the Administrator console session is logged off: that is a STOP and a BLOCKING row, not a retry.

Do:
1. **Timing.** Start each run only when the UTC clock is outside [09:15, 11:05) and [21:15, 23:05) (the two daily
   pulls at 09:45/21:45 and 10:15/22:15 UTC and their 50-minute deadlines). The puller also takes a box-wide session
   lock and `Die 7`s if a sibling holds it; that refusal is a wait-and-retry-once after 10 minutes, then a row.
   Run the two masters one after the other, never at once.
2. **The box-side copy (never the installed file, never the S3 code object).** In the SSM command: copy the same bytes
   the schedule runs (`s3://opal-data-assets/code/canonical-schwab-si2/sdd-daily-pull.ps1`, ETag
   `0017f9b549ca9f8013704f50c4327bed`, byte-identical to the repo file) to `C:\schwab-sdd\og-g5\sdd-enumerate-g5.ps1`,
   and make exactly TWO text edits to that copy with PowerShell `-replace`, each asserted to have matched once:
   (a) the ValidateSet gains `'08403355'`; (b) inside the `if ($Mode -eq 'enumerate')` block, one `Log` line per plan
   row printing its physical file name (`$_.phys` for each row of `$plan`), so the vendor filename grammar is visible.
   Print the two edited lines and the copy's SHA-256 to the SSM output.
3. **The run.** A scheduled task named `OpalOgG5Enumerate-<master>` runs
   `powershell.exe -ExecutionPolicy Bypass -File C:\schwab-sdd\og-g5\sdd-enumerate-g5.ps1 -Master <master> -Mode enumerate -Target monolith`
   with NO `-SnsTopicArn` (a refusal must page no one) and the default 30-day lookback. Then print, from
   `C:\schwab-sdd\daily\<master>\daily-pull.log`, every line of THIS run (from its `=== SDD DAILY PULL master=<m>
   mode=enumerate` header to the end). Unregister the task. After the second run, delete `C:\schwab-sdd\og-g5\`.
   Use `executionTimeout` 3600 and poll `aws ssm get-command-invocation` until terminal (each poll a separate command).
4. **The record**, `W/g5_enumerate_record.json`, exactly this shape:
   `{"instance_id": "i-0f3d57a97f14727af", "window": {"from": "YYYY-MM-DD", "to": "YYYY-MM-DD"},
     "box_copy": {"sha256": "...", "edits": ["<edited line a>", "<edited line b>"]},
     "runs": {"08403355": {"command_id": "...", "started_utc": "...", "exit_code": 0, "enumerated": <int>,
                           "by_type": {"<type>": <int>, ...}, "filename_grammar": ["<pattern>", ...],
                           "outcome": "FILES" | "ZERO_FILES"},
              "08335338": { ...the same keys... }},
     "side_by_side": {"types_only_in_08403355": [...], "types_only_in_08335338": [...], "grammar_equal": true|false},
     "task_unregistered": true, "copy_deleted": true}`
   `filename_grammar` generalises the names you saw (e.g. `{master}.CRS{YYYYMMDD}.{TYPE}.zip`,
   `{master}.CS{MMDDYY}.{TYPE}.zip`); never list a whole name that carries an account number.
   Also write `W/g5_enumerate.result.md`: the two runs side by side, the verdict on "the same shape" (same type set,
   same grammar) and, if `08403355` enumerated zero files over a window with trading days, the plain statement that the
   box's login is not entitled to that master and the fix is Schwab-side.
5. If 08403355 returns ZERO files, that is a RESULT, not a failure of this cell: record it (its `Die 2` log line is
   the evidence) and finish.

`W` = `org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~39/`.

## 2. BOUNDS

- `-Mode enumerate` ONLY. No `download`. Nothing lands in S3; the S3 code object, the installed
  `C:\schwab-sdd\sdd-daily-pull.ps1`, the repo puller, every Terraform file and every EventBridge rule are untouched.
- No `-SnsTopicArn`. No change to the box's scheduled tasks other than registering and unregistering your own.
- Two vendor list requests in all (one per master). A run that fails before the search may be retried once.
- Never: push, `git stash`, rebase, `checkout --` or `clean`; override a gate; RDP or touch the SI2 GUI.
- REFUSE a criterion you cannot meet as written. File a BLOCKING row and keep working.

## 3. SURFACES

<paths>
org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/0.9.0_WK_NFRA_OPLGTW~39/
org/missions/D9/NFRA/NFRA_OPLGTW/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read only: `infra/aws/ec2/canonical-schwab-si2/sdd-daily-pull.ps1`,
`infra/aws/terraform/canonical-schwab-ec2/monolith-daily-schedule.tf`, `data/assets/docs/SCHWAB_AUTO_PULL_DESIGN.md`.
AWS: `.tools/aws` (the repo's shim) for `ssm send-command`, `ssm get-command-invocation`, `s3api head-object`.

Rows: id `NFRA_OPLGTW-Z-W39-S<k>`, fabric `site-z`, disarm_owner `2.0.0_SA_COO~O`; `surfaced_at` = `date -u +%FT%TZ` at filing.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="OG-en-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/g5.AC1.sh; echo "exit=$?"</invocation><expect>(?s)08403355: invocation .*08335338: invocation .*RESULT: PASS.*exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="OG-en-1"><invocation>bash org/missions/D9/NFRA/NFRA_OPLGTW/deliverables/2.0.0_SA_COO~O/r32/checks/g5.AC2.sh; echo "exit=$?"</invocation><expect>(?s)\(a\) objects under schwab/08403355/: KeyCount=0 .*\(b\) code object ETag=0017f9b549ca9f8013704f50c4327bed .*Terraform roots: 0\n.*RESULT: PASS.*exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: every count in your record is re-read from the SSM invocations themselves; the control enumerates files.
- `AC2`: nothing landed under the new master, and the scheduled puller's code is the bytes it was.

## 5. WHEN YOU ARE DONE

1. Write the proof instance at `W/NFRA_OPLGTW.TO-OG-en-1.taxsma-master-enumerate.proof_of_spec.json`.
2. Validate it with `python .tools/proof-of-spec-check.py <instance>`.
3. If both criteria PASS, edit the ONE `<status>` tag of this order IN PLACE to `complete`.
4. Report once: literal AC outputs; the two SSM command ids; the side-by-side; the "same shape" verdict; commits and rows.
   Your next order (`OG-tm-1`) reads your record; you will be handed it by continuation.

<!-- ===================== RECORD FACE ===================== -->

**ISSUER NOTES:**
- Round 32 (R3-T.30), item 3; chain `OG-en-1` -> `OG-tm-1` (section 4a item 7) in slot ~39's queue.
- The CTO's item text says the order adds 08403355 to the `-Master` set "on its own branch only to make the call".
  The issuer tightens that in the same direction: the edit lives only in a box-side temp copy, so no branch carries a
  puller change that a drain could land.
- Spawned at or after 23:05Z 2026-10-08 (the next start outside both pull windows), a stated wait with its reason: the
  box-wide SDD session lock.
- Pre-cut: see the issuance commit.

<status>complete</status>
<round>32</round>
<slot>~39</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
