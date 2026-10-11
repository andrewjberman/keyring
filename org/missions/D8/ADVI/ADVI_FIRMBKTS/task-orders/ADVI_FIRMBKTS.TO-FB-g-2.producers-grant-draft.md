# ADVI_FIRMBKTS task order -- `FB-g-2` -- THE PRODUCERS' ROLE GRANT FOR THE CANONICAL PLATINUM HOME: DRAFTED, NOT APPLIED (AMENDED)

<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/ADVI/ADVI_FIRMBKTS/decompositions/ADVI_FIRMBKTS_DECOMP_R4.md</decomp_doc>
<owned_cells>FB-g-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_ADVI_FIRMBKTS~36</issued_to>
<issued_by>2.0.0_SA_COO~B1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- a Terraform module call and policy resource in repository source; no cron, rule, schedule or cadence is added or changed and nothing is applied.
comp-iam: DECLARED-NOT-APPLICABLE -- the cell DRAFTS the grant; it makes no AWS call and creates no principal or policy in AWS. The grant is its own act (FB-g-8) under its own signed pair; the actor reads the policy against the live role at that act.
comp-adversary: RUN by the issuer -- at base `r4_grant.py` reads 1 of 4 (G4 passes as a control: `terraform fmt -check` is clean; G1 to G3 FAIL as expected); on a fixture tree holding the conforming module call and resource it reads 4 of 4. Blindness: the check reads the policy text; it cannot say that the role's other 16 inline policies or its permission boundary leave the new Allow in force (the act's plan and a live get-role-policy read that), nor that the module outputs resolve at plan time (the act's scoped plan reads that).
EGRESS CLASS, declared: NONE.
</preflight>

## 1. THE CELL -- `FB-g-2` (round 4, enrichment item 1, the producers' role grant; row D1-S18; the CTO's ADDENDUM 4)

The gold producers run on instance profile `bd-exporter-profile`, role `bd-exporter-ec2-role` (Terraform:
`aws_iam_role.bd_exporter`, `infra/aws/terraform/bd-pipeline/iam.tf`). The role holds NO Allow for `s3:PutObject` or `s3:GetObject` on the canonical home of
the served platinum, and its only ListBucket allow on that bucket (`AdviChain49fListScoped`) is conditioned on other
prefixes. Once the producers' mode is `canonical` every put, get and list at the new home is refused. You DRAFT the grant as
one module call and one additive policy resource. Nothing is applied. **The policy name, the bucket and the prefix are
no longer typed**: the naming gate refused them (row D1-W25-S1) and the CTO ruled they come from the `opal_name` module
(`name` output, and the `bucket` and `platinum_prefix` outputs cell FB-g-13 added, merged).

### 1a. The resources (the whole spec)

Append to the END of `infra/aws/terraform/bd-pipeline/iam.tf`, in the file's own style (two-space indent, `jsonencode`, a short header comment naming this
cell and row D1-S18), exactly this module call and resource:

```
module "opal_name_platinum_grant" {
  source   = "../modules/opal_name"
  system   = "advi"
  scope    = "49financial"
  function = "platinum-canonical-rw"
  kind     = "policy"
}

resource "aws_iam_role_policy" "bd_exporter_advi_49f_platinum_canonical" {
  name = module.opal_name_platinum_grant.name
  role = aws_iam_role.bd_exporter.id
  policy = jsonencode({ Version = "2012-10-17", Statement = [ ...exactly the two statements below... ] })
}
```

Statement 1, `Sid = "AdviPlatinumCanonicalObjects"`: `Effect = "Allow"`, `Action = ["s3:PutObject", "s3:GetObject"]`,
`Resource = ["arn:aws:s3:::${module.opal_name_platinum_grant.bucket}/${module.opal_name_platinum_grant.platinum_prefix}*"]`.

Statement 2, `Sid = "AdviPlatinumCanonicalList"`: `Effect = "Allow"`, `Action = ["s3:ListBucket"]`,
`Resource = ["arn:aws:s3:::${module.opal_name_platinum_grant.bucket}"]`, `Condition = { StringLike = { "s3:prefix" =
["${module.opal_name_platinum_grant.platinum_prefix}*"] } }`.

**No `s3:DeleteObject`**, **no literal bucket, prefix or firm in any statement, no other resource, no `*` resource, no
Deny.** The module call's `scope` argument is the one place the firm's long form appears (a module argument is where the
gate permits it). The file's existing resources are untouched (a pure addition: zero deleted lines). Run `terraform fmt`
on the file.

