# Deploy Completion Record
**Date opened:** 2026-09-25T23:38:43.622784+00:00
**Status:** OPEN
**Deploy:** S140: admit irpt-performance-adapter-role to opal-data-49financial READ-ONLY on the engine prefixes (CTO 101058/101060, row @2c952bf460) -- -target bucket policy
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | aws_s3_bucket_policy.opal_data_49financial | live policy = DenyForeignFirmPrincipals + adapter ARN, and the three adapter-only Denies | -target apply 0/1/0 (23:4xZ). Live get-bucket-policy opal-data-49financial: Sids DenyForeignFirmPrincipals (ArnNotLike + irpt-performance-adapter-role, nothing removed), DenyPerformanceAdapterAnyOtherAction (NotAction GetObject/ListBucket), DenyPerformanceAdapterReadsOutsideTheEngine (NotResource gold/advi/canonical/twr_daily/* + twr_periods/*), DenyPerformanceAdapterListingOutsideTheEngine (StringNotLike s3:prefix). | CLOSED 20260925T234137Z |
| N1 | verify | negative arm (simulator + live) | simulated: adapter GetObject engine allowed, non-engine GetObject denied, PutObject denied, ListBucket unprefixed denied, a COT role denied; live: engine GetObject 200 via the adapter path |  | OPEN |
| V1 | verify | re-plan | No changes on the target | targeted re-plan after apply: No changes. | CLOSED 20260925T234137Z |

## Log

- 20260925T233843Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260925T234137Z LEG A1 closed: -target apply 0/1/0 (23:4xZ). Live get-bucket-policy opal-data-49financial: Sids DenyForeignFirmPrincipals (ArnNotLike +
- 20260925T234137Z LEG V1 closed: targeted re-plan after apply: No changes.
