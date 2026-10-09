# Deploy Completion Record
**Date opened:** 2026-10-08T19:08:57.468362+00:00
**Status:** HELD-SOVEREIGN-GATED -- gate: external / 1.0.0_SA_CTO~DELL1 ruling on a ONE-relationship widening. Leg G's literal criteria are MET on the 2026-10-09 04:00Z fire (log gold_incremental_2026-10-09_20261009_061917.log COMPLETE exit 0, 29/29 rc=0, C_06 'To process: 1', 'C06-RETAINED-RECLASS entries=262 holdings=298'; 3,354 concentration keys 0 multi_asset; 36/36 signed envelopes 0 multi_asset). The 298 = 141 multi_asset (84 ->equity, 57 ->fixed_income) in the 36 signed envelopes, as predicted, PLUS 157 'other'->commodities (PDBC, 157 retained dates) in gold/entities/clients/z08296368.json, OUTSIDE the signed 36 (R13_CHECKS/e75_retained_reclass_diff.py over 18,176 envelopes, E75_RETAINED_RECLASS_DIFF_20261009.json). Rollback targets recorded: envelope 8YWPRKyK... (10-08 05:25:03Z), client_timeseries XCWaYCxw... (10-08 05:25:03Z), platinum concentration Ns1L1OCm... (10-09 00:51:26Z). (held since 2026-10-09T06:37:41.375070+00:00)
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
- 20261009T063740Z HOLD RELEASED -> OPEN
- 20261009T063741Z HELD-SOVEREIGN-GATED gate=external/1.0.0_SA_CTO~DELL1 ruling on a ONE-relationship widening. Leg G's literal criter
