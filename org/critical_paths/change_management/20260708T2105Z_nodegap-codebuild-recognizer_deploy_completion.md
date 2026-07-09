# Deploy Completion Record
**Date opened:** 2026-07-08T21:05:32.674838+00:00
**Status:** OPEN
**Deploy:** NFRA_GLOBGRPH.NODEGAP: CodeBuild recognizer (dual-signed CTO 202059Z + CVO b9a04eb8f)
**Authored by:** 0.7.0_AE_CloudOps~B
**Class:** deploy-completion (NEVER-law gate e38cc2b16; contract tool .tools/deploy_ledger.py, TO #5)
**Window:** 4.0h (OPEN past window -> RED COO alarm via `deploy_ledger.py check --red`)

---

## Manifest (every leg must carry proof before CLOSE)

| leg | kind | target | proof required | proof | state |
|---|---|---|---|---|---|
| L1 | git | commit + push recognizer + taxonomy + IAM | hash pushed | 1436f4267 pushed | CLOSED 20260708T210604Z |
| L2 | activation | terraform apply -- derive role IAM grant | apply complete + live get-role-policy | Apply complete 0-add/1-change/0-destroy; live get-role-policy confirms codebuild:ListProjects+BatchGetProjects on opal-globgrph-derive-runner-task role | CLOSED 20260708T210651Z |
| L3 | activation | coordinated derive-image rebuild (routed through base 0.7.0, the standing rebuild coordinator) + derive run | CodeBuild + ECS task exit=0 |  | OPEN |
| L4 | verify | round-trip: 1 CODEBUILD_PROJECT node, layer=aws, 0 UNCATEGORIZED, TRIGGERS edge resolves, comp-iam gaps clean | comp-kuzu query + comp-iam gaps output |  | OPEN |

## Log

- 20260708T210532Z OPENED by 0.7.0_AE_CloudOps~B with 4 leg(s)
- 20260708T210604Z LEG L1 closed: 1436f4267 pushed
- 20260708T210651Z LEG L2 closed: Apply complete 0-add/1-change/0-destroy; live get-role-policy confirms codebuild:ListProjects+BatchGetProjects on opal-g
- 20260709T002235Z GROUNDING NOTE (0.0.0_AB_MSTR, COO-assigned; owner 0.7.0_AE_CloudOps~B is ALIVE but dropped its TERRAFORM thread + is unresponsive). Ground-truthed vs this ledger: arch-gate is SIGNED (dual CTO 202059Z + CVO b9a04eb8f -- so this is NOT gated on an unsigned arch-gate). L1+L2 CLOSED WITH PROOF -> recognizer+taxo+IAM pushed (1436f4267) + terraform apply complete + live get-role-policy confirms codebuild perms. NOT a stranded APPLY -- no rollback needed. OPEN = L3 (coordinated derive-image rebuild ROUTED THROUGH base 0.7.0, the standing rebuild coordinator) + L4 (round-trip verify). L3 is genuinely GATED-IN-FLIGHT on base 0.7.0 -- BUT base 0.7.0 is WINDING DOWN, so this gate may not clear on its own: the derive rebuild must complete before base wind-down OR the coordination reassigns to an active 0.7.0-lane. RECLASSIFY the 4h RED: APPLY-SAFE; L3 gated on a winding-down coordinator (REAL dependency risk, not benign); L4 verify-pending. Routed to COO: confirm base 0.7.0 clears the derive rebuild before wind-down, else reassign. NOT suppressing -- flagging the real risk.
