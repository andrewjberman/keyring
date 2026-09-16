# Deploy Completion Record
**Date opened:** 2026-09-16T04:02:58.217369+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260916T042126Z
**Deploy:** D12 WS-3 trusted-device cookie: deploy auth-handler @6328a6fbb2 (Andrew-direct 'deploy it')
**Authored by:** 0.0.0_AB_MSTR
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | source on origin/CLOUD | 6328a6fbb2 on origin (ls-remote read) | 6328a6fbb2522ce95c2b7e09632b4f67b8a565e8 on origin/CLOUD (git ls-remote read ~03:5xZ; local 0 ahead 0 behind); 6 files: deviceTrust.ts NEW, auth.ts, index.ts, mfa.ts, LD-0573, Andrew-direct record | CLOSED 20260916T040354Z |
| L2 | s3-prefix | artefact portal-auth/opalinvest-auth-handler.zip in opal-313476888478-lambda-artifacts | new S3 version-id + content-sha256 from head-object | s3://opal-313476888478-lambda-artifacts/portal-auth/opalinvest-auth-handler.zip VersionId=MgCLUfPi_XmQgPR7tsj7abKXy18sssmd content-sha256=h1tnQVRpRA52eWyfAia6CfBsJmn6xKwHa8IUC0zBSsQ= 41022 bytes LastModified 2026-09-16T04:08:07Z (head-object read); zip SHA256 printed by build-nodejs-lambda.sh == that sha; bundle 92 modules 128K, handler export validated. ROLLBACK PIN: prior VersionId=tDmDpVsQDJ03avoF5u7i6C0PSj3LyNTH sha=sJyR6xk2CIZDJIFQBqVqqfTMOtQ4v1asHfin4/GjXuw= (bucket versioning Enabled) | CLOSED 20260916T040928Z |
| L3 | activation | opalinvest-auth-handler code update via safe-apply -target=aws_lambda_function.auth_handler (WAF drift on this root EXCLUDED by target, not authorized) | Lambda CodeSha256 == artefact sha (get-function-configuration) | safe-apply -target=aws_lambda_function.auth_handler via .tools/terraform.exe v1.9.8: 'Apply complete! Resources: 0 added, 1 changed, 0 destroyed' at ~04:15Z; get-function-configuration AFTER: CodeSha256=h1tnQVRpRA52eWyfAia6CfBsJmn6xKwHa8IUC0zBSsQ= == artefact content-sha256, LastModified=2026-09-16T04:15:05Z, State=Active, LastUpdateStatus=Successful, CodeSize=41022; s3_object_version tDmDpVsQ.. -> MgCLUfPi_XmQgPR7tsj7abKXy18sssmd. WAF drift (aws_wafv2_web_acl.opal_cloudfront_protection) EXCLUDED by target, untouched -- not authorized tonight | CLOSED 20260916T041603Z |
| L4 | verify | 0-diff targeted plan + live API fail-closed probes (bogus device_trust cookie still yields mfaRequired; logout-everywhere unauth -> 401) | probe outputs quoted + plan No changes on target | 0-diff: targeted plan rc=0 'No changes'; untargeted plan back to exactly the pre-existing WAF drift (1 change, aws_wafv2_web_acl only). SMOKE: aws lambda invoke w/o origin secret -> CloudWatch INIT_START (Init 477ms) + 'POST /auth/logout-everywhere' + 'Origin verification FAILED' -> body statusCode 403 (new bundle boots, fails closed). LIVE EDGE via CloudFront https://opalinvest.dev: POST /auth/logout-everywhere unauth -> 401 Unauthorized (NEW route answers); POST /auth/logout with device_trust+refresh_token presented -> 200, set-cookie ONLY refresh_token=...Max-Age=0, NO device_trust set-cookie (POINT 4 PROVEN LIVE); POST /auth/login with bogus 64-hex device_trust + nonsense creds -> 401 'Invalid email or password' (bad cookie falls through). Positive path (MFA -> cookie -> password-only) is Andrew's own account to exercise; CloudWatch device_trust_minted / device_trust_skipped_mfa will confirm. | CLOSED 20260916T042016Z |

## Log

- 20260916T040258Z OPENED by 0.0.0_AB_MSTR with 4 leg(s)
- 20260916T040354Z LEG L1 closed: 6328a6fbb2522ce95c2b7e09632b4f67b8a565e8 on origin/CLOUD (git ls-remote read ~03:5xZ; local 0 ahead 0 behind); 6 files: 
- 20260916T040928Z LEG L2 closed: s3://opal-313476888478-lambda-artifacts/portal-auth/opalinvest-auth-handler.zip VersionId=MgCLUfPi_XmQgPR7tsj7abKXy18sss
- 20260916T041603Z LEG L3 closed: safe-apply -target=aws_lambda_function.auth_handler via .tools/terraform.exe v1.9.8: 'Apply complete! Resources: 0 added
- 20260916T042016Z LEG L4 closed: 0-diff: targeted plan rc=0 'No changes'; untargeted plan back to exactly the pre-existing WAF drift (1 change, aws_wafv2
- 20260916T042126Z CLOSED -- all 4 legs proven
