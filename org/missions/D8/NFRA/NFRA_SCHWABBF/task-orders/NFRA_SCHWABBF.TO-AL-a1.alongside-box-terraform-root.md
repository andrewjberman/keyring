# TO NFRA_SCHWABBF.TO-AL-a1 -- the Alongside Schwab Box, Terraform root part 1: backend, master map, IAM, secrets, security group, the Windows instance (text only)

<to_id>NFRA_SCHWABBF.TO-AL-a1</to_id>
<project>NFRA_SCHWABBF</project>
<issued_to>0.9.0_WK_NFRA_SCHWABBF~11</issued_to>
<issued_by>2.0.0_SA_COO~SA</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>alongside</workstream>

**Directive:** D8 | **Fabric:** laptop | **Decomp cell:** `AL-a-1` (`decompositions/NFRA_SCHWABBF_DECOMP_AL1.md`) |
**outcome_ref:** FWD-8 | **depends_on:** none

---

## WORKER FACE

### THE CELL

`AL-a-1`, the cloud half of PRD v0.5 C-ALONGSIDE. Andrew-direct 2026-10-20 ~13:5xZ: "it should be exact same setup and logic as already exists with the 49 schwab box. this one should explicitly be labeled as an alongside box".
You write a NEW Terraform root, as TEXT, plus a test. You run no `terraform init`, `plan` or `apply`, no `aws` command, nothing against Schwab. The apply is a later release act of the NFRA CloudOps lane. WORLD only because the files sit under `infra/`.

**New files (all under `infra/aws/terraform/alongside-schwab-ec2/`, which does not exist yet; you create it):** `main.tf`, `masters.tf`, `iam.tf`, `secrets.tf`, `box.tf`. A second cell (`AL-s-1`) later adds `schedule.tf` in the same folder and READS the addresses fixed below, so use these addresses EXACTLY.

**Prior art to read first (read-only; edit NOTHING in these):** `infra/aws/terraform/canonical-schwab-ec2/main.tf` (provider and backend shape), `iam.tf` (role, SSM attachment, profile, deny planes), `monolith-iam.tf` lines 1-118 (the per-master write-only statements), `secrets.tf` (metadata-only secrets with `prevent_destroy`), `infra/aws/terraform/modules/opal_name/` (the name builder module: inputs `system`, `scope`, `function`, `kind`; output `name`).

**Fixed addresses and values (the contract with `AL-s-1`; do not rename):**
- `local.alongside_firm = "cottonwood"`.
- `local.alongside_masters`, a map keyed by the master number, each value an object with `label` and `cron`; EXACTLY these four entries (no other master appears anywhere in the root):
  `"08719286" = { label = "Cottonwood firm FA08719286", cron = "cron(15 11,23 * * ? *)" }`,
  `"08134043" = { label = "Cottonwood advisor Stephen SL08134043", cron = "cron(45 11,23 * * ? *)" }`,
  `"08165601" = { label = "Cottonwood advisor Christa Bass", cron = "cron(15 12,0 * * ? *)" }`,
  `"08480305" = { label = "Cottonwood advisor Jay Rubottom", cron = "cron(45 12,0 * * ? *)" }`.
- `aws_instance.alongside_box`, `aws_iam_role.alongside_box`, `aws_iam_instance_profile.alongside_box`, `aws_security_group.alongside_box`, `aws_secretsmanager_secret.alongside_sdd_credentials`, `aws_secretsmanager_secret.alongside_ec2_credentials`.
- Names come from the builder module, NEVER typed (CLAUDE.md rule 30). Use `module "<x>_name"` blocks with `source = "../modules/opal_name"`, `system = "schwab"`, `scope = "alongside"`, `function = "si2-box"`, and `kind` = `role`, `profile`, `sg`, `runner`, `policy` (one module block each). Their outputs, measured with `lib/opal_naming.py` on 2026-10-20, are `schwab-alongside-si2-box-role`, `-profile`, `-sg`, `-runner`, `-policy`. The test must recompute them with `lib/opal_naming.py name(...)` and compare to the module inputs (it does not need terraform).

