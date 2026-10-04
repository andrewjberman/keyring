# Deploy Completion Record
**Date opened:** 2026-10-04T22:34:33.702311+00:00
**Status:** OPEN
**Deploy:** AMGT_CORPUS round 36 CRPS-al-5: one code-only redeploy of opal-amgt-scoped-api at 288de3d95d carrying al-1 (model.fiscal_unresolved)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | base re-read live + build at 288de3d95d from the clean detached checkout | base aoQ+WrefJ / 1769 / auoGQqF5 unchanged; CONTENT-DIFF exactly CHANGED lib/research/api/scoped_amgt.py (356 files, 0 added, 0 removed); size under ceiling |  | OPEN |
| L1 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + ContentLength + content-sha256, re-read by head-object |  | OPEN |
| L2 | activation | opal-amgt-scoped-api code-only safe-apply | full-plan show -json: exactly 1 update (the function), 0 destroy/IAM/route/gateway; memory 1769; live CodeSha256 = the new build |  | OPEN |
| L3 | verify | al5_served.py --where deployed + aq-5's regression set (r64 c9-c14, r65 c17, r66 c18/c19/c22, r67 c23-c26, c15 cold, RANGE cold) | al5 deployed build 1/1 control 1/1; regressions unchanged vs aq-5's close |  | OPEN |

## Log

- 20261004T223433Z OPENED by 2.0.0_SA_COO~X with 4 leg(s)
