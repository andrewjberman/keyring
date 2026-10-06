# Deploy Completion Record
**Date opened:** 2026-10-06T18:38:33.530520+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261006T191211Z
**Deploy:** Attribution two-sided funnel (Cash->FI, all else->Equity) in yang-generate-holdings-attribution + yang-generate-allocation-summary, source c7adf21d10; Andrew-direct record org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_173xZ_ATTRIBUTION_FUNNEL_CASH_TO_FI_REST_TO_EQUITY.md; deploy + refresh on Andrew's in-session word
**Authored by:** 4.0.0_SA_CRO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | terraform plan 0-diff on yang-pipeline after targeted apply | plan output line | post-apply terraform plan -target both modules (terraform 1.15.8 = state version): 'No changes. Your infrastructure matches the configuration.' | CLOSED 20261006T191210Z |
| V2 | verify | served holdings_attribution_data.json + allocation_summary.json carry only Fixed Income/Equity, totals tie to workbook | served-artifact read | served re-read 19:0xZ after invoking both Lambdas (200/None each; workbook 20260930 staged to uploads/ -- trigger filter is uploads/*manifest.json so inert): holdings_attribution_data.json gen 2026-10-06T19:02:27Z classes {Equity:214, Fixed Income:207}, 421/421 holdings, every non-class field equal to the pre-refresh snapshot; allocation_summary.json gen 19:02:41Z, every model two rows, FI bet = -Equity bet, AA totals tie to workbook Total row (offline run). Pre-refresh snapshots kept for rollback in the session scratchpad. | CLOSED 20261006T191210Z |
| yang-generate-holdings-attribution | tf-lambda | module.generate_holdings_attribution.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | targeted safe-apply of module.generate_holdings_attribution (plan 0 add/2 change/0 destroy across both legs); live get-function-configuration CodeSha256=TdZc5zkyw8Zmb+w1jiCviLKjdJbqLRxqIy5HkvMs2kQ= == S3 artifact content-sha256 == build output; LastModified 2026-10-06T18:56:56Z, State Active/Successful; source c7adf21d10; rollback = prior s3_object_version 9jsYx2n_puRLE.L0pFS9ioMvIwg4aYTX | CLOSED 20261006T191209Z |
| yang-generate-allocation-summary | tf-lambda | module.generate_allocation_summary.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | targeted safe-apply of module.generate_allocation_summary; live CodeSha256=Qk667D2V3CAU+SUaT03dYdGS2b2bKW8BpANRVarPdXg= == S3 artifact content-sha256 == build output; LastModified 2026-10-06T18:56:56Z, Active/Successful; source c7adf21d10; rollback = prior s3_object_version BxWpvrT9AKAV4p6Bl1o9vPYcz98NESHc | CLOSED 20261006T191210Z |

## Log

- 20261006T183833Z OPENED by 4.0.0_SA_CRO~X with 4 leg(s)
- 20261006T191209Z LEG yang-generate-holdings-attribution closed: targeted safe-apply of module.generate_holdings_attribution (plan 0 add/2 change/0 destroy across both legs); live get-f
- 20261006T191210Z LEG yang-generate-allocation-summary closed: targeted safe-apply of module.generate_allocation_summary; live CodeSha256=Qk667D2V3CAU+SUaT03dYdGS2b2bKW8BpANRVarPdXg= 
- 20261006T191210Z LEG V1 closed: post-apply terraform plan -target both modules (terraform 1.15.8 = state version): 'No changes. Your infrastructure matc
- 20261006T191210Z LEG V2 closed: served re-read 19:0xZ after invoking both Lambdas (200/None each; workbook 20260930 staged to uploads/ -- trigger filter
- 20261006T191211Z CLOSED -- all 4 legs proven
