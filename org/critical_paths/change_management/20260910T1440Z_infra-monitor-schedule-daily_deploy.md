# CHANGE: infrastructure-monitor-daily -> EVERY DAY

**archetype:** DEPLOY · **state:** CLOSED — LANDED AND VERIFIED (opened before the act, per NEVER-2)

| | |
|---|---|
| **Actor** | `1.0.0_SA_CTO~Z` |
| **Opened** | 2026-09-10 ~14:40Z |
| **Authority** | Andrew-direct at this seat's terminal, VERBATIM: *"i also want to make sure this report runs every single day, without fail, so that scheduler should be adjusted accordingly"* |
| **Resource** | EventBridge rule `infrastructure-monitor-daily` (us-east-1) |
| **Target** | `arn:aws:lambda:us-east-1:313476888478:function:opal-infrastructure-monitor` |

## THE ACT

| | |
|---|---|
| before | `cron(0 13 ? * MON-FRI *)` — weekdays only |
| after | `cron(0 13 * * ? *)` — every day |
| unchanged | 13:00 UTC = 9:00 AM ET · state ENABLED · target · lambda permission |

**Scope: the SCHEDULE ONLY.** No code, no target, no permission, no new resource.

## WHY THIS PATH

⛔ **NOT Terraform, because there is no Terraform resource to change.** This rule is
**console-managed** — `infra/aws/terraform/shared-infra/infra-monitor.tf:20` mentions it only in a
COMMENT (*"EventBridge trigger ... remain console-managed for now ... Folding them into TF is a small
later hygiene leg"*). Measured: 1 hit across 569 Terraform files, and it is that comment line.

So `aws events put-rule` is the only available path and is consistent with the resource's current
management model. ⚠ **It also perpetuates the console-orphan drift the file itself complains about**
— that is a real cost, it is named rather than hidden, and folding this rule into Terraform is
carried into the addendum's cut rather than done here as unrequested scope.

**This does NOT touch the Lambda code path**, which remains artifact -> S3 -> `source_code_hash` ->
`safe-apply`, and `aws lambda update-function-code` remains forbidden.

## ROLLBACK

One command, atomic, no state to unwind:
`aws events put-rule --name infrastructure-monitor-daily --schedule-expression "cron(0 13 ? * MON-FRI *)"`

## ⛔ WHAT THIS CHANGE DOES **NOT** ACHIEVE

**Andrew asked for "every single day, WITHOUT FAIL". This delivers the first half only.**

Measured on the live function at 14:4xZ:

| | |
|---|---|
| dead-letter queue | **None** |
| CloudWatch alarms naming the function | **0** |

**So if the report fails to run or errors, NOTHING reports it.** The only failure signal today is
Andrew noticing an email did not arrive — which is precisely the "an alert that reaches nobody"
class this very report exists to find, sitting on the report itself.

⚠ **Closing that limb means an alarm, which the standing moratorium reserves to Andrew's explicit
word.** His "without fail" is not read as that word — it is ambiguous between *"schedule it daily"*
and *"tell me when it breaks"*, and the receiving agent does not adjudicate scope. **Surfaced to him
directly; carried into ADDENDUM 01's cut as a candidate outcome, NOT built.**

## VERIFICATION (filled at close)

Read back FROM THE SERVICE at 14:4xZ, not from the command's own return:

- [x] `describe-rule` -> `cron(0 13 * * ? *)`, state **ENABLED**
- [x] target **UNCHANGED** — 1 target, `...:function:opal-infrastructure-monitor`, identical ARN
      before and after (both read explicitly; a schedule change that silently dropped a target
      would leave a rule that fires at nothing)
- [ ] **first weekend fire — Sat 2026-09-13 13:00Z.** The only arm this record cannot close today;
      the act is verified, the OUTCOME is observed on Saturday.

## CLOSE

**state: CLOSED.** Schedule is daily and the target survived. Nothing half-landed: a `put-rule` is
atomic and the read-back confirms both limbs.

⛔ **CLOSED ON THE ACT, NOT ON "WITHOUT FAIL".** The failure-visibility half above is UNBUILT and
remains with Andrew — closing this entry must not be read as having delivered it.
