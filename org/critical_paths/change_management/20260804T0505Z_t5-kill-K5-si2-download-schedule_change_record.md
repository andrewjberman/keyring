# T5 DEAD-CONSUMER KILL K5 -- canonical-schwab-si2-download-schedule rule family (change record + rollback note)

**Executor:** 0.7.0_AE_CloudOps~F | **Opened:** 2026-08-04T05:05Z | **Status:** CLOSED 2026-08-04T05:12Z (destroy verified)
**Authorization:** COO GO 042634Z (CTO split-gate 042600Z, Andrew categorical). Kill-list row 12
@b877dbc0f5 (T1.A LEGACY-KILL-CANDIDATE nomination + 49F converter-ops Andrew-deprecation 07-30 context).

## WHAT DIES (all of `canonical-schwab-si2-schedule/schedule.tf`, 4 resources)
1. `aws_cloudwatch_event_rule.si2_download` (`canonical-schwab-si2-download-schedule`, DISABLED)
2. `aws_cloudwatch_event_target.si2_download`
3. `aws_iam_role.events_invoke_ssm` (`canonical-schwab-si2-events-ssm-role`)
4. `aws_iam_role_policy.events_invoke_ssm` (`send-command-si2-download`)

Root's `main.tf` (backend/provider + doc header) stays; the root remains valid with zero resources.

## WHY DEAD
- Rule: DISABLED in the 07-29 baseline AND live (T1.A) -- zero fires by state, superseded by the two
  per-account daily-pull rules (08242234 + 08335338), Andrew-deprecated family (07-30).
- Role + policy: sole consumer is the dead rule. **BLAST-CHECKED LIVE 2026-08-04T05:0xZ: both LIVE
  daily-pull rules target role `canonical-schwab-si2-daily-events-ssm-role` (a DIFFERENT role) --
  measured via list-targets-by-rule on all three rules.** Killing the rule while leaving its
  single-purpose role would manufacture a fresh row-17-class dead grant; they die together.

## MECHANISM + ROLLBACK
TF-managed, own root `infra/aws/terraform/canonical-schwab-si2-schedule/` -> whole-file source
removal + targeted safe-apply (4 destroys). Rollback: `git revert` + targeted apply (fully
source-declared). Historical definition at schedule.tf@5b54436a0.

## POST-KILL VERIFY (filled at close)
- `aws events describe-rule --name canonical-schwab-si2-download-schedule` -> ResourceNotFoundException: **CONFIRMED 05:11Z**;
  role NoSuchEntity CONFIRMED same minute. Apply: 0/0/4 destroyed (post terraform init -reconfigure;
  root backend needed re-init in this tree). State list post-apply: EMPTY.
- Both LIVE daily-pull rules still ENABLED post-apply: **CONFIRMED 05:11Z** (08242234 + 08335338 both
  `"State":"ENABLED"` -- the pre-kill blast-check held).
- Access window: the rule was DISABLED (zero possible fires since before 07-29); no further log
  evidence exists or is needed for a disabled trigger.
