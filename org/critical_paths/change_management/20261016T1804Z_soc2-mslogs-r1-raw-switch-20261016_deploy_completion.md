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
| L1-apply | activation | trino root: safe-apply in-place update of collector + door code, door role policy, door env | apply receipt + plan summary | safe-apply rc=0 Apply complete 0 added 15 changed 0 destroyed at 2026-10-16T18:23:40Z; access.tf ade21bee08 | CLOSED 20261016T182437Z |
| L2-subscription | activation | Management API: start the four feeds incl. Audit.AzureActiveDirectory | HTTP statuses of the four starts | start HTTP: Audit.AzureActiveDirectory 200, Exchange 400, SharePoint 400, General 400 (the three already enabled; body not read); s1_check_r1.py subs R1-SUBS-OK all four listed | CLOSED 20261016T182634Z |
| L3-switch-readback | verify | s1_check_r1.py applied/subs/switch + r2_check_r1.py plan | check lines read |  | OPEN |
| L4-redeploy-7b | activation | trino root: safe-apply the repaired collector code hash alone (item 7b, repair 6cef75fd39) | plan summary + apply receipt + new switch_at.txt | safe-apply rc=0 Apply complete 0 added 1 changed 0 destroyed; collector LastModified 2026-10-16T23:10:36Z CodeSha256 ZWVtuj7Q... equals planned hash; switch_at.txt reset | CLOSED 20261016T231109Z |
| L5-fires-7b | verify | two scheduled collector fires after the new switch_at.txt: counts, duration, no timeout | per-fire counts line, duration, REPORT timeout status |  | OPEN |

## Log

- 20261016T180429Z OPENED by 0.7.0_AE_CloudOps~SOC21 with 3 leg(s)
- 20261016T182437Z LEG L1-apply closed: safe-apply rc=0 Apply complete 0 added 15 changed 0 destroyed at 2026-10-16T18:23:40Z; access.tf ade21bee08
- 20261016T182634Z LEG L2-subscription closed: start HTTP: Audit.AzureActiveDirectory 200, Exchange 400, SharePoint 400, General 400 (the three already enabled; body n
- 20261016T230837Z LEGS L4-redeploy-7b, L5-fires-7b added by 0.7.0_AE_CloudOps~SOC21 (TO-SM-r1 item 7b, fire 4 timeout repair)
- 20261016T231109Z LEG L4-redeploy-7b closed: safe-apply rc=0 Apply complete 0 added 1 changed 0 destroyed; collector LastModified 2026-10-16T23:10:36Z CodeSha256 ZWV
