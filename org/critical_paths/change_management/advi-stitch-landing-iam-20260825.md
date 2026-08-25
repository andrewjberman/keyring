# DEPLOY-COMPLETION LEDGER -- ADVI_STITCH Phase A, the legacy-landing IAM role

**Status:** **OPEN** -- opened at deploy-start.
**Opened:** 2026-08-25T21:2xZ by `0.7.0_AE_CloudOps~J`
**Closes when:** `aws iam get-role --role-name opal-advi-stitch-landing-role` resolves AND
`aws iam get-role-policy --role-name opal-advi-stitch-landing-role --policy-name
opal-advi-stitch-landing-scoped` returns the six-statement document, AND a targeted
`terraform plan` on the two addresses returns **0-diff**.
⛔ **NOT on apply exit code, NOT on the plan file, NOT on `terraform state show`** -- those are
DESIRED/plan-plane artifacts. The close is an APPLIED read from live IAM.

## Why this entry exists
NEVER#6: a begun deploy FINISHES in-session or rolls back + escalates loud to COO.

## What is being deployed
`infra/aws/terraform/opal-assets/advi_stitch_landing.tf` -- ONE new IAM role
(`opal-advi-stitch-landing-role`) + its inline scoped policy. **Two resources, both CREATE.
No modification to any existing resource. No Lambda, no bucket, no served key.**

- TO: `ADVI_STITCH.TO-A1-AE`, cells `STI-b-4` + `STI-inv-1`.
- Principal RULED by `2.0.0_SA_COO` 71437 (adopting this seat's recommendation in 71426).
- Source-tree correction applied from `2.0.0_SA_COO` 71457 (source is `opal-data-bd`, NOT
  `blackdiamond/49f/`) -- and independently measured at this seat before the correction arrived.

## ⛔ TARGETING, AND WHY IT IS MANDATORY HERE -- READ BEFORE ANY FUTURE APPLY IN THIS ROOT
An UNTARGETED `terraform plan` in `infra/aws/terraform/opal-assets/` returns
**`2 to add, 3 to change, 0 to destroy`.** The 3 changes are **NOT this deploy's** and are
**committed-but-unapplied** config authored by other seats:
  - `aws_iam_role_policy.bd49f_reporting_io`      (in-place)
  - `aws_iam_role_policy.emitter`                 (in-place)
  - `module.emitter.aws_lambda_function.this`     -- env `AGGREGATE_PREFIX`
        `gold/mdpf_revamp/_aggregate_aua/` -> `portal/gold/mdpf/_staging/aggregate_aua/`
`git status` on this root shows ONLY the new file as untracked, so those three are pending from
prior commits -- and commit `1abc54fa4c` states the deferral explicitly:
*"COMMIT-BEFORE-APPLY (Rule 2; applies pend DS~A's P2D-3 pin + the armed CTO gate)."*
**They are HELD ON A GATE. A bare apply in this root lands another seat's deferred work --
including a live Lambda env repoint of a served MDPF path -- under the applying seat's name.**
Therefore this deploy applies with:
    -target=aws_iam_role.advi_stitch_landing
    -target=aws_iam_role_policy.advi_stitch_landing
Targeted plan: **`2 to add, 0 to change, 0 to destroy`.**

## Evidence banked before apply
- `terraform validate` -> Success. `terraform fmt` -> clean.
- `aws accessanalyzer validate-policy --policy-type IDENTITY_POLICY` over the full final grant
  (all six statements, incl. `s3:prefix` condition keys) -> **0 findings**. This closes the
  action-name-typo false-deny mode, which is byte-identical to a missing grant in a simulate result.
- `aws iam get-role --role-name opal-advi-stitch-landing-role` -> `NoSuchEntity` (clean mint).
- Bucket policies read LIVE on all three buckets in the grant:
  - `opal-data-49financial`: `DenyForeignFirmPrincipals` on ArnLike `role/cot-*`, `role/inf-*`,
    `role/mdpf-*`, `role/opal-assets-mdpf-*`. The chosen name matches **none** of the four.
    A resource-policy Deny is NOT overridable by any identity grant -- hence the name check.
  - `opal-data-bd`: two CloudFront Allow statements, **no Deny**. No interference.
  - `opal-data-assets`: one Deny (`DenyParquetUnderBronze17a`) + a CloudFront read. See AC3 below.

## Design notes that are load-bearing (do not "simplify" these away)
1. **A DEDICATED role, not an extension.** Every existing bd49f role holds write on
   `opal-data-assets/blackdiamond/49f/*` (`bd49f_pull.tf:88`), and the operator identity is
   unrestricted admin (measured: PutObject on a foreign bucket -> `allowed`;
   `organizations:LeaveOrganization` -> `allowed`). Against either, **AC2's required DENY is
   UNOBTAINABLE, not merely unmet** -- the arm returns `allowed` whether or not the scoping is
   correct, so the criterion could never fail and therefore never inform.
2. **EXACT SEGMENTS on the source, not `gold/canonical/*`.** That prefix holds 11 children;
   only `performance/`, `nna/`, `holdings/` are in scope per `STI-a-3`. A `nna*` wildcard would
   silently reach `nna_atomic/` and `nna_validation/`; `holdings*` would reach `holdings_gaps/`.
3. **`ListBucket` is prefix-conditioned per bucket (NEVER#2).**
   `opal-data-assets/blackdiamond/` holds BOTH `49f/` and `cottonwood/` -- a **different firm**.
   An unconditioned `s3:ListBucket` would let this role enumerate Cottonwood's tree.
4. **An EXPLICIT Deny on the live tiers**, not merely the absence of a grant -- an explicit Deny
   cannot be widened by a later attached policy, so `STI-inv-1`'s protective property survives a
   future least-privilege edit by someone who does not hold this context.

## Rollback
`terraform destroy` targeted to the same two addresses, or delete the file and re-apply targeted.
**Zero blast radius: both resources are CREATE-only and nothing references them yet.** No served
key, no data path, no existing principal is modified by this deploy.

## What this deploy does NOT cover
- **AC1/AC2 EXERCISE** -- the simulate matrix runs after the role exists; recorded separately.
- **AC3** -- the `DenyParquetUnderBronze17a` bucket policy matches the literal `/bronze/` segment
  (`opal-data-assets/*/bronze/*.parquet`). `bronze_legacy/` does **not** contain that segment, so
  **the 17a guard does not reach the legacy tier.** Per AC3 the widening is a one-line segment
  addition **PROPOSED TO CTO, never self-applied** (bucket policy is the infra lane). Until then
  the no-parquet property rests on the DS lane's `inv-2`. The write-probes wait for the prefixes.
- **The migration itself** -- this is the grant only. The copy is `0.4.0_DS_ClientPlatform~Q`'s
  leg and gates on `STI-b-0`, which is NOT committed as of this entry (verified on both planes;
  local CLOUD is 26 ahead of origin under the integrator-only push gate).
