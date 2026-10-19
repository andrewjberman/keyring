# Deploy Completion Record
**Date opened:** 2026-10-17T14:43:53.725325+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261017T145527Z
**Deploy:** AMGT_RESAPP bq-2: PROD promote of amgt-sa-changed-list-value + amgt-sa-money-display (Security Analysis, Opal-internal)
**Authored by:** 0.4.0_DT_ClientPlatform~H2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | portal PROD push of the release branch | PROD head hash, ls-remote read | PROD 15bc21b3 -> 99d2b2a70cc1b5d39705d89a38312a4b8f7c3fa7; ls-remote read refs/heads/PROD = 99d2b2a70cc1b5d39705d89a38312a4b8f7c3fa7 | CLOSED 20261017T144723Z |
| L2 | verify | CI deploy workflow on the PROD head | conclusion success read by headSha | gh run 39042189942 Deploy to Production completed success on headSha 99d2b2a70cc1b5d39705d89a38312a4b8f7c3fa7 (only workflow for that sha); tag portal-v2.1.235 peels to it | CLOSED 20261017T145527Z |
| L3 | verify | PROMOTE_RECEIPT_BQ2.md written and AC1-AC3 read | receipt path and AC outputs | receipt 509558f20c PROMOTE_RECEIPT_BQ2.md; AC1 16 EQUAL 0 DIFFERS; AC2 completed success 99d2b2a7; AC3 count 6 (bar 4) | CLOSED 20261017T145527Z |

## Log

- 20261017T144353Z OPENED by 0.4.0_DT_ClientPlatform~H2 with 3 leg(s)
- 20261017T144723Z LEG L1 closed: PROD 15bc21b3 -> 99d2b2a70cc1b5d39705d89a38312a4b8f7c3fa7; ls-remote read refs/heads/PROD = 99d2b2a70cc1b5d39705d89a3831
- 20261017T145527Z LEG L2 closed: gh run 39042189942 Deploy to Production completed success on headSha 99d2b2a70cc1b5d39705d89a38312a4b8f7c3fa7 (only work
- 20261017T145527Z LEG L3 closed: receipt 509558f20c PROMOTE_RECEIPT_BQ2.md; AC1 16 EQUAL 0 DIFFERS; AC2 completed success 99d2b2a7; AC3 count 6 (bar 4)
- 20261017T145527Z CLOSED -- all 3 legs proven
