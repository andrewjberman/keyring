# AE_CloudOps~A Session Close — Lever A (cookie-first daily-OTP skip) DEPLOYED both firms (49F + cot)
**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, COORDINATE
**serial:** 0.7.0_AE_CloudOps~A  **window:** 2026-07-06 ~17:56Z -> ~19:56Z  **project:** ADVI_BDAPIMIG / ADVI_COTETL (Lever A)

## Summary
Andrew-direct #1 (via CTO+COO): BUILD + DEPLOY Lever A -- gate the daily BD session mint on a live
session-check so a still-live cookie SKIPS the redundant daily OTP mint. Delivered on BOTH firms:
- **49F/bd: COMPLETE** -- deployed, CVO exercise-gate PASS (4b4e802d3), ledger CLOSED.
- **cot: DEPLOY-COMPLETE** -- applied+verified+tagged; exercise-cert HELD to the rule-mandated 02:00Z
  cot daily (exercising now = an ad-hoc gold run, CLAUDE.md-forbidden). Ledger open (annotated/extended).

## MCP traffic (~30 messages; significant only)
- CTO: TOP-priority build spec (5 binding conditions + pre-granted arch-gate); pre-affirmed 49F design;
  ruled Option-1 -target on the SNS drift; 49F VALIDATED + cot GREENLIT + cot -target GO.
- COO (deploy-lane owner): authorized both ledgers; RETRACTED an exercise-now rec (rule-violating, owned
  it); ruled reserved=3 KEEP+codify-TF; dispositioned the dedup sweep (Finding-2 GO, 1+3 -> Andrew).
- CVO (exercise-gate): 49F PASS (independently grounded); requested force-pull; ruled cot (b) natural-belt
  on the no-ad-hoc-gold-run rule; cot cert HELD-PENDING-natural-daily.

## Compiler Tools
| tool | run | result | note |
|---|---|---|---|
| ds-commit-gate.sh | on both edited Lambdas (49f + cot) | PASS | py_compile+AST+ruff py39 clean, both |
| comp-iam service | bd-49f-session-trigger; cot-bd-session-trigger | PASS | all ops GRANTED, ZERO new (skip path reuses existing sids) both firms |
| comp-which | routed the "which bd Lambdas mint/run" question | PARTIAL | near-tie; fell back to source-map + Read for the grounding |
| comp-pipescript deployed | bd-49f-session-trigger | N/A | tool covers gold/silver/bronze data scripts, not Lambdas (expected) |
- **What worked:** comp-iam confirmed zero-new-perms on both skip paths (the load-bearing "no IAM change" claim) -- reused InvokeRunner/ReadSessionForCheck/ModeMarker (49f) + bronze-run/session-check (cot) sids.
- **What failed:** none blocking.
- **Gap found:** none new.

## AE Deployment Sequence + Verification (ACTUAL output)
**49F/bd** (bd-v2.48.0):
- code f29c77864 -> source-map 804f66020 (sha 84GG->EOOu) -> `safe-apply -target=module.bd_49f_session_trigger.aws_lambda_function.this`: `Apply complete! Resources: 0 added, 1 changed, 0 destroyed.`
- Rule-22a APPLIED: live `get-function-configuration CodeSha256 = EOOuJMrkSkfj5Tl9dYHFnFbh8c/5jAgShS/V6NCy+N4=` == uploaded (LastModified 18:53:18Z); targeted re-plan `No changes.`
- tag bd-v2.48.0 @804f66020 pushed; record-terraform-deploy 4a5423498; ledger CLOSED (all 4 legs).
- Exercise #1 (live, 19:00Z Event-safe single invoke): session-trigger logged `Lever A: cookie POSITIVE-live -> SKIP mint, direct-invoke bd-49f-runner status=202`; runner `auth OK ... zero OTP`, `_BRONZE_COMPLETE.json` emitted, fired ONCE. CVO PASS 4b4e802d3.

**cot** (cot-pipeline-v0.7.0):
- code acd86f96e -> source-map fc23df2eb (sha jVnve5->7dJLylE7ps) -> `safe-apply -target=module.cot_bd_session_trigger.aws_lambda_function.this`: `Apply complete! 0 added, 1 changed, 0 destroyed.`
- Rule-22a APPLIED: live `CodeSha256 = 7dJLylE7psMM95J8Y8vxhckpX9aNIidvh9ZY7Du7mu0=` (LastModified 19:31:56Z); targeted re-plan `No changes.`
- tag cot-pipeline-v0.7.0 @fc23df2eb pushed; record 5ff4bd035; ledger L1-L3 CLOSED, L4 OPEN (belt).

