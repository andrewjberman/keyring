# Deploy Completion Record
**Date opened:** 2026-09-25T16:00:05.310356+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260925T162649Z
**Deploy:** Export section A3: V3 auth-validator-edge with the render branch + exp fix (new Lambda@Edge version, distribution repointed)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | aws_lambda_function.auth_validator_edge[0] + aws_cloudfront_distribution.portal association | new version published from artifact Mfo4c4PG..; LIVE distribution EVTSA9VEHNZVH associates that version on all 26 behaviors (was 20) | 16:2xZ safe-apply of targeted plan (edge Lambda + distribution; ACL pulled in as dependency, CTO msg 100972): 0 added / 3 changed / 0 destroyed. auth-validator-edge:21 CodeSha256 Mfo4c4PGLRiZ3SocqpYPpi00XPl25T0yq11ruTpxlgc= (== built artifact), State Active/Successful; LIVE get-distribution EVTSA9VEHNZVH Status Deployed, 26 of 26 auth-validator-edge associations on :21 (was :20); other edge fns unchanged (router:26, router-response:5, public-data-router:7, cache-control-injector:2). WAF rollback record: change_management/20260925T1600Z_irpt-render-v3-a3-20260925_waf_acl_before.json; after: ..._waf_acl_after.json; rule-by-rule diff excluding Version = 0 of 6, LockToken unchanged 848a6d0b (WAF recorded no write). | CLOSED 20260925T162648Z |
| N1 | verify | negative arm before and after | unauthenticated scoped API request refused before and after; human Auth OK continues in the edge log with no runtime errors | Before (16:15Z, v20) and after (16:23Z, v21): no-token and bogus-bearer GETs to /api/general/trades/x and /api/scoped/advisor-intelligence/clients/growth at opalinvest.dev -> 401 x4 each time, identical bodies; the v21 log shows exactly those 2 'Auth FAILED invalid token' lines. Human traffic on v21 16:23-16:3xZ: Auth OK 8, runtime errors 0 (Task timed out/Runtime./Uncaught/TypeError). | CLOSED 20260925T162648Z |
| V1 | verify | targeted re-plan | No changes | Targeted re-plan after apply: edge Lambda + distribution No changes; plan 0/1/0 is ONLY aws_wafv2_web_acl.opal_cloudfront_protection rule attr = the recurring benign managed_rule_group_statement.version "" vs unset diff (row IRPT_BCKEND-S133; provider refuses version=""; CTO msg 100972 accepts it). | CLOSED 20260925T162649Z |

## Log

- 20260925T160005Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260925T162648Z LEG A1 closed: 16:2xZ safe-apply of targeted plan (edge Lambda + distribution; ACL pulled in as dependency, CTO msg 100972): 0 added / 
- 20260925T162648Z LEG N1 closed: Before (16:15Z, v20) and after (16:23Z, v21): no-token and bogus-bearer GETs to /api/general/trades/x and /api/scoped/ad
- 20260925T162649Z LEG V1 closed: Targeted re-plan after apply: edge Lambda + distribution No changes; plan 0/1/0 is ONLY aws_wafv2_web_acl.opal_cloudfron
- 20260925T162649Z CLOSED -- all 3 legs proven
