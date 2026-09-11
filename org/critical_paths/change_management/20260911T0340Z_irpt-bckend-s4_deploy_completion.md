# Deploy Completion Record
**Date opened:** 2026-09-11T03:40:08.103743+00:00
**Status:** OPEN
**Deploy:** IRPT IB-s-4: irpt-directory-refresh Lambda + its two roles + the ENABLED irpt-directory-refresh schedule in the directory root
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | wk-irpt_bckend-1-2 source commit for refresh.py, expiry.py, schedule.tf and the source-map registration | commit hash on the worker branch (LOCAL, never pushed) |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-directory-refresh.zip | head-object ContentLength + content-sha256 metadata == the sha build-and-upload computed over the built zip |  | OPEN |
| L3 | activation | terraform apply of infra/aws/terraform/investor-reporting/directory (state key investor-reporting/directory/tfstate) adding irpt-directory-refresh, its role, the scheduler role and the ENABLED schedule | safe-apply output showing ADDED only, with 0 changed and 0 destroyed so IB-s-1 and IB-s-12 resources are untouched |  | OPEN |
| L4 | activation | the irpt-directory-refresh EventBridge schedule, ENABLED | aws scheduler get-schedule State ENABLED + the declared expression and timezone |  | OPEN |
| L5 | verify | 0-diff terraform plan on the directory root (criterion S4-AC2) and the served CodeSha256 against the artifact metadata | plan No changes + CodeSha256 == content-sha256 |  | OPEN |

## Log

- 20260911T034008Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 5 leg(s)
