# NFRA_MCPMSP task order -- `MS-ir-1` -- ROUND 2, E1: the Opal-internal reader role and the gateway firm Deny, in Terraform

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPMSP/decompositions/NFRA_MCPMSP_DECOMP.md</decomp_doc>
<owned_cells>MS-ir-1</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_NFRA_MCPMSP~1</issued_to>
<issued_by>2.0.0_SA_COO~MS</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence.
comp-iam: RUN at MS-ir-2 (the role) and MS-dn-1 (the Deny); this cell writes the text they apply.
comp-adversary: DECLARED-NOT-APPLICABLE -- the Deny's adversary read is MS-dn-1's census.
EGRESS CLASS, declared: none.
</preflight>

## 1. THE CELL -- `MS-ir-1` (decomposition v2, R2.2)

Write TWO new files in `infra/aws/terraform/opal-gateway/` (your previous order MS-c-1's census is the input for the
second):
1. **`mcpmsp_internal_reader.tf`** -- the Opal-internal reader role for opal-internal askers:
   - every name through the HCL builder module `infra/aws/terraform/modules/opal_name` (precedent: this directory's
     `mcpmsp_firm_roles.tf`): `system = "gateway"`, `scope = "global"`, `function = "internal-reader"`, `kind = "role"`
     (= `gateway-global-internal-reader-role`) and `kind = "policy"`; a second function `internal-assume`, `kind =
     "policy"`, for the gateway's grant;
   - the bucket from `module.<call>.scope_bucket["global"]` (never a typed `opal-data-` literal -- the ENFORCE naming
     gate refuses it, measured in round 1);
   - policy: `s3:GetObject` on the same resources today's `gw_queryv0_portal_read` grants (`queryv0-iam.tf`: `json/*`,
     `platinum/*` of that bucket) -- Opal-internal askers see every firm (catalog rule 5);
   - trust: ONLY `aws_iam_role.gw` (`main.tf:146`); the gateway's one `sts:AssumeRole` on exactly this role's ARN.
2. **`mcpmsp_gateway_firm_deny.tf`** -- an explicit `Deny` on `s3:GetObject` for `aws_iam_role.gw` on the firm-segment
   keys MS-c-1's census lists (`firm_segments[]`) in the builder-named portal bucket, as one inline policy named by the
   builder (`system = "gateway"`, scope null, `function = "firm-deny"`, `kind = "policy"` = `gateway-firm-deny-policy`).
   Firm tokens come from builder outputs or module `scope` inputs, never typed literals outside a module `scope`.
   **This file is written now and applied ONLY by MS-dn-1** (held on the reader routing and a never-widen pair).

**Plans here need the local modules registered:** AC2's check makes a PRIVATE copy of the main tree's `.terraform`
(providers + backend pointer), runs `terraform get` (no network), copies the restored layer zip and the writer's staged
dir if absent, and plans with plan-only placeholders for the two writer variables. Never `init`, never apply here.

## 2. BOUNDS

1. Write surface: the two new `.tf` files only. `terraform fmt` them. No apply.
2. No push, no vendor call. REFUSE a criterion you cannot meet as written.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/mcpmsp_internal_reader.tf
infra/aws/terraform/opal-gateway/mcpmsp_gateway_firm_deny.tf
org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~1/**
org/missions/D6/NFRA/NFRA_MCPMSP/surprise-channel/investigations/INVESTIGATION_v1.Z.md
</paths>

Read, never write: `infra/aws/terraform/opal-gateway/*.tf`, `infra/aws/terraform/modules/opal_name/**`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~1/r2_c1_census.json`,
`org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/`. Rows: `INVESTIGATION_v1.Z.md`, id
`NFRA_MCPMSP-Z-W1-S<k>`, `disarm_owner` `2.0.0_SA_COO~MS`.

## 4. PROOF OF SPEC (literal; run from your worktree root after your commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MS-ir-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e1t.AC1.sh; echo "exit=$?"</invocation><expect>role_module=y role_named=y bucket_builder=y no_literal_a=y assume_grant=y deny_stmt=y verdict=OK; naming gate PASS on both files (1 path each) -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MS-ir-1"><invocation>bash org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/2.0.0_SA_COO~MS/round2/checks/e1t.AC2.sh; echo "exit=$?"</invocation><expect>plan: Plan: N to add (N >= 3), 0 to change, 0 to destroy; planned role name gateway-global-internal-reader-role seen>=1 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPMSP/deliverables/0.9.0_WK_NFRA_MCPMSP~1/NFRA_MCPMSP.TO-MS-ir-1.internal-reader-tf.proof_of_spec.json`.
Report once, with: the resource addresses in each file; the Deny's key list; the plan line; the commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round-2 issuance (E1; CTO ruling 27414: MCPMSP owns the role). Checks dry-run at base: AC1 FAIL as
expected; AC2 FAIL as expected (files absent). Builder names measured at the cut. Slot `~1` continues to MS-ir-2.

<status>staged</status>
<round>2</round>
<slot>~1</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker-light</worker_class>
