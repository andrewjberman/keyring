# TO NFRA_CTLPLN.TO-CT-d-5 -- round 4 CT-d-5: the resource-policy Deny -- a Dell cannot write a bucket, key, function or queue policy

<to_id>NFRA_CTLPLN.TO-CT-d-5</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~8</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-07</issued_date>
<status>complete</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>4</round>
<workstream>~C</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-d-5` (`decompositions/NFRA_CTLPLN_DECOMP.round4.md`) | **outcome_ref:** FWD-10 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

`CT-d-5`, PRD v0.12 ADDENDUM v0.10: "A bucket policy, a key policy and a Lambda permission are administered by the laptop through
C-ROLE-REQUEST's write-in ... The Dell policy denies the actions that write them." and "Next issuance: the Deny statements for those
actions, listed from the resource-policy actions of the services the Dell policy already allows (derived, never from memory), and one
exercised refusal." Andrew's word behind it: "For now, laptop should admin". You add the Deny and prove it by derivation and
simulation. You APPLY NOTHING; the exercised refusal on a Dell is run after your order by the issuer's route.

**What exists** (root `infra/aws/terraform/nfra-ctlpln-identity/`): `dell_deploy_policy.json` (4 Allow and 7 Deny statements; 4,951
characters without whitespace of a 6,144 limit), `dell_create_policy.json` (3,998), the two bus policies, `iam.tf`,
`tests/simulate_policy.py` (LAST line today `POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 all_ok=True`),
`tests/check_identity.py` (`... names_from_builder=7/7 policy_size_ok=True ok=True`), `tests/render_passrole.py --check` and
`tests/derive_protected_functions.py --check` (both render statements into `dell_deploy_policy.json` and must stay `in_sync=True`).
Today the access-granting actions are merely unallowed (implicit deny): nothing refuses them if a later Allow names them.

**RULED, and you keep it** (`1.0.0_SA_CTO`, row NFRA_CTLPLN-S6): `sqs:SetQueueAttributes` and `sns:SetTopicAttributes` STAY ALLOWED (IAM
has no condition that separates the Policy attribute), and the create calls for a key, queue, topic and bucket STAY ALLOWED with their
policy parameter. Your Deny must not catch any of those six.

**Build:**

1. `tests/derive_respol_actions.py` -- the derivation. It reads every Allow statement of the four Dell policy documents and lists the
   distinct service prefixes they allow (print the count and the list). For each service, a table inside the script (the table is the
   record) names that service's actions that WRITE or REMOVE a resource-based policy, a permission, or a grant: for example s3
   `PutBucketPolicy`, `DeleteBucketPolicy`, `PutBucketAcl`, `PutObjectAcl`, `PutAccessPointPolicy`; lambda `AddPermission`,
   `RemovePermission`, `AddLayerVersionPermission`, `RemoveLayerVersionPermission`; kms `PutKeyPolicy`, `CreateGrant`, `RevokeGrant`,
   `RetireGrant`; secretsmanager `PutResourcePolicy`, `DeleteResourcePolicy`; sns `AddPermission`, `RemovePermission`; sqs
   `AddPermission`, `RemovePermission`; logs `PutResourcePolicy`, `DeleteResourcePolicy`; ecr `SetRepositoryPolicy`,
   `DeleteRepositoryPolicy`; events `PutPermission`, `RemovePermission`; and the equivalent for every other allowed service that HAS
   such actions. A service with none is listed as `NONE <service>` with one line of why. A service you cannot settle is
   `UNSURE <service>` and counted; do not guess. The six ruled-allowed calls above are in an explicit `RULED-ALLOWED` list and are
   never in the Deny. The script then checks that every derived action is covered by the Deny statement of step 2 and that none of the
   six ruled calls is.
   LAST line `RESPOL-DERIVED services=<s> with_actions=<w> none=<n> unsure=<u> actions=<a> covered=<c>/<a> ruled_allowed_caught=<r> ok=<True|False>`,
   `ok=True` only when `c == a`, `r == 0` and `w + n + u == s`.
2. The policy: ONE statement `DenyResourcePolicyWrites`, Effect Deny, Resource `*`, the derived actions (exact names; a pattern only
   where it cannot catch a ruled-allowed call or a non-policy action). Put it in `dell_deploy_policy.json` if that document stays within
   6,144 characters without whitespace; otherwise in a new managed policy `dell_respol_policy.json`, name from
   `lib/opal_naming.name('cloudops', None, 'dell-agent-respol', 'policy')`, tagged `DisplayName = "DellBoxes"`, attached to the group
   in `iam.tf`, and the names count becomes 8/8 -- say which. Nothing else in any policy changes; the file's line endings are kept.
3. `tests/simulate_policy.py` -- a fourth block on the real files (dell1's effective set): `s3:PutBucketPolicy`, `lambda:AddPermission`,
   `kms:PutKeyPolicy`, `kms:CreateGrant`, `secretsmanager:PutResourcePolicy`, `sns:AddPermission`, `sqs:AddPermission`,
   `logs:PutResourcePolicy`, `ecr:SetRepositoryPolicy` -> each must be `explicitDeny` (an `implicitDeny` FAILS this block: the point is
   that the refusal is now explicit), 9 arms; `sqs:SetQueueAttributes` and `sns:SetTopicAttributes` -> `allowed`, 2 arms. In the first
   block, the existing denied arms for `s3:PutBucketPolicy`, `lambda:AddPermission`, `kms:PutKeyPolicy` and
   `secretsmanager:PutResourcePolicy` keep passing. LAST line
   `POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 respol_ok=11/11 all_ok=<True|False>`.

### ACCEPTANCE

<criterion id="CT4d5-AC1" cell_refs="CT-d-5"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/derive_respol_actions.py</invocation><expect>ruled_allowed_caught=0 ok=True</expect></criterion>
`CT4d5-AC1` -- every derived policy-writing action is denied and none of the six ruled-allowed calls is caught.

<criterion id="CT4d5-AC2" cell_refs="CT-d-5"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py</invocation><expect>POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 respol_ok=11/11 all_ok=True</expect></criterion>
`CT4d5-AC2` -- the cloud's evaluator explicitly denies the nine policy-writing actions, still allows the two ruled attribute calls,
and every earlier block holds.

<criterion id="CT4d5-AC3" cell_refs="CT-d-5"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/check_identity.py</invocation><expect>policy_size_ok=True ok=True</expect></criterion>
`CT4d5-AC3` -- the control: the root validates, names are the builder's and every document fits the limit. Also run
`tests/render_passrole.py --check` and `tests/derive_protected_functions.py --check` and put their last lines in your report: both
must still read `in_sync=True`.

<expected_criteria>CT4d5-AC1,CT4d5-AC2,CT4d5-AC3</expected_criteria>

## BOUNDS

- **Grant.** The paths block below plus your deliverables folder and this order's file.
- **No apply, no `terraform plan` against the backend, no IAM write.** AWS calls allowed, read-only: `iam:SimulateCustomPolicy`, and
  the listings `tests/derive_protected_functions.py --check` already makes.
- Do not type a firm name into any file outside a `tests/` directory; `tests/protected_functions_listing.json` already holds the
  function listing and you do not need to change it.
- **Refusal clause.** If a criterion cannot be met as written, stop, write the reason in your report and a surprise row (id
  `NFRA_CTLPLN-W8-S<k>`, `surfaced_at` = `date -u +%FT%TZ` at filing) in the investigation file, and do not weaken the test or the
  expected value.

<paths>
infra/aws/terraform/nfra-ctlpln-identity/dell_deploy_policy.json
infra/aws/terraform/nfra-ctlpln-identity/dell_respol_policy.json
infra/aws/terraform/nfra-ctlpln-identity/iam.tf
infra/aws/terraform/nfra-ctlpln-identity/tests/derive_respol_actions.py
infra/aws/terraform/nfra-ctlpln-identity/tests/simulate_policy.py
infra/aws/terraform/nfra-ctlpln-identity/tests/check_identity.py
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

The block is your WRITE grant. You READ and never edit: `dell_create_policy.json`, the bus policies, `protected_functions.json`,
`tests/render_passrole.py`, `tests/derive_protected_functions.py`, `tests/derive_resource_kinds.py`, `lib/opal_naming.py`.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round4.md</decomp_doc> (round 4), cell `CT-d-5`.
<owned_cells>CT-d-5</owned_cells>
</decomp_ref>

<proof_of_spec>
Criterion ids: CT4d5-AC1, CT4d5-AC2, CT4d5-AC3. Instance at `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~8/NFRA_CTLPLN.TO-CT-d-5.resource-policy-deny.proof_of_spec.json`,
validated with `python .tools/proof-of-spec-check.py <instance> CT4d5-AC1,CT4d5-AC2,CT4d5-AC3` BEFORE the flip.
</proof_of_spec>

**REPORT:** the three last lines and the two `--check` lines; the service list with each service's derived actions; every `NONE` and
`UNSURE` service; where the statement landed and each policy's character count; commits.

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE no schedule.
comp-iam: RUN at the cut by the simulation criterion (CT4d5-AC2), which requires explicitDeny on nine actions; base read `POLICY-SIM allowed_ok=22/22 denied_ok=19/19 passrole_ok=5/5 protected_ok=8/8 all_ok=True`; `comp-iam gaps` after the apply is the issuer's.
comp-adversary: RUN -- a later Allow silently granting a policy write (the Deny is explicit; implicitDeny fails the block); the Deny breaking a ruled-allowed update (the two attribute arms and ruled_allowed_caught=0); a service's policy action missed (derived per allowed service, UNSURE counted, the list printed for the CTO's read); BLIND: the six ruled calls still carry a policy with no cloud refusal (row NFRA_CTLPLN-S6, the CTO's stated residual); the live refusal on a Dell is the issuer's close act.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: PRD v0.12 @2f61412157 ADDENDUM v0.10; Andrew-direct record
`org/tier1_exec/1.0.0_SA_CTO/deliverables/ANDREW_DIRECT_20261007_065xZ_OPEN_CALLS_FOUR_ANSWERED_PASSROLE_YES_LAPTOP_ADMINS_STAY_CTO_PARKS_AND_CLOSES.md`;
rows NFRA_CTLPLN-S6, W4-S1, W4-S2; decomposition round 4. Base dry-run at the cut: CT4d5-AC1 base FAIL as expected (no file);
CT4d5-AC2 base FAIL as expected (no `respol_ok`); CT4d5-AC3 is a control and reads PASS at the base (the round-3 drain's read).
