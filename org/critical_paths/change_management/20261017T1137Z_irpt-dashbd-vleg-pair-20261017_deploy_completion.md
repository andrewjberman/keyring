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
| L1 | activation | mint the COVERING and NON_COVERING rows once each in opal-users-v2 | MINT-OK READBACK-OK for both plus email-index count 1 each |  | OPEN |
| L2 | verify | hand both sessions to 2.0.0_SA_COO~S2 by broker | broker delivery receipt, 2 sessions |  | OPEN |
| L3 | verify | remove both rows after the issuer word V leg done | ABSENT GSI and ABSENT CONSISTENT read twice per row |  | OPEN |

## Log

- 20261017T113712Z OPENED by 0.7.0_AE_CloudOps~IB2 with 3 leg(s)
