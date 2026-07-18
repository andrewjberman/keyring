# Deferred-item ledger -- globgrph alert resources HELD pending Andrew alert-phase-change

**Status:** DEFERRED-TO-POST-CONSOLIDATION (committed-but-unapplied; NOT a deploy, NOT stranded -- a deliberate indefinite hold). This is a HELD-item record, not a deploy-completion ledger (named `_deferred_item.md` so the `--red` half-landed scan does not treat a deliberate hold as an open deploy).
**Owner:** 0.7.0_AE_CloudOps
**Authorization:** Andrew-direct 2026-07-17 (SES/SNS/CloudWatch alert-suspension during the consolidation) + CTO ruling 200739Z. Memory: `feedback_suspend_new_alert_systems_during_consolidation`.
**Opened:** 2026-07-17 ~20:08Z

## >> ADDENDUM 2026-07-18 ~00:1xZ -- RESOURCE #1 (coevolution twin) SUBSUMED into the L5 freshness-teardown <<

The freshness-alarm teardown (Andrew clean-house; CTO P1) L5-globgrph leg **DELETED the entire
`infra/aws/terraform/globgrph/freshness_alarm.tf` mechanism** (commit **22becbb76**, applied 44-destroy).
Resource #1 below (the coevolution twin) was a **registry entry inside that file's
`freshness_producer_registry`**, so it was removed WITH the file -- it is no longer a
"committed-but-unapplied registry entry awaiting a standalone globgrph apply." **Its re-arm is now a
`git revert` of the L5 teardown commit 22becbb76** (which restores freshness_alarm.tf including the twin's
registry entry), NOT a standalone globgrph apply. Nothing was applied for it; the twin never went live.
**Resource #2 (the andrew@ critical-surface subscription, item2c) is UNCHANGED -- still parked
committed-but-unapplied** (item2c_surface_alarm.tf was NOT touched by L5; the L5 -target apply explicitly
EXCLUDED `aws_sns_topic_subscription.critical_surface_alerts_email`, which remains a config-ahead-of-state
create that stays unapplied). The shared `opal-critical-surface-alerts` topic SURVIVES.

## What is held + WHY

Andrew-direct: be very parsimonious/judicious about SES/SNS alert systems; SUSPEND creating NEW alert infrastructure during OPAL_CONSOLIDATION / OPAL_TAXONOMY (most current alerts are useless / for deprecated assets / miscalibrated / assigned to mid-migration surfaces). A freshness/staleness alarm on a mid-consolidation surface is precisely the suspended class. The two resources below are committed to the repo but were **held from apply** (I stopped the CTO-sequenced globgrph apply when Andrew's directive landed). This note exists so they are (a) not lost and (b) not silently applied on some future globgrph `terraform apply`.

## Held resources (2)

| # | Resource (TF address) | File / commit | Class | Reopens under |
|---|---|---|---|---|
| 1 | `aws_cloudwatch_metric_alarm.freshness_stale["fedobs_coevolution_snap_last_append"]` + its additive wiring (`WATCH_TARGETS` entry on `aws_lambda_function.freshness_alarm` and `aws_lambda_function.freeze_monitor`; `aws_iam_role_policy.freshness_alarm_read`) | `infra/aws/terraform/globgrph/freshness_alarm.tf` -- committed **0.8.0_AE_CloudComp base @85a4b4e00** | Freshness/staleness ALARM on a mid-consolidation surface (globgrph coevolution feed). The producer it watches is live+healthy; only the ALARM half is parked. | OPAL_TAXONOMY absence-twin phase, at Andrew's alert-phase-change. |
| 2 | `aws_sns_topic_subscription.critical_surface_alerts_email` -> `andrew@opalinvest.com` (companion `aws_sns_topic_subscription.critical_surface_alerts_sms` -> `+1786...7679`, same file, non-delivering SMS sandbox) | `infra/aws/terraform/globgrph/item2c_surface_alarm.tf` -- committed **0.8.0_AE_CloudComp~Z @9369f7451** | SES/SNS egress on the D8 `opal-critical-surface-alerts` topic (SEV1/SEV2 critical-surface findings). | **D8 / NFRA_GRAPHS critical-surface decision (its OWN lane), NOT a globgrph-apply.** |

## DISENTANGLEMENT (per CTO 200739Z)

Resource #2 is **NOT part of 0.8.0's coevolution twin.** It is **D8 critical-surface-alerts egress -- 0.7.0_AE_CloudOps's own NFRA_GRAPHS lane** (topic `opal-critical-surface-alerts`, item2c_surface_alarm.tf header attributes the D8 design to 0.7.0, 2026-06-12). It got **bundled into the globgrph terraform plan by accident** via ~Z's TF-staging commit 9369f7451. When Andrew reopens the alert phase, resource #2 must ride the **D8 critical-surface decision on its own merits**, NOT go live as a side effect of whatever globgrph apply happens to run next. Resources #1 and #2 are independent reopen decisions.

## RISK / control-of-record

Both resources live in the **`infra/aws/terraform/globgrph`** terraform state. A future unqualified `terraform apply -chdir=infra/aws/terraform/globgrph` **would apply them** unless the plan is read and these are excluded/targeted. Per Andrew's alert-suspension (which includes NOT adding new gates), **no blocking gate is added** -- this ledger note is the control-of-record. **Anyone applying globgrph before Andrew's alert-phase-change MUST read the plan and confirm these two do not ride it.**

## Door-6 emitter twin (related, separately routed)

CTO is asking Andrew whether the `opal-assets-daily-emitter` absence twin (the Door-6 completion-signal producer; highest-consequence untwinned producer -- silent stop -> mdpf never fires -> nothing pages, census D.2) warrants an **exception** to the suspension. Until Andrew rules, it stays DEFERRED with the rest. **Do NOT build it** pending Andrew's word.

## Reopen conditions

Andrew signals the consolidation reached the alert-phase. Then: resource #1 rides the OPAL_TAXONOMY absence-twin phase; resource #2 rides the D8 critical-surface decision. Neither applies before then.
