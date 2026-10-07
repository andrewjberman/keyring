# NFRA_CTLPLN -- the Dell identity root applied at site Z -- never-widen half (CTO), `1.0.0_SA_CTO~Z`, 2026-10-07 ~04:4xZ

**Why this seat:** MSTR~Z msg 30566 (Andrew, relayed from the laptop CTO terminal ~04:2xZ: "Where is the Dell Keys? i want that
issued") asks this seat's half "the moment the plan is read". This half is written AHEAD of the plan so it is not the wait.
**It binds only if the executor's plan has exactly the shape in section 2.** The COO half is `2.0.0_SA_COO~Z`'s.

**Source read:** `infra/aws/terraform/nfra-ctlpln-identity/` at `origin/CLOUD` 0ae63f9dbf (`iam.tf`, `main.tf` and the three policy
JSONs, read in full by this seat). The shared tree did not hold the root at the read.

## VERDICT: SIGNED for leg (1), the identity apply, on the plan shape below. Leg (3) is NOT signed: its root is not on origin.

## 1. What the act creates, and what it does not

- 1 group (`cloudops-dell-agents-group`).
- 2 users (`cloudops-dell1-agent-user`, `cloudops-dell2-agent-user`).
- 1 group membership.
- 3 managed policies (deploy, dell1-bus, dell2-bus).
- 1 group policy attachment and 2 user policy attachments.
- **NO access key.** `iam.tf` and `main.tf` carry no `aws_iam_access_key`.

Nothing existing changes: no existing principal, policy, role or resource is in the root.

## 2. Conditions on the plan (the half binds only on these)

1. **The plan is UNTARGETED and reads exactly `10 to add, 0 to change, 0 to destroy`**, with the ten resources of section 1.
   Any change or destroy, or any eleventh resource, is a STOP.
2. No `aws_iam_access_key` appears in the plan, and no key appears in state after the apply.
3. The root's own checks run before the apply: `tests/check_identity.py` (the names equal the builder's) and
   `tests/simulate_policy.py`.
4. The NEVER-2 ledger entry opens before the apply.
5. **After the apply, read live:**
   - Both users exist, each with 0 access keys.
   - The group holds exactly those 2 users.
   - The 3 policies exist at the JSON's bytes (compare the policy documents, not the names).
6. **Rollback:** `safe-apply` of a destroy of this root. It touches only what the root created. If a key exists by then, the key
   is deleted first.

## 3. The blast radius of what the keys will carry (NEVER-1: named here, not left to the policy's description)

The policy's description says the Dells "never change access, audit or delete production data". The explicit Deny statements
do enforce that for the Dell identity's OWN calls: every IAM write (PassRole included), every CloudTrail write, and deletes on
`opal-data-*`, DynamoDB tables and RDS. Three things the description does not say:

1. **`lambda:UpdateFunctionCode` + `lambda:InvokeFunction` on `Resource: "*"` reach every Lambda's execution role.**
   - A Dell identity can replace any function's code and invoke it. That code then runs under the function's role, which the
     Dell policy's Deny statements do not bind.
   - So the real ceiling of a Dell key is the union of every Lambda execution role in the account, not this policy.
   - Measured for one case only: 0 roles carry the AWS-managed `AdministratorAccess`. The custom role policies were NOT
     censused. The extent is unmeasured, and it is stated as that.
2. **`s3:PutObject` on `opal-*` includes OVERWRITE** of production data objects, and it includes the Terraform state bucket
   (`opal-313476888478-terraform-state`) and the Lambda artifact bucket. The Deny covers deletes on `opal-data-*`, not overwrites.
   On a versioned bucket the prior version survives. On an unversioned one it does not.
3. **The grant is cross-firm:** `opal-*` covers every firm's bucket. That is the same reach the site-Z and laptop agent
   identities have. It is named because CLAUDE.md section 5 keeps cross-firm reads a hard stop for pipelines.

**This seat signs with these named.** The Dells are Andrew's own machines running this fabric's agents, and the policy is a
guardrail on them, not a boundary against them. It is narrower than the identities the other two devices use.

**The tightening is NFRA_CTLPLN's to place** (the laptop CTO's project), as a row. It does not gate Andrew's order:
- Scope `lambda:UpdateFunctionCode` and `lambda:InvokeFunction` by a function-name prefix or tag.
- Exclude the state bucket from `PutObject`.

## 4. Two functional gaps the executor should expect (not safety; stated so a failure is not read as a broken key)

- **`iam:PassRole` is denied.** So `ecs:RunTask` and `ecs:RegisterTaskDefinition` with a task role, and `events:PutTargets`
  with a role, will fail for a Dell. `lambda:CreateFunction` is not granted at all. A Dell can update what exists and cannot
  create new principals or functions. That is the "site-Z-only IAM apply" design.
- **No `kms:Decrypt` / `kms:GenerateDataKey`.** Objects in a bucket encrypted with a customer KMS key will not read or write.

## 5. Leg (2), the keys (MSTR~Z's act on Andrew's word; this seat's conditions for it)

- One access key per user, created outside Terraform, after condition 5 reads 0 keys.
- The secret is never printed to a transcript, a log or a commit. It goes by `tailscale file cp` to `dell1:` and `dell2:`.
- The local copies are deleted and read back gone.
- `list-access-keys` then reads exactly 1 per user. A second key on either user is a STOP.

## 6. Leg (3) is not signed

`infra/aws/terraform/nfra-ctlpln-agentbus/` does NOT exist at `origin/CLOUD` 0ae63f9dbf.
- `git ls-tree origin/CLOUD infra/aws/terraform/` lists `nfra-agentbus`, `nfra-agentbus-alyssa01`, `nfra-agentbus-port2` and
  `nfra-ctlpln-identity` only.
- Until the laptop pushes that root, or names the one it means, there is nothing to plan or to sign.
- The bus policies above already name `agentbus-global-dell1-queue*` and `agentbus-global-dell2-queue*`. Those ARNs may not
  exist yet. The policies apply regardless, and the grant is inert until the queues do.

`1.0.0_SA_CTO~Z`, 2026-10-07 ~04:4xZ.
