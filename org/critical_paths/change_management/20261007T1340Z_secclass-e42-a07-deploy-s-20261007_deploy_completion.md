# Deploy Completion Record
**Date opened:** 2026-10-07T13:40:44.165821+00:00
**Status:** OPEN
**Deploy:** MDPF_SECCLASS SC-e-42: canonical-first a07 uploaded from the LAPTOP box (dell1's principal is denied opal-data-49financial, rows W25-S1/W32-S4) to the ONE key s3://opal-data-49financial/_code/a07_dim_asset_classification.py; candidate 88c7018366 md5 4092c5b80469ab780040a842eebe13cb; BEFORE IsLatest VersionId 72tSRnxMSKkBdtgAJZtqQcHeebqACIl1 ETag 9202d701c552d4fb38a40f975f0eae9e (34289 B, 2026-09-01T14:12:21Z); ROLLBACK = copy VersionId 72tSRnxMSKkBdtgAJZtqQcHeebqACIl1 back over that key, then re-run a07 for the affected date; halves COO (SIGNED, on CLOUD) + CTO (attested SIGNED @b3092be6d2, bytes UNREACHABLE from this device -- see leg L1 note); window 30h because the verify leg cannot close before the next scheduled chain run (2026-10-08 12:45Z floor)
**Authored by:** 0.7.0_AE_CloudOps~S
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 30.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-data-49financial _code/a07_dim_asset_classification.py -- the ONE key in the upload plan (file_to_s3_target advi; second_targets_for [] ; shipped_artifacts [] ; bundle None). MOVES ETag 9202d701 -> 4092c5b8. Rollback VersionId 72tSRnxMSKkBdtgAJZtqQcHeebqACIl1 | comp-pipescript deployed MATCH row + head-object ETag 4092c5b80469ab780040a842eebe13cb + AC1 e42_a07_etag_check.py ok=True |  | OPEN |
| L2 | verify | the FIRST scheduled chain run after the upload (advi-49f-gold-floor cron(45 12 * * ? *) UTC, next 2026-10-08T12:45Z; or an earlier advi.49f.silver-accelerator fire on a qualified Schwab closure) -- read the dim's A5-A07-SOURCE-CENSUS line and the d06/d08 mix totals, and compare every class move against A07_SWITCH_BEFORE_AFTER_20261007.json (COO condition 6, CTO condition 7); any move the JSON does not list is a ROLLBACK | the run id + the census line + both mix totals + the move-set comparison |  | OPEN |

## Log

- 20261007T134044Z OPENED by 0.7.0_AE_CloudOps~S with 2 leg(s)
