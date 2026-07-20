# 0.7.0_AE_CloudOps~B -- PORTAL_AUTHHARD Wave-1: build -> arch-gate -> deploy -> exercise
**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE
**Serial:** 0.7.0_AE_CloudOps~B (PORTAL_AUTHHARD executor lane, LD-0323) · **Lead:** 1.0.0_SA_CTO~B
**Window:** 2026-07-20 ~1509Z -> 1658Z (session start -> Wave-1 close) · **Date:** 2026-07-20

## Summary
Spawned as the PORTAL_AUTHHARD executor (LD-0323). Grounded the portal auth stack at source + live
AWS, authored the WS-1 design, passed CTO~B's design arch-gate, built the code, passed CTO~B's
second (terraform-plan) gate, safe-applied, and exercise-proved every WS-1/2a/8 acceptance criterion
LIVE. Shipped `portal-auth-v1.20.0`. Both deploy-completion ledgers CLOSED; the account-dependent
test user was created, exercised, and VERIFIED-DELETED atomically. Wave-1 is fully green pending
CVO's independent re-run.

## MCP traffic
~9 messages handled. Significant: MSTR-DIRECT context brief (mandate) · CTO~B GO (3 Wave-1 TOs) ·
CTO~B DESIGN arch-gate GO (RECOMMENDED) · CTO~B 2nd-gate GO to safe-apply · CTO~B GO on (a)
test-user (binding lifecycle conditions). Sent: READY ACK, WS-1 design, plan-for-2nd-gate, WS2a
500-not-401 correction, deploy RAVC, Wave-1-complete RAVC (all to CTO~B, CC MSTR).

## Compiler Tools
| Tool | Situation | Result | Note |
|---|---|---|---|
| comp-tagauthz (via safe-apply) | pre-apply authorization gate | PASS | 0 of 0 candidates overwrite an access-granting tag; default_tags Project/System key-collision checked clean |
| comp-pulse diff (risk-reflex, via safe-commit) | pre-commit danger-map | PASS | 5 files vs 1239 danger nodes; flagged iam.tf touch -> I grounded IAM on the live primitive |
| comp-iam service opalinvest-auth-handler | after-iam.tf-change check (Rule 20/22a) | PARTIAL | does NOT index the auth-handler by that name + is DESIRED/TF-only + models (action) not (action,resource) -> WRONG instrument for a NEW table; grounded instead on `aws iam simulate-principal-policy` (one --resource-arns/call, isolated +/- controls) per Rule 22a |

**What worked:** comp-tagauthz + the risk-reflex fired automatically inside safe-apply/safe-commit and
did real work (tag-authz clean; iam.tf immune-response nudge). **What failed:** comp-iam service is
not the right instrument for a new-table grant (correctly deferred to the live IAM primitive).
**Gap found:** none new -- the comp-iam action-not-resource limitation is already documented (Rule 22a).
Grounding beyond comp-* was direct Read + live aws (cloudfront get-origin-request-policy / wafv2
get-web-acl / iam simulate-principal-policy) with inline `# rail-checked:` markers on the CF inspects.

## Deployment Sequence + Verification (AE)
1. code (5 .ts) -> `tsc --noEmit` EXIT 0 -> bun esm bundle 105.82 KB (handler export present) -> safe-commit `70b2560f0`.
2. `build-nodejs-lambda.sh portal-auth opalinvest-auth-handler` -> zip sha `eTSZUm8eVGheF4tolXuoaOQPDh0nbV7qTle+q+xpJVc=` uploaded; source-map bumped.
3. TF (dynamodb.tf + iam.tf + waf-cloudfront.tf) -> `terraform validate` Success; `fmt` collateral on 2 unrelated files REVERTED -> safe-commit `a6d4f52ed`.
4. `terraform plan -out=/tmp/wave1.tfplan` -> **Plan: 1 to add, 3 to change, 0 to destroy** (DDB create / IAM append-only / WAF +AuthLoginRateLimit / Lambda artifact swap; CloudFront distribution NOT in change set) -> CTO~B 2nd gate PASS.
5. `safe-apply /tmp/wave1.tfplan` -> comp-tagauthz PASS -> **Apply complete! 1 added, 3 changed, 0 destroyed.**
6. 0-diff replan -> **"No changes. Your infrastructure matches the configuration."**
7. record-terraform-deploy (`067da416e`) -> tag `portal-auth-v1.20.0` -> `git push --follow-tags` (FF `5300b8867..067da416e` + new tag).
8. Deploy-completion ledger `portal-authhard-wave1` CLOSED (3/3 legs) -> `e2c70115e`.

