# Deploy Completion Record
**Date opened:** 2026-10-01T09:04:18.714738+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261001T120358Z
**Deploy:** IRPT_DASHBD round 1 DB-b-1: first mint of reporting gold account_return_daily + dim_return_method for 49financial over the six round-1 accounts, under contract 0.2.0 and PRD v0.5 rulings 17-21
**Authored by:** 0.4.0_DS_ClientPlatform~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | CLOUD: producer at bb8f3bb2d1 and contract 0.2.0 at 6a23aee53d | both hashes present on CLOUD and is-ancestor of the emitting HEAD | git merge-base --is-ancestor: bb8f3bb2d1 (producer, guard_state) ANCESTOR of the emitting HEAD; 6a23aee53d (contract 0.2.0) ANCESTOR. Negative control: bb8f3bb2d1 is NOT an ancestor of the older 0abf99fcd4, so the test discriminates. | CLOSED 20261001T120317Z |
| L2 | verify | s3://opal-data-49financial/irpt/49financial/gold/account_return_daily/ -- the day partitions | object listing read back from S3 with the partition count and summed row count, read from the LANDED parquet not the producer's stdout | Read back from S3, not from the producer's stdout: 559 parquet objects across 559 distinct date= partitions under irpt/49financial/gold/account_return_daily/, window 2024-07-08..2026-09-28, 1105 rows summed from the LANDED parquet. Matches the producer's claim of 559 days / 1105 rows independently. Prefixes were measured EMPTY before the mint with a positive control on a populated prefix, so this is a first mint. | CLOSED 20261001T120317Z |
| L3 | verify | s3://opal-data-49financial/irpt/49financial/gold/dim_return_method/method_version=1 -- one row | the landed row read back carrying the three measured numbers and the derived ceiling | dim_return_method/method_version=1: exactly 1 object, 1 row. method_version 1, method TWR_DAILY_GEOMETRIC, flow_convention END, income_basis cash_when_received, fee_basis GROSS_ONLY, tolerance 0.001244, large_flow_share 0.002535, band [-0.5, 0.5], comparability_max_excluded_weight 0.002488 (derived per amendment 6), day_count Account365, gips_alignment 'GIPS-aligned, not GIPS-compliant'. Only tieout_tolerance_proposed is null, which the order's own method spec requires (DB-b-3 fills it). | CLOSED 20261001T120317Z |
| L4 | verify | the served artifact conforms to contract 0.2.0 | schema_hash RECOMPUTED from the landed parquet equals 1b25d37ba6cfcf5a7413373ccdca57e306b86614aff94472ca65ca0025484946, every enum inside its declared set, guard_state non-null on every row, and zero rows carrying HOLDINGS_INCOME_FALLBACK | Conformance measured on the LANDED artifact: schema_hash RECOMPUTED from the landed parquet = 1b25d37ba6cfcf5a7413373ccdca57e306b86614aff94472ca65ca0025484946, equal to contract 0.2.0's declared value; 1 distinct schema across all 559 partitions (no drift), 19 fields; guard_state NULLS 0; rows carrying HOLDINGS_INCOME_FALLBACK 0 (ruling 17); non-finite total_return_daily 0 and emitted values outside the band 0 (ruling 19); zero values outside any declared set. Served guard_state: GRADED_AGREED 700, NOT_GRADED_OUTSIDE_DOMAIN 377, GUARD_NOT_REACHED 20, GRADED_DISAGREED 8. | CLOSED 20261001T120317Z |

## Log

- 20261001T090418Z OPENED by 0.4.0_DS_ClientPlatform~S with 4 leg(s)
- 20261001T120317Z LEG L1 closed: git merge-base --is-ancestor: bb8f3bb2d1 (producer, guard_state) ANCESTOR of the emitting HEAD; 6a23aee53d (contract 0.2
- 20261001T120317Z LEG L2 closed: Read back from S3, not from the producer's stdout: 559 parquet objects across 559 distinct date= partitions under irpt/4
- 20261001T120317Z LEG L3 closed: dim_return_method/method_version=1: exactly 1 object, 1 row. method_version 1, method TWR_DAILY_GEOMETRIC, flow_conventi
- 20261001T120317Z LEG L4 closed: Conformance measured on the LANDED artifact: schema_hash RECOMPUTED from the landed parquet = 1b25d37ba6cfcf5a7413373ccd
- 20261001T120358Z CLOSED -- all 4 legs proven
