# Deploy Completion Record
**Date opened:** 2026-10-17T16:27:00.874501+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R36S: irpt-status release r36S (acceptance.py gains get_commentary_ref) at pin ae2ab2072b: build and upload (U), scoped Terraform apply of the function code (C), after-reads G1-G6 (V); COO half blob b659221aa1, CTO half c9789c47f5
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U | s3-prefix | the irpt-status package built at the pin and uploaded as the new latest version of investor-reporting/irpt-status.zip | digest equal to the expected CodeSha256, object read back sha256 dbbe1d97 |  | OPEN |
| C | activation | scoped plan 0/1/0 at module.irpt_status.aws_lambda_function.this then safe-apply | plan counts and the live CodeSha256 274dl2bC |  | OPEN |
| V | verify | after-reads G1 to G6, the record A_AFTER_R36S.txt and the function-map record | the G1-G6 lines |  | OPEN |

## Log

- 20261017T162700Z OPENED by 0.7.0_AE_CloudOps~IB2 with 3 leg(s)
