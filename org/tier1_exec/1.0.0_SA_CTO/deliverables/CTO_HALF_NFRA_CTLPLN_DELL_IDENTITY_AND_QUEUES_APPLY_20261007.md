# CTO half -- NFRA_CTLPLN round 2: apply the Dell identities and the Dell inbound queues -- SIGNED

**Signer:** `1.0.0_SA_CTO`, 2026-10-07 ~04:2xZ. **For:** the site-Z CloudOps seat that applies, and its COO's half. **Authority:** Andrew-direct
~00:5xZ ("they should have deploy ability"), ~02:0xZ (Taildrop), ~04:2xZ ("Where is the Dell Keys? i want that issued"); PRD v0.6 signed by
`3.0.0_SA_CVO` (C-IDENTITY, C-BUS, FWD-10).

## The two acts (origin CLOUD 0ae63f9dbf)

1. `safe-apply` of `infra/aws/terraform/nfra-ctlpln-identity/` (CT-b-1, drained @002f93bacd; state key `nfra-ctlpln-identity/tfstate`).
2. `safe-apply` of `infra/aws/terraform/nfra-ctlpln-agentbus/` (CT-b-3, proof @2d01d40c9e; state key `nfra-ctlpln-agentbus/tfstate`).

## What I read (the roots themselves, at HEAD)

- **Identity root creates, and only creates:** group `cloudops-dell-agents-group`; users `cloudops-dell1-agent-user`, `cloudops-dell2-agent-user`;
  the group membership; policy `cloudops-dell-agent-deploy-policy` attached to the group; one bus policy per Dell attached to its user.
  **No `aws_iam_access_key` resource.** MEASURED before the act: none of these names exists (`NoSuchEntity` on both users and the group).
- **Deploy policy:**
  - allows S3 get/put/list on `opal-*`, six Lambda deploy actions, SQS send to the inbound queues, and read-only IAM/EC2/KMS for a plan;
  - DENIES every IAM write, CloudTrail writes, S3 deletes and lifecycle changes on `opal-data-*`, and table and database deletes.
  - `iam:PassRole` stays denied (ruling 105942).
- **Bus policies:** each Dell receives and deletes only on its own `agentbus-global-dellN-queue*`.
- **Queue root creates:** two FIFO queues, `agentbus-global-dell1-queue.fifo` and `agentbus-global-dell2-queue.fifo` (plan 2 add / 0 change / 0 destroy
  per the worker's proof). MEASURED before the act: no `agentbus-global*` queue exists.

## The half

- **Blast radius:** additive only. New IAM group, users, policies and attachments; two new queues. No existing identity, policy, queue, bucket or
  served output is changed or read by either apply. A plan that shows ANY change or destroy to an existing resource is outside this half: stop.
- **Writers:** N = 1 per root (its own state key; neither name exists anywhere else in the estate, measured above).
- **Both branches:** (A) the apply completes: the plan's adds exist, read back by name. (B) the apply stops part-way: re-run the same apply
  (idempotent adds) or `terraform destroy` on that root; nothing outside the root is touched either way.
- **Rollback:** `terraform destroy` of the root concerned. After keys exist, deactivate and delete the two access keys first.
- **The keys (not Terraform):** after act 1, one access key per Dell user, created at site Z, sent with `tailscale file cp <file> dell1:` /
  `dell2:`, the local copies deleted and read back gone. The key never enters git, state, the bus or a message. Andrew picks each up in person.
- **Acceptance:** `aws iam get-user` names both users; `aws iam simulate-principal-policy` for a Dell user reads allowed on an S3 put to an
  `opal-*` key and denied on `iam:CreateUser` and on an `opal-data-*` delete; both queues return a URL; the laptop reads the same.

**SIGNED.**

-- 1.0.0_SA_CTO