## 2. BOUNDS

1. One file changes: `infra/aws/terraform/bd-pipeline/iam.tf` (an appended module call and resource). No `terraform init`, plan or apply; no AWS call of
   any kind (the module's outputs are read from `modules/opal_name`, which you read and do not edit).
2. Do not edit `aws_iam_role.bd_exporter`, any existing policy, the module, or `CHANGELOG.json`.
3. If the commit is refused by the naming gate, do not override or force: file a BLOCKING row with the gate's lines.
4. ASCII only; LF endings. If something cannot be met within your paths, file a surprise row and stop.

## 3. SURFACES

<paths>
infra/aws/terraform/bd-pipeline/iam.tf
org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~36/
org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the rest of the repository, the checks under `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/`.

## 4. PROOF OF SPEC (literal)

<proof_of_spec>
Instance at `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~36/ADVI_FIRMBKTS.TO-FB-g-2.producers-grant-draft.proof_of_spec.json`.
  <criterion id="AC1" cell_refs="FB-g-2"><invocation>cd /c/dev/wk-firmbkts-36 &amp;&amp; timeout 100 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_grant.py --arms grant --root /c/dev/wk-firmbkts-36; echo "exit=$?"</invocation><expect>ROUND 4 GRANT: 4 of 4 arms</expect></criterion>
  <criterion id="AC2" cell_refs="FB-g-2"><invocation>cd /c/dev/wk-firmbkts-36 &amp;&amp; timeout 60 python org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/2.0.0_SA_COO~B1/round4/checks/r4_scope.py --root /c/dev/wk-firmbkts-36 --allow infra/aws/terraform/bd-pipeline/iam.tf --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~36/ --allow org/missions/D8/ADVI/ADVI_FIRMBKTS/surprise-channel/investigations/INVESTIGATION_v1.md --require infra/aws/terraform/bd-pipeline/iam.tf; echo "exit=$?"</invocation><expect>ROUND 4 SCOPE: OK</expect></criterion>
</proof_of_spec>

AC1 reads the module call, the resource, its statements (built from the module outputs, nothing typed), the additive diff
against the commit the worktree was cut from, and `terraform fmt -check`. AC2 is the write-surface bound. Each invocation
terminates inside its bound.

## 5. WHEN YOU ARE DONE

Instance at `D/ADVI_FIRMBKTS.TO-FB-g-2.producers-grant-draft.proof_of_spec.json`, `D` = `org/missions/D8/ADVI/ADVI_FIRMBKTS/deliverables/0.9.0_WK_ADVI_FIRMBKTS~36`.
Commit `infra/aws/terraform/bd-pipeline/iam.tf`, then the instance second. **Do not flip this order's `<status>`** (the issuer drains it). Row ids:
`ADVI_FIRMBKTS-D1-W36-S<k>`, `k` from 1, `surfaced_at` from `date -u +%FT%TZ`. Report once: AC1 and AC2 outputs and the
commit hash.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**AMENDMENT 2 (2.0.0_SA_COO~B1, 2026-10-11 ~13:xxZ; the CTO's round-3 ADDENDUM 4, msg 3853; rows D1-W25-S1, S2):** the
first seat (`~25`) drafted the grant with typed names and ARNs and passed AC1; the enforcing naming gate refused the
commit (`advi-49f-platinum-canonical-rw` out of pattern, the ARN a hand-kept carrier of the firm). Re-seated on slot `~36`
over the merged `FB-g-13`: the policy name is the module's `name` output, the ARNs its `bucket` and `platinum_prefix`
outputs. `<issued_to>` and the criteria are amended by the issuer; GATE viii reads `<placeholders>NONE</placeholders>` at
HEAD and no token in an invocation.

**ISSUER NOTES:** class WORLD by path floor, drafted not applied. The QA runner shares this role (row D1-S18's world_is),
so the grant also reaches it; the pair names that. The grant is least-privilege to one prefix; Delete is held back on
purpose. FB-g-8 (staged) applies it: the scoped `-target` must name BOTH the module and the resource (the policy reads the
module's outputs), the ledger entry, both pair halves, then a live get-role-policy read. The policy's live NAME is now
`advi-49f-platinum-canonical-rw-policy` (the builder's output); FB-g-8's criteria are amended to it at un-park.

<status>pending</status>
<round>4</round>
<to_id>ADVI_FIRMBKTS.TO-FB-g-2</to_id>
<slot>~36</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
