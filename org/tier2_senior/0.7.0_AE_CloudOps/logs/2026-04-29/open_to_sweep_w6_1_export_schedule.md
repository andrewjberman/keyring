# Session Log — Open TO Sweep + W6.1 Daily Orion Export Schedule

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-29
**GO:** Andrew (direct, "lets just get these knocked out")
**Status:** COMPLETE
**Tag:** `inf-pipeline-v1.7.0`

**Commits:**
- `da364ed0a` — Lambda source: inf-jwt-trigger export mode
- `9c370a07e` — TF: eventbridge.tf + iam.tf + lambdas.tf + source-map (W6.1)
- `2ce73fba7` — ci: record deploy inf-pipeline @ 9c370a07 [skip ci]

---

## Scope

Andrew directive: full sweep of open AE TOs after extended retirement/Node22 work. Two threads:

1. **Build:** ADVI_INFLEC.W6.1 — daily Orion export EventBridge schedule at 5pm ET.
2. **Cleanup:** Verify which staged TOs were actually done in prior sessions but had stale status fields, close them out so the queue reflects reality.

---

## W6.1 Build — Daily Orion Export Trigger

### Architecture decision

Existing inf-jwt-trigger Lambda already starts inf-exporter EC2 daily at 12:13 UTC for JWT refresh. Two options for the 5pm export trigger:

- (a) Create a new dedicated Lambda `inf-export-trigger`
- (b) Extend inf-jwt-trigger to handle a second mode via event payload

Chose (b). Cleaner — no duplicate Lambda code, no duplicate IAM role, and the EC2 lifecycle logic (state checks, polling) is shared. Mode is selected by the EventBridge target's `input` field passing `{"mode": "export"}`.

### Code changes

`infra/aws/lambda/inf-pipeline/inf-jwt-trigger/lambda_function.py`:
- `lambda_handler` reads `event.get('mode', 'jwt-extract')` — default preserves existing JWT renewal behavior.
- New `_handle_export()` path: write mode marker, ensure EC2 running (start if stopped, poll up to 8 min for `running`), send SSM RunCommand `opal-inf-export-run`.
- New `_send_export_command()` issues SSM with 3600s document timeout.
- New `_wait_for_running()` polls every 15s with 480s deadline.

### Infrastructure changes

`infra/aws/terraform/inf-pipeline/`:
- `eventbridge.tf`: new `aws_cloudwatch_event_rule.inf_export_schedule` cron(0 21 * * ? *) targeting `module.inf_jwt_trigger.function_arn` with `input = jsonencode({mode = "export"})`
- `iam.tf`: added `SendExportCommand` statement to `inf_jwt_trigger_policy` granting `ssm:SendCommand` on `document/opal-inf-export-run` + `instance/${inf_exporter.id}`
- `lambdas.tf`: bumped `inf_jwt_trigger` timeout 30s → 600s (export mode polls EC2 boot); new `aws_lambda_permission.eventbridge_inf_export_schedule`

### Plan + apply

```
Plan: 3 to add, 2 to change, 0 to destroy.
  + aws_cloudwatch_event_rule.inf_export_schedule
  + aws_cloudwatch_event_target.inf_export_schedule_target
  + aws_lambda_permission.eventbridge_inf_export_schedule
  ~ aws_iam_role_policy.inf_jwt_trigger_policy (SendExportCommand statement added)
  ~ module.inf_jwt_trigger.aws_lambda_function.this (timeout + s3_object_version + source_code_hash)

Apply complete! Resources: 3 added, 2 changed, 0 destroyed.
0-diff plan confirmed.
```

### DST behavior

Schedule fixed at 21:00 UTC. Resolves to:
- 5:00 PM EDT (mid-March → early November)
- 4:00 PM EST (early November → mid-March)

Most of the trading year is EDT, so the 5pm ET intent is met for ~8 months. EventBridge does not natively handle DST. Per Andrew confirmation, fixed UTC is acceptable.

---

## TO Closures — Stale Status Audit

Confirmed what's in AWS / TF / source vs what TOs claim. Closed 21 TOs that were observably done in prior sessions:

