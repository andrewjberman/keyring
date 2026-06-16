# Deploy-completion ledger -- NFRA_INFRPT.DR infrastructure-daily-snapshot fix

**class:** deploy_completion
**status:** CLOSED -- TF DEPLOY COMPLETE + VERIFIED (infra root cause RESOLVED). DR capability SUBSTANTIALLY restored (9 instance AMIs + ec2-instances.json now land where 0 restore points existed for ~4mo). COMPLETE manifest still gated by a SECOND, DISTINCT pre-existing CODE bug (EBS per-volume rate limit) -> tracked under the CTO-gated repoint/import follow-up. NOT a stranded deploy leg (the TF apply finished cleanly).
**opened:** 20260616T2001Z
**closed:** 20260616T2012Z
**owner:** 0.7.0_AE_CloudOps~B
**project / TO:** NFRA_INFRPT / DR (fix the failing 2AM DR backup -- ACTIVE failure)
**authorization:** COO GO 191458Z (Andrew-direct, CTO-signed; doc-of-record docs/briefs/infra-report-revamp-proposal-20260616.md) + COO PROCEED 200756Z (no STOP; minimal pure-TF fix endorsed; shared-role grant accepted as EXPLICITLY TEMPORARY pending the priority repoint). DR-first fast-track.
**code commit:** f6c905fdb (shared-infra TF only; the Lambda code is UNCHANGED + already tracked at infra/aws/lambda/infrastructure-daily-snapshot/). Pushed origin/CLOUD.

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

## Time-boxed least-privilege exception (CTO 201006Z condition 1)
The EC2-snapshot + IAM/events/dynamodb/s3-config-read grant added to the SHARED opal-portal-lambda-role
(EC2SnapshotPermissions widened + new InfraSnapshotIO) is an EXPLICIT, TRACKED, TIME-BOXED least-privilege
exception -- NOT a quiet permanent state. It modestly widens the portal-serving role's blast radius
(notably iam:ListRoles/GetRolePolicy). It is UNWOUND by DR2 (repoint the Lambda to the dedicated
infrastructure-snapshot-role + bring the orphan Lambda into TF), which COO is authoring now and which GOes
on this DR's restore-point RAVC2. Owner to confirm removal of these two inline policies at DR2 close.

## Apply + smoke-test evidence (20260616T2007Z)
- safe-apply: **6 added, 1 changed, 0 destroyed** (HALTGT clear). Targeted 0-diff re-plan = "No changes."
- IAM policy-sim post-apply: all 16 previously-denied actions now ALLOWED; s3:PutObject to the bucket ALLOWED.
- Controlled DR smoke (CTO-authorized one-time manual invoke -- backup-verification, not a gold run):
  - INFRA ROOT CAUSE RESOLVED + PROVEN: the run got PAST the original blocker (CreateImage) into the EBS step.
    **9 instance AMIs created** (ami-097c50029d3db668c etc.; bd-/moltbot/seeking-alpha; state pending) +
    **s3://opal-infrastructure-snapshots/2026-06-16/ec2-instances.json (27594 B, fresh mtime) LANDED.**
    This is REAL restore capability where there were ZERO restore points for ~4 months.
  - **BUT the COMPLETE manifest did NOT land** -- a SECOND, DISTINCT, pre-existing CODE bug surfaced (latent
    until now because the Lambda never got past step 1): `snapshot_ebs_volumes` (lambda_function.py:206)
    calls `ec2.create_snapshot` on volumes that step-1's `create_image` JUST snapshotted (AMI backing snaps),
    with NO backoff -> `SnapshotCreationPerVolumeRateExceeded` -> the handler RE-RAISES on any component
    error -> manifest.json + the remaining 7 component JSONs never written. STRUCTURAL (recurs every run, not
    transient -- did NOT burn more AMIs re-confirming). This is the false-clean class CTO condition 2 guards.
- DR close-gate status: PARTIAL. AMIs (the primary rollback artifact) + ec2-instances.json landed; the
  COMPLETE manifest is gated on the EBS code fix, which is Rule-1-coupled to the DR2 import (same operation).
  Sequencing conflict surfaced to COO/CTO in the restore-point RAVC2; resolution TBD (fold EBS code fix into
  DR2 + land complete manifest there). The TF DEPLOY itself is COMPLETE + verified (no stranded leg).

- VOLUME-COVERAGE (CTO false-clean condition, answered 202526Z): **0 detached/standalone volumes** (25 total,
  0 available) -> CTO's literal standalone axis is CLEAN. HONEST RESIDUAL: the skipped snapshot_ebs_volumes
  step also covered **16 of 25 volumes attached to 16 NON-critical instances** (the dead SmartX EC2
  i-06ebcb27395eb3f49 / the OPLMCP gw i-01d75141177c88b96 / ~14 agent-service EC2s) that the 9 AMIs do NOT
  cover (AMIs = the 9 critical bd-/moltbot/seeking-alpha instances + their attached vols only). So the (a)
  close stands on the 9 AMIs as PRIMARY restore (9 critical instances restorable NOW), but those 16
  non-critical-instance volumes are a **KNOWN DR2-PENDING coverage item** (NOT a silent omission). They had
  0 coverage for the entire ~4-mo outage anyway (DR-fix = 0 -> 9-critical-now, full on DR2). DR2 is LOCKED as
  the SCOPED FIX (COO 202656Z): (1) skip AMI'd-instance volumes (kills the double-snapshot rate-limit + cost)
  + (2) snapshot the remaining 16 + any future detached NON-FATALLY -> restores full volume coverage + lands
  the complete manifest. NOT a remove (remove would silently drop the 16).

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
