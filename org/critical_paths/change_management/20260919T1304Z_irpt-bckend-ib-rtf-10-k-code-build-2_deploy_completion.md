# Deploy Completion Record
**Date opened:** 2026-09-19T13:04:54.730873+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260919T130846Z
**Deploy:** IRPT_BCKEND IB-rtf-10 third pass (S96 ruled (i), msg 98251): K-CODE build -- irpt-directory-search rebuilt by build-and-upload.sh from HEAD 2b1c672e1f (>= 6e027591fc: the rtf-11 fix + the seam staged_from object) into its manifest artifact key so the re-plan carries K-CODE's one code change; prior live CodeSha256 aQxATFkcdtEBvs+v/zztQBOPcbR9XH9Lzjm9kUOmhmU= at version l4JK6aUnUgtrg.TFrxiKU8.XBM_6APl4 (the rollback source); build store only, never a function
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-search.zip | new VersionId latest + content-sha256 == built sha256 + read-back sha256(b64) == built + zip members == committed blobs; prior version l4JK6aUnUgtrg.TFrxiKU8.XBM_6APl4 kept; function CodeSha256 unchanged | BUILT from HEAD 46a106b4d1: irpt-directory-search.zip -> version hk9OUfwHZxlcwZDqN7cEknbJOXtvB3jd (latest, 13:06:35Z, 123282 bytes), content-sha256 == built HOpXPDoHhrVK/ayqsx1uKgzt9mWOjDlK+Ix2CPbCamI=, read-back equal; zip members 10 of 10 == committed blobs (seam = LF blob 191120 bytes, sha256 87f2f92f); prior version l4JK6aUnUgtrg.TFrxiKU8.XBM_6APl4 kept (== prior live aQxATFkc...); function CodeSha256 unchanged aQxATFkc...; builder's artifact_sha256 write reverted (S89 bar, grant = one staged_from object) | CLOSED 20260919T130845Z |

## Log

- 20260919T130454Z OPENED by 0.7.0_AE_CloudOps~V with 1 leg(s)
- 20260919T130845Z LEG L1 closed: BUILT from HEAD 46a106b4d1: irpt-directory-search.zip -> version hk9OUfwHZxlcwZDqN7cEknbJOXtvB3jd (latest, 13:06:35Z, 12
- 20260919T130846Z CLOSED -- all 1 legs proven
