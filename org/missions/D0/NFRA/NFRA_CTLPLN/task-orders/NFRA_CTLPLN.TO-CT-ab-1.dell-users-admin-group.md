# TO NFRA_CTLPLN.TO-CT-ab-1 -- workstream DELLADMIN round 1 (cell CT-ab-1): the two Dell agent users join Andrew_Berman's admin group and keep only three denies (Andrew-direct rec b)

<to_id>NFRA_CTLPLN.TO-CT-ab-1</to_id>
<project>NFRA_CTLPLN</project>
<issued_to>0.9.0_WK_NFRA_CTLPLN~77</issued_to>
<issued_by>2.0.0_SA_COO~C</issued_by>
<issued_date>2026-10-13</issued_date>
<status>pending</status>
<direct_act>false</direct_act>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<placeholders>NONE</placeholders>
<round>1</round>
<workstream>DELLADMIN</workstream>

**Directive:** D0 | **Fabric:** laptop | **Decomp cell:** `CT-ab-1` (`decompositions/NFRA_CTLPLN_DECOMP.round12.md`) | **outcome_ref:** FWD-10, FWD-5 |
**depends_on:** none

---

## WORKER FACE

### THE CELL

Andrew ruled (record `org/tier1_exec/2.0.0_SA_COO~C/deliverables/ANDREW_DIRECT_20261013_165xZ_DELL_USERS_ADMIN_GROUP_KEEP_THREE_DENIES.md`, read it whole): the Dell agent users `cloudops-dell1-agent-user` and `cloudops-dell2-agent-user` get the same access pattern as `Andrew_Berman`, i.e. membership of the existing IAM group `AdministratorAccessOpalCapital` (it is NOT managed by Terraform; do not create or import it), and every Deny that reaches them is removed EXCEPT exactly four statements: `DenyCloudTrailWrites`, `DenyS3DeletesOnProductionData`, `DenyTableAndDatabaseDeletes` (all three in `dell_deploy_policy.json`) and `DenyAuditTrailBucketWrites` (in `dell_create_policy.json`).

MEASURED at the cut (the Deny statements in the root `infra/aws/terraform/nfra-ctlpln-identity/`):
- `dell_deploy_policy.json`: `DenyCloudTrailWrites`, `DenyS3DeletesOnProductionData`, `DenyTableAndDatabaseDeletes` (KEEP); `DenyApiKeyReads`, `DenyCutoverParameterWrites`, `DenyProtectedFunctions` (REMOVE).
- `dell_create_policy.json`: `DenyAuditTrailBucketWrites` (KEEP).
- `dell_iam_roles_policy.json`: `DenyIamUsersGroupsKeysAndAccount` (REMOVE).
- `dell2_ssm_policy.json` (attached to both users): `DenyShellDocuments`, `DenyStartSessionOnShellScriptDocument` (REMOVE).
- `dell1_bus_policy.json`, `dell2_bus_policy.json`, `dell_planreads_policy.json`, `dell_respol_policy.json`: no Deny.
Also read `iam.tf` whole (the group `cloudops-dell-agents-group`, its nine managed-policy attachments, the users, `aws_iam_group_membership.dell_agents`) and every other `*.tf` in the root, in case a Deny is rendered from HCL rather than a JSON file.

### BUILD

1. Add, in `iam.tf`, ONE resource per Dell user of type `aws_iam_user_group_membership` that lists `AdministratorAccessOpalCapital` (keep the existing `aws_iam_group_membership.dell_agents` as is: the users stay in their own group). Comment it with the record path.
2. Remove the REMOVE statements above from their JSON documents; leave every Allow and the four KEEP statements byte-identical. If a document is left with no statements, keep it valid (do not delete files or resources; the plan should read changes, not destroys).
3. Update the comments in `iam.tf` that describe the removed Denies (they would now be false), and `tests/check_identity.py` where it asserts a removed Deny (it currently prints `IAM-PARTITION ... OK` and `IDENTITY-STATIC ... ok=True`; keep it passing, changing only what the ruling makes false; say what you changed).
4. A NEW check `infra/aws/terraform/nfra-ctlpln-identity/tests/check_admin_parity.py` (standard library only, reads files, no AWS): parses every `*.json` policy document and every `*.tf` in the root and prints exactly one final line `ADMIN-PARITY membership=<both|dell1|dell2|none> denies=<comma-separated sorted Sids of every Deny statement found> ok=<True|False>`, ok=True only when both users are given `AdministratorAccessOpalCapital` by an `aws_iam_user_group_membership` and the deny set is exactly `DenyAuditTrailBucketWrites,DenyCloudTrailWrites,DenyS3DeletesOnProductionData,DenyTableAndDatabaseDeletes`.

