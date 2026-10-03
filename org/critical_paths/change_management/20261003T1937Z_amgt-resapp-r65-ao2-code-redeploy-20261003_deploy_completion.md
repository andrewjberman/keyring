# Deploy Completion Record
**Date opened:** 2026-10-03T19:37:34.462915+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261003T195356Z
**Deploy:** AMGT_RESAPP round 65 AMGT-ao-2: one code-only redeploy of opal-amgt-scoped-api at pin 19cb3df089 (carries ao-1 title case + the ft quarantine-mechanism deletion); memory stays 1769
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + byte count + content-sha256 metadata of the uploaded object | UPLOADED s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip VersionId=5xO0vR9UWlx.XI59G0KNLJyAsjMKOes4 ContentLength=41150318 content-sha256=lPTMo20TWOn9GxEyMPa4EausVvWKpvyGQTeZcVFZlW0= (read back by the script, matches). Real build from detached worktree at pin 19cb3df089 reproduced the build-only figure EXACTLY: CONTENT-DIFF 355/352/3/0/0 vs KQSA62c3, SIZE 253725663 B of 262144000 (96.8%), cold-start FATAL [], request-time break [], ISOLATED 3 of 3. Prior VersionId .xFOZLD1X0znp_5COtZvp3UgWTBrw19p retained as rollback. | CLOSED 20261003T194059Z |
| L2 | activation | opal-amgt-scoped-api code-only safe-apply at pin 19cb3df089 | new CodeSha256 off KQSA62c3 + MemorySize still 1769 + 0-diff replan | CODE-ONLY safe-apply landed (Rule 18 wrapper, SAFE_APPLY_TERRAFORM resolved on PATH; .tools/terraform.exe absent on site Z). PLAN from show -json: 49 resource_changes, 1 non-no-op (module.scoped_amgt_api.aws_lambda_function.this, update), exactly 3 changed attributes (last_modified, s3_object_version .xFOZLD1X->5xO0vR9U, source_code_hash KQSA62c3->lPTMo20T); memory_size 1769->1769 UNCHANGED; action shapes only no-op/update; any delete or replace FALSE. DEPLOYED read live after apply: CodeSha256 lPTMo20TWOn9GxEyMPa4EausVvWKpvyGQTeZcVFZlW0= (equals the uploaded artifact), MemorySize 1769, CodeSize 41150318, LastModified 2026-10-03T19:47:12Z, State Active, LastUpdateStatus Successful. RE-PLAN: 'No changes. Your infrastructure matches the configuration', detailed-exitcode=0. | CLOSED 20261003T195021Z |
| L3 | verify | AC1 c17 deployed and AC2 c12 deployed plus regressions c9 c10 c11 c13 c14 | each check verdict line with exit=0; rollback VersionId .xFOZLD1X0znp_5COtZvp3UgWTBrw19p if any fails | ALL CRITERIA PASS on the DEPLOYED function, graded from the 19cb3df089 checkout per row Z-S342. AC1 r65 c17: 'R65 C17 SERVED: YES', exit=0 -- breakout/price names 94 all-caps 0, collected/chatter names 95 all-caps 0, both routes serve 'Mitsubishi UFJ Financial Group' whole (base was all-caps 55 of 94 and 56 of 95 with 'MITSUBISHI UFJ FINANCIAL GRO' on both). Denominators 94 and 95 UNCHANGED base-to-after, so no row moved. AC2 r64 c12: 'R64 C12 SERVED: YES', exit=0 -- one display name per security (The Boeing Co, Advanced Micro Devices Inc, Valero Energy Corp) across overlay/ranking/chatter/peers. REGRESSIONS all YES exit=0: c9 (4 window variants, 95 rows, bad 0), c10 (8 of 8 both movements), c11 (3 names), c13 (94 of 94 labeled), c14 (sector + encoded-key routes 200). ZERO FAIL lines in the whole run, and every after-line is identical to the base capture taken pre-apply. ROLLBACK NOT TAKEN. | CLOSED 20261003T195327Z |

## Log

- 20261003T193734Z OPENED by 0.7.0_AE_CloudOps~A with 3 leg(s)
- 20261003T194059Z LEG L1 closed: UPLOADED s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip VersionId=5xO0vR9UWlx.XI59G0KNLJyAsjM
- 20261003T195021Z LEG L2 closed: CODE-ONLY safe-apply landed (Rule 18 wrapper, SAFE_APPLY_TERRAFORM resolved on PATH; .tools/terraform.exe absent on site
- 20261003T195327Z LEG L3 closed: ALL CRITERIA PASS on the DEPLOYED function, graded from the 19cb3df089 checkout per row Z-S342. AC1 r65 c17: 'R65 C17 SE
- 20261003T195356Z CLOSED -- all 3 legs proven
