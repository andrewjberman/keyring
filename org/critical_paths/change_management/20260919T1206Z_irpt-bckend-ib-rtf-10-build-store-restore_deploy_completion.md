# Deploy Completion Record
**Date opened:** 2026-09-19T12:06:24.657825+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260919T120932Z
**Deploy:** IRPT_BCKEND IB-rtf-10 second pass: the S95 build-store restore -- the LIVE zips of irpt-status/narrative/export-render/performance-adapter (sha256 == live CodeSha256) uploaded to their manifest artifact keys so the re-plan carries no code change (COO ruling on S95, msg 98244); touches the build store only, never a function
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-status.zip | new VersionId + content-sha256 metadata == live CodeSha256 + read-back sha256(b64) == live CodeSha256; displaced version recorded | irpt-status.zip -> version QNerDSUu9GMYB0bZrjon6n_6VG9q3aR6 (latest), content-sha256 == live CodeSha256 LHprxKSP1lM3VhoP2ijEcUVCtI+yeZt8tPRkZwpRBdY=, read-back equal, 137832 bytes; displaced Fp_QWlcKDid_IrVgxtdbSHZoTcu5iHLx; function CodeSha256 unchanged | CLOSED 20260919T120931Z |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-narrative.zip | new VersionId + content-sha256 metadata == live CodeSha256 + read-back sha256(b64) == live CodeSha256; displaced version recorded | irpt-narrative.zip -> version Pu2QRmDx58Qo3hHwVM8L_gyotsmQ8h_6 (latest), content-sha256 == live sgolF/uXedgXpePoBoi5y1dIgOybQkgcokihEJFM+0I=, read-back equal, 157846 bytes; displaced xJmLYKYZ6Ad5W6NMIusKtOh3QbY_IIvM; function unchanged | CLOSED 20260919T120931Z |
| L3 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | new VersionId + content-sha256 metadata == live CodeSha256 + read-back sha256(b64) == live CodeSha256; displaced version recorded | irpt-export-render.zip -> version 5tV41pNz.TpJ8O1f6zZCAJ9M6BRqoYlI (latest), content-sha256 == live 4Dp6e0Vy+SfziPY+9wUSWSBS4JzS9diUtduOTxIqclQ=, read-back equal, 143467 bytes; displaced 4SHjHG9.poTQt9USOtnNtLqg393Ww1b_; function unchanged | CLOSED 20260919T120931Z |
| L4 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip | new VersionId + content-sha256 metadata == live CodeSha256 + read-back sha256(b64) == live CodeSha256; displaced version recorded | irpt-performance-adapter.zip -> version KI0U8m08xPkCgvem5bLmcU2fuWwOCLzs (latest), content-sha256 == live /Cn8XUZoSn1EGBax3+/UaVjJSAQiybZQ84vRVwiRcWs=, read-back equal, 166002 bytes; displaced b_FS5lpcphi04WwjjlTTXT_NxIkCFomi; function unchanged | CLOSED 20260919T120931Z |

## Log

- 20260919T120624Z OPENED by 0.7.0_AE_CloudOps~V with 4 leg(s)
- 20260919T120931Z LEG L1 closed: irpt-status.zip -> version QNerDSUu9GMYB0bZrjon6n_6VG9q3aR6 (latest), content-sha256 == live CodeSha256 LHprxKSP1lM3VhoP
- 20260919T120931Z LEG L2 closed: irpt-narrative.zip -> version Pu2QRmDx58Qo3hHwVM8L_gyotsmQ8h_6 (latest), content-sha256 == live sgolF/uXedgXpePoBoi5y1dI
- 20260919T120931Z LEG L3 closed: irpt-export-render.zip -> version 5tV41pNz.TpJ8O1f6zZCAJ9M6BRqoYlI (latest), content-sha256 == live 4Dp6e0Vy+SfziPY+9wUS
- 20260919T120931Z LEG L4 closed: irpt-performance-adapter.zip -> version KI0U8m08xPkCgvem5bLmcU2fuWwOCLzs (latest), content-sha256 == live /Cn8XUZoSn1EGB
- 20260919T120932Z CLOSED -- all 4 legs proven
