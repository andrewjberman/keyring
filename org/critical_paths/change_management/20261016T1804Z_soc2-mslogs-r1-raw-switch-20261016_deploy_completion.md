# Deploy Completion Record
**Date opened:** 2026-10-16T18:04:29.759766+00:00
**Status:** OPEN
**Deploy:** SOC2_MSLOGS round 1: in-place switch of the collector and door to raw bronze
**Authored by:** 0.7.0_AE_CloudOps~SOC21
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 7.49h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1-apply | activation | trino root: safe-apply in-place update of collector + door code, door role policy, door env | apply receipt + plan summary | safe-apply rc=0 Apply complete 0 added 15 changed 0 destroyed at 2026-10-16T18:23:40Z; access.tf ade21bee08 | CLOSED 20261016T182437Z |
| L2-subscription | activation | Management API: start the four feeds incl. Audit.AzureActiveDirectory | HTTP statuses of the four starts | start HTTP: Audit.AzureActiveDirectory 200, Exchange 400, SharePoint 400, General 400 (the three already enabled; body not read); s1_check_r1.py subs R1-SUBS-OK all four listed | CLOSED 20261016T182634Z |
| L3-switch-readback | verify | s1_check_r1.py applied/subs/switch + r2_check_r1.py plan | check lines read |  | OPEN |
| L4-redeploy-7b | activation | trino root: safe-apply the repaired collector code hash alone (item 7b, repair 6cef75fd39) | plan summary + apply receipt + new switch_at.txt | safe-apply rc=0 Apply complete 0 added 1 changed 0 destroyed; collector LastModified 2026-10-16T23:10:36Z CodeSha256 ZWVtuj7Q... equals planned hash; switch_at.txt reset | CLOSED 20261016T231109Z |
| L5-fires-7b | verify | two scheduled collector fires after the new switch_at.txt: counts, duration, no timeout | per-fire counts line, duration, REPORT timeout status |  | OPEN |
| L6-door-memory-7c | activation | trino root: safe-apply aws_lambda_function.access memory_size 1024->6144, timeout 300->600 (item 7c, door OutOfMemory in derive_silver) | plan summary + apply receipt + deployed memory/timeout read | safe-apply rc=0 0 added 3 changed 0 destroyed 2026-10-17T00:07:06Z; door MemorySize 6144 Timeout 600; aliases collector+member on v3; s1_check_r1.py applied R1-APPLIED-OK | CLOSED 20261017T000755Z |
| L7-door-10240-7e | activation | trino root: safe-apply aws_lambda_function.access memory_size 6144->10240, timeout stays 600 (item 7e, Andrew-direct via issuer) | plan summary + apply receipt + deployed memory read + s1_check_r1.py applied | safe-apply rc=0 0 added 3 changed 0 destroyed; door LastModified 2026-10-17T00:59:35Z MemorySize 10240 Timeout 600; aliases collector+member on v4; s1_check_r1.py applied R1-APPLIED-OK | CLOSED 20261017T010008Z |

## Log

- 20261016T180429Z OPENED by 0.7.0_AE_CloudOps~SOC21 with 3 leg(s)
- 20261016T182437Z LEG L1-apply closed: safe-apply rc=0 Apply complete 0 added 15 changed 0 destroyed at 2026-10-16T18:23:40Z; access.tf ade21bee08
- 20261016T182634Z LEG L2-subscription closed: start HTTP: Audit.AzureActiveDirectory 200, Exchange 400, SharePoint 400, General 400 (the three already enabled; body n
- 20261016T230837Z LEGS L4-redeploy-7b, L5-fires-7b added by 0.7.0_AE_CloudOps~SOC21 (TO-SM-r1 item 7b, fire 4 timeout repair)
- 20261016T231109Z LEG L4-redeploy-7b closed: safe-apply rc=0 Apply complete 0 added 1 changed 0 destroyed; collector LastModified 2026-10-16T23:10:36Z CodeSha256 ZWV
- 20261016T234209Z WINDOW extended 4.0h -> 7.49h (to 2026-10-17T01:30Z) per 2.0.0_SA_COO~S1: code repair redeployed 2026-10-16T23:10:36Z (item 7b); two scheduled fires 23:31Z and 00:31Z are the acceptance; close after item 8 reads
- 20261017T000458Z LEG L6-door-memory-7c added by 0.7.0_AE_CloudOps~SOC21 (TO-SM-r1 item 7c)
- 20261017T000755Z LEG L6-door-memory-7c closed: safe-apply rc=0 0 added 3 changed 0 destroyed 2026-10-17T00:07:06Z; door MemorySize 6144 Timeout 600; aliases collector+
- 20261017T005713Z LEG L7-door-10240-7e added by 0.7.0_AE_CloudOps~SOC21 (TO-SM-r1 item 7e)
- 20261017T010008Z LEG L7-door-10240-7e closed: safe-apply rc=0 0 added 3 changed 0 destroyed; door LastModified 2026-10-17T00:59:35Z MemorySize 10240 Timeout 600; alia
