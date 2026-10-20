# Deploy Completion Record
**Date opened:** 2026-10-20T01:06:44.494127+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261020T011555Z
**Deploy:** IRPT_BCKEND TO-IB-cw-6: Cottonwood retained-key release -- runner bundle (directory_runner.py f2d2329d39a1) FIRST, then irpt-directory-refresh zip (refresh.py 304eb35580ee) and the directory root apply
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | runner bundle s3://opal-data-mdpf/code/scripts/assets_gold/investor_reporting/investor-reporting.tar.gz via safe-deploy (Branch B: VersionId 7ywFHFyMHW5JcS7hjeGIIAWsNyyOOVMB, ETag 643410f6) | version before and after, every member equal to HEAD | bundle minted through safe-deploy at 2026-10-20T01:08Z: VersionId 7ywFHFyM.. -> .E1v3fla68vFitTPx_n3V_jymNoSv7.u (128897 bytes, ETag 1eb61c73); 12 of 12 members equal git show HEAD; Branch B version kept | CLOSED 20261020T010955Z |
| L2 | s3-prefix | irpt-directory-refresh zip built digest 3YK/4/pGsXjLNoYWmG2mqrps8y+t2QUiLiPt6osNT5g= uploaded and head-object verified (Branch B: S3 version zvhYGi4jAIJtLIQOXw4.EYKkuA_pIU8w, CodeSha256 I7T8wRYm) | digest, head-object | BUILD_ONLY and real build digest 3YK/4/pGsXjLNoYWmG2mqrps8y+t2QUiLiPt6osNT5g= equals the pin; uploaded, head-object VersionId nltPOQqQWTbDegOb0Zv3QhUldOLXzO1c size 49173, object sha256 equals the pin; Branch B zip version zvhYGi4jAIJtLIQOXw4.EYKkuA_pIU8w kept | CLOSED 20261020T011204Z |
| L3 | tf-lambda | directory root plan 0/1/0 on module.irpt_directory_refresh.aws_lambda_function.this, ONE safe-apply, clean re-plan | plan counts, replan, CodeSha256, env key names | plan 0 add 1 change 0 destroy at module.irpt_directory_refresh.aws_lambda_function.this (changed attributes last_modified, s3_object_version, source_code_hash only); ONE safe-apply finished 2026-10-20T01:13:37Z; replan No changes; CodeSha256 equals the zip pin; env key names equal the set before (8) | CLOSED 20261020T011500Z |
| L4 | verify | record, criteria output and proof committed with explicit paths | commit ids | record IBcw6_apply_record.json, IBcw6_criteria_output.txt, the proof instance and the function-map artifact_sha256 change committed together on branch wk-ib2-cw6-20261020; IBCW6-AC1, AC2 and AC3 PASS | CLOSED 20261020T011555Z |

## Log

- 20261020T010644Z OPENED by 0.7.0_AE_CloudOps~IB2 with 4 leg(s)
- 20261020T010955Z LEG L1 closed: bundle minted through safe-deploy at 2026-10-20T01:08Z: VersionId 7ywFHFyM.. -> .E1v3fla68vFitTPx_n3V_jymNoSv7.u (128897
- 20261020T011204Z LEG L2 closed: BUILD_ONLY and real build digest 3YK/4/pGsXjLNoYWmG2mqrps8y+t2QUiLiPt6osNT5g= equals the pin; uploaded, head-object Vers
- 20261020T011500Z LEG L3 closed: plan 0 add 1 change 0 destroy at module.irpt_directory_refresh.aws_lambda_function.this (changed attributes last_modifie
- 20261020T011555Z LEG L4 closed: record IBcw6_apply_record.json, IBcw6_criteria_output.txt, the proof instance and the function-map artifact_sha256 chang
- 20261020T011555Z CLOSED -- all 4 legs proven
