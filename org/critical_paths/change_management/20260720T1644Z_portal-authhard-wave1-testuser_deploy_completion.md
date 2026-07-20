# Deploy Completion Record
**Date opened:** 2026-07-20T16:44:21.788357+00:00
**Status:** CLOSED -- nothing stranded -- closed 20260720T164822Z
**Deploy:** PORTAL_AUTHHARD Wave-1 account-dependent EXERCISE test-user lifecycle (create -> exercise -> VERIFIED delete)
**Authored by:** 0.7.0_AE_CloudOps
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 1.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | verify | throwaway test user in opal-users-v2 VERIFIED-DELETED | post-delete GetItem returns no Item | test user authhard-wave1-test-1784565989@opal.test (PK USER#usr_test1784565989, firmId=authhard-test-firm-doesnotexist non-existent) created -> full trio exercised (WS1 counter-reset 401x4/200/401; WS2a disabled-refresh HTTP500+no-token, active 200; WS8 <12 reject/breached reject/passphrase accept; existing-sub-12 login 200) -> delete-item issued -> post-delete consistent-read GetItem returns NO Item. Atomic single-run + cleanup trap; user lifetime bounded to the run. | CLOSED 20260720T164821Z |

## Log

- 20260720T164421Z OPENED by 0.7.0_AE_CloudOps with 1 leg(s)
- 20260720T164821Z LEG L1 closed: test user authhard-wave1-test-1784565989@opal.test (PK USER#usr_test1784565989, firmId=authhard-test-firm-doesnotexist n
- 20260720T164822Z CLOSED -- all 1 legs proven
