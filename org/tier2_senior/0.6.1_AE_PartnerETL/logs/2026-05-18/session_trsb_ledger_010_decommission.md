# Session Log — TRSB_LEDGER.010 Decommission Legacy Public Trade Surface
**Agent:** 0.6.1_AE_PartnerETL
**Date:** 2026-05-18
**TO:** TRSB_LEDGER.010 (COO~B-issued, GO 2026-05-18 after Andrew supersession confirm)

## Summary

Decommissioned the legacy unauthenticated trade surface: removed the 11
remaining `/api/public/trades/*` routes (a P1 unauthenticated data exposure)
and retired the legacy `opal-trade-form-ui` CloudFront distribution +
S3 origin bucket. Both gates cleared pre-GO (supersession confirm +
destructive-op authorization, Andrew via CTO~B).

## Phase 1 — Recon (read-only, pre-GO, COO~B-authorized)

- routes.tf: 11 `aws_apigatewayv2_route` resources, all `authorization_type=NONE`,
  each targeting a SHARED integration (i_mvrx5ci / i_x3p4wrq / i_ehdnz7g) also
  used by the `/api/general/` twins.
- CF/S3: Terraform-managed in `trade-pipeline/` (`cloudfront-trade-form-ui.tf` +
  `s3.tf`) — clean Terraform teardown path, no manual steps.
- CloudFront E2RNVVND8GSGG3: Deployed/Enabled, domain d1sqgm6c3x3jxy.cloudfront.net,
  no custom-domain alias (no Route53 cleanup in scope).
- S3 `opal-trade-form-ui`: 7 objects / 147KB — legacy web-form static assets
  (HTML/JS/CSS/img), confirmed NOT trade records.
- Teardown gotcha flagged + locked into TO Phase 3: the bucket has versioning
  enabled + no `force_destroy` → a destroy would fail; sequence = add
  force_destroy first, apply, then remove.
- Traffic: CloudWatch Requests metric — 13 requests in 90 days, all on a single
  day (2026-04-27), zero in the last 3 weeks. Effectively dead. (Access logging
  was disabled — no per-request detail.) This empirical backed the supersession.

## Phase 2 — Remove the 11 public routes (shared-infra)

`infra/aws/terraform/shared-infra/apigateway-portal/routes.tf` — removed the 9
GET + 2 POST `/api/public/trades/*` route resources (r_h75lzsh, r_llrm3l0,
r_y8e4cbe, r_6rps3ff, r_gi0ojic, r_lxwgnpc, r_h6cx1c5, r_gna3k55, r_1jq65h8,
r_bs4f5nq, r_8pi62bp). The 010a workflow-removal comment was rewritten into a
full-family tombstone. Shared integrations + the 13 `/api/general/trades/*`
routes left intact (verified — integrations defined in integrations.tf, untouched).

- Commit 677614841.
- `terraform plan`: 0 add, 0 change, **11 destroy** — exactly the 11 public
  routes, no integration, no general route (TO Phase-2 mandate `<expect>` met).
- `terraform apply`: 11 destroyed. `terraform plan` re-run: No changes (0-diff).
- P1 exposure CLOSED.

## Phase 3a — force_destroy on the bucket (trade-pipeline)

`trade-pipeline/s3.tf` — added `force_destroy = true` to
`aws_s3_bucket.trade_form_ui` (versioned bucket; required before the destroy).
- Commit 784e42ddc. `terraform plan`: 1 in-place change (force_destroy
  false→true). `terraform apply`: 1 changed. 0-diff verified.
- Note: `terraform fmt` initially reformatted an unrelated `lambdas.tf`
  (whitespace-only, was non-canonical at HEAD) — reverted via `git checkout`;
  switched to targeted `terraform fmt s3.tf`. lambdas.tf untouched in the commit.

## Phase 3b — Teardown opal-trade-form-ui CloudFront + S3 (trade-pipeline)

Deleted `cloudfront-trade-form-ui.tf` (3 resources: OAC, distribution
E2RNVVND8GSGG3, bucket_policy) and removed the `trade_form_ui` block from
`s3.tf` (5 resources: bucket + versioning + SSE + PAB + website_configuration);
s3.tf header comment updated (5→4 buckets). The other 5 trade-pipeline buckets
untouched.
- Commit 33d543813 (cloudfront-trade-form-ui.tf deleted + s3.tf trade_form_ui
  block removed; s3.tf header updated 5->4 buckets).
- `terraform plan`: 0 add, 0 change, **8 destroy** (3 CF + 5 S3) — isolated.
- `terraform apply`: 8 destroyed, exit 0. CloudFront E2RNVVND8GSGG3 disabled +
  propagated + deleted in 3m19s; the versioned bucket was force-purged + deleted.
  `terraform plan` re-run: No changes (0-diff).

