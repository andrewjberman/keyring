# Deploy Completion Record
**Date opened:** 2026-10-14T12:41:29.650192+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T124327Z
**Deploy:** IRPT_ANLREQ TO-DELETE-C449-U7: delete the ONE version of the ONE synthetic stored input (full 64-hex 38104be4dc81abe6a67dcb837add8576df86a7cdecc21b08e5de6e33c58be29f) under irpt/49financial/state/normalized_portfolios/ in opal-data-irpt, by VersionId, ONE call, and nothing else. NOT RECOVERABLE (a deleted S3 version cannot be restored; the object is synthetic). AUTHORITY: Andrew verbatim '8.) Yes delete of synthetic leftover is approved.' (ANDREW_DIRECT_20261014_114xZ line 10; the act, not a seat, CTO msg 109130); issuer GO XB-20261014T123613Z-be5e after the dell2 ledger irpt-c449-delete-20261014 closed at 050eca6b81. PRINCIPAL: Andrew_Berman (AdministratorAccess); the Dell identities are denied this act on purpose and are not used. Bounds: no other key, version or bucket, no prefix delete, no lifecycle or policy change.
**Authored by:** 0.7.0_AE_CloudOps~U7
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L | verify | simulator for my principal, open-deploy census, list-object-versions of the prefix read whole; selection must equal exactly 1 key, 1 version, LastModified 2026-10-14T04:23:53Z, 4586 bytes | decision, denominators and the selection printed | Pre-checks 2026-10-14T12:4xZ. Open-deploy census over every live worktree: 2 of 2 read, 32 open entries, 0 naming opal-data-irpt (the dell2 entry irpt-c449-delete-20261014 CLOSED at 050eca6b81, sentinel gone from this tree). SIMULATOR for Andrew_Berman on arn:aws:s3:::opal-data-irpt/irpt/49financial/state/normalized_portfolios/*: s3:DeleteObjectVersion allowed and s3:DeleteObject allowed, matched statement AdministratorAccess. list-object-versions on the prefix read whole: 1 page, last page not truncated, 11 versions, 0 delete markers, 11 distinct keys. Selection by the full 64-hex: exactly 1 key, exactly 1 entry: VersionId sE_H5lz2MhTiv_mZm_EVe7aJTbV5HFzD, LastModified 2026-10-14T04:23:53Z, 4586 bytes, IsLatest, not a delete marker: equals the order. A dry run of the guarded script passed with nothing deleted. | CLOSED 20261014T124247Z |
| D | s3-prefix | delete that one version by its VersionId in ONE call | the call result printed, deleted equals versions before | ONE call: s3 DeleteObject with VersionId sE_H5lz2MhTiv_mZm_EVe7aJTbV5HFzD on the one selected key (bucket opal-data-irpt, prefix irpt/49financial/state/normalized_portfolios/, leaf 38104be4...be29f.json), 2026-10-14T12:4xZ, principal Andrew_Berman: HTTP 204, DeleteMarker not set, version id echoed equal. deleted 1 = versions before 1. No batch, prefix or recursive delete, no lifecycle or policy change; the Dell identities were not used. | CLOSED 20261014T124327Z |
| R | verify | head-object without VersionId answers 404 and list-object-versions for the exact key returns 0 versions and 0 delete markers within a bounded 5 minute window | HEAD NoSuchKey and VERSIONS_AFTER 0 | Read-back (bounded 5 minute window, first read at t=0s sufficed): head-object of the key without a VersionId answered 404/NoSuchKey; list-object-versions with Prefix equal to the full key, exact-match filter, returned 0 versions and 0 delete markers (VERSIONS_AFTER 0). Whole prefix re-read: 10 versions, 0 delete markers, 10 distinct keys (before 11 / 0 / 11), so exactly one entry left and the other 10 keys are untouched. Result file org/tier2_senior/0.7.0_AE_CloudOps~U7/deliverables/irpt_anlreq_c449/C449_DELETE_RESULT.txt carries the five exact lines (grep count 5). No object body, account identifier or name in any file, log or message. | CLOSED 20261014T124327Z |

## Log

- 20261014T124129Z OPENED by 0.7.0_AE_CloudOps~U7 with 3 leg(s)
- 20261014T124247Z LEG L closed: Pre-checks 2026-10-14T12:4xZ. Open-deploy census over every live worktree: 2 of 2 read, 32 open entries, 0 naming opal-d
- 20261014T124327Z LEG D closed: ONE call: s3 DeleteObject with VersionId sE_H5lz2MhTiv_mZm_EVe7aJTbV5HFzD on the one selected key (bucket opal-data-irpt
- 20261014T124327Z LEG R closed: Read-back (bounded 5 minute window, first read at t=0s sufficed): head-object of the key without a VersionId answered 40
- 20261014T124327Z CLOSED -- all 3 legs proven
