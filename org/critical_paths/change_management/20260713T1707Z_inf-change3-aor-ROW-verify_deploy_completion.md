# Deploy Completion Record
**Date opened:** 2026-07-13T17:07:21.216841+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260716T132930Z -- gate: external / The scheduled inf-accounts-v2-daily run at cron(22 13 * * ? *) = 13:22Z. NOT to be forced. TWO independent reasons, and COO's is the stronger one I had missed: (1) an ad-hoc invoke REWRITES snapshot_date=2026-07-13 IN PLACE -- that partition ALREADY EXISTS (873 rows, written 13:22:50Z today) and accounts_v2 uses a FIXED key per date, so a re-emit OVERWRITES BYTES. That is the in-place-partition-rewrite hazard we documented this morning (6 of 69 accounts_v2 partitions rewritten after their own snapshot_date). (2) this lambda calls the ORION VENDOR API, so an ad-hoc run is agent-initiated vendor egress AND an ad-hoc validation run (NEVER#4's spirit: validate on the SCHEDULED run's artifacts, never one you manufactured to validate against). NOTHING IS BLEEDING: the gold chain is HELD (INF_GOLD_DISPATCH_HOLD applied, both trigger rules DISABLED -- COO re-verified), the fold switch is OFF, and nothing is served. There is no reason to buy 20 hours with an in-place rewrite. THE ACCEPTANCE READ IS COO'S, NOT MINE (the verifier is not the do-er). (held since 2026-07-13T17:07:21.376596+00:00)
**Deploy:** CHANGE-3 AoR: THE ROW. Re-opened because I closed inf-change3-aor-consumer-ship on a DEPLOY when the bar was a ROW -- COO is right and the close was premature.
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 24.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | advisor_of_record_raw PRESENT in a LIVE accounts_v2 partition PRODUCED BY THE DEPLOYED lambda (scheduled run, cron 13:22Z) | READ THE ROW: expect ~837/873 non-null (95.9%); a coverage figure BELOW that is a signal, and 873/873 is ALSO a signal; distinct values exactly {Peter Lee, Joe Brandenburg, Patrick Scanlan, Noel Soderblom, Scanlan_IWM, Soderblom_IWM}. POSITIVE CONTROL on the read: rep_id present (so an absence is a REAL absence). | 13:22Z scheduled-fire row read: s3://opal-data-inf/silver/api_dims/accounts_v2/snapshot_date=2026-07-16/data.parquet LM=2026-07-16T13:22:52Z ETag=88bc5b2d46a838112d273b1418c06a83 80217B (pre-fire baseline 12:57Z = run-7 ETag a022a448/80207B/02:49:02Z -- flip proves scheduled-run provenance; sentinel absent-13:16Z -> present-13:22:52Z second discriminator). advisor_of_record_raw 837/874=95.8% (exact pre-registered numerator; neither below-ratio nor 100% signal); distinct set exact-6 {Peter Lee, Joe Brandenburg, Patrick Scanlan, Noel Soderblom, Scanlan_IWM, Soderblom_IWM} missing NONE extra NONE; POSITIVE CONTROL rep_id 874/874; row drift 873->874 disclosed, matches run-7 SSOT. Two independent readers byte-agree (lambda STEP3 print vs parquet read). Invoke 0f375bb1 statusCode 200. COO ACCEPTANCE: inbox 20260716T132723Z (acceptance read was COO's per ledger terms). | CLOSED 20260716T132849Z |

## Log

- 20260713T170721Z OPENED by 0.7.0_AE_CloudOps with 1 leg(s)
- 20260713T170721Z HELD-SOVEREIGN-GATED gate=external/The scheduled inf-accounts-v2-daily run at cron(22 13 * * ? *) = 13:22Z. NOT to 
- 20260716T132849Z LEG L1 closed: 13:22Z scheduled-fire row read: s3://opal-data-inf/silver/api_dims/accounts_v2/snapshot_date=2026-07-16/data.parquet LM=
- 20260716T132930Z CLOSED -- all 1 legs proven
