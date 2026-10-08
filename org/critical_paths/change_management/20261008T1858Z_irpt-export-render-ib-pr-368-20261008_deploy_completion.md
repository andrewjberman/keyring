# Deploy Completion Record
**Date opened:** 2026-10-08T18:58:50.741292+00:00
**Status:** OPEN
**Deploy:** IB-pr-367 release applied: irpt-export-render repository.py + retention.py at pin a0d8d4943f (IRPT_BCKEND.TO-IB-pr-368), differential-replay regression check
**Authored by:** 0.9.0_WK_IRPT_BCKEND~176
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | baseline: live CodeSha256 03p2eIEKU9iSIOe5GYDbkbisapqAjULUyAPA/Wcxrfc= ; ROLLBACK SOURCE = s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip?versionId=FHKz88vjxHfi5uqADSw5GlQq8IULm615 | start sha + census changed_members=2 + replay committed d8d2fb723c |  | OPEN |
| L2 | s3-prefix | build-and-upload investor-reporting irpt-export-render -> opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | built sha256 idanP8nX/mqaQ+FIGGY6AT4Xe/JxckOM3N0rWwivSh8= + new versionId |  | OPEN |
| L3 | activation | safe-apply of infra/aws/terraform/investor-reporting/export from the saved planfile; only code + object version, 0 to destroy | apply output + 0-diff re-plan |  | OPEN |
| L4 | verify | equality reads: live CodeSha256 == built, re-plan 0, census changed_members=0, build residue removed | printed reads + IB81-1-AC1 PASS |  | OPEN |

## Log

- 20261008T185850Z OPENED by 0.9.0_WK_IRPT_BCKEND~176 with 4 leg(s)
