# Deploy Completion Record
**Date opened:** 2026-07-08T21:05:32.674838+00:00
**Status:** OPEN -- honestly SCHEDULED-GATED (NOT stranded): L1/L2 proven; L3-rebuild DONE (fb953edc); L3-run rides the ~02:00Z nightly; L4 post-nightly (base 0.7.0). Reassigned off wedged ~B. See 20260709T0155Z disposition note.
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
- 20260709T0155Z DISPOSITION CORRECTION (0.7.0_AE_CloudOps base; base COO 015415Z ACCEPTED + independently Rule-22-verified). SUPERSEDES the 002235Z "winding-down coordinator / dependency-risk" concern on BOTH facts: (1) base 0.7.0 is NOT winding down; (2) the L3 derive-image REBUILD IS ALREADY DONE -- CodeBuild 2b39cc5e SUCCEEDED -> ECR opal-globgrph-derive-runner:latest = sha256:fb953edc06.. (tag 20260708-211342; base COO re-verified live). Recognizer baked-confirmed (CODEBUILD_PROJECT in derive_runner.py + live_codebuild_projects() in comp_aws_cli.py; built from origin/CLOUD where 1436f4267 is committed, so no future rebuild drops it). The L3 derive-RUN rides the ~02:00Z SCHEDULED NIGHTLY (Andrew no-on-demand-derive rule) -- a SCHEDULED-GATE, not a strand. L4 round-trip verify REASSIGNED to base 0.7.0 (COO~B 003501Z, since ~B is MSTR-confirmed WEDGED, telemetry 4.5h-dead). RECLASSIFY: this is NOT a stranded half-deploy -- APPLY-SAFE (L1/L2 proven) + L3-rebuild DONE (fb953edc) + L3-run scheduled-gated (nightly) + L4 base-0.7.0 post-nightly. CLOSES GREEN after the ~02:00Z nightly ingests the CODEBUILD_PROJECT node + base 0.7.0's round-trip verify. Do NOT reassign to the wedged ~B.
