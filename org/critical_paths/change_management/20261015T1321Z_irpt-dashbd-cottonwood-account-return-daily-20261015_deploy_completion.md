# Deploy Completion Record
**Date opened:** 2026-10-15T13:21:01.669675+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-260 (revision 2, packet sha256 a1b080c5fe06, COO half @fed117446e, CTO half @ed790ad4bf): APPLY the signed Cottonwood account-return landing pair: upload the FIRST object version of investor-reporting/irpt-cot-account-return-daily-lambda.zip, plan EXACTLY 7 add / 0 change / 0 destroy (function irpt-cot-account-return-daily-lambda 1024 MB with the native pyarrow layer, execution and scheduler roles and policies, log group, schedule irpt-cot-account-return-daily-daily DISABLED), ONE safe-apply, then Act 2 ONE synchronous event {day 2026-07-10} writing ONE partition (two objects) under irpt/cottonwood/gold/account_return_daily/; NO enable, NO days event, NO second invoke
**Authored by:** 0.7.0_AE_CloudOps~DB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | tree commit and the sha256 of each file in the packet's section 2; packet blob, sha256 and both halves; marker scan; live absence reads; the layer read | the printed reads |  | OPEN |
| L2 | s3-prefix | BUILD_ONLY zip line equals the packet's fQFe4moIeMHspIjLxO2C04TobQW6cNZc7mfwstcMWzs=, import smoke rc 0, then upload the key's FIRST object version; built==landed | zip sha256, smoke rc, VersionId |  | OPEN |
| L3 | activation | fmt -check, init, validate, saved plan EXACTLY 7/0/0 on the seven addresses (1 layer, memory 1024, timeout 900, reserved concurrency 1, schedule DISABLED); then ONE safe-apply, read-backs, replan No changes | plan line, apply line, read-backs, replan line |  | OPEN |
| L4 | activation | Act 2: ONE synchronous invoke {day 2026-07-10}, no retry; after-read: the partition holds exactly data.parquet and manifest.json, history 3325 partitions to 2026-06-22 untouched, REPORT Max Memory Used under 717 MB, layer pyarrow version | response, REPORT line, LIST |  | OPEN |
| L5 | verify | Act 3 (the catch-up days events) is a SEPARATE order after the issuer reads this record; the schedule stays DISABLED; stays OPEN for the issuer 2.0.0_SA_COO~D2 | the issuer's order and read |  | OPEN |

## Log

- 20261015T132101Z OPENED by 0.7.0_AE_CloudOps~DB2 with 5 leg(s)
