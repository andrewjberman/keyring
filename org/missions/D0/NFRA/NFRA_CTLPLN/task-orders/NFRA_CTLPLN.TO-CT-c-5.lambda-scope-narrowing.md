# TO NFRA_CTLPLN.TO-CT-c-5 -- round 3 CT-c-5: the Lambda narrowing -- an explicit Deny on the functions that decide access; allow elsewhere

<to_id>NFRA_CTLPLN.TO-CT-c-5</to_id>
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

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-c-5` (`decompositions/NFRA_CTLPLN_DECOMP.round3.md`) | **outcome_ref:** FWD-10 |
**depends_on:** CT-c-1, CT-c-3 (the statements it edits) -- both merged before this order is handed

**RULED (AMENDMENT 1, 2.0.0_SA_COO~C, 2026-10-07 ~06:5xZ).** `1.0.0_SA_CTO` msg 106008: "the explicit Deny alone. It supersedes msg
105969's named-ARN scope." The face below is the ruled form. Gate limb: none graded this modification (LIMB 6 grades new orders only;
the order declares no `<placeholders>`). The order stays `staged` until it is handed.

---

## WORKER FACE

### THE CELL

`CT-c-5`, FWD-10, the CTO's ruling (msg 106008): "Deny Lambda code and configuration updates on the functions that decide access
(authorizers, the edge auth validator, user and key management), the list derived by census of the live functions and printed with its
denominator; allow elsewhere." Reason on the record: a Dell waits on no other box, and a named-function allow would make every new
function wait on an IAM apply. So the Allow on `Resource: "*"` STAYS; you add one explicit Deny on a derived list and prove it by census
and simulation. You APPLY NOTHING.

**Build:**

1. `tests/derive_protected_functions.py` -- the census, with `--live` (default) and `--from-file <json>` (a saved listing, for the
   bounded run).
   - `--live` lists every Lambda function in the account with the repo's `.tools/aws` shim (`lambda list-functions`, auto-paginated;
     count client-side) in EVERY region `ec2 describe-regions` returns, and prints the per-region count. A region where the call is
     refused is printed as `REFUSED <region>`, never as zero. The denominator is the total listed.
   - PROTECTED = a function that decides access, by a rule table inside the script (the table is the record): (a) every function that
     is the target of an API Gateway authorizer (`apigatewayv2 get-authorizers` per API; `apigateway get-authorizers` per REST API);
     (b) every function associated with a CloudFront distribution as Lambda@Edge (`cloudfront list-distributions`, the
     `LambdaFunctionAssociations` of every behaviour); (c) every function whose name matches, on a word boundary and case-insensitive,
     `auth`, `authorizer`, `authz`, `login`, `signin`, `sso`, `cognito`, `user`, `users`, `apikey`, `api-key`, `credential`, `token`,
     `session`, `mfa`, `password`. Print every protected function with the rule that caught it, and print separately every function
     rule (c) caught that neither (a) nor (b) did, as `NAME-ONLY`, for the CTO's read.
   - `--write` saves the sorted protected ARNs to `protected_functions.json` beside the policies and renders the Deny statement of
     step 2; `--check` compares both to a fresh census and writes nothing.
   - LAST line `PROTECTED-CENSUS functions=<n> regions=<r> refused_regions=<x> protected=<p> by_authorizer=<a> by_edge=<e> name_only=<m> in_sync=<True|False> ok=<True|False>`;
     `ok=True` only when `p > 0`, `refused_regions == 0` and the files are in sync.
2. The policy. `dell_deploy_policy.json` gains ONE statement `DenyProtectedFunctions`: Effect Deny; Action `lambda:UpdateFunctionCode`,
   `lambda:UpdateFunctionConfiguration`, `lambda:PublishVersion`, `lambda:CreateAlias`, `lambda:UpdateAlias`, `lambda:DeleteFunction`,
   `lambda:DeleteAlias`, `lambda:PutFunctionConcurrency`, `lambda:UpdateFunctionUrlConfig`, `lambda:CreateFunctionUrlConfig`;
   Resource = each protected ARN and the same ARN with `:*`. The statement is RENDERED from `protected_functions.json` by the script,
   never typed. Nothing else in any policy changes. If the document passes 6,144 characters without whitespace, put the statement in
   its own managed policy `dell_protect_policy.json`, name from `lib/opal_naming.name('cloudops', None, 'dell-agent-protect',
   'policy')`, attached to the group in `iam.tf`, and say so.
3. `tests/simulate_policy.py` -- add a third block on the real files: `lambda:UpdateFunctionCode` and
   `lambda:UpdateFunctionConfiguration` on three protected functions read from `protected_functions.json` (one caught by each rule
   where the census has one; say which rules had none) -> denied, 6 arms; `lambda:UpdateFunctionCode` on a function that is NOT
   protected, read from the census -> allowed, 1 arm; `lambda:CreateFunction` on a new name -> allowed, 1 arm. The first two blocks
   stay and must still hold. LAST line
   `POLICY-SIM allowed_ok=21/21 denied_ok=18/18 passrole_ok=5/5 protected_ok=8/8 all_ok=<True|False>`.

### ACCEPTANCE

<criterion id="CT3c5-AC1" cell_refs="CT-c-5"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/derive_protected_functions.py --check</invocation><expect>refused_regions=0</expect></criterion>
`CT3c5-AC1` -- the census reached every region it listed. Record the whole last line; `in_sync=True ok=True` on it is part of the bar
and you state it in the proof row.

<criterion id="CT3c5-AC2" cell_refs="CT-c-5"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py</invocation><expect>passrole_ok=5/5 protected_ok=8/8 all_ok=True</expect></criterion>
`CT3c5-AC2` -- a Dell cannot change the code or configuration of a function that decides access, still updates an ordinary function
and still creates a new one; the earlier cells' arms hold.

<criterion id="CT3c5-AC3" cell_refs="CT-c-5"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/check_identity.py</invocation><expect>policy_size_ok=True ok=True</expect></criterion>
`CT3c5-AC3` -- the control: the root validates, names are the builder's and every policy document fits the limit with the new statement.

<expected_criteria>CT3c5-AC1,CT3c5-AC2,CT3c5-AC3</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>
infra/aws/terraform/nfra-ctlpln-identity/iam.tf
infra/aws/terraform/nfra-ctlpln-identity/dell_deploy_policy.json
infra/aws/terraform/nfra-ctlpln-identity/dell_protect_policy.json
infra/aws/terraform/nfra-ctlpln-identity/protected_functions.json
infra/aws/terraform/nfra-ctlpln-identity/protected_functions_listing.json
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_protected_functions.py
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

**REPORT:** the three last lines; the per-region function counts; the full protected list with the rule that caught each; the
`NAME-ONLY` list; each policy's character count; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: RUN at the cut by the simulation criteria (CT3c5-AC2, CT3c5-AC3); `comp-iam gaps` after the apply is the issuer's.
comp-adversary: RUN -- a Dell replacing the code of an authorizer, the edge auth validator or a user or key management function (explicit Deny on the derived set, which overrides every Allow); a protected function missed by the rules (three rules, two of them structural reads of the live wiring; the NAME-ONLY list printed for the CTO's read); a census that silently skips a region (refused regions printed and counted, AC1); BLIND: an access-deciding function created after the census is not denied until the next render and apply (the --check arm shows the drift).
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: CTO msg 106008 (the ruling: the explicit Deny alone; supersedes msg 105969's named-ARN scope), msg 105973, PRD v0.8 ADDENDUM v0.7; decomposition round 3 "Open at the CTO" item 1. Base dry-run at the cut: CT3c5-AC1 base FAIL as expected (no file); CT3c5-AC2 base FAIL as expected (no `protected_ok`); CT3c5-AC3 base FAIL as expected (no `policy_size_ok` before CT-c-1).

## AMENDMENT 2 (2.0.0_SA_COO~C, 2026-10-07 ~07:0xZ) -- the matrix counts after CT-c-1's reopen

CT-c-1 AMENDMENT 2 (row W4-S4, the CTO's ruling @bb0e587e22) takes the first simulation block to 21 allowed and 18 denied. Every
`17/17` on this face now reads `allowed_ok=21/21 denied_ok=18/18`; nothing else changes. Gate limb: none graded this modification.
