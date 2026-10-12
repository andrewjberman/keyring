# Deploy Completion Record
**Date opened:** 2026-10-12T02:03:50.194617+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T021315Z
**Deploy:** IAM-z-1 ACT 4: delete-role-policy S3Access on FredIngestionLambdaRole -- both its ARNs are the 404 opal-market-update, so a narrowed document would be empty (pair COO @3860c1c906 / CTO @364e77ecdd)
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| delete | activation | FredIngestionLambdaRole/S3Access | list-role-policies no longer lists S3Access and still lists fred-ingestion-secrets-read, SecretsManagerAccess and yield-curve-artifact-write | delete-role-policy rc=0; list-role-policies read back shows 3 policies with S3Access absent; get-role-policy S3Access rc=254 NoSuchEntity against a positive control of yield-curve-artifact-write rc=0; baseline matched the rollback canonically immediately before the act | CLOSED 20261012T021314Z |
| foldgrant | verify | opal-data-portal-v2/json/macro/yield_curve_fred.json | the fold's own grant yield-curve-artifact-write is byte-unchanged and still authorises PutObject+GetObject on exactly that key | yield-curve-artifact-write byte-identical before and after (sha256 9e39ddff2822b58f82c4da4833d08229bfbb02360bb1577949797b6a0d217128); simulate-principal-policy one resource-arn per call: s3:PutObject allowed, s3:GetObject allowed on opal-data-portal-v2/json/macro/yield_curve_fred.json; negative control s3:PutObject on opal-market-update/* -> implicitDeny | CLOSED 20261012T021314Z |

## Log

- 20261012T020350Z OPENED by 0.7.0_AE_CloudOps~IR with 2 leg(s)
- 20261012T021314Z LEG delete closed: delete-role-policy rc=0; list-role-policies read back shows 3 policies with S3Access absent; get-role-policy S3Access rc
- 20261012T021314Z LEG foldgrant closed: yield-curve-artifact-write byte-identical before and after (sha256 9e39ddff2822b58f82c4da4833d08229bfbb02360bb1577949797
- 20261012T021315Z CLOSED -- all 2 legs proven
