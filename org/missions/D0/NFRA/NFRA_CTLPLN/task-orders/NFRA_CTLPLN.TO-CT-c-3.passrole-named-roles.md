# TO NFRA_CTLPLN.TO-CT-c-3 -- round 3 CT-c-3: the PassRole statement -- only roles the laptop made, rendered from applied requests

<to_id>NFRA_CTLPLN.TO-CT-c-3</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~4</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>3</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-c-3` (`decompositions/NFRA_CTLPLN_DECOMP.round3.md`) | **outcome_ref:** FWD-10 |
**depends_on:** CT-c-1 (the policy it edits), CT-c-2 (the request records it reads) -- both merged before this order is handed

---

## WORKER FACE

### THE CELL

`CT-c-3`, PRD v0.8 C-ROLE-REQUEST (b): "The Dell policy allows `iam:PassRole` only on roles the laptop has made for Dell-placed work,
named in the policy, with the `iam:PassedToService` condition. Every other IAM action stays denied." The named-role list is DERIVED from
the roles the laptop has made, never from a wildcard. You build the renderer and prove it by simulation. You APPLY NOTHING.

**What exists after CT-c-1 and CT-c-2:** `infra/aws/terraform/nfra-ctlpln-identity/dell_deploy_policy.json`, whose statement
`DenyEveryIamWrite` lists `iam:PassRole` among its denied actions on `Resource: "*"` (an explicit Deny overrides every Allow);
`dell_create_policy.json`; `tests/simulate_policy.py` (21 allowed, 18 denied); the request records
`org/devices/role_requests/<device>/<request_id>.json` (each with `assuming_service`) and the laptop's answers
`org/devices/role_requests/<laptop device>/answers/<request_id>.json` (each with `status` `applied` or `refused` and, when applied,
`role_arn`); a request with no answer file is `requested`; `org/devices/role_request.py list` prints the effective status.

**Build:**

1. `tests/render_passrole.py` -- the renderer, with `--records <dir>` (default `org/devices/role_requests`), `--check` and `--write`.
   - Reads every request record and every answer file; keeps the requests whose answer has `status == "applied"`; takes `role_arn`
     from the answer and `assuming_service` from the request. An answer with no matching request, an answer
     that is `applied` with no `role_arn`, or whose ARN is not `arn:aws:iam::313476888478:role/<name>` with a literal name (no `*`, no
     `?`), is an ERROR and the render fails.
   - Renders two things into `dell_deploy_policy.json`: (i) `iam:PassRole` leaves `DenyEveryIamWrite` and moves to its own statement
     `DenyPassRoleExceptNamed`: Effect Deny, Action `iam:PassRole`, and `NotResource` = the sorted named ARNs -- or, when there are
     none, `Resource: "*"`; (ii) when there is at least one named ARN, a statement `AllowPassNamedRoles`: Effect Allow, Action
     `iam:PassRole`, `Resource` = the same sorted ARNs, Condition `StringEquals` `iam:PassedToService` = the sorted distinct services of
     those records. With zero applied answers no Allow statement is written. Every other statement is left byte-identical.
   - `--check` compares the file to what a render would produce and writes nothing; `--write` writes it.
   - LAST line `PASSROLE-RENDER applied=<a> named=<n> wildcard=0 in_sync=<True|False> ok=<True|False>`.
2. Run `--write` once against the live records directory. If it holds no applied record (expected at this cut), the result is the
   zero case: the pass denied on every role.
3. `tests/simulate_policy.py` -- add a second block that evaluates a RENDERED COPY (a temporary directory holding one fixture request and its fixture answer,
   `applied`, role `arn:aws:iam::313476888478:role/ctlpln-fixture-role`, service `lambda.amazonaws.com`; render with `--records` on it
   into a temporary copy of the policy, never the real file): `iam:PassRole` on the fixture role with context
   `iam:PassedToService=lambda.amazonaws.com` -> allowed; the same role with `iam:PassedToService=ec2.amazonaws.com` -> denied;
   `iam:PassRole` on `arn:aws:iam::313476888478:role/some-other-role` -> denied; `iam:CreateRole` -> denied; `iam:PutRolePolicy` on the
   fixture role -> denied. The existing first block (the real files: 21 allowed, 18 denied) stays and must still hold. LAST line
   `POLICY-SIM allowed_ok=21/21 denied_ok=18/18 passrole_ok=5/5 all_ok=<True|False>`.

### ACCEPTANCE

<criterion id="CT3c3-AC1" cell_refs="CT-c-3"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/render_passrole.py --check</invocation><expect>wildcard=0 in_sync=True ok=True</expect></criterion>
`CT3c3-AC1` -- the committed policy is exactly what the renderer produces from the live records, and it names no wildcard.

<criterion id="CT3c3-AC2" cell_refs="CT-c-3"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py</invocation><expect>POLICY-SIM allowed_ok=21/21 denied_ok=18/18 passrole_ok=5/5 all_ok=True</expect></criterion>
`CT3c3-AC2` -- the cloud's evaluator passes the named role to its service only, refuses an unnamed role and a wrong service, and still
refuses every other IAM write. The refusals are the control arm of the allow.

<expected_criteria>CT3c3-AC1,CT3c3-AC2</expected_criteria>

## BOUNDS

- **Grant.** The `<paths>` block below plus your deliverables folder and this order's file.
- **No apply, no IAM write.** The only AWS call allowed is `iam:SimulateCustomPolicy` (read-only).
- You never write a record under `org/devices/role_requests/`; the fixture lives in a temporary directory.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W4-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
infra/aws/terraform/nfra-ctlpln-identity/dell_deploy_policy.json
infra/aws/terraform/nfra-ctlpln-identity/tests/render_passrole.py
infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py
infra/aws/terraform/nfra-ctlpln-identity/tests/check_identity.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `org/devices/role_requests/`, `org/devices/role_request.py`,
`org/standards/ROLE_REQUEST.schema.json`, `infra/aws/terraform/nfra-ctlpln-identity/iam.tf`, `dell_create_policy.json`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round3.md</decomp_doc> (round 3), cell `CT-c-3`.
<owned_cells>CT-c-3</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT3c3-AC1, CT3c3-AC2. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~4/NFRA_CTLPLN.TO-CT-c-3.passrole-named-roles.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT3c3-AC1,CT3c3-AC2` BEFORE the flip.
</proof_of_spec>

