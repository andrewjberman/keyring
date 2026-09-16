# NEVER-WIDEN CO-SIGN -- CTO HALF -- AMGT_RESAPP round 10, cell `AMGT-ri-4`: THE MOUNT, DEPLOYED

**Signer:** `1.0.0_SA_CTO~W` (the project's CTO limb on Andrew's word of 2026-09-14 ~23:2xZ).
**Date:** 2026-09-15 ~01:1xZ. **Verdict:** SIGNED.
**Counterpart half:** `ledger/NEVER_WIDEN_ROUND10_MOUNT_COO_HALF.md` (`2.0.0_SA_COO~W`, in the tree at this
signing, 72 lines). **This half is the CTO's OWN read of the act's blast radius**, re-derived from the producer's
rule and the live plane at this seat, not a restatement of the COO's. Where the two halves disagree on a NUMBER
the disagreement is named below; on the ACT they agree.

## RULING: NEVER-1 BINDS THIS ACT

CLAUDE.md NEVER-1: *"NEVER move served output without never-widen sign-off (CTO+COO)."* The act adds eleven
routes to the shared portal HTTP API `7k3ed8px20` (`opal-portal-data-proxy-api`), which serves every portal
page's data calls. Widening a served API's route set is moving served output. The round-8 reading (decomp s.16a,
row `Z-W11-S2` carried two rounds for want of this signature) stands and is not overturned here: the sign-off is
one file each and costs less than the argument. Both halves present = AC1 met.

## THE ACT, READ FROM THE PRODUCER'S OWN RULE (the harvest root's terraform against `harvest/tfstate`)

**Vintages:** `infra/aws/terraform/harvest/scoped-amgt-api.tf` at HEAD `b4439b997d` (272 lines; last commit
`271e8f8b43`, `AMGT-rf-2`, 2026-09-12, never applied). `harvest/tfstate` read from the backend object at
~01:0xZ: serial 25, terraform 1.15.8, **16 resources, 0 of them scoped/amgt** (list: enqueue integration +
route + role + policy + attachment + permission, the two harvest tables, the bucket and its three
configuration resources, the SQS queue, and `module.harvest_enqueue`'s function + log group + artifact data
source). So every managed resource in `scoped-amgt-api.tf` is absent from state and the plan's add-set is
exactly that file's declarations, counted by this seat from the file:

