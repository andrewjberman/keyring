# Deploy Completion Record
**Date opened:** 2026-10-11T16:02:07.573007+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD DB-b-130: overwrite exactly 2 keys so Cottonwood's served method row 3 states the income reason worded for the method, under the signed pair (packet 6fbce1ff...)
**Authored by:** 0.7.0_AE_CloudOps~CB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | the CAPTURE, which IS the rollback: head-object + get-object both keys to a path outside the repo, plus get-bucket-versioning | per key sha256, size, ETag, VersionId, saved_path; ETags must read 9c774f3770e82ed5e7e6b2a4ebe3e7d3 and 6d5aabdd1e0f3cc9ff2a6c544bd327fd, sizes 11641 and 2037; versioning must read Enabled |  | OPEN |
| L2 | activation | the OVERWRITE of exactly 2 keys via emit_method_row(s3, SCOPE, thresholds, upload=True, src=entry) | keys_written, and the pre-write dry-run diff showing income_basis_reason as the ONLY column moved besides measured_at |  | OPEN |
| L3 | verify | the SERVED read-back plus the mint's own method-row verify | head_after per key, served_after row members, the diff, and method_row=match only if that is what was read |  | OPEN |

## Log

- 20261011T160207Z OPENED by 0.7.0_AE_CloudOps~CB2 with 3 leg(s)
