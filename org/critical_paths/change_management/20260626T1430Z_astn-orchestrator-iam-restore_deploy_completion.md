# Deploy Completion Ledger -- astn-wsjft orchestrator IAM restore

**Opened:** 2026-06-26T14:30Z | **Owner:** 0.5.0_AE_OpalETL | **Status:** CLOSED 2026-06-26T14:40Z
**Trigger:** Andrew-direct -- "did the ASTN brief go out to Austin this morning?" investigation.

## Problem (grounded)
The 06-26 3am-ET ASTN_WSJFT CEO brief did NOT send. Root cause (live CloudWatch logs,
/aws/lambda/astn-wsjft-orchestrator): the orchestrator Lambda fired on schedule but FAILED at
`_ec2.start_instances` -- `UnauthorizedOperation: astn-wsjft-orchestrator-role is not authorized
to perform ec2:StartInstances`. The EC2 runner never started -> no fetch -> no digest -> no SES
send. comp-iam reconcile: the role was missing all 8 modeled ops (declared in orchestrator.tf's
aws_iam_role_policy.orchestrator but NEVER APPLIED live = a half-landed deploy; Lambda code
shipped 06-25 13:08, policy never landed). No 06-25/06-26 audit artifacts in s3://opal-data-astn/email/.

## Legs
1. [DONE] Diagnose + ground root cause (logs + comp-iam + TF read).
2. [DONE] Forward last real brief (06-24 render) to andrew@ via SES (MessageId 0100019f0449049f-...).
3. [DONE] commit 58a2211 -- lifecycle ignore_changes=[associate_public_ip_address] on aws_instance.astn
   (the force-replace that bundled-blocked the targeted IAM apply; same drift class as etfs-reports).
4. [DONE] safe-apply astn-pipeline root (HALT_ACK=1) -- Apply complete: 0 added, 2 changed, 0
   destroyed; instance id UNCHANGED (i-059405dfefcb4b44a, no replace). role_policy + instance
   metadata in-place.
5. [DONE] Verify: AUTHORITATIVE live get-role-policy -> ec2:StartInstances/StopInstances +
   ssm:SendCommand/GetCommandInvocation/DescribeInstanceInformation + sns:Publish + s3:ListBucket +
   logs ALL present. Grant restored. (NOTE: comp-iam served a STALE all-MISSING snapshot post-apply
   -- it did not reflect the just-applied policy; live get-role-policy is ground truth. comp-iam
   freshness gap logged.)

## Residuals (benign, non-blocking)
- terraform plan -detailed-exitcode=2 remains, but the ONLY diff is the `astn_public_ip` OUTPUT
  refreshing "" -> live ephemeral IP (44.202.110.3). No resource add/change/destroy. Inherent to an
  ephemeral-IP start-on-demand host (the IP changes every stop/start) -- pre-existing, not introduced
  by this change, not worth chasing (moving target).
- Instance is currently running (launched 14:22:38Z, predates this apply -- NOT started by it). It is
  a 3am one-shot vehicle; the auto-shutdown enforcer owns stopping it (stopping EC2 = human-confirm
  per CLAUDE.md, so not actioned here).

## Validation
- IAM grant live-verified post-apply (authoritative get-role-policy). Fix landed.
- E2E (the real send) deferred to the scheduled 3am run tomorrow OR an Andrew-approved one-off
  recovery invoke (would send a mid-day brief to Austin). 4am absence-guard backstops a no-show.
  Asked Andrew which.

**Closed:** 2026-06-26T14:40Z -- IAM restore landed + live-verified. E2E validation gated on next
scheduled run / Andrew recovery-send decision.
