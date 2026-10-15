# TO IRPT_BCKEND.TO-IB-pr-559 -- READ AWS for the writer of the daily Orion Inflection flat keys (bronze/{positions,transactions,performance}/<date>.jsonl.gz, 11:39-11:56Z): what writes them, how it is stopped or handed to the scheduled handler; READ ONLY (CTO half of IB-pr-556, condition 1, msg 8062)

<to_id>IRPT_BCKEND.TO-IB-pr-559</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~403</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>SERVED</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~PO</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Ordered by:** the CTO half of the Orion pairs packet (`deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_IB_pr_556_ORION_PAIRS_CTO_HALF.md`, condition 1: "locate the 11:39-11:56Z writer before (b) deploys, or (b) does not deploy"; msg 8062) and the four managers' answers (msgs 8063 to 8073) | **Decomp cell:** `IB-pr-559` (decomposition section 197) | **outcome_ref:** FWD-3

---

## WORKER FACE

**Your worktree:** `C:/dev/wk-IRPT_BCKEND-403`, cut from the current branch by the issuer. Commit with `bash .tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~403 <0.9.0_WK_IRPT_BCKEND~403@opal.agent>" -F <msgfile> -- <explicit paths>` (message file by the Write tool, ending with `Co-Authored-By: Claude Haiku 5.5 <noreply@anthropic.com>`; no backtick or dollar-parenthesis in the command line). `portal` shows modified in a fresh worktree: NEVER commit it. Never push. Do not run a recursive grep over the repository (use Grep, Glob, Read on named files and folders). Commit gates take minutes: wait. The commit-time client-data check reads WARN-only on dell2 by ruling: expected. **Paths you post are `file:///` absolute URIs or markdown links to them.** AWS CLI goes through the `.tools/aws` shim.

**Client data rule:** counts, dates, hashes, commit ids, object-key templates, resource NAMES (function, task, job, rule) and file paths only in any tracked file; no account id, AWS account number, ARN with an account number, IP address, household id, quantity or value. Scratch lives OUTSIDE the worktree (`C:/dev/_scratch403/`).

**Cell `IB-pr-559` (inlined).** The READ `IB-pr-552` (`deliverables/0.9.0_WK_IRPT_BCKEND~396/IB199-4_orion_raw_producer_read.json`; and `deliverables/0.9.0_WK_IRPT_BCKEND~400/IB200-4_orion_pairs_design.json` `live_writer`; rows `IRPT_BCKEND-D2-S182` and `D2-S184` in `org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md`; READ ALL FIRST) measured that the flat Orion Inflection keys `s3://opal-data-inf/bronze/<feed>/<date>.jsonl.gz` land EVERY day (transactions 11:39-11:43Z, performance 11:45-11:49Z, positions 11:48-11:56Z, on 2026-10-10 to 2026-10-14) after the deployed positions parquet (11:25-11:26Z), and that nothing in the repository or the scheduled objects read so far names the writer. The four boxes' managers have now read their scheduled tasks and running processes and reported NONE (dell2 195 tasks, dell1 196, laptop 211, site Z 214; msgs 8063, 8070, 8073 and the dell1 answer): the writer is not a Windows scheduled task. What those reads did not cover: AWS, and session-only crons inside seats. The CTO's condition: the writer is located before the scheduled handler deploys, or the handler does not deploy; the manual CLI writes (`data/inf/manual_api/pull_inflection_{positions,transactions,performance}_*.py`) are retired in the same pair, so the writer must be found and stopped or handed over in the same window. **This order READS AWS to find it. It changes, stops, starts, deletes and writes NOTHING.**

