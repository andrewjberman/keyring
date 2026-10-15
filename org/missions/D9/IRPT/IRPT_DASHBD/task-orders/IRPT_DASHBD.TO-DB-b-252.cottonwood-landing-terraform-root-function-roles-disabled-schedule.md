# TO IRPT_DASHBD.TO-DB-b-252 -- the COTTONWOOD LANDING TERRAFORM ROOT (round 123, workstream B-49F): a NEW root `infra/aws/terraform/investor-reporting/account-return-daily/` holding the function `irpt-cot-account-return-daily-lambda` (module yang-lambda: the function and its log group), its execution role and policy, its scheduler role and policy, and a schedule created DISABLED at `cron(15 8 ? * MON-FRI *)` New York; every name from the builder module, every IAM action explicit; written in files only, nothing planned, applied or deployed; the applier's plan must read 7 add / 0 change / 0 destroy

<to_id>IRPT_DASHBD.TO-DB-b-252</to_id>
<project>IRPT_DASHBD</project>
<issued_to>0.9.0_WK_IRPT_DASHBD~206</issued_to>
<issued_by>2.0.0_SA_COO~D2</issued_by>
<issued_date>2026-10-15</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>123</round>
<workstream>B-49F</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Workstream:** B-49F, round 123 | **Ordered by:** 1.0.0_SA_CTO~DELL2, CTO ROUND-123 ANALYSIS (B-49F) section 2 ruling 3 and section 3 cell 3 (`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_ROUND_ANALYSIS_IRPT_DASHBD_B-49F_ROUND_123_20261015.md @1ffd4f5afb`: "The Cottonwood landing pair packet is cut next round, with a `*-cot-*` role, builder names, the 15-member closure, and the naming-gate citation for its artifact key") | **Rows:** IRPT_DASHBD-D2-W206-S<k> | **Decomp cell:** `DB-b-252` (decomposition section 121) | **outcome_ref:** FWD-11, FWD-21 | **depends_on:** none (the handler and the source-map entry it deploys are merged, round 122)

**Risk class WORLD** is the floor of the paths below (an `infra/` path): this order writes Terraform files in a NEW root and runs no Terraform command and no AWS call; the plan and the apply are another seat's act under a signed never-widen pair.

---

## WORKER FACE

Your workspace worktree is `C:/dev/wk-irpt-dashbd-206` (branch `wk-IRPT_DASHBD-206`); run everything from its root. Your folder is `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~206/`. Never push; never commit the workspace `portal` gitlink. Client data lives ONLY under `C:/dev/_irpt_private_evidence_20261009/`: counts, dates, hashes and words only in the repo, a row, a commit message or your report; never a household or account id or a client value (a public security identifier with a count of accounts is not a client value). Your private output folder is `C:/dev/_irpt_private_evidence_20261009/IRPT_DASHBD/0.9.0_WK_IRPT_DASHBD~206/` (create it if absent). **A commit message, a row, a record or a report that quotes a client figure is a defect even if it is later removed: your branch is merged whole, history included. Before every commit, scan what you stage for a client figure and for long identifier runs.** The commit gate's client-data list is absent on this box, so that scan is yours. **Commit order: the artifacts first, then the proof instance, then the status flip to complete as the LAST commit; once the order is complete your grant ends, so do every edit before the flip.**

**Why.** Round 120 read the landing facts (`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~195/RD_CW_LANDING_FACTS_R120.json`: the five builder names, the five IAM statements, the schedule and its trading-day frontier, the expected plan of 7 adds, the blast radius and the rollback). Round 121 built the adapter's write path; round 122 built the handler `infra/aws/lambda/investor-reporting/account-return-daily/handler.py` and the source-map entry `irpt-cot-account-return-daily-lambda` (15 staged members, pins null). Nothing yet deploys it. This cell writes the Terraform root that does, as a pure ADDITION: a new directory with its own state key, so no existing root, function, role, zip or schedule is touched. The schedule is created DISABLED and enabled only after the catch-up's after-read, by another act.

