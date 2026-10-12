# Deploy Completion Record
**Date opened:** 2026-10-12T17:22:40.577498+00:00
**Status:** OPEN
**Deploy:** MDPF_CANON CN-d-1 + CN-d-5 (ADHOC.canon-r4-code-deploy, WORLD): three named gold scripts to opal-data-mdpf code/scripts/gold/, the mdpf-gold-lambda package at pin 0d39789fdf, one on-demand run read against a before baseline, the whole-tree equality print classified. Keys: code/scripts/gold/mdpf_gold_consolidator.py, dim_mdpf_account_distribution.py, dim_mdpf_aggregate_aua_timeseries.py. Lambda: mdpf-gold-lambda. Consumers of the global account-distribution object s3://opal-data-assets/portal/gold/mdpf/global/account-distribution/<date>.json: the portal MDPF account-distribution view (catalog entry portal_mdpf_account_distribution) and the lambda's own category-views phase; enumeration is the comp-find census (2610 hits), not exhaustive.
**Authored by:** 0.7.0_AE_CloudOps~DELL1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | before print: whole-tree mdpf-code-equality, prior ETag and VersionId of the three keys, baseline ETags and body hashes of the global account-distribution and every firm scope's four artifacts | equality print attached, three prior VersionIds recorded, baseline object list with ETags printed |  | OPEN |
| L2 | s3-prefix | s3://opal-data-mdpf/code/scripts/gold/mdpf_gold_consolidator.py (D1, safe-deploy.sh named file) | mdpf-code-equality --files exit 0 and named_not_equal 0 |  | OPEN |
| L3 | s3-prefix | s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_account_distribution.py (D1, safe-deploy.sh named file) | mdpf-code-equality --files exit 0 and named_not_equal 0 |  | OPEN |
| L4 | s3-prefix | s3://opal-data-mdpf/code/scripts/gold/dim_mdpf_aggregate_aua_timeseries.py (D1, safe-deploy.sh named file) | mdpf-code-equality --files exit 0 and named_not_equal 0 |  | OPEN |
| L5 | tf-lambda | aws_lambda_function.mdpf_gold (D2: build_package.py --pin 0d39789fdf, upload, targeted safe-apply) | plan moves only the function code; deployed package manifest sha256 of the three files equals the pin |  | OPEN |
| L6 | activation | the one on-demand mdpf-gold-lambda invoke in its schedule's own event shape, FIRMBKTS ledgers re-read immediately before | global account-distribution gains exactly meta.cottonwood_fold.value_date and age_trading_days; every other object value-equal; manifest errors empty |  | OPEN |
| L7 | verify | classification of every non-EQUAL name in the after print (read only, nothing deployed from it), after print attached | every non-EQUAL name classified with a reason; the three D1 names read EQUAL |  | OPEN |

## Log

- 20261012T172240Z OPENED by 0.7.0_AE_CloudOps~DELL1 with 7 leg(s)
