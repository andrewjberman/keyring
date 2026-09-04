# Deploy Completion Record
**Date opened:** 2026-09-04T03:29:04.689870+00:00
**Status:** OPEN
**Deploy:** TO-OP-S-9C: remove the residual opal-users grant from trade-submission-lambda-role (trade-pipeline/iam.tf:63-64) after a deployed-bytes + config oracle agreed it is unused
**Authored by:** 0.7.0_AE_CloudOps~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | BEFORE: five invocable functions invoked and their responses captured; the two mail senders' dormancy recorded as UNCOMPUTABLE-BY-CONSTRUCTION | 5 of 5 invoke results pasted |  | OPEN |
| L2 | git | SITEZ commit removing trade-pipeline/iam.tf:63-64 | commit hash |  | OPEN |
| L3 | activation | terraform apply on the trade-pipeline root | apply output |  | OPEN |
| L4 | verify | AFTER: the same five invoked, same results as the before; APPLIED-plane get-role-policy showing table/opal-users absent from trade-submission-policy | 5 of 5 plus the live policy read |  | OPEN |
| L5 | verify | UNSCOPED re-plan 0-diff on trade-pipeline; residual set re-enumerated estate-wide; runbook entry written where a person diagnosing a failed trade will meet it | plan output + census + runbook path |  | OPEN |

## Log

- 20260904T032904Z OPENED by 0.7.0_AE_CloudOps~X with 5 leg(s)
