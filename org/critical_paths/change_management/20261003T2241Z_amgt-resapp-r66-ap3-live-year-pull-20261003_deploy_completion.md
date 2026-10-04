# Deploy Completion Record
**Date opened:** 2026-10-03T22:41:17.858139+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261003T230148Z
**Deploy:** AMGT_RESAPP round 66 AMGT-ap-3: ONE live Bloomberg PX_LAST year pull (95 tickers, 2025-08-28..2026-10-02) on Andrew's per-use word card 4; writes one bronze object and four 90D/365D generation partitions
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-data-harvest bloomberg/harvest/bronze/price_history_px_last/date=2026-10-02/year_pull.json | the run's vendor request count plus the S3 key head-object size | ONE live run, exit=0, 22:44:21Z-22:44:55Z. Vendor word card 4 @9fe6e6f111 verified in committed bytes BEFORE the call. 95 of 95 ticker(s) usable series, 0 insufficient, excluded 0 (no Bloomberg form). LANDED s3://opal-data-harvest/bloomberg/harvest/bronze/price_history_px_last/date=2026-10-02/year_pull.json put_performed=True existed=False (write-once, nothing overwritten). head-object: ContentLength 562248 B, VersionId 6d2NH.kpXFWSYT5McZXVDLT6j0PRyzkk, LastModified 2026-10-03T22:44:48Z, SSE AES256, Metadata document-sha256=33b4b04972828326e858ead222f2e2923a7ad543512480ec3454283c3f806ae1 which EQUALS the sha256 the run printed. Window 2025-08-28..2026-10-02 (400 calendar days, end = lib.trading_calendar.prev_trading_day), equal to the --plan read and to the issuer's. | CLOSED 20261003T225859Z |
| L2 | activation | the four generation partitions TRENDING_PRICE_90D/365D and BREAKOUT_PRICE_90D/365D at #2026-10-02 | rows written per generation; any write to a 30-day partition or pointer is a STOP | FOUR generations COMPLETE, pointer_written=True each, failed axes=[]. Rows MEASURED on opal-harvest-security-metrics, not taken from the run log, and all four MATCH it: TRENDING_PRICE_90D 94, BREAKOUT_PRICE_90D 94, TRENDING_PRICE_365D 95, BREAKOUT_PRICE_365D 95. Pointers at <axis>#2026-10-02/_CURRENT carry this run's generation ids (20261003T224449Z-b4a154111210, 20261003T224451Z-134867eed5bb, 20261003T224453Z-904e073ee178, 20261003T224453Z-065b739b3403) written_at 2026-10-03T22:44Z. THE 30-DAY STOP DID NOT FIRE, measured on the live table with a positive control: the 30-day axes are DIFFERENT partition keys (TRENDING_PRICE#2026-10-02, BREAKOUT_PRICE#2026-10-02); each holds exactly 1 item, its _CURRENT pointer, at generation 20261003T110628Z-4ff62071cb80 and 20261003T110629Z-d4cfe7cba7f3 written_at 2026-10-03T11:06Z -- the morning daily job, 11h38m BEFORE this run. The same instrument reads 22:44Z on the four axes this run wrote, so it discriminates and the 30-day untouched verdict is not a blind read. No 30-day partition and no 30-day pointer was written. | CLOSED 20261003T225957Z |
| L3 | verify | AC1 r66 c22 local from the pin checkout and AC2 r64 c10 deployed DELTA=0 against the pre-run baseline | each check verdict line with exit=0 | BOTH CRITERIA PASS, graded from the pin checkout at 8f10187a78. AC1 r66 c22 --where local: 'R66 C22 SERVED: YES', exit=0, 4 of 4 clauses -- trending price days=90 rows 94 window_days 90 window_end 2026-10-02 last 2026-10-02 note '' reason ''; days=365 rows 95; breakout price days=90 rows 94; days=365 rows 95. Base per the issuer's comp-adversary was 0 rows and 'not produced yet' local AND deployed, so this is a movement, not a standing truth. AC2 r64 c10 --where deployed: 'R64 C10 SERVED: YES', exit=0, 8 of 8, and DELTA=0 EXACTLY -- every one of the 8 lines is byte-identical to the pre-run baseline captured on the same instrument and tree before the pull (trending and breakout default/30 serve 94 rows at window_days 30; days 90 and 365 serve 0 rows with the identical 'not produced yet' reason string). That is the served proof that the deployed code reads only the 30-day partitions and the new generations are invisible to it. Rollback not applicable: write-once object, no overwrite, no delete. | CLOSED 20261003T230046Z |

## Log

- 20261003T224117Z OPENED by 0.7.0_AE_CloudOps~A with 3 leg(s)
- 20261003T225859Z LEG L1 closed: ONE live run, exit=0, 22:44:21Z-22:44:55Z. Vendor word card 4 @9fe6e6f111 verified in committed bytes BEFORE the call. 9
- 20261003T225957Z LEG L2 closed: FOUR generations COMPLETE, pointer_written=True each, failed axes=[]. Rows MEASURED on opal-harvest-security-metrics, no
- 20261003T230046Z LEG L3 closed: BOTH CRITERIA PASS, graded from the pin checkout at 8f10187a78. AC1 r66 c22 --where local: 'R66 C22 SERVED: YES', exit=0
- 20261003T230148Z CLOSED -- all 3 legs proven