| declared in `scoped-amgt-api.tf` | live name / shape | managed adds |
|---|---|---|
| `module.scoped_amgt_api` (source `../modules/yang-lambda`, the same module `harvest_enqueue` uses; state shows that module = 1 function + 1 log group + 1 `data.aws_s3_object`) | `opal-amgt-scoped-api`, python3.11, 512 MB, 29 s, env `HARVEST_METRICS_TABLE` / `HARVEST_ARTICLES_TABLE` from the table resources | 2 (+1 data source, not an add) |
| `aws_iam_role.scoped_amgt_api` | `opal-amgt-scoped-api-role` | 1 |
| `aws_iam_role_policy_attachment.scoped_amgt_api_logs` | AWSLambdaBasicExecutionRole | 1 |
| `aws_iam_role_policy.scoped_amgt_api_grants` | reads on the two harvest tables + indexes; star-marker writes on the metrics table (per the COO half's read of :89-153; this seat did not re-read every grant line and covers the policy AS DECLARED AT `b4439b997d`) | 1 |
| `aws_apigatewayv2_integration.scoped_amgt_api` | AWS_PROXY on `local.portal_api_id` = `"7k3ed8px20"` (`harvest/main.tf:100`, a literal) | 1 |
| `aws_apigatewayv2_route.scoped_amgt_api[*]`, `for_each` over `local.scoped_amgt_routes` | **11 keys, listed below**; `authorization_type = "CUSTOM"`, `authorizer_id = local.portal_authorizer_id` = `"naqxlm"` (`main.tf:102`, a literal) | 11 |
| `aws_lambda_permission.scoped_amgt_api_apigw` | invoke from `arn:aws:execute-api:us-east-1:313476888478:7k3ed8px20/*/*` | 1 |
| `terraform_data.scoped_amgt_route_count_check` | precondition `length(local.scoped_amgt_routes) == 11` | 1 |
| **total** | | **19 to add, 0 to change, 0 to destroy** |

The eleven route keys, copied from the file's `scoped_amgt_routes` list (each written out in full, by that
file's own rule): `GET /api/scoped/amgt/lead-panel/rankings/{movement}/{subject}` ·
`GET /api/scoped/amgt/lead-panel/timeseries/{movement}/{subject}` · `GET /api/scoped/amgt/watchlist` ·
`POST /api/scoped/amgt/watchlist/star` · `POST /api/scoped/amgt/watchlist/unstar` ·
`GET /api/scoped/amgt/security/{security_key}/overlay` · `.../thesis` · `.../peers` · `.../coverage` ·
`.../print` · `POST /api/scoped/amgt/refresh`. **Collision test at this seat: 0 of the 11 are in the live
route set** (set intersection against the 85 live keys read at ~01:0xZ), so all eleven are pure creates and
none is a change to an existing route.

**One write outside terraform:** `s3://opal-313476888478-lambda-artifacts/research/opal-amgt-scoped-api.zip`.
Measured at ~01:0xZ: `head-object` -> **404, the key does not exist** (positive control: the sibling
`research/opal-research-pull-enqueue.zip` lists, 1,964 B, 2026-09-11). So the upload CREATES a key; the bucket
has **versioning Enabled**, so the rollback is a delete marker on that one key, and no prior version is
displaced because there is none.

**Authorizer `naqxlm` measured live:** `portal-jwt-authorizer`, type REQUEST, the ONLY authorizer on the API;
84 of the 85 live routes with an authorizer use it (the exceptions are `$default` on it too, and the three
`NONE` routes: `ANY /auth/{proxy+}`, `OPTIONS /auth/{proxy+}`, `OPTIONS /{proxy+}`). The eleven new routes
join the CUSTOM/`naqxlm` class, never the NONE class.

## THE TWO PROPERTIES THIS ACT WIDENS, AND THEIR WRITERS COUNTED

**Property 1: the route set of `7k3ed8px20`.** Live at ~01:0xZ, **85 routes, 0 naming amgt** -- read with
`get-routes` AUTO-PAGINATED and counted client-side. ⛔ **THE COO HALF SAYS 25, AND 25 IS A PAGE:**
`get-routes --no-paginate` returns 25 Items with a `NextToken`; `--max-results 25` returns the same page; the
auto-paginated read returns 85 with no token. CLAUDE.md 22a names this trap. The MECHANISM in the COO half is
unaffected (every existing route is in another root's state and a plan from `harvest` cannot touch it); its
NAMED OUTCOME "the 25 stay, 11 are added, total 36" is wrong in its counts and reads correctly as **"the N
present at the before-snapshot stay, 11 are added, total N+11", with N = 85 at this seat's read and N measured
by the worker at AC4 with the same auto-paginated instrument.** ⚠ **AND THE ORDER `TO-AMGT-ri-4` HARDCODES THE
PAGE COUNT:** AC4 expects `routes-before 25` and AC6 expects `before 25, after 36`, while their own invocations
(`get-routes --query "Items[].RouteKey" --output text`) auto-paginate and will read 85 and 96. **On a correct
apply those two criteria grade NOT MET.** That is the issuer's to amend before the worker reaches AC4 (the
expectation is `before N` as measured, `after N+11`, `amgt-after 11`, `before-subset-of-after True`, `lost []`);
this half covers the act either way, and names the defect so the miss is not graded as the world's.
**Writers of property 1, counted by this seat by RESOURCE TYPE rather than by the literal id:** files declaring
`resource "aws_apigatewayv2_route"` estate-wide = **9**; of those, **8 files across 7 roots target
`7k3ed8px20`** -- `shared-infra/apigateway-portal/routes.tf` (the API's own root), `harvest/api-gateway.tf`
(the enqueue route, applied), `harvest/scoped-amgt-api.tf` (THIS act), `investor-reporting/api/routes.tf`,
`ticket-center/main.tf`, `portal-content/main.tf`, `partners-api/api-gateway.tf`, `bd-pipeline/api-gateway.tf`;
the ninth, `inf-pipeline/api-gateway.tf`, targets a different API (`inf_otp_relay`). Every one of the 8
resolves the id by a literal in its own root (`local.portal_api_id` / `local.partners_api_id` = `"7k3ed8px20"`,
or the API resource itself), so no writer hides behind a variable the literal census would miss. (The COO
half's "13 files across 8 roots" is a census of the LITERAL id, which also counts readers -- CloudFront in
`portal-auth`, a README, a CHANGELOG, an outputs file -- and `trade-pipeline`, which names the id on an
integration and declares no route.) **Only `harvest` moves in this act; the other 6 roots' states are not read,
planned or applied.** So the outcome for property 1 follows from ONE writer's rule, and that rule is the
add-set above.

**Property 2: the harvest root's OWN state (serial 25), which the same plan also grades.** Its writers are the
files of `infra/aws/terraform/harvest/` and nothing else. ⛔ **ONE OF THEM IS THE UNCOMMITTED GUARD EDIT:**
`s3.tf` at HEAD reads `bucket = "opal-data-research"`, a bucket that no longer exists (deleted at the 09-11
migration's close-out; the live bucket is `opal-data-harvest`, in state), and `bucket` is ForceNew. **A plan
run against HEAD's bytes of `s3.tf` proposes 1 to destroy + 1 to add on the bucket and is OUTSIDE this
signature** -- AC3's `0 to destroy` refuses it, correctly. **This half covers the plan ONLY when the planning
worktree's `s3.tf` reads `opal-data-harvest`**, which cell `AMGT-ri-2` (queued before `ri-4` in the same
worker, per the issuer) puts there under its own guard, and which the shared tree already carries unstaged
(row `Z-S89`, ledger addendum `@160ca062c5`). Stated here so the precondition is a written line and not an
assumption riding on cell order.

## BLAST RADIUS, PER KEY, AND THE ROLLBACK FOR EACH -- BOTH BRANCHES COVERED

| key | may be touched? | rollback |
|---|---|---|
| the 85 existing routes of `7k3ed8px20` | NO -- other roots' state; verified by AC4/AC6 before-subset-of-after with `lost []` | none needed; if `lost` is non-empty the act is outside this signature and the worker STOPS |
| the 11 new routes, 1 integration, 1 permission | CREATED; reachable only past authorizer `naqxlm` with a portal JWT, then firm-scoped by the edge's claims | `terraform destroy -target` on the three addresses from the harvest root (or `state rm` + `delete-route` per key); the 85 unaffected |
| function, role, attachment, policy, log group | CREATED, private | same `destroy -target` set |
| artifact key `research/opal-amgt-scoped-api.zip` | CREATED (404 today) | `s3 rm` = a delete marker (versioned bucket); nothing displaced |
| `harvest/tfstate` | serial 25 -> 26 with 19 additions | `destroy -target` of the 19 returns it to the 16-resource shape |
| the two harvest DynamoDB tables | READ by the adapter; star-marker WRITES only on explicit `star`/`unstar` calls, which round 10's exercise does not make | not touched by the apply; the policy grants are revocable with the role |
| `opal-data-harvest` bucket | NOT in the add-set; `0 to destroy` is the guard | if the plan names it, STOP (property 2 above) |
| the portal (DEV/PROD/gitlink `e85f6eb84f`) | NOT touched; the page that calls these routes exists on `refs/drains/rg-2-portal` only | freeze stands: COMMIT YES / PROMOTE NO |

**If the apply fails midway** (a partial add), the rollback is the same `destroy -target` over whatever
addresses landed, read from the post-apply state; the 85 cannot have moved in either branch.

## WHAT THIS HALF DOES NOT COVER

Any `change` or `destroy` line in the plan; any add outside the 19 addresses above; a `NONE` authorization on
any new route; any grant beyond the policy as declared at `b4439b997d`; any write to the article store; any
touch to the 85; a plan from a worktree whose `s3.tf` reads `opal-data-research`; any promote, push or gitlink
move. Any of these means the plan is not the act this half covers and `AMGT-ri-4` refuses at AC3.

## INSTRUMENTS, WITH THEIR VINTAGE

`get-api` / `get-routes` (auto-paginated; `--no-paginate` and `--max-results 25` as the page-size tests) /
`get-authorizers` on `7k3ed8px20` at ~01:0xZ · `lambda get-function-configuration` on `opal-amgt-scoped-api`
(ResourceNotFound) with `amgt-resapp-chatter-axis` as the positive control · `s3 cp` of `harvest/tfstate` parsed
in python (serial, resource list) · `head-object` on the artifact key with a sibling key as control ·
`get-bucket-versioning` · the tf file read at HEAD `b4439b997d`, the eleven keys extracted from its own list and
intersected with the live 85 · Grep for `resource "aws_apigatewayv2_route"` and for `^\s*api_id\s*=` across
`infra/aws/terraform` (denominators printed above). Nothing was planned, applied, uploaded or invoked by this
seat. Push state: LOCAL.

-- `1.0.0_SA_CTO~W`
