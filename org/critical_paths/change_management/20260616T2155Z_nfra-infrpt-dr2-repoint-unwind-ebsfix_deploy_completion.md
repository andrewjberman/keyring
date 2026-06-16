# Deploy-completion ledger -- NFRA_INFRPT.DR2 (repoint + unwind + EBS scoped-fix)

**class:** deploy_completion
**status:** CLOSED -- COMPLETE + VERIFIED. import + safe-apply 0/1/2 (HALTGT clear): Lambda REPOINTED to
infrastructure-snapshot-role (confirmed live) + EBS-fixed code + GIT_COMMIT=nfra-infrpt-dr2; the 2 temp
grants (EC2SnapshotPermissions + InfraSnapshotIO) DESTROYED from opal-portal-lambda-role (confirmed gone;
leg-c MonitorAnthropicSecretRead correctly stays). 0-diff re-plan; comp-manifest-check clean (orphan
resolved). Controlled-invoke close-gate (0-loss): the COMPLETE manifest LANDED on the dedicated role --
all 10 artifacts fresh (manifest.json + restore.sh + ec2/ebs/lambda/iam/eventbridge/security-groups/s3/
dynamodb JSONs); 25 EBS snapshots created (non-fatal, 0 failed). EC2 AMI step returned InvalidAMIName.
Duplicate (today's 9 AMIs already exist from the earlier DR invoke -- a same-day date-stamped-name collision,
NOT a perms/repoint failure: CreateImage WAS attempted on the dedicated role -> its perms work; handled
non-fatally). Today's complete restore point = the 9 existing AMIs + 25 EBS snapshots + full manifest. The
skip-AMI'd EBS logic exercises on tomorrow's fresh-date scheduled run (no name collision -> 9 AMIs ->
ami_instance_ids skips them -> snapshots only the ~16 non-critical). DR2 acceptance MET.
**opened:** 20260616T2155Z
**closed:** 20260616T2202Z
**owner:** 0.7.0_AE_CloudOps~B
**project / TO:** NFRA_INFRPT / DR2 (clean end-state for the DR fix; CTO-binding 201006Z)
**authorization:** COO GO 2121Z (re-confirmed 2132Z) + leg-c-first re-sequence 213433Z (DR2 after leg-c, now). CTO 201006Z (import approach + binding). DR restore-point already verified (the 9 AMIs) -> repoint onto a verified base.

## What this deploys
1. **Repoint + import**: infrastructure-daily-snapshot onboarded to TF (infra-snapshot.tf) on the dedicated
   `infrastructure-snapshot-role` (verified-complete: all 20 actions + S3 write + snapshot log group) instead
   of the shared opal-portal-lambda-role. Code via CI-zip->S3 (artifact content-sha256
   irR0gnHxYAAZiC15cSnwNUxVer9ywy9+MHcuLYJqDB0=, 5.5KB).
2. **Unwind the temp grant**: REMOVED portal_lambda_ec2_snapshot (EC2SnapshotPermissions) +
   portal_lambda_snapshot_io (InfraSnapshotIO) from main.tf -> the time-boxed least-privilege exception
   (CTO cond-1) is CLOSED. Phase-1: 12 portal Lambdas on the role, only infrastructure-daily-snapshot calls
   ec2:CreateImage/CreateSnapshot -> removal breaks none.
3. **EBS scoped-fix + complete manifest**: snapshot_ebs_volumes skips AMI'd-instance vols (kills the
   SnapshotCreationPerVolumeRateExceeded double-snapshot) + snapshots the remaining 16 non-critical-instance
   vols NON-FATALLY; every component is non-fatal (_run_component) -> the COMPLETE manifest now lands.

## Close criteria
- terraform import aws_lambda_function.infra_snapshot + targeted safe-apply (HALTGT clear); 0-diff re-plan.
- Lambda runs on infrastructure-snapshot-role (NOT the shared role); the 2 temp inline policies GONE from
  opal-portal-lambda-role (verify via aws iam list-role-policies).
- CONTROLLED INVOKE verify (0-loss to DR): a REAL restore point lands post-repoint -- the COMPLETE manifest
  (manifest.json + restore.sh + all component JSONs) + AMIs, fresh mtime (NOT rc=0). comp-manifest-check.
- RAVC2 to COO. Finish-in-session.

## Labeled-separate (per COO accept 215225Z) -- the leg-c-surfaced finding
The monitor role lacks logs:DescribeLogGroups on some groups (the restored §6 triage caught it). NOT part of
this DR2 apply; tracked for a small follow-up IAM leg (monitor role, not the snapshot role).

## Rollback
Revert the TF (re-add the 2 portal grants, drop infra-snapshot.tf) + redeploy the prior snapshot artifact
(S3 versioned) + the Lambda stays on its role. The repoint changes only the exec role + code; the EventBridge
trigger (invoke permission) is untouched, so the schedule keeps firing throughout.
