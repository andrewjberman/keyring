# Deploy Completion Record
**Date opened:** 2026-09-26T13:51:54.574384+00:00
**Status:** OPEN
**Deploy:** Bounded admin+internal+Dev UI-walk principal (packet v3 blob 07b7a000; CTO b70ede1756, CRO a157c45762): K1 + K1-CRED, walked by ~D (HAR) + ~Y's ONE upload (K4, one resident securities_info GET); K3 selections retained; deleted after
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | opal-users-v2 K1 (role admin, opal-capital, userType Dev) + SSM K1-CRED (name only) | pre-read clean + user/selection census baseline; put + consistent read-back digest (passwordHash excluded) | 13:53:14Z K1 USER#usr_irptuiwalk_1790430787 put (attribute_not_exists), consistent read-back digest 24058c3c.. EQUAL (passwordHash excluded); role admin, firmId opal-capital, userType Dev, status active, no MFA fields; K1-CRED /irpt/ui-walk-principal/1790430787/password SecureString alias/aws/ssm (name only); pre-read clean; census baseline 13:51:56Z users 50 digest 0cb6bf08.., SELECTION# 34 (UI_WALK_CENSUS_BEFORE_20260926.json @ef091bc82e); handed to ~D and ~Y 13:53Z; delete by 14:53Z (cron 3d36d71d) | CLOSED 20260926T135447Z |
| D1 | verify | K1 delete | consistent GetItem no Item + CloudFront login refused 1 of 1 + K1-CRED ParameterNotFound + ~D reload lands /login |  | OPEN |
| A1 | verify | route-graded audit | HAR + ~Y log: 0 requests outside the admitted classes, 0 /auth/admin; user census == baseline; SELECTION# new ids traced to /selections POSTs; K4 rows named; no IRPT/auth request after last exp |  | OPEN |

## Log

- 20260926T135154Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260926T135447Z LEG C1 closed: 13:53:14Z K1 USER#usr_irptuiwalk_1790430787 put (attribute_not_exists), consistent read-back digest 24058c3c.. EQUAL (pa
