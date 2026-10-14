# Deploy Completion Record
**Date opened:** 2026-10-14T01:45:34.260138+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261014T020412Z
**Deploy:** IRPT_ANLREQ TO-APPLY-R28a unit L2: irpt-status ops/status.py (CORRECTION_WORDS gains TICKER_KEPT_BY_HISTORY, TICKER_CHECK_FAILED, TICKER_NOT_CHECKED; words only) to CodeSha256 MIVrDbv+..; pair COO blob e9bb20d7fe + CTO half @d3adae2fc8
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | COO half hash e9bb20d7fe; census over every live worktree (open entries naming irpt-status or opal-ticket-api); R0b live CodeSha256, key latest version and object hash; R0d fresh turned_back 0; A3 before envelope | reads printed | COO half hash e9bb20d7fe2f6d610c88c4399e6a4387af5e7743 (CTO half @d3adae2fc8 exists); AMENDMENT 1 of the order read. Census: 32 worktrees, 104 entries, 0 errors; 5 name irpt-status or opal-ticket-api, all CLOSED on trunk; the only open entry naming a surface is irpt-ycg-catalogue-ultrashort-20261013 (irpt-ycharts-generate, ~IB2, L6 unproven), printed, does not stop L2/L1 per AMENDMENT 1. R0b: live CodeSha256 vlGh380Q.., key latest 2_5Slkao1.. (64 versions), object hash equal. R0d fresh 2026-10-14T01:42:20Z: 56 template inputs, turned_back 0, reader_version_inputs 0 (R0D_RECOUNT.txt). A3 before: invoke status 200, no FunctionError, body 406 bytes, sha256 588cea1d4612ef48.. (deterministic over two reads). | CLOSED 20261014T014629Z |
| L2 | s3-prefix | detached worktree at a4b7c48fad (core.longpaths), guard printed, repin diff da4e88d212 applied uncommitted, BUILD_ONLY digest equals MIVrDbv+.., then upload, read back equals the staged zip 30856b0dbbfe | digest, VersionId, readback | Build and upload: worktree a4b7c48fad (core.longpaths, guard 8), repin diff da4e88d212 applied uncommitted, BUILD_ONLY digest MIVrDbv+/w8ioVB24xS97gnETVbNRCroDiY+Ne5osbA= equals EXPECTED and the kept build bytes equal the staged zip (sha256 30856b0dbbfe..); real run (script verify: write VERIFIED size=363730) landed new VersionId V_g2PtX08Ktkbo5XYohrB5pHDFctjzZE; read back by VersionId: 363730 bytes, sha256 equals the staged zip 30856b0dbbfe.. | CLOSED 20261014T014840Z |
| L3 | verify | scoped plan -target=module.irpt_status.aws_lambda_function.this: 0 add 1 change 0 destroy, last_modified s3_object_version source_code_hash only | plan summary and attributes | scoped plan from infra/aws/terraform/investor-reporting/ops -target=module.irpt_status.aws_lambda_function.this saved outside the repo: Plan: 0 to add, 1 to change, 0 to destroy; attributes last_modified, s3_object_version (2_5Slkao1.. -> V_g2PtX08Ktkbo5XYohrB5pHDFctjzZE), source_code_hash (vlGh380Q.. -> MIVrDbv+..) only; environment, role, tags not in the diff. | CLOSED 20261014T015216Z |
| L4 | activation | safe-apply on the saved plan | Apply complete 0/1/0 | pre-apply mail check by get_delivery_state: 0 non-READ; .tools/safe-apply.sh on the saved plan 01:49:40Z-01:51:21Z: Apply complete! 0 added, 1 changed, 0 destroyed (seat-gates APPLY-WHO ADMITTED; crossbox-deploy-check in WARN mode printed 'would stop under ENFORCE': open call dell2-20261013T214715Z-f61b of IRPT_BCKEND, a pending question to Andrew whose scope lists the investor-reporting roots, token match only; comp-tagauthz PASSED). No aws lambda update-function-code used. | CLOSED 20261014T015216Z |
| L5 | verify | S1 CodeSha256 MIVrDbv+..; S2 49 members, only status.py differs from 2_5Slkao1..; S3 credential-less refusal envelope equals A3 before | S1-S3 | S1 live CodeSha256 MIVrDbv+/w8ioVB24xS97gnETVbNRCroDiY+Ne5osbA= (LastModified 2026-10-14T01:51:15Z, Successful) TRUE; S2 live zip 363730 bytes, 49 members, only status.py differs from 2_5Slkao1.. TRUE; S3 credential-less refusal envelope after: invoke 200, no FunctionError, body sha256 588cea1d4612ef48.. equals A3 before TRUE. | CLOSED 20261014T015216Z |
| L6 | git | status.py row of the repin diff plus artifact_* and last_deployed_* applied to the trunk map in own worktree; commit | commit hash | Map record commit 8fdee64bb2 on scratch branch aq2-r28-map (own full worktree, core.longpaths), merged to box/dell2 as bbbbf7521f via safe-merge. Net diff lambda-source-map.json only: 2 of 235 entries (irpt-status: the status.py row of the repin diff, applied cleanly, plus the record; opal-ticket-api: the record); verified by a parsed old-vs-new comparison. last_deployed_commit is the last commit touching source_dir (irpt-status 9441d74dbb, opal-ticket-api cbdfe204a0); the build bases were a4b7c48fad and 4279513f95 and source_dir is unchanged between them and the map head. | CLOSED 20261014T020412Z |

## Log

- 20261014T014534Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 6 leg(s)
- 20261014T014629Z LEG L1 closed: COO half hash e9bb20d7fe2f6d610c88c4399e6a4387af5e7743 (CTO half @d3adae2fc8 exists); AMENDMENT 1 of the order read. Cen
- 20261014T014727Z LEG L2 closed: PARTIAL (build half): worktree a4b7c48fad0559ff06155e505b51e97b3c5f6437 detached with core.longpaths, guard 8 mentions a
- 20261014T014840Z LEG L2 closed: Build and upload: worktree a4b7c48fad (core.longpaths, guard 8), repin diff da4e88d212 applied uncommitted, BUILD_ONLY d
- 20261014T015216Z LEG L3 closed: scoped plan from infra/aws/terraform/investor-reporting/ops -target=module.irpt_status.aws_lambda_function.this saved ou
- 20261014T015216Z LEG L4 closed: pre-apply mail check by get_delivery_state: 0 non-READ; .tools/safe-apply.sh on the saved plan 01:49:40Z-01:51:21Z: Appl
- 20261014T015216Z LEG L5 closed: S1 live CodeSha256 MIVrDbv+/w8ioVB24xS97gnETVbNRCroDiY+Ne5osbA= (LastModified 2026-10-14T01:51:15Z, Successful) TRUE; S2
- 20261014T020412Z LEG L6 closed: Map record commit 8fdee64bb2 on scratch branch aq2-r28-map (own full worktree, core.longpaths), merged to box/dell2 as b
- 20261014T020412Z CLOSED -- all 6 legs proven
