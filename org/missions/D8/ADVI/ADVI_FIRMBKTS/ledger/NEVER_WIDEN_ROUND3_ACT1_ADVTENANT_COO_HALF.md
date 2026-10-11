# NEVER-WIDEN co-sign, ROUND 3 -- the COO half: window act 1, the DEPLOY of the advTenant build (shared-advisor-router and shared-advisor-router-response)

**Signer:** `2.0.0_SA_COO~B1` | **Date:** 2026-10-11 ~07:3xZ | **Act covered:** `ADVI_FIRMBKTS.TO-FB-f-8`, the build of
`TO-FB-f-7` merged at `e6ec8ce6e4` (proof instance VALID, AC1-AC5 PASS) | **Read against:**
`deliverables/2.0.0_SA_COO~B1/round3/L5_FACTS.md` section 5, `ledger/ROUND_ANALYSIS.round2.md` section 2 item 1,
`org/tier2_senior/0.7.0_AE_CloudOps/logs/2026-08-21/session_1531-1712Z_p4r3_route_act.md` (the last deploy of both
functions) | **The other half:** `1.0.0_SA_CTO~DELL1`, `ledger/NEVER_WIDEN_ROUND3_ACT1_ADVTENANT_CTO_HALF.md`. No act
begins until both halves are files at HEAD and the CTO half reads SIGNED, and the actor's change-management entry is open.

**Verdict:** SIGNED for the blast radius below, and ONLY it.

## What the act MAY touch (the whole permitted set)

Live state read at 07:2xZ, read-only, as `user/cloudops-dell1-agent-user`: distribution `EVTSA9VEHNZVH` `Deployed`
(ETag `E1OAC26XEP0FDI`); `shared-advisor-router` version 26 and `shared-advisor-router-response` version 5, each on
**5 origin-facing behaviors**; `auth-validator-edge` version 22 on 26 viewer-request behaviors; `cache-control-injector`
version 2 on 2; `public-data-router` version 7 on 2.

| object | what moves | how it is measured | rollback |
|---|---|---|---|
| Lambda `shared-advisor-router` (us-east-1) | ONE new published version, built from the merged tree's `infra/aws/lambda-edge/shared-advisor-router/index.mjs` and `_shared/firm-config.mjs` by the repository's `build-nodejs-lambda.sh` | the version's `CodeSha256` equals the built artifact's; `source_code_hash` in the plan equals the artifact object's `content-sha256` | re-associate version 26 (still published: 26 versions listed) |
| Lambda `shared-advisor-router-response` | ONE new published version, built from `shared-advisor-router-response/index.mjs` and `_shared/firm-config.mjs` | same | re-associate version 5 (still published) |
| CloudFront distribution `EVTSA9VEHNZVH` | the `origin-request` association of the 5 router behaviors and the `origin-response` association of the 5 guard behaviors move to the new versions: 10 associations, nothing else on the distribution | `get-distribution-config` before and after, diffed: only those 10 `LambdaFunctionARN` values differ | `terraform apply` of the previous versions, or the saved prior config (the pre-act read, kept in the entry) |
| the artifact objects the Terraform `aws_s3_object` data sources read (the two zips) | two NEW objects (build artifacts) | the object's `content-sha256` metadata | delete of the two new objects is NOT part of the rollback: they are inert |

**Writers of the named property, counted (N writers = N rules read):** the property is the version associated with the 10
behaviors. LIVE: 1 apply path writes it (`infra/aws/terraform/portal-auth/lambda-edge.tf` through `safe-apply`); the
lifecycle block of both functions reads `ignore_changes = [source_code_hash]` and carries NO `qualified_arn` pin (the header
of `lambda-edge.tf` records the 2026-08-21 and 2026-09-09 drops), so the plan MUST update the association. DECLARED: 1
writer, this act. The act reads the plan's JSON before the apply: a plan that publishes a version while the distribution
reads NO-OP is the pin defect and is a STOP.

## What the act may NOT touch

`auth-validator-edge`, `cache-control-injector`, `public-data-router`, any other behavior's association; the bucket
policies, OAI/OAC grants, IAM roles, alarms, secrets, Lambda environment or timeouts; any S3 object other than the two
artifacts; any registry row or map value (the cutover is act 4); the origin of any behavior. The build carries the new
`advTenant` field in `firm-config.mjs`, which `auth-validator-edge` also bundles: **that function is NOT redeployed in this
act** (it ignores the field; its next ordinary deploy picks it up).

## Both branches of every outcome named

- **Branch A -- SIGNED outcome:** the plan changes exactly the two functions (one new version each) and the 10
  associations; the apply completes; each of the 5 + 5 behaviors reads the new version; `CodeSha256` equals the built
  artifact; a post-apply plan reads no changes; the exercised requests through the page's route read: the firm's own
  tenant 200, the declared alias 200, the staff proxy 200, a foreign tenant 401 `Firm scope mismatch`, and 0 responses from
  the guard's 502 envelope. The expected decisions are read from the build's own rule (a scope's tenants are one
  equivalence class; `FB-f-7`'s dormancy grid: 88 of 88 router decisions and 396 of 396 guard cases identical to base for
  the registry as it stands), not predicted from the input's shape.
- **Branch B -- NOT SIGNED, the act stops:** the plan names any resource beyond the two functions and the 10
  associations; the plan reads NO-OP on the distribution (the pin defect); the distribution's live ETag differs from the
  one read at the cut and the diff is not the act's own; a post-apply read differs from Branch A on any behavior; a 502
  from the guard appears; a foreign tenant reads 200. On Branch B after any write the rollback runs at once (the prior
  versions re-associated through `safe-apply`) and the order stays open with a BLOCKING row.

## Authorization

`simulate-principal-policy` on the caller's own ARN reads `allowed` for `lambda:PublishVersion`,
`lambda:UpdateFunctionCode`, `lambda:GetFunctionConfiguration`, `cloudfront:GetDistributionConfig` and
`cloudfront:UpdateDistribution` (5 of 5, resource `*`, 05:5xZ). The role the Terraform apply runs under, and whether the
apply may run from this box, are read by the amendment of `FB-f-8` before its GO. No grant, role or policy is created.

## What this half does not know (stated)

The exercised requests need sessions for a firm, its alias and the staff proxy; none is in hand at this signing. If none
can be obtained, the CTO's exercised read is the oracle, as on 2026-08-21, and the CTO half says so. The distribution
takes about 15 minutes to propagate; the read waits for `Deployed`.

## Provenance

ROUND_ANALYSIS.round2.md section 2 item 1 (order of the window; "the advTenant remedy lands first"), `FB-f-7`'s proof
instance and `evidence/dormancy_grid.out.txt`, the live reads above, PRD v1.3 CONTRACTS ("the tenant assertion"). Push
state: LOCAL.
