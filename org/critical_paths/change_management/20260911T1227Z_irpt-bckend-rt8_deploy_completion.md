# Deploy Completion Record
**Date opened:** 2026-09-11T12:27:12.159012+00:00
**Status:** OPEN
**Deploy:** IRPT_BCKEND IB-rt-8 -- the export controller, the render command document, the five-contract layer and the three roots re-pointed
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | worktree branch wk-irpt_bckend-2-4 commit of the export controller, identity/package/dispatch/exclusion, the host entry, the export root and the layer source | commit hash |  | OPEN |
| L2 | s3-prefix | s3://opal-313476888478-lambda-layers/irpt-common.zip (5 of 5 contracts) and s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | head-object ContentLength + content-sha256 equal to the built zips |  | OPEN |
| L3 | activation | terraform apply of the performance, narrative and export roots -- the layer version republished and all three functions re-pointed, plus the irpt-export-render-run SSM document and the controller's scoped grants | safe-apply output |  | OPEN |
| L4 | verify | a capabilities invoke of irpt-export-render reads 5 of 5 contracts from /opt/python/irpt_contracts; get-layer-version prints the version; 3 of 3 functions reference it; CodeSha256 equals the built zip; all three roots re-plan 0-diff | verbatim CLI output |  | OPEN |

## Log

- 20260911T122712Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 4 leg(s)
