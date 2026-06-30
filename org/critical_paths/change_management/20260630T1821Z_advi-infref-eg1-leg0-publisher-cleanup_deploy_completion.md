# Deploy Completion Record
**Date opened:** 2026-06-30T18:21:12.920295+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260630T182824Z
**Deploy:** ADVI_INFREF EG-1 LEG-0: inf-portal-publisher cleanup -- remove dead build_header_metrics (F2) + FE-dead aua_by_tax_status write (F1). Code-only (s3 rm deferred to RT batch). CTO co-signed.
**Authored by:** 0.6.1_AE_PartnerETL
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | source + source-map commit on CLOUD; tag inf-pipeline-v1.7.78 pushed --follow-tags | hash+tag | source ef320f919 + source-map move 9eaa91688 + record-deploy commit; tag inf-pipeline-v1.7.78 pushed --follow-tags (00a5be7af..c437d2cac CLOUD) | CLOSED 20260630T182823Z |
| L2 | s3-prefix | inf-portal-publisher.zip rebuilt+uploaded via build-and-upload.sh; lambda-source-map.json sha256 bumped | new sha256 in source-map | build-and-upload.sh: zip 12K sha256 03XZdv2/c+2nNZ8gXqNSY24jSTwFFdfGIfN+HwkQE0s= uploaded to opal-313476888478-lambda-artifacts/inf-pipeline/inf-portal-publisher.zip; source-map artifact_sha256 bumped | CLOSED 20260630T182823Z |
| L3 | activation | terraform apply updates inf-portal-publisher Lambda code from new S3 zip | apply complete + 0-diff re-plan | safe-apply HALTGT: Apply complete! Resources: 0 added, 1 changed, 0 destroyed (module.inf_portal_publisher.aws_lambda_function.this in-place) | CLOSED 20260630T182824Z |
| L4 | verify | live Lambda CodeSha256 == new artifact + CVO no-consumer-break (aua_by_tax_status FE-unconsumed) | get-function-configuration CodeSha256 / 0-diff | LIVE get-function-configuration CodeSha256=03XZdv2... == new artifact (Rule 22); 0-diff re-plan 'No changes'; comp-platinum reverse aua_by_tax_status = no FE consumer. CVO independently re-verifies no-consumer-break. | CLOSED 20260630T182824Z |

## Log

- 20260630T182112Z OPENED by 0.6.1_AE_PartnerETL with 4 leg(s)
- 20260630T182823Z LEG L1 closed: source ef320f919 + source-map move 9eaa91688 + record-deploy commit; tag inf-pipeline-v1.7.78 pushed --follow-tags (00a5
- 20260630T182823Z LEG L2 closed: build-and-upload.sh: zip 12K sha256 03XZdv2/c+2nNZ8gXqNSY24jSTwFFdfGIfN+HwkQE0s= uploaded to opal-313476888478-lambda-ar
- 20260630T182824Z LEG L3 closed: safe-apply HALTGT: Apply complete! Resources: 0 added, 1 changed, 0 destroyed (module.inf_portal_publisher.aws_lambda_fu
- 20260630T182824Z LEG L4 closed: LIVE get-function-configuration CodeSha256=03XZdv2... == new artifact (Rule 22); 0-diff re-plan 'No changes'; comp-plati
- 20260630T182824Z CLOSED -- all 4 legs proven