**The cell (`DB-b-252`).**
1. **Read first, whole:** the issuer's checker `org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r123/p123_cotroot.py` (your three criteria; its docstring, the HCL, scope and facts clauses); the landing facts above (names, iam, schedule, expected plan, blast radius, rollback); the PRECEDENT root `infra/aws/terraform/investor-reporting/holdings-performance/` (`main.tf` the terraform, backend and provider blocks, `lambda.tf` the module call, `iam.tf` the execution and scheduler roles with their policy documents, `locals.tf` how the firm scope and buckets are DERIVED and never typed, `schedule.tf` the schedule resource) and the sibling root `infra/aws/terraform/investor-reporting/reporting-gold/`; the module `infra/aws/terraform/modules/yang-lambda/` (`variables.tf`: `function_name`, `artifact_bucket`, `artifact_key`, `role_arn`, `handler`, `timeout`, `memory_size`, `reserved_concurrent_executions`) and `modules/opal_name/`; the source-map entry `irpt-cot-account-return-daily-lambda` in `infra/aws/lambda/ci/lambda-source-map.json` (its `artifact_s3_key`, `source_dir`); the handler's docstring (what it reads and writes); `lib/opal_naming.py` and `infra/logic/registry/scopes.json`.
2. **The new root** `infra/aws/terraform/investor-reporting/account-return-daily/` (the directory name is the function's own token and carries no firm: the naming gate refuses a firm token in a NEW hand-kept literal, so every firm-scoped name, bucket and prefix is DERIVED the way the precedent derives it, from the registry, never typed; if the gate refuses any literal, file a row with the file and line and stop on that point). Files `main.tf` (terraform, backend `s3` with key `investor-reporting/account-return-daily/tfstate`, provider, caller identity), `locals.tf`, `lambda.tf`, `iam.tf`, `schedule.tf` (you may split differently, but every file is `.tf` in that directory). Contents:
   - FIVE `opal_name` module calls for the five names of the landing facts (function kind `lambda`; role `execution`; policy `execution`; role `scheduler`; kind `daily`), with the scope DERIVED. The checker recomputes the five names with `lib/opal_naming.py name()` from the builder arguments you record and compares them with the facts' names; it also requires that none of the five names appears as a typed string in the files.
   - ONE `yang-lambda` module call: `handler = "handler.lambda_handler"`, a `timeout` (the handler runs at most 5 days a fire at about one Black Diamond silver read each; choose and justify in the words), a `memory_size` (justify), `reserved_concurrent_executions = 1`, NO `environment_variables` (no firm token in an environment), the artifact bucket and key taken from the source-map entry (read `artifact_s3_key` from `lambda-source-map.json` with `file`/`jsondecode`, or cite the literal the way the naming gate's citation rule requires: the gate tells you), `role_arn` of the execution role.
   - TWO `aws_iam_role` and TWO `aws_iam_role_policy` (execution; scheduler) and ONE `aws_scheduler_schedule` and nothing else (no `aws_lambda_permission`, no extra resource type). The execution policy's statements, each with explicit `actions` and derived `resources`, no `*`: `s3:GetObject` on the two Black Diamond silver tables ONLY (`fact_allocations`, `fact_transactions`, in the silver root the adapter reads); `s3:ListBucket` on the silver bucket with an `s3:prefix` `StringLike` condition for those two table prefixes; `s3:PutObject` on the ONE Cottonwood gold prefix `account_return_daily` (exactly one PutObject statement in the root); `logs:CreateLogStream` and `logs:PutLogEvents` on the function's own log group. The scheduler role's policy: `lambda:InvokeFunction` on the one function's ARN (exactly one such statement). The assume-role documents use `sts:AssumeRole` for the right service principals.
   - The schedule: `state = "DISABLED"`, `schedule_expression = "cron(15 8 ? * MON-FRI *)"`, `schedule_expression_timezone = "America/New_York"`, target the function with the scheduler role, and a `flexible_time_window` of OFF; its comment says it is created DISABLED and enabled after the catch-up's after-read (see the landing facts).
3. **No other file changes:** not the handler, the source map, any existing root, `lib/`, the registry or the adapter.
4. **The facts record** `RD_COT_ROOT_FACTS_R123.json` in your folder with EXACTLY these fields: `root` ("infra/aws/terraform/investor-reporting/account-return-daily/"); `files_changed` (every `.tf` file of the root, at least three, each {`file`, `sha256` (of the bytes at your final commit), `kind` "terraform"}); `names` (a list of exactly five, in the landing facts' order, each {`purpose`, `builder_args` {`system`, `scope`, `function`, `kind`, and `qualifier` when the name has one}, `name`}: the checker recomputes `name` from `builder_args`); `resources` (the seven Terraform addresses the plan will add: two `aws_iam_role.<x>`, two `aws_iam_role_policy.<x>`, one `aws_scheduler_schedule.<x>`, and the module's `module.<m>.aws_lambda_function.this` and `module.<m>.aws_cloudwatch_log_group.lambda`); `expected_plan` {`to_add` 7, `to_change` 0, `to_destroy` 0, `words`}; `schedule` {`cron`, `zone`, `state` ("DISABLED"), `words`}; `iam` {`statement_ids` (the sids of every statement in the root, equal to the HCL's), `no_wildcard` true, `words`}; `artifact` {`entry` ("irpt-cot-account-return-daily-lambda"), `key` (the artifact key as the source map states it), `words`}; `validated` {`ran` (boolean), `words` (the box has no terraform: say what you could check)}; `derivations` {`scope`, `buckets`, `prefixes`} (one sentence each: where each is derived from); `words`; `claim` ("inferred"); `files_in_repo` false; `served_values_changed` false; `pushed` false; `deployed` false. No run of 8 or more digits outside a `path`, `file`, `key`, `where`, `sha256`, `vintage`, `resources`, `name`, `arn` or `arns` field.

<criterion id="DB123-3-AC1" cell_refs="DB-b-252"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r123/p123_cotroot.py" . DB123-3-AC1</invocation><expect>DB123-3-AC1 PASS</expect></criterion>
`DB123-3-AC1` -- the root's `.tf` files declare exactly two `aws_iam_role`, two `aws_iam_role_policy` and one `aws_scheduler_schedule` and no other resource type; exactly one `yang-lambda` module with handler `handler.lambda_handler`, a timeout, a memory size and `reserved_concurrent_executions = 1`, no environment variable; at least five `opal_name` module calls and none of the five builder names typed; the schedule is `DISABLED` with the cron and zone above; every IAM statement has explicit allowed actions, exactly one PutObject (on the `account_return_daily` prefix) and one `lambda:InvokeFunction`, both silver tables named, no all-resources grant; the artifact key is the source-map entry's or read from the source map; the backend key is `investor-reporting/account-return-daily/tfstate`. Base: FAIL (no root).
<criterion id="DB123-3-AC2" cell_refs="DB-b-252"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r123/p123_cotroot.py" . DB123-3-AC2</invocation><expect>DB123-3-AC2 PASS</expect></criterion>
`DB123-3-AC2` -- the change is ADDITIVE: in the worker's own commits every file under `infra/`, `data/`, `lib/` and `org/standards/` lies inside the new root, the root did not exist before the worker's first commit, and the commits touch at least three of its files. Base: FAIL (no commit).
<criterion id="DB123-3-AC3" cell_refs="DB-b-252"><invocation>python -I "org/missions/D9/IRPT/IRPT_DASHBD/deliverables/2.0.0_SA_COO~D2/checks/r123/p123_cotroot.py" . DB123-3-AC3</invocation><expect>DB123-3-AC3 PASS</expect></criterion>
`DB123-3-AC3` -- `RD_COT_ROOT_FACTS_R123.json` has exactly the form of step 4; its five names EQUAL what `lib/opal_naming.py name()` returns for the recorded arguments; its seven resources match the HCL; the plan is 7 add / 0 change / 0 destroy; the schedule block is DISABLED; its statement ids equal the HCL's; its files hash as recorded; flags false; no long digit run outside the exempt fields. Base: FAIL (no record).

<expected_criteria>DB123-3-AC1,DB123-3-AC2,DB123-3-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below. Everything else is read, never edited: the handler, the adapter, the source map, every existing Terraform root and module, `lib/`, the registry, the issuer's check files and the portal.
- **Reads and writes.** Reads: repo files and `lib/opal_naming.py` run locally. No AWS call of any kind, no Terraform command (`init`, `plan`, `validate` and `fmt` included; the box has none), no S3, no deploy, no push, no vendor call, no secret read. Writes: the repo files of the grant.
- **Client data.** None is involved.
- **Refusal clause.** A criterion you cannot satisfy AS WRITTEN is reported with your measurement, never repaired, widened or satisfied by a route this order did not name. A name the builder refuses is a missing registry row: file a BLOCKING row and stop on that point (never type the name). If the naming gate refuses any literal of the root, file a row with the file and line and stop; never force, override or edit the gate. An edit outside the grant is a defect: stop and file a row.
- **Rows** go to the investigation file in the grant, ids `IRPT_DASHBD-D2-W206-S<k>` (start at S1), with the real current UTC time (`date -u +%FT%TZ`); append as BYTES. Commit with `.tools/safe-commit.sh`; run its gates in the background and wait for them. ASCII only in anything you write; every `.py` passes ruff (target py39, no semicolon-joined statements).

<paths>
infra/aws/terraform/investor-reporting/account-return-daily/
org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~206/
org/missions/D9/IRPT/IRPT_DASHBD/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_DASHBD/task-orders/IRPT_DASHBD.TO-DB-b-252.cottonwood-landing-terraform-root-function-roles-disabled-schedule.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_DASHBD/decompositions/IRPT_DASHBD_DECOMP.md</decomp_doc> section 121 (round 123, workstream B-49F), cell `DB-b-252`.
<owned_cells>DB-b-252</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: DB123-3-AC1, DB123-3-AC2, DB123-3-AC3 (mechanical). The instance goes at
`org/missions/D9/IRPT/IRPT_DASHBD/deliverables/0.9.0_WK_IRPT_DASHBD~206/IRPT_DASHBD.TO-DB-b-252.cottonwood-landing-terraform-root-function-roles-disabled-schedule.proof_of_spec.json`.
Validate it with `python .tools/proof-of-spec-check.py <instance> DB123-3-AC1,DB123-3-AC2,DB123-3-AC3` BEFORE the flip (the ids as ONE comma-joined argument); pin each artifact row to the commit that carried it (a PENDING-THIS-COMMIT pin that predates the instance commit makes it INVALID).
</proof_of_spec>

**REPORT:** your final message, once: each criterion's last line; the files of the root and what each holds; the five names; the seven resources; the timeout and memory you chose and why; how the scope, buckets and prefixes are derived; any gate refusal; what you could not check without Terraform. Words and counts only.

---

## RECORD FACE

<preflight>
comp-blast: DECLARED-NOT-APPLICABLE -- reason: a new Terraform root and a facts record in a branch; nothing is planned, applied, scheduled or deployed, and the apply is another seat's act under a signed never-widen pair; every resource is new and no existing one is touched.
comp-iam: DECLARED-NOT-APPLICABLE -- reason: no grant is changed in AWS; the root defines a new execution role and policy (Get on two silver tables, List under a prefix condition, Put on one gold prefix, logs) and a scheduler role (invoke one function); none takes effect before the applier's apply, under the pair.
comp-routes: DECLARED-NOT-APPLICABLE -- reason: no route is changed; nothing is deployed.
comp-schedule: DECLARED-NOT-APPLICABLE -- reason: no schedule is touched.
comp-cache: DECLARED-NOT-APPLICABLE -- reason: no cache surface is touched; nothing is deployed.
comp-adversary: DECLARED-NOT-APPLICABLE -- reason: not run by the issuer as a tool; the criteria FAIL at base and the checker's clauses are exercised by its self-test (green and red arms); its clauses were dry-run at the base (no root) and exercised by its self-test (eleven HCL arms and nine facts arms).
lane: the <paths> block IS the grant.
</preflight>
