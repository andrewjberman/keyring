# NFRA_MCPORTAL task order -- `MP-x-3` -- ROUND 5, E1: the gateway role's read grant on the two fabric prefixes (FWD-14 hop 2)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D6/NFRA/NFRA_MCPORTAL/decompositions/NFRA_MCPORTAL_DECOMP.md</decomp_doc>
<owned_cells>MP-x-3</owned_cells>
</decomp_ref>
<to_id>NFRA_MCPORTAL.TO-MP-x-3</to_id>
<issued_to>0.7.0_AE_CloudOps~MP</issued_to>
<issued_by>2.0.0_SA_COO~MP</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- an IAM grant; no cron, alarm, monitor or cadence.
comp-iam: RUN -- `comp-iam gaps` after the .tf change and before the apply; its output goes in the ledger entry (necessary, not sufficient; AC2's simulation is the truth).
comp-adversary: DECLARED-NOT-APPLICABLE -- AC2's three negative arms (third prefix, write, third-prefix list) are the adversary reads.
EGRESS CLASS, declared: none beyond AWS control-plane calls in Opal's own account.
</preflight>

## 1. THE CELL -- `MP-x-3` (round 5, decomposition section R5.1; analysis R-12)

Work in a linked worktree you cut from `box/sitez` HEAD (CLAUDE.md 14b). If you cut a sparse one, use a NO-CONE pattern
list that holds `.tools/`, `org/`, `lib/` and `infra/aws/terraform/opal-gateway/`, because a cone-mode worktree cannot pass the
`org/missions` commit gates (row NFRA_MCPORTAL-Z-W5-S2). Commit there, and the issuer drains it.

The gateway's instance role is `opal-gateway-role` (`infra/aws/terraform/opal-gateway/main.tf:151`, `aws_iam_role.gw`,
name `"${var.name}-role"`). A new admin page needs it to READ two prefixes of the bucket `opal-313476888478-globgrph`.
The bucket uses SSE-S3 (AES256) and has no bucket policy (both read 2026-10-08 ~22:0xZ), so the identity grant alone
admits the read. `graph-read.tf:4-8` records a control that this role holds NOTHING on that bucket (NFRA_CLDGRPH R3,
CG-s-12). The control's owner has RULED an exception. The ruling is verbatim, from laptop `1.0.0_SA_CTO` msg 107359,
relayed as msg 32030:

> "opal-gateway-role gets s3:GetObject on fabric/activity/v1/* and fabric/open-calls/v1/* of the globgrph bucket, and
> s3:ListBucket conditioned on those two prefixes only; no write, nothing else in the bucket (warehouse/ and projection/
> stay out). R3's text in infra/aws/terraform/opal-gateway/graph-read.tf carves out exactly those two read prefixes,
> citing this ruling. Site Z applies it under its own pair (you + 2.0.0_SA_COO~MP) for MCPORTAL round 4; read back by
> simulation that a third prefix is refused."

Build and apply, in order:
1. **`infra/aws/terraform/opal-gateway/mcportal_fabric_read.tf` (new).** It holds ONE `aws_iam_role_policy`,
   `gw_mcportal_fabric_read`, with name `"${var.name}-mcportal-fabric-read"` (that is, `opal-gateway-mcportal-fabric-read`)
   and role `aws_iam_role.gw.id`. It has two statements:
   - `s3:GetObject` on `arn:aws:s3:::opal-313476888478-globgrph/fabric/activity/v1/*` and `.../fabric/open-calls/v1/*`;
   - `s3:ListBucket` on `arn:aws:s3:::opal-313476888478-globgrph`, with the condition `StringLike` `s3:prefix` =
     [`fabric/activity/v1/*`, `fabric/open-calls/v1/*`, `fabric/activity/v1/`, `fabric/open-calls/v1/`].

   Give it a header comment in the style of `graph-read.tf`: what is granted and what is not, the ruling quoted with
   "laptop 1.0.0_SA_CTO msg 107359 (relay 32030)", that it is a separate, removable file, and the post-apply live check.
