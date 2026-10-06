# Deploy Completion Record
**Date opened:** 2026-10-06T18:38:33.530520+00:00
**Status:** OPEN
**Deploy:** Attribution two-sided funnel (Cash->FI, all else->Equity) in yang-generate-holdings-attribution + yang-generate-allocation-summary, source c7adf21d10; Andrew-direct record org/tier1_exec/4.0.0_SA_CRO/deliverables/ANDREW_DIRECT_20261006_173xZ_ATTRIBUTION_FUNNEL_CASH_TO_FI_REST_TO_EQUITY.md; deploy + refresh on Andrew's in-session word
**Authored by:** 4.0.0_SA_CRO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V1 | verify | terraform plan 0-diff on yang-pipeline after targeted apply | plan output line |  | OPEN |
| V2 | verify | served holdings_attribution_data.json + allocation_summary.json carry only Fixed Income/Equity, totals tie to workbook | served-artifact read |  | OPEN |
| yang-generate-holdings-attribution | tf-lambda | module.generate_holdings_attribution.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |
| yang-generate-allocation-summary | tf-lambda | module.generate_allocation_summary.aws_lambda_function.this | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served |  | OPEN |

## Log

- 20261006T183833Z OPENED by 4.0.0_SA_CRO~X with 4 leg(s)
