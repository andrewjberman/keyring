# AE 0.7.0_AE_CloudOps~C Session Log — ADVI_DEMOV1.001

**Date:** 2026-05-22
**Agent:** 0.7.0_AE_CloudOps~C
**TO:** ADVI_DEMOV1.001 (issued by 2.0.0_SA_COO~C) — Phase 1 of ADVI_DEMOV1
**Project:** ADVI_DEMOV1 — Advisor Intelligence demo tenant

---

## Objective

Stand up the demo tenant's serving infrastructure: the `opal-data-demo` S3
bucket (Terraform), its CloudFront OAI bucket policy, the `demo` firm entry in
the edge `FIRM_CONFIG` single-source module, the routing CI sentinel, and a
rebuild/redeploy of both Lambda@Edge functions. End state: bucket + routing
live and empty, ready for the Phase-4 transform run.

## Resources Changed

| Resource | Change |
|----------|--------|
| `opal-data-demo` S3 bucket | CREATED — versioning Enabled, AES256 encryption, public-access-block all-true (mirrors opal-data-bd). In `shared-infra/s3.tf`. |
| `opal-data-demo` bucket policy | CREATED — Terraform-managed `aws_s3_bucket_policy` (ruling R3). Two statements: `AllowCloudFrontOACReadPlatinum` (cloudfront.amazonaws.com service principal, GetObject on `platinum/*`, gated by EVTSA9VEHNZVH SourceArn) + `AllowScopedAdvisorOAI` (OAI principal E139998VWH0PD, GetObject on `/*`). |
| `firm-config.mjs` FIRM_CONFIG | MODIFIED — additive `demo -> opal-data-demo` entry (mockadv non-real-firm template). 49financial / inflection / mockadv unchanged. |
| `firm-routing.spec.mjs` | MODIFIED — CI sentinel test for the `demo` route, same commit as the firm-config change (R3). |
| `auth-validator-edge` (Lambda@Edge) | REDEPLOYED — rebuilt; firm-config.mjs is bun-build-inlined into the bundle. |
| `shared-advisor-router` (Lambda@Edge) | REDEPLOYED — rebuilt; firm-config.mjs inlined; firm-routing test gate ran 8/8 pass. |
| `iam.tf` | NO CHANGE — see Module / IAM Decisions below. |

## Module / IAM Decisions (criterion 1 + 3 — AE's call, documented)

- **Module choice (criterion 1):** `opal-data-demo` bucket + OAI policy homed in
  `shared-infra/s3.tf`, following the `opal-data-etfs` / `opal-data-mdpf`
  precedent for standalone data buckets with no dedicated pipeline module. The
  demo is a frozen, refreshable static snapshot — explicitly no pipeline behind
  it (PRD §1 out-of-scope) — so a pipeline module would have nothing else in it.
- **opal-partners-data IAM (criterion 3):** NO iam.tf edit. `comp-iam service
  opal-partners-data` -> role `partners-lambda-role`; its `ReadPartnerBuckets`
  statement (partners-api/iam.tf) already grants `s3:GetObject` + `s3:ListBucket`
  on `arn:aws:s3:::opal-data-*` and `opal-data-*/*` — the wildcard that covers
  every partner bucket (bd/inf/etfs/mdpf), and `opal-data-demo` matches it. The
  role HOLDS the grant; criterion 3's end-state is met by existing infra. An
  explicit per-bucket ARN would be the lone exception to a deliberate module
  pattern. Flagged to + concurred by 2.0.0_SA_COO~C 2026-05-22.
- **Edge execution role:** NO change. Edge S3 reads are OAI-mediated via the
  bucket policy (principal E139998VWH0PD), not the `lambda-edge-execution-role`.
  The TF-managed bucket policy is the mechanism.

## Deployment Sequence

