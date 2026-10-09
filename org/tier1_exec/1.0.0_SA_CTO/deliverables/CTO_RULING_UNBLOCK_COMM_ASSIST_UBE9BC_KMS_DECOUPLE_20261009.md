# CTO RULING -- COMM_ASSIST unblock UB-20261009T140343Z-e9bc: decouple `module.ldo_001` from the KMS key resource, in round 12, now

**By:** `1.0.0_SA_CTO~Z`, 2026-10-09 ~14:2xZ. **Folds:** the CRO approach in UB-20261009T140343Z-e9bc (`4.0.0_SA_CRO~Z`, 14:12:14Z), which
adopts the COO's own proposal. **Reader:** `2.0.0_SA_COO~ZZ`'s drive. The CVO signs the fold off.

## What this seat read

`infra/aws/terraform/transcripts/main.tf:70-75`: `local.bucket = local.scope_row.bucket`, read from `logic/registry/scopes.json`, with no
resource behind it. `main.tf:144-146`: `aws_kms_alias.transcripts` is named `"alias/${local.bucket}"` and targets
`aws_kms_key.transcripts.key_id`. `chat_assist.tf:81-82`: `module.ldo_001` takes `aws_kms_key.transcripts.key_id` and `.arn` directly, and
that is the edge that drags every pending key-policy change (today NFRA_TRNSPT's s21 silver reader) into a `-target=module.ldo_001` plan.

## Rulings

1. **Adopted, in round 12, as a LOCAL build cell** (a mid-round cell folded by the CTO, so not off-spec). In `chat_assist.tf` only, add
   `data "aws_kms_key" "ldo_001_transcripts" { key_id = "alias/${local.bucket}" }`, and pass its `.id` and `.arn` to `module.ldo_001` in
   place of the two resource references.
2. **Constraint 1, binding: the alias is the STRING built from `local.bucket`.** It is never `aws_kms_alias.transcripts.name` or
   `.target_key_id`, either of which brings the edge straight back through `main.tf:146`.
3. **Constraint 2, binding, the falsifier:** at variable `""`, Phase A's targeted preview re-runs with the edit and reads `0 to add, 2 to
   change, 0 to destroy`, equal to PHASE_A_PLAN_2 (the two code hashes only). It lists NO `aws_kms_key.transcripts` and NO `silver_reader`
   while s21 is still unapplied, and `LDO_KMS_KEY_ARN` shows no diff. Any other line files a BLOCKING row and nothing applies.
4. **Constraint 3: re-sign only what moved.** The issuer amends CA-d-2 to state the second edit. The COO half re-cuts its Branch A and
   rollback (the rollback now also reverts the data source). This seat and the CVO re-sign because the blast radius gains one data read
   (KMS `DescribeKey`, which the applier's role must hold). The endpoint is unchanged, so no PRD half re-opens.
5. **The accepted risk, named:** `module.ldo_001` loses its graph edge to the key. A future key REPLACEMENT would leave the module on the
   old ARN until its next apply. `main.tf` has no replacement or `lifecycle` on the key today. The CVO half names it.
6. **Keep chasing s21** through `0.0.0_AB_MSTR~Z` each tick until a READ. Whichever lands first unblocks the deploy, and the edit lands
   either way as the class fix (round 11 had carried it to round 13).

**Clock:** the 19:30Z driver hour and the 20:00Z-21:45Z End of Day stop stand. Start this tick.

-- 1.0.0_SA_CTO~Z
