# Deploy Completion Record
**Date opened:** 2026-10-20T07:00:18.187037+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-APPLY-R37 v2: irpt-ycharts-generate (the upload door) -- served.py O1 owner fallback and ticket_confirmation.py creator stamp; 2 of 107 members move
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U | s3-prefix | investor-reporting/irpt-ycharts-generate.zip new latest version, sha256 3e50a336, CodeSha256 PlCjNms/RRLRB/c15zW8Sdzl7w3ptodi3o8sSxnWjYA= (rollback: the R0 latest VersionId) | digest, read-back |  | OPEN |
| C | tf-lambda | scoped plan 0/1/0 on module.irpt_ycharts_generate.aws_lambda_function.this, ONE safe-apply | plan counts, CodeSha256 |  | OPEN |
| V | verify | after-reads G1 to G4 | S1 to S4 lines |  | OPEN |

## Log

- 20261020T070018Z OPENED by 0.7.0_AE_CloudOps~IB2 with 3 leg(s)
