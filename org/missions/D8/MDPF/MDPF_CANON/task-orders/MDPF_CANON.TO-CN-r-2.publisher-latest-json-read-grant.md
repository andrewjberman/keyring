# MDPF_CANON task order -- `CN-r-2` -- THE PUBLISHER ROLE MAY READ THE SERVED MDPF PREFIX (CTO round-9 analysis item 2; the build, never the deploy)


<!-- ===================== WORKER FACE -- this is the WHOLE of the worker's context ===================== -->

<decomp_ref>
<decomp_doc>org/missions/D8/MDPF/MDPF_CANON/decompositions/MDPF_CANON_DECOMP.md</decomp_doc>
<owned_cells>CN-r-2</owned_cells>
</decomp_ref>
<issued_to>0.9.0_WK_MDPF_CANON~30</issued_to>
<issued_by>2.0.0_SA_COO~D1</issued_by>
<placeholders>NONE</placeholders>
<preflight>
comp-schedule: DECLARED-NOT-APPLICABLE -- no cron, alarm, monitor or cadence is added or changed; the cell adds one IAM policy resource to existing Terraform source.
comp-iam: RUN by the issuer (2.0.0_SA_COO~D1) on DELL1, read-only: the role's three inline policies read live (write+list, Gold read, Tax-control read) and the lambda's environment; the live role holds no GetObject on opal-data-portal-v2. The live simulate of the POST-change policy is NOT run (nothing is applied); the check evaluates the parsed Terraform statements instead.
comp-adversary: RUN by the issuer -- r10_cn_r_2.py statement 0 of 5, rest 4 of 4, eval 3 of 5 at base (the passing arms are controls); a scratch reference tree reads 5 of 5, 4 of 4, 5 of 5; 13 planted defects each turn their named arm red; selftest OK.
EGRESS CLASS, declared: NONE (the worker writes no AWS and makes no network call).
</preflight>

## 1. THE CELL -- `CN-r-2` (round 10)

**The gap (measured by the issuer, read-only).** The publisher lambda `opal-assets-mdpf-portal-publisher` runs as `opal-assets-mdpf-egress-publisher-role` (Terraform: `infra/aws/terraform/opal-assets/mdpf_egress_publisher.tf`).
It writes the served MDPF objects under `platinum/mdpf/` in the bucket `opal-data-portal-v2` and keeps a pointer `platinum/mdpf/_manifests/latest.json`. On each run it reads the pointer to learn what it published last, and for a pair whose
inputs have not changed it reads the served object back and compares its hash, then skips the write. The role is not allowed `s3:GetObject` anywhere in `opal-data-portal-v2`, so both reads fail, the lambda treats every pair as new, and every run
republishes all 18 pairs (and the history leaves). This cell adds ONE read-only grant so those reads succeed. It changes Terraform source only. You do not apply anything; a CloudOps seat applies the merged code in its own window after the drain.

**The change (the whole of it).** Append the two blocks below to the END of `mdpf_egress_publisher.tf`, after the last existing block (`resource "aws_iam_role_policy" "mdpf_egress_publisher_taxsma_control"`), separated by one blank line, and add a short ASCII comment
line or two above them naming the cell (`MDPF_CANON.TO-CN-r-2`). The text of the two blocks is byte for byte this:

```
module "mdpf_publisher_live_serve_read_policy_name" {
  source   = "../modules/opal_name"
  system   = "mdpf"
  function = "publisher-live-serve-read"
  kind     = "policy"
}

resource "aws_iam_role_policy" "mdpf_egress_publisher_live_serve_read" {
  name = module.mdpf_publisher_live_serve_read_policy_name.name
  role = aws_iam_role.mdpf_egress_publisher.id

  policy = jsonencode({
    Version = "2012-10-17"
    Statement = [{
      Sid      = "ReadLiveServedMdpf"
      Effect   = "Allow"
      Action   = ["s3:GetObject"]
      Resource = "arn:aws:s3:::${local.platinum_bucket}/${local.mdpf_egress_live_write_prefix}"
    }]
  })
}
```

Both locals already exist in the directory (`local.platinum_bucket` is `opal-data-portal-v2`, defined in `emitter.tf`; `local.mdpf_egress_live_write_prefix` is `platinum/mdpf/*`, defined in `mdpf_egress_publisher.tf`): read their definitions first and confirm, and if either is not what is said here, file a BLOCKING row naming what you read and STOP.
The policy is a SEPARATE resource (like the Tax-control policy above it) so the plan adds one resource and no existing policy changes. It is NOT gated by `count` or `for_each`: the write grant is gated off by `mdpf_egress_live_serve_write_cosigned`,
this read is not, and gating it would leave the unchanged branch dead. The name comes from the `opal_name` builder module, never a typed literal. Do not widen the resource to the bucket, to `json/mdpf/`, to `platinum/etfs/` or to the staging prefix; do not add an action;
do not add a Condition; do not touch the `s3:ListBucket` statement.

