# TO IRPT_BCKEND.TO-IB-hm-8 -- DECLARE in Terraform (no apply) the narrow role the HMAC list stage assumes, its two-statement policy, the one Secrets Manager secret CONTAINER, and the three environment variables the directory refresh Lambda hands to its builds (CTO rulings msg 10203 and 10234; rule 30)

<to_id>IRPT_BCKEND.TO-IB-hm-8</to_id>
<project>IRPT_BCKEND</project>
<issued_to>0.9.0_WK_IRPT_BCKEND~454</issued_to>
<issued_by>2.0.0_SA_COO~P2</issued_by>
<issued_date>2026-10-17</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>10</round>
<workstream>~PM</workstream>

**Directive:** D9 | **Fabric:** dell2 | **Decomp cell:** `IB-hm-8` (decomposition section 246) | **outcome_ref:** FWD-21 | **Ordered by:** the CTO's rulings: msg 10203 (the HMAC list is written to ONE key per firm, `address()` output), msg 10234 (B: a narrow role holding `secretsmanager:GetSecretValue` on the one secret and `s3:PutObject` on the three firm keys, trusted by the host's role only; the host profile gains only `sts:AssumeRole` on that role; the honest wording: any job on the host can assume it, so B buys CloudTrail attribution and one place to revoke, not isolation), CLAUDE.md rule 30, and the builder outputs recorded in `deliverables/2.0.0_SA_COO~P2/IB-hm-3_BUILDER_OUTPUTS_FOR_THE_HMAC_LIST_20261017.md`. **This order DECLARES; it never applies.** The apply is a separate WORLD order to `0.7.0_AE_CloudOps~IB2` under a signed never-widen pair.

---

## WORKER FACE

**Cell `IB-hm-8` (inlined).** The Terraform root `infra/aws/terraform/investor-reporting/directory` already holds the precedent for exactly this shape: `principal_49f.tf` declares a narrow role the daily-runner HOST assumes for one firm (names from the `opal_name` module, never typed; trust only the host role's ARN, derived from the EC2 manifest; a header that states the never-widen class and that the apply is a separate signed order). **Mirror it** in a NEW file `infra/aws/terraform/investor-reporting/directory/hmac_list_stage.tf` (and ONE additive edit to `schedule.tf`'s Lambda environment map):

