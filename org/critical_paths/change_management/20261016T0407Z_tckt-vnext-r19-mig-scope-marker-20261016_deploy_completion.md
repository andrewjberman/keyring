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
| M1 | verify | opal-users-v2 internal PROFILE selection read: 19 selected, 3 with allowedFirmIds, 1 not active, of 23 | counts printed equal to the pair | r19_mig_apply.py select/apply 04:0xZ: counts {selected 19, with_list_attr 3, not_active 1, internal 23} equal the pair; ScannedCount 86; 0 selected rows already marked | CLOSED 20261016T041245Z |
| M2 | activation | 19 conditional update-items setting scope_all_firms BOOL true | rows_written 19, failed_conditions 0 | 19 update-items, 19 written, 0 failed conditions (R19_MIG_RESULT.json rows_written=19, failed_conditions=[]) | CLOSED 20261016T041245Z |
| M3 | verify | ConsistentRead read-back of every written row | marker BOOL true and hash of all other attributes unchanged, 19 of 19 | ConsistentRead get-item of 19 of 19: scope_all_firms BOOL true, sha256 of all other attributes equal to the before-hash, readback_bad=0 | CLOSED 20261016T041245Z |
| M4 | verify | r19_mig_check.py against the live table and R19_MIG_RESULT.json | MIG-OK line |  | OPEN |

## Log

- 20261016T040724Z OPENED by 0.7.0_AE_CloudOps~TV2 with 4 leg(s)
- 20261016T041245Z LEG M1 closed: r19_mig_apply.py select/apply 04:0xZ: counts {selected 19, with_list_attr 3, not_active 1, internal 23} equal the pair; 
- 20261016T041245Z LEG M2 closed: 19 update-items, 19 written, 0 failed conditions (R19_MIG_RESULT.json rows_written=19, failed_conditions=[])
- 20261016T041245Z LEG M3 closed: ConsistentRead get-item of 19 of 19: scope_all_firms BOOL true, sha256 of all other attributes equal to the before-hash,