**STEP 1 -- read.** Read `mdpf_egress_publisher.tf` from top to bottom and `infra/aws/terraform/modules/opal_name/main.tf`. Note that the file already carries three non-ASCII characters in old comments: leave every existing byte alone and add ASCII only.

**STEP 2 -- edit.** Use the Edit tool (or Write on the whole file with every existing line unchanged) to append the blocks. The file's line endings stay as they are.

**STEP 3 -- format.** Run `terraform fmt -check infra/aws/terraform/opal-assets/mdpf_egress_publisher.tf` from the worktree root. If it prints the file name or exits non-zero, run `terraform fmt infra/aws/terraform/opal-assets/mdpf_egress_publisher.tf` and read the diff: it may touch only your added lines;
if it would reformat an existing line, undo and file a row. `terraform fmt` is a local formatter and is the only terraform command you may run.

## 2. BOUNDS

1. **No AWS call of any kind and no terraform command except `terraform fmt`**: no `init`, `plan`, `validate`, `apply`, `safe-apply`, no `aws`, no `s3`, no `lambda`, no invoke, no push. Read-only repository access is allowed. The criteria make no network call. REFUSE, do not rescue.
2. Only the one `.tf` file in section 3 changes (plus your deliverables and the surprise channel). The other 22 files of `infra/aws/terraform/opal-assets/` and `infra/aws/terraform/modules/opal_name/` are byte-equal to base at the end, and `mdpf_egress_publisher.tf` equals base plus exactly the two blocks and your comment lines (the criteria hash the rest).
3. **Never** add an action other than `s3:GetObject`, a resource other than the one in the block, a `Condition`, a `count`, a `for_each`, a typed policy name, or any non-ASCII character. Never edit the write, list, Gold or Tax-control grants.
4. **CLIENT DATA:** none is involved; print no credential. No non-ASCII in what you write.
5. If an item cannot be met within your paths, file a row and stop on that criterion.

## 3. SURFACES

<paths>
infra/aws/terraform/opal-assets/mdpf_egress_publisher.tf
org/missions/D8/MDPF/MDPF_CANON/task-orders/MDPF_CANON.TO-CN-r-2.publisher-latest-json-read-grant.md
org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~30/
org/missions/D8/MDPF/MDPF_CANON/surprise-channel/investigations/INVESTIGATION_v1.md
</paths>

Read-only: the whole repository, in particular `infra/aws/terraform/opal-assets/` (the other files), `infra/aws/terraform/modules/opal_name/main.tf`, `infra/aws/lambda/opal-assets/opal-assets-mdpf-portal-publisher/lambda_function.py` (what the reads are for), and the issuer's check
`org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/checks/r10_cn_r_2.py` (read it, never edit it).

## 4. PROOF OF SPEC (literal; timeout 120 per invocation)

<proof_of_spec>
  <criterion id="AC1" cell_refs="CN-r-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 120 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/checks/r10_cn_r_2.py" statement; echo "exit=$?"</invocation><expect>CN-R-2 STATEMENT: 5 of 5 arms -- and exit=0</expect></criterion>
  <criterion id="AC2" cell_refs="CN-r-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 120 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/checks/r10_cn_r_2.py" rest; echo "exit=$?"</invocation><expect>CN-R-2 REST: 4 of 4 arms -- and exit=0</expect></criterion>
  <criterion id="AC3" cell_refs="CN-r-2"><invocation>cd "$(git rev-parse --show-toplevel)" &amp;&amp; timeout 120 python "org/missions/D8/MDPF/MDPF_CANON/deliverables/2.0.0_SA_COO~D1/round10/checks/r10_cn_r_2.py" eval; echo "exit=$?"</invocation><expect>CN-R-2 EVAL: 5 of 5 arms -- and exit=0</expect></criterion>
</proof_of_spec>

