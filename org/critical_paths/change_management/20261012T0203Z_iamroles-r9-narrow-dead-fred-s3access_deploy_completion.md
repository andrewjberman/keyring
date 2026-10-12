# Deploy Completion Record
**Date opened:** 2026-10-12T02:03:50.194617+00:00
**Status:** OPEN
**Deploy:** IAM-z-1 ACT 4: delete-role-policy S3Access on FredIngestionLambdaRole -- both its ARNs are the 404 opal-market-update, so a narrowed document would be empty (pair COO @3860c1c906 / CTO @364e77ecdd)
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| delete | activation | FredIngestionLambdaRole/S3Access | list-role-policies no longer lists S3Access and still lists fred-ingestion-secrets-read, SecretsManagerAccess and yield-curve-artifact-write |  | OPEN |
| foldgrant | verify | opal-data-portal-v2/json/macro/yield_curve_fred.json | the fold's own grant yield-curve-artifact-write is byte-unchanged and still authorises PutObject+GetObject on exactly that key |  | OPEN |

## Log

- 20261012T020350Z OPENED by 0.7.0_AE_CloudOps~IR with 2 leg(s)
