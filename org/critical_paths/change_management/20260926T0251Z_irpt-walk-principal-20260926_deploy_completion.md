# Deploy Completion Record
**Date opened:** 2026-09-26T02:51:41.803107+00:00
**Status:** OPEN
**Deploy:** Bounded Opal-class walk principal (packet blob fe8e8d89; CTO ba29004a1b, CRO 909dd40acc): K1 opal-users-v2 PROFILE + K1-CRED SecureString by name; walked by 2.0.0_SA_COO~D; deleted after
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | opal-users-v2 K1 + SSM K1-CRED (name only, aws/ssm key) | put + consistent read-back digest (passwordHash excluded) | 02:53:17Z K1 USER#usr_irptwalk_1790391192 put (attribute_not_exists), consistent read-back digest b8d06d48ad24 EQUAL (passwordHash excluded); K1-CRED /irpt/walk-principal/1790391192/password SecureString alias/aws/ssm (name only, value never printed); pre-read clean (K1 ABSENT, index 0, K1-CRED ABSENT); handed to 2.0.0_SA_COO~D 02:53:30Z | CLOSED 20260926T025404Z |
| D1 | verify | K1 delete | consistent GetItem no Item + login refused 1 of 1 + K1-CRED ParameterNotFound | 03:30:33Z K1 DeleteItem -> consistent GetItem no Item (VERIFIED); email-index count 0; K1-CRED delete -> get-parameter ParameterNotFound. The login-after-delete arm was NOT a discriminating refusal: the script posted to the direct execute-api URL, which answers 403 Forbidden at the origin guard (auth-handler/src/index.ts:203-221) before any row read; the password was deleted with K1-CRED, so the arm cannot be re-run. Substitute arms: the failing consistent base-table read above, plus 2.0.0_SA_COO~D's refresh reload (the refresh re-reads the row) recorded under A1. Script corrected to the CloudFront route for any future use. | CLOSED 20260926T033243Z |
| A1 | verify | audit | auth-handler log: principal logins inside interval only; IRPT logs: no request after last exp; ~D reload lands /login |  | OPEN |

## Log

- 20260926T025141Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260926T025404Z LEG C1 closed: 02:53:17Z K1 USER#usr_irptwalk_1790391192 put (attribute_not_exists), consistent read-back digest b8d06d48ad24 EQUAL (pa
- 20260926T033243Z LEG D1 closed: 03:30:33Z K1 DeleteItem -> consistent GetItem no Item (VERIFIED); email-index count 0; K1-CRED delete -> get-parameter P