- `AC1`: the added policy is PARSED from the real Terraform source: one resource attached to the publisher role, one statement, Allow, `s3:GetObject` only, exactly the resource `arn:aws:s3:::opal-data-portal-v2/platinum/mdpf/*`, no Condition, NotAction, NotResource or Principal; the name is the builder module's output; no `count` or `for_each`; ASCII added only.
- `AC2`: nothing else moved: the file minus the two added blocks equals the base (comments and blank lines ignored), the block inventory is the base plus the two, the 22 neighbouring files are byte-equal, and `terraform fmt -check` parses the file.
- `AC3`: the role's policy documents are EVALUATED with S3 object-level matching: GetObject on `latest.json` and on eight served keys is allowed; it stays DENIED on `json/mdpf`, `platinum/etfs`, the staging prefix and two other buckets; the existing Gold and Tax-control reads still hold; the write set is unchanged (Put on `platinum/mdpf` and staging allowed, on `json/mdpf` and the Gold tree denied, Delete denied).

## 5. WHEN YOU ARE DONE

Write the instance at
`org/missions/D8/MDPF/MDPF_CANON/deliverables/0.9.0_WK_MDPF_CANON~30/MDPF_CANON.TO-CN-r-2.publisher-latest-json-read-grant.proof_of_spec.json`
(beside the order's own file stem, which is the name the pipeline gate searches for). **Flip this order's `<status>` to `complete` in the SAME commit as your proof instance** (the order file is in your paths), and only when every criterion passes.
A row id on this project carries the dell1 infix: `MDPF_CANON-D1-W30-S<k>`, with `surfaced_at` taken from `date -u +%FT%TZ` at filing.
Report once: the diff (one line per file), the output line of every criterion, the commit hash, and any row.

<!-- ===================== RECORD FACE -- does NOT travel to the worker ===================== -->

**ISSUER NOTES:** round 10, issuer 2.0.0_SA_COO~D1, on the CTO's round-9 analysis section 4 item 2 and section 3 (b) (`ROUND_ANALYSIS.round9.md`; `1.0.0_SA_CTO~DELL1`).
- **Risk and class:** WORLD, because `.tools/to-pipeline-gate.py` GATE (xii) floors any `<paths>` entry under `infra/` at WORLD. What the worker does is LOCAL (source and `terraform fmt`). The WORLD act is the apply, cut as a separate order: `ADHOC.canon-r10-publisher-latest-read-deploy` (`0.7.0_AE_CloudOps~DELL1`).
- **Where this contradicts the CTO's ask and CloudOps' measurement (visible at the round-N analysis):** the ask says "one read-only IAM element ... a read of `latest.json`". A grant on `latest.json` ALONE does not end the republish. `_publish_one` reads the pointer (needs `latest.json`), then, when the Tax switch is ON and the prior row carries `served_sha256`, reads the SERVED object
  (`platinum/mdpf/<scope>/...`) and compares its hash; a denied read there sets `served_ok` false and the pair republishes ("REPAIR"). So the grant is on `platinum/mdpf/*`, the same prefix the role already writes (its NEVER#3 record scoped the role to `platinum/mdpf/*`), not on the pointer key. The check's arm `latest-only` (a mutant granting the pointer alone) turns E2 red for this reason.
  The width is a read of what the role itself writes; it reads no `json/mdpf`, `etfs`, staging or other bucket (E3).
- **Do the "18 of 18" and the "unchanged" claim hold?** Only while no gold or Tax-control input has moved since the pointer row was written. If any pair's input moved, that pair publishes for a true reason; the deploy order's proof reads the manifest per pair.
- **Never-widen:** the apply widens a ROLE (one new read), and the single proof run is expected to write nothing. Whether CTO+COO name the read grant and that one run as a pair is the issuer's call; this draft does not decide it.
- **What the checks cannot prove (stated, not hidden):** the Terraform plan was NOT run (no provider init on this box: "1 to add" is expected from the separate-resource shape, not measured); the live post-change `simulate-principal-policy` is not exercised (the check evaluates the parsed statements with its own S3 matcher, validated against the live role's present documents as the positive and negative controls); the simulator also returns NOT-DECIDABLE without an `s3:prefix` context on the pre-change role, so the live before-print needs the context keys the deploy order names.
- **Pre-cut dry run (base box/dell1 @ccb162ba19):** AC1 0 of 5, AC2 4 of 4 (controls), AC3 3 of 5 (E3, E4, E5 controls). Reference tree 5/4/5. `worker-light` was considered: the cell is about 25 product lines, but the blocks are byte-exact and the arms are strict; class `worker-light` is acceptable (issuer's call).
- **Fanout:** one cell, one chain, slot ~30, no edge to the other round-10 cells. Base box/dell1.

<status>complete</status>
<round>10</round>
<to_id>MDPF_CANON.TO-CN-r-2</to_id>
<slot>~30</slot>
<fabric>dell1</fabric>
<risk>WORLD</risk>
<worker_class>worker</worker_class>
