# Deploy Completion Record
**Date opened:** 2026-09-26T08:44:38.514587+00:00
**Status:** OPEN
**Deploy:** opal-assets-silver-etf rebuilt from CLOUD HEAD so the TrueShares holdings converter runs in production (NFRA_MCPINDEX MX-s-3)
**Authored by:** 0.7.0_AE_CloudOps~I
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: re-vendored 8 modules + BUILD_MANIFEST.json vendor_sha256 | commit hash of the source change and of its drain |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-silver-etf.zip | build-and-upload.sh verified-write line (head-object ContentLength == local size AND content-sha256 metadata == this build's sha) |  | OPEN |
| L3 | activation | module.silver_converter["etf"].aws_lambda_function.this via .tools/safe-apply.sh | get-function-configuration CodeSha256 == the new artifact content-sha256, LastModified after the apply |  | OPEN |
| L4 | verify | terraform plan re-run after apply | 0-diff (No changes) on infra/aws/terraform/opal-assets |  | OPEN |
| L5 | verify | deployed import-health smoke on the live function | invoke returns no Runtime.ImportModuleError and the handler imports etf_conversion |  | OPEN |
| L6 | git | infra/aws/lambda/ci/lambda-source-map.json artifact_sha256 + the ledger close | commit hash |  | OPEN |
| opal-assets-silver-etf | tf-lambda | module.silver_converter["etf"].aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20260926T084438Z OPENED by 0.7.0_AE_CloudOps~I with 7 leg(s)

## Blast radius and rollback per key (NEVER-2; measured BEFORE the act, not predicted from shape)

**WRITE SET -- exactly two objects. Anything else in the plan is a STOP.**

1. `s3://opal-313476888478-lambda-artifacts/opal-assets/opal-assets-silver-etf.zip` (bucket is VERSIONED).
   PRE-ACT, read at 2026-09-26T08:3xZ via `s3api head-object`:
     VersionId       prXNS9i0cDwKGWlFPhbwER.0tMof8kGj
     content-sha256  a14fYacwkjPlkj7P5qb7QGTKDeQ2A9GTnkM/t1rTxcs=
     ContentLength   51829
     LastModified    2026-07-15T23:22:38+00:00
   ROLLBACK: `s3api copy-object` that VersionId back over the same key, re-setting
   `--metadata content-sha256=a14fYacwkjPlkj7P5qb7QGTKDeQ2A9GTnkM/t1rTxcs= --metadata-directive REPLACE`,
   then re-run safe-apply. The old bytes are never deleted -- versioning is the rollback.

2. Lambda `opal-assets-silver-etf`. PRE-ACT, `get-function-configuration`:
     CodeSha256   a14fYacwkjPlkj7P5qb7QGTKDeQ2A9GTnkM/t1rTxcs=   (== the artifact's, so deployed == artifact)
     LastModified 2026-07-15T23:24:02.000+0000
     CodeSize 51829 | Runtime python3.11 | Memory 1024 | Timeout 900
   ROLLBACK: restore (1), then safe-apply.

**NOT TOUCHED, and why it cannot be.** The other six silver families (orion, eclipse, blackdiamond,
schwab, smartx, bd49finsurance) each carry their OWN `artifact_key` -- `opal-assets/opal-assets-silver-
<family>.zip` (silver.tf, module "silver_converter", for_each over local.silver_families). Rebuilding
etf's key cannot move theirs, EVEN THOUGH THEY VENDOR THE SAME mirror-framework modules from the same
repo source; each keeps the bytes it was last built from until it is rebuilt on its own motion. That is
the standing drift this order does not close and does not widen to.

**No env-var row.** `etf` is absent from `local.silver_build_commit` (only `schwab` is in that map), so
the `contains(keys(...))` merge contributes nothing for this family and the environment block does not
move. No schedule, event rule, IAM role, layer or the `aws_s3_bucket_notification.monolith_bronze`
singleton is in this act.

**EXPECTED PLAN, BOTH BRANCHES, read from the producer's own rule (modules/yang-lambda/main.tf:
`s3_object_version = data.aws_s3_object.artifact.version_id`, `source_code_hash =
data.aws_s3_object.artifact.metadata["content-sha256"]`):**
  - PASS branch: exactly ONE in-place update, `module.silver_converter["etf"].aws_lambda_function.this`,
    with `s3_object_version` and `source_code_hash` changing and nothing else. 0 to add, 1 to change,
    0 to destroy.
  - STOP branch: any other resource named, or any destroy -> NO APPLY, a BLOCKING surprise row, and this
    ledger goes to HELD rather than CLOSE. TO bound 1 makes this refusal, not a judgment call.

**Grant delta: NONE, measured.** `comp-iam service opal-assets-silver-etf` reads "No AWS operations
detected" -- it parses only `lambda_function.py`, so that is a FLOOR and not an answer. The answer is the
call-surface diff between the OLD vendored bytes (753fe90fb1^) and the NEW (HEAD) across all 9 files:
services added NONE, calls added NONE, calls removed NONE; both sides read the same 4
(`get_object`, `get_paginator`, `head_object`, `put_object`). No new grant need, so no BLOCKING row.
