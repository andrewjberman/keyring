# Deploy Completion Record
**Date opened:** 2026-10-03T19:46:49.560403+00:00
**Status:** OPEN
**Deploy:** opal-portal-authorizer: the render-token branch admits the 49F reporting SERIES route (row S307, IB-pr-307 @79db37c149; packet blob 89ac848918 @5c92c0a; CTO half batch 227 @ca49283ff1)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| N1 | verify | negative arm before and after | no-token + bogus-bearer GETs on two scoped routes 401 (4 of 4) both times | no-token and bogus-bearer GETs on /api/general/trades/x and /api/scoped/advisor-intelligence/clients/growth at opalinvest.dev: 401 x4 before (19:4xZ) and 401 x4 after (19:52:3xZ); authorizer log since 19:52:32Z: 0 runtime errors | CLOSED 20261003T195352Z |
| D1 | activation | build + upload opal-portal-authorizer from CLOUD @79db37c149 | artifact content-sha256 = S3 bytes; bundle carries the series route + which guard | 19:5xZ build-nodejs-lambda.sh portal-auth opal-portal-authorizer from CLOUD @ca49283ff1 (contains the IB-pr-307 merge 79db37c149): bundled 78 modules, @aws-sdk external; S3 portal-auth/opal-portal-authorizer.zip version Ofvov7aT, content-sha256 gQp2IooAM3EgebVQeII27xcE+KuEDhyYfrlwr6Jqcsc= = the bytes; the bundle carries 'GET .../reporting/{account_id}/{which}': {param account_id, claim accountSetId, require {which: series}}, the three existing routes, and the route-parameter guard loop | CLOSED 20261003T194845Z |
| D2 | tf-lambda | targeted safe-apply aws_lambda_function.portal_authorizer (code only) | live CodeSha256 = artifact; re-plan 0 | 19:52:32Z targeted safe-apply 0/1/0 (s3_object_version QLGNN9 -> Ofvov7aT, source_code_hash sgQWoygZ -> gQp2IooA; env unchanged): live opal-portal-authorizer CodeSha256 gQp2IooAM3EgebVQeII27xcE+KuEDhyYfrlwr6Jqcsc= = artifact, Active/Successful, env keys [IRPT_RENDER_JWT_PUBLIC_KEY_PEM]; targeted re-plan No changes | CLOSED 20261003T195352Z |
| S | verify | CTO stop: right after D2, a signed-in human request to a scoped route answers 200 and N1's 401s hold | human 200 + 401s; else roll D2 back to sgQWoygZ at once | CTO batch 227 stop, after D2 (19:52:32Z) and before P1/P2: 2.0.0_SA_COO~D's signed-in load (msg 104716) -- GET /api/scoped/investor-reporting/reporting/acc_.../manifest HTTP 200 at 19:55:57.885Z and .../series HTTP 200 at 19:55:58.431Z, the tab drew the account; corroborated by the authorizer log (the walker principal verified x19 from 19:55:43Z) and the read Lambda serving 2 invocations with 0 errors; N1's 401s held after D2 (4 of 4). No rollback owed | CLOSED 20261003T195812Z |
| P2 | verify | a render token for account X asking the series route for account Y refuses | V2 refuses (path id does not match its claim); jti + sha256 recorded, no token | 19:58:18Z auth_p2_foreign_token_probe.py: a render token minted for 49F account X (accountSetId ...24d5; render key read by name, never printed; jti render-85027e4cc0b74436b4f21f2ec8a2ea17, token sha256 62aa058bef0a8e2e, exp-iat 300 s) asked GET .../reporting/acc_...21be/series (account Y) through opalinvest.dev -> HTTP 403 Forbidden; the edge (V3) logged render_accepted for that jti (shape), and the authorizer (V2) refused it on the NEW route entry: 'Render token path id does not match its claim' route GET .../reporting/{account_id}/{which}, claimName accountSetId -- the route is live in V2 and its account pin holds | CLOSED 20261003T195900Z |
| P1 | verify | ~D re-walks a 49F export outside the six | the export issues a receipt naming the frozen as_of |  | OPEN |

## Log

- 20261003T194649Z OPENED by 2.0.0_SA_COO~P with 6 leg(s)
- 20261003T194845Z LEG D1 closed: 19:5xZ build-nodejs-lambda.sh portal-auth opal-portal-authorizer from CLOUD @ca49283ff1 (contains the IB-pr-307 merge 79
- 20261003T195352Z LEG D2 closed: 19:52:32Z targeted safe-apply 0/1/0 (s3_object_version QLGNN9 -> Ofvov7aT, source_code_hash sgQWoygZ -> gQp2IooA; env un
- 20261003T195352Z LEG N1 closed: no-token and bogus-bearer GETs on /api/general/trades/x and /api/scoped/advisor-intelligence/clients/growth at opalinves
- 20261003T195812Z LEG S closed: CTO batch 227 stop, after D2 (19:52:32Z) and before P1/P2: 2.0.0_SA_COO~D's signed-in load (msg 104716) -- GET /api/scop
- 20261003T195900Z LEG P2 closed: 19:58:18Z auth_p2_foreign_token_probe.py: a render token minted for 49F account X (accountSetId ...24d5; render key read
