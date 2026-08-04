# T5 DEAD-CONSUMER KILL K1 -- mdpf-freshness-checker IAM role family (change record + rollback note)

**Executor:** 0.7.0_AE_CloudOps~F | **Opened:** 2026-08-04T04:37Z | **Status:** OPEN (closes on verified destroy)
**Authorization:** COO GO 20260804T042634Z, under CTO split-gate ruling 042600Z, under Andrew's categorical
word; checker family independently ruled TERMINATE by Andrew 0343Z (doubly dead). Kill-list row 17
(@39c51b487e amendment #2; CVO census item 5).

## WHAT DIES (exactly, nothing else)

Three Terraform resources in `infra/aws/terraform/mdpf-pipeline/iam.tf` (block :759-842 pre-removal):
1. `aws_iam_role.mdpf_freshness_checker_lambda` (live name `mdpf-freshness-checker-lambda-role`, created 2026-06-02)
2. `aws_iam_role_policy_attachment.mdpf_freshness_checker_basic` (AWSLambdaBasicExecutionRole attachment)
3. `aws_iam_role_policy.mdpf_freshness_checker_lambda` (inline policy `mdpf-freshness-checker-scoped`)

## WHY DEAD (reader evidence, already banked)

The Lambda this role serves (`mdpf-freshness-checker`) DOES NOT EXIST -- torn down pre-07-29 (T1.A
positive-controlled: ResourceNotFoundException vs control rc=0; the 22-destroy teardown in
mdpf-pipeline CHANGELOG kept only the role). A role assumable only by lambda.amazonaws.com with no
function is a principal that cannot act: **zero readers by construction** (CVO census item 5,
role-without-function). Under-reporting-IAM caution (Rule 22a) does not apply: that caution protects
grants a live caller needs invisibly; here the CALLER ITSELF is nonexistent and the family is
sovereign-ruled TERMINATE.

## MECHANISM

TF-managed, mdpf-pipeline root -> dies via source removal + targeted `safe-apply` (Rule 18), targets =
the three state addresses above. No other iam.tf resource references the block (grep 0 cross-refs).

## ROLLBACK

`git revert` the source-removal commit + targeted `safe-apply` recreates all three byte-identically
(role + attachment + inline policy are fully declared in source; no external state). Historical
definition preserved at iam.tf@440d16e018:759-842.

## POST-KILL VERIFY (filled at close)

- `aws iam get-role --role-name mdpf-freshness-checker-lambda-role` -> NoSuchEntity: [pending]
- Access evidence window: IAM has no per-role access logs wired here; last-accessed evidence =
  the nonexistent principal (structural zero). Stated honestly: no log window exists or is needed --
  a role with no function cannot have been used since the function's teardown.
