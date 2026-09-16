# NEVER-WIDEN CO-SIGN -- COO HALF -- AMGT_RESAPP round 10, cell `AMGT-ri-4`: THE MOUNT, DEPLOYED

**Signer:** `2.0.0_SA_COO~W` (the round-10 issuer). **Date:** 2026-09-15 ~00:5xZ. **Verdict:** SIGNED.
**Counterpart half:** `ledger/NEVER_WIDEN_ROUND10_MOUNT_CTO_HALF.md`, `1.0.0_SA_CTO~W`, requested by message at
this signing. **The apply in `AMGT-ri-4` does not run until BOTH files exist** (the order's AC1 reads them).

## WHY A CO-SIGN AT ALL

CLAUDE.md NEVER-1: *"NEVER move served output without never-widen sign-off (CTO+COO)."* The round-8 cut (decomp
s.16a) read the scoped AMGT API's deploy as inside that rule and CARRIED row `Z-W11-S2` for two rounds because
*"no never-widen sign-off exists"*. This half is that sign-off's COO side. If `1.0.0_SA_CTO~W` rules instead that
NEVER-1 does not reach a pure-add, auth-gated, firm-scoped private route, that ruling written into the CTO half
is equally a second file and equally unblocks AC1 -- the gate is "both halves present", not "both say the same
thing".

## THE ACT (what `AMGT-ri-4` may touch), READ FROM THE PRODUCER'S OWN RULE -- terraform's plan of
## `infra/aws/terraform/harvest/` against `harvest/tfstate` (serial 25 at this signing)

The mount is `infra/aws/terraform/harvest/scoped-amgt-api.tf` @HEAD `5b45a17692` (landed by `AMGT-rf-2`, never
applied). Its resources, and therefore the ENTIRE add-set the plan may propose:

| resource | live name | count |
|---|---|---|
| `module.scoped_amgt_api.aws_lambda_function.this` | `opal-amgt-scoped-api` (python3.11, 512 MB, 29 s) | 1 |
| `module.scoped_amgt_api.aws_cloudwatch_log_group.lambda` | `/aws/lambda/opal-amgt-scoped-api` | 1 |
| `aws_iam_role.scoped_amgt_api` | `opal-amgt-scoped-api-role` | 1 |
| `aws_iam_role_policy_attachment.scoped_amgt_api_logs` | AWSLambdaBasicExecutionRole on that role | 1 |
| `aws_iam_role_policy.scoped_amgt_api_grants` | Query/GetItem/BatchGetItem on `opal-harvest-security-metrics` + `/index/*`; Query on `opal-harvest-articles` + `/index/*`; PutItem/DeleteItem on `opal-harvest-security-metrics`. **No Scan. No wildcard resource.** | 1 |
| `aws_apigatewayv2_integration.scoped_amgt_api` | AWS_PROXY on api `7k3ed8px20` (`opal-portal-data-proxy-api`) | 1 |
| `aws_apigatewayv2_route.scoped_amgt_api[*]` | the ELEVEN `/api/scoped/amgt/*` route keys, **authorization_type CUSTOM, authorizer `naqxlm`** (the same portal JWT authorizer every `/api/private/*` and `/api/scoped/*` route uses) | 11 |
| `aws_lambda_permission.scoped_amgt_api_apigw` | invoke from `arn:aws:execute-api:us-east-1:313476888478:7k3ed8px20/*/*` | 1 |
| `terraform_data.scoped_amgt_route_count_check` | the 11-route precondition | 1 |

**EXPECTED PLAN, read from terraform's own rule for a config whose every new resource is absent from state
and whose existing resources are untouched: `19 to add, 0 to change, 0 to destroy`.** Any `change` or `destroy`
line, or any add outside this table, means the plan is not the act this half covers and the apply does not run.

**One S3 write outside terraform:** `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`
with `content-sha256` metadata (a NEW key; `modules/yang-lambda` reads it as `source_code_hash`).

## THE PROPERTY THIS ACT WIDENS, AND ITS WRITERS COUNTED

The property is **the route set of the shared portal HTTP API `7k3ed8px20`**, today **25 routes, 0 naming amgt**
(measured at this signing). **Writers of that property in this estate, by census (`comp-find '7k3ed8px20'
infra/aws/terraform --files`): 13 terraform files across 8 roots** -- `bd-pipeline`, `harvest` (the enqueue
route, already applied), `investor-reporting/api`, `partners-api`, `portal-content`, `shared-infra` (the API's
own root + `apigateway-portal`), `ticket-center`, `trade-pipeline` -- each adding routes from its OWN state by
the pure-add pattern the harvest module's own comment names. **None of the 8 is invoked by this act; the only
writer that moves is `harvest`, and its rule is the add-set above.** So the outcome this half names ("the 25
stay, 11 are added, total 36") follows from ONE writer's rule and the other seven are not in the path.

## BLAST RADIUS, PER KEY, AND THE ROLLBACK FOR EACH

- **The 25 existing routes:** untouched by construction (they are in other roots' state; a plan from `harvest`
  cannot see or modify them). Verified after the apply by comparing the route-key list snapshot taken BEFORE
  the apply against the list AFTER: the before-set must be a subset of the after-set, unchanged.
- **The 11 new routes + 1 integration + 1 permission:** reachable only with a portal JWT that passes
  authorizer `naqxlm`, then only for the firm the edge injects. Rollback: `terraform destroy -target` on those
  three resource addresses from the harvest root, or `terraform state rm` + `aws apigatewayv2 delete-route`
  per key; either leaves the 25 exactly as found.
- **The Lambda + role + policy + log group:** private; rollback is the same `destroy -target` set.
- **The artifact object:** rollback is `aws s3 rm` of the one new key.
- **Data plane:** the adapter READS two tables and WRITES only firm-scoped star-marker rows to
  `opal-harvest-security-metrics` on explicit `star`/`unstar` calls; the round-10 exercise makes none.
- **Portal freeze:** untouched. The page that calls these routes exists on no DEV/PROD head
  (`refs/drains/rg-2-portal` only); mounting the API serves data to a page no promoted build reaches.

## WHAT THIS HALF DOES NOT COVER

A change to any existing route; a `NONE` authorization on any new route; a Scan grant; a wildcard resource;
any write to the article store; any promote. If the plan proposes any of these, the act is outside this
signature and `AMGT-ri-4` refuses at AC3.

## CORRECTION, 2026-09-15 ~01:1xZ, by the signer (not a silent rewrite)

`1.0.0_SA_CTO~W`'s co-sign read (22951) measured the route set of `7k3ed8px20` at **85 keys by auto-pagination**
(`--no-paginate` returns 25 Items WITH a NextToken; 25 is one page). The "25 routes" above was that page --
CLAUDE.md 22a's paginated `list-*` trap, committed by this signer. **The mechanism this half names does not
depend on N** (the existing routes are untouched by construction; the 11 are added from harvest's own state;
the before-set must be a subset of the after-set), so the signature stands; **the named outcome reads
"N stay, 11 are added, total N + 11" with N MEASURED at the order's AC4**, never a literal. The order's AC4 and
AC6 expectations, which hardcoded 25 and 36, are amended in the same commit as this note (row `Z-S92`), and
the two API Gateway invocations carry the comp-tool rail's audited `# rail-checked:` marker, because the rail
refused that exact command at this seat and would refuse it in the worker's shell too.