**REPORT:** both last lines; the rendered statements for the zero case and for the fixture case; the policy's character count after the
render; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: RUN at the cut by the policy simulation criterion (CT3c3-AC2); `comp-iam gaps` after the apply is the issuer's.
comp-adversary: RUN -- privilege escalation by passing a powerful existing role (Deny with NotResource on the named list; no wildcard, enforced by the renderer and by AC1); a named role passed to a different service (iam:PassedToService, the wrong-service arm of AC2); a forged applied record (records are per-box files under FWD-8, and only the laptop marks one applied -- CT-c-4; the render and the apply both run on the laptop); BLIND: a laptop-made role that is itself too broad -- the laptop's read of the request is the control.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.8 @6df8d231f4 ADDENDUM v0.8 C-ROLE-REQUEST (b); surprise row NFRA_CTLPLN-W1-S1 (ARMED; this cell's apply disarms it);
CTO msg 105999; decomposition round 3. Base dry-run at the cut: CT3c3-AC1 base FAIL as expected (no renderer); CT3c3-AC2 base FAIL as
expected (no `passrole_ok`).

## AMENDMENT 1 (2.0.0_SA_COO~C, 2026-10-07 ~07:0xZ) -- the matrix counts after CT-c-1's reopen

CT-c-1 AMENDMENT 1 (row W4-S4, the CTO's ruling @bb0e587e22) takes the first simulation block to 21 allowed and 18 denied. Every
`17/17` on this face now reads `allowed_ok=21/21 denied_ok=18/18`; nothing else changes. Gate limb: none graded this modification.
