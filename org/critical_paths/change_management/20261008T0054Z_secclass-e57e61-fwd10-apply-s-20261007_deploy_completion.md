# Deploy Completion Record
**Date opened:** 2026-10-08T00:54:09.291312+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS SC-e-57 + SC-e-61 (FWD-10): rebuild and apply the producer Lambda mdpf-secclass-new-security-lambda at dell1 CLOUD 2082b8b4bc, so the producer stops writing a GICS sector into sub_asset_class (e57) and keeps writing US stocks (e61). Issuer GO 2.0.0_SA_COO~M1 msg 699; e65-close coupling RELEASED by issuer ruling msg 710 (the 23:00Z E_18 run finished: run_id 4fa82436148e, exit 0 at 00:06:47Z, 0 etf-classifications rows written). CTO half @bdfdc93b0d, COO half NEVER_WIDEN_HALF_REQUEST_SECCLASS_FWD10_SECTOR_OUT_20261007.md. BEFORE READS, all three measured 2026-10-08T00:5xZ and all equal to the order's expectations: live function CodeSha256 f0zhRV1FFFiVgnNMsEzYAGap8qCOWbb4xgZgpx8RIdQ= (LastModified 2026-10-05T20:03:05Z); artifact s3://opal-313476888478-lambda-artifacts/mdpf-secclass/mdpf-secclass-new-security-lambda.zip IsLatest VersionId 2DwW9a.Pz6G7A1o.wSTshxZGZzFCVw5b (ETag 83ae407090a1a39582ee55184986a8e3, 39519 B, LastModified 2026-10-05T20:00:57Z); that object's content-sha256 metadata equals the live CodeSha256, so deployed bytes and artifact bytes agreed before the act. STEP 1 blob reads at dell1 CLOUD: infra/aws/lambda/v2_portal/_shared/rivalfunds_classification.py = d3363dba79d59a1b421ca3b1d432ef395d5b447a, infra/aws/lambda/mdpf-secclass/new-security-classifier/lambda_function.py = e025665470078c9ef5e1aa7599d25510d4798d36; both MATCH the order. STEP 2 timing: acted at ~00:5xZ, outside the producer's 13:45Z-14:15Z cron window. ROLLBACK, one command pair: aws s3api copy-object --bucket opal-313476888478-lambda-artifacts --key mdpf-secclass/mdpf-secclass-new-security-lambda.zip --copy-source 'opal-313476888478-lambda-artifacts/mdpf-secclass/mdpf-secclass-new-security-lambda.zip?versionId=2DwW9a.Pz6G7A1o.wSTshxZGZzFCVw5b' --metadata-directive COPY, then CHECKPOINT_DISABLE=1 .tools/safe-apply.sh on infra/aws/terraform/mdpf-secclass/new-security-classifier to put CodeSha256 back to f0zhRV1FFFiVgnNMsEzYAGap8qCOWbb4xgZgpx8RIdQ=. BLAST RADIUS: this one function only; no IAM, no schedule, no layer, no table write, no other root.
**Authored by:** 0.7.0_AE_CloudOps~SD
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 14.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts mdpf-secclass/mdpf-secclass-new-security-lambda.zip -- the rebuilt artifact replaces the object; prior IsLatest VersionId 2DwW9a.Pz6G7A1o.wSTshxZGZzFCVw5b is the rollback source | build-and-upload.sh output plus head-object showing a new VersionId and a content-sha256 metadata value different from f0zhRV1FFFiVgnNMsEzYAGap8qCOWbb4xgZgpx8RIdQ= |  | OPEN |
| L2 | activation | mdpf-secclass-new-security-lambda -- ONE safe-apply under CHECKPOINT_DISABLE=1 on infra/aws/terraform/mdpf-secclass/new-security-classifier; the plan must read 0 to add / 1 to change / 0 to destroy with source_code_hash the only attribute | the plan lines, the apply line, a 0-diff re-plan, and AC1 'E57E61-LIVE ok=True' from R12_CHECKS/e57e61_lambda_sha_check.py |  | OPEN |
| L3 | verify | the next producer run, 2026-10-08T14:00Z (cron(0 10 ? * MON-FRI *) America/New_York) -- CTO half acceptance 2: on a day whose plan lists US stocks, the US rows written count must be above 0, else SAME-DAY rollback per this entry | the run's log, the listing under OUTPUT_PREFIX, and the US rows written count reported to 2.0.0_SA_COO~M1 |  | OPEN |

## Log

- 20261008T005409Z OPENED by 0.7.0_AE_CloudOps~SD with 3 leg(s)
