# Deploy Completion Record
**Date opened:** 2026-09-11T12:27:12.159012+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260911T124259Z
**Deploy:** IRPT_BCKEND IB-rt-8 -- the export controller, the render command document, the five-contract layer and the three roots re-pointed
**Authored by:** 0.9.0_WK_IRPT_BCKEND~4
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | worktree branch wk-irpt_bckend-2-4 commit of the export controller, identity/package/dispatch/exclusion, the host entry, the export root and the layer source | commit hash | commit 1365a96fad on wk-irpt_bckend-2-4 (LOCAL; a worker never pushes): the export controller (identity/package/dispatch/exclusion, render.py rewritten down, handler.py re-purposed), the host half under infra/aws/ec2/investor-reporting-export/, the export root's ssm.tf and its two scoped grants, the layer source at 5 contracts, and this ledger opened with its sentinel committed immediately (row W3-S4's rule) | CLOSED 20260911T124214Z |
| L2 | s3-prefix | s3://opal-313476888478-lambda-layers/irpt-common.zip (5 of 5 contracts) and s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip | head-object ContentLength + content-sha256 equal to the built zips | TWO artifacts, both write-VERIFIED by head-object. Layer: s3://opal-313476888478-lambda-layers/irpt-common.zip sha256 zZev6jylQVJsizQQKX6UgMa698iTAvA4JI6vzxfXWrQ=, ContentLength 627841, metadata content-sha256 identical, 157 members carrying 5 of 5 IRPT contracts. Controller: s3://opal-313476888478-lambda-artifacts/investor-reporting/irpt-export-render.zip sha256 11ZotLOJLP5xWjGUW+WQD9IKSQnEhoOTuJzR3HEGXww=, 35220 bytes, write VERIFIED by build-and-upload; the ADHC_DRIFTD.002 parity check refused the first build until the four new modules were registered, and the three fixture render_package files were removed from files[] because the fixture package is retired as evidence | CLOSED 20260911T124214Z |
| L3 | activation | terraform apply of the performance, narrative and export roots -- the layer version republished and all three functions re-pointed, plus the irpt-export-render-run SSM document and the controller's scoped grants | safe-apply output | THREE safe-apply runs, one per root. performance: 'Apply complete! Resources: 1 added, 1 changed, 1 destroyed.' publishing irpt-common:3 and re-pointing the adapter (the destroyed resource is layer version 2, replaced in the same apply). narrative: '0 added, 1 changed, 0 destroyed' re-pointing to :3. export: '3 added, 1 changed, 0 destroyed' -- aws_ssm_document.export_render_run, aws_iam_role_policy.export_render_evidence, aws_iam_role_policy.export_render_dispatch and the controller re-pointed. NOTHING ELSE was touched: no existing bucket, table, route, behavior or other Lambda, and the YCharts root was NOT applied and its host was NOT started | CLOSED 20260911T124214Z |
| L4 | verify | a capabilities invoke of irpt-export-render reads 5 of 5 contracts from /opt/python/irpt_contracts; get-layer-version prints the version; 3 of 3 functions reference it; CodeSha256 equals the built zip; all three roots re-plan 0-diff | verbatim CLI output | FIVE OF FIVE IN THE RUNTIME: an aws lambda invoke of irpt-export-render action=capabilities returns contracts_dir=/opt/python/irpt_contracts and contracts_available='5 of 5', each with its schema $id read from the layer -- PerformanceReport, NarrativePacket, RenderPackage, ExportBundle, ExportReceipt. get-layer-version irpt-common:3 prints CodeSha256 zZev6jylQVJsizQQKX6UgMa698iTAvA4JI6vzxfXWrQ= / 627841 bytes / python3.12. THREE OF THREE functions reference arn:...:layer:irpt-common:3 (irpt-performance-adapter, irpt-narrative, irpt-export-render). irpt-export-render CodeSha256 11ZotLOJLP5xWjGUW+WQD9IKSQnEhoOTuJzR3HEGXww= equals the built zip. An invoke of action=render_preflight returns decision=HUMAN_GATED naming the host, its live state (stopped), the declared control holding it there and the three-command operator act -- the served service reads the world and refuses rather than dispatching into a stopped box. Row W4-S10 is closed in the world: the three export contracts that read UNAVAILABLE in round 1 now read available from the layer | CLOSED 20260911T124258Z |

## Log

- 20260911T122712Z OPENED by 0.9.0_WK_IRPT_BCKEND~4 with 4 leg(s)
- 20260911T124214Z LEG L1 closed: commit 1365a96fad on wk-irpt_bckend-2-4 (LOCAL; a worker never pushes): the export controller (identity/package/dispatch
- 20260911T124214Z LEG L2 closed: TWO artifacts, both write-VERIFIED by head-object. Layer: s3://opal-313476888478-lambda-layers/irpt-common.zip sha256 zZ
- 20260911T124214Z LEG L3 closed: THREE safe-apply runs, one per root. performance: 'Apply complete! Resources: 1 added, 1 changed, 1 destroyed.' publishi
- 20260911T124258Z LEG L4 closed: FIVE OF FIVE IN THE RUNTIME: an aws lambda invoke of irpt-export-render action=capabilities returns contracts_dir=/opt/p
- 20260911T124259Z CLOSED -- all 4 legs proven
