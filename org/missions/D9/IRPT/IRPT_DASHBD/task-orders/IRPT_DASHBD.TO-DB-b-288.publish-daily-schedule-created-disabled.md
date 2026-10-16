# TO IRPT_DASHBD.TO-DB-b-288 -- the DAILY SCHEDULE of the Cottonwood series publish, created DISABLED (round 148): a scheduler role, its policy and one schedule appended to the `reporting-publish-iso` root; everything else byte-identical

<to_id>IRPT_DASHBD.TO-DB-b-288</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~232</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-16</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>148</round>
<workstream>PUBWRITE</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** PUBWRITE, round 148 | **Ordered by:** 1.0.0_SA_CTO~DELL2, org/missions/D9/IRPT/IRPT_DASHBD/deliverables/1.0.0_SA_CTO~DELL2/NEVER_WIDEN_COTTONWOOD_REPORTING_PUBLISH_LAMBDA_CTO_HALF.md @474f33174c (condition 1) ("2.0.0_SA_COO~D2 owes the daily schedule, in its own pair, before any page reads this prefix as served") | **Decomp cell:** `DB-b-288` (decomposition section 149).

**Risk class WORLD** is the floor of the paths below (`infra/` paths): this order writes Terraform files and runs no Terraform command, no AWS write and no upload. NOTHING is planned, applied or deployed; the applier's plan for these files must read 3 add / 0 change / 0 destroy. The schedule is created DISABLED: enabling it is the CTO's separate word (a later one-line change, its own pair).

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-232` (branch `wk-IRPT_DASHBD-232`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~232/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~232/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** The Cottonwood series are published by hand. The CTO's condition on that publish is a daily schedule before any page reads the prefix as served. The report-build function's schedule (`cron(15 9 ? * MON-FRI *)`, after the landing fire at 08:15 and the account-dim fire at 08:45) is the model; this one fires after it, so a day's returns and its unreported-day statement are in place first. **The report-build root next door (`infra/aws/terraform/investor-reporting/reporting-gold-iso/`: `iam.tf` scheduler role and policy, `schedule.tf`) is the BLUEPRINT**: copy its scheduler pieces and change what is below.

**The cell (`DB-b-288`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p156_pubschedule.py` (your three criteria; `check_unchanged` and `check_hcl` are the exact spec); the four files of `infra/aws/terraform/investor-reporting/reporting-publish-iso/` (`main.tf`, `locals.tf`, `lambda.tf`, `iam.tf`); the blueprint's `iam.tf` (its scheduler block) and `schedule.tf`; `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/../r147/p149_pubroot.py` (the helpers the checker reuses).
2. **Edits.** `main.tf`, `locals.tf` and `lambda.tf` stay BYTE-IDENTICAL to the base. `iam.tf` keeps its current text as an UNCHANGED PREFIX and you APPEND the scheduler block: two new `opal_name` modules (`system = "irpt"`, `scope = local.irpt_pub_firm`, `function = "reporting-publish"`; kind `role` with qualifier `scheduler`, and kind `policy` with qualifier `scheduler`), an assume-role policy document with the single statement id `SchedulerRoleAssumedBySchedulerService` (principal `scheduler.amazonaws.com`), `aws_iam_role.irpt_reporting_publish_iso_scheduler`, a policy document with the single statement id `InvokeThePublishFunctionOnly` (action `lambda:InvokeFunction` ONLY, `resources = [module.irpt_reporting_publish_iso.function_arn]`), and `aws_iam_role_policy.irpt_reporting_publish_iso_scheduler`. A NEW file `schedule.tf`: one `opal_name` module (`system = "irpt"`, `scope = local.irpt_pub_firm`, `function = "reporting-publish"`, `kind = "daily"`) and `aws_scheduler_schedule.irpt_reporting_publish_iso` with `state = "DISABLED"`, `schedule_expression = "cron(30 9 ? * MON-FRI *)"`, `schedule_expression_timezone = "America/New_York"`, `flexible_time_window { mode = "OFF" }` and a `target` with `arn = module.irpt_reporting_publish_iso.function_arn`, `role_arn` the scheduler role's ARN and `input = jsonencode({ upload = true })`. A comment says the schedule is created DISABLED, why `{"upload": true}` (the function's default event is a dry run), and that enabling it is a later separate act. No alarm, no SNS topic, no SES, no notification, no other resource type. No firm word in any hand-kept string (the commit-time naming gate refuses it): every name comes from the builder.
3. **Run the checks yourself before the record:** `python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p156_pubschedule.py" . DB156-1-AC1`, then AC2 (this runs the real naming gate in plan mode on the three new names; it reads the committed files for placement, so COMMIT your Terraform files first), then AC3.
4. **Record** `RD_PUBLISH_SCHEDULE_FACTS_R148.json` in your folder with EXACTLY these fields: `root` ("infra/aws/terraform/investor-reporting/reporting-publish-iso/"); `new_names` (the three builder names, in the order scheduler role, scheduler policy, schedule); `new_resources` (the three addresses the plan will add: `aws_iam_role.irpt_reporting_publish_iso_scheduler`, `aws_iam_role_policy.irpt_reporting_publish_iso_scheduler`, `aws_scheduler_schedule.irpt_reporting_publish_iso`); `expected_plan` ({"add": 3, "change": 0, "destroy": 0, "claim": "inferred"}); `schedule` ({"cron": "cron(30 9 ? * MON-FRI *)", "zone": "America/New_York", "state": "DISABLED", "input": {"upload": true}}); `words` (one paragraph, 80 to 1800 characters: what the files declare, what the checks proved, what is NOT proven: no plan, no apply, no fire, and that enabling is a separate word).

