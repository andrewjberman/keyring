# Deploy Completion Record
**Date opened:** 2026-09-29T02:29:06.317585+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260929T030705Z
**Deploy:** IB-er-203: first build+apply of irpt-holdings-performance-lambda + irpt-holdings-performance-daily schedule (new resources only)
**Authored by:** 0.9.0_WK_IRPT_BCKEND~65
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-holdings-performance-lambda.zip | build-and-upload OK line + head-object sha256 metadata == zip sha256 | build-and-upload investor-reporting irpt-holdings-performance-lambda: s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-holdings-performance-lambda.zip sha256 a1ZUOSw5lg5CH2Fe6Dq7UsZSpbiXQtwFRNp084Cerms= 112985 bytes; head-object write VERIFIED (size+sha256 metadata match) | CLOSED 20260929T023140Z |
| A2 | activation | module.irpt_holdings_performance / module.irpt_holdings_performance_schedule | plan (new resources only), safe-apply success, readback (get-function + get-schedule ENABLED) | plan 7/0/0 (all creates); safe-apply 20260929 (HALT_ACK routine, tagauthz PASSED, tombstone-gate CLEAN): Apply complete! Resources: 7 added, 0 changed, 0 destroyed; readback get-function irpt-holdings-performance-lambda Active/Successful timeout=300 memory=1536 handler=handler.lambda_handler layer=irpt-performance-native-layer:1; get-schedule irpt-holdings-performance-daily ENABLED cron(30 7 ? * MON-FRI *) America/New_York target=irpt-holdings-performance-lambda | CLOSED 20260929T024711Z |
| V1 | verify | one invoke of irpt-holdings-performance-lambda for the latest computable trading day | manifest object at the address the invoke's own return names, read back from S3 | invoke irpt-holdings-performance-lambda {date:2026-09-25} (the latest trading day with fully-landed silver as of this deploy -- 2026-09-28's silver had not yet landed at invoke time, see row S1): rc=0 ok=true; log EMIT: 1 day(s) landed, 7540 row(s), census OK=6650 NO-PRIOR-HOLDINGS=881 NON-POSITIVE-BASE=6 ALL-HOLDINGS-EXCLUDED=3; readback head-object irpt/49financial/gold/holdings_performance_daily/date=2026-09-25/data.parquet ContentLength=297155; get-object .../holdings_performance_manifest/date=2026-09-25/manifest.json rows=7540 landed=true etag=98b81e55c6989cbc7cae6008dfa9a34b | CLOSED 20260929T030538Z |
| V2 | verify | 0-diff re-plan of the holdings-performance root | terraform plan reads No changes | terraform plan infra/aws/terraform/investor-reporting/holdings-performance (post-fix state): No changes. Your infrastructure matches the configuration. | CLOSED 20260929T030704Z |

## Log

- 20260929T022906Z OPENED by 0.9.0_WK_IRPT_BCKEND~65 with 4 leg(s)
- 20260929T023140Z LEG A1 closed: build-and-upload investor-reporting irpt-holdings-performance-lambda: s3://opal-313476888478-lambda-artifacts/investor-r
- 20260929T024711Z LEG A2 closed: plan 7/0/0 (all creates); safe-apply 20260929 (HALT_ACK routine, tagauthz PASSED, tombstone-gate CLEAN): Apply complete!
- 20260929T030538Z LEG V1 closed: invoke irpt-holdings-performance-lambda {date:2026-09-25} (the latest trading day with fully-landed silver as of this de
- 20260929T030704Z LEG V2 closed: terraform plan infra/aws/terraform/investor-reporting/holdings-performance (post-fix state): No changes. Your infrastruc
- 20260929T030705Z CLOSED -- all 4 legs proven
