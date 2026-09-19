# Deploy Completion Record
**Date opened:** 2026-09-19T15:55:39.504589+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rtf-12 second pass (msg 98279): ONE build of the 6 serving functions (ycharts deferred, S102) by build-and-upload.sh from HEAD 9fc936185d (manifest @dbf7667178: raw_keys.json x6, firm_registry.json on the S99 four) -- build store only, never a function; each prior build-store version (== live CodeSha256) kept as the rollback source
**Authored by:** 0.7.0_AE_CloudOps~V
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-directory-search.zip | new version latest, metadata == bytes == built sha, delta vs live == the added member(s) + the seam line endings where applicable, every other member byte-identical; prior version hk9OUfwHZxlcwZDqN7cEknbJOXtvB3jd (== live HOpXPDo...) kept as the rollback source; function CodeSha256 unchanged |  | OPEN |
| L2 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-status.zip | new version latest, metadata == bytes == built sha, delta vs live == the added member(s) + the seam line endings where applicable, every other member byte-identical; prior version QNerDSUu9GMYB0bZrjon6n_6VG9q3aR6 (== live LHprxKSP...) kept as the rollback source; function CodeSha256 unchanged |  | OPEN |
| L3 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-holdings.zip | new version latest, metadata == bytes == built sha, delta vs live == the added member(s) + the seam line endings where applicable, every other member byte-identical; prior version XGnVW2ED9FW0zOpRr0V5K12adFHrpeO7 (== live 78XvypHO...) kept as the rollback source; function CodeSha256 unchanged |  | OPEN |
| L4 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-narrative.zip | new version latest, metadata == bytes == built sha, delta vs live == the added member(s) + the seam line endings where applicable, every other member byte-identical; prior version Pu2QRmDx58Qo3hHwVM8L_gyotsmQ8h_6 (== live sgolF/uX...) kept as the rollback source; function CodeSha256 unchanged |  | OPEN |
| L5 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | new version latest, metadata == bytes == built sha, delta vs live == the added member(s) + the seam line endings where applicable, every other member byte-identical; prior version 5tV41pNz.TpJ8O1f6zZCAJ9M6BRqoYlI (== live 4Dp6e0Vy...) kept as the rollback source; function CodeSha256 unchanged |  | OPEN |
| L6 | s3-prefix | opal-313476888478-lambda-artifacts/investor-reporting/irpt-performance-adapter.zip | new version latest, metadata == bytes == built sha, delta vs live == the added member(s) + the seam line endings where applicable, every other member byte-identical; prior version KI0U8m08xPkCgvem5bLmcU2fuWwOCLzs (== live /Cn8XUZo...) kept as the rollback source; function CodeSha256 unchanged |  | OPEN |

## Log

- 20260919T155539Z OPENED by 0.7.0_AE_CloudOps~V with 6 leg(s)
