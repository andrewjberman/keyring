# Deploy Completion Record
**Date opened:** 2026-10-12T06:27:16.257900+00:00
**Status:** OPEN
**Deploy:** ADVI_FIRMBKTS TO-FB-f-10 (window act 3, GO AMENDMENT 3 @b375e17c9d): the DELTA COPY of a fresh manifest of the 11 served classes of opal-data-bd into s3://opal-data-49financial/advi/49financial/platinum/ -- OVERWRITES about 49,000 keys round 2's copy wrote (the first copy never overwrote); --keep-newer-than MOVE_TS 2026-10-12T06:22:08Z; per-key rollback = the destination's prior VersionId from F7_DELTA_ROLLBACK.tsv (versioning Enabled); pair COO half @9ece707d55 + ADDENDUM 1 @3c47103dc7, CTO half @cb9fa20806; deletes nothing, writes only keys the manifest names; inert until act 4
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-write reads: pair bytes and SIGNED, the authorization at prefix grain (9 reads, Delete control explicitDeny), destination versioning Enabled, MOVE_TS and the legacy-quiet read | the entry carries the read lines |  | OPEN |
| L2 | verify | step 2 and 3: manifest --out F7_MANIFEST_2.tsv.gz and manifest --verify (the ownership key printed placed by name), residue --record before | MANIFEST VERIFIED line, the manifest sha256 and count, the residue counts before |  | OPEN |
| L3 | verify | step 4 plan, read-only: absent, equal, differs, kept-newer, refused printed, the ownership key by name; refused above 0 is a STOP | the plan line quoted |  | OPEN |
| L4 | activation | step 4 apply --execute in bounded runs to DELTA COMPLETE with stale-source=0 errors=0; F7_DELTA_ROLLBACK.tsv written and fsynced before each overwrite | the completion line and the rollback record row count |  | OPEN |
| L5 | verify | AC1 manifest --verify, AC2 compare DEST-VS-MANIFEST EQUAL (or the differing keys exactly the kept-newer set), AC3 residue --check unchanged; the ownership key by name as equal or kept-newer with LastModified | the three outputs quoted |  | OPEN |
| L6 | git | proof instance, second manifest, rollback record and residue records written, status flipped complete in one commit | commit hash |  | OPEN |

## Log

- 20261012T062716Z OPENED by 0.7.0_AE_CloudOps~FB1 with 6 leg(s)
