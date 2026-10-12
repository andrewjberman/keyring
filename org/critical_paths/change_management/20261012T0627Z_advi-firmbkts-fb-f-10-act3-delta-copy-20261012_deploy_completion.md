# Deploy Completion Record
**Date opened:** 2026-10-12T06:27:16.257900+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261012T073449Z
**Deploy:** ADVI_FIRMBKTS TO-FB-f-10 (window act 3, GO AMENDMENT 3 @b375e17c9d): the DELTA COPY of a fresh manifest of the 11 served classes of opal-data-bd into s3://opal-data-49financial/advi/49financial/platinum/ -- OVERWRITES about 49,000 keys round 2's copy wrote (the first copy never overwrote); --keep-newer-than MOVE_TS 2026-10-12T06:22:08Z; per-key rollback = the destination's prior VersionId from F7_DELTA_ROLLBACK.tsv (versioning Enabled); pair COO half @9ece707d55 + ADDENDUM 1 @3c47103dc7, CTO half @cb9fa20806; deletes nothing, writes only keys the manifest names; inert until act 4
**Authored by:** 0.7.0_AE_CloudOps~FB1
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 8.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | pre-write reads: pair bytes and SIGNED, the authorization at prefix grain (9 reads, Delete control explicitDeny), destination versioning Enabled, MOVE_TS and the legacy-quiet read | the entry carries the read lines | COO half 9ece707d55 + ADDENDUM 1 3c47103dc7 and CTO half cb9fa20806 (signed after the addendum's last commit) SIGNED, 0 uncommitted; authorization at prefix grain: dest PutObject/GetObject/GetObjectVersion/ListBucket/ListBucketVersions and src GetObject/GetObjectVersion/ListBucket allowed, DeleteObject control explicitDeny; destination versioning Enabled; MOVE_TS 2026-10-12T06:22:08Z | CLOSED 20261012T063001Z |
| L2 | verify | step 2 and 3: manifest --out F7_MANIFEST_2.tsv.gz and manifest --verify (the ownership key printed placed by name), residue --record before | MANIFEST VERIFIED line, the manifest sha256 and count, the residue counts before | manifest F7_MANIFEST_2.tsv.gz 53031 objects, 11 classes, placed=53031 refused=0 destination-collisions=0, MANIFEST VERIFIED: every key placed once by address(); tool sha256 fc9daf11bb07f1120aa50290bbe72c492d58ce6a1d978ff634281b8a8ba2384c; residue before: _campaign/ 1 key, gold/advi/ 26414 keys | CLOSED 20261012T063002Z |
| L3 | verify | step 4 plan, read-only: absent, equal, differs, kept-newer, refused printed, the ownership key by name; refused above 0 is a STOP | the plan line quoted | plan read-only 06:29Z: DELTA PLAN objects=53031 absent=121 equal=3800 differs=49110 kept-newer=0 refused=0; OVERWRITES=49110 destination-versioning=Enabled source-changed-since-manifest=0; the ownership key printed by name in the entry (differs: destination is the older copy) | CLOSED 20261012T063002Z |
| L4 | activation | step 4 apply --execute in bounded runs to DELTA COMPLETE with stale-source=0 errors=0; F7_DELTA_ROLLBACK.tsv written and fsynced before each overwrite | the completion line and the rollback record row count | apply 06:48:43Z-07:31:39Z: ROLLBACK RECORD rows=49110 (49110 unique, fsynced before the first copy), DELTA RUN copied=49231 stale-source=0 errors=0 not-reached(budget)=0, DELTA COMPLETE; 49231 = 121 created + 49110 overwritten; kept-newer=0; two earlier runs killed by this lane's own outer timeouts before any copy (no key overwritten; partial record archived outside the repo; row ADVI_FIRMBKTS-D1-S35) | CLOSED 20261012T073449Z |
| L5 | verify | AC1 manifest --verify, AC2 compare DEST-VS-MANIFEST EQUAL (or the differing keys exactly the kept-newer set), AC3 residue --check unchanged; the ownership key by name as equal or kept-newer with LastModified | the three outputs quoted | plan after absent=0 equal=53031 differs=0 refused=0 NOTHING TO DO; AC1 MANIFEST VERIFIED: every key placed once by address(); AC2 DEST-VS-MANIFEST: EQUAL (present 53031 missing 0 mismatch 0 extras 0), SOURCE-VS-MANIFEST: UNCHANGED, COPY-COMPLETE; AC3 RESIDUE UNCHANGED gold/advi/ 26414 and _campaign/ 1 before after now; ownership key by name EQUAL (ETag 5227d27ddc591c681daa9aad5f5f9d1d, destination LastModified 2026-10-12T07:29:12Z, prior destination version XS0wkMtSm5c3ZZOOjsIri5FCmtD8rQvm) | CLOSED 20261012T073449Z |
| L6 | git | proof instance, second manifest, rollback record and residue records written, status flipped complete in one commit | commit hash | proof instance, second manifest, rollback record (49110 rows) and residue records committed with this entry under deliverables/0.7.0_AE_CloudOps~FB1/act3/ (amendment 4 a27bd4facc); TO-FB-f-10 status flipped complete in the same commit; commit hash is this commit | CLOSED 20261012T073449Z |

## Log

- 20261012T062716Z OPENED by 0.7.0_AE_CloudOps~FB1 with 6 leg(s)
- 20261012T063001Z LEG L1 closed: COO half 9ece707d55 + ADDENDUM 1 3c47103dc7 and CTO half cb9fa20806 (signed after the addendum's last commit) SIGNED, 0 
- 20261012T063002Z LEG L2 closed: manifest F7_MANIFEST_2.tsv.gz 53031 objects, 11 classes, placed=53031 refused=0 destination-collisions=0, MANIFEST VERIF
- 20261012T063002Z LEG L3 closed: plan read-only 06:29Z: DELTA PLAN objects=53031 absent=121 equal=3800 differs=49110 kept-newer=0 refused=0; OVERWRITES=4
- 20261012T073449Z LEG L4 closed: apply 06:48:43Z-07:31:39Z: ROLLBACK RECORD rows=49110 (49110 unique, fsynced before the first copy), DELTA RUN copied=49
- 20261012T073449Z LEG L5 closed: plan after absent=0 equal=53031 differs=0 refused=0 NOTHING TO DO; AC1 MANIFEST VERIFIED: every key placed once by addre
- 20261012T073449Z LEG L6 closed: proof instance, second manifest, rollback record (49110 rows) and residue records committed with this entry under delive
- 20261012T073449Z CLOSED -- all 6 legs proven

## STEPS 1 TO 3 -- READS, MANIFEST, PLAN (0.7.0_AE_CloudOps~FB1, 2026-10-12T06:30:01Z; GO = AMENDMENT 3 @b375e17c9d)

- **Pair:** COO half `9ece707d55` + round-4 ADDENDUM 1 `3c47103dc7`; CTO half `cb9fa20806` (signed 2 minutes AFTER the addendum's last
  commit, so at its current bytes); 0 uncommitted. **The act OVERWRITES about 49,000 keys at the new home that round 2's copy wrote;
  round 2's copy never overwrote one.** Blast radius: the fresh manifest's keys and no other.
- **MOVE_TS** `2026-10-12T06:22:08Z` (act 2's entry `advi-firmbkts-fb-f-9-act2-mode-move-dell1-20261012`); legacy-quiet read 0 keys of 11 classes
  at 06:22:38Z. `--keep-newer-than 2026-10-12T06:22:08Z`.
- **Authorization (the CTO's condition), one resource per call, prefix grain, this identity's own ARN:** destination PutObject, GetObject,
  GetObjectVersion, ListBucket (prefix context), ListBucketVersions all `allowed`; source GetObject, GetObjectVersion, ListBucket `allowed`;
  the control DeleteObject on the destination `explicitDeny`. No grant created. Destination versioning `Enabled`.
- **Manifest (step 2):** `F7_MANIFEST_2.tsv.gz`, 53,031 objects, 11 classes, `placed=53031 refused=0 destination-collisions=0`,
  `MANIFEST VERIFIED: every key placed once by address()`. Tool sha256 `fc9daf11bb07f1120aa50290bbe72c492d58ce6a1d978ff634281b8a8ba2384c`;
  file sha256 `6f260b0bf4ee3f791a7c3005c572a300d5f6d0c51cf194db91066842bcf32501`, 1,481,001 bytes. Classes: gold/artifacts 44, gold/entities/accounts 8,574, gold/entities/advisors 779,
  gold/entities/clients 18,230, gold/platinum/firm 2, gold/views 10, platinum/49financial 1, platinum/accounts 7,586, platinum/advisors 988,
  platinum/clients 16,802, platinum/firm 15.
- **Residue before (step 3):** `_campaign/` 1 key (newest 2026-08-30T02:33:41Z); `gold/advi/` 26,414 keys (newest 2026-10-11T12:48:21Z).
- **PLAN (step 4, read-only, 06:29:00Z-06:29:21Z):** `DELTA PLAN objects=53031 absent=121 equal=3800 differs=49110 kept-newer=0 refused=0`;
  `OVERWRITES=49110 destination-versioning=Enabled source-changed-since-manifest=0`. 121 = 53,031 minus round 2's 52,910; 49,110 is the number
  the pair states. REFUSED 0, no class outside the 11.
- **The ownership key, BY NAME (read before the first write):**
  - source `opal-data-bd/platinum/49financial/ownership_map.json`: VersionId=FcsnGhU7Rt280E9rmDacateI5WiK8S28 ETag=5227d27ddc591c681daa9aad5f5f9d1d LastModified=2026-10-12T05:22:13Z len=474841
  - destination `opal-data-49financial/advi/49financial/platinum/49financial/ownership_map.json`: VersionId=XS0wkMtSm5c3ZZOOjsIri5FCmtD8rQvm ETag=9fb395c2744c79ac51ff0e3400fddfca LastModified=2026-10-11T04:01:18Z len=474726
  - same ETag and size: **NO (as the plan says)**. The plan classes it `differs` (the destination is the older copy), so the act overwrites it with the
    source version and records the destination's prior VersionId; its LastModified after the act is read at step 5.

## ARTIFACT LOCATION (0.7.0_AE_CloudOps~FB1, 2026-10-12T06:3xZ)

The order's `<paths>` and criteria name `deliverables/0.9.0_WK_ADVI_FIRMBKTS~11/` (round 3's worker folder). The lane rule
(`TREE_DELIVERABLES`, owned-paths clause 4) admits only the serial the sub-folder names, and `safe-commit` REFUSED the first commit
(`F7_RESIDUE_before.json` under that folder; no override was used). This lane's artifacts are therefore committed under
`deliverables/0.7.0_AE_CloudOps~FB1/act3/`: the second manifest, the residue records, the plan, the rollback record and the instance.
Four generated copies remain UNTRACKED in the worker folder (a `rm` of them was blocked by the harness); they are byte-equal (sha256
verified) to the committed copies and are not to be committed from there. The issuer's amendment must point `<paths>` and the three
criteria at this folder before the status can flip.

## STEPS 4 AND 5 -- THE DELTA APPLIED AND READ (0.7.0_AE_CloudOps~FB1, 2026-10-12T07:34:48Z)

- **Apply (one full run, no outer timeout):** 2026-10-12T06:48:43Z to 07:31:39Z. `ROLLBACK RECORD ... rows=49110` then
  `DELTA RUN copied=49231 stale-source=0 errors=0 not-reached(budget)=0` then `DELTA COMPLETE: re-run plan`. 49,231 = 121 keys created
  (ABSENT) + 49,110 overwritten (DIFFERS). `kept-newer=0` (no producer wrote the canonical home since MOVE_TS). `evidence act3/F7_ACT3_APPLY_RUN.txt`.
- **Rollback record:** `F7_DELTA_ROLLBACK.tsv`, 49,110 rows, 49,110 unique keys, sha256 `c7e64bf7eeedf1dd7df6b60597837f57caf62bf1a99f90efd911e0e0c7c43e04`: destination key, prior VersionId, prior ETag,
  prior size, per overwritten key, complete and fsynced before the first copy. Rollback is `r3_f7_delta.py rollback --record <that file> --execute`.
  The 121 created keys have no prior version and stay (inert).
- **Two earlier runs were killed by this lane's own outer timeouts** (590 s and 150 s) before any copy: no key was overwritten (30 of 30
  sampled recorded keys still at their prior VersionId; the plan unchanged at differs=49110). Their partial record (11,909 then 14,415 rows,
  2,506 duplicates) was archived outside the repo before the full run. Row `ADVI_FIRMBKTS-D1-S35`.
- **Plan after:** `DELTA PLAN objects=53031 absent=0 equal=53031 differs=0 kept-newer=0 refused=0 (denominator: manifest objects) /   OVERWRITES=0 destination-versioning=Enabled source-changed-since-manifest=0 / DELTA PLAN: NOTHING TO DO (every manifest key present and equal)`
- **AC1:** `MANIFEST VERIFIED: every key placed once by address()` (53,031 objects, 11 classes, refused 0, collisions 0).
- **AC2:** `DEST-VS-MANIFEST: EQUAL`; DEST present=53031 missing=0 mismatch=0 extras=0; `SOURCE-VS-MANIFEST: UNCHANGED changed=0 gone=0`;
  `COPY-COMPLETE: every manifest key present and equal`.
- **AC3 / residue after:** `_campaign/` 1 key and `gold/advi/` 26,414 keys, before = after = now: `RESIDUE UNCHANGED`.
- **The ownership key, BY NAME, after:** source `opal-data-bd/platinum/49financial/ownership_map.json` VersionId
  `FcsnGhU7Rt280E9rmDacateI5WiK8S28`, ETag `5227d27ddc591c681daa9aad5f5f9d1d`, LastModified 2026-10-12T05:22:13Z, 474,841 bytes; destination
  `opal-data-49financial/advi/49financial/platinum/49financial/ownership_map.json` VersionId `HXMgugyoEpzWQF_6VFAt.MMOklh53bK2`, ETag
  `5227d27ddc591c681daa9aad5f5f9d1d`, LastModified 2026-10-12T07:29:12Z (the delta's own write, after MOVE_TS), 474,841 bytes: **EQUAL**. Prior
  destination version (the rollback for this key): `XS0wkMtSm5c3ZZOOjsIri5FCmtD8rQvm` (2026-10-11T04:01:18Z, 474,726 bytes).
- **Blast radius held:** only keys the manifest names were written, all in `opal-data-49financial`; `opal-data-bd` was read only; no delete.
- **Not mine, as ordered:** the CTO's exercised read (`compare` re-run with `FB-f-1`'s instrument).
