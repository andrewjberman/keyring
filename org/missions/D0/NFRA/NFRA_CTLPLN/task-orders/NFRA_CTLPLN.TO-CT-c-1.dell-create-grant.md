# TO NFRA_CTLPLN.TO-CT-c-1 -- round 3 CT-c-1: the create grant -- a Dell creates, updates and tags non-IAM resources; IAM stays denied

<to_id>NFRA_CTLPLN.TO-CT-c-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~4</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-c-1` (`decompositions/NFRA_CTLPLN_DECOMP.round3.md`) | **outcome_ref:** FWD-10 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-c-1`, FWD-10, PRD v0.8 C-IDENTITY (the v0.7 sentence): the Dell policy grants create, update and tag for the non-IAM resource kinds
declared under the Terraform roots of the projects placed on a Dell; the list is DERIVED from those roots by a script, never typed from
memory; the four Deny statements are kept. You write the policy and prove it with a derivation check and a policy simulation. You APPLY
NOTHING.

**What exists** (root `infra/aws/terraform/nfra-ctlpln-identity/`, applied at site Z): `iam.tf` (group `cloudops-dell-agents-group`, two
users, managed policy `cloudops-dell-agent-deploy-policy` from `dell_deploy_policy.json`, two per-Dell bus policies);
`tests/check_identity.py` (last line today `IDENTITY-STATIC validate=ok no_access_key=True names_from_builder=6/6 ok=True`);
`tests/simulate_policy.py` (last line today `POLICY-SIM allowed_ok=8/8 denied_ok=11/11 all_ok=True`).

**Build:**

1. `tests/derive_resource_kinds.py` -- the derivation.
   - Dell-placed projects: every `org/missions/D*/*/*/project.json` whose `placement` is `DELL1` or `DELL2` and whose `status` is not
     `closed`. Print the count and the codes.
   - Their Terraform roots: every directory directly under `infra/aws/terraform/` whose name is cited as `infra/aws/terraform/<name>` in
     any file under those projects' `task-orders/` folders. Print the roots and, per root, which projects cite it. A project with no
     order contributes none; print those projects as `no-orders`.
   - Resource kinds: every `resource "<kind>"` in the `.tf` files of those roots (skip `.terraform/`). Print the distinct count.
   - Classify EVERY kind into exactly one of four classes, by a table inside the script (the table is the record):
     `IAM` (kind starts `aws_iam_`); `HELD-ACCESS` (a resource whose only purpose is to grant access: `aws_lambda_permission`,
     `aws_s3_bucket_policy`, `aws_sqs_queue_policy`, `aws_sns_topic_policy`, `aws_secretsmanager_secret_policy`, `aws_kms_grant`,
     `aws_cloudwatch_log_resource_policy`, and any other kind you find of that nature -- say which); `NOT-AWS` (`local_file`,
     `terraform_data` and the like); `GRANT` (everything else).
   - For each `GRANT` kind the table names the IAM actions that create, update and tag it (for example `aws_dynamodb_table` ->
     `dynamodb:CreateTable`, `dynamodb:UpdateTable`, `dynamodb:TagResource`, `dynamodb:UntagResource`, plus the update-time calls such
     as `dynamodb:UpdateTimeToLive`, `dynamodb:UpdateContinuousBackups`). No delete action. Then the script reads the two policy files
     and reports every `GRANT` kind whose create action no Allow statement covers as `uncovered`.
   - LAST line: `KINDS-DERIVED projects=<p> roots=<r> kinds=<k> grant=<g> iam=<i> held_access=<h> not_aws=<n> uncovered=<u> ok=<True|False>`
     with `ok=True` only when `uncovered=0` and `g+i+h+n == k`.
2. The policy. A managed policy is limited to 6,144 characters (whitespace not counted), so put the create, update and tag actions in a
   SECOND managed policy `dell_create_policy.json`, name `cloudops-dell-agent-create-policy`
   (`lib/opal_naming.name('cloudops', None, 'dell-agent-create', 'policy')`), tagged `DisplayName = "DellBoxes"`, attached to the group in
   `iam.tf`. Use service-level action patterns where they stay inside the rule (for example `dynamodb:Create*`, `dynamodb:Update*`,
   `dynamodb:Tag*`), never `<service>:*`. If one file still exceeds the limit, split by service family into a third file named by the
   builder and say so in your report.
   - `dell_deploy_policy.json` keeps its four Deny statements BYTE-IDENTICAL. An explicit Deny there overrides any Allow in any policy.
   - Do NOT allow, in any statement: any `iam:` write, `iam:PassRole`, or the access-granting actions (`lambda:AddPermission`,
     `lambda:RemovePermission`, `s3:PutBucketPolicy`, `s3:DeleteBucketPolicy`, `kms:PutKeyPolicy`, `kms:CreateGrant`,
     `secretsmanager:PutResourcePolicy`, `sns:AddPermission`, `sqs:AddPermission`, `logs:PutResourcePolicy`). They are open questions
     above this order; leave them unallowed and add no new Deny for them.
   - Two actions cannot be separated from access by the action name: `sqs:SetQueueAttributes` and `sns:SetTopicAttributes` set a
     policy as one attribute among many. Allow them (an update needs them) and file ONE surprise row naming both.
