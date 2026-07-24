# Deploy Completion Record
**Date opened:** 2026-07-23T21:12:09.455472+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260723T211851Z
**Deploy:** A1: key-scoped disable of legacy aum-metrics.json portal write (CTO 210937Z -- the Andrew-confirmed $1.95B radial must not revert at cron(30 11)Z)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| opal-smartx-ingestion-pipeline | tf-lambda | aws_lambda_function.ingestion_pipeline | TF apply (0 destroy) + 0-diff replan + deployed source_code_hash matches uploaded sha + verify-on-served | Write set grounded: main() makes exactly 2 puts (:831 timeseries UNGATED pending A2, :832 metrics GATED). Sibling flag DISABLE_PORTAL_AUM_METRICS_WRITE per CTO's per-key-family granularity call. Commit e7a4ef7a7 BEFORE apply; artifact rebuilt (sha-verified upload); safe-apply targeted; live function shows BOTH flags + CodeSha256 yYju4HCONr/aGYKWUHmW63U9C0edSGucVhdEDmsKySc=. EXERCISED ON THE DEPLOYED RUNTIME (strongest form): real {job:account_distribution} invocation with both gates live -- PROTECTED keys byte-survived (bell ETag 14d668ef unchanged; aum-metrics ETag 9bae4b42 -- the Andrew-confirmed radial -- unchanged) while the job reported 3/3 producer success (proves nothing keys on the gated writes) and the ungated per-firm bell was rewritten as expected (a24874497, the same daily legacy write). Mutant direction for the bell gate proven earlier via stubbed-S3 (flag unset -> put fires). Clock met: both disables live ahead of tomorrow's cron(30 11)Z. | CLOSED 20260723T211850Z |

## Log

- 20260723T211209Z OPENED by 0.7.0_AE_CloudOps with 1 leg(s)
- 20260723T211850Z LEG opal-smartx-ingestion-pipeline closed: Write set grounded: main() makes exactly 2 puts (:831 timeseries UNGATED pending A2, :832 metrics GATED). Sibling flag D
- 20260723T211851Z CLOSED -- all 1 legs proven

## AMENDMENT (0.7.0_AE_CloudOps, 2026-07-24T02:2xZ) -- FLAG #3, the clobber-guard family COMPLETE
CTO 20260724T001913Z discharged the A2 hold (mechanism named: 147 per-firm anchor at Global scope;
fix live on portal 148; Andrew-verified "values and counts look correct"). DISABLE_PORTAL_AUM_TIMESERIES_WRITE
gated at the write site (:831 put), both source copies synced, commit 48c3903d5 BEFORE apply, artifact
sha-verified upload, targeted safe-apply, live function carries ALL THREE flags + CodeSha256
voja8JiVHtdGvTTHInF4ICeYfR/m3FqQSSX6DNFfBzM=. EXERCISED ON THE DEPLOYED RUNTIME: real
{"job":"account_distribution"} invocation, producers 3/3 green, and all three json/portfolios/* keys
byte-SURVIVED (bell 14d668ef / aum-metrics 9bae4b42 / aum-timeseries f96cfc43 -- the last now carrying
the 148-fix revamp bytes, which is exactly what the gate protects). Tomorrow's cron(30 11)Z legacy run
can no longer touch any portfolios key; COO's byte-verify window covers these three ETags as recorded.
