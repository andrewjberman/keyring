# Deploy Completion Record
**Date opened:** 2026-09-19T13:04:54.730873+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtf-10 third pass (S96 ruled (i), msg 98251): K-CODE build -- irpt-directory-search rebuilt by build-and-upload.sh from HEAD 2b1c672e1f (>= 6e027591fc: the rtf-11 fix + the seam staged_from object) into its manifest artifact key so the re-plan carries K-CODE's one code change; prior live CodeSha256 aQxATFkcdtEBvs+v/zztQBOPcbR9XH9Lzjm9kUOmhmU= at version l4JK6aUnUgtrg.TFrxiKU8.XBM_6APl4 (the rollback source); build store only, never a function
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-search.zip | new VersionId latest + content-sha256 == built sha256 + read-back sha256(b64) == built + zip members == committed blobs; prior version l4JK6aUnUgtrg.TFrxiKU8.XBM_6APl4 kept; function CodeSha256 unchanged |  | OPEN |

## Log

- 20260919T130454Z OPENED by 0.7.0_AE_CloudOps~V with 1 leg(s)
