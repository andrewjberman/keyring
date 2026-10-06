# Deploy Completion Record
**Date opened:** 2026-10-06T07:14:52.954994+00:00
**Status:** OPEN
**Deploy:** AMGT_RESAPP round 74 AMGT-ax-5: item 0 (the Lato font DATA_MEMBERS patch, committed ALONE as the build commit) then TWO legs -- code carrying ax-1/ax-3/ax-4 (CHANGED 4 + ADDED 3), then ONE greedy security route 'GET /api/scoped/amgt/security/{proxy+}' on gateway 7k3ed8px20 so a key containing '/' reaches the function. CTO conditions 1-5 @1b2be81842, COO half @ef57fb9fdc. The route leg carries a 401 NEGATIVE control (unauthenticated slash-key GET) and a 200 POSITIVE control (BP and NG on Z-S276's 4 routes). c55 becomes a PIN on every later redeploy of this function (CTO ruling 4). Route rollback is the REVERSE PLAN removing the one added key, never a touch to the 10 existing routes.
**Authored by:** 0.7.0_AE_CloudOps~A
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L0 | verify | base re-read live + open_deploys union over every live worktree + the gateway route BASELINE on the applied plane | CodeSha256 satkY3HXAhzfU7zYZ5fk+EmNHaqIRfj7bBtVlG4XfIY= and MemorySize 1769 unchanged; per-tree denominator printed with 0 unresolved; gateway baseline counted CLIENT-SIDE over the auto-paginated whole: 112 rows retrieved, 10 security GET routes, 10 CUSTOM, 0 non-CUSTOM, 0 greedy, one authorizer naqxlm, with a positive control proving the filter discriminates |  | OPEN |
| L1 | git | ITEM 0: git apply round74/ax5_build_fonts.patch to infra/aws/terraform/harvest/build-and-upload-scoped-amgt.sh and commit THAT FILE ALONE -- that commit is the build commit | the commit touches exactly one path; it adds three DATA_MEMBERS rows for lib/research/print/fonts/Lato-Regular.ttf, Lato-Bold.ttf and FONT_LICENSE.txt; its hash is recorded as the build commit and is on CLOUD at or after 0c9b9db840 |  | OPEN |
| L2 | verify | CODE LEG build at item 0's commit from a clean detached checkout, CONTENT-DIFF vs deployed satkY3HX | exactly CHANGED lib/research/api/scoped_amgt.py + lib/research/api/monthly_chatter.py + lib/research/coverage/pool_reader.py + lib/research/print/render_pack.py, ADDED lib/research/print/fonts/Lato-Regular.ttf + Lato-Bold.ttf + FONT_LICENSE.txt, REMOVED none; size 255309631 B under the 262144000 ceiling; ADDED 3 and not 0 is the proof item 0 repaired the packaging defect that VERIFY-SCOPE cannot see |  | OPEN |
| L3 | s3-prefix | opal-313476888478-lambda-artifacts research/opal-amgt-scoped-api.zip | new VersionId + ContentLength + content-sha256, re-read by head-object |  | OPEN |
| L4 | activation | opal-amgt-scoped-api code-only safe-apply, then leadpanel_cold_warm.py --label after and the cold invokes' AMGT_PHASE lines | full-plan show -json: exactly 1 update (the function), 0 destroy/IAM/route/gateway in THIS plan; memory 1769; live CodeSha256 = the new build; leadpanel after output and the phase table captured into deliverables |  | OPEN |
| L5 | activation | ROUTE LEG: one added entry in local.scoped_amgt_routes then ONE safe-apply | plan is exactly 1 to add, 0 to change, 0 to destroy on aws_apigatewayv2_route.scoped_amgt_api, anything else a STOP; after it the applied plane reads 11 security GET routes with 1 greedy and ALL CUSTOM, counted client-side; an UNAUTHENTICATED GET on a slash-key path answers 401 (the negative control proving the authorizer applies); an authenticated GET on BP/_LN_Equity and NG/_LN_Equity answers 200 on all 4 of Z-S276's routes (the positive control) |  | OPEN |
| L6 | verify | AC1 c53/c55/c56 deployed, AC2 the r71-r73 regression set, and the /freshness COLD miss timed 65 s after the warm calls | each criterion SERVED YES with exit=0; c53 warm /freshness under about 2 s with values EQUAL over every row served (302 per the ISSUER GO, not the CTO half's 292); c56 shows Lato in the rendered print; the cold-miss call timed and reported as report-only |  | OPEN |

## Log

- 20261006T071452Z OPENED by 0.7.0_AE_CloudOps~A with 7 leg(s)
