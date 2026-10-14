# Deploy Completion Record
**Date opened:** 2026-10-14T12:41:29.650192+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-DELETE-C449-U7: delete the ONE version of the ONE synthetic stored input (full 64-hex 38104be4dc81abe6a67dcb837add8576df86a7cdecc21b08e5de6e33c58be29f) under irpt/49financial/state/normalized_portfolios/ in opal-data-irpt, by VersionId, ONE call, and nothing else. NOT RECOVERABLE (a deleted S3 version cannot be restored; the object is synthetic). AUTHORITY: Andrew verbatim '8.) Yes delete of synthetic leftover is approved.' (ANDREW_DIRECT_20261014_114xZ line 10; the act, not a seat, CTO msg 109130); issuer GO XB-20261014T123613Z-be5e after the dell2 ledger irpt-c449-delete-20261014 closed at 050eca6b81. PRINCIPAL: Andrew_Berman (AdministratorAccess); the Dell identities are denied this act on purpose and are not used. Bounds: no other key, version or bucket, no prefix delete, no lifecycle or policy change.
**Authored by:** 0.7.0_AE_CloudOps~U7
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L | verify | simulator for my principal, open-deploy census, list-object-versions of the prefix read whole; selection must equal exactly 1 key, 1 version, LastModified 2026-10-14T04:23:53Z, 4586 bytes | decision, denominators and the selection printed |  | OPEN |
| D | s3-prefix | delete that one version by its VersionId in ONE call | the call result printed, deleted equals versions before |  | OPEN |
| R | verify | head-object without VersionId answers 404 and list-object-versions for the exact key returns 0 versions and 0 delete markers within a bounded 5 minute window | HEAD NoSuchKey and VERSIONS_AFTER 0 |  | OPEN |

## Log

- 20261014T124129Z OPENED by 0.7.0_AE_CloudOps~U7 with 3 leg(s)