## Phase 4 — Tags, deploy record, push

- Tags: `shared-infra-v1.15.0` (on 677614841), `trade-pipeline-v1.17.0` (on
  33d543813) — annotated.
- shared-infra deploy recorded via `record-terraform-deploy.sh shared-infra`
  (auto-delegated to the conservative resource-map recorder) — commit 02be968ee,
  CHANGELOG entry shared-infra-v1.15.0.
- trade-pipeline CHANGELOG entry added manually — commit 7420e4c3a,
  `functions_updated: []`. `record-terraform-deploy.sh trade-pipeline` was
  deliberately NOT run: trade-pipeline has no resource-map, so the script would
  blunt-set last_deployed_commit=HEAD for all 23 trade-pipeline Lambda
  source-map entries and mask any genuinely-pending Lambda drift (e.g. an
  in-flight 0.7.0 handler-lane deploy). TO-10 deployed no Lambda.
- `git push --follow-tags` — landed the TRSB_LEDGER.010 commits + both tags +
  the pre-existing unpushed CLOUD backlog (CTO~B PRD + COO~B decomposition
  commits), clearing the push debt.

## Smoke

Route removal (verified post-Phase-2, API endpoint 7k3ed8px20):
- GET /api/public/trades/submissions -> HTTP 401
- GET /api/public/trades/users -> HTTP 401
- POST /api/public/trades/submit -> HTTP 401
  (all via the authorizer-protected $default fall-through — the TO-accepted
  end state, per the 010a precedent)
- GET /api/general/trades/submissions -> HTTP 401 (authorizer rejects the
  no-token request — the authenticated route is intact + routed, not 404)

Legacy form + portal (post-teardown):
- `aws cloudfront get-distribution --id E2RNVVND8GSGG3` -> NoSuchDistribution.
- `aws s3 ls s3://opal-trade-form-ui/` -> NoSuchBucket.
- Legacy form URL `https://d1sqgm6c3x3jxy.cloudfront.net/` -> HTTP 000 (dead).
- Authenticated portal API `GET /api/general/trades/submissions` -> HTTP 401
  (routed + authorizer-protected; intact — not 404).

## Compiler Tools

| Tool | Phase | Result |
|------|-------|--------|
| Direct read: routes.tf + cloudfront-trade-form-ui.tf + s3.tf | 1 (recon) | All 11 public routes enumerated; CF/S3 confirmed Terraform-managed. comp-routes N/A — the portal API Gateway is uninstrumented (PRD §5). |
| aws cloudfront get-distribution / cloudwatch get-metric-statistics | 1 | Distribution state + 90-day traffic (13 reqs, all one day, none in 3 weeks). |
| terraform plan (shared-infra, trade-pipeline x2) | 2/3 (before each apply) | Each plan isolated to the intended change — 11 route destroys; force_destroy 1-change; 8 CF/S3 destroys. No shared integration, no /api/general/ route, no unrelated resource. |
| comp-iam | after commit | N/A — no new boto3/aws-cli op; route + CF + S3 resource removals only, no iam.tf change. |
| terraform plan 0-diff (post-apply, both modules) | 3 | No changes — deployed state matches config. |

## RAVC2

RAVC2-close sent to 2.0.0_SA_COO~B; CC 1.0.0_SA_CTO~B — recon census, the three
commit SHAs, both tags, the 8-resource teardown, AC5 smoke evidence, and the
destructive-teardown step log.

## Status

TRSB_LEDGER.010 COMPLETE — all ACs met:
- AC1: Phase-1 gate honored — work began only after COO~B relayed Andrew's
  supersession confirm.
- AC2: 11 `/api/public/trades/*` routes removed; the 4 shared integrations +
  13 `/api/general/trades/*` routes intact.
- AC3: CloudFront E2RNVVND8GSGG3 disabled + deleted, S3 opal-trade-form-ui
  emptied + deleted (NoSuchDistribution / NoSuchBucket). No other distribution
  or bucket affected — the 5 sibling trade-pipeline buckets untouched. No S3
  object deletion outside the force_destroy of the legacy bucket.
- AC4: every terraform plan isolated to intended destructions; applies
  succeeded; 0-diff re-plan on both modules; tags applied.
- AC5: removed public routes -> 401; legacy form URL dead; authenticated portal
  TradeSubmission API path unaffected.
- AC6: no emoji; deployed per the EC2/Terraform standard; this session log.

Ships: commits 677614841 (routes) / 784e42ddc (force_destroy) / 33d543813
(teardown); deploy records 02be968ee / 7420e4c3a; tags shared-infra-v1.15.0 +
trade-pipeline-v1.17.0. The legacy unauthenticated trade surface (TRSB_LEDGER
PRD §9) is decommissioned end to end — both the route family and the standalone
form distribution.
