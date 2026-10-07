# TO NFRA_CTLPLN.TO-CT-c-5 -- round 3 CT-c-5: the Lambda narrowing -- each Dell updates only its projects' functions; protected functions denied

<to_id>NFRA_CTLPLN.TO-CT-c-5</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~4</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>staged</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-c-5` (`decompositions/NFRA_CTLPLN_DECOMP.round3.md`) | **outcome_ref:** FWD-10 |
**depends_on:** CT-c-1, CT-c-3 (the statements it edits) -- both merged before this order is handed

**STAGED ON A RULING.** This order is cut on `1.0.0_SA_CTO`'s msg 105969 as written. The decomposition's "Open at the CTO" item 1 asks
whether the scope is named ARNs, a project name prefix, or the explicit Deny alone. The issuer amends this face to the ruled form
before it is handed; a worker never starts it while `<status>` reads `staged`.

---

## WORKER FACE

### THE CELL

`CT-c-5`, FWD-10, the CTO's ruling (msg 105969): "the narrowing -- Lambda deploy actions scoped to named function ARNs of the projects
placed on each Dell, plus an explicit Deny on the auth, IAM-adjacent and security-sweep functions." Today
`dell_deploy_policy.json` allows `lambda:UpdateFunctionCode`, `lambda:UpdateFunctionConfiguration`, `lambda:PublishVersion`,
`lambda:CreateAlias`, `lambda:UpdateAlias` and `lambda:InvokeFunction` on `Resource: "*"` for both Dells. You narrow it and prove it by
derivation and simulation. You APPLY NOTHING.

**Build:**

1. `tests/derive_lambda_scope.py` -- the derivation.
   - Per Dell, the placed projects (`project.json` `placement` `DELL1` / `DELL2`, `status` not `closed`) and their Terraform roots,
     by the SAME method as `tests/derive_resource_kinds.py` (import it; do not write the method twice).
   - Per root, every `aws_lambda_function`'s `function_name` that is a literal string or resolves from literals in the same root; a
     name the script cannot resolve is printed as `UNRESOLVED <root> <resource address>` and counted.
   - The PROTECTED set: every function declared in root `portal-auth`, plus every function in any root whose name matches, on a word
     boundary and case-insensitive, `auth`, `authorizer`, `iam`, `credential`, `secret`, `security`, `sweep`, `guard`, `kms`, `sso`,
     `cognito`. Print each protected function with the rule that caught it.
   - A function both placed and protected is PROTECTED (the Deny wins) and printed as `PLACED-BUT-PROTECTED`.
   - LAST line `LAMBDA-SCOPE dell1_functions=<a> dell2_functions=<b> protected=<p> unresolved=<u> unscoped_update_statements=<s> ok=<True|False>`,
     where `s` counts Allow statements in the Dell policies that carry a Lambda update action on `Resource: "*"`; `ok=True` only when
     `s == 0`.
2. The policies. Remove the six Lambda actions from the group policy's `*` statement. Add one per-Dell managed policy,
   `dell1_lambda_policy.json` and `dell2_lambda_policy.json`, names `cloudops-dell1-agent-lambda-policy` and
   `cloudops-dell2-agent-lambda-policy` (`lib/opal_naming.name('cloudops', None, 'dell1-agent-lambda', 'policy')`), tagged
   `DisplayName = "DellBoxes"`, attached to that Dell's user only: Allow the six actions on that Dell's derived function ARNs
   (`arn:aws:lambda:us-east-1:313476888478:function:<name>` and `...:<name>:*`). Add to the group's deploy policy one statement
   `DenyProtectedFunctions`: Effect Deny, every `lambda:` write (`lambda:Update*`, `lambda:Publish*`, `lambda:Create*`,
   `lambda:Delete*`, `lambda:Put*`, `lambda:Add*`, `lambda:Remove*`, `lambda:Tag*`, `lambda:Untag*`) on the protected ARNs. Every
   policy document stays under 6,144 characters without whitespace; if a Dell's list does not fit, split it into two policies named by
   the builder and say so.
3. `tests/simulate_lambda_scope.py` -- per Dell, its effective set in one `simulate_custom_policy` call: `lambda:UpdateFunctionCode` on
   one of its own functions -> allowed (2 arms, one per Dell); on one of the OTHER Dell's functions -> denied (2 arms); on three
   protected functions (one from `portal-auth`, two caught by name) -> denied for dell1 (3 arms). LAST line
   `LAMBDA-SIM own_allowed=<a>/2 other_box_denied=<b>/2 protected_denied=<c>/3 all_ok=<True|False>`.
4. `tests/check_identity.py` -- the name comparison covers the two new policies.

### ACCEPTANCE

<criterion id="CT3c5-AC1" cell_refs="CT-c-5"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/derive_lambda_scope.py</invocation><expect>unscoped_update_statements=0 ok=True</expect></criterion>
`CT3c5-AC1` -- no Dell policy carries a Lambda update action on every function.

<criterion id="CT3c5-AC2" cell_refs="CT-c-5"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_lambda_scope.py</invocation><expect>LAMBDA-SIM own_allowed=2/2 other_box_denied=2/2 protected_denied=3/3 all_ok=True</expect></criterion>
`CT3c5-AC2` -- each Dell updates its own project's function, not the other Dell's, and never a protected one.

<criterion id="CT3c5-AC3" cell_refs="CT-c-5"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py</invocation><expect>denied_ok=17/17 passrole_ok=5/5</expect></criterion>
`CT3c5-AC3` -- the control: the earlier cells' denials and the PassRole arms still hold. The allowed count of that matrix changes with
this cell (its `lambda:UpdateFunctionCode` arm moves to a named function); update that one arm and report the new allowed total.

<expected_criteria>CT3c5-AC1,CT3c5-AC2,CT3c5-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **No apply, no IAM write.** The only AWS call allowed is `iam:SimulateCustomPolicy` (read-only).
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
infra/aws/terraform/nfra-ctlpln-identity/iam.tf
infra/aws/terraform/nfra-ctlpln-identity/dell_deploy_policy.json
infra/aws/terraform/nfra-ctlpln-identity/dell1_lambda_policy.json
infra/aws/terraform/nfra-ctlpln-identity/dell2_lambda_policy.json
infra/aws/terraform/nfra-ctlpln-identity/dell*_lambda_*.json
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_lambda_scope.py
infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_lambda_scope.py
infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py
infra/aws/terraform/nfra-ctlpln-identity/tests/check_identity.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `tests/derive_resource_kinds.py`, `tests/render_passrole.py`,
`dell_create_policy.json`, the bus policies, `lib/opal_naming.py`, every `project.json`, and the `.tf` files of the derived roots.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round3.md</decomp_doc> (round 3), cell `CT-c-5`.
<owned_cells>CT-c-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT3c5-AC1, CT3c5-AC2, CT3c5-AC3. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~4/NFRA_CTLPLN.TO-CT-c-5.lambda-scope-narrowing.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT3c5-AC1,CT3c5-AC2,CT3c5-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three last lines; per Dell the function count and the unresolved names; the full protected list with the rule that
caught each; every `PLACED-BUT-PROTECTED` function; each policy's character count; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: RUN at the cut by the simulation criteria (CT3c5-AC2, CT3c5-AC3); `comp-iam gaps` after the apply is the issuer's.
comp-adversary: RUN -- a Dell replacing the code of an authorizer or a credential-handling function (explicit Deny on the protected set, which overrides every Allow including CT-c-1's create actions); one Dell deploying over the other's project (per-user policies); a protected function missed by the name rule (the worker prints the full list for the CTO's read; the rule is word-boundary and stated on the face); BLIND: a function a Dell creates after this apply is in no named list -- the decomposition's "Open at the CTO" item 1, which is why this order is staged.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO msg 105969 (copied in `0.0.0_AB_MSTR` msg 105970), msg 105973, PRD v0.8 ADDENDUM v0.7 ("The Lambda narrowing follows it");
decomposition round 3. Base dry-run at the cut: CT3c5-AC1 and CT3c5-AC2 base FAIL as expected (no file); CT3c5-AC3 base FAIL as
expected (prints no `passrole_ok` before CT-c-3).
