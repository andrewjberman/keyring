# COO never-widen half -- NFRA_CTLPLN: the Dell identity root, STEP A of three -- the Denies first (two policies changed in place)

**Author:** `2.0.0_SA_COO~C`, 2026-10-08 ~08:3xZ. **Read at:** trunk @5cff7df18d (the merge of cell CT-a-1 AMENDMENTS 11 to 13).
Root `infra/aws/terraform/nfra-ctlpln-identity/`. **Counterpart owed:** a CTO half.
**Authority:** `1.0.0_SA_CTO` msg 106838: "the Denies step applies BEFORE plan 1 ... So: Denies, then plan 1 (targeted at its
five), then the Allow. Send me the half for the Denies step first; it can be signed alone."; msg 106781 (the three ruled
Denies); msg 106838 item 1 (the seven audit-bucket settings); msgs 106743 and 106757 (dell2's parameter read, by exact ARN);
Andrew-direct 2026-10-08 ~00:4xZ as recorded (this seat read the record and did not hear the word).

## The three steps, so this one is read in its place

| step | what | state |
|---|---|---|
| **A (this half)** | two policies changed in place: Denies added, plus two small Allows that live in the same document | this pair |
| B | plan 1's remaining four resources: the secrets policy and attachment created, the old Deny policy and attachment destroyed | pair signed (COO @63fe18a5fd, CTO @a8c3e4943e); its plan shape changes, see below |
| C | the Allow of 70 resource-policy actions and its attachment, behind `-var apply_respol_allow=true` | its own pair, not yet written |

## The act

One `safe-apply` of the root TARGETED at exactly `aws_iam_policy.dell_agent_create` and `aws_iam_policy.dell_agent_deploy`, at the
laptop. The variable `apply_respol_allow` is NOT passed (it defaults to false).

## The plan, MEASURED

Laptop, 2026-10-08 ~08:2xZ, read-only, exit 2: `Plan: 0 to add, 2 to change, 0 to destroy.` 54 added lines, ZERO removed.

**`aws_iam_policy.dell_agent_create`, updated in place, gains four statements and loses nothing:**

| statement | effect | what |
|---|---|---|
| `DenyAuditTrailBucketPolicy` | Deny | 21 `s3` write actions on `arn:aws:s3:::opal-cloudtrail-logs-313476888478` and its objects: the 14 policy, ACL, access-point and access-grant actions of the Allow's list, and the 7 settings writes (lifecycle, logging, notification, encryption, versioning, ownership controls, public-access block) |
| `DenyAgentbusQueuePolicy` | Deny | `sqs:AddPermission`, `sqs:RemovePermission`, `sqs:SetQueueAttributes` on the four agentbus queue ARNs, exact, no wildcard |
| `SimulateOwnPolicyOnly` | Allow | `iam:SimulatePrincipalPolicy` on `user/${aws:username}` (already signed in plan 1; it rides here because it is in this document) |
| `ReadPublicAmiParameter` | Allow | `ssm:GetParameter` on `arn:aws:ssm:us-east-1::parameter/aws/service/ami-amazon-linux-latest/al2023-ami-kernel-default-x86_64` only |

**`aws_iam_policy.dell_agent_deploy`, updated in place:** the existing statement `DenyProtectedFunctions` gains four actions on
its own twenty resources (the ten protected functions and their qualified forms): `lambda:AddPermission`,
`lambda:RemovePermission`, `lambda:AddLayerVersionPermission`, `lambda:RemoveLayerVersionPermission`.

**Writers of the property: N = 1**, this root; read.

## Blast radius

Two managed policies of the Dell agent group; two principals (`cloudops-dell1-agent-user`, `cloudops-dell2-agent-user`).

**This step NARROWS in three places and WIDENS in two. Both stated in full.**

Narrowing (new refusals; each simulated for both users, explicit deny with the new statement matched, 181 of 181 arms
including controls):
1. **The audit-trail bucket.** 7 of the 21 actions are things a Dell CAN DO TODAY and will lose: changing that bucket's
   lifecycle, logging, notification, encryption, versioning, ownership controls and public-access block. They predate this
   project (found by the cell's worker, row NFRA_CTLPLN-W14-S16) and are closed by this step. The other 14 are not allowed
   today; the Deny is laid ahead of step C's Allow.
2. **The four agentbus queues.** `sqs:SetQueueAttributes` and the two permission actions are refused on them. Today the
   resource-policy Deny still covers these; after step B removes it, this statement is what keeps a Dell from changing a
   queue's policy. Receive, send, delete, change-visibility and the reads are NOT denied: simulated before and after, 48 of 48
   arms identical (a Dell receives on its own queue, sends to the others, and is refused a receive on another box's queue,
   exactly as today).
3. **The ten protected functions.** Permission actions refused. Not allowed today either; laid ahead of step C.

**Could a narrowing break a Dell run in flight?** Only by one of the 7 audit-bucket settings writes or by a queue-attribute
write on an agentbus queue. No Dell-placed project's write set names the audit bucket or the agentbus Terraform (the queues
are the laptop's, `infra/aws/terraform/nfra-ctlpln-agentbus/` and `nfra-agentbus-port2/`). This seat did not sweep running Dell
jobs; the claim is from the placement register, not from a process read.

Widening (new allows):
4. **One public parameter read**, the exact ARN above, one action. Simulated: allowed for both users on that ARN; a different
   public parameter and an account parameter refused. It is the read `2.0.0_SA_COO~Y2` on dell2 has been refused since ~00:3xZ
   (`infra/aws/terraform/investor-reporting/ycharts/instance.tf:40`), which blocks a release behind Andrew's own retry. Four
   other Terraform roots read the same parameter and are covered by the same grant; `opal-gateway` reads the ARM variant,
   which is NOT covered.
5. **Self-simulate**, as signed in plan 1.

## What this does to step B (plan 1), stated so nobody is surprised

Plan 1 was signed as five resources with the create policy changed in place. After step A the create policy is already at
its final text, so step B's TARGETED plan at the same five addresses will read **`2 to add, 0 to change, 2 to destroy`**, not
`2 to add, 1 to change, 2 to destroy`. This seat amends its plan-1 half and order TO-APPLY-11 to that shape when step A has
applied and the plan is measured; the CTO's half needs the same one-line amendment. Nothing in plan 1's blast radius changes.

## Expected outcome, BOTH branches

- **A:** the targeted plan reads exactly `0 to add, 2 to change, 0 to destroy`, those two policies and no other; ZERO removed
  lines; the create policy gains exactly the four statements named and the deploy policy's one statement gains exactly the
  four actions named; the strings `respol_allow`, `vendor_secrets` and `dell_agent_respol` do not appear as resources in the
  plan -> apply.
- **B:** any other count, a third resource, any removed line, a fifth statement, a wildcard in either new Deny's resources or
  in the parameter's ARN, an account id inside the parameter's ARN -> apply NOTHING and report.

## Rollback per key

Per policy, independent: the live default version of each policy document is saved with its SHA-256 before the apply; IAM
keeps the previous policy version, so `set-default-policy-version` to it restores that policy in one call, or the merge is
reverted and the same targeted apply runs. A parameter read made in the interval is a read of a public value; nothing to undo.

## Conditions

1. The plan shape of branch A, classified immediately before the apply.
2. Immediately before the plan: `python infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py` reads
   `undo_denied=181/181 selfsim_ok=9/9 ssm_ok=15/15 routes_ok=5/5 vendor_ok=235/235 all_ok=True`.
3. Both live policy documents saved with SHA-256; one NEVER-2 ledger entry opened and closed.
4. Read-back LIVE with `simulate-principal-policy` on each Dell user, matched statement named: `s3:PutLifecycleConfiguration`
   and `s3:PutBucketPolicy` on the audit bucket refused by `DenyAuditTrailBucketPolicy`; `sqs:SetQueueAttributes` on each of
   the four agentbus queues refused (today by the old Deny policy as well: name every matched statement);
   `sqs:ReceiveMessage` on the user's own queue allowed and `sqs:SendMessage` allowed, as before; `lambda:AddPermission` on one
   protected function refused; `ssm:GetParameter` on the exact ARN allowed, on `.../al2023-ami-kernel-6.1-x86_64` refused;
   self-simulate allowed on self, refused on the other user. A re-plan with the same two targets reads no changes.
5. The exercised read is dell2's own: its seat's `terraform plan` of the YCharts root no longer fails on the parameter. Until
   then: APPLIED, not EXERCISED.
6. Rows NFRA_CTLPLN-W14-S16 (the seven settings) and the queue and audit-bucket parts of W14-S15 are disarmed by this step
   applying; the protected-function part of W14-S15 is disarmed here too, ahead of the Allow.

**SIGNED** -- `2.0.0_SA_COO~C`
