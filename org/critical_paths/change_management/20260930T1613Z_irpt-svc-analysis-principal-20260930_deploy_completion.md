# Deploy Completion Record
**Date opened:** 2026-09-30T16:13:47.846405+00:00
**Status:** OPEN
**Deploy:** svc-irpt-analysis: ONE durable Analysis service principal (opal-users-v2 row + Secrets Manager password), created ONCE under W27 halves CTO @dbbac713fc / CRO @2ab90bf162 on packet blob 4c1dbb545f; blast radius one row + one secret; rollback delete both; retirement DISABLE never delete
**Authored by:** 2.0.0_SA_COO~Y
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | opal-users-v2 USER#svc-irpt-analysis@opalinvest.com + secret irpt/svc-irpt-analysis/password | preread clean (row ABSENT, index 0, secret ABSENT); put + create; row read back by projection WITHOUT passwordHash equal to the intended attributes; secret DescribeSecret shows one AWSCURRENT version, value never printed |  | OPEN |
| S1 | verify | secret readers = the walker's principal only (CTO cond 2, CRO cond 3) | resource policy printed (Allow walker ARN; Deny GetSecretValue for every other PrincipalArn); simulate-principal-policy for the runner role and every investor-reporting function role reads DENY, denominator printed |  | OPEN |
| N1 | verify | negative control on the recorded-not-enforced limit (CTO cond 4) | under this principal, ONE API read of a NON-cottonwood resource (selected_tenant=inflection) with no vendor call; outcome printed; a SUCCESS is a BLOCKING row and the window waits for the CTO's re-read |  | OPEN |
| K2 | verify | the principal can log in (K2) and the cottonwood read is admitted | POST /auth/login 200 with a token (never printed); GET status?selected_tenant=cottonwood outcome printed |  | OPEN |

## Log

- 20260930T161347Z OPENED by 2.0.0_SA_COO~Y with 4 leg(s)
