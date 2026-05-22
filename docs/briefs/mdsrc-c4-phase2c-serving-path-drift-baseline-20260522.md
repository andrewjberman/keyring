# YALP_MDSRC.C4 — Phase-2C Serving-Path Drift Baseline

| Field | Value |
|---|---|
| TO | YALP_MDSRC.C4 — dt-phase2c-serving-path-drift-baseline |
| Owner | 0.3.0_DT_TradingOperations |
| Date | 2026-05-22 |
| Type | Read-only baseline (no code / no infrastructure change) |
| Priority | P3 — preparatory; feeds C2 (YCharts market-data pull) and D1 (yang cutover) |
| PRD | docs/architecture/YALP_MDSRC.md v0.3.2 — Phase 2C, TO-C2 |
| Distribution | CloudFront `EVTSA9VEHNZVH` (opalinvest.dev) |
| Routing source of truth | `infra/aws/terraform/portal-auth/cloudfront-distribution.tf` |

## 1. Purpose

The Phase-2C YCharts-pull migration (TO-C2) re-sources the artifacts behind the
portal's market-data / macro serving paths. Before that migration touches
routing, this document captures the documented current state of the
`/api/general/*` and `/json-tiered/*` CloudFront path families so C2/D1 start
from known ground rather than discovering routing drift mid-cutover.

This is an audit only. No routing, CloudFront, or code change is made by C4.

## 2. Method

- `comp-routes behaviors` — captured all 22 ordered CloudFront behaviors + the
  default behavior of distribution `EVTSA9VEHNZVH`.
