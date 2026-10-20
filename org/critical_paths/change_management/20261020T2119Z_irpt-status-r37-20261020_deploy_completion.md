# Deploy Completion Record
**Date opened:** 2026-10-20T21:19:50.218569+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R37 (two PDF routes): release r37 of the irpt-status Lambda, owned_report.py moves, pin 474f174e89
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U | s3-prefix | new latest version of investor-reporting/irpt-status.zip in opal-313476888478-lambda-artifacts, object sha256 078474759a81... | object read back equal |  | OPEN |
| C | activation | terraform scoped apply of module.irpt_status.aws_lambda_function.this at CodeSha256 B4R0dZqBRhclmQLOiBHp3Ft/wNbMomNZhUflCCRfEyE= | Apply complete 0 added 1 changed 0 destroyed |  | OPEN |
| V | verify | after-reads G1 to G6 | G1 to G6 lines |  | OPEN |

## Log

- 20261020T211950Z OPENED by 0.7.0_AE_CloudOps~IB2 with 3 leg(s)
