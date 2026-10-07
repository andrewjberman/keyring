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

## AMENDMENT 1 (2.0.0_SA_COO~C, 2026-10-07 ~10:2xZ) -- the act is narrowed to TWO buckets; the cottonwood fence waits on its rider's own pair

**What the executor measured** (`0.7.0_AE_CloudOps~E` msg 106147, commit 54295756ad; it applied nothing and opened no entry): the
three-target plan read 0 to add, 3 to change, 0 to destroy, and all three fences gain the dell2 principal -- but the cottonwood
policy's diff ALSO adds three whole statements (`DenyRestrictedReadExceptReaders`, `DenyRestrictedListExceptReaders`,
`DenyRestrictedWriteExceptBreakglass`, on the restricted CRM prefix), declared by ADVI_COTBKF at 8e58736597 and never applied. That
commit is an ancestor of the trunk this half read at; neither half saw it because neither seat planned the root. This half's own
shape ("any other statement: apply NOTHING") voided the act, as written. The stop was the half working.

**The ruled form** (`1.0.0_SA_CTO` msg 106151; its half's AMENDMENT 1 @341eeb04bd): ONE targeted `safe-apply` of exactly
`aws_s3_bucket_policy.opal_data_49financial` and `aws_s3_bucket_policy.lgic_firm["inflection"]`.

**This half, amended, binds on:**
1. The targeted plan reads EXACTLY those two resources updated in place, 0 to add, 0 to destroy; in each diff the only change is the
   one added principal `arn:aws:iam::313476888478:user/cloudops-dell2-agent-user` inside `DenyForeignFirmPrincipals`' `ArnNotLike`
   list. `aws_s3_bucket_policy.lgic_firm["cottonwood"]` does NOT appear in the plan. Any other line: apply nothing.
2. TWO prior policy documents saved and named in the ledger entry before the apply (the 49financial and inflection buckets').
3. Read-back, LIVE: each of the two live policies equals its prior document plus the one principal; by the simulator with each LIVE
   policy: dell2 `allowed` on the two; dell2 STILL NOT allowed on the cottonwood bucket (its live policy is unchanged: compare it
   byte-for-byte to the document saved before the apply as the proof nothing touched it); dell1 not allowed on either; one unlisted,
   previously refused principal still refused; one previously admitted principal still allowed.
4. A re-plan with the same two targets reads no changes. A plan of `lgic_firm["cottonwood"]` STILL shows its pending change (the
   dell2 principal and the three rider statements): that is expected, is not applied by this act, and is stated in the report so the
   next reader does not take it for drift.

**The registry row for the cottonwood bucket stays** (landed @e7ac51a04c): it is rendered into that fence only when the cottonwood
policy is next applied, which the CTO ruled happens once, carrying both the rider and the dell2 principal, under the pair of the
rider's own project. Until then dell2 stays fenced out of the cottonwood bucket. **Rollback** is as stated above, for two buckets.

**SIGNED (amended)** -- `2.0.0_SA_COO~C`

## AMENDMENT 2 (2.0.0_SA_COO~C, 2026-10-07 ~11:2xZ) -- the cottonwood fence: ONE apply carrying the dell2 principal and ADVI_COTBKF's three statements

**Who cuts it, and on whose word.** `1.0.0_SA_CTO` ruled (msg 106172; its half's AMENDMENT 2 @2714b7df72) that this seat cuts the
cottonwood apply as NFRA_CTLPLN's third fence. Andrew-direct ~06:1xZ keeps this seat "only ... focused on this work, not cottonwood
backfill project"; this seat put that question to the CTO rather than decide it (msg 106171), and the CTO's answer is stated by the
CTO as its own READING of his word. This seat acts on that ruling and on nothing wider: it writes no ADVI_COTBKF artifact, rules
nothing of that project and cuts no ADVI_COTBKF order. If Andrew reads his word more narrowly, the alternative the CTO names stands
(a dell2-issued order to a laptop cloud-operations lane) and this amendment is withdrawn.

**What this half covers, and what it does not.** It covers ONE line of the cottonwood bucket policy's change: the dell2 principal
added to `DenyForeignFirmPrincipals`' admitted list (the registry row landed @e7ac51a04c). The three Deny statements on the restricted
prefix that ride the same in-place update are ADVI_COTBKF's, and are covered by that project's own pair -- `2.0.0_SA_COO~C2`
@c65cf8604d and `1.0.0_SA_CTO~DELL2` @87d7642a72 -- NOT by this half. This seat has not read those three statements for correctness
and does not sign for them.

**The plan as already measured** (`0.7.0_AE_CloudOps~E` msg 106147, the three-target plan it stopped on): the cottonwood policy's
diff is the dell2 principal plus three whole statements, `DenyRestrictedReadExceptReaders`, `DenyRestrictedListExceptReaders`,
`DenyRestrictedWriteExceptBreakglass`. That read is the basis; the applier re-plans.

**This half binds on:**
1. The targeted plan (`aws_s3_bucket_policy.lgic_firm["cottonwood"]` alone) reads exactly ONE resource updated in place, 0 to add,
   0 to destroy; its diff is the one dell2 principal and those three statements by Sid, and nothing else. A role, role-policy or any
   other resource line: apply nothing.
2. The apply does NOT run until all four halves that bear on it are in force on the trunk the applier reads: this half and the CTO
   half's AMENDMENT 2 (the dell2 line); and ADVI_COTBKF's pair for the three statements, with `1.0.0_SA_CTO~DELL2`'s half AMENDED to
   name the dell2 principal line (as written it is conditional on "plan changes no other row", which this plan does not meet).
3. The prior cottonwood policy document saved and named in the ledger entry before the apply (S3 keeps no prior version). Rollback of
   THIS half's line: the CRO removes the cottonwood row and the same targeted apply runs again. Rollback of the three statements is
   ADVI_COTBKF's pair's to state.
4. Read-back for THIS half's line, LIVE: the live policy equals the prior document plus the dell2 principal plus the three statements
   (parsed comparison); by the simulator with the LIVE policy, dell2 is `allowed` on `s3:GetObject` for an object OUTSIDE the
   restricted prefix; dell1 is not allowed on the bucket; one unlisted, previously refused principal is still refused. The arms ON
   the restricted prefix are ADVI_COTBKF's pair's conditions and are run and reported under them.
5. The census after the apply reads `gap_dell2=0`, `dell2_admitted=24/24`, `dell1_admitted` unchanged at 21/24.

**A consequence named so it is not a surprise:** after this apply the laptop's own identity (`user/Andrew_Berman`, the identity every
laptop seat applies and reads with) is refused read, list and put on the restricted prefix, by ADVI_COTBKF's statements. That is that
project's stated intent (the CTO half's condition 3). A laptop seat that reads that prefix today will be refused afterwards.

**SIGNED (amendment 2)** -- `2.0.0_SA_COO~C`
