# Deploy-Completion Ledger -- opal-data-refresh-api (TO_PORTALREFRESH_BE_01 F1-F4)

**Status:** OPEN
**Opened:** 2026-07-17T14:00Z
**Owner:** 0.2.0_DT_PortfolioAnalytics
**Lambda:** opal-data-refresh-api (pipeline: data-refresh)
**TO:** TO_PORTALREFRESH_BE_01 @56b9d938d (CTO; F4 pulled forward 135518Z, batch judged safe)

## Scope (one file: infra/aws/lambda/data_refresh/lambda_function.py)
- F1: rollback manifest seam join -- resolve SFN pipeline_execution_id from DDB executionArn
  (describe_execution -> input), read UUID-keyed outputs-manifest first, exec-keyed legacy path
  as fallback read, re-processing as explicit degraded path; restore logs + returns manifestKey.
- F2: server-side already-running guard on rollback -- 409 REJECTED_ALREADY_RUNNING /
  REJECTED_STATE_UNVERIFIABLE (fail-closed). Contract v1.1 ACK'd by 0.2.0_DE 135735Z.
- F3: no-emoji/non-ASCII cleanup in deployed prints + comments.
- F4: validate_user_type reads API GW v2 nested authorizer context (authorizer.lambda.email)
  ahead of top-level; kills the 100pct dev@test.com fallback. + Rule-23 docstring email swap.

## Legs
- [ ] 1. Source committed (commit-gate)
- [ ] 2. build-and-upload.sh data-refresh opal-data-refresh-api
- [ ] 3. terraform plan (expect: lambda update from new S3 version, nothing else)
- [ ] 4. safe-apply
- [ ] 5. 0-diff plan
- [ ] 6. record-terraform-deploy + tag + push --follow-tags
- [ ] 7. Behavior verify (Rule 22a): (a) version-restore path fires with manifestKey logged;
        (b) concurrent rollback 409s; (c) F4 -- next real authenticated portal action writes a
        history row with the real email (corrected-pkl upload doubles as evidence).

## Rollback surface
Previous artifact version retained in S3 (versioned artifacts bucket); revert = re-point
s3_object_version via terraform to prior version / re-upload prior zip + apply.
