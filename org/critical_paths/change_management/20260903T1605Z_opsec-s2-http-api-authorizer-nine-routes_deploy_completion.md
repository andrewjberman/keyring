# Deploy Completion Record
**Date opened:** 2026-09-03T16:05:01.493570+00:00
**Status:** OPEN
**Deploy:** NFRA_OPSEC202609.TO-OP-S-2 deliverable 1: portal-jwt-authorizer (REQUEST authorizer naqxlm) onto the 9 data routes of HTTP API 7k3ed8px20 that read NONE -- nine IN-PLACE attribute edits in shared-infra/apigateway-portal/routes.tf, applied SCOPED (-target) because the module's state lives in the shared-infra ROOT whose baseline carries a foreign global_graph lifecycle-expiry change (row Z-S17) that must NOT ride
**Authored by:** 0.7.0_AE_CloudOps~Z
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | routes.tf nine in-place edits (authorization_type NONE->CUSTOM + authorizer_id portal_jwt) committed under 0.7.0_AE_CloudOps~Z; UNSCOPED baseline quoted BEFORE the first edit | commit hash + the quoted baseline |  | OPEN |
| L2 | activation | ROLLBACK EXERCISED FIRST on ONE route (r_as2dsme, GET /v1/health/data-availability): attach, read CUSTOM/naqxlm, DETACH, read back to NONE -- proves the reverse works before the nine rely on it | both live reads, before and after the detach |  | OPEN |
| L3 | activation | safe-apply SCOPED to exactly the nine route resources: module.apigateway_portal.aws_apigatewayv2_route.{r_as2dsme,r_c0k8rl0,r_gwygx58,r_m8wdq80,r_mxus2bs,r_o2xr1ct,r_ruzaqhq,r_sogv7z9,r_t81twif} -- ROLLBACK: revert the nine attributes and re-apply the same targets, an in-place UpdateRoute back to NONE | apply output reading 9 changed, 0 added, 0 destroyed |  | OPEN |
| L4 | verify | S2-AC1: live get-routes reads AuthorizationType CUSTOM + AuthorizerId naqxlm on 9 of 9 (denominator 9); the 3 by-design NONE (OPTIONS /{proxy+} 3stqzjk, OPTIONS /auth/{proxy+} tqkdv6s, ANY /auth/{proxy+} vuudpyq) UNCHANGED; 60+9=69 authorized of 72 | before/after pairs pasted |  | OPEN |
| L5 | verify | S2-AC5 TWO-SIDED unscoped re-plan on the shared-infra ROOT: the nine routes 0-diff AND the foreign aws_s3_bucket_lifecycle_configuration.global_graph change STILL PRESENT -- a clean unscoped plan here is a FAILURE, not a pass (laptop CTO ruling relayed 19665) | the re-plan output showing both sides |  | OPEN |
| L6 | verify | S2-AC2 + S2-AC3 probes under the OP-x-1 verdict against the NAMED demo-firm fixture: valid fixture login REFUSED at the direct HTTP-API address and ADMITTED through CloudFront; anonymous novel-keyword POST refused with the vendor-call count reading 0 by a named instrument whose positive control is an EXISTING record | exact invocations + captured responses |  | OPEN |
| L7 | verify | push state MEASURED by ls-remote + is-ancestor, stated as a measured value never a default | ls-remote read |  | OPEN |

## Log

- 20260903T160501Z OPENED by 0.7.0_AE_CloudOps~Z with 7 leg(s)
