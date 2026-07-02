# 0.7.0_AE_CloudOps -- NFRA_AGENTBUS.S2: SQS transport + IAM/KMS partition (control-1, sim-only)

**archetype:** DEPLOY
**secondary_archetypes:** IMPLEMENT, VALIDATE

**Window:** 2026-07-02 ~18:55Z (COO~B GO) -> ~19:32Z. **Lane:** 0.7.0_AE_CloudOps (base).
**TO:** NFRA_AGENTBUS.S2 (issued 2.0.0_SA_COO~B). **Status:** COMPLETE + RAVC-ACCEPTED (COO~B 193153Z).

## Summary
Built + proved control-1 (the IAM/KMS/SQS partition) of the S1 5-control cross-principal security
model, in a SINGLE-TENANT SIMULATION. New Terraform module, safe-applied 0-diff, and the partition
proven fail-closed on LIVE state (real bidirectional AccessDenied via sts assume-role). First
NFRA_AGENTBUS leg to ship.

## What shipped (commit e29940a74, tag nfra-agentbus-v1.0.0)
New module `infra/aws/terraform/nfra-agentbus/` (state key `nfra-agentbus/tfstate`), 6 files, built to
the binding S1 spec (`docs/briefs/nfra_agentbus_s1_security_model_spec_DRAFT_20260702.md`, arch-gate
PASS 5b7ef1613). 10 resources, safe-apply 0-diff:
- 2 FIFO SQS queues (queue-pair): `agentbus-sim01-alpha-to-beta.fifo` (beta's inbound),
  `agentbus-sim01-beta-to-alpha.fifo` (alpha's inbound). SSE-KMS + message-group scoping.
- per-collaboration KMS key + alias `alias/agentbus-sim01` (rotation on); kms:Decrypt/GenerateDataKey
  scoped to the 2 fleet roles + root.
- 2 simulated fleet roles (`agentbus-sim01-fleet-{alpha,beta}-role`), same-account assumable
  (trust = account root), least-privilege identity policies: SEND to the pair + RECEIVE own-inbound ONLY.
- default-deny + explicit two-principal-allow queue policies (model the cross-principal gate).
- `simulated=true` var with a validation guard blocking a live-activation flip (AB-ACTIVATE stays fenced).

## Control-1 proof (LIVE, not TF-desired -- the acceptance bar, AC2/PRD SS6.1)
Via `aws sts assume-role` into each sim fleet, live SQS ops:
| Step | Op | Expect | Got |
|---|---|---|---|
| A1 | alpha SEND -> beta-inbound | ALLOW | ALLOW (kms:GenerateDataKey exercised) |
| B1 | beta SEND -> alpha-inbound | ALLOW | ALLOW |
| B2 | beta RECEIVE own-inbound | ALLOW + msg | ALLOW, got "hello-from-alpha" (kms:Decrypt exercised) |
| A2 | alpha RECEIVE own-inbound | ALLOW + msg | ALLOW, got "hello-from-beta" |
| **B3** | **beta RECEIVE alpha-inbound (CROSS)** | **DENY** | **AccessDenied (no identity-based policy allows sqs:receivemessage)** |
| **A3** | **alpha RECEIVE beta-inbound (CROSS)** | **DENY** | **AccessDenied** |
Partition provably-scoped, both directions. A cross-partition read succeeding would have been STOP-class; none.
KMS partition proven by the round-trip (send-encrypt + receive-decrypt worked ONLY under the scoped roles).

## Compiler Tools
| Tool | `<run>` (mandate phase) | Result |
|---|---|---|
| `comp-to NFRA_AGENTBUS.S2` | set race-free TO context | PASS |
| S1 spec read + `git cat-file 5b7ef1613` | phase-1: S1 arch-gate PASS confirmed before building | PASS (S1 COMPLETE) |
| `aws sqs/iam list` (baseline) | phase-1: confirm no existing agentbus resources | PASS (clean, net-new) |
| `.tools/safe-apply.sh -chdir=... apply` | phase-2: Rule-18 HALT-gated apply (never bare) | PASS (HALT-gate cleared; 10 add/0/0) |
| `terraform plan` (re-plan) | phase-2: 0-diff verification | PASS ("No changes") |
| `comp-iam gaps` | phase-2: no new permission gap after iam.tf | PASS (0 new gap; 3 missing/208 deny-present all pre-existing/unrelated -- bd cot-deny intentional, SES unmodeled) |
| `aws sts assume-role` + `sqs receive-message` | phase-3: LIVE deny-test own-ALLOW/cross-DENY | PASS both directions (real AccessDenied) |
| `aws cloudwatch list-metrics AWS/SQS` | phase-3: metering present per queue-pair (SS4.1) | PASS (Sent/Received/Deleted + ApproximateAgeOfOldestMessage +more) |
| `.tools/safe-commit.sh` | scoped module + inventory commits | PASS (surface-check OK) |

**What worked:** constructed-ARN locals broke the policy dependency cycle cleanly; the assume-role live
deny-test is unambiguous ground truth (real AccessDenied, not a TF-desired inference). **What failed:**
nothing. **Gap found:** none new.

## Governance fence (honored exactly)
SINGLE-TENANT SIMULATION only: both fleets = same-account assumable IAM roles under our own principal;
`simulated=true` var-guarded; NO cross-principal activation (that is the FENCED AB-ACTIVATE Directive
item, not this TO). All AWS via safe-apply (Terraform only). No live cross-principal message crossed.

## Blockers
None. S2 COMPLETE + RAVC-ACCEPTED by COO~B.

## Current State (handoff)
- Module `infra/aws/terraform/nfra-agentbus/` LIVE @ e29940a74 / tag nfra-agentbus-v1.0.0. State key
  `nfra-agentbus/tfstate`. 10 resources applied 0-diff. Queues PURGED (clean slate).
- Resources PERSIST for NFRA_AGENTBUS-S4 (CVO) independent re-verification -- my live deny-test is what
  S4 re-runs. Outputs (queue urls/arns, role arns, KMS arn) exported for the S3 broker adapter (separate lane).
- Core doc `pipeline_inventory.xml` updated with the nfra_agentbus section.
- AGENTBUS arch-gate authority = 1.0.0_SA_CTO~B (Andrew re-scope: base CTO = ETL-only). S2 arch-gate #1
  + open S1 Q4 (collaboration lifecycle: who creates/tears-down a queue-pair+key+grants) routed to CTO~B.

## Next Steps
- **[1.0.0_SA_CTO~B]** arch-gate #1 verdict on control-1; home the S1 Q4 collaboration-lifecycle/consent gate.
- **[3.x_CVO / S4]** independent live re-verify of the persisted partition (spawns when the S2/S3/S4 batch is ready).
- **[0.7.0_AE_CloudOps]** IDLE:available for the next Andrew-direct cloud-ops slice or S3-adjacent work if base COO routes it.
- **[follow-up]** initialize CHANGELOG.json for nfra-agentbus via record-terraform-deploy (Known-Issue #5, non-urgent).
