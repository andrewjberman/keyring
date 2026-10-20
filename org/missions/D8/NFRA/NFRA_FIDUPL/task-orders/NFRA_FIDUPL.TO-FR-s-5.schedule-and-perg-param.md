# TO NFRA_FIDUPL.TO-FR-s-5 -- the Terraform root: schedule switch and the per-G list parameter

<to_id>NFRA_FIDUPL.TO-FR-s-5</to_id>
<project>NFRA_FIDUPL</project>
<issued_to>0.9.0_WK_NFRA_FIDUPL~6</issued_to>
<issued_by>2.0.0_SA_COO~P1</issued_by>
<issued_date>2026-10-20</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>2</round>
<workstream>fidelity-perg</workstream>

**Directive:** D8 | **Fabric:** dell1 | **Decomp cell:** `FR-s-5` (`decompositions/NFRA_FIDUPL_DECOMP_R2.md` v1.0) | **outcome_ref:** FWD-9, C-BACKFILL |
**depends_on:** none (built against fakes; interfaces in worker reference section 11)

---

## WORKER FACE

### THE CELL

**FR-s-5** -- The schedule and the per-G list home in the Terraform root: a `schedule_enabled` variable (default false) controlling the three rules' state, the SSM SecureString parameter for the per-G list (name from the builder, value ignored after creation) and the box role's read grant on that one parameter; plan only. Contract rows: C-TF, C-WINDOW, CTO msg 8637.

**Read first, in this order:** `org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_R1_WORKER_REFERENCE.md` (sections 1 and 11 bind you; the rest is context) and the cell text above. Project NFRA_FIDUPL: the Fidelity Wealthscape daily export is landed raw every morning; round 2 splits it per firm by G number, backfills history per G number, and schedules it. You build against fakes; nothing here runs live.

### WHAT TO BUILD

Edit `infra/aws/terraform/canonical-fidelity-ec2/` (APPLIED in round 1: read every file first; the box, role, secret, automation and three disabled rules exist). PLAN ONLY: never apply.

1. `variables.tf` (new or existing): `variable "schedule_enabled" { type = bool, default = false }`. In `schedule.tf` the three `aws_cloudwatch_event_rule` entries take `state = var.schedule_enabled ? "ENABLED" : "DISABLED"`. With the default the rules do not change.
2. `perg.tf` (new): one `aws_ssm_parameter`, `type = "SecureString"`, for the per-G list; its NAME from the HCL builder module (system `fidelity`, scope `alongside`); a placeholder value that is not a G number (for example the text `UNSET`); `lifecycle { ignore_changes = [value] }` so a human or the executor writes the real value once and Terraform never touches it. Per CTO msg 8637 no G number goes in git, a tfvars file or Terraform state. If the builder refuses a name for a parameter, file a surprise row and stop that piece.
3. The box role gains `ssm:GetParameter` on that ONE parameter's ARN (no wildcard, no `ssm:GetParametersByPath`); add the statement to the existing role policy. The IAM guard check (`fu6g`) must stay green: any Resource star keeps its `# STAR-OK:` comment.
4. An output `perg_parameter_name`. The one added resource is the parameter; the plan also shows the changed role policy.
Mechanical bars: the root validates (reuse FU6-AC1's check), the guard stays green, and the plan reads exactly `Plan: 1 to add, 1 to change, 0 to destroy.` with the one add being the SSM parameter (check `fr5p`).

### ACCEPTANCE

<criterion id="FR5-AC1" cell_refs="FR-s-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu6v</invocation><expect>R1-FU6V-OK Success! The configuration is valid\.</expect></criterion>
`FR5-AC1` -- the root still initialises without a backend and validates.

<criterion id="FR5-AC2" cell_refs="FR-s-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fu6g</invocation><expect>R1-FU6G-OK no ingress</expect></criterion>
`FR5-AC2` -- no ingress, no wildcard secret grant, no secret version, prevent_destroy present, every Resource star annotated.

<criterion id="FR5-AC3" cell_refs="FR-s-5"><invocation>python org/tier1_exec/2.0.0_SA_COO/deliverables/NFRA_FIDUPL_R1/R1_CHECKS/r1_checks.py fr5p</invocation><expect>R1-FR5P-OK Plan: 1 to add, 1 to change, 0 to destroy\.</expect></criterion>
`FR5-AC3` -- the plan adds only the SSM parameter and changes only the box role policy.

<expected_criteria>FR5-AC1,FR5-AC2,FR5-AC3</expected_criteria>

Dry-run at the base (HEAD of box/dell1 at the cut): `FR5-AC1` base: PASS as expected (a regression guard on round 1); `FR5-AC2` base: PASS as expected (a regression guard on round 1); `FR5-AC3` base: FAIL as expected.

## BOUNDS

- **Grant.** The `<paths>` block below, this order's file and your deliverables folder. Everything else named here you READ.
- **Fixtures only.** Every test uses SYNTHETIC data and fakes; no network, no AWS, no live call. G numbers and account numbers in tests are made up and are never real ones.
- **No secret, no alert; no G number, account number or firm label in any output.** Counts and booleans only (reference section 11).
- **Refusal clause.** A builder refusal (`address()` or `name()`): add nothing typed; file a surprise row (`NFRA_FIDUPL-D1-W<n>-S<k>`, `<n>` your slot, `<k>` next unused across the investigation file) and stop that piece. A premise that fails is a row too, never a guess.
- **ASCII and Python 3.9 syntax** in every file (reference section 1).
- **PLAN ONLY.** Never run `terraform apply` or `safe-apply`; `init` and `plan` only through the criterion invocations. The CloudOps seat applies later by its own order.

Reads (outside the grant):
- `infra/aws/terraform/modules/opal_name/`
- `lib/opal_naming.py`
- `infra/aws/terraform/canonical-schwab-ec2/` (the sibling root)

<paths>
infra/aws/terraform/canonical-fidelity-ec2/
org/missions/D8/NFRA/NFRA_FIDUPL/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant (your deliverables folder is granted by the tree convention).

<decomp_ref>
<decomp_doc>org/missions/D8/NFRA/NFRA_FIDUPL/decompositions/NFRA_FIDUPL_DECOMP_R2.md</decomp_doc> (round 2), cell `FR-s-5`.
<owned_cells>FR-s-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: FR5-AC1,FR5-AC2,FR5-AC3. Instance at `org/missions/D8/NFRA/NFRA_FIDUPL/deliverables/0.9.0_WK_NFRA_FIDUPL~6/NFRA_FIDUPL.TO-FR-s-5.schedule-and-perg-param.proof_of_spec.json`, validated with `python .tools/proof-of-spec-check.py <instance> FR5-AC1,FR5-AC2,FR5-AC3` BEFORE the flip. Commit code first, then pin.
</proof_of_spec>

**REPORT:** what was built and where, any address or name with its builder call, the test names, each check line verbatim, every surprise row id, commits.

---

## RECORD FACE

<preflight>
comp-schedule: RUN at the drain -- the three rules' state variable; BLIND to live rules (none changes with the default); the issuer prints the plan denominator.
comp-iam: RUN at the drain -- one read grant on one parameter; BLIND to the root's computed names; the issuer prints the denominator.
comp-adversary: DECLARED-NOT-APPLICABLE -- build round on fakes; runs when the live round touches this surface.
lane: the paths block.
</preflight>

Source: CTO msg 8663 (PRD v0.4.5 @e4bb46835e); Andrew-direct @b329e1c5f3; decomposition round 2 cell FR-s-5; worker reference section 11.
