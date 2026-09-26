# Deploy Completion Record
**Date opened:** 2026-09-26T13:51:54.574384+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T144234Z
**Deploy:** Bounded admin+internal+Dev UI-walk principal (packet v3 blob 07b7a000; CTO b70ede1756, CRO a157c45762): K1 + K1-CRED, walked by ~D (HAR) + ~Y's ONE upload (K4, one resident securities_info GET); K3 selections retained; deleted after
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | opal-users-v2 K1 (role admin, opal-capital, userType Dev) + SSM K1-CRED (name only) | pre-read clean + user/selection census baseline; put + consistent read-back digest (passwordHash excluded) | 13:53:14Z K1 USER#usr_irptuiwalk_1790430787 put (attribute_not_exists), consistent read-back digest 24058c3c.. EQUAL (passwordHash excluded); role admin, firmId opal-capital, userType Dev, status active, no MFA fields; K1-CRED /irpt/ui-walk-principal/1790430787/password SecureString alias/aws/ssm (name only); pre-read clean; census baseline 13:51:56Z users 50 digest 0cb6bf08.., SELECTION# 34 (UI_WALK_CENSUS_BEFORE_20260926.json @ef091bc82e); handed to ~D and ~Y 13:53Z; delete by 14:53Z (cron 3d36d71d) | CLOSED 20260926T135447Z |
| D1 | verify | K1 delete | consistent GetItem no Item + CloudFront login refused 1 of 1 + K1-CRED ParameterNotFound + ~D reload lands /login | 14:22:22Z K1 DeleteItem -> consistent GetItem no Item (VERIFIED); email-index 0; login through CloudFront (https://opalinvest.dev/auth/login) with the password -> HTTP 401 Invalid email or password, REFUSED 1 of 1 (the discriminating arm the 03:30Z delete lacked); K1-CRED -> ParameterNotFound. Both walkers done first: ~D 14:14Z (msg 101220), ~Y K5 14:18:08Z (msg 101227). ~D reload for /login asked 14:22Z (A1). | CLOSED 20260926T142326Z |
| A1 | verify | route-graded audit | HAR + ~Y log: 0 requests outside the admitted classes, 0 /auth/admin; user census == baseline; SELECTION# new ids traced to /selections POSTs; K4 rows named; no IRPT/auth request after last exp | Route-graded audit (P's own read of ~D's HAR prod-uiwalk-20260926.har sha256 6b51023c.., on disk, gitignored): 350 entries = 335 GET/HEAD/OPTIONS + 9 auth login/refresh + 3 POST directory/resolve + 3 POST selections; 0 outside the admitted classes; 0 /auth/admin; 0 JWT-shaped strings, 0 Bearer values. ~Y (msgs 101196/101227): 2 logins, ONE POST /analysis/inputs (K4 NORMALIZED 12.03), ONE POST /analysis (K5 UNEXPECTED jsonschema, nothing written, no vendor call). Census before 13:51:56Z / after 14:31:01Z: users 50 -> 50, status/role/type digest 0cb6bf08.. EQUAL; SELECTION# 34 -> 37 (+3 = the HAR's 3 selections POSTs, K3 retained). ~D reload 14:23:48Z landed /login. IRPT logs after 14:34:00Z (last token exp ~14:33Z), 6 functions: 0 requests, only irpt_warm keep-warm (6). Interval [13:53:14Z put, 14:33Z last exp]; deleted 14:22:22Z. | CLOSED 20260926T144234Z |

## Log

- 20260926T135154Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260926T135447Z LEG C1 closed: 13:53:14Z K1 USER#usr_irptuiwalk_1790430787 put (attribute_not_exists), consistent read-back digest 24058c3c.. EQUAL (pa
- 20260926T142326Z LEG D1 closed: 14:22:22Z K1 DeleteItem -> consistent GetItem no Item (VERIFIED); email-index 0; login through CloudFront (https://opali
- 20260926T144234Z LEG A1 closed: Route-graded audit (P's own read of ~D's HAR prod-uiwalk-20260926.har sha256 6b51023c.., on disk, gitignored): 350 entri
- 20260926T144234Z CLOSED -- all 3 legs proven