| TO | Closure evidence |
|---|---|
| `TRSB_PATHFIX.TO-1` | All 12 `/api/general/trades/*` routes present with CUSTOM+naqxlm. `trade-pipeline-v1.6.0` already tagged. |
| `TRSB_PATHFIX.TO-3` | All 9 spec emails (austin/adam/yang/lauren/menachem/manav/aj/andrew/alyssa) verified in SES. Production-access form is non-AE action — Andrew owns. |
| `ADVI_INFLEC.W1.1` | `opal-data-inf` bucket exists, TF-managed, mirrors opal-data-bd layout. |
| `ADVI_INFLEC.W1.3` | `FIRM#inflection` row exists in `opal-users-v2` (SK=META, written by AE 2026-04-21; TO had wrong key spec). |
| `ADVI_INFLEC.W1.4` | `opal-partner-inflection` table ACTIVE, PAY_PER_REQUEST, PK=email, GSI=ByAdvisorRole. |
| `ADVI_INFLEC.W1.6` | `'inflection': 'inf'` present in auth-validator-edge FIRM_BUCKET_MAP (commit `c9f6c7e6d`); deployed via portal-auth `f2718822` / v1.15.0. |
| `ADVI_INFLEC.W1.7` | Same — shared-advisor-router FIRM_BUCKET_MAP, paired commit. |
| `ADVI_INFLEC.W1.9` | All 4 inf-* services in EC2_MANIFEST.json. |
| `ADVI_INFLEC.W2.1` | `inf-gold-layer-runner` i-0ed5afded2ebd4ed4 active. |
| `ADVI_INFLEC.W2.2` | `inf-gold-trigger` Lambda module deployed. |
| `ADVI_INFLEC.W2.3` | All 3 publisher modules (inf-portal-publisher, inf-portal-advisor-publisher, inf-client-detail) deployed. |
| `ADVI_INFLEC.W2.4` | `inf-exporter` i-081ae6aafb394fb1a active. |
| `ADVI_INFLEC.W2.5` | OTP relay function URL live (`swk4gc6kd7k3osowr3464l7u540exjbp.lambda-url`). |
| `ADVI_INFLEC.W2.6` | Orion sign-in selectors confirmed (commit `b1e19d51a`). |
| `ADVI_INFLEC.W2.7` | `orion_export.ts` shipped (commit `510f5798e` W3.B). |
| `ADVI_INFLEC.W2.8` | Daily JWT cron + manual SSM dispatches validate end-to-end. |
| `ADVI_INFLEC.W6.1` | This session — see above. |
| `ADVI_INFLEC.W6.3` | `inf-otp-alert` SNS topic + exporter SNS:Publish IAM (commit `554785087` W6.2 batch). |
| `ADVI_INFLEC.W6.4` | OTP relay form (mobile web) deployed (commit `a2dd1e335` W3.B pivot). |
| `ADVI_INFLEC.ORNREN.002` | EC2_MANIFEST `dispatch_script` already points to `s3://opal-data-inf/code/gold/orion-gold-dispatch.sh` for both inf-gold-layer-runner + inf-gold-qa-runner. DS ORNREN.001 + AE rewire shipped earlier. |

---

## Side Quest — user@inflection.com Initial Account

Andrew requested first real Inflection account. Two writes per ONBOARDING.md §2:

- `opal-users-v2` `USER#user@inflection.com` PROFILE row — bcrypt2b hash of `inflection2026`, role=user, tier=advisor, firmId=inflection, mustChangePassword=false
- `opal-partner-inflection` row — email=user@inflection.com, advisorKey=inflection_user, advisorRole=architect, firmRole=admin

Both writes succeeded with `attribute_not_exists` condition.

---

## Remaining Open TOs (still genuinely staged or blocked)

- `TRSB_TFIMPT.W3` — staged, requires API GW import to Terraform. Real work, not yet done.
- `ADHC_COMPIL.004` — staged, gates on ADHC_COMPIL.003 (CTO/DS scope, not in AE queue).
- `ADHC_COMPIL.007` — staged + optional, gates on ADHC_COMPIL.006 (CTO/DS scope).
- Lambda@Edge Node22 Wave B — deferred from earlier session, awaiting GO from Andrew/CTO.

---

## Compiler Tool Runs

None — all changes were straightforward TF + Lambda source. No new IAM consumers (only one new statement on existing role), no new portal routes, no schema changes.
