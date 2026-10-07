# Deploy Completion Record
**Date opened:** 2026-10-07T22:56:15.802381+00:00
**Status:** OPEN
**Deploy:** irpt-ycharts-generate release 1: IB-pr-357 (served.py 7cc704) + ~P x3 + ~G2 x2 inert + E-Y4 x14; pin 1b5afe6a49; built ZspX0qD2..; rollback uFTONal.. / S3 objver w031eAfDs6mh..; CTO half d2d2859a2a
**Authored by:** 2.0.0_SA_COO~Y2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-release baseline: live CodeSha256 == S3 objver w031eAfDs6mh content-sha256 == tfstate source_code_hash (uFTONal..); before-key-set of the LIVE zip (after-read 4 before); CloudWatch Errors/Invocations hour-before | three-plane equality + key set + metric numbers |  | OPEN |
| L2 | s3-prefix | build-and-upload investor-reporting irpt-ycharts-generate -> opal-313476888478-lambda-artifacts/investor-reporting/irpt-ycharts-generate.zip | built sha256 == ZspX0qD2.. + new versionId |  | OPEN |
| L3 | activation | safe-apply of infra/aws/terraform/investor-reporting/ycharts saved plan -target module.irpt_ycharts_generate.aws_lambda_function.this; 0 add 0 destroy | apply output + 0-diff re-plan |  | OPEN |
| L4 | verify | after-reads 1-7 of NEVER_WIDEN_PAIR_RELEASE1 + CTO msg 1133 (a) no-token POST refusal envelope lacks internal_correlation_id, (b) CloudWatch hour-after vs hour-before | after-reads file |  | OPEN |

## Log

- 20261007T225615Z OPENED by 2.0.0_SA_COO~Y2 with 4 leg(s)
