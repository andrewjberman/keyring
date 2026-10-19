# TO NFRA_FIDUPL.TO-FU-s-6 -- the Terraform root for the Fidelity uploader (plan only)

<to_id>NFRA_FIDUPL.TO-FU-s-6</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~4</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-19</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>fidelity-uploader</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FU-s-6` (`decompositions/NFRA_FIDUPL_DECOMP.md` v1.0) | **outcome_ref:** FWD-1 |
**depends_on:** none (G-1 met)

---

## WORKER FACE

### THE CELL

**FU-s-6** -- The Terraform root beside `canonical-schwab-ec2/`: EventBridge schedule (the three Schwab-window crons), an SSM Automation document that starts the box, runs the wrapper and stops it, the box (Linux, SSM-only, no ingress), the Wealthscape secret (metadata only, `prevent_destroy`), per-secret grants, the box role's write grant on the Fidelity prefix of `opal-data-assets` (no bucket created); names from `name()`; `terraform plan` only. Contract rows: C-TF, C-WINDOW (cron stated, not fixed), PRD ruling (c).

**Read first, in this order:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (the facts, interfaces and handoff contract every cell shares; it is part of your context) and the cell text above. The project is NFRA_FIDUPL: the Fidelity Wealthscape daily export is landed raw every morning with nobody signing in; round 1 builds one thread end to end on fixtures and a few real read-only seams, and FU-x-1 proves the live sign-in.

### WHAT TO BUILD

Build the root `infra/aws/terraform/canonical-fidelity-ec2/` (the directory name follows its sibling `canonical-schwab-ec2/`; every AWS RESOURCE name inside comes from the builder). Read the sibling root first: `main.tf` (provider and the S3 backend pattern: use the same state bucket with key `canonical-fidelity-ec2/tfstate`), `monolith-daily-schedule.tf`, `secrets.tf` and `iam.tf`; and the builder module `infra/aws/terraform/modules/opal_name`.

Resources, each with its name from the HCL builder module (system `fidelity`, scope `alongside`, a function and kind of your choosing; a builder refusal is a surprise row, not a typed name):
1. **The box:** one EC2 instance, Linux (the latest Amazon Linux 2023 AMI by SSM public parameter), a small instance type (t3.medium is the estate's auto-login size), IMDSv2 required, an encrypted root volume, an instance profile, a security group with NO ingress rules and egress open, no key pair, no public-IP requirement beyond what egress to the internet needs. The instance is created stopped-capable (it is started and stopped by the automation below, never left running by this root: do not manage its state field).
2. **The box role:** the AWS-managed SSM core policy attachment; `secretsmanager:GetSecretValue` on the EXACT ARNs of the Wealthscape secret (below) and of the existing `quo/api-key` (look the latter up with a data source by name; do not create it); `s3:PutObject`, `s3:GetObject` and `s3:ListBucket` on the Fidelity landing prefix of `opal-data-assets` only, the prefix taken from `address('fidelity','alongside','bronze','x','20000101')` with the table and date stripped (compute it once with the Python builder and record the string in a comment; the policy ARN must not widen beyond `fidelity/alongside/bronze/*`); `ssm`-agent needs only. NO `*` Resource, NO secret prefix wildcard (the `schwab/*` hazard is named at `canonical-schwab-ec2/secrets.tf:11-13`).
3. **The secret:** `aws_secretsmanager_secret` for the Wealthscape credentials, METADATA ONLY (never an `aws_secretsmanager_secret_version`), with `lifecycle { prevent_destroy = true }`, name from the builder. A human writes its value; this root never does.
4. **The run automation:** an `aws_ssm_document` of type `Automation` that (a) starts the instance, (b) waits for it to be `Online` in SSM, (c) runs `aws:runCommand` AWS-RunShellScript with `python3 /opt/fidelity-uploader/box/run.py`, with a long execution timeout, (d) stops the instance in a final step that runs whether or not (c) failed (use `onFailure: step:<stop step>`). Its assume role is a role this root creates, scoped to start and stop THIS instance only and to SendCommand on the one document and the one instance. If the document cannot express a step, file a surprise row naming it.
5. **The schedule:** three `aws_cloudwatch_event_rule` entries with the Schwab window's crons (read them from `canonical-schwab-ec2/monolith-daily-schedule.tf`: `cron(45 9 * * ? *)`, `cron(15 10 * * ? *)`, `cron(45 10 * * ? *)`), each with a target that starts the automation, and a role EventBridge assumes scoped to `ssm:StartAutomationExecution` on that one document. Mark the crons PROVISIONAL in a comment (Fidelity's generation hour is unmeasured until the 2026-10-20 status rows). The rules are created ENABLED = false until a human enables them (state `DISABLED`), so applying the root causes no scheduled run.
6. **Outputs:** the instance id, the document name, the secret id (pointer), the role ARN.
No bucket, no SNS topic, no CloudWatch alarm, no Lambda. All files ASCII.

### ACCEPTANCE

<criterion id="FU6-AC1" cell_refs="FU-s-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu6v</invocation><expect>R1-FU6V-OK Success! The configuration is valid\.</expect></criterion>
`FU6-AC1` -- the root initialises without a backend and validates.

<criterion id="FU6-AC2" cell_refs="FU-s-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu6g</invocation><expect>R1-FU6G-OK no ingress</expect></criterion>
`FU6-AC2` -- no ingress, no wildcard secret grant, no secret version, prevent_destroy present.

<criterion id="FU6-AC3" cell_refs="FU-s-6"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu6p</invocation><expect>R1-FU6P-OK Plan: \d+ to add, 0 to change, 0 to destroy\.</expect></criterion>
`FU6-AC3` -- the plan against the real backend only adds.

<expected_criteria>FU6-AC1,FU6-AC2,FU6-AC3</expected_criteria>

Dry-run at the base (HEAD of box/dell1 at the cut): `FU6-AC1` base: FAIL as expected.
Dry-run at the base (HEAD of box/dell1 at the cut): `FU6-AC2` base: FAIL as expected.
Dry-run at the base (HEAD of box/dell1 at the cut): `FU6-AC3` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder. Everything else named here you READ.
- **Fixtures only.** Tests use SYNTHETIC data. The real Wealthscape export files hold client names and account numbers and are never read into a test, a log or a commit.
- **No secret, no alert.** No secret value anywhere (file, log, environment, command line, surprise row); no SNS, SES or notification of any kind.
- **Refusal clause.** A builder refusal (`address()` or `name()`): add nothing typed; file a surprise row (`NFRA_FIDUPL-D1-W<n>-S<k>`, next unused across every document under `surprise-channel/`) and stop that piece. A premise that fails against live state is a surprise row too, never a guess.
- **ASCII and Python 3.9 syntax** in every file (reference section 1).
- **PLAN ONLY.** You never run `terraform apply` or `safe-apply`. `terraform init` and `plan` are read operations against the state backend and AWS; run them only through the criterion invocations. Do not create, change or delete any AWS object.

Reads (outside the grant):
- `infra/aws/terraform/canonical-schwab-ec2/` (the sibling root)
- `infra/aws/terraform/modules/opal_name/`
- `infra/aws/terraform/bd-pipeline/bd-49f-session-chain.tf` lines 44-60 (a staggered start-on-demand chain)
- `infra/aws/ec2/EC2_MANIFEST.json` (the `cot-exporter` entry: stopped between runs)
- `lib/opal_naming.py`

<paths>
infra/aws/terraform/canonical-fidelity-ec2/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention).

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP.md</decomp_doc> (round 1), cell `FU-s-6`.
<owned_cells>FU-s-6</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FU6-AC1,FU6-AC2,FU6-AC3. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~4/NFRA_FIDUPL.TO-FU-s-6.terraform-root.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FU6-AC1,FU6-AC2,FU6-AC3` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, each check line verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- thread round; the lens runs on the enrichment round that touches the schedule (FWD-2); denominator 0 schedules created by this order; the schedule is created DISABLED, so no run is scheduled.
comp-iam: RUN at the drain -- BLIND to the root today (it does not exist); the issuer prints the denominator over the written root's grants, and this order carries the six grant limits in step 2 above as the bars.
comp-adversary: DECLARED-NOT-APPLICABLE -- thread round; runs on the enrichment round that touches this surface.
lane: the paths block.
</preflight>

Source: PRD v0.4.3 (@37a9865739) and the CTO's rulings through msg 8514; decomposition round 1 cell FU-s-6; worker reference.
