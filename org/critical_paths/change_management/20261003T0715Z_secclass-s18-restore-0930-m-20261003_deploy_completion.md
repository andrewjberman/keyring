# Deploy Completion Record
**Date opened:** 2026-10-03T07:15:22.422417+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS-S18 disarm: BD served state back to as_of 09-30 (CTO batch 213 item 1; CTO half CTO_HALF_S18_RESTORE_0930_SERVED_20261003.md @5ec7db4eea; next fire ruled batch 219: (a) hold + (b) watermark reset)
**Authored by:** 2.0.0_SA_COO~M
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| 0 | verify | runner stopped; no BD gold fire during the act | describe-instances + rule schedules | 07:1xZ: runner i-01003b035d2988dfb stopped (describe-instances); the BD gold fires are bd-gold-nightly-fallback cron(0 23 ? * MON-SAT *) and bd-canonical-prices-daily cron(0 4 * * ? *) (both target bd-gold-trigger, list-rule-names-by-target; the monthly rule is DISABLED), so no fire runs before 23:00Z. | CLOSED 20261003T071628Z |
| C | s3-prefix | copy-object of 23,542 served keys to their pre-04:00Z VersionIds (S18_RESTORE_SET_20261003.tsv), read back per key; 36 run-created keys left | restore result counts + read-back | 07:18:49Z-07:58:15Z s18_restore.py --write (8 threads; per key head-object check that the current VersionId is the run's, copy-object from the restore-to VersionId with MetadataDirective COPY, head read-back): 23,578 rows -> RESTORED 23,541, SKIP-CREATED 36 (run-created keys left, a restore there is a delete), REFUSED-REWRITTEN 0, READBACK-MISMATCH 1. The one mismatch, gold/views/client_tax_liability.parquet, is the ETag oracle on a multipart source (restore-to iK_J_hVO.. ETag 66d00ce8...-2; the copy is single-part, ETag 72528d90..., new VersionId HSp14cjv..): content read 08:0xZ, sha256 restored == restore-to (383cdf7ac190aecb, 11,880,824 bytes each), negative control run version klGFKwRO.. differs (c4ecf32a59efe74d, 11,749,700 bytes). So 23,542 restored in content, 0 refused. Result file R9_CHECKS/S18_RESTORE_RESULT_WRITE.tsv (rollback = each key's run VersionId in S18_RESTORE_SET_20261003.tsv). | CLOSED 20261003T080229Z |
| V | verify | served read: platinum/firm/mix_summary.json data_as_of 2026-09-30 at 1,843,114,311.70; one 335-set account's served AUA at its 09-30 value | served key reads | 08:1xZ served reads, opal-data-bd: platinum/firm/mix_summary.json VersionId 5ACI.iHP.. (07:58:18Z, the restore) data_as_of 2026-09-30, 8 classes, MV sum 1,843,114,311.70, pct sum 1.000000 (= the pre-run 09-30 version wma_kZ0X.. named in row S18). One 335-set account: platinum/accounts/z0812888131/summary.json VersionId c4DHYEqd.. (07:19:39Z) timeseries ends 2026-09-30 aua_canonical 27,904.62 (row S18's 09-30 value); negative control, the run's version jR92W0P9.., ends 2026-10-01 aua_canonical 0.00. Left as is under the half: the 36 run-created keys (platinum/clients x 28, platinum/accounts x 5, platinum/advisors/emma_satine x 3) and gold/ intermediates outside the set (gold/entities, gold/positions_cube 10-01), which the recompute overwrites (CTO batch 220). | CLOSED 20261003T080543Z |
| H | activation | disable bd-gold-nightly-fallback and bd-canonical-prices-daily before 23:00Z; read back State DISABLED | describe-rule x2 | 07:17Z aws events disable-rule, read back by describe-rule: bd-gold-nightly-fallback cron(0 23 ? * MON-SAT *) State DISABLED; bd-canonical-prices-daily cron(0 4 * * ? *) State DISABLED (both target bd-gold-trigger; the monthly rule was already DISABLED). Done by CLI as an operational hold: the Terraform state of these rules now differs from live until leg R re-enables them -- no apply of their root before leg R. | CLOSED 20261003T071810Z |
| R | activation | when the class cell lands: watermarks to 09-30 and the two rules re-enabled before Monday 04:00Z (else report by Sunday 18:00Z) | watermark reads + describe-rule x2 |  | OPEN |

## Log

- 20261003T071522Z OPENED by 2.0.0_SA_COO~M with 5 leg(s)
- 20261003T071628Z LEG 0 closed: 07:1xZ: runner i-01003b035d2988dfb stopped (describe-instances); the BD gold fires are bd-gold-nightly-fallback cron(0 2
- 20261003T071810Z LEG H closed: 07:17Z aws events disable-rule, read back by describe-rule: bd-gold-nightly-fallback cron(0 23 ? * MON-SAT *) State DISA
- 20261003T080229Z LEG C closed: 07:18:49Z-07:58:15Z s18_restore.py --write (8 threads; per key head-object check that the current VersionId is the run's
- 20261003T080543Z LEG V closed: 08:1xZ served reads, opal-data-bd: platinum/firm/mix_summary.json VersionId 5ACI.iHP.. (07:58:18Z, the restore) data_as_
