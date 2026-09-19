# Deploy Completion Record
**Date opened:** 2026-09-19T12:06:24.657825+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtf-10 second pass: the S95 build-store restore -- the LIVE zips of irpt-status/narrative/export-render/performance-adapter (sha256 == live CodeSha256) uploaded to their manifest artifact keys so the re-plan carries no code change (COO ruling on S95, msg 98244); touches the build store only, never a function
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-status.zip | new VersionId + content-sha256 metadata == live CodeSha256 + read-back sha256(b64) == live CodeSha256; displaced version recorded |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-narrative.zip | new VersionId + content-sha256 metadata == live CodeSha256 + read-back sha256(b64) == live CodeSha256; displaced version recorded |  | OPEN |
| L3 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | new VersionId + content-sha256 metadata == live CodeSha256 + read-back sha256(b64) == live CodeSha256; displaced version recorded |  | OPEN |
| L4 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip | new VersionId + content-sha256 metadata == live CodeSha256 + read-back sha256(b64) == live CodeSha256; displaced version recorded |  | OPEN |

## Log

- 20260919T120624Z OPENED by 0.7.0_AE_CloudOps~V with 4 leg(s)