3. `tests/simulate_policy.py` -- extend the matrix; evaluate dell1's effective set (both group policies and `dell1_bus_policy.json` in
   one `simulate_custom_policy` call). ALLOWED (17): the existing 8, plus `dynamodb:CreateTable`, `sqs:CreateQueue`, `s3:CreateBucket`
   on `arn:aws:s3:::opal-x-test`, `secretsmanager:CreateSecret`, `scheduler:CreateSchedule`, `lambda:CreateFunction`,
   `logs:TagResource`, `dynamodb:TagResource`, `apigateway:POST` on `arn:aws:apigateway:us-east-1::/apis`. DENIED (17): the existing 11,
   plus `iam:PassRole`, `iam:CreateRole`, `s3:PutBucketPolicy`, `lambda:AddPermission`, `kms:PutKeyPolicy`,
   `secretsmanager:PutResourcePolicy`. Either decision `explicitDeny` or `implicitDeny` counts as denied; print which. LAST line
   `POLICY-SIM allowed_ok=<a>/17 denied_ok=<d>/17 all_ok=<True|False>`.
4. `tests/check_identity.py` -- the name comparison now covers the new policy (7 names), and it prints the character count of each
   policy document without whitespace against 6,144. LAST line
   `IDENTITY-STATIC validate=<ok|fail> no_access_key=<True|False> names_from_builder=<k>/<n> policy_size_ok=<True|False> ok=<True|False>`.
   A first `terraform init` of this root downloads a 700 MB provider and may pass 120 s; the root's `.terraform.lock.hcl` is committed,
   so run the check once outside the bound to warm the plugin cache, then under the bound for the record, and say so.

### ACCEPTANCE

<criterion id="CT3c1-AC1" cell_refs="CT-c-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/derive_resource_kinds.py</invocation><expect>uncovered=0 ok=True</expect></criterion>
`CT3c1-AC1` -- every derived non-IAM, non-access kind has its create action allowed, and the four classes sum to the kinds found.

<criterion id="CT3c1-AC2" cell_refs="CT-c-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py</invocation><expect>POLICY-SIM allowed_ok=17/17 denied_ok=17/17 all_ok=True</expect></criterion>
`CT3c1-AC2` -- the cloud's own evaluator allows the creates and still denies every IAM write, the pass, the access-granting actions and
the production deletes. The denied arm is the control: it must hold with the new Allow statements present.

<criterion id="CT3c1-AC3" cell_refs="CT-c-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/check_identity.py</invocation><expect>names_from_builder=7/7 policy_size_ok=True ok=True</expect></criterion>
`CT3c1-AC3` -- the root validates, every name is the builder's, and each policy document fits the managed-policy limit.

<expected_criteria>CT3c1-AC1,CT3c1-AC2,CT3c1-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **No apply, no `terraform plan` against the backend, no IAM write of any kind.** The only AWS call allowed is
  `iam:SimulateCustomPolicy` (read-only).
- **Never** an `aws_iam_access_key`, a key, a secret or a credential in any file.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
infra/aws/terraform/nfra-ctlpln-identity/iam.tf
infra/aws/terraform/nfra-ctlpln-identity/dell_deploy_policy.json
infra/aws/terraform/nfra-ctlpln-identity/dell_create_policy.json
infra/aws/terraform/nfra-ctlpln-identity/dell_create_*.json
infra/aws/terraform/nfra-ctlpln-identity/.terraform.lock.hcl
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_resource_kinds.py
infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py
infra/aws/terraform/nfra-ctlpln-identity/tests/check_identity.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `infra/aws/terraform/nfra-ctlpln-identity/main.tf`, `dell1_bus_policy.json`,
`dell2_bus_policy.json`, `lib/opal_naming.py`, every `org/missions/D*/*/*/project.json` and `task-orders/` folder, and the `.tf` files
of the derived roots.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round3.md</decomp_doc> (round 3), cell `CT-c-1`.
<owned_cells>CT-c-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT3c1-AC1, CT3c1-AC2, CT3c1-AC3. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~4/NFRA_CTLPLN.TO-CT-c-1.dell-create-grant.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT3c1-AC1,CT3c1-AC2,CT3c1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three last lines; the derived counts (projects, roots, kinds per class); the full `HELD-ACCESS` list you classified; the
character count of each policy; any kind whose actions you were unsure of; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: RUN at the cut by the policy simulation criterion (CT3c1-AC2); base read `POLICY-SIM allowed_ok=8/8 denied_ok=11/11 all_ok=True`; `comp-iam gaps` after the apply is the issuer's.
comp-adversary: RUN -- privilege escalation (every IAM write and the pass stay under the kept explicit Deny; access-granting actions unallowed); audit tampering (CloudTrail Deny kept); destructive data acts (no delete granted; production delete Deny kept); BLIND: an action whose name hides a policy attribute (sqs:SetQueueAttributes, sns:SetTopicAttributes -- rowed by the worker), and a create action for a kind the derivation's table maps wrongly (found at the first Dell apply).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.8 @6df8d231f4 ADDENDUM v0.7 (round 3's first cell), C-IDENTITY; Andrew-direct record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_063xZ_DELLS_CREATE_RESOURCES_NO_IAM_DEPLOYS_NOT_GATED_ON_SITEZ.md`; CTO
msgs 105997, 105999; decomposition round 3. Base dry-run at the cut: CT3c1-AC1 base FAIL as expected (the script does not exist);
CT3c1-AC2 base FAIL as expected (prints 8/8 and 11/11); CT3c1-AC3 base FAIL as expected (prints 6/6 and no `policy_size_ok`).
