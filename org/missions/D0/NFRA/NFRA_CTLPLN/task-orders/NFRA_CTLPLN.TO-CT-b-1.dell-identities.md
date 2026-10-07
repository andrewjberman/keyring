# TO NFRA_CTLPLN.TO-CT-b-1 -- round 2 CT-b-1: the Dell identities -- one group, two users, the deploy policy, no access key

<to_id>NFRA_CTLPLN.TO-CT-b-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~1</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-b-1` (`decompositions/NFRA_CTLPLN_DECOMP.round2.md`) | **outcome_ref:** FWD-10 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-b-1`, FWD-10: each Dell acts in the cloud under its own identity, may deploy trunk code, and can never change access. You write the
Terraform and prove it with a static check and a policy simulation. You APPLY NOTHING: the apply is an IAM-creating apply, done at site Z by the
issuer's route, and the access keys are created after it, outside Terraform.

**The contract (PRD v0.6 C-IDENTITY, the CTO's rulings):**
- One IAM group and one IAM user per Dell. Names are builder output, already read (NAMING_SCHEMA v1.13): group `cloudops-dell-agents-group`,
  users `cloudops-dell1-agent-user` and `cloudops-dell2-agent-user`, managed policy `cloudops-dell-agent-deploy-policy`. Re-read each with
  `lib/opal_naming.name('cloudops', None, '<function>', '<kind>')` in your check (functions `dell-agents` group, `dell1-agent` / `dell2-agent`
  user, `dell-agent-deploy` policy) -- never type a name the check does not compare to the builder.
- Andrew's display name for the group is **DellBoxes**: put `DisplayName = "DellBoxes"` as a tag on the policy and on both users (IAM groups
  take no tags; say so in a comment).
- **ALLOW** what code and data deploys need: S3 object read/write/list on the `opal-*` buckets and the Terraform state bucket
  `opal-313476888478-terraform-state` (plus its lock table if the backend uses one -- read `infra/aws/terraform/nfra-agentbus-port2/main.tf`
  for the backend shape), Lambda, ECS task definitions and services, EventBridge rules and targets, DynamoDB items, CloudWatch Logs, SQS send/
  receive on `agentbus-*` queues, and the read-only Describe/Get/List calls a `terraform plan` makes.
- **DENY** (explicit Deny statements, so no Allow can override them): every IAM write (`iam:Create*`, `iam:Delete*`, `iam:Put*`,
  `iam:Attach*`, `iam:Detach*`, `iam:Update*`, `iam:Add*`, `iam:Remove*`, `iam:Tag*`, `iam:Untag*`, `iam:PassRole` is NOT denied only if a
  deploy needs it -- deny it unless you find a deploy path that needs it, and say which); every CloudTrail write (`cloudtrail:Stop*`,
  `cloudtrail:Delete*`, `cloudtrail:Update*`, `cloudtrail:Put*`); production data deletes (`s3:DeleteBucket*`, `s3:DeleteObject*` and
  `s3:PutLifecycleConfiguration` on `opal-data-*` buckets, `dynamodb:DeleteTable`, `dynamodb:DeleteBackup`, `rds:Delete*`).
- **No `aws_iam_access_key` resource, anywhere** (a key in state is a secret in state). Keys are created later, one per user, at site Z.
- The policy document lives in `dell_deploy_policy.json` and is loaded with `file()`, so the simulation reads the same bytes Terraform applies.

**Build** a new Terraform root `infra/aws/terraform/nfra-ctlpln-identity/`:
- `main.tf`: `terraform { required_version >= 1.5.0; required_providers aws ~> 5.0; backend "s3" { bucket
  "opal-313476888478-terraform-state", key "nfra-ctlpln-identity/tfstate", region us-east-1 } }` and `provider "aws" { region us-east-1 }`;
  a header comment naming FWD-10, C-IDENTITY, the site-Z-only apply and the no-key rule.
- `iam.tf`: `aws_iam_group`, two `aws_iam_user` (tagged), `aws_iam_group_membership` (or `aws_iam_user_group_membership`), `aws_iam_policy`
  from `dell_deploy_policy.json` (tagged), `aws_iam_group_policy_attachment`.
- `tests/check_identity.py` -- the static check: runs `terraform -chdir=<root> init -backend=false -input=false` and `terraform validate`;
  asserts no `aws_iam_access_key` in any `.tf`; asserts every name in `iam.tf` equals the builder output; prints as the LAST line
  `IDENTITY-STATIC validate=<ok|fail> no_access_key=<True|False> names_from_builder=<k>/<n> ok=<True|False>`.
- `tests/simulate_policy.py` -- the policy simulation: calls `aws iam simulate-custom-policy` (read-only; boto3 `iam.simulate_custom_policy`)
  with `dell_deploy_policy.json` for a fixed matrix -- ALLOWED: `s3:PutObject` on `arn:aws:s3:::opal-data-assets/x`, `lambda:UpdateFunctionCode`,
  `ecs:RegisterTaskDefinition`, `sqs:SendMessage` on an `agentbus-*` queue ARN, `s3:GetObject` on the state bucket; DENIED: `iam:CreateUser`,
  `iam:CreateAccessKey`, `iam:AttachUserPolicy`, `iam:PutRolePolicy`, `cloudtrail:StopLogging`, `cloudtrail:DeleteTrail`, `s3:DeleteObject`
  on `arn:aws:s3:::opal-data-assets/x`, `s3:DeleteBucket` on `arn:aws:s3:::opal-data-assets`, `dynamodb:DeleteTable`; prints one line per
  action with its decision and, as the LAST line, `POLICY-SIM allowed_ok=<a>/5 denied_ok=<d>/9 all_ok=<True|False>`.

### ACCEPTANCE

