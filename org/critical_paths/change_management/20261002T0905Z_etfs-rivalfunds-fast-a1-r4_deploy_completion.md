# Deploy Completion Record
**Date opened:** 2026-10-02T09:05:07.399051+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS FAST: CRO~RV CALL 8 split guard (pin CLOUD 2a9a11a025, plan 0/5/0) + 2026-10-01 rebuild and republish
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| D1 | activation | safe-apply infra/aws/terraform/etfs-rivalfunds saved plan /c/tmp/rv_apply4.tfplan (5 Lambdas source_code_hash; no policy) | apply output: Apply complete 0 added 5 changed 0 destroyed |  | OPEN |
| D2 | verify | five CodeSha256 after apply differ from the 0d4b3f6e4d set | get-function output |  | OPEN |
| D3 | activation | rebuild + republish 2026-10-01: daily-lambda only publish-page refresh_a1, batch fast-a1-publish-1001d | request id + marker + new holding_contribution revision |  | OPEN |
| D4 | verify | moved fields: BASG/GQGU/CGIC YTD, 5 refused rows with reasons, the 7 newly priced days | S3 readback |  | OPEN |

## Log

- 20261002T090507Z OPENED by 2.0.0_SA_COO~RV with 4 leg(s)
