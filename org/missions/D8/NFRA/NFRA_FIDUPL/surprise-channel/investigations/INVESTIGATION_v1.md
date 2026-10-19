# NFRA_FIDUPL -- surprise channel, INVESTIGATION v1 (round 1, dell1 fabric)

**Opened by:** `2.0.0_SA_COO~P1` at the L6 cut (seat rows; the CVO assembles from L8 -- spine v3 L8).
**Home:** the project tree's channel (`org/standards/PROJECT_TREE.contract.json` `surprise_channel_glob`); the gate
`.tools/surprise-row-gate.py` validates every NEW row (schema `org/surprise_channel/schemas/investigation_item.schema.json`).
Lane `ANY`.
**Id grammar:** a worker's row is `NFRA_FIDUPL-D1-W<n>-S<k>` (`<n>` = its slot, `<k>` next unused within that coordinate); a
seat's row is `NFRA_FIDUPL-D1-S<k>`; the CVO's adjudication rows live in `../adjudications/` as `NFRA_FIDUPL-D1-C-S<k>`.
**Append-only during the round.** Never edit an existing row.

```json
[
  {
    "id": "NFRA_FIDUPL-D1-S1",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "2.0.0_SA_COO~P1",
    "surfaced_at": "2026-10-19T20:15:59Z",
    "one_line": "The naming builder homes the code and state tiers of scope alongside in opal-data-alongside, a bucket that does not exist, and admits no meta or _ops tier, so round 1 puts the run record in the bronze tier as table _runs and delivers box code by SSM instead of an S3 code home.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "disarm_owner": "1.0.0_SA_CTO~DELL1 (owns the confirmation of the _runs home and the final code home; this seat only surfaces)",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -c \"import sys; sys.path.insert(0,'lib'); import opal_naming as o; print(o.address('fidelity','alongside','state','daily_pull','20261016','run.json'))\" (2026-10-19 ~20:0xZ) printed s3://opal-data-alongside/fidelity/alongside/state/daily_pull/20261016/run.json",
        "the same call with tier 'code' printed s3://opal-data-alongside/fidelity/alongside/code/canonical-fidelity/x; with tier 'meta' and with '_ops' it raised: tier is not one of NAMING_SCHEMA.json key.tier (enum bronze, silver, gold, platinum, state, code)",
        "address('fidelity','alongside','bronze','_runs','20261016','run.json') printed s3://opal-data-assets/fidelity/alongside/bronze/_runs/20261016/run.json",
        "CTO msg 8473: opal-data-alongside is NOT provisioned"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "PRD C-NAMES: every address is lib/opal_naming.py address() output; the Schwab run record lives under {source}/{scope}/_ops/daily_pull/ and meta/pulls/ and its code under an S3 code prefix.",
    "world_is": "For scope alongside the builder gives the code and state tiers a bucket that does not exist and has no tier for a run record, so a builder-clean run record and code home exist only in the bronze tier of opal-data-assets (the _runs table) and by SSM delivery to the box.",
    "notes": "Decision recorded in decompositions/NFRA_FIDUPL_DECOMP.md section 7 items 1 and 2. Nothing acts on a typed path."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S1",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T20:45:00Z",
    "one_line": "The HCL name builder refuses scope alongside at plan time: its generated_locals.tf predates the alongside scope row, so all 13 name calls in the Fidelity root fail a precondition, while the Python name() admits the same scope.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "terraform -chdir=infra/aws/terraform/canonical-fidelity-ec2 plan -input=false -no-color at worktree commit 1b5c10e11a printed 13 'Error: Module output value precondition failed' blocks, each 'local.name_scope_ok is false' with the message 'scope must be the LONG form of a FIRM, GLOBAL or MASTER row' (captured in the worktree at .scratch/fu6_plan.txt, not committed)",
        "infra/aws/terraform/modules/opal_name/generated_locals.tf at 1b5c10e11a carries 0 occurrences of the word alongside in scope_long, scope_short and scope_class; its header names registry@2e6709ab25, which is not an object in this repository",
        "infra/logic/registry/scopes.json at 1b5c10e11a carries the FIRM row key alongside (class FIRM), added by commit bd84d81948 (registry 4.0.0_SA_CRO~FIDELITY), an ancestor of HEAD",
        "python -I lib/opal_naming.py generate --out .scratch/gen failed with FileNotFoundError on data/firm_registry.json, the regeneration input, which this worktree does not carry",
        "python -I -c name('fidelity','alongside','uploader','role') at HEAD returned fidelity-alongside-uploader-role: the Python builder and the HCL builder disagree on the same scope"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "CLAUDE.md rule 30 and the FU-s-6 cell: every AWS resource name comes from the HCL builder (modules/opal_name) with system fidelity and scope alongside; a builder refusal is a surprise row, never a typed name.",
    "world_is": "The HCL builder's generated table is older than the registry row for alongside, so the HCL builder refuses every name this root asks for; the root validates (FU6-AC1 PASS) and cannot plan (FU6-AC3 FAIL) until the generated table is regenerated from a registry that carries the row.",
    "notes": "No name was typed and no scope was dropped to get around the refusal. Regeneration is outside this order's grant (modules/opal_name is read-only to FU-s-6). Owner of the regeneration: the registry owner (4.0.0_SA_CRO~FIDELITY lineage) or the CTO."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S2",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T20:45:00Z",
    "one_line": "No builder names the Wealthscape secret: the SECRET grammar {system}/{scope}/{purpose} is graded only, name() refuses a secret kind, and no secret constructor exists, so the Wealthscape secret piece is stopped and the root has no secret, no prevent_destroy, no secret grant and no secret id output.",
    "class": "BLOCKING",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python -I -c name('fidelity','alongside','wealthscape','credentials') at HEAD raised ValueError: kind 'credentials' is neither a NAMING_SCHEMA.json kind nor a cadence",
        "org/standards/NAMING_SCHEMA.json key secret: grammar {system}/{scope}/{purpose}, scope_form SHORT; kind.closed_at_l4 records that the secret kind was DROPPED because secrets keep their own slash-path grammar",
        "grep of lib/opal_naming.py for a secret constructor or def name/address/key over a secret returned none; the SECRET references at lines 906, 2204, 3071-3311 are grading and detection code only",
        "infra/aws/terraform/canonical-fidelity-ec2/main.tf, box.tf and outputs.tf at commit 1b5c10e11a: no aws_secretsmanager_secret resource, no secret grant for the Wealthscape credentials, no secret id output"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FU-s-6 item 3: an aws_secretsmanager_secret for the Wealthscape credentials, metadata only, prevent_destroy true, name from the builder; item 2: the box role grants GetSecretValue on its exact ARN.",
    "world_is": "No builder row can produce the Wealthscape secret name, so that resource and its grant cannot be written without typing a name, which the refusal clause forbids. The box, as planned, cannot read Wealthscape credentials until a builder path exists.",
    "notes": "The Quo key grant (quo/api-key, an existing secret, looked up by data source) is built. Surfaced for the CTO: a SECRET builder or a registered secret-name rule is needed before FU-s-6 can be completed."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S3",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T20:45:00Z",
    "one_line": "The FU6-AC2 guard refuses any literal 0.0.0.0/0, so it flags the egress-open rule the order requires; the guard cannot tell an egress rule from an ingress rule when both are a bare CIDR string.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu6g at 1b5c10e11a printed R1-FU6G-FAIL 0.0.0.0/0; no prevent_destroy on the secret (process rc 0; the verdict line is the result)",
        "infra/aws/terraform/canonical-fidelity-ec2/box.tf egress block of aws_security_group.box carries cidr_blocks = [0.0.0.0/0] with protocol -1 and no ingress block exists in the root",
        "the order's FU-s-6 item 1 names egress open and no ingress rules; r1_checks.py tf_guard tests the substring 0.0.0.0/0 across all .tf files"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FU6-AC2 (FU-s-6): no ingress, no wildcard secret grant, no secret version, prevent_destroy present; item 1: security group with NO ingress rules and egress open.",
    "world_is": "Egress open means 0.0.0.0/0 on the egress rule, so the guard's substring test fails on a rule the order requires; the no-ingress half of the guard is satisfied. The guard's prevent_destroy clause also fails because of S2.",
    "notes": "The egress literal was not rewritten to evade the guard. The guard's rule needs an egress-aware form, a CTO ruling, before FU6-AC2 can grade PASS."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S4",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T20:45:00Z",
    "one_line": "The run automation's wait step and stop step call SSM and EC2 describe actions that do not take a resource ARN, and the order forbids a * Resource, so the root grants only the resource-scoped actions and the automation may fail at its wait or stop step at run time.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "infra/aws/terraform/canonical-fidelity-ec2/automation.tf at 1b5c10e11a grants ec2:StartInstances, ec2:StopInstances, ssm:SendCommand and ssm:GetCommandInvocation only, each on the one instance or the one AWS-RunShellScript document",
        "the aws:waitForAwsResourceProperty step calls ssm DescribeInstanceInformation and the aws:changeInstanceState step may call ec2 DescribeInstances; neither is granted because the order forbids a * Resource",
        "the run is plan-only in this round; no AWS call of the automation was made, so the runtime need is INFERRED from the action definitions, not measured"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FU-s-6 item 2: no * Resource; item 4: the automation starts the instance, waits for Online, runs the wrapper and stops the instance in a step that runs whether or not the run failed.",
    "world_is": "The no-star rule and the wait step cannot both hold if the AWS action needs an unscopable Describe grant; the stop step is still reached through onFailure only if the stop step itself can run, which depends on the same grant.",
    "notes": "Proof needed at FU-x-1 or the first enabled run: a live describe of the automation execution. Not checked here (plan only)."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S5",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T20:45:00Z",
    "one_line": "The schedule role carries iam:PassRole on the automation role, beyond the one action the order names, because SSM requires the starting principal to pass the automation's assume role.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "GROUNDED",
      "evidence": [
        "infra/aws/terraform/canonical-fidelity-ec2/schedule.tf at 1b5c10e11a: aws_iam_role_policy.schedule statement PassTheAutomationRoleToSSM grants iam:PassRole on aws_iam_role.automation.arn with condition iam:PassedToService ssm.amazonaws.com",
        "the order's FU-s-6 item 5 names ssm:StartAutomationExecution on that one document as the role's scope"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FU-s-6 item 5: a role EventBridge assumes scoped to ssm:StartAutomationExecution on that one document.",
    "world_is": "The schedule role also holds a PassRole limited to the automation role and to SSM. It is the narrowest grant that lets the document's assume role be used by the start call, and it names no other role.",
    "notes": "Scoped as narrowly as the mechanism allows; a CTO ruling can narrow it further if SSM does not need it on this path."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S6",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T20:45:00Z",
    "one_line": "The box is created in the running state: aws_instance has no argument to create it stopped, so the first apply leaves the t3.medium running until the automation or a human stops it.",
    "class": "OBSERVATION",
    "hazard_standing": "ARMED",
    "disarm_owner": "2.0.0_SA_COO~P1 (stop the instance once after the first apply, before any rule is enabled)",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "infra/aws/terraform/canonical-fidelity-ec2/box.tf at 1b5c10e11a sets instance_initiated_shutdown_behavior = stop and manages no state argument, as the order's item 1 requires",
        "the aws_instance resource in the hashicorp/aws 5.x provider has no create-stopped argument (INFERRED from the provider schema; not read from a plan, which was refused at the name precondition)"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FU-s-6 item 1: the instance is created stopped-capable and is never left running by this root.",
    "world_is": "The instance will run after the first apply until something stops it, which is a cost exposure and not a data exposure, since no rule is enabled and the box has no inbound path.",
    "notes": "Armed until the first apply is stopped. The root cannot disarm it itself; the disarm owner runs the stop after apply."
  },
  {
    "id": "NFRA_FIDUPL-D1-W4-S7",
    "project": "NFRA_FIDUPL",
    "fabric": "dell1",
    "surfaced_by": "0.9.0_WK_NFRA_FIDUPL~4",
    "surfaced_at": "2026-10-19T20:45:00Z",
    "one_line": "The order names no VPC or subnet, so the root takes the account's default VPC by data source and places the box with a public IP for egress; the default VPC's existence in us-east-1 is not measured by this round.",
    "class": "OBSERVATION",
    "hazard_standing": "INERT",
    "grounding": {
      "status": "INFERRED",
      "evidence": [
        "infra/aws/terraform/canonical-fidelity-ec2/main.tf at 1b5c10e11a: data aws_vpc default with default = true; box.tf sets associate_public_ip_address = true",
        "the sibling canonical-schwab-ec2 root names no VPC either; the order's item 1 asks for no public IP beyond what egress needs"
      ]
    },
    "disposition": "UNDER_INVESTIGATION",
    "spec_asserts": "FU-s-6 item 1: no public-IP requirement beyond what egress to the internet needs.",
    "world_is": "The default VPC is assumed present and is the placement for the box; the plan was refused before the VPC read could be shown, so the assumption is not measured here.",
    "notes": "A dedicated VPC or subnet is a CTO placement decision; this round uses the default VPC."
  }
]
```
