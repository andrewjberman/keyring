# Deploy Completion Record
**Date opened:** 2026-10-02T08:17:16.220449+00:00
**Status:** OPEN
**Deploy:** ETFS_RIVALS FAST: CVO grade-2 fix redeploy (pin CLOUD fc80f776e4, plan 0/5/0) + 2026-10-01 A1 rebuild and republish (refresh_a1)
**Authored by:** 2.0.0_SA_COO~RV
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 12.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| B1 | activation | safe-apply infra/aws/terraform/etfs-rivalfunds saved plan /c/tmp/rv_apply2.tfplan (5 Lambdas source_code_hash in place; no policy change) | apply output: Apply complete 0 added 5 changed 0 destroyed |  | OPEN |
| B2 | verify | five CodeSha256 after apply differ from the 7aa0186d45 base | get-function output |  | OPEN |
| B3 | activation | rebuild + republish 2026-10-01: daily-lambda only publish-page refresh_a1, batch fast-a1-publish-1001b | request id + marker + manifest a1_produced OK + new table revisions |  | OPEN |
| B4 | verify | moved fields read back: ETFT/SCHY/BIDD YTD totals, money-market lines absent, trend window starts and . marks, sector panels; SCHY/BIDD refused rows printed (CALL 6 condition 3) | S3 readback + evidence file |  | OPEN |

## Log

- 20261002T081716Z OPENED by 2.0.0_SA_COO~RV with 4 leg(s)
