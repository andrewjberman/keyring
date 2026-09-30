# Deploy Completion Record
**Date opened:** 2026-09-30T16:13:47.846405+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260930T162742Z
**Deploy:** svc-irpt-analysis: ONE durable Analysis service principal (opal-users-v2 row + Secrets Manager password), created ONCE under W27 halves CTO @dbbac713fc / CRO @2ab90bf162 on packet blob 4c1dbb545f; blast radius one row + one secret; rollback delete both; retirement DISABLE never delete
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | opal-users-v2 USER#svc-irpt-analysis@opalinvest.com + secret irpt/svc-irpt-analysis/password | preread clean (row ABSENT, index 0, secret ABSENT); put + create; row read back by projection WITHOUT passwordHash equal to the intended attributes; secret DescribeSecret shows one AWSCURRENT version, value never printed | 16:19:29Z preread clean (row ABSENT, index 0, secret ResourceNotFoundException); secret created arn:...:secret:irpt/svc-irpt-analysis/password-rfHf9l, 1 version AWSCURRENT 0bae1828, value never printed; row USER#svc-irpt-analysis@opalinvest.com put conditional, read-back digest 38b676a95c54 (passwordHash excluded) EQUAL; readback projection 18 of 18 attributes: role admin, userType service, firmId opal-capital, status active, allowedFirmIds cottonwood, tier internal, mfaEnabled false, mustChangePassword false, createdBy 2.0.0_SA_COO~Y svc-irpt-analysis-20260930; email-index count 1 | CLOSED 20260930T162549Z |
| S1 | verify | secret readers = the walker's principal only (CTO cond 2, CRO cond 3) | resource policy printed (Allow walker ARN; Deny GetSecretValue for every other PrincipalArn); simulate-principal-policy for the runner role and every investor-reporting function role reads DENY, denominator printed | resource policy re-put 16:2xZ naming the secret ARN explicitly: Allow arn:aws:iam::313476888478:user/Andrew_Berman GetSecretValue+DescribeSecret; Deny GetSecretValue Principal * Condition ArnNotEquals aws:PrincipalArn walker. simulate-principal-policy with that resource policy over 24 roles (every irpt-*/investor-*/ycharts-* role incl. irpt-ycharts-runner-role and irpt-ycharts-generate-role): allowed 0, explicitDeny 24, denominator 24 (iam list-roles filter); the walker's user is the one Allow | CLOSED 20260930T162549Z |
| N1 | verify | negative control on the recorded-not-enforced limit (CTO cond 4) | under this principal, ONE API read of a NON-cottonwood resource (selected_tenant=inflection) with no vendor call; outcome printed; a SUCCESS is a BLOCKING row and the window waits for the CTO's re-read | OUTCOME = SUCCEEDED (the branch the CTO half names as a BLOCKING row): under svc-irpt-analysis, GET /api/scoped/investor-reporting/directory/search?selected_tenant=inflection&q=&limit=1 answered HTTP 200 with 1 directory entry of INFLECTION served (counts only logged); status-summary on inflection resolved firm_id fir_b6b200b4395e94aaa604d5fa (NOT_FOUND = no job, not a scope refusal). No vendor call reached (Opal API only). The API admits any SELECTED firm for this principal (FIRM_OPERATIONS on the selected firm); allowedFirmIds is enforced only in the resident since IB-yr-293 @784ac650d0. BLOCKING row filed; the window WAITS for the CTO's re-read (CTO half condition 4). Log: deliverables/IRPT_MVP_Y/live_walk/SVC_PRINCIPAL_NEGCONTROL_20260930.json | CLOSED 20260930T162741Z |
| K2 | verify | the principal can log in (K2) and the cottonwood read is admitted | POST /auth/login 200 with a token (never printed); GET status?selected_tenant=cottonwood outcome printed | POST /auth/login (CloudFront same-origin) HTTP 200, accessToken present (never printed), mfaRequired none, 16:2xZ; GET directory/search?selected_tenant=cottonwood&q=&limit=1 HTTP 200, 1 entry served; status-summary cottonwood resolved fir_0fe2a06331f1b4a68133fcb2 (NOT_FOUND = no job yet) | CLOSED 20260930T162742Z |

## Log

- 20260930T161347Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
- 20260930T162549Z LEG C1 closed: 16:19:29Z preread clean (row ABSENT, index 0, secret ResourceNotFoundException); secret created arn:...:secret:irpt/svc-
- 20260930T162549Z LEG S1 closed: resource policy re-put 16:2xZ naming the secret ARN explicitly: Allow arn:aws:iam::313476888478:user/Andrew_Berman GetSe
- 20260930T162741Z LEG N1 closed: OUTCOME = SUCCEEDED (the branch the CTO half names as a BLOCKING row): under svc-irpt-analysis, GET /api/scoped/investor
- 20260930T162742Z LEG K2 closed: POST /auth/login (CloudFront same-origin) HTTP 200, accessToken present (never printed), mfaRequired none, 16:2xZ; GET d
- 20260930T162742Z CLOSED -- all 4 legs proven
