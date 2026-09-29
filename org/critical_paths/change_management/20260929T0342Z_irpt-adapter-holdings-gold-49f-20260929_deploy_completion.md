# Deploy Completion Record
**Date opened:** 2026-09-29T03:42:55.464991+00:00
**Status:** OPEN
**Deploy:** Performance adapter reads the holdings-basis gold for 49F (TO-IB-pr-201/202; PRD v0.19 rulings 10, 12): code (holdings_gold.py + retained/installed/entry + schema OPAL_HOLDINGS) + adapter IAM (performance root) + 49F bucket fence (shared-infra); engine read retires in the same act; applies AFTER window 21 closes
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload + gates | census vs live qfxZ0DzB: only the named members differ (+holdings_gold.py); flat + ~Y zip_module_census; cold start with /var/task mapped | Source map irpt-performance-adapter: holdings_gold.py ADDED (a595a14264, afc37c0a), retained.py 90c4b596f3->a595a14264 (880cf928->bf5f00e8), installed.py b905df2c60->a595a14264 (b5e6f42c->a2125b3a), entry.py 57a58117fb->a595a14264 (4d22ff2e->b34a1171), PerformanceReport.schema.json b905df2c60->78eeb223f8 (21bacfa9->c4e2fdb1); 65 other members unchanged. build-and-upload rc 0 with BAU_PARITY_SKIP=1 (build tooling not members, per _build_note); the build's deletion of tracked performance/*.py restored (0 left). S3 investor-reporting/irpt-performance-adapter.zip VersionId ABB89j26YSZbacEIz3Vgt2.o5_EhkIHj sha qosuSxAfYQv5mRab02qyta9h1p7HEnjSphvYzQANlsg= (424346 bytes). CENSUS vs live qfxZ0DzB (get-function bytes): 69 -> 70, added holdings_gold.py ONLY, differ PerformanceReport.schema.json, entry.py, installed.py, retained.py ONLY, removed 0. flat_zip_module_census: pin skew 0, rc 0. ~Y zip_module_census: new FAIL set {entry, errors, handler, maintained_sources, request_composition, resolve, routetable, transport} is a strict subset of live qfxZ0DzB's (live also flags installed.py, retained.py) -- 0 new flags. Cold start with /var/task mapped: IMPORT OK, named UNAVAILABLE envelope, rc 0 -- same as live's. | CLOSED 20260929T035956Z |
| P1 | verify | plans for both roots | performance root plan: role policy + lambda code only; shared-infra plan: bucket policy only; no other change | Plans 04:0xZ (-lock=false, -out; to be re-planned fresh at apply). PERFORMANCE root: Plan 0/2/0 -- aws_iam_role_policy.performance_retained: ListBucket s3:prefix gold/advi/canonical/twr_daily/ -> irpt/49financial/gold/holdings_performance_daily/ (Sid ReadEngineTwrDailyPartitionInventory -> ReadHoldingsGoldPartitionInventory); GetObject/GetObjectVersion opal-data-49financial/gold/advi/canonical/twr_daily/date=*/data.parquet -> .../irpt/49financial/gold/holdings_performance_daily/date=*/data.parquet (Sid ReadEngineTwrDailyPartitions -> ReadHoldingsGoldPartitions); module.irpt_performance_adapter.aws_lambda_function.this: s3_object_version 5bmwADQs -> new, source_code_hash qfxZ0DzB -> new, nothing else. SHARED-INFRA root: Plan 0/1/0 -- aws_s3_bucket_policy.opal_data_49financial: DenyPerformanceAdapterReadsOutsideTheEngine -> ...OutsideTheHoldingsGold (NotResource twr_daily/* + twr_periods/* -> irpt/49financial/gold/holdings_performance_daily/*); DenyPerformanceAdapterListingOutsideTheEngine -> ...OutsideTheHoldingsGold (StringNotLike s3:prefix same swap); DenyForeignFirmPrincipals and DenyPerformanceAdapterAnyOtherAction unchanged. Prefix = builder output address('irpt','49financial','gold','holdings_performance_daily','date=...') printed 2026-09-29. | CLOSED 20260929T040450Z |
| D1 | activation | apply shared-infra bucket fence + performance root | halves at HEAD; W21 closed; CRO before-read (49F YTD/1Y + a retained engine report + COT/INF controls); safe-apply both; readback CodeSha + policies; real cold-start invoke; re-plan 0 |  | OPEN |
| A1 | verify | the Performance page | 49F figures served OPAL_HOLDINGS with page words; a retained engine report not reopened; COT and INF unchanged; both readers counted |  | OPEN |

## Log

- 20260929T034255Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260929T035956Z LEG U1 closed: Source map irpt-performance-adapter: holdings_gold.py ADDED (a595a14264, afc37c0a), retained.py 90c4b596f3->a595a14264 (
- 20260929T040450Z LEG P1 closed: Plans 04:0xZ (-lock=false, -out; to be re-planned fresh at apply). PERFORMANCE root: Plan 0/2/0 -- aws_iam_role_policy.p
