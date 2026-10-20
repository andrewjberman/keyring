# TO NFRA_SCHWABBF.TO-AL-s1 -- the Alongside Schwab Box, Terraform root part 2: four daily schedule rules (DISABLED), the SSM targets, the events role (text only)

<to_id>NFRA_SCHWABBF.TO-AL-s1</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~11</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-20</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>alongside</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-s-1` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) |
**outcome_ref:** FWD-8 | **depends_on:** `AL-a-1` (same worker, queued second; this order is handed to the worker when `AL-a-1` is complete; its files must exist in your worktree)

---

## WORKER FACE

### THE CELL

`AL-s-1`, the schedule half of PRD v0.5 C-ALONGSIDE. Andrew-direct 2026-10-20 ~13:5xZ: "it should be exact same setup and logic as already exists with the 49 schwab box". The 49F box's daily pull is: EventBridge rule -> SSM `AWS-RunPowerShellScript` as SYSTEM -> the command fetches the puller from S3, registers a one-shot scheduled task that runs AS ADMINISTRATOR (the vault holding the Schwab token is Administrator's; SYSTEM reads an empty vault), proves it started, waits, and propagates the real exit code. You write the Alongside copy as Terraform TEXT. No `terraform` command, no `aws` command, nothing applied.

**Read first (read-only, edit nothing):** `infra/aws/terraform/canonical-schwab-ec2/monolith-daily-schedule.tf` in full (the rule, the target with its long `input`, the events role and its policy; keep its explanatory comments in short form, and KEEP the `$ErrorActionPreference='Continue'` choice and the reason for it). Then the files `AL-a-1` wrote in your worktree under `infra/aws/terraform/alongside-schwab-ec2/` (`main.tf`, `masters.tf`, `iam.tf`, `secrets.tf`, `box.tf`).

**Addresses you READ (fixed by `AL-a-1`; do not redefine):** `local.alongside_masters` (map: master -> `{label, cron}`), `local.alongside_firm`, `aws_instance.alongside_box`. If any is missing in your worktree, STOP with a surprise row.

**New file:** `infra/aws/terraform/alongside-schwab-ec2/schedule.tf` (only this file; you do not edit `AL-a-1`'s files).

**Build.**
1. Variables (defined in `schedule.tf`): `alongside_schedule_state` (string, default `"DISABLED"`, validation: one of `ENABLED` / `DISABLED`) and `sns_critical_topic_arn` (string, default `"arn:aws:sns:us-east-1:313476888478:opal-critical-surface-alerts"`, the topic the 49F puller already passes; no new topic, no new alert).
2. Name modules (`source = "../modules/opal_name"`): `module "daily_rule_name"` with `for_each = local.alongside_masters`, `system = "schwab"`, `scope = each.key`, `function = "si2-pull"`, `kind = "daily"` (output for 08719286: `schwab-08719286-si2-pull-daily`); `module "events_role_name"` (`scope = "alongside"`, `function = "si2-events"`, `kind = "role"` -> `schwab-alongside-si2-events-role`); `module "events_policy_name"` (`scope = "alongside"`, `function = "send-daily-pull"`, `kind = "policy"` -> `schwab-alongside-send-daily-pull-policy`). No typed ternary for names: every rule, role and policy name is module output (PRD C-ALONGSIDE: "the 49F root's typed-name ternary is NOT copied").
3. `aws_cloudwatch_event_rule.alongside_daily` (`for_each = local.alongside_masters`): `name` = the rule module's `.name`, `schedule_expression = each.value.cron`, `state = var.alongside_schedule_state`, description naming the master's `label` and "Alongside Schwab Box".
4. `aws_cloudwatch_event_target.alongside_daily` (`for_each` the same map): `arn = "arn:aws:ssm:us-east-1::document/AWS-RunPowerShellScript"`, `role_arn` the events role, `run_command_targets { key = "InstanceIds", values = [aws_instance.alongside_box.id] }`, and `input = jsonencode({ executionTimeout = ["3600"], commands = [...] })` with the 49F command list adapted ONLY as follows: the code path is `s3://opal-data-assets/code/alongside-schwab-si2/sdd-daily-pull.ps1`; the on-box paths (`C:\schwab-sdd\...`), the task name prefix `OpalSddDailyPull-`, the 90 s start check, the 50-minute wait and the fail-loud `throw` lines are UNCHANGED; the master comes from `${each.key}`; the SNS value comes from `var.sns_critical_topic_arn`; the puller invocation is `-Master ${each.key} -Target monolith -SnsTopicArn <sns>`. No master number is typed anywhere in the file.
5. `aws_iam_role.alongside_events_ssm` (events.amazonaws.com trust, name from the events role module) and `aws_iam_role_policy.alongside_events_ssm` (name from the policy module) with ONE statement `SendDailyPullToAlongsideBox`: `ssm:SendCommand` on exactly `arn:aws:ssm:us-east-1::document/AWS-RunPowerShellScript` and `aws_instance.alongside_box.arn`. No `"*"` resource.
6. Output `alongside_daily_rule_arns` (map of master to rule ARN).
7. Test `data/canonical/schwab/tests/test_alongside_schedule_tf.py` (reads `.tf` text and `lib/opal_naming.py`; no terraform, no network):
   - FIRE TIMES (name contains `fire_times`): parse the four cron strings from `masters.tf`; every Alongside fire is at least 30 minutes from every other Alongside fire AND at least 30 minutes from each of the six 49F fire times, which the test declares as a literal list in the test file itself (09:45, 10:15, 10:45, 21:45, 22:15, 22:45 UTC; do not read the 49F Terraform).
   - DISABLED (name contains `disabled`): `alongside_schedule_state` defaults to `"DISABLED"`, the rule uses it, and the validation lists exactly `ENABLED` and `DISABLED`.
   - SSM COMMAND (name contains `ssm_command`): the commands block contains the Alongside code path, the `Unregister-ScheduledTask` cleanup, the `/RU Administrator /IT /RL HIGHEST` registration, the `NEVER STARTED` throw and the `LastTaskResult` propagation, derives the master from `${each.key}`, and contains no 8-digit master literal and none of the strings `canonical-schwab-si2`, `i-0f3d57a97f14727af`, `49financial`.
   - ROLE SCOPE (name contains `role_scope`): the policy has exactly two resources, the document and the instance ARN, and no `"*"`.
   - BUILDER NAMES (name contains `builder_names`): the three module inputs, passed to `lib/opal_naming.py name(...)`, return the strings in item 2 (for all four masters' rules), and no `name =` in `schedule.tf` is a typed literal.

### ACCEPTANCE

<criterion id="AL1-s1-AC1" cell_refs="AL-s-1"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_schedule_tf.py -q -p no:cacheprovider --color=no -k "fire_times or disabled"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL1-s1-AC1` -- the four fires keep the 30-minute stagger against each other and the six 49F fires, and ship DISABLED.

<criterion id="AL1-s1-AC2" cell_refs="AL-s-1"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_schedule_tf.py -q -p no:cacheprovider --color=no -k "ssm_command"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL1-s1-AC2` -- the SSM command keeps every fail-loud step of the 49F hand-off and names no 49F resource.

<criterion id="AL1-s1-AC3" cell_refs="AL-s-1"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_schedule_tf.py -q -p no:cacheprovider --color=no -k "role_scope or builder_names"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL1-s1-AC3` -- the events role reaches one document and one instance; every name is builder output.

<expected_criteria>AL1-s1-AC1,AL1-s1-AC2,AL1-s1-AC3</expected_criteria>

Dry-run at the base 2026-10-20 (the test file does not exist): all three, "file or directory not found" (rc 4) -- FAIL as expected. Write the test first and watch it fail, then build.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit (including `AL-a-1`'s five files).
- **WORLD floor, nothing applied.** No `terraform` command, no `aws` command, no deploy. Rules ship DISABLED; enabling them is a later release act.
- **Refusal clause.** If a criterion cannot be met as written (a cross-file address is missing, the builder refuses a name), stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W11-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
infra/aws/terraform/alongside-schwab-ec2/schedule.tf
data/canonical/schwab/tests/test_alongside_schedule_tf.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, round 1), cell `AL-s-1`.
<owned_cells>AL-s-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AL1-s1-AC1, AL1-s1-AC2, AL1-s1-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~11/NFRA_SCHWABBF.TO-AL-s1.alongside-box-daily-schedule.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL1-s1-AC1,AL1-s1-AC2,AL1-s1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** the file with its line count, each resource address, the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE as a tool run -- the six 49F fire times and the four Alongside fires are inlined and the test checks the 30-minute separation; the rules ship DISABLED so no gate is armed.
comp-iam: DECLARED-NOT-APPLICABLE as a tool run -- the events role is new and scoped to one document and one instance (copy of monolith-daily-schedule.tf:176-202); BLIND: the live IAM plane.
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition findings 2 (no fire before the sign-in: DISABLED) and 5 (the pull must run as an Administrator scheduled task) are inlined above.
lane: the <paths> block IS the grant.
</preflight>

Chain A, second order: the same worker takes it by continuation (its context intact) once AL-a-1 is complete. Source: PRD v0.5 C-ALONGSIDE; decomposition `NFRA_SCHWABBF_DECOMP_AL1.md` cell AL-s-1, rulings 4-5.
