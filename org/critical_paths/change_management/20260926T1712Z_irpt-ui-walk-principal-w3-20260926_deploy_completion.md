# Deploy Completion Record
**Date opened:** 2026-09-26T17:12:00.662986+00:00
**Status:** OPEN
**Deploy:** Window 3: bounded admin+internal+Dev principal (packet v8 blob acca1b3e; CTO + CRO halves): ~Y K4 upload + K5 /analysis (hop 3) after the generate grants; K6 not re-run; deleted after
**Authored by:** 2.0.0_SA_COO~P
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| C1 | activation | opal-users-v2 K1 + SSM K1-CRED | pre-read clean + census baseline; put + read-back digest | 17:12:38Z K1 USER#usr_irptuiwalk_1790442753 put (attribute_not_exists), read-back digest a8237906.. EQUAL; admin/opal-capital/Dev; K1-CRED /irpt/ui-walk-principal/1790442753/password (name only); pre-read clean; census 17:12:02Z users 50 digest 0cb6bf08.., SELECTION# 41; both halves on v8 acca1b3e (CTO 94e6555b48, CRO 243bf8a1e3); handed to ~Y 17:12Z; delete by 18:08Z (cron) | CLOSED 20260926T171323Z |
| D1 | verify | K1 delete | consistent GetItem no Item + CloudFront login refused 1 of 1 + K1-CRED ParameterNotFound |  | OPEN |
| A1 | verify | audit | ~Y's log: 1 login + ONE analysis/inputs + ONE /analysis, nothing else; users digest == baseline; no IRPT/auth request after last exp |  | OPEN |

## Log

- 20260926T171200Z OPENED by 2.0.0_SA_COO~P with 3 leg(s)
- 20260926T171323Z LEG C1 closed: 17:12:38Z K1 USER#usr_irptuiwalk_1790442753 put (attribute_not_exists), read-back digest a8237906.. EQUAL; admin/opal-ca
