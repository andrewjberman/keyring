# Deploy-completion ledger -- OPAL_MDPFCLEANUP.TO-3 K3 (REDUCED SET) producer kill

**Opened:** 20260818T1340Z by 0.7.0_AE_CloudOps. **GO chain:** COO K3 GO 130956Z (unconditional 132953Z) -> consumers-first STOP 133601Z (2 rows falsified-live) -> COO ruling 133706Z (bounded kill proceeds; runner/DLQ KEEP-UNTIL-REHOMED; Andrew's runner stop word RETRACTED) -> CTO GATE-GO 133935Z (5 post-apply reads as close conditions).
**PRD:** docs/architecture/OPAL_MDPFCLEANUP_PRD.md v1.1 @9f75dcb996 s3 row 41 (K3), s3.1 invocation-history requirement.
**Plan:** SAVED plan file k3_reduced.tfplan **sha256 8a18ba8a45a9ed9f** -- `terraform plan -destroy` with 10 `-target` addresses (the named act, COO 130956Z), root infra/aws/terraform/mdpf-pipeline. **Plan: 0 to add, 0 to change, 10 to destroy -- expected-rows-only, 0 riders, 0 non-destroy verbs.**
**Status: OPEN -- finishes in-session or rolls back + escalates loud (NEVER#8).**

## Kill set (10; every row K3-only by construction)
event_rule.mdpf_daily_refresh · event_target.mdpf_daily_refresh · lambda_permission.eventbridge_mdpf_trigger · module.mdpf_daily_trigger.aws_lambda_function.this (mdpf-daily-trigger, CodeSha256 xqTiW2Z/ETxDjILu0x0VulMvN9jVux9gG4thanF+mbo=, last invocation 2026-08-18 12:44:42Z via the rule, 1-3/day 7d, sole invoke principal = the rule) · module.mdpf_daily_trigger.aws_cloudwatch_log_group.lambda · iam_role_policy.mdpf_trigger_lambda · iam_role_policy_attachment.mdpf_trigger_basic · iam_role.mdpf_trigger_lambda · sqs_queue_policy.mdpf_trigger_dlq (POLICY only: single stmt, SourceArn = K3 rule; floor sends via its execution role) · cloudwatch_metric_alarm.mdpf_chain_failed (Service=mdpf-daily-runner).

## HELD -- KEEP-UNTIL-REHOMED (edges proven by three plans: 17-target pulled the FLOOR schedule = 26 destroys; minus-DLQ pulled the ACCRUAL bridge = 21; single-target iam_role.mdpf_runner alone drags 5 accrual resources)
aws_instance.mdpf_daily_runner (i-02448edb624a7a7cf) + role/profile/policy/attachment/SG.mdpf_runner -- accrual-bridge.tf:113 RUNNER_INSTANCE_ID, :59/:76 ec2 grants; the KEEP accrual bridge start-if-stopped + SSM-runs on it (invoked daily incl. today) · aws_sqs_queue.mdpf_trigger_dlq -- scheduled-floor.tf:155 dead_letter_config + :104 FloorDlqSend · alarm.mdpf_trigger_dlq_depth (watches the shared queue) · ssm_parameter.mdpf_custody_source (KEEP consumer build_mdpf_wse_49f_non_model_aua.py:150). **Andrew's runner stop/terminate word @874b52729c RETRACTED from tonight (COO (d)): given on a K3-only census, premise falsified -- surfaced, not spent.**

| Leg | Act | Proof required (CTO 133935Z) | State |
|---|---|---|---|
| K3-1 | safe-apply the SAVED plan (sha 8a18ba8a45a9ed9f) | apply rc + destroyed count = 10 | PENDING |
| K3-2a | absence reads + controls | rule/lambda/role/log-group/alarm NotFound; floor schedule + accrual lambda + runner instance PRESENT | PENDING |
| K3-2b | DLQ policy removal landed | get-queue-attributes Policy = absent AND QueueArn present | PENDING |
| K3-2c | floor DLQ path survives (APPLIED plane) | simulate floor exec role sqs:SendMessage on DLQ = allowed (one arn); SEPARATE positive control on the floor role | PENDING |
| K3-3 | declaration-removal commit | 10 decls + lambda-source-map row + CHANGELOG; re-plan converges modulo @2740e4de8f rider; tag; proof_TO-3 rev2 | PENDING |

**Rollback:** BEFORE K3-3 lands = one untargeted `safe-apply` on the root re-creates all 10 from the still-declared config (no data, no state). AFTER K3-3 = `git revert` + apply. **Consumer-exercise (TO-5):** tomorrow's 13:30Z floor mint of the cot dim with NO 12:4xZ legacy write preceding it.
**Residuals (CTO, dated items to COO on the two re-homes):** (i) runner lifecycle owner is now nobody -- the accrual bridge starts-if-stopped and never stops it; EC2 stop is Andrew-reserved; (ii) the DLQ is now floor-only substrate; retires with its depth alarm when the floor gets its own DLQ. **Rider named:** post-apply root non-0-diff = the @2740e4de8f X-ii-a staged re-home (route_bindings + policy rows) -- not drift.

**Closed:** {CLOSE}
