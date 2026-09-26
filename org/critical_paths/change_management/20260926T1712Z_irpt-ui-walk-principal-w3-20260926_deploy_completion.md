# Deploy Completion Record
**Date opened:** 2026-09-26T17:12:00.662986+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260926T173343Z
**Deploy:** Window 3: bounded admin+internal+Dev principal (packet v8 blob acca1b3e; CTO + CRO halves): ~Y K4 upload + K5 /analysis (hop 3) after the generate grants; K6 not re-run; deleted after
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | opal-users-v2 K1 + SSM K1-CRED | pre-read clean + census baseline; put + read-back digest | 17:12:38Z K1 USER#usr_irptuiwalk_1790442753 put (attribute_not_exists), read-back digest a8237906.. EQUAL; admin/opal-capital/Dev; K1-CRED /irpt/ui-walk-principal/1790442753/password (name only); pre-read clean; census 17:12:02Z users 50 digest 0cb6bf08.., SELECTION# 41; both halves on v8 acca1b3e (CTO 94e6555b48, CRO 243bf8a1e3); handed to ~Y 17:12Z; delete by 18:08Z (cron) | CLOSED 20260926T171323Z |
| D1 | verify | K1 delete | consistent GetItem no Item + CloudFront login refused 1 of 1 + K1-CRED ParameterNotFound | 17:22:22Z K1 DeleteItem -> consistent GetItem no Item (VERIFIED); CloudFront login -> HTTP 401 Invalid email or password, REFUSED 1 of 1; K1-CRED ParameterNotFound; after ~Y's done (msg 101352) | CLOSED 20260926T173230Z |
| A1 | verify | audit | ~Y's log: 1 login + ONE analysis/inputs + ONE /analysis, nothing else; users digest == baseline; no IRPT/auth request after last exp | ~Y's log (msgs 101352): 1 login + ONE POST analysis/inputs (K4 NORMALIZED portfolio_d188498e.., handled=1 17:15:35Z, +7 rows) + ONE POST /analysis (K5 UNEXPECTED MaintainedSourceRefused 'maintained recipe title descriptor required', corr-85a852bf59dd, nothing written, no vendor call); no page walk in this window (no HAR). Census before 17:12:02Z / after 17:31:23Z: users 50 -> 50 digest 0cb6bf08.. EQUAL; SELECTION# 41 -> 41. IRPT logs after 17:32:00Z (read 17:33:00Z, a 1-minute window just past the last token's exp ~17:31Z): 0 events in 6 functions. Interval [17:12:38Z put, ~17:31Z last exp]; deleted 17:22:22Z. | CLOSED 20260926T173343Z |

## Log

- 20260926T171200Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260926T171323Z LEG C1 closed: 17:12:38Z K1 USER#usr_irptuiwalk_1790442753 put (attribute_not_exists), read-back digest a8237906.. EQUAL; admin/opal-ca
- 20260926T173230Z LEG D1 closed: 17:22:22Z K1 DeleteItem -> consistent GetItem no Item (VERIFIED); CloudFront login -> HTTP 401 Invalid email or password
- 20260926T173343Z LEG A1 closed: ~Y's log (msgs 101352): 1 login + ONE POST analysis/inputs (K4 NORMALIZED portfolio_d188498e.., handled=1 17:15:35Z, +7 
- 20260926T173343Z CLOSED -- all 3 legs proven
