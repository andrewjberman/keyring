# Deploy Completion Record
**Date opened:** 2026-10-07T04:31:48.445910+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 77 AMGT-ba-20: the round-77 code redeploy of opal-amgt-scoped-api (build at EXACTLY 14a36147bd, CONTENT-DIFF CHANGED 8 + ADDED 8) plus ONE gateway route swap (POST /api/scoped/amgt/refresh out, GET /api/scoped/amgt/resolve in), then ONE snapshot event. Pair: COO @b0bb011946 / CTO @90de9b291b
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip built in a detached worktree at 14a36147bd | UPLOAD line sha256_b64 + head-object read-back VersionId/content-sha256/ContentLength match; CONTENT-DIFF SUMMARY files 380 IDENTICAL 364 CHANGED 8 ADDED 8 REMOVED 0 against OVpDhfwD | UPLOAD /c/tmp/ba20-r77-14a36147bd.zip (built in detached worktree C:/tmp/ba20-build-14a36147bd at rev-parse 14a36147bdacb15cf40867e5801ec7931a469df1) -> s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip size=41981131 sha256_b64=MkM9Kf37nmI+thEmZR+ij8ybbxGrHxqtsonjyI7N5eg=; read back OK VersionId=VHwcuot4i70V2evVL44EBgQc0BcAtScd content-sha256 and ContentLength match. PRIOR object VersionId=AEDyCJJPpYRRIfJEWYFRaXxP9g5nRYsw content-sha256=OVpDhfwDG3BzKE++wDxMlFA6JrwpTnH3FiHC+NrzsrE= (rollback by copy-object available in addition to apply-at-prior-commit). CONTENT-DIFF SUMMARY: files 380, IDENTICAL 364, CHANGED 8, ADDED 8, REMOVED 0, against OVpDhfwD -- the 16 files are EXACTLY the pair's table, no rider. SIZE: package 133657520 B unzipped over 380 entries + layer opal-amgt-print-deps:1 121743633 B = 255401153 B against 262144000 (97.4%, 6742847 B spare) | CLOSED 20261007T043654Z |
| L2 | activation | ONE safe-apply on infra/aws/terraform/harvest/ -- function code + ONE route swap only, memory_size stays 1769 | UNTARGETED plan read before apply (no other resource); post-apply CodeSha256 differs from OVpDhfwDG3BzKE++wDxMlFA6JrwpTnH3FiHC+NrzsrE= AND equals the built zip sha256_b64; 0-diff re-plan; route list carries GET /resolve and not POST /refresh, 18 non-greedy routes | UNTARGETED plan on infra/aws/terraform/harvest/ read BEFORE the apply: 'Plan: 1 to add, 1 to change, 1 to destroy' and exactly three addresses -- aws_apigatewayv2_route.scoped_amgt_api[GET /api/scoped/amgt/resolve] created, aws_apigatewayv2_route.scoped_amgt_api[POST /api/scoped/amgt/refresh] destroyed, module.scoped_amgt_api.aws_lambda_function.this updated in-place; the lambda's only moved attributes are last_modified, s3_object_version AEDyCJJPpYRRIfJEWYFRaXxP9g5nRYsw -> VHwcuot4i70V2evVL44EBgQc0BcAtScd and source_code_hash OVpDhfwD -> MkM9Kf37 (memory_size NOT in the diff). ONE safe-apply of that saved plan: 'Apply complete! Resources: 1 added, 1 changed, 1 destroyed.' Post-apply get-function-configuration: CodeSha256 MkM9Kf37nmI+thEmZR+ij8ybbxGrHxqtsonjyI7N5eg= (DIFFERS from base OVpDhfwDG3BzKE++wDxMlFA6JrwpTnH3FiHC+NrzsrE= and EQUALS the built zip sha256_b64), MemorySize 1769 unchanged, CodeSize 41981131 = the zip, LastModified 2026-10-07T04:40:17Z. Re-plan: 'No changes. Your infrastructure matches the configuration.' (-detailed-exitcode 0). LIVE gateway 7k3ed8px20 read after the swap: scoped-amgt 19 routes, non-greedy 18 as the pair fixes; POST /api/scoped/amgt/refresh ABSENT, GET /api/scoped/amgt/resolve PRESENT | CLOSED 20261007T044444Z |
| L3 | activation | ONE direct invoke {"amgt_scheduled_action": "refresh_freshness_snapshot"} so the new code writes the /freshness snapshot | the snapshot stamp read back from amgt/harvest/state/freshness_snapshot/current/snapshot.json |  | OPEN |
| V1 | verify | AC1 r77_deployed 3 of 3, AC2 r76 c62/c63 + r75 c59 burst40, AC3 r75 c57/c58/c61 + r74 c53/c55/c56 + r71 c38, all --where deployed | every criterion YES with exit=0; a NO rolls the code and the route list back TOGETHER (prior artifact through the module, one code-only safe-apply); snapshot rollback is copy-object from VersionId JG_6dEHiqJz..PozaZFTXiUFGezcwPky, NEVER a delete |  | OPEN |

## Log

- 20261007T043148Z OPENED by 0.7.0_AE_CloudOps~A with 4 leg(s)
- 20261007T043654Z LEG L1 closed: UPLOAD /c/tmp/ba20-r77-14a36147bd.zip (built in detached worktree C:/tmp/ba20-build-14a36147bd at rev-parse 14a36147bdac
- 20261007T044444Z LEG L2 closed: UNTARGETED plan on infra/aws/terraform/harvest/ read BEFORE the apply: 'Plan: 1 to add, 1 to change, 1 to destroy' and e
