# Deploy Completion Record
**Date opened:** 2026-09-12T08:44:00.248094+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260912T085304Z
**Deploy:** IRPT_BCKEND IB-rt-6: the absence oracle -- redeploy irpt-directory-refresh with list-established absence and the conditioned ListBucket grant, then re-drive the production fire
**Authored by:** 0.9.0_WK_IRPT_BCKEND~2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | s3-prefix | opal-313476888478-lambda-artifacts investor-reporting/irpt-directory-refresh.zip | VersionId + content-sha256 equal to the rebuilt zip | investor-reporting/irpt-directory-refresh.zip VersionId vnb2ZAHYnMSuCS4jEr88jtFkhHh9x0WD, metadata content-sha256=/qyUho5JNtliMMu79XjnVVsvl6Y2CAlfxEgPANXouJE= equal to the rebuilt zip; git status --porcelain over the five packaged members read 0 lines | CLOSED 20260912T085302Z |
| L2 | activation | terraform apply: the conditioned ListBucket statement + the new function code | safe-apply rc=0, no destroy line | safe-apply rc=0: 'Apply complete! Resources: 0 added, 2 changed, 0 destroyed.'; saved plan carried no destroy line; tombstone-gate CLEAN (0 creates against 7 tombstones) | CLOSED 20260912T085303Z |
| L3 | verify | served CodeSha256 == built, post-apply plan No changes, and simulate-principal-policy shows ListBucket allowed under the prefix condition | three-way hash + plan + simulation | served CodeSha256 /qyUho5JNtliMMu79XjnVVsvl6Y2CAlfxEgPANXouJE= == built, LastUpdateStatus Successful. THE SAME INSTRUMENT THAT SAID implicitDeny NOW SAYS allowed, WITH A NEGATIVE CONTROL: simulate-principal-policy s3:ListBucket on arn:aws:s3:::opal-data-bd with context s3:prefix=investor-reporting/directory/_refresh/ -> allowed; the identical call with s3:prefix=gold/ -> implicitDeny, so the condition genuinely scopes the grant and did not simply open the bucket | CLOSED 20260912T085303Z |
| L4 | activation | re-drive the production fire for 2026-09-11 across three firms | the three manifests present with build_dispatch SSM and a real command id each | 3 of 3 firms: aws lambda invoke StatusCode 200, every envelope REFRESH_DISPATCHED/RUNNING/WAIT with manifest_read_error None and manifest_written True. The three manifests read back from S3 carry build_dispatch SSM with real command ids -- 49financial 940c828f-c176-4a2d-afcc-1693d3d97fe6, inflection afcc6558-a624-4107-8507-10c96cc99727, cottonwood 777591bb-2ccb-4ad1-ba6d-29d3c5150f14 -- each of which resolves through ssm get-command-invocation (all three Failed rc=1 on the host, ModuleNotFoundError trading_calendar; the BUILD is blocked, the DISPATCH is not) | CLOSED 20260912T085303Z |

## Log

- 20260912T084400Z OPENED by 0.9.0_WK_IRPT_BCKEND~2 with 4 leg(s)
- 20260912T085302Z LEG L1 closed: investor-reporting/irpt-directory-refresh.zip VersionId vnb2ZAHYnMSuCS4jEr88jtFkhHh9x0WD, metadata content-sha256=/qyUho
- 20260912T085303Z LEG L2 closed: safe-apply rc=0: 'Apply complete! Resources: 0 added, 2 changed, 0 destroyed.'; saved plan carried no destroy line; tomb
- 20260912T085303Z LEG L3 closed: served CodeSha256 /qyUho5JNtliMMu79XjnVVsvl6Y2CAlfxEgPANXouJE= == built, LastUpdateStatus Successful. THE SAME INSTRUMEN
- 20260912T085303Z LEG L4 closed: 3 of 3 firms: aws lambda invoke StatusCode 200, every envelope REFRESH_DISPATCHED/RUNNING/WAIT with manifest_read_error 
- 20260912T085304Z CLOSED -- all 4 legs proven