<criterion id="CT2b1-AC1" cell_refs="CT-b-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/check_identity.py</invocation><expect>no_access_key=True names_from_builder=6/6 ok=True</expect></criterion>
`CT2b1-AC1` -- the root validates, carries no access key, and every name is the builder's.

<criterion id="CT2b1-AC2" cell_refs="CT-b-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py</invocation><expect>POLICY-SIM allowed_ok=8/8 denied_ok=11/11 all_ok=True</expect></criterion>
`CT2b1-AC2` -- the cloud's own evaluator allows the five deploy actions and denies the nine access, audit and production-delete actions.

<expected_criteria>CT2b1-AC1,CT2b1-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Terraform's `.terraform/` and lock file stay
  uncommitted unless the root's siblings commit `.terraform.lock.hcl` (read `infra/aws/terraform/nfra-agentbus-port2/`).
- **No apply, no `terraform plan` against the backend, no IAM write of any kind.** The only AWS call allowed is
  `iam:SimulateCustomPolicy` (read-only).
- **Never** an `aws_iam_access_key`, a key, a secret or a credential in any file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W1-S<k>`) in the investigation file, and do not weaken the test or the expected value.

<paths>
infra/aws/terraform/nfra-ctlpln-identity/main.tf
infra/aws/terraform/nfra-ctlpln-identity/iam.tf
infra/aws/terraform/nfra-ctlpln-identity/dell_deploy_policy.json
infra/aws/terraform/nfra-ctlpln-identity/dell1_bus_policy.json
infra/aws/terraform/nfra-ctlpln-identity/dell2_bus_policy.json
infra/aws/terraform/nfra-ctlpln-identity/.terraform.lock.hcl
infra/aws/terraform/nfra-ctlpln-identity/tests/check_identity.py
infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round2.md</decomp_doc> (round 2), cell `CT-b-1`.
<owned_cells>CT-b-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT2b1-AC1, CT2b1-AC2. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~1/NFRA_CTLPLN.TO-CT-b-1.dell-identities.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT2b1-AC1,CT2b1-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both check lines, the policy's Allow and Deny statements in brief, whether `iam:PassRole` is denied and why, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: RUN at the cut by the policy simulation criterion (CT2b1-AC2); `comp-iam gaps` after the site-Z apply is the issuer's.
comp-adversary: RUN -- privilege escalation (every IAM write denied, PassRole denied unless a measured need); audit tampering (CloudTrail writes denied); destructive data acts (production deletes denied); secrets (no access key in Terraform, CTO 105913); BLIND: a deploy path needing an action the Allow omits (found at the first Dell deploy; the fix is a policy amendment applied at site Z).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.6 @0bab4b7532 C-IDENTITY, FWD-10; CTO msgs 105913, 105915, 105920, 105929; decomposition round 2.

## AMENDMENT 1 (2.0.0_SA_COO~C, 2026-10-07 ~02:5xZ) -- a Dell's fabric manager uses the bus: send to every box, receive only its own

Andrew asked, relayed by `1.0.0_SA_CTO` (msg 105931): a Dell MSTR needs the agentbus. The order's "SQS send/receive on agentbus-* queues" is
too wide: a Dell must NOT read another box's inbound queue. The issuer amends its own order (CLAUDE.md rule 27, L6); gate limb: none graded
this modification (LIMB 6 grades new orders only; the order declares no `<placeholders>`). CT2b1-AC1 and CT2b1-AC2 expectations change as below.
1. **The group's deploy policy** (`dell_deploy_policy.json`): REMOVE the agentbus receive; ALLOW `sqs:SendMessage`, `sqs:GetQueueUrl`,
   `sqs:GetQueueAttributes` on the four boxes' inbound queues only: `arn:aws:sqs:us-east-1:313476888478:agentbus-ajbdev-sitez-to-laptop.fifo`
   (laptop's, ARN read live), `arn:aws:sqs:us-east-1:313476888478:agentbus-ajbdev-laptop-to-sitez.fifo` (site Z's), and the Dells' by prefix
   `arn:aws:sqs:us-east-1:313476888478:agentbus-global-dell1-queue*` and `...agentbus-global-dell2-queue*` (their FIFO names land with CT-b-3;
   the prefix covers the builder's final form).
2. **One per-user bus policy each**, names builder output: `cloudops-dell1-agent-bus-policy`, `cloudops-dell2-agent-bus-policy`
   (`name('cloudops', None, 'dell1-agent-bus', 'policy')`), files `dell1_bus_policy.json` / `dell2_bus_policy.json`, attached with
   `aws_iam_user_policy_attachment` to that Dell's user only, tagged DisplayName=DellBoxes: ALLOW `sqs:ReceiveMessage`, `sqs:DeleteMessage`,
   `sqs:ChangeMessageVisibility`, `sqs:GetQueueAttributes` on that Dell's own queue prefix only.
3. **The check** now compares SIX names to the builder (group, two users, deploy policy, two bus policies): last-line expectation
   `no_access_key=True names_from_builder=6/6 ok=True`.
4. **The simulation** evaluates dell1's effective set (the group policy + `dell1_bus_policy.json` together in one
   `simulate_custom_policy` call). ALLOWED (8): the four non-SQS deploy actions of the original matrix (`s3:PutObject` data, `lambda:UpdateFunctionCode`,
   `ecs:RegisterTaskDefinition`, `s3:GetObject` state) plus `sqs:SendMessage` to the laptop's, site Z's and dell2's inbound queues and
   `sqs:ReceiveMessage` on dell1's own. DENIED (11): the original nine plus `sqs:ReceiveMessage` on the laptop's inbound queue and on dell2's.
   Last-line expectation `POLICY-SIM allowed_ok=8/8 denied_ok=11/11 all_ok=True`.
