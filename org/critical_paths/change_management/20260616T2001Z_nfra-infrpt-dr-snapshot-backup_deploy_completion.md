# Deploy-completion ledger -- NFRA_INFRPT.DR infrastructure-daily-snapshot fix

**class:** deploy_completion
**status:** OPEN (deploy-start; targeted safe-apply pending)
**opened:** 20260616T2001Z
**closed:** --
**owner:** 0.7.0_AE_CloudOps~B
**project / TO:** NFRA_INFRPT / DR (fix the failing 2AM DR backup -- ACTIVE failure)
**authorization:** COO GO 191458Z (Andrew-direct, CTO-signed; doc-of-record docs/briefs/infra-report-revamp-proposal-20260616.md). DR-first fast-track.
**code commit:** (filled at commit -- shared-infra TF only; the Lambda code is UNCHANGED + already tracked)

## Root cause (from live CloudWatch logs + IAM policy simulation -- NOT guessed)
The `infrastructure-daily-snapshot` Lambda (EventBridge `infrastructure-snapshot-daily`, cron(0 7 * * ? *))
has NEVER produced a restore point -- first failure 2026-02-17T21:34Z, one minute after deploy. The report's
"failing 3/3" is its own 3-run lookback; the TRUE outage is ~4 months / 0 restore points ever. THREE
compounding failures:
1. **Target bucket `opal-infrastructure-snapshots` never existed** (404 HeadBucket / NoSuchBucket) -> the
   Lambda's save_to_s3 had no destination even if IAM were perfect.
2. **Lambda runs as the shared `opal-portal-lambda-role`, which was missing 16 of the 20 actions it needs**
   (policy-sim). The live error was `UnauthorizedOperation ec2:CreateImage on arn:aws:ec2:us-east-1::snapshot/*`
   -- the EC2SnapshotPermissions inline policy granted CreateImage but its Resource list had the account-less
   `image/*` form yet the ACCOUNT-SCOPED `snapshot/*` form; CreateImage authorizes the to-be-created backing
   snapshots against the ACCOUNT-LESS `snapshot/*` ARN -> deny. It also lacked CreateSnapshot (EBS leg) +
   s3:PutObject + iam/events/dynamodb/s3-config reads (every later component would also have failed; the
   handler re-raises on any component error).
3. **A purpose-built `infrastructure-snapshot-role` exists with the COMPLETE correct perms but is unused**
   (RoleLastUsed empty) -- the Lambda was simply wired to the wrong role. The Lambda + its EventBridge
   trigger are console orphans (source tracked at infra/aws/lambda/infrastructure-daily-snapshot/ +
   in the source map, but NOT in Terraform).

## Fix (this deploy -- minimal, certain, pure-Terraform; DR-restore now)
shared-infra TF, targeted apply:
- **s3.tf:** create `opal-infrastructure-snapshots` (versioning + AES256 SSE + public-access-block + 30-day
  manifest lifecycle = the code's stated retention).
- **main.tf:** fix `portal_lambda_ec2_snapshot` (EC2SnapshotPermissions) -> complete EC2 image/snapshot
  lifecycle on Resource="*" (the ARN-scoping was the bug; mirrors the proven dedicated role); + add
  `portal_lambda_snapshot_io` (InfraSnapshotIO) for the scoped S3 write + the iam/events/dynamodb/s3-config/
  lambda READS the 8 non-EC2 components need.
- Plan (targeted): **6 add, 1 change, 0 destroy.**

## Deferred to FOLLOW-UP (flagged to COO -- NOT this DR deploy)
- **Repoint the Lambda to the verified-complete `infrastructure-snapshot-role` + bring the orphan Lambda
  (and its EventBridge trigger) into Terraform** (repo packages Lambdas via CI-zip->S3->s3_key; needs a CI
  artifact, so it is a careful change, not a DR-fast-track move). This UNWINDS the shared-portal-role grant
  added here (removes IAM-read etc. from the portal surface) -> feed to P1 DRIFT.
- **No AMI / EBS-snapshot reaper:** once working, the Lambda creates an AMI + EBS snapshots DAILY for bd-/
  moltbot/seeking-alpha instances with NO cleanup (the 30-day S3 lifecycle governs only the manifests). This
  is a cost leak the moment DR starts working -> fast-follow (candidate P2 cost).

## Close criteria
- safe-apply 6/1/0 (HALTGT clear) + 0-diff re-plan; bucket exists.
- Controlled invoke SUCCEEDS + writes a FRESH restore point -- verify the ARTIFACTS land in
  s3://opal-infrastructure-snapshots/{date}/ (manifest.json + component JSONs + restore.sh) AND an AMI is
  created (false-clean class: rc=0 is NOT enough -- the artifact must exist).
- RAVC2 to COO. Finish-in-session.

## Rollback
Pure IAM + a new (empty) bucket; additive. Revert = `git revert` the TF commit + targeted destroy of the
new bucket if required. No existing resource modified destructively (EC2 policy = in-place widen of an
already-broken policy; reverting restores the prior broken state).
