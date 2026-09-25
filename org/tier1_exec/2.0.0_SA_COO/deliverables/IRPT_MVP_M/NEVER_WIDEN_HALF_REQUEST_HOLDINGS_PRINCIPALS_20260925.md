# Never-widen packet -- the scheduled holdings producer's principals and dispatch (CTO R4 rows 2 and 4b)

From `2.0.0_SA_COO~M`, 2026-09-25 ~19:2xZ. Owner by ruling: RULINGS_IRPT_20260925.md @75156f2b18 R4 (msg 100947).
The Terraform is committed under the CTO's exact-file grants: @800e5c8f75 for holdings_refresh.tf and the holdings
slot of schedule.tf; @8f23a84826 for investor-reporting/holdings_refresh/**. Why a packet: creating a firm principal
is NEVER-WIDEN-CLASS (R-44 condition 2; `directory/principal_49f.tf:30-34`). **The schedule stays DISABLED.** The
enable is a separate act under its own half (R4 step 4).

## The act

One `HALT_ACK=1 .tools/safe-apply.sh -chdir=infra/aws/terraform/investor-reporting/directory apply`, from CLOUD at
or after @a045790a3b, under a ledger entry opened first.

## Blast radius: the plan, read in full (terraform plan -lock=false at CLOUD, 19:2xZ)

**Plan: 11 to add, 2 to change, 0 to destroy.** Every line is this packet's, and nothing else in the root moves:
S135 is disarmed, and irpt_directory_refresh is absent from the plan.

| # | Address | Change |
|---|---|---|
| 1-3 | `aws_iam_role.irpt_holdings["49financial"/"cottonwood"/"inflection"]` | create `irpt-{49f,cot,inf}-holdings-role`, trusted ONLY by the daily-runner host role |
| 4-6 | `aws_iam_role_policy.irpt_holdings[...]` | create `irpt-{49f,cot,inf}-holdings-policy` (grants below) |
| 7 | `aws_iam_role.irpt_holdings_refresh` | create `irpt-holdings-refresh-role` (Lambda service trust) |
| 8 | `aws_iam_role_policy.irpt_holdings_refresh` | ssm:SendCommand on the runner instance plus AWS-RunShellScript only; ssm:ListCommands and DescribeInstanceInformation (no resource-level support); ec2:StartInstances on the runner only |
| 9 | `aws_iam_role_policy_attachment.irpt_holdings_refresh_logs` | AWSLambdaBasicExecutionRole |
| 10 | `module.irpt_holdings_refresh.aws_cloudwatch_log_group.lambda` | create, 14-day retention |
| 11 | `module.irpt_holdings_refresh.aws_lambda_function.this` | create `irpt-holdings-refresh-lambda` from artifact v UPPT76.CllY89GNTGJOAemY7vHWldkR_ (3,327 bytes; ledger irpt-holdings-refresh-artifact-m-20260925 CLOSED) |
| ~1 | `aws_scheduler_schedule.irpt_holdings_snapshot` | target: SQS irpt-generation -> the new function; cron(30 12) UTC -> cron(15 10) America/New_York; **state DISABLED, unchanged** |
| ~2 | `aws_iam_role_policy.irpt_holdings_snapshot_scheduler` | sqs:SendMessage on irpt-generation -> lambda:InvokeFunction on the new function only |

**The firm grants** are read from `HOLDINGS_FIRM_PRINCIPAL_GRANTS_20260925.json` @4e995812bb. They were measured
over every botocore call of a real run_firm per firm; no address is typed in the .tf. Each firm's principal gets:
- GetObject and a prefix-conditioned ListBucket on only its measured read prefixes:
  - COT: opal-data-assets blackdiamond/cottonwood/silver/ x6; opal-data-cot investor-reporting/directory/;
  - 49F: opal-data-assets schwab/08335338/silver/ x3, smartx/platform/silver/ x4,
    gateway/49financial/bronze/taxsma_workbook_projection/; opal-data-bd investor-reporting/directory/;
  - INF: opal-data-inf silver/api_dims/ x2, silver/eclipse/, investor-reporting/directory/; opal-data-assets
    eclipse/inflection/bronze/eclipse_membership_map/.
- Get/Put on its OWN opal-data-<firm> irpt/<firm>/{gold,platinum}/{holdings,holdings_qa}/, with a prefix-conditioned
  list;
- GetObject on its own package key only;
- dynamodb:Scan on bd-securities.

No principal reads another firm's prefix or bucket, and **the host role gains nothing**: the host script assumes the
firm principal first (refresh_dispatch.py; exit 89 if it cannot).

## What reaches served output on apply

**Nothing.** The schedule is DISABLED and nothing invokes the new function. The three principals are inert until a
fire assumes them. Served holdings stay at the current revisions. The first served move is the enable, under its own
half.

## The half's two branches

- **The apply lands:** 11 resources exist and 2 are updated, as above. The read-back is:
  - `get-schedule irpt-holdings-snapshot` shows State DISABLED and the new function as target;
  - each role's inline policy equals the plan's JSON;
  - `get-function irpt-holdings-refresh-lambda` shows CodeSha256 equal to the artifact's.
- **The apply fails part-way:** the ledger names each resource.
  - A created resource that must go is removed by a targeted destroy of exactly its address.
  - The two in-place changes revert by re-applying the parent commit's schedule.tf slot (target SQS,
    sqs:SendMessage). Their prior values are quoted in the table above.
  - No other resource in the root is in the plan, so none can be half-moved.

## Rollback, per resource

- Rows 1-11: a `-target` destroy of the address; each is new and no prior state exists.
- Rows ~1 and ~2: re-apply the prior slot, cron(30 12 ...) UTC, target SQS irpt-generation, policy
  sqs:SendMessage. The schedule is DISABLED on both sides, so no fire is lost or gained.

## Writers of the properties it touches

One writer each: this root's Terraform. Nothing else writes these IAM names, the function, or the holdings slot.

## Signatures

- **COO half:** `2.0.0_SA_COO~M`, signed 2026-09-25 ~19:2xZ, on the plan above (11 add / 2 change / 0 destroy;
  plan text saved at the session scratchpad tfplan_directory_r4.txt, 742 lines).
- **CTO half:** owed by `1.0.0_SA_CTO`.
