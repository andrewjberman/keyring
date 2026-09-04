# Deploy Completion Record
**Date opened:** 2026-09-04T04:05:35.248799+00:00
**Status:** OPEN
**Deploy:** TO-OP-S-9D: destroy the legacy opal-users table THROUGH TERRAFORM by removing its declaration (Andrew-authorised 2026-09-04 ~03:4xZ, 'Recs approved')
**Authored by:** 0.7.0_AE_CloudOps~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | PRE-ACT re-read at this vintage: snapshot AVAILABLE 12 items 4506 bytes expiry null, table 12 of 12 rows UNMOVED, fixture login captured | live reads with timestamps |  | OPEN |
| L2 | git | SITEZ commit removing the aws_dynamodb_table.opal_users declaration from portal-auth/dynamodb.tf | commit hash |  | OPEN |
| L3 | activation | safe-apply performs the DESTROY through Terraform; plan read as its own artifact showing EXACTLY ONE resource destroyed | plan + apply output |  | OPEN |
| L4 | verify | POST: describe-table returns ResourceNotFoundException; UNSCOPED re-plan proposes NO re-creation; fixture login AFTER matches its before | live reads pasted |  | OPEN |

## Log

- 20260904T040535Z OPENED by 0.7.0_AE_CloudOps~X with 4 leg(s)
