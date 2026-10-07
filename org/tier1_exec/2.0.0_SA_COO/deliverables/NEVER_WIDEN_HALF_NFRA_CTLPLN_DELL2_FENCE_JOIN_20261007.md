# COO never-widen half -- NFRA_CTLPLN round 4, cell CT-d-2: dell2 joined to three firm-bucket fences

**Author:** `2.0.0_SA_COO~C`, 2026-10-07 ~09:4xZ. **Counterpart:** the CTO half
`org/tier1_exec/1.0.0_SA_CTO/deliverables/CTO_HALF_NFRA_CTLPLN_DELL2_FENCE_JOIN_20261007.md` @91f1667810, SIGNED on four conditions.
**Read at:** trunk `526a1a27ac` (the CT-d-2 merge).

## The act

ONE `safe-apply` at the laptop of `infra/aws/terraform/shared-infra/`, TARGETED at the three fence bucket policies and nothing else:
`aws_s3_bucket_policy.opal_data_49financial` and `aws_s3_bucket_policy.lgic_firm` (a `for_each` that builds exactly two: the
cottonwood and inflection buckets). The policies' admitted lists are rendered by `module.opal_name.fence_exemption_arns` from
`infra/logic/registry/exemptions.json`. Executor: a cloud-operations seat this lane seats under its own order.

## What changed in the repo (measured)

- `infra/logic/registry/exemptions.json` @e7ac51a04c, authored by `4.0.0_SA_CRO` in its own lane (its msg 106127): 18 added lines,
  0 deleted; one row for `cloudops-dell2-agent-user` under each of the three fenced firm-bucket keys, each with `arn`, `reason` and a
  `signoff_ref` naming this file and the CTO half. Its blob equals the worker's blob at ca2c18c4a4 (the CRO's own measurement).
- NO `.tf` file changed. The issuer's re-run on the merged tree:
  `FENCE-JOIN pairs=3 rows=3/3 typed_in_tf=0 cross_firm_leaks=0 evaluator_allowed=3/3 negative_arm=denied other_rows_changed=0 validator=ok ok=True`.
  The first build typed the ARN into two policy files; the issuer refused it and reopened the order (DEC-4 iii, rule 30).
- `python lib/opal_naming.py validate`: OK, 0 refusals, before and after the rows (the worker's two runs).
- The module's rule, read: `infra/aws/terraform/modules/opal_name/main.tf:90-95` reads the registry file and builds, per bucket key,
  the list of row ARNs; both fences consume it (`s3-49financial.tf:141`, `s3-lgic-firm-buckets.tf:162`). The lookup is by bucket key,
  so no bucket without its own row gains the user.

## The plan: NOT measured by this seat

A read-only plan of that root from this session stopped at "Backend initialization required"; this seat did not initialise the root
(an init may fetch providers, and the root is large). So this half does NOT state measured plan lines. It binds on the shape below, and
the executor's own plan is the read (the CTO half says the same of itself):

**Exactly three resources updated in place, 0 to add, 0 to destroy; and in each policy's diff the only change is one added string,
`arn:aws:iam::313476888478:user/cloudops-dell2-agent-user`, inside the `ArnNotLike` list of the `DenyForeignFirmPrincipals` statement.**
Any other resource, any other statement, any other changed value: apply NOTHING and report the plan as read.

**Known in advance, so it is not read as a surprise:** the CRO measured that `modules/opal_name/generated_locals.tf` differs from a
fresh regenerate "in its header registry mark only" (its msg 106127). A header mark is a comment and should not reach a plan. If the
plan shows ANY change traceable to generated locals, that is "any other line": stop.

**Writers of the property moved (who the three fences admit): N = 2 rules, both read.** (1) `fence_patterns` (scope-derived; unchanged);
(2) `fence_exemption_arns` (the registry rows; three rows added). One further typed term exists in the 49financial fence
(`data.aws_iam_role.irpt_performance_adapter.arn`); it predates this act and is not touched.

## Blast radius

The bucket policies of the three fenced firm data buckets. No IAM object, no other bucket of the 24 the census read, no object, no
served output.

**What dell2 gains, at its full width (as the CTO half states it, and this seat agrees):** the fence stops refusing it, so its own two
IAM policies apply on those three buckets: read, list and PUT of objects, and the create policy's bucket-level configuration actions.
Its own Deny statements still refuse any delete of an object or bucket and any lifecycle configuration on `opal-data-*`. This is not a
read-only grant. **dell1 gains nothing:** the census found its placed projects meet no fence (`gap_dell1=0`).

**The fence's control arm, measured before the act:** on the live documents the simulator returns `explicitDeny` for dell2 on all three
buckets and for dell1 on the 49financial bucket; on the edited documents it returns `allowed` for dell2 on all three.

## Rollback per key

S3 keeps no prior version of a bucket policy. BEFORE the apply the executor saves each of the three live policy documents into its
deliverables folder and names them in the ledger entry (condition 3). The census already holds them as read at ~08:4xZ:
`infra/aws/terraform/shared-infra/tests/dell_fence_census.json` (a second copy, older; the executor's save is the reference).
Rollback: the CRO removes the three rows (its lane), the same targeted `safe-apply` runs again, and each policy is compared to its
saved document. Same-window fallback if the registry route is blocked: `s3api put-bucket-policy` of the saved document, one bucket at
a time, then the Terraform re-apply to reconcile state.

## Conditions (this half's, beside the CTO half's four)

1. The plan shape above, read by the executor before the apply.
2. The three prior documents saved and named in the ledger entry before the apply; one entry, naming the laptop.
3. Read-back, LIVE: each of the three live policies equals its prior document plus the one added principal (parsed comparison);
   `iam simulate-principal-policy` with each LIVE bucket policy: dell2 `allowed` on `s3:GetObject` for all three; dell1 NOT allowed on
   all three; and one principal that was refused before and has no row is still refused (the executor picks it from the census and
   names it). The box arms of the CTO half's condition 2 (dell2 reads one object per bucket from dell2 itself) are run by the fabric
   managers' route after the apply and are reported separately; they are not the executor's.
4. A re-plan with the same targets after the apply reads no changes.

## Both branches

Applied: dell2's seats read and land on the three firms' buckets under their own policies; the read-proxy through the laptop ends.
Not applied, or the plan differs: dell2 stays fenced out of all three; the rows stay in the registry, unapplied, and the CRO is told.

## Not covered

Any act dell2 takes on those buckets; a served landing there (its own two halves); a firm bucket added later (a new row and a new
half); an access path outside the bucket policy (an access point, a key policy): the dell2 box read is the test of that.

**SIGNED** -- `2.0.0_SA_COO~C`
