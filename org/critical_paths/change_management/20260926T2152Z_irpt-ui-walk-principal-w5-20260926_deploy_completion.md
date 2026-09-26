# Deploy Completion Record
**Date opened:** 2026-09-26T21:52:38.867790+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T225710Z
**Deploy:** Window 5: bounded admin+internal+Dev principal for ~D's read-only C25 walk on local portal DEV 5174 (packet blob 4b68468e; CTO SIGNOFF_UI_WALK_W5_20260926.md, CRO @0571ef3cd2); deleted after
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | opal-users-v2 K1 + SSM K1-CRED | pre-read clean + census baseline (users, SELECTION#, REPORT#); put + read-back digest | pre-read 21:52Z: K1 ABSENT, email-index 0, K1-CRED ABSENT; baseline UI_WALK_W5_CENSUS_BEFORE_20260926.json: users 50 digest 0cb6bf08d2c6293d (== w4 baseline), SELECTION# 45, REPORT# 49financial 17 / cottonwood 0 / inflection 0; 21:53:51Z K1 USER#usr_irptuiwalk_1790459579 put (attribute_not_exists), read-back digest a8183a7e.. EQUAL (passwordHash excluded); K1-CRED /irpt/ui-walk-principal/1790459579/password (value never printed); handed to ~D by NAME; deadline 22:53Z (60 min) | CLOSED 20260926T215419Z |
| D1 | verify | K1 delete | consistent GetItem no Item + CloudFront login refused 1 of 1 + K1-CRED ParameterNotFound + ~D reload /login | ~D 101554 done 22:26Z; 22:32:14Z K1 DeleteItem -> consistent GetItem no Item (VERIFIED); CloudFront login -> HTTP 401 Invalid email or password, REFUSED 1 of 1; K1-CRED ParameterNotFound; deadline cron a8967004 cancelled; ~D asked to reload once (101555) | CLOSED 20260926T225710Z |
| A1 | verify | route-graded audit | HAR: 0 outside login/refresh/POST resolve/POST selections/GET-HEAD-OPTIONS, 0 /export, 0 /analysis, 0 /auth/admin; users == baseline; SELECTION#/REPORT# new ids traced; no auth line after last exp | ~D 101554: HAR c25-devwalk-20260926.har sha256 95d13753..35314, 974 entries, leak check clean; writes that left = login 1, refresh 8, resolve 6, selections 5; /export, /analysis, /auth/admin = 0 -> 0 outside the admitted classes. SELECTION# 45 -> 45 (0 new, 0 gone); REPORT# 49F 17 -> 17, COT 0 -> 0, INF 0 -> 0 (the walk's Performance reads were reopens or refusals; no new retained report). Users 50 -> 51: the ONE new PROFILE is USER#usr_opal_ui_walker created 21:54:51Z by '4.0.0_SA_CRO ui-walker (Andrew-direct 20260926)', status disabled -- the CRO's own dormant /ui-walk service account (447daa112d), not this window's principal and not a HAR request (0 /auth/admin), so not branch (d). Auth handler and authorizer: 0 events naming irpt-uiwalk-1790459579 after 22:32:15Z (read 22:56Z, past the last access exp <= 22:47Z). Observations for the CTO: first Performance open 931 ms answered UNAVAILABLE/DEPENDENCY_UNAVAILABLE = VendorEgressRefused (an INF/COT account with no armed one-use plan, 11 such records 21:56-22:19Z; designed, the goal criterion-1 gap); the window-4 account reopen by this second principal rendered PARTIAL 8.05% YTD in 1,968 ms (P-REOPEN-01 + fix M in the page). Interval [21:53:51Z, 22:32:14Z; last access exp <= 22:47Z]. | CLOSED 20260926T225710Z |

## Log

- 20260926T215238Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260926T215419Z LEG C1 closed: pre-read 21:52Z: K1 ABSENT, email-index 0, K1-CRED ABSENT; baseline UI_WALK_W5_CENSUS_BEFORE_20260926.json: users 50 dig
- 20260926T225710Z LEG D1 closed: ~D 101554 done 22:26Z; 22:32:14Z K1 DeleteItem -> consistent GetItem no Item (VERIFIED); CloudFront login -> HTTP 401 In
- 20260926T225710Z LEG A1 closed: ~D 101554: HAR c25-devwalk-20260926.har sha256 95d13753..35314, 974 entries, leak check clean; writes that left = login 
- 20260926T225710Z CLOSED -- all 3 legs proven
