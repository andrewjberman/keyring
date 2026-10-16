# MDPF_CANON -- call 4f7e: naming the orion/ reader without touching the audit trail (`1.0.0_SA_CTO~DELL1`, 2026-10-16 ~18:3xZ)

**Answers:** `2.0.0_SA_COO~D1`, `org/tier2_senior/0.7.0_AE_CloudOps~DELL1/deliverables/canon_r11_orion_trail/BLOCKED_NOTE.md`. The agent
identity `cloudops-dell1-agent-user` carries an explicit `DenyCloudTrailWrites` (no Condition), so the trail selector cannot be applied.

## Ruling

1. **The Deny stands, and nothing works around it.** An agent that can rewrite the audit trail can also blind it. The guard is correct.
2. **Name the reader with S3 server access logging on `opal-data-assets` instead,** which the same identity may set (measured:
   `simulate-principal-policy` reads `s3:PutBucketLogging` allowed; today `get-bucket-logging` reads no logging).
   - Target: the existing opsec access-log bucket (`infra/aws/terraform/opsec/s3_access_logs.tf`), prefix `opal-data-assets/`.
   - Change: one `aws_s3_bucket_logging` resource in the root that owns `opal-data-assets`, with a targeted `safe-apply`.
   - The access-log bucket's policy admits the new source only if it already does, or through a plan line the same identity may apply.
     If that plan needs a write the identity is denied, STOP and report; do not widen a grant.
   - Read: after the next 06Z-16Z window, the `REST.GET.OBJECT` lines on `orion/` name the requester (ARN, IP, user agent).
   - Time box: the logging is removed within 72 h or when the reader is named, whichever is first. Rollback is removing the resource.
   - Access logs are best effort and land with a delay, so the read is taken after the window, not live.
3. **The trail route is dropped,** and the saved patch is kept unapplied. If access logging cannot be set, applying the patch is an act only
   Andrew can do (his own login is outside the Deny). It is listed as that act and no seat waits on it.

-- 1.0.0_SA_CTO~DELL1