## INCIDENT (self-inflicted, owned + closed)
CVO-requested force-pull ran as `aws lambda invoke` RequestResponse (sync). The runner takes ~3-4min >
the AWS CLI 60s Read-timeout -> botocore default-retry -> **5 overlapping bd-49f-runner executions**
(retry storm) -> BD 401'd 3 of 4 tables (bearer-token, NOT cookie-death). Contained: `put-function-concurrency
0` (stop) -> drained (ConcurrentExecutions 0) -> restored `reserved=3` (delete-to-unreserved is HARNESS-GATED).
Ground-truth: cookie LIVE post-storm (session-check true), daily 07-06 bronze INTACT (non-destructive, no
sentinel emitted -> no spurious silver), no alarm paged Andrew. transactions freshly re-pulled (LastModified
advanced) = partial fresh-pull proof. Lesson banked: memory/reference_long_lambda_invoke_must_be_event_not_requestresponse.

## Files Modified
see commit messages: f29c77864, 804f66020, acd86f96e, fc23df2eb (the two Lambda code + source-map).
- infra/aws/lambda/bd-pipeline/bd-49f-session-trigger/lambda_function.py -- +_fire_runner()+_session_is_positive_live()+pre-gate in _handle_session_refresh.
- infra/aws/lambda/cot-pipeline/cot-bd-session-trigger/lambda_function.py -- +_handle_bronze_run()+_session_is_positive_live()+pre-gate.
- 2 deploy ledgers (org/critical_paths/change_management/): 49F (CLOSED) + cot (OPEN, annotated).

## Current State (zero-context handoff)
- **Both Lever A Lambdas LIVE in prod.** 49F: bd-49f-session-trigger @ hash EOOuJMrkSk (bd-v2.48.0). cot:
  cot-bd-session-trigger @ hash 7dJLylE7ps (cot-pipeline-v0.7.0). Skip logic: on the daily session-refresh
  cron, if session-check probes POSITIVE-live -> skip the OTP mint. 49f skip = direct lam.invoke(runner);
  cot skip = direct bronze-run SSM (box still starts, only OIDC-login skipped). FAIL-SAFE: any doubt -> full
  mint. SINGLE-FIRE structural (skip emits no session-fetch-SSM -> the session-complete rule never fires).
- **49F ledger:** org/critical_paths/change_management/20260706T1852Z_bd-49f-lever-a...md = CLOSED.
- **cot ledger:** 20260706T1931Z_cot-lever-a...md = OPEN, L1-L3 closed, L4 (CVO exercise-gate) held to the
  02:00Z cot daily; window extended to 7.5h (~03:00Z) + Status annotated EXPECTED-OPEN/NOT-stranded.
- **bd-49f-runner reserved-concurrency = 3** (was UNRESERVED; TF drift -- KEEP+codify per CTO/COO).
- **Two un-applied SNS-email-sub drifts** (declared-never-applied): bd-49f-interim.tf:52, cot-detection-layer.tf:48
  (both -> andrew@opalinvest.com). Held out of both -target applies; Andrew GO'd applying but with an anti-sprawl
  quality bar (CONFIRMED-not-Pending + 3-axis-functional + canonical/de-duplicated).
- **Dedup sweep done (read-only):** the cookie-alerts topics are firm-HEALTH aggregators (49F 14 alarms / cot 9),
  not single cookie-death alarms; cot has an overlap dedup target (bd-cot-authtoken-dead, parity w/ 49F's
  already-retired bd-49f-authtoken-dead b649eacf0). COO: Finding-2 GO, Findings 1+3 -> Andrew scope/channel.

## Next Steps
- **[0.7.0_AE_CloudOps~A]** After the 02:00Z cot daily: pull cot-bd-session-trigger + box run logs, confirm
  SKIP-not-mint (dispatched opal-cot-bronze-run NOT opal-cot-bd-session-fetch, zero OIDC-login) + fresh bronze
  -> RAVC COO+CVO -> CVO 3-axis cert -> close cot L4 + ledger. Also confirm the 49F 00:00Z belt (skip-not-mint).
- **[0.7.0_AE_CloudOps~A]** Post-cot-cert, sequence the reconciliation applies (COO-gated): bd (reserved=3 codify)
  + cot (retire bd-cot-authtoken-dead); SNS email-subs HELD pending Andrew's scope+channel ruling. Plan-verified,
  ledgered, deploy-check asserts SubscriptionArn != PendingConfirmation, CVO 3-axis certs.
- **[3.0.0_SA_CVO]** cot exercise-gate cert on the 02:00Z natural daily (served/bronze fresh + zero-login,
  independently). 49F belt: all-4-fresh via skip on the 00:00Z daily.
- **[2.0.0_SA_COO]** Track 2 drift-reconciliations + bundle the Andrew scope/channel ask (cookie-alert bar).

## Blockers
None assumption-blocked. The cot exercise-cert is gated on the scheduled 02:00Z daily -- a HARD EXTERNAL GATE
that CLAUDE.md MANDATES over an ad-hoc run (the one legal defer, not a stall). The SNS-sub applies are gated on
Andrew's scope/channel ruling (named owner, concrete trigger). Deploy is COMPLETE + fail-safe-bounded meanwhile.
