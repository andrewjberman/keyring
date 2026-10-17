# Deploy Completion Record
**Date opened:** 2026-10-17T11:37:12.811219+00:00
**Status:** OPEN
**Deploy:** IRPT_DASHBD TO-DB-b-331: two synthetic V-leg users rows in opal-users-v2, minted, handed to S2 by broker, removed and read ABSENT twice
**Authored by:** 0.7.0_AE_CloudOps~IB2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | activation | mint the COVERING and NON_COVERING rows once each in opal-users-v2 | MINT-OK READBACK-OK for both plus email-index count 1 each | MINT-OK READBACK-OK for COVERING and NON_COVERING, entitlement_rows=0 each, email-index counts [1, 1], both sign-ins 200 (minted 11:38Z) | CLOSED 20261017T113834Z |
| L2 | verify | hand both sessions to 2.0.0_SA_COO~S2 by broker | broker delivery receipt, 2 sessions | both sessions sent to 2.0.0_SA_COO~S2 by broker at 11:38:54Z (delivered receipt, 2 sessions); scratch copy deleted | CLOSED 20261017T113921Z |
| L3 | verify | remove both rows after the issuer word V leg done | ABSENT GSI and ABSENT CONSISTENT read twice per row | both rows removed after V leg done (msg 10524); ABSENT GSI and ABSENT CONSISTENT read three times per row, the last two a minute apart; p197 DBC197-2-AC1 PASS | CLOSED 20261017T120009Z |

## Log

- 20261017T113712Z OPENED by 0.7.0_AE_CloudOps~IB2 with 3 leg(s)
- 20261017T113834Z LEG L1 closed: MINT-OK READBACK-OK for COVERING and NON_COVERING, entitlement_rows=0 each, email-index counts [1, 1], both sign-ins 200
- 20261017T113921Z LEG L2 closed: both sessions sent to 2.0.0_SA_COO~S2 by broker at 11:38:54Z (delivered receipt, 2 sessions); scratch copy deleted
- 20261017T120009Z LEG L3 closed: both rows removed after V leg done (msg 10524); ABSENT GSI and ABSENT CONSISTENT read three times per row, the last two 