| Step | Action | Result |
|------|--------|--------|
| 0 | Owned-paths gap (`~C` not in `CLOUD_OPS_OR_ETL`) | Routed to COO~C; fixed in `2a949a584` (added `~C` to CLOUD_OPS_OR_ETL + SHARED_CLOUD_OPS) |
| 1 | Commit source | `16fd50aa6` infra(cloudops): s3.tf + firm-config.mjs + firm-routing.spec.mjs |
| 2 | `terraform apply` shared-infra (HALTGT-gated `safe-apply.sh`) | 5 added, 0 changed, 0 destroyed |
| 3 | 0-diff plan shared-infra | No changes. Infrastructure matches the configuration. |
| 4 | `build-nodejs-lambda.sh portal-auth shared-advisor-router` | SHA256 `CPCpW/98VNaSobhqVwfcBWxnZhXmo/htu2j6g0iTVvc=`; firm-routing test gate 8/8 pass |
| 5 | `build-nodejs-lambda.sh portal-auth auth-validator-edge` | SHA256 `XZT4+4dFITCfVIESU3XfyumsFtzEj2VwIAMrfuOSi18=` |
| 6 | Commit source map | `1941ec3e5` ci: upload edge artifacts [skip ci] |
| 7 | portal-auth Stage 1 apply (Lambda republish) | 0 added, 2 changed, 0 destroyed |
| 8 | portal-auth Stage 2 apply (CF distribution association ARN bump) | 0 added, 1 changed, 0 destroyed (CF modify ~1m31s) |
| 9 | 0-diff plan portal-auth | No changes. Infrastructure matches the configuration. |
| 10 | `record-terraform-deploy.sh shared-infra` | `713d99116` ci(shared-infra): record deploy [skip ci] |
| 11 | `record-terraform-deploy.sh portal-auth` | `380fb6ab6` ci: record deploy portal-auth [skip ci] |
| 12 | Tag + push --follow-tags | `shared-infra-v1.16.0` @ 713d99116, `portal-auth-v1.16.0` @ 380fb6ab6 |

**0-diff confirmed:** yes — both `shared-infra` and `portal-auth` replan clean.
**CloudFront propagation:** Stage 2 CF distribution apply complete; Lambda@Edge
global edge replication continues ~5-10 min post-apply (non-blocking).
**IAM changes:** none (see Module / IAM Decisions).

## Deployment Tags

| Pipeline | Tag | Commit |
|----------|-----|--------|
| shared-infra | `shared-infra-v1.16.0` | `713d99116` |
| portal-auth | `portal-auth-v1.16.0` | `380fb6ab6` |

## Verification

**comp-routes trace getPlatinumFirmDashboard (Phase 3):**
```
ROUTE: getPlatinumFirmDashboard
  URL: /api/scoped/advisor-intelligence/platinum/firm/dashboard.json
  CloudFront:
    behavior: /api/scoped/advisor-intelligence/*.json
    origin:   S3-opal-data-bd (s3)
  Auth: edge JWT: YES
  Router: shared-advisor-router
  S3 key: platinum/firm/dashboard.json
```
The trace confirms the static path: CF EVTSA9VEHNZVH -> behavior
`/api/scoped/advisor-intelligence/*.json` -> edge router `shared-advisor-router`.
The origin shows `S3-opal-data-bd` because that is the *declared default*
origin; the `demo`-specific resolution to `opal-data-demo` is the runtime
origin-mutation inside shared-advisor-router (it is FIRM_CONFIG data, not a
route edge — comp-routes shows the static graph). The
shared-advisor-router -> opal-data-demo leg is verified by the two checks below.

**firm-routing.spec.mjs CI sentinel — 8/8 pass** (ran in the shared-advisor-router
build gate, against the exact handler code that was bundled + deployed):
```
✔ X-Firm-Id '49financial' routes to opal-data-bd
✔ X-Firm-Id 'inflection' routes to opal-data-inf
✔ X-Firm-Id 'mockadv' routes to opal-data-bd
✔ X-Firm-Id 'demo' routes to opal-data-demo        <- new (asserts domainName == opal-data-demo.s3.us-east-1.amazonaws.com)
✔ [SENTINEL] X-Firm-Id 'cottonwood' -> unmapped fallback
✔ X-Firm-Id 'opal-capital' ?firm=inf -> opal-data-inf
✔ X-Firm-Id 'opal-capital' missing ?firm= -> 400
✔ Missing X-Firm-Id -> 403
```
49F / Inflection / mockadv routes unchanged — zero regression (criterion 9).

**opal-data-demo deployed state (AWS CLI):**
```
head-bucket: OK (arn:aws:s3:::opal-data-demo, us-east-1)
versioning:  Enabled
bucket policy: 2 statements live -
  AllowCloudFrontOACReadPlatinum (Service cloudfront.amazonaws.com,
    GetObject opal-data-demo/platinum/*, Condition SourceArn EVTSA9VEHNZVH)
  AllowScopedAdvisorOAI (AWS OAI E139998VWH0PD, GetObject opal-data-demo/*)
```
Bucket empty — expected; TO-2/TO-4 (DS~C) populate it.

## Compiler Tools