1. **Names.** Two `module "..." { source = "../../modules/opal_name" ... }` blocks: `system = "irpt"`, `function = "hmac-list-stage"`, `kind = "role"` and `kind = "policy"`, NO scope (the earlier worker measured `name("irpt", None, "hmac-list-stage", "role")` = `irpt-hmac-list-stage-role` and the policy `irpt-hmac-list-stage-policy`). Read `infra/aws/terraform/modules/opal_name/variables.tf` first. The secret's name `irpt/hmac-list/key` has no builder and no module (the grader accepts it and a registry row is refused as redundant, see the builder-outputs file): write it as a `locals` literal with a comment that cites `n.grade("irpt/hmac-list/key", "SECRET")` returning `CONFORMANT`.
2. **The secret CONTAINER.** `resource "aws_secretsmanager_secret"` named by that local, with a description. **NO `aws_secretsmanager_secret_version` anywhere in the root and NO secret value in any file**: the value is generated and put once by the apply order, never by Terraform (state would hold it).
3. **The role.** `aws_iam_role` named by the role module, trust policy with ONE principal: `local.irpt_runner_role_arn` (defined in `principal_49f.tf`, the host role, derived from the EC2 manifest) and nothing else; no wildcard, no condition-less service principal.
4. **The policy.** `aws_iam_role_policy` named by the policy module with exactly TWO statements: `ReadTheOneHmacSecretOnly` (`secretsmanager:GetSecretValue`, resource = the secret's ARN) and `PutTheThreeFirmListKeysOnly` (`s3:PutObject`, resources = the three object ARNs of the three per-firm list keys). **No other action, no `"*"` resource anywhere in this file.** The three keys come from the recorded builder outputs `s3://opal-data-assets/globgrph/<firm>/silver/account_id_list/hmac` for the three firms of `data/firm_registry.json` (kind client): derive the firm tokens in Terraform from the registry the same way `principal_49f.tf` does (`module.irpt_scopes`), and compose each URI by the builder's pattern in ONE `locals` map, with a comment citing the builder call; the check re-runs the builder for the three firm tokens and requires the strings in your file to equal its results EXACTLY.
5. **The environment (additive).** In `schedule.tf`, in the directory refresh Lambda's environment variable map (about lines 152 to 166), add THREE keys: `IRPT_HMAC_SECRET_ID` (the secret's name), `IRPT_HMAC_ROLE_ARN` (BUILT from the account id and the role module's name, the way `irpt_49f_directory_read_role_arn` is, not read back from the resource) and `IRPT_HMAC_LIST_URI_MAP` (`jsonencode` of the `{firm_id: uri}` map). No existing key changes.
6. **The host side.** The earlier READ found no `sts:AssumeRole` statement on the host role in this root. In the same account a trust policy that names the host role's ARN grants the assume by itself, but a permission boundary or a service control policy may require the identity policy too. **Do NOT edit any file outside this root.** Read how the host role's identity policy is written for the 49F source role (search `infra/aws/terraform/mdpf-pipeline/iam.tf` for the 49F principal and for `sts:AssumeRole`) and record in your notes whether the host role needs an added `sts:AssumeRole` statement on the new role's ARN, in which file, and the exact statement. If it does, that is a SEPARATE cell: report it, do not write it.
7. **The header.** The file header states, in plain words: it declares a NEVER-WIDEN-class act, the apply is a separate order after both signed halves, the role is assumable by any job on the shared host (so the role buys attribution and one place to revoke, not isolation), no value is held anywhere in Terraform, and the three keys hold keyed HMACs only.

**Do, in this order:**
1. Read `principal_49f.tf` whole, the `opal_name` module, `schedule.tf` lines 140 to 215 (the Lambda environment map and locals), the builder-outputs file, and `data/firm_registry.json`.
2. Write the file and the one edit. If `.tools/terraform.exe` exists in your worktree and runs offline, run `terraform fmt -check -diff` on the two files and record the result; do not run `init`, `plan` or `apply` (no AWS call of any kind).
3. Run the three criteria below from the repository root, each under `timeout 300` (AC3 reads `HEAD~1..HEAD`: run it AFTER your one commit). Record AC1 and AC2 output verbatim in `deliverables/0.9.0_WK_IRPT_BCKEND~454/IBhm8_criteria_output.txt` BEFORE the commit; write the proof instance named under proof_of_spec and validate it with `python .tools/proof-of-spec-check.py <instance>`; write `IBhm8_notes.md` (the host-side finding of step 6, the fmt result, anything odd).
4. **ONE commit** with explicit paths (`.tools/safe-commit.sh --author "0.9.0_WK_IRPT_BCKEND~454 <0.9.0_WK_IRPT_BCKEND~454@opal.agent>" -F <msgfile> -- <paths>`, the message file written by the Write tool): `hmac_list_stage.tf`, `schedule.tf`, your deliverables folder and any surprise row. If safe-commit is slow it is waiting on other seats: wait, never run it twice at once, never amend. Do not push. Report once, under 150 words.

**Criteria (run each under `timeout 300` from the repository root):**

<criterion id="IBHM8-AC1" cell_refs="IB-hm-8"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r251/p251_cells.py" . IBHM8-AC1</invocation><expect>IBHM8-AC1 PASS</expect></criterion>
<criterion id="IBHM8-AC2" cell_refs="IB-hm-8"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r251/p251_cells.py" . IBHM8-AC2</invocation><expect>IBHM8-AC2 PASS</expect></criterion>
<criterion id="IBHM8-AC3" cell_refs="IB-hm-8"><invocation>python "org/missions/D9/IRPT/IRPT_BCKEND/deliverables/2.0.0_SA_COO~P2/checks/r251/p251_cells.py" . IBHM8-AC3</invocation><expect>IBHM8-AC3 PASS</expect></criterion>

<expected_criteria>IBHM8-AC1, IBHM8-AC2, IBHM8-AC3</expected_criteria>

What the checks grade: AC1 the declaration by static markers (the two name modules, the secret container with NO secret version in the root, the role's single trust principal, the policy's two statements with exactly the two actions and no `"*"` resource, the three environment keys in `schedule.tf`); AC2 the three list-key URIs in your file equal what `lib/opal_naming.py address()` returns for the three firm tokens, re-run by the check; AC3 your ONE commit touches only the new `.tf`, `schedule.tf` and this order's paths. The plan and the apply are the next orders'. Do not edit the checks.

## BOUNDS

- **Grant:** create `infra/aws/terraform/investor-reporting/directory/hmac_list_stage.tf`; ONE additive edit to `schedule.tf` (the three environment keys); write `deliverables/0.9.0_WK_IRPT_BCKEND~454/`; the surprise channel for rows. **NO terraform init, plan or apply; NO AWS call; NO file outside the root except your deliverables and rows; NO secret value, key material or real id; NO change to any existing resource, statement or environment key; NO push.**
- **Refusal clause:** STOP and report, writing nothing further, if the host role ARN cannot be derived as `principal_49f.tf` derives it, if the `opal_name` module refuses the role or policy name, or if a builder call for a firm key returns a different address than the recorded one. File a surprise ROW for anything odd and keep working; a broker message is never the carrier.

<paths>
infra/aws/terraform/investor-reporting/directory/
org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~454/
org/missions/D9/IRPT/IRPT_BCKEND/surprise-channel/investigations/INVESTIGATION_v1.md
org/missions/D9/IRPT/IRPT_BCKEND/task-orders/IRPT_BCKEND.TO-IB-hm-8.declare-the-hmac-list-stage-role-secret-and-env.md
</paths>

<decomp_ref>
<decomp_doc>org/missions/D9/IRPT/IRPT_BCKEND/decompositions/IRPT_BCKEND_DECOMP.md</decomp_doc> section 246 (round 10, workstream ~PM), cell `IB-hm-8`.
<owned_cells>IB-hm-8</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: IBHM8-AC1, IBHM8-AC2, IBHM8-AC3. The instance goes at `org/missions/D9/IRPT/IRPT_BCKEND/deliverables/0.9.0_WK_IRPT_BCKEND~454/IRPT_BCKEND.TO-IB-hm-8.declare-the-hmac-list-stage-role-secret-and-env.proof_of_spec.json` (the file stem of THIS order plus `.proof_of_spec.json`).
Record in it the order's own relative invocation for each criterion. Validate it with `python .tools/proof-of-spec-check.py <instance>` BEFORE the flip to complete.
</proof_of_spec>

---

## RECORD FACE

<preflight>
comp-blast: RUN -- DECLARES a new secret container, a new narrow role with a two-statement policy and three additive Lambda environment keys; NOTHING is applied by this order (no init, no plan, no apply); the apply is a later WORLD order under a never-widen pair that states the plan (new resources only, plus the one changed Lambda environment) and both branches. The role is assumable by any job on the shared host: attribution and one place to revoke, not isolation (CTO ruling B).
comp-iam: RUN -- the role's trust is the host role ARN only; its policy is GetSecretValue on one ARN and PutObject on three keys; no wildcard; the host-role identity statement, if one is needed, is a separate cell (step 6 reports it).
comp-routes: DECLARED-NOT-APPLICABLE -- no route is touched.
comp-schedule: DECLARED-NOT-APPLICABLE -- no schedule is touched (only the Lambda's environment map gains keys).
comp-cache: DECLARED-NOT-APPLICABLE -- no cache surface is touched.
comp-adversary: RUN -- p251_cells.py IBHM8 dry-run at base on dell2 2026-10-17 ~05:3xZ: AC1, AC2, AC3 FAIL. Positive control (control251.py) over synthetic git repos with a stub naming module: the three positives PASS and each negative (a missing name module, the secret container missing, a secret version present, a trust principal that is not the host role local or has a second principal, a third policy statement, an extra action, a wildcard resource, a missing environment key, a second sts:AssumeRole, a list-key URI that differs from the builder result, a firm token typed as a literal, either .tf file or an outside file wrong in the commit) fails its own arm. NOT measured by me: Terraform syntax validity beyond what the worker's fmt run shows, the plan, the host-role identity statement, anything live.
lane: the paths block IS the grant; worker `0.9.0_WK_IRPT_BCKEND~454`. Class WORLD (the gate's floor for an infra path; this order declares and applies nothing).
</preflight>