- Cross-checked the three in-scope behaviors against the authoritative
  Terraform source `infra/aws/terraform/portal-auth/cloudfront-distribution.tf`
  (behaviors #6, #7, #8).
- `comp-routes rewrites` — captured the `public-data-router` URL-rewrite map.
- `aws s3 ls s3://opal-data-portal-v2/json/` and `.../json-tiered/` — grounded
  the surface-to-prefix mapping (read-only listing).
- Cross-referenced PRD §5.2 (the 32-surface matrix) for the C2-migrated surfaces.

The `comp-routes` routing model and the portal-auth Terraform agree exactly
(22 ordered behaviors, identical origins / cache policies / Lambda@Edge
associations). No drift exists between the comp-graph routing model and
Terraform state.

## 3. The three in-scope serving behaviors (current state)

All three target the same origin: `S3-opal-data-portal-v2-json`
(`opal-data-portal-v2.s3.us-east-1.amazonaws.com`, OAC `E24L6358YRRKAE`).

CloudFront `*` does not match `/`, so each path depth needs its own behavior.
Behavior precedence is most-specific-first; the three are evaluated in this
order relative to each other:

### Behavior #6 — `/api/general/json-tiered/*`

| Property | Value |
|---|---|
| Target origin | S3-opal-data-portal-v2-json |
| Allowed methods | GET, HEAD, OPTIONS |
| Cached methods | GET, HEAD |
| Cache policy | `json_tiered_5min` (id `3eda5c45-0def-4131-87bc-19a31223c270`) — 5-minute TTL |
| Origin request policy | Managed-CORS-S3Origin |
| viewer-request | `auth-validator-edge` (Lambda@Edge) |
| origin-request | `public-data-router` (Lambda@Edge — strips `/api/general/` prefix) |
| origin-response | `cache-control-injector` (Lambda@Edge) |
| Compress | true |

### Behavior #7 — `/json-tiered/*`

| Property | Value |
|---|---|
| Target origin | S3-opal-data-portal-v2-json |
| Allowed methods | GET, HEAD, OPTIONS |
| Cached methods | GET, HEAD |
| Cache policy | `json_tiered_5min` (id `3eda5c45-...`) — 5-minute TTL |
| Origin request policy | Managed-CORS-S3Origin |
| viewer-request | NONE |
| origin-request | NONE |
| origin-response | NONE |
| Compress | true |

Direct, unauthenticated, un-rewritten S3 passthrough.

### Behavior #8 — `/api/general/*`

| Property | Value |
|---|---|
| Target origin | S3-opal-data-portal-v2-json |
| Allowed methods | GET, HEAD (no OPTIONS) |
| Cached methods | GET, HEAD |
| Cache policy | Managed-CachingOptimized (default TTL 1 day, max 1 year) |
| Origin request policy | Managed-CORS-S3Origin |
| viewer-request | `auth-validator-edge` (Lambda@Edge) |
| origin-request | `public-data-router` (Lambda@Edge — strips `/api/general/` prefix) |
| origin-response | `cache-control-injector` (Lambda@Edge) |
| Compress | true |

Catch-all for `/api/general/` paths not matched by the more-specific
`/api/general/trades/*` (behavior #1) or `/api/general/json-tiered/*`
(behavior #6).

### URL rewrites (`public-data-router`, from `comp-routes rewrites`)

| Incoming prefix | Rewritten S3 prefix |
|---|---|
| `/api/general/json/` | `json/` |
| `/api/general/json-tiered/` | `json-tiered/` |

`public-data-router` strips the `/api/general/` viewer prefix at origin-request
time. The `S3-opal-data-portal-v2-json` origin keys live under `json/` and
`json-tiered/`. Behavior #7 (`/json-tiered/*`) has no router, so it reads the
`json-tiered/` S3 prefix directly without a rewrite.

## 4. Custom error responses

The distribution has **no `custom_error_response` blocks**. The former
distribution-global `custom_error_response` (403/404 -> 200 `/index.html`) was
removed by TRSB_LEDGER.011 because, being distribution-global, it masked
`/api/*` 4xx JSON as 200 HTML and crashed the portal's `JSON.parse`. SPA
deep-link fallback is now an `aws_cloudfront_function` (`portal-spa-fallback`)
attached to the default (S3) cache behavior only.

Consequence for the in-scope paths: `/api/general/*`, `/api/general/json-tiered/*`,
and `/json-tiered/*` all pass through their real origin status code and body on
4xx — no HTML masking. This is the intended post-TRSB_LEDGER.011 design state,
not drift. It is favorable for C2: a YCharts-pull failure surfacing as a 403/404
will reach the portal as a real status + body, not as masked HTML.

## 5. C2-migrated surfaces -> serving-path mapping (PRD §5.2 cross-ref)

The C2 YCharts pull re-sources the YCharts-replaceable and the YCharts-input
legs of the hybrid surfaces. Their portal artifacts are served from the
`S3-opal-data-portal-v2-json` origin under the `json/` prefix. S3 listing of
`s3://opal-data-portal-v2/json/` confirms these content prefixes exist:

| PRD §5.2 surface | Class | S3 content prefix (under `json/`) | Serving behavior |
|---|---|---|---|
| WS1-MO-01..04 — Market Overview heatmap / RSI / timeseries | YCharts-replaceable | `market-overview/` | #8 `/api/general/*`; also #6/#7 `json-tiered/market-overview/` |
| WS1-VAL-01 — Valuation multiples + ranges | YCharts-replaceable | `valuation/`, `valuations/` | #8 `/api/general/*` |
| WS1-VAL-02 — Valuation risk premium | Hybrid | `valuation/` / `capital-markets/` | #8 `/api/general/*` |
| WS1-COR-01 — Correlation matrices | Hybrid | `correlations/` | #8 `/api/general/*` |
| WS1-MAC-01 — Macroeconomics 12 groups | Hybrid (Bloomberg-leaning) | `macro/`, `capital-markets/` | #8 `/api/general/*` |
| WS2-MP-01/02/04 — Model Portfolios benchmark returns | YCharts-replaceable / Hybrid | `model_portfolios/`, `benchmarks/`, `returns/` | #8 `/api/general/*` |
| WS2-MP-05 — Model Portfolios peer performance | Hybrid | `peers/` | #8 `/api/general/*` |
| WS1-DDB-01 — DynamoDB 71-entity daily price series | YCharts-replaceable | (DynamoDB-backed; not an S3 CloudFront path) | n/a — not on `/api/general/*` or `/json-tiered/*` |

Headline mapping conclusion: every C2-migrated **S3-served** market-data /
macro artifact is served through behavior #8 `/api/general/*` (the catch-all),
with the Market Overview family additionally available under the tiered
behaviors #6/#7. The DynamoDB price-series backbone (WS1-DDB-01) is not served
by either in-scope path family and is out of this baseline's routing surface.

The migration re-sources artifact **content** (producer swap: yang Bloomberg
`data_pkl` -> daily YCharts pull). It does **not**, by itself, require a routing
change — **provided C2 writes to the same S3 keys**. If C2 changes any S3 key
name, behaviors #6/#7/#8 and the `public-data-router` rewrite map must be
updated in lockstep.

## 6. Baseline findings (drift / surprises flagged for Phase-2C)

No live routing defect was found. All findings below are drift / design
observations for C2/D1 to account for, not breakage.

**BF-1 (highest impact) — freshness behavior differs by path family.**
Behavior #8 `/api/general/*` uses Managed-CachingOptimized (default TTL 1 day,
max 1 year). Behaviors #6/#7 (json-tiered) use `json_tiered_5min` (5-minute
TTL). A **daily** YCharts pull served under `/api/general/*` will be
CloudFront-cache-stale for up to the CachingOptimized TTL unless C2 issues an
explicit CloudFront invalidation after each pull, or the origin object sets a
short `Cache-Control` header (note: `cache-control-injector` runs on
origin-response for #6/#8 and can shape this). C2 must decide its freshness
mechanism: (a) post-pull CloudFront invalidation, (b) rely on
`cache-control-injector` headers, or (c) move the C2 artifacts onto a
json-tiered (5-min) path. This is the single most important item for the
migration to plan around.

**BF-2 — `/json-tiered/*` (root) has no Lambda@Edge; `/api/general/json-tiered/*`
has all three.** The root `/json-tiered/*` behavior carries no
`auth-validator-edge`, no `public-data-router`, and no `cache-control-injector`.
The `/api/general/json-tiered/*` behavior carries all three. Two routes reach
the same `opal-data-portal-v2/json-tiered/` S3 prefix with different auth
posture and different rewrite behavior. C2/D1 must be explicit about which of
the two it serves new tiered artifacts through; serving via the root path
bypasses `auth-validator-edge`.

**BF-3 — `/api/general/*` does not allow OPTIONS.** Behavior #8 `allowed_methods`
is `GET, HEAD` only; behaviors #6/#7 allow `GET, HEAD, OPTIONS`. A CORS
preflight against an `/api/general/*` artifact will not be served. If C2's
re-sourced artifacts ever need a browser CORS preflight on that path, behavior
#8 needs `OPTIONS` added. (Current consumers are same-origin portal fetches, so
this is latent, not active.)

**BF-4 — the `json_tiered_5min` cache policy is not Terraform-managed.** It is
referenced by a `data "aws_cloudfront_cache_policy"` source with a hardcoded ID
(`3eda5c45-0def-4131-87bc-19a31223c270`). The 5-minute freshness behavior on the
json-tiered paths depends on a CloudFront cache policy outside Terraform state —
a console edit to that policy would not be caught by `terraform plan` drift
detection. C2/D1 should be aware the json-tiered TTL is an unmanaged dependency.

**BF-5 — no custom error responses (documented, not drift).** See §4. Recorded
here so C2 does not re-discover it: 4xx on the in-scope paths pass through as
real status + body. This is the intended TRSB_LEDGER.011 state.

**BF-6 — S3 content-namespace observations.** Under `s3://opal-data-portal-v2/json/`,
both `valuation/` and `valuations/` prefixes exist (singular + plural split);
`json-tiered/` currently serves only `market-overview/`. These are content-key
observations, not routing-config issues — but C2 should reconcile which
valuation prefix is canonical before it picks its target write keys, to avoid
re-sourcing into a stale prefix.

**BF-7 — `ycharts-pipeline` Terraform has no CloudFront config.** The
`infra/aws/terraform/ycharts-pipeline/` module (lambdas.tf, ecr.tf, secrets.tf,
eventbridge.tf, cloudwatch.tf, iam.tf, main.tf) exists but has no `cloudfront.tf`
and no behaviors. This confirms C2 is scoped as a producer-side build: the
YCharts pull writes artifact content into the existing `opal-data-portal-v2`
S3 keys, and the portal-auth distribution continues to serve them unchanged.
No new CloudFront distribution or behavior is scaffolded for YCharts. The
routing surface stays exactly as captured in §3 unless C2 changes S3 keys
(see §5).

**BF-8 — historical: market-metrics CDN decommissioned.** The standalone
market-metrics CDN (`E2LPCXXBLDGWXY`) was decommissioned 2026-04-15
(CDRS_TFIMPT.004); `market-metrics.json` is now served via the portal
distribution at `/api/general/*` (behavior #8). Recorded so C2 does not look
for a separate market-data distribution — there is exactly one
(`EVTSA9VEHNZVH`).

## 7. Handoff to C2 / D1

- The routing surface C2 re-sources is **behavior #8 `/api/general/*`** for all
  S3-served market-data/macro artifacts, plus **#6/#7** for the Market Overview
  tiered variants. All point at one origin (`opal-data-portal-v2`).
- C2 is a producer swap. **If C2 keeps the existing S3 keys, no routing change
  is needed.** If C2 renames any key, #6/#7/#8 and the `public-data-router`
  rewrite map change in lockstep — re-run `comp-routes behaviors` after.
- C2 must pick a freshness mechanism for the daily pull on the long-TTL
  `/api/general/*` path (BF-1) — this is the action item with the largest
  blast radius.
- No live defect surfaced; nothing requires immediate COO action. This baseline
  is informational input to the C2/D1 routing step.

## 8. Compiler Tools

| Tool | Result | Notes |
|---|---|---|
| `comp-routes behaviors` | 22 ordered behaviors + default captured | Primary evidence. Behaviors #6/#7/#8 are the in-scope families. |
| `comp-routes rewrites` | `public-data-router` map captured | `/api/general/json[-tiered]/` -> `json[-tiered]/` prefix strip. |
| portal-auth `cloudfront-distribution.tf` cross-check | Terraform == comp-routes model | No drift between routing model and Terraform state. |
| `aws s3 ls opal-data-portal-v2/json[-tiered]/` | Content prefixes listed | Grounded the §5 surface-to-prefix mapping; surfaced BF-6. |

No code change made — C4 is a read-only baseline, so Phase-2 (before-commit) and
Phase-3 (after-commit) compiler gates do not apply.
