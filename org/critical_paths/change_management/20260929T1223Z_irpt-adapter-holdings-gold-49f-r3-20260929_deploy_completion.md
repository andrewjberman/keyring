# Deploy Completion Record
**Date opened:** 2026-09-29T12:23:22.250167+00:00
**Status:** OPEN
**Deploy:** RE-SWITCH after the 10:58Z rollback: Performance adapter reads 49F from the holdings gold -- hD7G6YT1's source + the runners_49f sys.path fix (TO-IB-pr-201 amendment 2, drained 66469ce943), 49F ALONE (CTO 102746); adapter IAM + 49F bucket fence re-pointed
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload + gates | census vs live qfxZ0DzB and vs hD7G6YT1 (only installed.py differs from hD7G6YT1); flat + zip_module_census; P20-3-AC1 on the built zip; cold container of the BUILT artifact: YTD, QTD, 1Y, 3Y, SI each a figure or a named refusal (sweep-2 s.1) | Source map: installed.py re-pinned a595a14264 -> 66469ce943 (WK~77 drain; blob cd2f1d86, sha256 b00fc65e); every other member as hD7G6YT1. build-and-upload rc 0 (BAU_PARITY_SKIP=1), tracked sources restored. S3 investor-reporting/irpt-performance-adapter.zip VersionId TBy0pL.rwpHBE1BBqkyIDYC6Dky4QS7j (12:23:58Z) sha +h/AH/RY. Census: vs hD7G6YT1 (3donK_gT) ONLY installed.py differs; vs live qfxZ0DzB 69 -> 70, holdings_gold.py added, PerformanceReport.schema.json/entry.py/installed.py/retained.py differ. flat_zip_module_census pin skew 0; ~Y zip_module_census FAIL set a strict subset of live's (installed.py, retained.py leave it). Cold start /var/task mapped: IMPORT OK, named envelope, rc 0. P20-3-AC1 PASS on CLOUD @66469ce943. SWEEP-2 s.1 cold container of the BUILT zip (checks/r20/adapter_cold_periods.py, runners dir absent from harness path), end 2026-09-28: ..498003/..884180/..064180/..480090 x YTD/QTD/1Y/3Y/SI = 16 figures (OPAL_HOLDINGS) + 4 x 3Y UNSUPPORTED_OPERATION (HoldingsWindowNotRuled), 0 UNEXPECTED; control hD7G6YT1 FAILS (ModuleNotFoundError parity_period_returns). | CLOSED 20260929T124351Z |
| P1 | verify | fresh plans for both roots | performance: role policy + code only; shared-infra: bucket policy only | TF re-pointed by restoring 9e0bde13e3~1 bytes (= ae20e904e6) of performance/retained.tf and shared-infra/s3-49financial.tf. Plans 12:4xZ, main tree, .tools/terraform.exe: performance 0/2/0 = aws_iam_role_policy.performance_retained (Sids ReadEngineTwrDaily* -> ReadHoldingsGold*; list prefix gold/advi/canonical/twr_daily/ -> irpt/49financial/gold/holdings_performance_daily/; GetObject date=*/data.parquet likewise) + module.irpt_performance_adapter.aws_lambda_function.this (code only; source_code_hash qfxZ0DzB -> known after apply from S3 latest TBy0pL); shared-infra -target=aws_s3_bucket_policy.opal_data_49financial 0/1/0 (the two adapter Deny statements: NotResource/StringNotLike engine prefixes -> irpt/49financial/gold/holdings_performance_daily/*). Identical to r2's P1. | CLOSED 20260929T124351Z |
| D1 | activation | apply performance root then shared-infra | halves at HEAD; before-read; safe-apply both; readback; deployed invokes YTD/QTD/1Y/3Y/SI on a fresh container never UNEXPECTED; CRO 102750 conditions; re-plan 0 |  | OPEN |
| A1 | verify | all-accounts served census through real deployed invokes + both readers | census per period; the 7 SI >=+100% accounts named; engine reports not reopened; COT/INF unchanged |  | OPEN |

## Log

- 20260929T122322Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260929T124351Z LEG U1 closed: Source map: installed.py re-pinned a595a14264 -> 66469ce943 (WK~77 drain; blob cd2f1d86, sha256 b00fc65e); every other m
- 20260929T124351Z LEG P1 closed: TF re-pointed by restoring 9e0bde13e3~1 bytes (= ae20e904e6) of performance/retained.tf and shared-infra/s3-49financial.