**Build.**
1. `main.tf`: `terraform { required_version = ">= 1.5.0"; required_providers aws "hashicorp/aws" "~> 5.0"; backend "s3" { bucket = "opal-313476888478-terraform-state", key = "alongside-schwab-ec2/tfstate", region = "us-east-1" } }`; `provider "aws" { region = "us-east-1" }`; variables `box_vpc_id` (default `"vpc-0cc0c6a75e54605e3"`), `box_subnet_id` (default `"subnet-039d04cfaee66a5f6"`), `box_instance_type` (default `"t3.large"`). A header comment names the box "Alongside Schwab Box", says it is the Alongside copy of the 49F Schwab Box, and that nothing here is applied by the cell.
2. `masters.tf`: the two locals above; the five `module` name blocks.
3. `iam.tf`: `aws_iam_role.alongside_box` (name from the role module; trust: `ec2.amazonaws.com`), `aws_iam_role_policy_attachment` of `arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore`, `aws_iam_role_policy` (name from the policy module) whose `jsonencode` policy has these statements, and `aws_iam_instance_profile.alongside_box` (name from the profile module). The statements:
   - `AlongsideCodeRead`: `s3:GetObject` on `arn:aws:s3:::opal-data-assets/code/alongside-schwab-si2/*` ONLY (no ListBucket). Comment: `code/` is the reserved system prefix and the builder has no code tier, so this prefix is the one declared non-builder address.
   - `AlongsideSddCredentialsRead`: `secretsmanager:GetSecretValue` on EXACTLY `aws_secretsmanager_secret.alongside_sdd_credentials.arn` (one ARN, no `schwab/*`).
   - `AlongsideEc2CredentialsWrite`: `secretsmanager:PutSecretValue` on EXACTLY `aws_secretsmanager_secret.alongside_ec2_credentials.arn`.
   - `MonolithSchwabList`: `s3:ListBucket` on `arn:aws:s3:::opal-data-assets` with `Condition.StringLike["s3:prefix"] = ["schwab/${local.alongside_firm}/bronze/*"]`. Comment the reason from `monolith-iam.tf:44-52` in your own words (a listing denial is swallowed by the resumability index).
   - `MonolithSchwabWrite`: `s3:PutObject` on one resource PER MASTER, built with a `for` over `keys(local.alongside_masters)`: `arn:aws:s3:::opal-data-assets/schwab/${local.alongside_firm}/bronze/*/date=*/${master}.*`. NEVER a resource equal to `.../schwab/cottonwood/bronze/*` (folder-wide wildcard), and NO `s3:GetObject`, NO `s3:DeleteObject` on data anywhere in the policy except the code read above (the write-only invariant, PRD C-ALONGSIDE).
   - `MonolithSchwabOpsWrite`: `s3:PutObject` on `arn:aws:s3:::opal-data-assets/schwab/${master}/_ops/*`, per master, same `for` shape. `MonolithSchwabMetaPullsWrite`: `s3:PutObject` on `.../schwab/${master}/meta/pulls/*`, per master. Comment: meta and `_ops` stay at MASTER scope because Andrew has not answered the silver/meta/`_ops` scope question (PRD OPEN AT ANDREW item 1).
   - `DenyBdPlane`, `DenyCotPlane`, `DenyInfPlane`: `Effect = "Deny"`, `Action = ["s3:*"]`, on `arn:aws:s3:::opal-data-bd` + `/*`, `opal-data-cot` + `/*`, `opal-data-inf` + `/*` (copy of `iam.tf:97-118`).
