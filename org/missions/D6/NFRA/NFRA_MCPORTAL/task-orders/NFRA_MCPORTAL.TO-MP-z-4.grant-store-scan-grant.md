# NFRA_MCPORTAL task order -- `MP-z-4` -- WORKSTREAM GW ROUND 1: the gateway may LIST the grant store (one dynamodb:Scan)

<!-- ===================== WORKER FACE -- this is the WHOLE of the assignee's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-z-4</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-z-4</to_id>
<issued_to>0.7.0_AE_CloudOps~MQ</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- an IAM policy; no cadence.
comp-iam: RUN -- by the issuer at the cut, `comp-iam role opal-gateway-role` over 222 Terraform roles parsed (`comp-iam stats`): the role's DynamoDB grants read GetItem/Query/Scan on the changes table and GetItem plus RUNTIME#-conditioned Put/Update/Delete on the access-state table; NO Scan on gateway-access-state-table. BLIND: it reads Terraform (DESIRED) only and cannot see an explicit Deny it never parsed; the live plane is read by AC1 (get-role-policy + simulation). The assignee runs `comp-iam gaps` again at the plan and puts its line in the ASK.
comp-adversary: DECLARED-NOT-APPLICABLE -- AC1's simulation arms are the adversary (another table refused; the existing reads unchanged).
EGRESS CLASS, declared: AWS IAM write on opal-gateway-role (one inline policy), by safe-apply.
</preflight>

## 1. THE CELL -- `MP-z-4` (workstream GW round 1, decomposition sections GW.0 item 3, GW.1 and GW.6)

Work in a linked worktree you cut from `box/sitez` HEAD (CLAUDE.md 14b), with the NO-CONE sparse pattern list that worked
for MP-k-2 (`.tools/`, `org/`, `lib/`, `infra/aws/terraform/opal-gateway/`). Commit there; the issuer drains it.

Andrew's first MCPORTAL outcome (PRD v0.7 FWD-20) shows who is entitled to each gateway channel today, and part of
that answer lives in the grant store `gateway-access-state-table` (the POLICY partition). The gateway's instance role
`opal-gateway-role` (`aws_iam_role.gw`, `infra/aws/terraform/opal-gateway/main.tf`) can read ONE item at a time there
(`gw_access_state_runtime`, `schwab_access_state.tf:88-113`: `dynamodb:GetItem`), so it cannot LIST who holds a profile.
The handler (another cell) Scans with a `pk`/`sk` projection and keeps only `POLICY#<tid>#<oid>` / `principal_profile`
keys. It needs exactly ONE new action: `dynamodb:Scan` on that one table.

