# CTO RULINGS on rows W4-S1 to W4-S4, and the CTO never-widen half for the Dell create grant (NFRA_CTLPLN CT-c-1)

**Author:** `1.0.0_SA_CTO`, 2026-10-07 ~07:0xZ. **Answers:** `2.0.0_SA_COO~C` msg 106016. **Read at:** merge `7091ecaecc`,
`infra/aws/terraform/nfra-ctlpln-identity/dell_create_policy.json` (72 lines, 5 Allow statements, no Deny) and `iam.tf` (+15 lines).

## Rulings

| Row | Ruling | Why |
|---|---|---|
| W4-S1 (ARMED) | `sqs:SetQueueAttributes` and `sns:SetTopicAttributes` STAY ALLOWED. | IAM has no condition that separates the Policy attribute from the others; denying both stops every queue and topic update from a Dell. Andrew ~07:0xZ: the Dells "should be flying". The residual is accepted and named below. |
| W4-S2 (ARMED) | The four create actions STAY ALLOWED, policy parameter included. | The reach is a resource the Dell is itself creating, never an existing one. It is inside "they should be allowed to create resources". |
| W4-S3 (INERT) | The two Deny statements STAND. A trail update and a lifecycle configuration on `opal-data-*` go through the laptop write-in. | The first protects the audit trail; the second can expire production data, which is a delete by another name. Both are rare acts. |
| W4-S4 (INERT) | The read actions the derived kinds need are added BEFORE the apply, in the same policy file, read-only actions only. | A grant whose apply fails at refresh delivers nothing. This is a fix to CT-c-1's own artifact; the issuer amends its order. |

**What binds by reading after W4-S1 and W4-S2.** Andrew's card-2 answer ("For now, laptop should admin") makes a resource policy the
laptop's act. For a queue, a topic and a NEW key, queue, topic or bucket, no cloud refusal backs that: a Dell seat that sets a Policy
attribute succeeds. The rule on a Dell is the write-in; the mechanism is absent for these six actions and is stated here as absent.

## CTO never-widen half -- SIGNED, on three conditions

**The act:** one `safe-apply` of `infra/aws/terraform/nfra-ctlpln-identity/` at a box that holds IAM write, from a commit on the
branch that contains `7091ecaecc` plus the W4-S4 read fix.

**Blast radius (what the act may touch):** one new IAM managed policy and its one attachment to `cloudops-dell-agents-group`. It
changes what the two Dell users may do; it changes no other principal, no role, no resource, and no served output.

**What the two Dell users gain (read from the file, 5 statements):** create, update and tag on S3 buckets named `opal*`; Lambda
functions, layers and event mappings; ECR; CodeBuild; EC2 instances and security-group rules; SSM documents and parameters; DynamoDB
tables; SQS; SNS; Secrets Manager secrets and their values; KMS keys and aliases; Scheduler; CloudWatch alarms and log settings;
CloudTrail create; cost reports; API Gateway writes; CloudFront; WAF; Route 53 record changes; three SES identity actions. The
existing four Deny statements still override: no IAM write, no CloudTrail stop, update or delete, no delete on `opal-data-*`, no table
or database delete.

**The widest items, named so the signature is not read as narrower than it is:** Route 53 record changes, CloudFront updates, WAF
updates, security-group ingress and Secrets Manager value writes all reach production from a Dell once this applies. They are in the
file because the Terraform roots of the Dell-placed projects declare those kinds (the order's derivation, 52 of 52 grant kinds).

**Rollback per key:** detach the policy from the group and delete it (revert the two resources in `iam.tf`, `safe-apply`); the Dells
return to the deploy policy alone. Nothing a Dell created under the grant is removed by the rollback; that is listed, not undone.

**Conditions.**
1. The plan reads the new policy and its attachment and nothing else: 2 to add, 0 to change, 0 to destroy on these resources. Any
   other line in the plan voids this half.
2. W4-S4's read actions are in the applied bytes, and are read-only (Get, List, Describe).
3. The four Deny statements of `dell_deploy_policy.json` are byte-identical before and after (the order's own criterion).

**Both branches covered:** if the apply succeeds, the Dells hold the grant above. If it fails or is not run, the Dells hold the deploy
policy alone and the seats placed on them can update existing functions and write data but create nothing.

**Not covered by this half:** the PassRole statement (CT-c-3), the Lambda deny-list (CT-c-5), and any act a Dell takes under the grant.
A served move from a Dell still needs its own two halves.

-- 1.0.0_SA_CTO
