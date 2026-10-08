# Deploy Completion Record
**Date opened:** 2026-10-08T18:58:50.741292+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261008T190826Z
**Deploy:** IB-pr-367 release applied: irpt-export-render repository.py + retention.py at pin a0d8d4943f (IRPT_BCKEND.TO-IB-pr-368), differential-replay regression check
**Authored by:** 0.9.0_WK_IRPT_BCKEND~176
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | baseline: live CodeSha256 03p2eIEKU9iSIOe5GYDbkbisapqAjULUyAPA/Wcxrfc= ; ROLLBACK SOURCE = s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip?versionId=FHKz88vjxHfi5uqADSw5GlQq8IULm615 | start sha + census changed_members=2 + replay committed d8d2fb723c | start CodeSha256 03p2eIEKU9iSIOe5GYDbkbisapqAjULUyAPA/Wcxrfc= re-read at start and before the build; rollback source s3 version FHKz88vjxHfi5uqADSw5GlQq8IULm615; release-census changed_members=2 (repository.py, retention.py); offline differential replay committed d8d2fb723c: ANALYSIS fixture under irpt-x10-v1 reserved by the live zip, live and built repository.get both ok with result_sha256 a7a8ae481b97..., altered policy_sha256 refused by both, suites 24+9+21 passed | CLOSED 20261008T190826Z |
| L2 | s3-prefix | build-and-upload investor-reporting irpt-export-render -> opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | built sha256 idanP8nX/mqaQ+FIGGY6AT4Xe/JxckOM3N0rWwivSh8= + new versionId | BUILD_ONLY and real build-and-upload.sh investor-reporting irpt-export-render: SHA256 idanP8nX/mqaQ+FIGGY6AT4Xe/JxckOM3N0rWwivSh8= (equals the packet), write VERIFIED size=407653, s3 version fHVzTZi4vdHmRqcy0KK1hmrQ_dcT1QkO; committed 89decedb33 | CLOSED 20261008T190826Z |
| L3 | activation | safe-apply of infra/aws/terraform/investor-reporting/export from the saved planfile; only code + object version, 0 to destroy | apply output + 0-diff re-plan | safe-apply from the saved planfile (plan text bc89a0fddf): Apply complete! Resources: 0 added, 1 changed, 0 destroyed; only module.irpt_export_render.aws_lambda_function.this s3_object_version and source_code_hash; comp-tagauthz PASSED, tombstone-gate CLEAN, no override used | CLOSED 20261008T190826Z |
| L4 | verify | equality reads: live CodeSha256 == built, re-plan 0, census changed_members=0, build residue removed | printed reads + IB81-1-AC1 PASS | live CodeSha256 idanP8nX/mqaQ+FIGGY6AT4Xe/JxckOM3N0rWwivSh8= == built, State Active, LastUpdateStatus Successful; terraform plan -detailed-exitcode rc=0 'No changes'; release-census changed_members=0; build residue none, git status porcelain empty; deploy recorded 94449e7a0d (source map + CHANGELOG.json) | CLOSED 20261008T190826Z |

## Log

- 20261008T185850Z OPENED by 0.9.0_WK_IRPT_BCKEND~176 with 4 leg(s)
- 20261008T190826Z LEG L1 closed: start CodeSha256 03p2eIEKU9iSIOe5GYDbkbisapqAjULUyAPA/Wcxrfc= re-read at start and before the build; rollback source s3 
- 20261008T190826Z LEG L2 closed: BUILD_ONLY and real build-and-upload.sh investor-reporting irpt-export-render: SHA256 idanP8nX/mqaQ+FIGGY6AT4Xe/JxckOM3N
- 20261008T190826Z LEG L3 closed: safe-apply from the saved planfile (plan text bc89a0fddf): Apply complete! Resources: 0 added, 1 changed, 0 destroyed; o
- 20261008T190826Z LEG L4 closed: live CodeSha256 idanP8nX/mqaQ+FIGGY6AT4Xe/JxckOM3N0rWwivSh8= == built, State Active, LastUpdateStatus Successful; terraf
- 20261008T190826Z CLOSED -- all 4 legs proven
