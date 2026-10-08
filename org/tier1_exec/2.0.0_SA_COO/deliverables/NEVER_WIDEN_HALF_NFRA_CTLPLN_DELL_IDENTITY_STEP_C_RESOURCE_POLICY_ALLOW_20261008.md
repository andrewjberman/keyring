# COO never-widen half -- NFRA_CTLPLN: the Dell identity root, STEP C of three -- the Allow of resource-policy actions

**Author:** `2.0.0_SA_COO~C`, 2026-10-08 ~12:2xZ. **Read at:** trunk @203344e1b1. Root `infra/aws/terraform/nfra-ctlpln-identity/`.
**Counterpart owed:** a CTO half.
**Authority:** Andrew-direct 2026-10-08 ~00:4xZ, "lets start with lifting 1 2 3 6", item 3 of the list he answered being "Change
who may reach a resource: bucket policies, key policies, Lambda permissions, queue policies (an explicit deny of 75 actions)"
(record `org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261008_004xZ_LIFT_FOUR_DELL_LIMITS_SECRETS_FIRM_DATA_RESOURCE_POLICIES_PUSH.md`;
this seat read the record and did not hear the word); `1.0.0_SA_CTO` msg 106731 ruling 1 (the Allow, not only the Deny
removed); msg 106733 (the Secrets Manager actions out; four routes reported and allowed); msg 106781 (three routes out, by
explicit Deny); msg 106838 (the seven audit-bucket settings; the order Denies, plan 1, Allow).

## Where this step stands

| step | what | state |
|---|---|---|
| A | the Denies first; the public parameter read; self-simulate | APPLIED 2026-10-08T09:19:39Z (order TO-APPLY-12) |
| B | the secrets read of 66; the old Deny policy removed | APPLIED 2026-10-08T11:33:48Z (order TO-APPLY-11) |
| **C (this half)** | the Allow of 70 resource-policy actions and its attachment | this pair |

After step B the issuer's untargeted plan of the root with the default variable reads "No changes" (measured ~12:0xZ).

## The act

One `safe-apply` of the root with `-var apply_respol_allow=true` on BOTH the plan and the apply, at the laptop. It may be
untargeted: with steps A and B applied, the variable is the only difference between configuration and world.

## The plan, MEASURED

Laptop, 2026-10-08 ~12:1xZ, read-only, `-var apply_respol_allow=true`, exit 2: `Plan: 2 to add, 0 to change, 0 to destroy.`
100 added lines, zero removed.

- `aws_iam_policy.dell_agent_respol_allow[0]` created: ONE statement, `AllowResourcePolicyChanges`, Effect Allow, Resource `*`,
  70 actions (counted in the plan: 70). By service: s3 14, ec2 12, logs 5, ses 5, ecr 4, kms 4, lambda 4, sqs 3, ssm 3,
  cloudfront 2, codebuild 2, dynamodb 2, events 2, rds 2, route53 2, sns 2, wafv2 2. No `iam:`, no `secretsmanager:`, no
  `cloudtrail:` action is in the plan (grep: zero).
- `aws_iam_group_policy_attachment.dell_agent_respol_allow[0]` created: attaches it to the Dell agent group.

**Writers of the property: N = 1**, this root; read. The group then holds 6 managed policies of a quota of 10.

## Blast radius

Two principals, `cloudops-dell1-agent-user` and `cloudops-dell2-agent-user`, and so every agent seat on those two boxes.

**What they gain, at full width.** The ability to change WHO MAY REACH a resource, on any resource of these services in the
account that no explicit Deny protects: a bucket's policy and ACLs, a key's policy and grants, a function's or layer's
permissions, a queue's and a topic's policy, an image repository's policy, a log destination's and a resource policy on logs,
an event bus's policy, a mail identity's policy, a DNS and a firewall resource policy, a database snapshot's and a VPC
endpoint's sharing attributes. In plain terms: a Dell seat can then make a bucket public, share a key with another account,
let any principal invoke an unprotected function, or open a queue, wherever nothing below stops it.