4. `secrets.tf`: `aws_secretsmanager_secret.alongside_sdd_credentials` (name `"schwab/alongside/sdd-credentials"`, this secret ALREADY EXISTS, so add an `import { to = aws_secretsmanager_secret.alongside_sdd_credentials, id = "schwab/alongside/sdd-credentials" }` block and the `prevent_destroy = true` + `ignore_changes = [tags, tags_all, force_overwrite_replica_secret, recovery_window_in_days]` lifecycle exactly as `canonical-schwab-ec2/secrets.tf` does) and `aws_secretsmanager_secret.alongside_ec2_credentials` (name `"schwab/alongside/ec2-credentials"`, NEW, same lifecycle, description "Alongside Schwab Box Windows Administrator login, generated on the box by bootstrap; never in repo/chat"). METADATA ONLY: no `aws_secretsmanager_secret_version` resource anywhere (a value in state is a defect).
5. `box.tf`: `data "aws_ssm_parameter" "windows_ami"` for `/aws/service/ami-windows-latest/Windows_Server-2022-English-Full-Base`; `aws_security_group.alongside_box` (name from the sg module, `vpc_id = var.box_vpc_id`, description "Alongside Schwab Box: no standing ingress; RDP via SSM port forwarding", ZERO `ingress` blocks, one `egress` allowing all outbound); `aws_instance.alongside_box` (`ami` from the data source `.value`, `instance_type = var.box_instance_type`, `subnet_id = var.box_subnet_id`, `vpc_security_group_ids`, `iam_instance_profile` = the profile name, `metadata_options { http_tokens = "required" }`, `root_block_device { volume_size = 100, volume_type = "gp3", encrypted = true }`, tags `Name` = the runner module's name, `Device = "Alongside Schwab Box"`, `System = "schwab"`, `Scope = "alongside"`, `Project = "NFRA_SCHWABBF"`, and `lifecycle { prevent_destroy = true, ignore_changes = [ami, user_data] }`). Outputs: `alongside_box_instance_id`, `alongside_box_role_arn`, `alongside_box_security_group_id`.
6. The root contains NO text `49financial`, `08242234`, `08335338` or `08403355` (one writer per master, PRD C-ONEWRITER; the 49F box's masters never appear here).
7. Test `data/canonical/schwab/tests/test_alongside_box_tf.py` reads the `.tf` files as TEXT (no terraform, no network, no AWS), plus `lib/opal_naming.py` and `infra/logic/registry/scopes.json`:
   - BUILDER NAMES (name contains `builder_names`): each of the five module blocks' inputs, passed to `lib/opal_naming.py name(...)`, returns the string listed above; no resource `name =` in the root is a typed string literal except the two secret names and the `Device` tag.
   - IAM GRANTS (name contains `iam_grants`): the write statement lists exactly four per-master resources of the shape above, derived from the map (the four map keys equal the `masters` of the registry `scopes.json` rows whose `firm` is `cottonwood` and `vendor` is `schwab`); no resource equals the bare folder `schwab/cottonwood/bronze/*`; no `s3:GetObject` or `s3:DeleteObject` outside `AlongsideCodeRead`; the secret statements name one ARN each; the three Deny statements exist.
   - SECRETS (name contains `secrets`): two secret resources, the import block for the existing one, `prevent_destroy` on both, no `aws_secretsmanager_secret_version`.
   - BOX INSTANCE (name contains `box_instance`): zero `ingress` blocks, `http_tokens = "required"`, the `Device` tag value, `prevent_destroy`, the lifecycle `ignore_changes` list, the AMI parameter path.
   - ONE WRITER (name contains `one_writer`): none of the four forbidden strings of item 6 appears in any `.tf` file of the root.
   - REGISTRY (name contains `registry`): the master map and the registry rows agree both ways (a master in one and not the other fails).
   - FMT: if `terraform` is on PATH, `terraform fmt -check -recursive` on the folder exits 0; otherwise print `SKIP: terraform not on PATH` and pass (put this arm in a test whose name contains `box_instance`).

### ACCEPTANCE

<criterion id="AL1-a1-AC1" cell_refs="AL-a-1"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_box_tf.py -q -p no:cacheprovider --color=no -k "builder_names or iam_grants"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL1-a1-AC1` -- every name is builder output, and the role's grants are per master, write-only, with the deny planes.

<criterion id="AL1-a1-AC2" cell_refs="AL-a-1"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_box_tf.py -q -p no:cacheprovider --color=no -k "secrets or box_instance"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL1-a1-AC2` -- two metadata-only secrets (one adopted by import), and a labeled instance with no standing ingress.

<criterion id="AL1-a1-AC3" cell_refs="AL-a-1"><invocation>python -m pytest data/canonical/schwab/tests/test_alongside_box_tf.py -q -p no:cacheprovider --color=no -k "one_writer or registry"</invocation><expect>^[0-9]+ passed[ ,]</expect></criterion>
`AL1-a1-AC3` -- the four Cottonwood masters only, matching the registry both ways.

<expected_criteria>AL1-a1-AC1,AL1-a1-AC2,AL1-a1-AC3</expected_criteria>

Dry-run at the base 2026-10-20 (the test file does not exist): all three, "file or directory not found" (rc 4) -- FAIL as expected. Write the test FIRST and run each criterion to see it fail on the missing root files, then build.

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file. Everything else named here you READ and never edit (`canonical-schwab-ec2/`, `canonical-schwab-si2/`, `lib/opal_naming.py`, the registry, the other cell's files).
- **WORLD floor, nothing applied.** No `terraform init/plan/apply`, no `aws` command, no secret value written or read, no deploy. The existing secret `schwab/alongside/sdd-credentials` is named, never read.
- **Refusal clause.** If a criterion cannot be met as written (for example the builder refuses a name, or a statement shape cannot be expressed), stop, write the reason in your report and a surprise row (id `NFRA_SCHWABBF-W11-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing), and do not weaken the test to pass.

<paths>
infra/aws/terraform/alongside-schwab-ec2/main.tf
infra/aws/terraform/alongside-schwab-ec2/masters.tf
infra/aws/terraform/alongside-schwab-ec2/iam.tf
infra/aws/terraform/alongside-schwab-ec2/secrets.tf
infra/aws/terraform/alongside-schwab-ec2/box.tf
data/canonical/schwab/tests/test_alongside_box_tf.py
org/missions/D8/NFRA/NFRA_SCHWABBF/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. Everything else named here you READ and never edit.

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_SCHWABBF/decompositions/NFRA_SCHWABBF_DECOMP_AL1.md</decomp_doc> (Alongside workstream, round 1), cell `AL-a-1`.
<owned_cells>AL-a-1</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: AL1-a1-AC1, AL1-a1-AC2, AL1-a1-AC3. Instance at `org/missions/D8/NFRA/NFRA_SCHWABBF/deliverables/0.9.0_WK_NFRA_SCHWABBF~11/NFRA_SCHWABBF.TO-AL-a1.alongside-box-terraform-root.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> AL1-a1-AC1,AL1-a1-AC2,AL1-a1-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT (your final message):** each file with its line count, the resource addresses you created, the pytest summary lines, the commit hash, any surprise row id.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule in this cell (cell AL-s-1 owns it).
comp-iam: DECLARED-NOT-APPLICABLE as a tool run -- the role is new; the copy-source statements (monolith-iam.tf:36-118, iam.tf:28-121) were read at the cut; BLIND: the live IAM plane (0 roles read).
comp-adversary: DECLARED-NOT-APPLICABLE -- decomposition findings 1 (four masters share one firm folder: per-master file-name grants) and 4 (204-until-entitled) are inlined above.
lane: the <paths> block IS the grant.
</preflight>

Source: PRD v0.5 C-ALONGSIDE, C-NAMES, C-ONEWRITER; decomposition `NFRA_SCHWABBF_DECOMP_AL1.md` cell AL-a-1 and rulings 1-8.
