# Deploy Completion Record
**Date opened:** 2026-09-25T15:46:41.481404+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260925T155103Z
**Deploy:** Export section A2: V2 opal-portal-authorizer with the render branch + exp fix + render public key env (targeted)
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 2.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| A1 | activation | aws_lambda_function.portal_authorizer | CodeSha256 == sgQWoygZ..; env IRPT_RENDER_JWT_PUBLIC_KEY_PEM equals the render public key's current slot | targeted safe-apply (0/1/0; tagauthz PASSED) 15:48:45Z: opal-portal-authorizer CodeSha256 sgQWoygZdbs8wX3Iknehfdo2mj6b17mQ48N+sepxdp4= == artifact content-sha256 (bun ESM bundle of CLOUD @972976ebca: render branch + exp fix; OPSEC signer TTL d09246e8fd rides as RELEASED -- its owner's completion commit carries its own deploy ledger and it is live in opalinvest-auth-handler @6328a6fbb2 since 2026-09-16); env IRPT_RENDER_JWT_PUBLIC_KEY_PEM == the render public key's current slot | CLOSED 20260925T155009Z |
| N1 | verify | negative arm before and after | no-token and bogus-bearer invokes deny before and after; real human verifications continue in the authorizer log after deploy with no error spike | BEFORE and AFTER the deploy, direct invokes of opal-portal-authorizer with no token and with a bogus bearer both answer {isAuthorized:false}. Human path live: the 30 min before, 19 invocations / 17 human 'Token verified successfully' / 0 failed; after 15:48:46Z, 6 invocations / 4 verified / 0 verification failures / 0 runtime errors (authorizer log). | CLOSED 20260925T155103Z |
| V1 | verify | targeted re-plan | No changes | targeted terraform plan (-target=aws_lambda_function.portal_authorizer) after apply: No changes | CLOSED 20260925T155009Z |

## Log

- 20260925T154641Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260925T155009Z LEG A1 closed: targeted safe-apply (0/1/0; tagauthz PASSED) 15:48:45Z: opal-portal-authorizer CodeSha256 sgQWoygZdbs8wX3Iknehfdo2mj6b17
- 20260925T155009Z LEG V1 closed: targeted terraform plan (-target=aws_lambda_function.portal_authorizer) after apply: No changes
- 20260925T155103Z LEG N1 closed: BEFORE and AFTER the deploy, direct invokes of opal-portal-authorizer with no token and with a bogus bearer both answer 
- 20260925T155103Z CLOSED -- all 3 legs proven