### RULES FOR THIS CELL

Write surface = the `<paths>`. NO terraform command that needs credentials (no init/plan/apply), no aws, no push; nothing is applied by this cell (a separate signed pair applies it). `.tools/safe-commit.sh` for every commit. Do NOT commit the `portal` gitlink. ASCII only; Python 3.11. CLAUDE.md and org/XXX.md are LOCKED. If the naming gate or any gate REFUSES, STOP and file a BLOCKING row. FOUND SOMETHING ODD OFF-TASK? Append ONE row (`spec_asserts` + `world_is`) to `org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md` (id `NFRA_CTLPLN-W77-S<k>`, `surfaced_at` = `date -u +%FT%TZ`) and keep working.

### ACCEPTANCE

<proof_of_spec>
<criterion id="CTab1-AC1" cell_refs="CT-ab-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/check_admin_parity.py</invocation><expect>denies=DenyAuditTrailBucketWrites,DenyCloudTrailWrites,DenyS3DeletesOnProductionData,DenyTableAndDatabaseDeletes ok=True</expect></criterion>
`CTab1-AC1` -- both memberships present and only the four kept denies remain.

<criterion id="CTab1-AC2" cell_refs="CT-ab-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/check_admin_parity.py</invocation><expect>membership=both</expect></criterion>
`CTab1-AC2` -- both users, not one.

<criterion id="CTab1-AC3" cell_refs="CT-ab-1"><invocation>python infra/aws/terraform/nfra-ctlpln-identity/tests/check_identity.py</invocation><expect>ok=True</expect></criterion>
`CTab1-AC3` -- the existing static identity check still passes (a control that PASSES at the base).
</proof_of_spec>

<expected_criteria>CTab1-AC1,CTab1-AC2,CTab1-AC3</expected_criteria>

Each invocation runs from the worktree root under `timeout 120`; record the criterion text as the invocation. Write the proof instance to `org/missions/D0/NFRA/NFRA_CTLPLN/deliverables/0.9.0_WK_NFRA_CTLPLN~77/NFRA_CTLPLN.TO-CT-ab-1.dell-users-admin-group.proof_of_spec.json`, validate it with `python .tools/proof-of-spec-check.py <instance> CTab1-AC1,CTab1-AC2,CTab1-AC3`, flip `<status>` to `complete` only when all pass and the instance is VALID (if refused as outside your grant, leave it `pending` and say so). Report the diff summary per file.

<decomp_ref>
<decomp_doc>org/missions/D0/NFRA/NFRA_CTLPLN/decompositions/NFRA_CTLPLN_DECOMP.round12.md</decomp_doc>
<owned_cells>CT-ab-1</owned_cells>
</decomp_ref>

<paths>
infra/aws/terraform/nfra-ctlpln-identity/
org/missions/D0/NFRA/NFRA_CTLPLN/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

---

## RECORD FACE

<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE this cell schedules nothing.
comp-iam: DECLARED-NOT-APPLICABLE at this cell (no AWS call); the apply cell CT-ab-2 runs it with its denominator.
comp-adversary: RUN -- a kept deny removed by mistake (AC1's exact set); one user only (AC2); a Deny rendered from HCL the JSON scan misses (the check reads every .tf too); a resource deleted so the plan reads a destroy (BUILD 2 keeps documents); BLIND: whether the live group carries an extra attachment the repo does not show (CT-ab-2's plan reads it).
risk: WORLD is declared because the L6 gate derives a floor from the infra path; this cell applies nothing.
lane: the <paths> block IS the grant (worker RULING 1).
</preflight>

Source: Andrew-direct record @ff6d6d5fd7; CTO ruling @53acd6fe5f section 1.
