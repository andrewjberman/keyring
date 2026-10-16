# Deploy Completion Record
**Date opened:** 2026-10-16T04:07:24.786847+00:00
**Status:** OPEN
**Deploy:** TCKT_VNEXT TO-R19-MIG: scope_all_firms = BOOL true on the 19 active internal PROFILE rows of opal-users-v2 with no allowedFirmIds (one conditional update-item per row, no address read; pair blob ee84f96d70, order blob 558473dce2f9, check blob 24286f537272); the release is NOT part of this act
**Authored by:** 0.7.0_AE_CloudOps~TV2
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| M1 | verify | opal-users-v2 internal PROFILE selection read: 19 selected, 3 with allowedFirmIds, 1 not active, of 23 | counts printed equal to the pair |  | OPEN |
| M2 | activation | 19 conditional update-items setting scope_all_firms BOOL true | rows_written 19, failed_conditions 0 |  | OPEN |
| M3 | verify | ConsistentRead read-back of every written row | marker BOOL true and hash of all other attributes unchanged, 19 of 19 |  | OPEN |
| M4 | verify | r19_mig_check.py against the live table and R19_MIG_RESULT.json | MIG-OK line |  | OPEN |

## Log

- 20261016T040724Z OPENED by 0.7.0_AE_CloudOps~TV2 with 4 leg(s)