**Do, in this order (read-only calls only: `describe`, `list`, `get`, `head`, `lookup-events`, `filter-log-events`):**
1. **Base.** `git rev-parse HEAD` before your first commit is `base_commit`.
2. **Object metadata first (the cheapest evidence).** For at least three flat keys (one per feed) of the most recent days, `head-object` on `opal-data-inf`: record the metadata keys, the content type, the last-modified second, and whether any metadata or the S3 `x-amz-` fields name a writer role, tool or session (names only; no IP address, no account number). If versioning is on, list a key's versions and their timestamps (a writer that rewrites shows several).
3. **CloudTrail.** If CloudTrail records S3 data events for `opal-data-inf` (check `describe-trails` / `get-event-selectors`; record whether it does), `lookup-events` (or the trail's S3/Athena log location if one is readable) for `PutObject` / `CompleteMultipartUpload` on the three flat prefixes between 2026-10-10 and 2026-10-14: the principal NAME (role or user name, never an id), the user agent family (for example `aws-cli`, `Boto3`, `Lambda`, `ecs`), the source type (an AWS service principal or an address class: say `service`, `corporate` or `other`, never the address) and the times. `events_matching` counts them. If data events are not recorded, say so: that is a finding.
4. **S3 server access logs.** `get-bucket-logging` on `opal-data-inf`: enabled or not, and if enabled where the logs go and whether they are readable by you (read a day's logs for the flat prefixes if so: requester name and operation only).
5. **Enumerate the compute that could be the writer (counts with denominators, names of matches only):** Lambda functions whose name, environment variable NAMES or description mention inf, orion, bronze or positions (list all, print the count); EventBridge rules and Scheduler schedules (`events list-rules` paginated to the end, `scheduler list-schedules`) firing between 11:00 and 12:00 UTC; ECS clusters, task definitions and scheduled tasks; Glue jobs; EC2 instances (name tags and whether one is a runner that executes the repository's pull scripts: `describe-instances` names and states only) and SSM associations / maintenance windows / `list-commands` for the window (command document names and status only); CodeBuild projects and Step Functions state machines mentioning the same words. The bronze runner `inf-bronze-runner` EC2 and `inf-bronze-trigger` Lambda (the READ found them) are the first candidates: read what the runner executes and whether it pulls the repository's manual scripts.
6. **Conclude.** Record `writer` = `{"claim":"measured|inferred|absent","kind":"lambda|ecs_task|glue_job|ec2_instance|ssm_association|eventbridge_rule|codebuild|stepfunction|external_person|seat_session_cron|other|not_found","name":"<the resource name, 4+ characters, required unless not_found>","statement":"<who writes the flat keys, where it runs, since when, whether it still runs: 40+ characters>","evidence":["<line naming a source and a count or name, 20+ characters>", ... at least three]}`. `measured` only if an artifact states it (a CloudTrail event naming the principal, a task definition running the pull); `inferred` otherwise; `not_found` is an allowed kind (it can never be `measured`): say exactly what was searched. Record `handover` (40+ characters): how the writer is stopped or handed to the scheduled handler in the release's ledger (for example: disable that rule or task in the same ledger as the handler's first enabled day, keeping it as the rollback), or why this does not apply (for example the writer is a person's manual run: say who by role only).
7. **Write** `deliverables/0.9.0_WK_IRPT_BCKEND~403/IB202-1_flat_key_writer_read.json`: `{"base_commit":"<40hex>","writer":{..},"searched":{"cloudtrail":{"window":"2026-10-10 to 2026-10-14","events_matching":<n>,"method":"<30+ characters>"},"s3_access_logs":{"enabled":true|false,"result":"<20+ characters>"},"lambda_functions_listed":<n>,"eventbridge_rules_listed":<n>,"ecs_clusters_listed":<n>,"glue_jobs_listed":<n>,"ec2_instances_listed":<n>,"ssm_associations_listed":<n>},"object_metadata":{"keys_examined":<n, at least 3>,"findings":"<30+ characters>"},"handover":"..","notes":["what each fact rests on and what was not read"],"functions_invoked":0,"sign_ins_made":0,"aws_writes_made":0,"rows_written":0,"figures_written":0,"vendor_requests_sent":0}`.

**Run the three criteria below from your worktree root**, record each output and exit code verbatim in `IB202-1_criteria_output.txt`, write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`, and commit with explicit paths (record and criteria output first, then set the instance's artifact rows to the hash of that commit, the instance last). Do NOT edit this order file or the check; do not flip `<status>`. If a criterion fails, fix YOUR record (never the check); a check no record can pass is the issuer's defect: file a BLOCKING row and report. Remove your scratch if you can. Report once, under 150 words.

**Criteria (run each under `timeout 120` from your worktree root, record the output and exit code verbatim):**

<criterion id="IB202-1-AC1" cell_refs="IB-pr-559"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r202/p202_cells.py" . IB202-1-AC1</invocation><expect>IB202-1-AC1 PASS</expect></criterion>
<criterion id="IB202-1-AC2" cell_refs="IB-pr-559"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r202/p202_cells.py" . IB202-1-AC2</invocation><expect>IB202-1-AC2 PASS</expect></criterion>
<criterion id="IB202-1-AC3" cell_refs="IB-pr-559"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r202/p202_cells.py" . IB202-1-AC3</invocation><expect>IB202-1-AC3 PASS</expect></criterion>

<expected_criteria>IB202-1-AC1, IB202-1-AC2, IB202-1-AC3</expected_criteria>

What the checks grade: AC1 the writer with a claim, a kind from the list and a statement and three evidence lines (a located writer needs a name; `not_found` can never be `measured`); AC2 the search as counts (CloudTrail window with dates and the matching events, S3 access logs enabled or not with the result, and the six enumeration counts); AC3 at least three keys' object metadata with findings, the hand-over, notes, the six bound counters 0, no long digit run. Do not edit the checks.

## BOUNDS

- **Grant:** the `paths` block, the worktree and the scratch directory outside the repository. READ ONLY. **Nothing is stopped, started, disabled, enabled, deleted, invoked, written to AWS, pulled, signed or sent, and no Orion request is made:** the only AWS calls are `describe`, `list`, `get`, `head`, `lookup-events`, `filter-log-events` and `get-*` reads with your identity. A denial is recorded, never worked around or widened. No secret value is read (names only).
- **Refusal clause:** STOP, file a row, change nothing more, on any of: a call that writes, starts, stops, disables, invokes or sends; a need to read a secret value; an account number, ARN with an account number or IP address in a tracked file. Never weaken a check.
- **Row ids** are `IRPT_BCKEND-D2-W403-S<k>` (start at 1); file a row for anything odd (a fenced json block in `INVESTIGATION_v1.md` with `grounding` and `surfaced_at` = `date -u +%FT%TZ`) and keep working.

<paths>
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~403/
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 197 (round 3, workstream ~PO), cell `IB-pr-559`.
<owned_cells>IB-pr-559</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IB202-1-AC1, IB202-1-AC2, IB202-1-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~403/IRPT_BCKEND.TO-IB-pr-559.read-aws-for-the-orion-daily-flat-key-writer.proof_of_spec.json`.
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE you report.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- the order lists and describes AWS objects (S3 object metadata, CloudTrail events, Lambda, EventBridge, ECS, Glue, EC2, SSM, CodeBuild, Step Functions) with the worker's own identity; it writes only the worker's records; nothing is stopped, started or changed, so no served byte moves; the stop or hand-over it describes is a later act in the release's ledger.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no permission is changed; the reads use the worker's own identity (a denial is recorded, not widened).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: schedule objects are described (read), never created, enabled or disabled.
comp-cache: DECLARED-NOT-APPLICABLE -- no CloudFront or cache surface is touched.
comp-adversary: RUN -- p202_cells.py IB202-1 dry-run at base on dell2 2026-10-15 ~05:3xZ: AC1, AC2, AC3 FAIL (no record). Positive control in a temp root the run created itself (a synthetic record; removed): all three PASS; eleven negatives, each failing its own arm: an unknown writer kind, two evidence lines, not_found claimed as measured, a writer with no name, no CloudTrail window dates, a missing search count, the access-logs state missing, two keys examined, no hand-over, a vendor request sent, a long digit run.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~403` (worktree `C:/dev/wk-IRPT_BCKEND-403`). Class SERVED (reads served objects and live infrastructure descriptions; writes only the worker's records).
</preflight>