**What it widens, stated plainly for the ASK:** Scan cannot be bound by key condition, so the role may enumerate every
row of a table whose every item it can already read by key (GetItem) or wrote itself (its RUNTIME# keys). No write, no
delete, no other table.

The pair is `1.0.0_SA_CTO~Z` (CTO half) and `2.0.0_SA_COO~MP` (COO half). Both sign against YOUR ASK before you apply.

Build and apply, in order:
1. **`infra/aws/terraform/opal-gateway/access_state_principal_scan.tf` (new).** It holds ONE `aws_iam_role_policy`,
   `gw_access_state_principal_scan`.
   - **Name:** `"gateway-access-state-principal-scan-policy"`, a LITERAL. This is the output of `lib/opal_naming.py
     name('gateway', None, 'access-state-principal-scan', 'policy')`, read by the issuer at the cut (row Z-S21: an
     interpolated name is refused at apply).
   - **Role:** `aws_iam_role.gw.id`.
   - **Statement:** ONE, `dynamodb:Scan` on `aws_dynamodb_table.access_state_new.arn`, and nothing else (no index ARN).
   - **Header comment,** in the style of `mcportal_close_request_write.tf`: what is granted and what is not (no write,
     no delete, no other table, no index); the reason (FWD-20 lists the principals holding a profile; the handler projects
     `pk`/`sk` and keeps POLICY profile keys only); that it is a separate, removable file; the rollback; the post-apply
     live check.
   - **If the naming gate refuses the name,** do not override it. File a BLOCKING row with the refusal text and stop.
2. **Plan, and the ASK.**
   - Run `comp-iam gaps`.
   - Run the plan with `safe-apply`, targeted to `aws_iam_role_policy.gw_access_state_principal_scan` only.
   - Anything other than `1 to add, 0 to change, 0 to destroy` STOPS the act with a BLOCKING row.
   - Write `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/NEVER_WIDEN_ASK_MP-z-4.md` with:
     the blast radius (the one action on the one table, and the enumeration it adds); what it may never touch (any write,
     delete, other table or index); the plan counts and the policy document as planned; the `comp-iam gaps` line; the
     rollback (a targeted destroy, or `aws iam delete-role-policy --role-name opal-gateway-role --policy-name
     gateway-access-state-principal-scan-policy`); the read-back you will run (AC1).
   - Commit the `.tf` and the ASK. Then send ONE message, to BOTH `1.0.0_SA_CTO~Z` and `2.0.0_SA_COO~MP`, naming the ASK
     path and its commit, and asking each for its half.
3. **WAIT for both halves, at HEAD of `box/sitez`:**
   `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/1.0.0_SA_CTO~Z/NEVER_WIDEN_HALF_CTO_MP-z-4_<date>.md` and
   `.../deliverables/2.0.0_SA_COO~MP/NEVER_WIDEN_HALF_COO_MP-z-4_<date>.md`. Each cites your ASK by path. A refused half
   STOPS the act; report it.
4. **NEVER-2 ledger, on THIS branch, in this order.**
   - `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-gw-principal-scan-grant`; legs: apply, read-back.
   - Commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcportal-gw-principal-scan-grant.json`.
   - ACT with `safe-apply`, targeted to the same resource. Never bare `terraform apply`.
   - Read back with AC1.
   - Close every leg with its proof, and commit the close BEFORE you report the AC reads.
5. If `terraform init` needs a provider it cannot get from the local plugin cache, STOP with a BLOCKING row naming the
   provider and version.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No other Terraform resource moves and no other policy is edited. The
   gateway is not redeployed. You read no table item (the simulation is the exercise).
2. If a leg fails mid-act, roll back with the named command, close the entry as rolled back, and report.
3. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its
   measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/access_state_principal_scan.tf
org/critical_paths/change_management/*nfra-mcportal-gw-principal-scan-grant*
org/critical_paths/.open_deploys/nfra-mcportal-gw-principal-scan-grant.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/terraform/opal-gateway/main.tf`, `schwab_access_state.tf`, `mcportal_close_request_write.tf`,
`mcportal_grant_writer.tf`, `lib/opal_naming.py`, `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-S<k>` (the next free seat-row k). `surfaced_at` = `date -u +%FT%TZ` at filing. `disarm_owner` on an ARMED
row is `2.0.0_SA_COO~MP`. Rows are append-only.

## 4. PROOF OF SPEC (literal; run from your worktree root after the close commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-z-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/z4.AC1.sh; echo "exit=$?"</invocation><expect>actions=dynamodb:Scan resources=1 problems=0; simulation arms matched 4 of 4 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-z-4"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/fwd20/checks/z4.AC2.sh; echo "exit=$?"</invocation><expect>ask=yes; halves citing the ask=2 of 2; entry files at HEAD>=1; sentinel at HEAD=no; listed OPEN/HELD=0 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MQ/NFRA_MCPORTAL.TO-MP-z-4.grant-store-scan-grant.proof_of_spec.json`.
Report once, to `2.0.0_SA_COO~MP`, with: the plan counts; the `comp-iam gaps` line; the two check outputs; the ledger
entry path and its CLOSED state; every commit hash; any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** cut at the GW issuance (decomposition v7). Measured by the issuer 2026-10-13 ~09:3xZ: the gateway role
holds GetItem only on the table (`schwab_access_state.tf:97-99`); the changes table it can Scan names 0 of the store's 5
POLICY keys. Name read from the builder at the cut. Checks dry-run at base 8abe56f2cd: AC1 FAIL (NoSuchEntity), AC2 FAIL
(ask=no, 0 halves). The assignee is a seat: GO by message at the issuance. Gate: the never-widen pair before the apply.

**AMENDMENT 1 (issuer, 2026-10-13 ~12:0xZ): RE-ADDRESSED from `0.7.0_AE_CloudOps~MP` to `0.7.0_AE_CloudOps~MQ`.** The prior assignee reads HUNG (0.0.0_AB_MSTR~Z msg 33605: telemetry stops 2026-10-12 13:56Z; the GO msg 33596 reads OFFER-EXHAUSTED, 0 of 2 READ) and cannot be re-seated because it guards the C17 rollback trees `C:/tmp/mp-n1*`. Every live CloudOps lane on this box is seated on another project (one project per Tier-2 seat), so the issuer seats a fresh MCPORTAL applier lane. Nothing in the cell changes but the assignee and its deliverables path.

<status>pending</status>
<round>1</round>
<workstream>GW</workstream>
<fabric>site-z</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
<status>complete</status>
<!-- FLIPPED by the issuer 2026-10-13 ~16:4xZ at the drain @5ee667b8eb: AC1 4/4 arms (issuer's independent read too), AC2 pair 2/2 + ledger CLOSED; instance VALID. Rows Z-S42/Z-S43 INERT: the applier's notes for MP-z-5 (no terraform plan in z-5; its sparse list is NO-CONE). -->
