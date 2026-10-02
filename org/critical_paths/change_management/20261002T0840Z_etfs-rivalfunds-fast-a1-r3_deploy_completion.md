# Deploy Completion Record
**Date opened:** 2026-10-02T08:40:00.562857+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS FAST: CRO~RV CALL 6 conditions 1-2 + futures never priced (pin CLOUD 0d4b3f6e4d, plan 0/5/0) + 2026-10-01 rebuild and republish
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | safe-apply infra/aws/terraform/etfs-rivalfunds saved plan /c/tmp/rv_apply3.tfplan (5 Lambdas source_code_hash; no policy) | apply output: Apply complete 0 added 5 changed 0 destroyed |  | OPEN |
| C2 | verify | five CodeSha256 after apply differ from the fc80f776e4 set | get-function output |  | OPEN |
| C3 | activation | rebuild + republish 2026-10-01: daily-lambda only publish-page refresh_a1, batch fast-a1-publish-1001c | request id + marker + new holding_contribution revision |  | OPEN |
| C4 | verify | moved fields: BASG/CGIC/SCHY YTD, 12 refused holding-days with reasons in caption + audit list, 0 futures priced | S3 readback |  | OPEN |

## Log

- 20261002T084000Z OPENED by 2.0.0_SA_COO~RV with 4 leg(s)