**EXERCISE (Rule 22a, LIVE against opalinvest.dev):**
- WS-1 throttle: 8 wrong-pw -> `401,401,401,401,401,429,429,429` (progressive cooldown). Counter-reset: `401x4 -> 200 -> 401` (not 429).
- WS-1 reset/forgot: `200x5 -> 429` (independent; generic-200 below cap = enumeration-safe).
- WS-1 logs: `login_failed` + `auth_throttled` structured lines confirmed in `/aws/lambda/opalinvest-auth-handler` (hashed account, reason, ts). A log, no alarm.
- WS-1 IAM: simulate-principal-policy -> throttle table Get/Update/DeleteItem=allowed; PutItem (isolated neg control)=implicitDeny.
- WS-1 WAF: get-web-acl -> `AuthLoginRateLimit` Block/Limit 100/pri 2 live; existing RateLimitRule untouched.
- WS-2a: active refresh 200; **disabled -> /auth/refresh -> HTTP 500 + NO token minted**; re-enable -> 200. blast-containment: token firmId claim = the non-existent test firm.
- WS-8: `<12` rejected, breached `password1234` rejected, passphrase-with-spaces accepted (200); existing sub-12 user logs in (200).
- Test-user lifecycle: create -> exercise -> delete-item -> consistent-read GetItem NO Item; independent re-confirm GONE; ledger `portal-authhard-wave1-testuser` CLOSED.

## Files Modified
See commit messages: `70b2560f0` (5 .ts: throttle.ts + breached-passwords.ts NEW, auth.ts/index.ts/password.ts),
`a6d4f52ed` (dynamodb.tf/iam.tf/waf-cloudfront.tf/lambda-source-map.json), `067da416e` (source-map/CHANGELOG),
`e2c70115e` + `d84ac01d4` (deploy + testuser ledgers), `c9b9ce88a` + `d84ac01d4` (exercise deliverable).

## Blockers
None open. Two were surfaced-and-resolved in-session: (1) trusted-client-IP not available to the Lambda
(/auth/* forwards no CloudFront-* header) -> resolved by moving the per-IP axis to a WAF rate rule
(CTO~B RECOMMENDED, no CF-distribution edit); (2) test account needed for the account-dependent trio ->
CTO~B GO on (a), executed under binding lifecycle conditions, verified-deleted.

## Current State (handoff surface)
- **DEPLOYED + LIVE:** `portal-auth-v1.20.0` on `opalinvest-auth-handler` (nodejs22.x, us-east-1). New table
  `opal-portal-auth-throttle` (PAY_PER_REQUEST, PK=pk, TTL=ttl). WAF web-ACL `opal-cloudfront-protection`
  (id a09833c0-...) now has rule `AuthLoginRateLimit` (Block/100/pri2, scoped /auth/login|forgot-password|
  reset-password). IAM role `opalinvest-auth-lambda-role` inline policy `auth_permissions` has one added
  statement (Get/Update/DeleteItem on the throttle table ARN).
- **Code:** `infra/aws/opalinvest_dev/lambda/auth-handler/src/` -- new `throttle.ts` (progressive-cooldown,
  no-hard-lockout, sha256(email) keying, fail-open) + `breached-passwords.ts` (offline curated top-N);
  `auth.ts` login/forgot throttle + refresh status re-check; `index.ts` 429/Retry-After map; `password.ts`
  min12+passphrase+breached.
- **TF:** `infra/aws/terraform/portal-auth/{dynamodb,iam,waf-cloudfront}.tf`. Repo == live (0-diff verified).
- **Deliverable:** `org/tier2_senior/0.7.0_AE_CloudOps/deliverables/PORTAL_AUTHHARD_WAVE1_EXERCISE_20260720.md`.
- **Ledgers:** both CLOSED (`20260720T1629Z_portal-authhard-wave1`, `20260720T1644Z_...-testuser`). No open sentinels.
- **Follow-ups (out of Wave-1 scope):** (1) password-policy rejection returns HTTP 500 not 400 (pre-existing
  index.ts map; rejection correct, status poor UX); (2) WS-8 breached list is a curated top-N -- full top-10k
  needs an off-Opal egress word or a file drop; (3) WAF 100-req block-burst not run (prod-flood risk); (4)
  WS2a 500->403 map frontend-safe but not taken.

## Next Steps
- **[1.0.0_SA_CTO~B]** consolidated ground-truth pass at Wave-1 close (WAF on web-ACL / DDB / simulate /
  throttle-refresh-password exercises) -- your stated plan. Then route Wave-2 tasking (WS-2b revocation /
  WS-6 role-split / WS-3 MFA). Also: route CVO for the independent re-run (base->~Z lane change today) or
  clear me to ping 3.0.0_SA_CVO~Z directly.
- **[3.0.0_SA_CVO~Z]** independent exercise re-run -- deliverable has every assertion + evidence; both
  exercise scripts available on request.
- **[0.7.0_AE_CloudOps~B]** IDLE/reachable; holding for CTO~B consolidated pass + Wave-2. Follow-up #1
  (500->400 password map) is a trivial fast-follow if wanted.