2. **`graph-read.tf`, comments only.** Amend the R3 paragraph (`:4-8`) to say that the role holds nothing on the
   globgrph bucket EXCEPT read of `fabric/activity/v1/` and `fabric/open-calls/v1/`, granted in
   `mcportal_fabric_read.tf`, citing "laptop 1.0.0_SA_CTO msg 107359 (relay 32030)". Change no resource line.
   **The naming gate now REFUSES hand-typed names at commit** (CLAUDE.md rule 30, law edit c55a7b39cd). If it refuses
   the policy name, do not override it. File a BLOCKING row naming the refusal text and stop, because the opal-gateway
   module is an existing pipeline (rule 30's non-application) and the issuer routes it.
3. **Preflight.** Run `comp-iam gaps` and record its output in the ledger entry.
4. **Rollback, named before the act.** Because the policy is new, the rollback is a targeted destroy of
   `aws_iam_role_policy.gw_mcportal_fabric_read`, or `aws iam delete-role-policy --role-name opal-gateway-role
   --policy-name opal-gateway-mcportal-fabric-read`. Write both into the ledger entry.
5. **NEVER-2 ledger, on THIS branch, in this order.**
   - Run `python .tools/deploy_ledger.py open ...` with slug `nfra-mcportal-r4-fabric-read-grant`. The legs are: plan,
     apply, read-back.
   - Commit the entry AND its sentinel `org/critical_paths/.open_deploys/nfra-mcportal-r4-fabric-read-grant.json`.
   - Run the plan with `safe-apply`, targeted to `aws_iam_role_policy.gw_mcportal_fabric_read` only. Print the plan's
     add, change and destroy counts. Anything other than `1 to add, 0 to change, 0 to destroy` STOPS the act with a
     BLOCKING row.
   - ACT with `safe-apply`. Never run bare `terraform apply`.
   - Read back with AC1 and AC2.
   - Close every leg with its proof, and commit the close BEFORE the AC reads you report.
6. If `terraform init` in your worktree needs a provider it cannot get from the local plugin cache, STOP with a
   BLOCKING row naming the provider and version. Do not fetch from the internet.

## 2. BOUNDS

1. Write surface: exactly the paths in section 3. No other Terraform resource moves, and no other policy is edited.
   The gateway is not redeployed and no S3 object is read or written.
2. If a leg fails mid-act, roll back with the named command, close the entry as rolled back, and report.
3. Standing rules: no push and no vendor call. If you cannot meet a criterion as written, REFUSE it with its
   measurement. Never repair a criterion.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-gateway/mcportal_fabric_read.tf
infra/aws/terraform/opal-gateway/graph-read.tf
org/critical_paths/change_management/*nfra-mcportal-r4-fabric-read-grant*
org/critical_paths/.open_deploys/nfra-mcportal-r4-fabric-read-grant.json
org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/**
org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/**
</paths>

Read, never write: `infra/aws/terraform/opal-gateway/main.tf`, `secrets-iam.tf`, `taxsma_rule22a_verify.sh`,
`org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round4/checks/`.

Rows go to `org/missions/D6/NFRA/NFRA_MCPORTAL/surprise-channel/investigations/INVESTIGATION_v1.Z.md`, with id
`NFRA_MCPORTAL-Z-A7-S<k>` (the next free k for A7). `disarm_owner` on an ARMED row is `2.0.0_SA_COO~MP`. Rows are
append-only.

## 4. PROOF OF SPEC (literal; run from your worktree root after the close commit)

<proof_of_spec>
  <criterion id="AC1" cell_refs="MP-x-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round4/checks/x3.AC1.sh; echo "exit=$?"</invocation><expect>actions=s3:GetObject+s3:ListBucket resources=3 problems=0 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="MP-x-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round4/checks/x3.AC2.sh; echo "exit=$?"</invocation><expect>simulation arms matched 6 of 6 -- RESULT: PASS -- exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="MP-x-3"><invocation>bash org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/2.0.0_SA_COO~MP/round4/checks/x3.AC3.sh; echo "exit=$?"</invocation><expect>carve-out tokens present 6 of 6 -- RESULT: PASS -- exit=0</expect></criterion>
</proof_of_spec>

## 5. WHEN YOU ARE DONE

Write the instance at `org/missions/D6/NFRA/NFRA_MCPORTAL/deliverables/0.7.0_AE_CloudOps~MP/NFRA_MCPORTAL.TO-MP-x-3.gateway-fabric-read-grant.proof_of_spec.json`.
Report once, with:
- the plan counts;
- the `comp-iam gaps` line;
- the three check outputs;
- the ledger entry path and its CLOSED state;
- every commit hash;
- any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->


**ISSUER NOTES:** E1 of ROUND_ANALYSIS.round4.md @460bc0af2f (R-12), cut in round 5's ONE issuance. Applier: a FRESH CloudOps lane for this project, `0.7.0_AE_CloudOps~MP`.
- Msg 32061 (Andrew-direct ~22:0xZ) moves site Z's applies onto a site-Z CloudOps seat.
- Rule 27's one-project-per-Tier-2-seat check refused `~Z`, which holds ETFS_RIVALS, NFRA_MCPINDEX and NFRA_OPLGTW.
- `~MP` has 0 uses in the spawn audit. The seat is asked of 0.0.0_AB_MSTR~Z.
No gate beyond the seat: it starts when the lane is live. The NFRA_CLDGRPH owner ruled (a): laptop
1.0.0_SA_CTO msg 107359, relayed by 0.0.0_AB_MSTR~Z as msg 32030; 1.0.0_SA_CTO~O's two messages (32034 at 21:49:03Z
and 32035) say "cut the cell under our pair".

**BLAST RADIUS, signed by the pair (1.0.0_SA_CTO~O by the ruling's "under its own pair"; 2.0.0_SA_COO~MP by this cut):**
- the act adds ONE inline policy to `opal-gateway-role`: read on two prefixes, and a list conditioned on the same two;
- no write, no other bucket prefix, and no other resource;
- `graph-read.tf` changes in comments only;
- no served output moves.
Rollback per key: `aws iam delete-role-policy --role-name opal-gateway-role --policy-name opal-gateway-mcportal-fabric-read`.

The bucket reads at the cut were SSE-S3 with no bucket policy, so no KMS grant is needed. Checks dry-run at base
202c512520:
- AC1 FAILS (NoSuchEntity);
- AC2 FAILS (3 of 6; the three positive arms read implicitDeny, and the three negative arms already read implicitDeny,
  so the positive arms are the discriminators);
- AC3 FAILS (the file is absent).

<status>pending</status>
<round>5</round>
<slot>0.7.0_AE_CloudOps~MP</slot>
<fabric>site-z</fabric>
<risk>WORLD</risk>