**What is OUT, and why it holds** (each simulated for both users; the cell's run reads `freed_allowed=70/70 freed_excluded=5
undo_denied=181/181`):

| left out or denied | how | effect |
|---|---|---|
| every `iam:` action (1 of the 75) | not in the Allow; `DenyEveryIamWrite` also denies | a Dell cannot change a role's trust |
| `cloudtrail:PutResourcePolicy`, `DeleteResourcePolicy` (2) | not in the Allow; `DenyCloudTrailWrites` | the trail itself |
| `secretsmanager:PutResourcePolicy`, `DeleteResourcePolicy` (2) | not in the Allow (issuer's exclusion, CTO confirmed msg 106733) | a Dell cannot grant itself one of the 28 withheld platform keys through a secret's own policy |
| permission actions on the ten protected functions | explicit Deny, LIVE since step A | a Dell cannot let another principal invoke the portal's authorizers and auth handlers |
| 21 writes on the audit-trail log bucket | explicit Deny, LIVE since step A | a Dell cannot rewrite its policy or expire its logs |
| queue policy actions on the four agentbus queues | explicit Deny, LIVE since step A | receive-only-own-queue holds |

**What this Allow CAN undo, accepted by the CTO as inside what Andrew lifted (msg 106733), stated so it is signed with open
eyes.** By simulation, for both users, each reads ALLOWED after this step (an identity simulation does not include the
resource's own policy, which could still refuse):
1. **A firm fence.** `s3:PutBucketPolicy` on the 49 Financial, Cottonwood and Inflection data buckets. A Dell could rewrite
   the bucket policy that keeps one firm's principals out of another's data. (`s3:DeleteBucketPolicy` there is refused by an
   older Deny; a rewrite is not.)
2. **The Terraform state bucket's policy.** Rewrite and delete both read allowed.
3. **Any key's policy or grants**, including the key that encrypts `schwab/sdd/session`. A Dell could give itself decrypt on
   that key; it still could not read the secret, whose read is not granted and whose own policy it cannot write.
4. **The transcripts key's policy.** A Dell could widen itself past the decrypt-only grant applied on 2026-10-07.
5. **Object and bucket ACLs** on the shared assets bucket (`opal-data-assets`).

A Dell seat that uses any of these does so under its own box's never-widen pair and tells the laptop, per the CTO's ruling
on Andrew's 19:0xZ word; no tool enforces that today. The laptop's seat-gate checks are in WARN mode and do not grade a
resource-policy call made directly with the AWS command line.

**Not examined:** organization-level policies; the resource policies already on each of the resources above; whether any
Dell job in flight would behave differently once these calls stop being refused.

## Expected outcome, BOTH branches

- **A:** the plan with `-var apply_respol_allow=true` reads exactly `2 to add, 0 to change, 0 to destroy`, those two
  resources and no other; ZERO removed lines; one statement, Effect Allow, exactly 70 actions; a grep of the plan for each of
  `"iam:`, `"secretsmanager:`, `"cloudtrail:` reads zero -> apply.
- **B:** any other count, a third resource, any change to an existing policy (it would mean step A or B is not as applied),
  an action count other than 70, any `iam:`, `secretsmanager:` or `cloudtrail:` action -> apply NOTHING and report.

## Rollback per key

One act undoes it whole: apply the root again WITHOUT the variable (the default false makes both resources count 0), or
detach and delete the one policy. A resource policy a Dell changed in the interval is NOT undone by that: each such change is
its own act with its own rollback, which is why the CTO's rule has the Dell report it.

## Conditions

1. The plan shape of branch A, classified immediately before the apply, the three greps recorded.
2. Immediately before the plan: `python infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py` reads
   `freed_allowed=70/70 freed_excluded=5 undo_denied=181/181 selfsim_ok=9/9 ssm_ok=15/15 routes_ok=5/5 vendor_ok=235/235 all_ok=True`.
3. The group's attached-policy list saved before; one NEVER-2 ledger entry opened and closed.
4. Read-back LIVE with `simulate-principal-policy` on each Dell user, matched statement named. ALLOWED: `s3:PutBucketPolicy` on
   `opal-data-assets`; `lambda:AddPermission` on a non-protected function; `kms:PutKeyPolicy` on a key. REFUSED:
   `lambda:AddPermission` on one protected function (`DenyProtectedFunctions`); `s3:PutBucketPolicy` and
   `s3:PutLifecycleConfiguration` on the audit bucket (`DenyAuditTrailBucketPolicy`); `sqs:SetQueueAttributes` on an agentbus
   queue (`DenyAgentbusQueuePolicy`); `secretsmanager:PutResourcePolicy` on `opal/auth/jwt-private-key` (no Allow);
   `iam:UpdateAssumeRolePolicy` (`DenyEveryIamWrite`); one routes arm as before. `sqs:ReceiveMessage` on the user's own queue
   and `sqs:SendMessage` allowed as before. A re-plan WITH the variable reads no changes.
5. THE APPLIER MAKES NO RESOURCE-POLICY CALL ITSELF: the read-back is by simulation only. The exercise is a Dell's own first
   use, reported to the laptop. Until then: APPLIED, not EXERCISED.
6. Every later plan or apply of this root, by any seat, passes `-var apply_respol_allow=true`, or it will plan to DESTROY the
   Allow. This seat's next act after the apply is to make that durable (the variable's default set to true in the root, or a
   tfvars file the wrappers read), as a cell, and until it lands the order's report says so in its first line.
7. The CTO tells Andrew the five routes of "What this Allow CAN undo" in plain words when it signs, as it said it would for
   four of them (msg 106733); the fifth (object ACLs on the shared assets bucket) is added here.

**SIGNED** -- `2.0.0_SA_COO~C`
