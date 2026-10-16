# Deploy Completion Record
**Date opened:** 2026-10-16T18:04:29.759766+00:00
**Status:** OPEN
**Deploy:** SOC2_MSLOGS round 1: in-place switch of the collector and door to raw bronze
**Authored by:** 0.7.0_AE_CloudOps~SOC21
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1-apply | activation | trino root: safe-apply in-place update of collector + door code, door role policy, door env | apply receipt + plan summary |  | OPEN |
| L2-subscription | activation | Management API: start the four feeds incl. Audit.AzureActiveDirectory | HTTP statuses of the four starts |  | OPEN |
| L3-switch-readback | verify | s1_check_r1.py applied/subs/switch + r2_check_r1.py plan | check lines read |  | OPEN |

## Log

- 20261016T180429Z OPENED by 0.7.0_AE_CloudOps~SOC21 with 3 leg(s)
