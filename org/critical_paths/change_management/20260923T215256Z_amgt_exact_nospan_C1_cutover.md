# AMGT exact no-span C1 cutover

Status: CLOSED — C1 act completed and measured 2026-09-23T22:03:28Z. Opened 2026-09-23T21:52:56Z before any cloud write; opening commit `b0f33e7821`. C4 runtime acceptance remains pending separately.
Executor: `2.0.0_SA_COO~Z`.

Review update 2026-09-23T22:17:11Z: CTO25099 relays CVO record `4cb1b6b009`, C4 PASS. Pending-C4 statements below describe the execution-time handoff and are superseded by this review result. The guard remedy is complete; incident closure is withheld pending CVO's historical-gap remediation. E0 and the authenticated product thread remain ungraded. Boundaries: `AMGT_EXPERIENCE/C4_RELAY_RECEIPT.md`.

## Authority and bound act

Current AMGT closer mandate and direct Andrew authorization are recorded at `568f2f0c88`. CTO25083 explicitly directs this exact C1 sequence; CTO25085 prioritizes uploading the already-signed bytes as the first act. CTO half `83e9f90be5`, failure-policy amendment `3b4083a685`, COO half `5b455971f8`; CVO pre-deploy review `031fee04bc` passed, with C1-C5 execution conditions retained. No later source integration is within this package's signature.

The act changes S3 object `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`, then applies the harvest Terraform stack through `.tools/safe-apply.sh` to update only `module.scoped_amgt_api.aws_lambda_function.this` (`opal-amgt-scoped-api`). N=1 live Terraform declaration consumes this key; source `infra/aws/terraform/harvest/scoped-amgt-api.tf`. No ECS image/tag or task family consumes this ZIP. Served routes affected by its logic are thesis drafting sections and overlay description fallback. No IAM, configuration, routes, retained drafting objects or vendor writes are in scope.

## Artifact

- Existing file: `C:/tmp/amgt-r-no-span-package-20260923/candidate.zip`; never rebuild it.
- SHA256: `0c44108821fe52850c77b119490039453b082c3639fae6dbf58de054b1397a55`.
- Size: 807904 bytes; MD5 `cb90ed8636c79c9dbc29120923349bc5`.
- Required S3 `content-sha256` metadata and expected Lambda CodeSha256: `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=`.
- Expected original live CodeSha256: `r93CxQqrk8k8h2Q8KO4Iicn3pk8kyF4SFo47a9Cca5w=`; RevisionId `d906e911-aed5-4e21-afcd-0b9a6dcdbdc7`.

## Execution and stop rules

1. Freshly verify the original live hash and RevisionId, existing object, and exact candidate bytes before uploading. A RevisionId-only change stops for configuration/coverage re-review.
2. Upload exact bytes and required metadata; verify head-object size/metadata and independently downloaded bytes. Retain S3 VersionId in the completion evidence. No branch-tip builder.
3. Review a saved Terraform plan constrained to the named function/code artifact; refuse unrelated managed changes. Apply only through the canonical safe-apply wrapper. Any gate refusal halts and is reported without bypass.
4. Verify Lambda CodeSha256 and stored artifact agreement, then hand off the full C4 post-deploy battery to CVO: twelve GETs, 210 served/zero spanless, missing-firm negative control and both overlay controls. C4 and E0 are not implied by a successful apply.

The signed failure-policy correction controls: the old ZIP's hash is known, but it restores the known defect. No automatic code rollback to it. Fail closed/fix forward on the observed failure; an availability trade requires Andrew's contemporaneous decision. A halt leaves the exact measured artifact/function state recorded here and is escalated immediately.

## Observed execution

At opening no cloud write had occurred. Fresh baseline code hash and RevisionId matched. At 21:58:23Z the exact signed ZIP was uploaded; S3 VersionId `ZacA2Kn0CWoJqOFLvTPe2kzZ4x_ctTYe`, length 807904, ETag `cb90ed8636c79c9dbc29120923349bc5`, required content-sha256 metadata and independently downloaded bytes all matched. No rebuild was performed.

The saved incident-scoped Terraform plan had one in-place function update and only three changed attributes: `source_code_hash`, `s3_object_version`, and computed `last_modified`. Plan SHA256 `e087e85607f682576935cefedc1180c96e2dfe255a7c8523ab9363cea6207646`. Baseline live code hash and RevisionId were rechecked after plan review. Canonical `.tools/safe-apply.sh` applied that saved plan and exited 0: 0 added, 1 changed, 0 destroyed. The surfaced routine inbox used its documented `HALT_ACK=1`; no STOP, naming, tag-authz or tombstone override was set. Existing-name warnings remained warnings; tag-authz passed and tombstone gate was clean.

At 22:02:49Z Lambda was Active with LastUpdateStatus Successful; live CodeSha256 `DEQQiCH+UoUMd7EZSQA5RTsILDY5+ubb9Y3gVLE5elU=` matched signed candidate and S3 bytes/metadata. New RevisionId `3fe27dc6-15a0-428f-b084-dd54d98e3c76`. A full, untargeted post-apply plan showed zero resource changes; its exit 2 is solely the existing `scoped_amgt_route_keys` output update, which was not applied. No unrelated infrastructure mutation was performed.

Evidence: `AMGT_EXPERIENCE/C1_PREFLIGHT.json`, `C1_UPLOAD_RECEIPT.json`, `C1_UPLOAD.json`, `C1_PLAN_REVIEW.json`, `C1_VERIFY_DEPLOYED.json`, `C1_POSTAPPLY_PLAN.json`, and `C1_EXECUTION.md` in the COO deliverables home. CVO was asked at 22:03:14Z to run the full twelve-GET C4 battery, missing-firm negative control and both overlay controls. Closing this execution ledger does not close C4, E0, B08, Price or NO_COVERAGE acceptance.
