# Deploy Completion Record
**Date opened:** 2026-10-08T19:08:57.468362+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / BD positions_cube has no partition past 2026-10-06; leg needs C_06 to rebuild. Measured 2026-10-09 ~01:2xZ by 2.0.0_SA_COO~M1: the 2026-10-08 23:00Z fire (log gold_incremental_2026-10-09_20261009_011552.log) ran COMPLETE exit 0, 29 of 29 done rc=0, but C_06 read 'Watermark: 2026-10-06 ... To process: 0 ... No new partitions -- artifacts are current' and returned before the merge, so no C06-RETAINED-RECLASS line and gold/views/mix_daily_summary.json unchanged (05:26:01Z 10-08). platinum/firm/mix_summary.json rewritten 00:46:44Z (VersionId J.tOphoPr...): mix.unclassified 6.94 pct byte-equal to the pre-fire version; composition.unclassified 1116 sec / $142.50M -> 58 sec / $1.41M (D_03/D_04 carry e76). (held since 2026-10-09T01:22:37.472809+00:00)
**Deploy:** MDPF_SECCLASS SC-e-75: deploy data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py (retained dated entries outside the six reclassified) to s3://opal-data-bd/code/gold/; the next scheduled BD gold fire heals 141 holdings on 105 dated entries of 36 envelopes and D_04 republishes 36 concentration files. Bucket versioning Enabled; pre-fire VersionIds of 108 keys (36 envelopes, 36 client_timeseries, 36 concentration) in E75_PREFIRE_VERSIONS_20261008.json. Code rollback: VersionId xypYDUXvKLIIDTKDioI34eU4XQnb.NDY. Halves: COO SIGNED @fd0886f7da, CTO SIGNED @0ca2c444c7 (conditions 1-3).
**Authored by:** 2.0.0_SA_COO~M1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| V | verify | get-bucket-versioning Enabled and the 72 pre-fire VersionIds recorded before the deploy | the versioning read and the version file | 2026-10-08 ~19:1xZ, 2.0.0_SA_COO~M1: s3api get-bucket-versioning opal-data-bd -> Status Enabled; head-object VersionIds of 108 of 108 keys recorded (36 gold/entities/clients/{rid}.json + 36 gold/client_timeseries/{rid}.json = the 72 of CTO condition 1, plus 36 platinum/clients/{rid}/concentration.json), 0 missing, in MDPF_SECCLASS_M/E75_PREFIRE_VERSIONS_20261008.json; code rollback VersionId xypYDUXvKLIIDTKDioI34eU4XQnb.NDY (LastModified 2026-10-07T04:16:19Z). | CLOSED 20261008T190907Z |
| D | s3-prefix | C_06 served at s3://opal-data-bd/code/gold/ equals the repo bytes | safe-deploy SHA verify / comp-pipescript deployed MATCH line | 2026-10-08 19:09:16Z: safe-deploy 'DEPLOYED [bd] data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py' + 'VERIFY OK comp-pipescript deployed ...C_06...'; head-object VersionId 91ldXB2hFlCbFssz6_IvjctWrqNE4JGt ETag d7eb83b655b63143c24552bdfff197ad = md5 of the repo file. Side effect named: safe-deploy also re-shipped 3 _shared modules to code/gold/lib/_shared/; 2 byte-identical (DELTA=0), etf_classification_scheduled.py changed bytes (e65 amendment 3, owned by ledger secclass-e65b-namekey-deploy-s-20261007) and was RESTORED to prior VersionId keWIVX74... bytes at 19:10:11Z (new VersionId YoJkpC5X..., ETag 3f1e6be8... = prior). Row MDPF_SECCLASS-D1-S12. | CLOSED 20261008T191044Z |
| G | verify | after the next scheduled BD gold fire: multi_asset census = 0 across the 36 concentration keys and the C06-RETAINED-RECLASS line in that fire's log | served_multi_asset_split.py output and the log line |  | OPEN |

## Log

- 20261008T190857Z OPENED by 2.0.0_SA_COO~M1 with 3 leg(s)
- 20261008T190907Z LEG V closed: 2026-10-08 ~19:1xZ, 2.0.0_SA_COO~M1: s3api get-bucket-versioning opal-data-bd -> Status Enabled; head-object VersionIds 
- 20261008T191044Z LEG D closed: 2026-10-08 19:09:16Z: safe-deploy 'DEPLOYED [bd] data/black_diamond/scripts/gold/C_06.client_mix_timeseries.py' + 'VERIF
- 20261009T012237Z HELD-SOVEREIGN-GATED gate=external/BD positions_cube has no partition past 2026-10-06; leg needs C_06 to rebuild. M
