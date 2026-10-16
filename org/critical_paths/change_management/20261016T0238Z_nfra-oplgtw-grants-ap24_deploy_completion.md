# Deploy Completion Record
**Date opened:** 2026-10-16T02:38:59.297797+00:00
**Status:** CLOSED -- nothing stranded -- closed 20261016T030053Z
**Deploy:** NFRA_OPLGTW TO-OG-ap-24 Phase B: six client vendor read roles (6 roles + 6 inline policies, 12 adds, 0 change, 0 destroy), applied ONE role at a time via safe-apply, targeted, each read back from IAM; .tf sha256-16 21a54e8f197eeea2; three halves signed (CTO 1ef958e44b, COO 947810faa8, CVO 5b66771763); GO msg 34663
**Authored by:** 0.7.0_AE_CloudOps~ZS
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 6.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| R1 | verify | inf-orion role+policy apply then get-role and get-role-policy | policy document equal to the plan | safe-apply targeted 2 added 0 changed 0 destroyed; iam get-role: trust Principal opal-gateway-role only, Action sts:AssumeRole, no Condition, 1 statement; list-role-policies 1 inline, 0 attached; targeted replan No changes (live policy equals config); role gateway-inf-orion-read-role | CLOSED 20261016T030017Z |
| R2 | verify | inf-eclipse role+policy apply then get-role and get-role-policy | policy document equal to the plan | safe-apply targeted 2 added 0 changed 0 destroyed; iam get-role: trust Principal opal-gateway-role only, Action sts:AssumeRole, no Condition, 1 statement; list-role-policies 1 inline, 0 attached; targeted replan No changes (live policy equals config); role gateway-inf-eclipse-read-role | CLOSED 20261016T030017Z |
| R3 | verify | 49f-blackdiamond role+policy apply then get-role and get-role-policy | policy document equal to the plan | safe-apply targeted 2 added 0 changed 0 destroyed; iam get-role: trust Principal opal-gateway-role only, Action sts:AssumeRole, no Condition, 1 statement; list-role-policies 1 inline, 0 attached; targeted replan No changes (live policy equals config); role gateway-49f-blackdiamond-read-role | CLOSED 20261016T030017Z |
| R4 | verify | cot-commonwealth role+policy apply then get-role and get-role-policy | policy document equal to the plan | safe-apply targeted 2 added 0 changed 0 destroyed; iam get-role: trust Principal opal-gateway-role only, Action sts:AssumeRole, no Condition, 1 statement; list-role-policies 1 inline, 0 attached; targeted replan No changes (live policy equals config); role gateway-cot-commonwealth-read-role | CLOSED 20261016T030018Z |
| R5 | verify | cot-blackdiamond role+policy apply then get-role and get-role-policy | policy document equal to the plan | safe-apply targeted 2 added 0 changed 0 destroyed; iam get-role: trust Principal opal-gateway-role only, Action sts:AssumeRole, no Condition, 1 statement; list-role-policies 1 inline, 0 attached; targeted replan No changes (live policy equals config); role gateway-cot-blackdiamond-read-role | CLOSED 20261016T030018Z |
| R6 | verify | smartx role+policy apply then get-role and get-role-policy | policy document equal to the plan | safe-apply targeted 2 added 0 changed 0 destroyed; iam get-role: trust Principal opal-gateway-role only, Action sts:AssumeRole, no Condition, 1 statement; list-role-policies 1 inline, 0 attached; targeted replan No changes (live policy equals config); role gateway-smartx-read-role | CLOSED 20261016T030018Z |
| V1 | verify | targeted re-plan of the six pairs | No changes | terraform plan -lock=false, six role targets + six policy targets (12): No changes. Your infrastructure matches the configuration; each pair also read No changes after its own apply. Simulation per role (one resource per call): in-prefix GetObject allowed, other prefix explicitDeny, opal-data-bd explicitDeny, PutObject explicitDeny, 6 of 6 | CLOSED 20261016T030053Z |
| V2 | verify | live gateway-blackdiamond-read-role and gateway-schwab-read-role policy hashes | 4893211d4408180a and a3e8ca81172af8cc unchanged | policy sha256-16 (sort_keys, compact) re-read from IAM after the sixth apply: gateway-blackdiamond-read-policy 4893211d4408180a (want 4893211d4408180a), gateway-schwab-read-role-policy a3e8ca81172af8cc (want a3e8ca81172af8cc); W/GR_APPLIED.json written | CLOSED 20261016T030053Z |

## Log

- 20261016T023859Z OPENED by 0.7.0_AE_CloudOps~ZS with 8 leg(s)
- 20261016T030017Z LEG R1 closed: safe-apply targeted 2 added 0 changed 0 destroyed; iam get-role: trust Principal opal-gateway-role only, Action sts:Assu
- 20261016T030017Z LEG R2 closed: safe-apply targeted 2 added 0 changed 0 destroyed; iam get-role: trust Principal opal-gateway-role only, Action sts:Assu
- 20261016T030017Z LEG R3 closed: safe-apply targeted 2 added 0 changed 0 destroyed; iam get-role: trust Principal opal-gateway-role only, Action sts:Assu
- 20261016T030018Z LEG R4 closed: safe-apply targeted 2 added 0 changed 0 destroyed; iam get-role: trust Principal opal-gateway-role only, Action sts:Assu
- 20261016T030018Z LEG R5 closed: safe-apply targeted 2 added 0 changed 0 destroyed; iam get-role: trust Principal opal-gateway-role only, Action sts:Assu
- 20261016T030018Z LEG R6 closed: safe-apply targeted 2 added 0 changed 0 destroyed; iam get-role: trust Principal opal-gateway-role only, Action sts:Assu
- 20261016T030053Z LEG V1 closed: terraform plan -lock=false, six role targets + six policy targets (12): No changes. Your infrastructure matches the conf
- 20261016T030053Z LEG V2 closed: policy sha256-16 (sort_keys, compact) re-read from IAM after the sixth apply: gateway-blackdiamond-read-policy 4893211d4
- 20261016T030053Z CLOSED -- all 8 legs proven
