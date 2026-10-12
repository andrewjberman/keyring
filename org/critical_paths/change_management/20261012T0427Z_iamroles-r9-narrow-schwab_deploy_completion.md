# Deploy Completion Record
**Date opened:** 2026-10-12T04:27:23.116730+00:00
**Status:** OPEN
**Deploy:** IAM-z-2 PHASE B act (b): delete-role-policy schwab-bucket-access on bd-exporter-ec2-role -- 2 of 2 ARNs are the 404 opal-data-schwab (pair COO @4afde83a62 / CTO @c790b17440)
**Authored by:** 0.7.0_AE_CloudOps~IR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| delete | activation | bd-exporter-ec2-role/schwab-bucket-access | list-role-policies reads 16 with schwab-bucket-access absent; get-role-policy on it returns NoSuchEntity; the other 16 policies untouched |  | OPEN |
| realrun | verify | bd-exporter-ec2-role | ONE real bd run that STARTS AFTER the delete and completes successfully -- RoleLastUsed advances past the delete time and the run's own record shows success; NEVER substituted by a simulation |  | OPEN |

## Log

- 20261012T042723Z OPENED by 0.7.0_AE_CloudOps~IR with 2 leg(s)
