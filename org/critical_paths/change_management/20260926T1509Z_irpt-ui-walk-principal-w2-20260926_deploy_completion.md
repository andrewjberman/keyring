# Deploy Completion Record
**Date opened:** 2026-09-26T15:09:35.045450+00:00
**Status:** OPEN
**Deploy:** Window 2: bounded admin+internal+Dev principal (packet v7 blob 3edebd85; CTO + CRO halves): ~Y K4 upload + K5 /analysis (hop 3) on the jsonschema-fixed generate; ~D K6 = ONE 49F account-level Performance page read (export-B BEFORE); K3 selections retained; deleted after
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | opal-users-v2 K1 (admin, opal-capital, Dev) + SSM K1-CRED | pre-read clean + census baseline; put + read-back digest | 15:10:02Z K1 USER#usr_irptuiwalk_1790435397 put (attribute_not_exists), read-back digest e151a99f.. EQUAL (passwordHash excluded); role admin / opal-capital / Dev, no MFA fields; K1-CRED /irpt/ui-walk-principal/1790435397/password (name only); pre-read clean; census 15:09:36Z users 50 digest 0cb6bf08.., SELECTION# 37 (UI_WALK_W2_CENSUS_BEFORE_20260926.json); both halves on v7 3edebd85 at HEAD; handed to ~D (K6) and ~Y (K4, K5) 15:10Z; delete by 16:08Z (cron 9fd10e72) | CLOSED 20260926T151202Z |
| D1 | verify | K1 delete | consistent GetItem no Item + CloudFront login refused 1 of 1 + K1-CRED ParameterNotFound + ~D reload /login | 15:26:02Z K1 DeleteItem -> consistent GetItem no Item (VERIFIED); email-index 0; CloudFront login -> HTTP 401 Invalid email or password, REFUSED 1 of 1; K1-CRED ParameterNotFound. Both walkers done first: ~Y 101272 (K4 NORMALIZED portfolio_f40b800e.., K5 UNEXPECTED S3 GetObjectVersion denied, nothing written), ~D 101273 (K6). ~D reload for /login still owed (A1). | CLOSED 20260926T152642Z |
| A1 | verify | route-graded audit | HAR + ~Y logs: 0 outside admitted classes, 0 /auth/admin; users digest == baseline; SELECTION# new ids traced; K4/K5/K6 writes named; no IRPT/auth request after last exp |  | OPEN |

## Log

- 20260926T150935Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260926T151202Z LEG C1 closed: 15:10:02Z K1 USER#usr_irptuiwalk_1790435397 put (attribute_not_exists), read-back digest e151a99f.. EQUAL (passwordHash 
- 20260926T152642Z LEG D1 closed: 15:26:02Z K1 DeleteItem -> consistent GetItem no Item (VERIFIED); email-index 0; CloudFront login -> HTTP 401 Invalid em
