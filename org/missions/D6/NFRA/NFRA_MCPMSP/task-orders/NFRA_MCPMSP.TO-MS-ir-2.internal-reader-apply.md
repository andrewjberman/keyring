# NFRA_MCPMSP task order -- `MS-ir-2` -- ROUND 2, E1: the Opal-internal reader role goes live (no Deny)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-ir-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~1</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: RUN -- AC2/AC3 simulate the new role and the gateway role. Blindness: those two roles and the named keys.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC3 is the control that the Deny is NOT applied.
EGRESS CLASS, declared: none (Opal's own AWS account).
</preflight>

## 1. THE CELL -- `MS-ir-2` (decomposition v2, R2.2)

Apply ONLY `mcpmsp_internal_reader.tf`'s resources (your previous order MS-ir-1 wrote them; merged to CLOUD before
this order) -- the role, its policy, the gateway's AssumeRole policy. **Never the resources of
`mcpmsp_gateway_firm_deny.tf`** (that is MS-dn-1's, held).
1. **Ledger first** (NEVER-2): `python .tools/deploy_ledger.py open --slug nfra-mcpmsp-r2-internal-role ...` with the
   blast radius (one role, its policy, one AssumeRole policy on the gateway role; rollback = `terraform destroy -target`
   of exactly those) and legs (targeted apply; simulate); commit the entry AND its sentinel
   `org/critical_paths/.open_deploys/nfra-mcpmsp-r2-internal-role.json` before the apply.
2. **Plan, then `bash .tools/safe-apply.sh -chdir=infra/aws/terraform/opal-gateway apply -target=...`** with a PRIVATE
   Terraform data dir (copy the main tree's `.terraform/providers` and `terraform.tfstate`, `terraform get`, never
   `init`), the restored layer zip and the writer's `.build/staged` copied from the main tree if absent, and the writer's
   two variables read from the LIVE function's environment (`aws lambda get-function-configuration --function-name
   mcportal-grant-writer-lambda`: `MCPORTAL_OWNER_KEY_CLAIM`, `MCPORTAL_OWNER_KEY`) into shell variables passed as
   `-var` / `TF_VAR_*` -- never printed, logged or committed. The plan must read only additions for your targets; any
   other change is a BLOCKING row and no apply. If safe-apply's HALT-GATE blocks on routine mail with zero STOP-class
   lines, follow its own protocol (`HALT_ACK=1`).
3. Read AC2/AC3, close the legs and the entry (sentinel removed), commit.

## 2. BOUNDS

1. Blast radius: the internal-reader addresses only. The gateway role's existing policies are untouched.
2. No push, no vendor call. REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
org/critical_paths/change_management/
org/critical_paths/.open_deploys/nfra-mcpmsp-r2-internal-role.json
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~1/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/terraform/opal-gateway/*.tf`, `.tools/safe-apply.sh`, `.tools/deploy_ledger.py`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W1-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your last commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-ir-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e1a.AC1.sh; echo "exit=$?"</invocation><expect>slug nfra-mcpmsp-r2-internal-role: entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0; SCAN DENOMINATOR present -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-ir-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e1a.AC2.sh; echo "exit=$?"</invocation><expect>role gateway-global-internal-reader-role: firm-key=allowed global-key=allowed; gateway AssumeRole=allowed -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MS-ir-2"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e1a.AC3.sh; echo "exit=$?"</invocation><expect>gateway role opal-gateway-role: firm-key GetObject=allowed; inline policy gateway-firm-deny-policy present=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~1/NFRA_MCPMSP.TO-MS-ir-2.internal-reader-apply.proof_of_spec.json`.
Report once, with: the role ARN (the release puts it in `.env`); the plan and apply lines; the three check lines; the
ledger path; the commit hash; any row.

**Handoff (issuer, 2026-10-01):** MS-ir-1 merged at 6e44ef41c6. The three targets are
`aws_iam_role.int_reader`, `aws_iam_role_policy.int_reader`, `aws_iam_role_policy.gw_assume_int_reader` -- and NEVER
`aws_iam_role_policy.gw_firm_deny`. `.tools/safe-apply.sh`'s naming plan stage now renders the TARGETED plan (MS-s-1,
merged bd3fc6fcc1), so a whole-tree literal elsewhere no longer blocks this apply; a refusal on your three targets is a
BLOCKING row. Run `git merge CLOUD` in your worktree first.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 issuance (E1); WORLD: a grant. Checks dry-run at base: AC1 FAIL as expected; AC2 FAIL as
expected (NoSuchEntity); AC3 PASS as expected (the control: the gateway role reads the firm key today, no Deny policy).

<status>staged</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
