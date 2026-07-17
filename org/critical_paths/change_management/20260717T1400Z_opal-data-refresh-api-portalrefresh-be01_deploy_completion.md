# Deploy-Completion Ledger -- opal-data-refresh-api (TO_PORTALREFRESH_BE_01 F1-F4)

**Status:** COMPLETE
**Closed:** 2026-07-17T14:33Z
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
- [x] 1. Source committed (commit-gate)
- [x] 2. build-and-upload.sh data-refresh opal-data-refresh-api
- [x] 3. terraform plan (expect: lambda update from new S3 version, nothing else)
- [x] 4. safe-apply
- [x] 5. 0-diff plan
- [x] 6. record-terraform-deploy + tag + push --follow-tags
- [x] 7. Behavior verify (Rule 22a): (a) version-restore path fires with manifestKey logged;
        (b) concurrent rollback 409s; (c) F4 -- next real authenticated portal action writes a
        history row with the real email (corrected-pkl upload doubles as evidence).

## Rollback surface
Previous artifact version retained in S3 (versioned artifacts bucket); revert = re-point
s3_object_version via terraform to prior version / re-upload prior zip + apply.

## Closure evidence (exercised, 2026-07-17 14:1x-14:3xZ)
- Commit 05980fae1 (+ source map 2513b9954, deploy record, tag data-refresh-v2.3.0, 0-diff plan).
- Runtime import + F4: GET history invoke w/ API-GW-v2 nested authorizer -> log "Lambda authorizer
  context: email=be01-verify@opalinvest.dev" (no dev fallback). Official F4 acceptance = next REAL
  authenticated portal action (synthetic-event caveat per CTO history warning, honored).
- F1: rollback exec-7cccfb6a354b -> method=version-based, manifestKey=data-refresh/archive/
  53a06944-3aee-41f7-9aa0-eba586e4d0c2/outputs-manifest.json, 99 files, CF I7U5BSI1E0I9ONV6OMXEV2WSBR.
  Byte-identical restore of current state (chosen so the exercise could not move served data).
- F2: concurrent rollback during RUNNING 20260717_v1-3b05edbf -> 409 REJECTED_ALREADY_RUNNING with
  running_execution payload (contract v1.1 shape, DE ACK 135735Z).
- F3/fallback (c): synthetic row exec-be01c-fallback (arn=pending, current-vintage inputs) ->
  method=re-processing, exec-7837877a78c0, pipeline SUCCEEDED, served verified identical
  (data_as_of 2026-07-16, ST YTD 1.86/vol 3.3); synthetic row deleted post-test.
- Lane note: commits under audited GIT_COMMIT_AUTHOR_OVERRIDE=CLOUD_OPS_OR_ETL (CTO TO 56b9d938d
  assigns this AE-lane Lambda to 0.2.0_DT; enumeration gap surfaced to CTO in closure).