| Tool | When | Result | Notes |
|------|------|--------|-------|
| `comp-iam service opal-partners-data` | Phase 1 | role `partners-lambda-role`, s3:GetObject + s3:ListBucket GRANTED | `ReadPartnerBuckets` `opal-data-*` wildcard covers opal-data-demo — no iam.tf edit needed |
| `comp-iam service shared-advisor-router` | Phase 1 | no match | Lambda@Edge not in the comp-iam index — anticipated by the TO `<if_mismatch>`; edge reads are OAI/bucket-policy-mediated |
| `comp-iam gaps` | Phase 2 | 2 gaps, both pre-existing | `mdpf-daily-trigger` (s3:GetObject/PutObject) — out of TO-1 scope, predates this work. **Zero new gaps** from ADVI_DEMOV1.001. |
| `comp-routes behaviors` | Phase 2 | 23 behaviors intact | All `/api/scoped/advisor-intelligence/*` behaviors show auth-validator-edge + shared-advisor-router + shared-advisor-router-response unchanged — no drift |
| `comp-routes trace getPlatinumFirmDashboard` | Phase 3 | CF -> shared-advisor-router confirmed | See Verification — full chain to opal-data-demo verified via the CI sentinel + AWS state |

Gap found: none. The TO `<if_mismatch>` for `comp-iam service shared-advisor-router`
(Lambda@Edge not in index) was anticipated — handled per the TO's documented fallback.

## Acceptance Criteria

| # | Criterion | Status |
|---|-----------|--------|
| 1 | opal-data-demo bucket via Terraform, versioning+encryption+PAB | DONE — shared-infra/s3.tf; module choice documented above |
| 2 | OAI bucket policy (E139998VWH0PD + EVTSA9VEHNZVH SourceArn, per-bucket) | DONE — TF-managed `aws_s3_bucket_policy`, verified live |
| 3 | opal-partners-data role holds s3:GetObject + s3:ListBucket on opal-data-demo; comp-iam gaps clean | DONE — via the pre-existing `ReadPartnerBuckets` `opal-data-*` wildcard; comp-iam gaps shows 0 new gaps (COO~C concurred) |
| 4 | additive `demo` FIRM_CONFIG entry; 49F/INF/mockadv unchanged | DONE — firm-config.mjs |
| 5 | firm-routing.spec.mjs covers `demo`, same commit, passes | DONE — `16fd50aa6`; 8/8 |
| 6 | both Lambda@Edge fns rebuilt + redeployed | DONE — auth-validator-edge + shared-advisor-router, two-stage apply |
| 7 | terraform apply 0-diff; record-terraform-deploy.sh; git tag; lambda-source-map.json updated | DONE — both modules 0-diff; tags v1.16.0; source map at `1941ec3e5` |
| 8 | Phase-3 comp-routes trace confirms X-Firm-Id=demo -> opal-data-demo | DONE — see Verification |
| 9 | 49F/INF/mockadv routes still resolve; zero regression | DONE — firm-routing.spec.mjs 8/8; firm-config change purely additive |
| 10 | Session log with Compiler Tools section | DONE — this log |

## Current State

ADVI_DEMOV1.001 COMPLETE. The demo tenant's serving infrastructure is live and
empty:
- `opal-data-demo` S3 bucket created, Terraform-managed, with the CloudFront OAI
  bucket policy. shared-infra-v1.16.0.
- `demo -> opal-data-demo` routing live in the edge `FIRM_CONFIG`; both
  Lambda@Edge functions redeployed; CF distribution EVTSA9VEHNZVH points at the
  new edge versions. portal-auth-v1.16.0.
- A request with X-Firm-Id=demo resolves CF -> shared-advisor-router ->
  opal-data-demo (verified). Bucket empty — by design at this phase.

## Next Steps

1. [2.0.0_SA_COO~C] RAVC2 validation; flip ADVI_DEMOV1.001 `<status>` to complete
   (COO owns the task_orders lane).
2. [DS~C] TO-2 — build the two-pass transform engine.
3. [DS~C] TO-3 — `FIRM#demo` DynamoDB record + demo Cognito user + portal
   `ROUTER_FIRM_SUFFIX` entry. NOTE: shared-advisor-router v9 blocks
   `platinum/{advisors,clients}/{id}/summary.json` from S3-direct (401) — the
   demo needs BOTH the edge entry (this TO, done) AND the `FIRM#demo` record.
4. [DS~C] TO-4 — run the transform, populate opal-data-demo, PII-leak scan.

Pre-existing finding surfaced for COO routing (not TO-1 scope): `comp-iam gaps`
reports 2 permission gaps on `mdpf-daily-trigger` (s3:GetObject/PutObject via
`aws s3 cp`) — predates this work; candidate for a separate mdpf-pipeline TO.

## Closure (addendum 2026-05-22T18:16Z)

RAVC2 ACCEPTED by 2.0.0_SA_COO~C — ADVI_DEMOV1.001 CLOSED, TO `<status>complete</status>`
committed `6dc4d50d1`. COO~C verified all 10 ACs empirically (5 commits confirmed
as origin/CLOUD ancestors; both v1.16.0 tags; opal-data-demo bucket + policy
checked live in AWS). AE lane for ADVI_DEMOV1 is clear — TO-1 was the only AE TO;
TO-3 / TO-4 are DS~C. RAVC loop closed.