<criterion id="DB156-1-AC1" cell_refs="DB-b-288"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p156_pubschedule.py" . DB156-1-AC1</invocation><expect>DB156-1-AC1 PASS</expect></criterion>
`DB156-1-AC1` -- `main.tf`, `locals.tf` and `lambda.tf` are byte-identical to the base; `iam.tf` keeps the base text as a prefix and only appends; the root declares exactly two roles, two role policies and one schedule, six `opal_name` calls and one yang-lambda module; the schedule is DISABLED at the cron above with the flexible window OFF, the function ARN as target and the input `{"upload": true}`; the statement ids are the six earlier ones plus the two new; the one `lambda:InvokeFunction` statement holds only that action on the function ARN; the one PutObject statement is unchanged; no builder name is typed.
<criterion id="DB156-1-AC2" cell_refs="DB-b-288"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p156_pubschedule.py" . DB156-1-AC2</invocation><expect>DB156-1-AC2 PASS</expect></criterion>
`DB156-1-AC2` -- the checker builds the three new names from the root's own module arguments with `lib/opal_naming.py` and runs the REAL `.tools/naming-apply-gate.py` in plan mode on a synthetic plan holding them: three CONFORMANT lines, no REFUSE.
<criterion id="DB156-1-AC3" cell_refs="DB-b-288"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r148/p156_pubschedule.py" . DB156-1-AC3</invocation><expect>DB156-1-AC3 PASS</expect></criterion>
`DB156-1-AC3` -- the facts record has exactly the form above and its names equal the checker's recount.

<expected_criteria>DB156-1-AC1,DB156-1-AC2,DB156-1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the function's code, the source map, the other roots, the handlers, the issuer's check files.
- **Reads and writes.** Reads: repo files, the naming gate, `lib/opal_naming.py`. Writes: the repo files of the grant and your private folder. No Terraform command, no AWS call, no upload, no push, no invoke.
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. If the naming gate refuses a name, record its refusal line verbatim, file a BLOCKING row and stop; never type a name to pass it.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W232-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/terraform/investor-reporting/reporting-publish-iso/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~232/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-288.publish-daily-schedule-created-disabled.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 149 (round 148, workstream PUBWRITE), cell `DB-b-288`.
<owned_cells>DB-b-288</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB156-1-AC1, DB156-1-AC2, DB156-1-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~232/IRPT_DASHBD.TO-DB-b-288.publish-daily-schedule-created-disabled.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB156-1-AC1,DB156-1-AC2,DB156-1-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the three addresses; the statement ids; what is NOT proven. Counts, paths and words only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: Terraform files in a branch; nothing is planned, applied, scheduled or deployed.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; the scheduler role is new and holds only lambda:InvokeFunction on the one function; no existing grant changes.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its HCL clause was validated by the issuer against a scratch reference block appended to the real root (green) and 14 single-fault arms (all red) by the self-test, and its naming clause probed against the real gate on the three names (3 CONFORMANT).
lane: the <paths> block IS the grant.
</preflight>
