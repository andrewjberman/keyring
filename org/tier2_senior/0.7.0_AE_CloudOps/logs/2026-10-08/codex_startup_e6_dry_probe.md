# Exact-seat startup and E6 dry probe - 0.7.0_AE_CloudOps

**archetype:** VALIDATE
**Date:** 2026-10-08, approximately 4:05-4:15 PM Eastern
**Task Orders:** IRPT_BCKEND.TO-APPLY-E6; NFRA_CTLPLN.TO-APPLY-18; GRAPH_OVERLAY.TO-APPLY-1
**Status:** Dry probe COMPLETE; applies BLOCKED on a repository defect.
**Push state:** LOCAL; origin CLOUD a8689cb2595050a7c40427160113abd8fd5e4e8c, measured by git ls-remote. No push.

## Objective

Initialize the launcher-supplied exact Codex seat and handle the nine unread carriers in COO 107198 priority order.

## Deployment Sequence

| Step | Action | Result |
|---|---|---|
| 1 | codex-seat-load.py and identity check | Exact serial 0.7.0_AE_CloudOps; OPAL_AGENT_SERIAL matches |
| 2 | Required contracts and ordered role files | Read; Codex runtime and shared-branch law supersede older Claude/push instructions |
| 3 | codex-seat-status.ps1 | GREEN, all nine checks; one heartbeat, bridge and detector |
| 4 | Exact inbox files | Nine read and content-ACKed; current priority E6 0-1, D2 A, graph overlay; later legs still gated |
| 5 | E6 leg 0 caller/schema read | Andrew_Berman in account 313476888478; tenant HASH and request_revision RANGE, both strings |
| 6 | E6 conditional dry probe | Expected ConditionalCheckFailedException, CLI exit 255; no row deleted |
| 7 | Terraform preflight | Missing required infra/aws/TERRAFORM_PIPELINE_STRATEGY.md, named in seat README Mandatory Reading |
| 8 | Report and relay | Result file to MSTR for dell2 relay; repository defect to COO~C and CTO; overlay STOP copied to CRO |
| 9 | Infrastructure apply | None. No IAM changes, patch application, image push, digest pins, task revisions, or pointer changes |

## Verification

Exact result: `An error occurred (ConditionalCheckFailedException) when calling the DeleteItem operation: The conditional request failed`.
Evidence: `deliverables/irpt_e6_20261008/LEG0_RESULT.md`, `leg0-key.json`, and `leg0-response.txt`.
The graph worker is Terraform-owned: `infra/aws/terraform/globgrph/projection.tf:212`, resource `aws_ecs_task_definition.projection_worker`. Its order therefore requires safe-apply and encounters the same missing-guide prerequisite.

## Compiler Tools

| Tool | Result |
|---|---|
| comp-which | Used before inspections. Startup exact-file query and graph Terraform-root query returned NO FIT; permitted direct reads/search used. Cloud-ops discovery fallback timed out at its 90-second budget. |
| comp-iam service irpt-ycharts-generate | Resolved generate role and 17 existing statements; does not substitute for live exact-resource proof. |
| sequence-check.py --project IRPT_BCKEND | PLACED at stage 4, EXECUTING, no unmet gate; local COO lane dark is a placement note. Explicit laptop carrier from COO~C governs these legs. |
| comp-diff | Run before evidence commit; stale graph detected and rebuilding. Final result recorded by command output. |

**What worked:** canonical loader/readiness oracle; exact-file message reads; live DynamoDB conditional rejection as the dry-probe oracle.
**What failed:** mandatory Terraform guide read: path not found; compiler cloud-ops discovery timeout.
**Gap found:** seat README references an absent mandatory guide. Repository-closed instructions prohibit inventing a replacement procedure.

## Current State

E6 leg 0 is done and enables leg 1 conditionally, but leg 1 has not been applied. D2 A and the graph overlay have not deployed. All nine original carriers were moved to read only after ACK and their required first handling (probe, gate retention, priority adoption or preflight STOP/report). Task-order statuses remain with the issuer.

## Next Steps

1. [1.0.0_SA_CTO / 2.0.0_SA_COO~C] Repair or authoritatively correct the mandatory Terraform guide reference.
2. [0.7.0_AE_CloudOps] Resume E6 leg 1, then D2 leg A, then graph overlay using their existing GOs and exact plan/digest conditions once prerequisite is resolved.
3. E6 leg 2 remains held for dell2 keys file and COO GO; Andrew's one-object approval is recorded. D2 B waits for COO GO on send (1); D2 C follows X1 or its deadline if opened. No second monitor or cron was launched.