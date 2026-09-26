# Deploy Completion Record
**Date opened:** 2026-09-26T21:52:38.867790+00:00
**Status:** OPEN
**Deploy:** Window 5: bounded admin+internal+Dev principal for ~D's read-only C25 walk on local portal DEV 5174 (packet blob 4b68468e; CTO SIGNOFF_UI_WALK_W5_20260926.md, CRO @0571ef3cd2); deleted after
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | opal-users-v2 K1 + SSM K1-CRED | pre-read clean + census baseline (users, SELECTION#, REPORT#); put + read-back digest | pre-read 21:52Z: K1 ABSENT, email-index 0, K1-CRED ABSENT; baseline UI_WALK_W5_CENSUS_BEFORE_20260926.json: users 50 digest 0cb6bf08d2c6293d (== w4 baseline), SELECTION# 45, REPORT# 49financial 17 / cottonwood 0 / inflection 0; 21:53:51Z K1 USER#usr_irptuiwalk_1790459579 put (attribute_not_exists), read-back digest a8183a7e.. EQUAL (passwordHash excluded); K1-CRED /irpt/ui-walk-principal/1790459579/password (value never printed); handed to ~D by NAME; deadline 22:53Z (60 min) | CLOSED 20260926T215419Z |
| D1 | verify | K1 delete | consistent GetItem no Item + CloudFront login refused 1 of 1 + K1-CRED ParameterNotFound + ~D reload /login |  | OPEN |
| A1 | verify | route-graded audit | HAR: 0 outside login/refresh/POST resolve/POST selections/GET-HEAD-OPTIONS, 0 /export, 0 /analysis, 0 /auth/admin; users == baseline; SELECTION#/REPORT# new ids traced; no auth line after last exp |  | OPEN |

## Log

- 20260926T215238Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260926T215419Z LEG C1 closed: pre-read 21:52Z: K1 ABSENT, email-index 0, K1-CRED ABSENT; baseline UI_WALK_W5_CENSUS_BEFORE_20260926.json: users 50 dig
