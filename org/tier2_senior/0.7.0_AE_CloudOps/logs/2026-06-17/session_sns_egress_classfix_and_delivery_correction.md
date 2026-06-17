# SNS-egress class-fix + the delivery-layer correction (0.7.0_AE_CloudOps~B)

**archetype:** DIAGNOSE
**secondary_archetypes:** DEPLOY, IMPLEMENT, VALIDATE, COORDINATE

Window: since the convergence-close log (97a39687d, ~21:21Z) -> ~23:21Z. Lane: 0.7.0_AE_CloudOps~B.
Trigger: COO /drive URGENT redirect (Andrew: fabric driving, not parked) -> SNS-egress 0-sub fix.

## Current State

The SNS monitoring-egress class is now fixed + detected to the DELIVERY layer (not just sub-confirmed). The headline is a CORRECTION I caught of my own work + a deeper estate-wide root cause.

THE CORRECTION (own it): I had RAVC'd opal-critical-surface-alerts egress "fixed + verified -- pages the phone." That was WRONG -- I verified subscription-CONFIRMED + publish-ACCEPTED (MessageId), NOT the DELIVERY metric. Doing the find-insure-budget egress-verify properly (NumberOfNotificationsDelivered) exposed it: critical-surface Delivered=0/Failed=1. The D8 SMS page did NOT reach the phone.

ROOT CAUSE (estate-wide, account-level): SNS SMS IsInSandbox=True + MonthlySpendLimit=$1 -> SMS delivers ONLY to verified numbers -> EVERY confirmed SMS sub is NON-DELIVERING (critical-surface, find-insure-budget, + the pre-existing opal-infrastructure-alerts / ec2-long-running). "Confirmed subscription" != "delivers."

FIX (COO ruling 230358Z = option B, EMAIL):
- Added email subs (andrew@opalinvest.com) to critical-surface (globgrph item2c) + find-insure-budget (imo sns.tf var-default binding). SES email is non-sandboxed + the monitor's proven channel. Both PendingConfirmation -> ANDREW one-time click-confirms (his tomorrow item). SMS subs RETAINED (non-delivering) until email confirms, then dropped.
- DELIVERY-VERIFY deferred to TOMORROW (after Andrew confirms): test publish -> NumberOfNotificationsDelivered>0. Will NOT claim verified until that metric is >0.
- (A) SMS sandbox-lift routed to Andrew (durable SMS fix; account-level/AWS-support).

DETECTION HARDENED (the durable class-fix; shared-infra-v1.30.0): check_sns_egress now verifies DELIVERY-capability. A topic whose only confirmed subs are SMS while SMS is sandboxed -> deliverable=0 -> flagged NON-DELIVERING (RED), not OK. Queries get-sms-sandbox-account-status (IAM sns:GetSMSSandboxAccountStatus, simulate-confirmed allowed). Verified in-Lambda (archive 23-16-11): 4 RED (the 2 new + the 2 pre-existing SMS topics), inf-otp OK (lambda sub), trade-ses WATCH (0-sub intentional). sms_sandboxed currently reads None = IAM-propagation lag to the Lambda role-session creds (perm correct per simulate; resolves next report; detection flags correctly via fail-toward-visible meanwhile).

ALSO this window (before the sandbox discovery): the 0-sub DETECTION itself (check_sns_egress base, shared-infra-v1.29.0); the critical-surface SMS sub + find-insure-budget SMS sub (both later superseded by email); smartx default-tags reconcile (Option A: Pipeline=smartx preserved + Project=OpalPortal, verified on the instance -- cleared the smartx drift); a real KMS find (find_insure_data_key granted only root + the Lambda role, not the SNS service -> SSE-SNS delivery would fail even with a subscriber; added the scoped SNS-service grant -- though moot vs the sandbox, it was a genuine second gap).

## Compiler Tools

| Tool | Invocation | Result | Note |
|---|---|---|---|
| aws sns list-topics/list-subscriptions-by-topic | estate 0-sub census | PASS | 9 topics; found 4 0-sub then the deeper SMS-sandbox layer |
| aws sns get-sms-sandbox-account-status | account SMS status | PASS | IsInSandbox=True -- the load-bearing root cause |
| aws cloudwatch get-metric-statistics | NumberOfNotificationsDelivered/Failed | PASS | the DELIVERY-layer verify (caught Delivered=0/Failed=1) |
| aws iam simulate-principal-policy | sns:GetSMSSandboxAccountStatus | PASS | allowed -> the None is propagation, not a perm bug |
| ds-commit-gate.sh / comp-iam gaps | lambda_function.py / iam | PASS | clean each |
| safe-apply.sh | globgrph + imo + shared-infra (xN) | PASS | email subs + KMS grant + IAM + Lambda code; 0-destroy |
| record-terraform-deploy.sh | shared-infra-v1.29.0 + v1.30.0 | PASS | |

**What worked:** the egress-verify discipline taken to the DELIVERY metric caught my own premature "verified" + the estate-wide SMS-sandbox root cause; the detection hardened to the delivery layer (fail-toward-visible so it flags even when the sandbox-read lags); IAM simulate confirmed the perm (None = propagation, not a bug) rather than assuming. **What failed:** my initial critical-surface "verified" stopped at sub+publish (the exact egress-not-verified class) -- corrected loudly. **Gap:** Andrew's email-confirm (tomorrow) gates the final delivery-verify; sms_sandboxed-read propagation to confirm next report.

## Blockers

None blocking me. The delivery-verify is GATED on Andrew's one-time email-confirm (tomorrow, non-urgent -- D8 clean tonight per CTO). The (A) sandbox-lift is Andrew/AWS-support.

## Next Steps

- **[Andrew]** One-time click-confirm the 2 SNS email subs (critical-surface + find-insure-budget); decide (A) SMS sandbox-lift (durable SMS fix).
- **[0.7.0_AE_CloudOps~B]** TOMORROW: after Andrew confirms -> test publish -> verify NumberOfNotificationsDelivered>0 -> drop the non-delivering SMS subs -> RAVC2 the delivery metric. Confirm sms_sandboxed reads on the next report.
- **[2.0.0_SA_COO]** Route the 2 pre-existing SMS-only topics (opal-infrastructure-alerts/ec2-long-running, not my lane) now surfaced by the hardened detection.

## Files Modified

See commit messages: the egress-B commit (globgrph item2c email + imo sns.tf var + lambda_function.py detection hardening + shared-infra infra-monitor.tf IAM), the KMS-grant commits (imo kms.tf), the 0-sub-detection + critical-surface/find-insure SMS commits (superseded by email). Deploys: shared-infra-v1.29.0 (0-sub detection) + v1.30.0 (delivery-layer hardening + email channel).
