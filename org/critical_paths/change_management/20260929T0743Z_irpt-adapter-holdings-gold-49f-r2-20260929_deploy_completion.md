# Deploy Completion Record
**Date opened:** 2026-09-29T07:43:57.041870+00:00
**Status:** OPEN
**Deploy:** RE-CUT: Performance adapter reads 49F from the holdings gold under PRD v0.20 (S195) -- artifact hD7G6YT1 (a595 switch + IB-pr-211 render request + IB-pr-214 fresh-path guard) + adapter IAM + 49F bucket fence; engine read retires
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| U1 | verify | artifact build + upload + gates | census vs live qfxZ0DzB; flat + ~Y zip_module_census; cold start | Built 07:3xZ while the superseded ledger irpt-adapter-holdings-gold-49f-20260929 was still open (this r2 entry opened at 07:43Z; the upload serves nothing until apply). Source map: entry.py (IB-pr-211) + retained.py (IB-pr-214) re-pinned to c7f136c9d8 (b34a1171->8465a60d, bf5f00e8->ea895201); every other member as the refused build. build-and-upload rc 0 BAU_PARITY_SKIP=1; tracked performance/*.py restored (0 left). S3 investor-reporting/irpt-performance-adapter.zip VersionId 3donK_gTGSDdJb5PQZVt9X.hx4Bpp8Ry sha hD7G6YT1o5ibIocQCn9uApRtV108eHkX6aq+w43EK8I= (424559 bytes), read back by version. CENSUS vs live qfxZ0DzB (unchanged at 07:3xZ): 69 -> 70, added holdings_gold.py ONLY, differ PerformanceReport.schema.json, entry.py, installed.py, retained.py ONLY; vs the refused qosuSxAf: entry.py + retained.py ONLY. flat_zip_module_census pin skew 0 rc 0; ~Y zip_module_census FAIL set identical to the refused build's (a strict subset of live's; 0 new flags). Cold start /var/task mapped: IMPORT OK, named UNAVAILABLE envelope, rc 0. | CLOSED 20260929T074459Z |
| P1 | verify | fresh plans for both roots | performance: role policy + code only; shared-infra: bucket policy only | Fresh plans 07:4xZ (-lock=false, -out): performance root 0/2/0 -- aws_iam_role_policy.performance_retained (engine prefix -> holdings gold prefix, same diff as the refused cut's P1) + aws_lambda_function.this code fields only; shared-infra 0/1/0 -- aws_s3_bucket_policy.opal_data_49financial (the adapter fence twr_daily/twr_periods -> irpt/49financial/gold/holdings_performance_daily/*), DenyForeignFirmPrincipals and ...AnyOtherAction unchanged. TF files unchanged since ae20e904e6. | CLOSED 20260929T074609Z |
| D1 | activation | apply performance root then shared-infra | halves at HEAD; CRO before-read incl. a cusip-less-holding and a near-zero-base account; safe-apply both; readback; cold start; SI wall < 48 s; re-plan 0 | Halves at HEAD naming blob a4679360: CTO @50e2dcdafe + c873a29dc6 (102650; precondition met, 102648/102650), CRO @c3298523cc/bc44e043ab + addendum 1 @7cf9824434 (102665 conditions; GO 102698 with BEFORE figures on qfxZ0DzB: NEW-01 refusal, control 5.93%, ..3510 196.32%, ..2297 145.08%, ..0090 8.41%, INF 7.98%, COT DEPENDENCY_UNAVAILABLE). Gold precondition: E4-AC3 + E3-AC4 PASS on the issuer's re-run after the v0.21 ruling-18 re-emit (DS~E @bf1683f172). Live before 10:0xZ: CodeSha qfxZ0DzB. Fresh plans == P1 (perf 0/2/0, shared 0/1/0); S3 latest version 3donK_gT == hD7G6YT1 before apply. safe-apply performance (HALT_ACK=1, 0 STOP) rc 0 10:14:18Z: 0/2/0; safe-apply shared-infra rc 0 10:17:40Z: 0/1/0 (49F named-refusal gap ~3 min, as the packet named). READBACK: CodeSha256 hD7G6YT1o5ibIocQCn9uApRtV108eHkX6aq+w43EK8I= Active/Successful 10:14:14Z; role irpt-performance-retained-policy ReadHoldingsGoldPartitionInventory (s3:prefix irpt/49financial/gold/holdings_performance_daily/) + ReadHoldingsGoldPartitions (.../date=*/data.parquet); bucket DenyPerformanceAdapter{Reads,Listing}OutsideTheHoldingsGold on irpt/49financial/gold/holdings_performance_daily/*. Real cold-start invoke: 200, Init, FunctionError None, 0 Traceback, named envelope. Re-plan both roots: No changes. Rollback: S3 version 5bmwADQs (qfxZ0DzB) + revert ae20e904e6's two .tf files. | CLOSED 20260929T102106Z |
| A1 | verify | the Performance page, both readers | 49F OPAL_HOLDINGS figures; engine reports not reopened; the two S195 accounts not served as implausible; COT/INF unchanged |  | OPEN |

## Log

- 20260929T074357Z OPENED by 2.0.0_SA_COO~P with 4 leg(s)
- 20260929T074459Z LEG U1 closed: Built 07:3xZ while the superseded ledger irpt-adapter-holdings-gold-49f-20260929 was still open (this r2 entry opened at
- 20260929T074609Z LEG P1 closed: Fresh plans 07:4xZ (-lock=false, -out): performance root 0/2/0 -- aws_iam_role_policy.performance_retained (engine prefi
- 20260929T102106Z LEG D1 closed: Halves at HEAD naming blob a4679360: CTO @50e2dcdafe + c873a29dc6 (102650; precondition met, 102648/102650), CRO @c32985
