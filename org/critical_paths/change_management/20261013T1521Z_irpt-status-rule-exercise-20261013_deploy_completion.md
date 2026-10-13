# Deploy Completion Record
**Date opened:** 2026-10-13T15:21:17.730981+00:00
**Status:** OPEN
**Deploy:** IRPT_ANLREQ TO-EXERCISE-R21: driven exercise of the status rule on irpt-directory-search: synthetic internal identities norow, disabled (and active) select cottonwood through the live edge; rows written for the sitting and removed; pair COO blob d1d4296341 + CTO half @decdd94c48 (choice A)
**Authored by:** 0.7.0_AE_CloudOps~AQ2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 3.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| E1 | verify | step 0: grants met, open-entry denominator (no open entry naming opal-users-v2 or irpt-directory-search); pair step 1: three USER# keys ABSENT by ConsistentRead and the email index returns nothing | reads printed |  | OPEN |
| E2 | activation | write disabled and active rows (attribute_not_exists(PK), with email); ConsistentRead each back | two items PRESENT as designed |  | OPEN |
| E3 | verify | one token per identity (held in process only), three GETs norow then disabled then active-only-if-both-refused, >=60s apart; UTC start, status, refusal code, body sha256 | per-request record |  | OPEN |
| E4 | verify | per-sub-window INTERNAL-CALLER-CLASS counts with streams denominator | one line per sub-window with the expected class |  | OPEN |
| E5 | activation | after later exp: delete written rows (attribute_exists(PK)); all three addresses ABSENT by GSI and ConsistentRead | six ABSENT reads |  | OPEN |
| E6 | verify | counts to 1.0.0_SA_CTO~DELL2, report to 2.0.0_SA_COO~Y2, signing-key read reported via 0.0.0_AB_MSTR~DELL2 | messages sent |  | OPEN |

## Log

- 20261013T152117Z OPENED by 0.7.0_AE_CloudOps~AQ2 with 6 leg(s)
