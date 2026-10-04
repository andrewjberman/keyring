# Deploy Completion Record
**Date opened:** 2026-10-04T22:34:33.702311+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261004T231048Z
**Deploy:** AMGT_CORPUS round 36 CRPS-al-5: one code-only redeploy of opal-amgt-scoped-api at 288de3d95d carrying al-1 (model.fiscal_unresolved)
**Authored by:** 2.0.0_SA_COO~X
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | base re-read live + build at 288de3d95d from the clean detached checkout | base aoQ+WrefJ / 1769 / auoGQqF5 unchanged; CONTENT-DIFF exactly CHANGED lib/research/api/scoped_amgt.py (356 files, 0 added, 0 removed); size under ceiling | base re-read live 22:3xZ after RESAPP aq-5 CLOSED 22:27:41Z: CodeSha256 aoQ+WrefJ+JjQcymqyrt2c7MEIlTPmvjJEv8sqZ6M98=, memory 1769, artifact VersionId auoGQqF5cmI7xLgeCy6Z5Qq4w2TQ7icX -- unchanged; real build from the clean detached sparse checkout C:/tmp/crps-al5-build at 288de3d95d: CONTENT-DIFF SUMMARY files 356, IDENTICAL 355, CHANGED 1 (lib/research/api/scoped_amgt.py), ADDED 0, REMOVED 0 against aoQ+WrefJ -- equal to the halves' list; VERIFY-SCOPE FATAL [] break []; ISOLATED OK 3/3; SIZE 253753934 B of 262144000 (96.8%) | CLOSED 20261004T223746Z |
| L1 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + ContentLength + content-sha256, re-read by head-object | UPLOADED s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip VersionId=O1WGPxfTK9vszvvZqzzuOfjQAGMOIZiM ContentLength=41158959 content-sha256=2rFeF57lMh8MkU6WRgZyImZt7RMlW14BdxmUjIBvSSQ= (uploader read-back matches; independently re-read by head-object: same VersionId, ContentLength, content-sha256, LastModified 2026-10-04T22:36:21Z) | CLOSED 20261004T223746Z |
| L2 | activation | opal-amgt-scoped-api code-only safe-apply | full-plan show -json: exactly 1 update (the function), 0 destroy/IAM/route/gateway; memory 1769; live CodeSha256 = the new build | CODE-ONLY safe-apply LANDED rc 0 (HALT_ACK=1 after reading the 28 HALT-GATE items: 0 touch this function or act) on the planfile graded from show -json on a FULL plan: DENOMINATOR 49 resource_changes {no-op 48, update 1}; the one = module.scoped_amgt_api.aws_lambda_function.this, moved exactly last_modified, s3_object_version auoGQqF5cmI7xLgeCy6Z5Qq4w2TQ7icX -> O1WGPxfTK9vszvvZqzzuOfjQAGMOIZiM, source_code_hash aoQ+WrefJ -> 2rFeF57l; memory_size 1769 -> 1769; 0 IAM/route/gateway/destroy/create. 'Modifications complete after 7s', 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed.' Live read after: CodeSha256 2rFeF57lMh8MkU6WRgZyImZt7RMlW14BdxmUjIBvSSQ= (= the upload), MemorySize 1769, LastModified 2026-10-04T22:42:11Z, LastUpdateStatus Successful | CLOSED 20261004T224253Z |
| L3 | verify | al5_served.py --where deployed + aq-5's regression set (r64 c9-c14, r65 c17, r66 c18/c19/c22, r67 c23-c26, c15 cold, RANGE cold) | al5 deployed build 1/1 control 1/1; regressions unchanged vs aq-5's close | Branch A. al5_served.py --where deployed (CodeSha256 2rFeF57l): b1 PASS 1299_HK served 97 = block 97, BA 0 = 0; c1 PASS fiscal_year_figures 543/543, 686/686 -> 'al5 deployed build 1/1 control 1/1' (evidence/r36_al5_leg_v_served.txt). Regression set vs aq-5's close (evidence/r36_al5_leg_v_regressions.txt): r67 c23 YES, c25 YES, c26 YES, c24 NO = aq-5's closing state (mismatches 74 on days 30/90/365, the missing-grant cause aq-5 recorded; unchanged); r66 c18/c19/c22 YES; r65 c17 YES; r64 c9-c14 YES; r64 c15 first read NO on WARM invokes only (3x ~250 ms, 200, 6 headlines -- warm containers from the preceding 14 checks), re-run after 15 min idle 23:09:35Z: YES, 3 of 3 COLD at 1935/2369/2327 ms (init 205/174/169 ms) under 5000 ms, every headline, AMGT_SEGMENT 3/3 -- in aq-5's band (1937-1972 ms). No 502, no rollback. | CLOSED 20261004T231048Z |

## Log

- 20261004T223433Z OPENED by 2.0.0_SA_COO~X with 4 leg(s)
- 20261004T223746Z LEG L0 closed: base re-read live 22:3xZ after RESAPP aq-5 CLOSED 22:27:41Z: CodeSha256 aoQ+WrefJ+JjQcymqyrt2c7MEIlTPmvjJEv8sqZ6M98=, me
- 20261004T223746Z LEG L1 closed: UPLOADED s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip VersionId=O1WGPxfTK9vszvvZqzzuOfjQAGM
- 20261004T224253Z LEG L2 closed: CODE-ONLY safe-apply LANDED rc 0 (HALT_ACK=1 after reading the 28 HALT-GATE items: 0 touch this function or act) on the 
- 20261004T231048Z LEG L3 closed: Branch A. al5_served.py --where deployed (CodeSha256 2rFeF57l): b1 PASS 1299_HK served 97 = block 97, BA 0 = 0; c1 PASS 
- 20261004T231048Z CLOSED -- all 4 legs proven
