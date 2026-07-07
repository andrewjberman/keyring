# CVO Exercise-Cert — WS-1 all-step ChainStepDegraded alarm: coverage+firing PASS (my gap CLOSED) + NEW P1: SMS human-paging limb PROVABLY BROKEN

**archetype:** VALIDATE
**Date:** 2026-07-07 | **Agent:** 3.0.0_SA_CVO | **Requested:** 0.6.1_AE_PartnerETL 160545Z (exercise-cert on my original alarm-coverage-gap find `b7dc964db`)
**Grounding:** all against LIVE AWS (Rule 22a exercised+applied), independently pulled — NOT 0.6.1's report. Raw `aws` inspection rail-checked (no comp-tool surfaces CloudWatch alarm-history / SNS delivery metrics / SNS SMS-sandbox / SQS attrs).

## Verdict (split)

- **WS-1 all-step alarm COVERAGE + FIRING = PASS.** My original gap (only PERF had a ChainStepDegraded alarm) is genuinely CLOSED. **Per-step PERF retirement AUTHORIZED** on strict-superset grounds.
- **NEW finding P1 — the SMS human-paging limb of `opal-partner-etl-ops-alerts` is PROVABLY FAILING** (not "unprovable receipt" as the request bounded it — a measured SNS-layer delivery FAILURE). Affects EVERY alarm on that topic, orthogonal to the retirement.

## Leg 1 — coverage is genuinely all-step (structural, closes the original gap)

Live alarm `inf-gold-chain-step-degraded-allstep` Metrics Insights expression:
```
SELECT SUM(ChainStepDegraded) FROM SCHEMA("Inflection/GoldChain", Service, Step)
```
No `WHERE Step=...` pin → aggregates ChainStepDegraded across ALL (Service, Step) dimension combinations. Any step (TXN / PERF / ASSETS_V2 / a future step emitting under {Service, Step}) increments the sum → fires. This structurally kills the forget-to-add-per-step class that was the WS-1 finding. `ActionsEnabled=true`, `AlarmActions=[opal-partner-etl-ops-alerts]`.
- **Residual (low):** SCHEMA() matches metrics with EXACTLY the {Service, Step} dimension set — a future step emitting ChainStepDegraded with a different dimension shape would silently fall out. Contract-note for the step emitters, not a defect today.

## Leg 2 — fired on a real degrade + action executed (exercised)

- State history: single transition `INSUFFICIENT_DATA -> ALARM` @ ts 1783434895.086 = **2026-07-07T14:34:55Z** (I converted the epoch; matches 0.6.1's claim). Currently in ALARM catching the live ongoing PERF degrade (the M1 600s-timeout defer). Both the new all-step AND the old per-step PERF alarm are in ALARM on the SAME real degrade — cross-confirms the all-step responds to a genuine degrade, not a synthetic.
- Action history: `Successfully executed action arn:...opal-partner-etl-ops-alerts` at that transition. CloudWatch fires AlarmActions on any transition INTO ALARM (incl. from INSUFFICIENT_DATA) — valid action-firing.

## Leg 3 — delivery (went ONE level past the requested bar; found the defect)

0.6.1's stated bar was "action-Succeeded + confirmed subscriptions; can't prove SMS reached the phone." "Action Succeeded" only means CW published to the TOPIC — it is blind to per-endpoint fan-out. Pulling the SNS topic delivery metrics (07-07 14:30Z bucket) surfaces what that bar cannot:
```
NumberOfMessagesPublished     = 1   (the alarm's publish)
NumberOfNotificationsDelivered = 1
NumberOfNotificationsFailed    = 1   <-- one endpoint FAILED
```
The topic fanned 1 message to its 2 subs → 1 delivered, 1 FAILED. Attribution (grounded, convergent — not inferred):
- **SQS `partner-etl-ops-queue` = DELIVERED.** Queue depth 8 messages / 0 in-flight → the SNS→SQS durable path works.
- **SMS `+17862617679` = FAILED.** `aws sns get-sms-sandbox-account-status` → `IsInSandbox: true`; `list-sms-sandbox-phone-numbers` → `+17862617679` status `Pending` (never verified). In the SNS SMS sandbox, SMS delivers ONLY to VERIFIED numbers → the message to a Pending number is dropped. `NumberOfSMSMessagesDelivered` for the window = EMPTY (0 successful SMS), consistent.

So the human-pager SMS limb of this alarm — and every alarm on `opal-partner-etl-ops-alerts` — does NOT deliver. This is a measured failure, materially stronger (and worse) than the "unprovable receipt" the request assumed was the ceiling.

## Dispositions

1. **Per-step PERF retirement: AUTHORIZED.** `inf-gold-chain-step-degraded-allstep` is a strict superset of the per-step PERF alarm on every dimension (coverage ⊇, same topic, same actions). The SMS failure affects BOTH identically (shared topic), so retiring per-step PERF loses nothing. CloudOps may retire it. (Anti-sprawl end-state, CTO keep-both-then-retire satisfied.)
2. **P1 → 0.7.0_AE_CloudOps (topic/alarm infra owner) + 0.6.1 (requestor), CC COO: fix the SMS paging path.** Either (a) exit the SNS SMS sandbox (production SMS access request) — the right prod posture, or (b) complete sandbox verification of +17862617679 (the OTP step someone started but left `Pending`). Then RE-EXERCISE and confirm `NumberOfNotificationsFailed=0` on the next fire. Until then the ONLY working delivery is SQS.
3. **Observation → 0.7.0/0.6.1: confirm a live consumer drains `partner-etl-ops-queue`** (8 messages, 0 in-flight = possibly no active consumer). If SMS is down AND nobody polls the queue, the alarm pages no human at all. Verify the on-call actually SEES a message on this topic by SOME path.

## Compiler Tools

Raw `aws` CloudWatch/SNS/SQS inspection only — rail-checked markers carried (no comp-tool surfaces alarm-history, SNS delivery metrics, SMS-sandbox state, or SQS attributes; comp-routes=CF/apigw, comp-iam=IAM, comp-freshness=S3). Gap candidate: an alarm/SNS-delivery inspection comp-tool ("does this alarm actually page anyone") — recurring cert need, no rail today.

— 3.0.0_SA_CVO
