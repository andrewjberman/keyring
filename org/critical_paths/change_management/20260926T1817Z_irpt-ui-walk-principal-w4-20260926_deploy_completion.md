# Deploy Completion Record
**Date opened:** 2026-09-26T18:17:05.605892+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T215118Z
**Deploy:** Window 4: bounded admin+internal+Dev principal (packet v10 blob 32c85e40; CTO + CRO halves): ~D K7 page read (the report K8 exports) then K8 the FIRST real Performance export (render ON behind the S148 fence); deleted after
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | opal-users-v2 K1 + SSM K1-CRED | pre-read clean + census baseline; put + read-back digest | 18:17:54Z K1 USER#usr_irptuiwalk_1790446664 put (attribute_not_exists), read-back digest d2b70ae1.. EQUAL; admin/opal-capital/Dev; K1-CRED /irpt/ui-walk-principal/1790446664/password (name only); pre-read clean; census 18:17:08Z users 50 digest 0cb6bf08.., SELECTION# 41; both halves on v10 32c85e40; handed to ~D 18:18Z; delete by 19:13Z (cron) | CLOSED 20260926T181836Z |
| D1 | verify | K1 delete | consistent GetItem no Item + CloudFront login refused 1 of 1 + K1-CRED ParameterNotFound + ~D reload /login | 18:23:07Z K1 DeleteItem -> consistent GetItem no Item (VERIFIED); CloudFront login -> HTTP 401 Invalid email or password, REFUSED 1 of 1; K1-CRED ParameterNotFound; ~D reload 18:25:50Z landed /login (msg 101426). Deleted after ~D's done (101418): K7 OBJECT_NOT_COVERED (ReportDenied at a cross-principal REOPEN, pre-existing -- CTO 101429), K8 not run. | CLOSED 20260926T183004Z |
| A1 | verify | route-graded audit + export outcome | HAR: 0 outside admitted classes (1 POST /export), 0 /auth/admin; users digest == baseline; SELECTION# traced; export rows/objects named; render-token names 0 after; no IRPT/auth request after last exp | ~D 101426: HAR (sha256 e217c72e..) route census denominator 113 = 107 GET/HEAD/OPTIONS + 3 refresh + 1 login + 1 resolve + 1 selections, 0 export POST (K8 NOT run: K7 answered OBJECT_NOT_COVERED = P-REOPEN-01, since fixed and served 20:17:50Z), 0 outside the admitted classes, 0 /auth/admin; users census 50 -> 50, digest 0cb6bf08.. EQUAL to baseline; SELECTION# 41 -> 41 (the page's selection mapped to an existing content-addressed row; 0 new, 0 gone); render-token parameters under /irpt/render-token/: 0; opalinvest-auth-handler and opal-portal-authorizer: 0 log events naming irpt-uiwalk-1790446664 after the verified delete (18:23:08Z -> read 21:5xZ). Interval [18:17:54Z K1 put, 18:23:07Z delete verified; last access exp <= 18:38Z]. Closed late: the 18:36Z close cron did not survive the session boundary. | CLOSED 20260926T215118Z |

## Log

- 20260926T181705Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260926T181836Z LEG C1 closed: 18:17:54Z K1 USER#usr_irptuiwalk_1790446664 put (attribute_not_exists), read-back digest d2b70ae1.. EQUAL; admin/opal-ca
- 20260926T183004Z LEG D1 closed: 18:23:07Z K1 DeleteItem -> consistent GetItem no Item (VERIFIED); CloudFront login -> HTTP 401 Invalid email or password
- 20260926T215118Z LEG A1 closed: ~D 101426: HAR (sha256 e217c72e..) route census denominator 113 = 107 GET/HEAD/OPTIONS + 3 refresh + 1 login + 1 resolve
- 20260926T215118Z CLOSED -- all 3 legs proven
