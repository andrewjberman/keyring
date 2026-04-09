# Session Log: ADVI_ANONYM.016 -- Books Tab / Advisor Intelligence Auth Fix

**Agent:** 0.7.0_AE_CloudOps
**Date:** 2026-04-07
**Duration:** ~90 min
**Project:** ADVI_ANONYM
**Trigger:** Andrew reported Books tab not displaying data after ADVI_ANONYM.016 migration

## Problem

The ADVI_ANONYM.016 migration moved the portal from `/api/shared/` to `/api/scoped/` paths and removed the old `/api/shared/*` CloudFront behavior. Multiple downstream pieces were not updated, causing a total outage of the Advisor Intelligence page on both production (once cache expired) and localhost.

## Root Causes (4 layered issues)

### 1. Missing CloudFront behaviors (depth-awareness)

CloudFront `*` does NOT match `/`. The existing behaviors:
- `/api/scoped/advisor-intelligence/clients/*` -- only depth-2
- `/api/scoped/advisor-intelligence/*.json` -- only depth-1

Every multi-level path fell through to the SPA default origin, returning `index.html` instead of JSON. This affected ALL advisor-intelligence API calls with subdirectories: `artifacts/*/*`, `entities/*/*`, `advisors/*/*`, `clients/*/*`, `timeseries/*`, `snapshots/*`.

**Fix:** Replaced 3 narrow behaviors with 9 depth-aware behaviors covering depths 1-3, split by origin type (S3 for artifacts/entities, API Gateway for everything else). Added `auth-validator-edge` to all API GW behaviors to prevent the 403->index.html masking by CloudFront's custom error response.

### 2. Missing API Gateway routes

Two routes were never added to Terraform when the portal code was migrated:
- `GET /api/scoped/advisor-intelligence/clients/{clientKey}/detail`
- `GET /api/scoped/advisor-intelligence/advisors/{advisorId}/mix-views`

**Fix:** Added both route resources to `partners-api/api-gateway.tf`.

### 3. shared-advisor-router double-prefixing (GLDRST.021 interaction)

GLDRST.021 restructured portal paths to include `artifacts/` and `entities/` prefixes. The router's else clause already prepended `artifacts/`, creating double paths like `/gold/artifacts/artifacts/timeseries_chart.json`.

**Fix:** Added explicit handlers for `artifacts/` and `entities/` prefixes in the router (v10). These pass through to `/gold/` directly. Legacy flat paths still go through the else clause.

### 4. opal-partners-data Lambda path guard

The Lambda's routing guard checked for `/shared/advisor-intelligence` in the request path, but the portal now sends `/scoped/advisor-intelligence`. Every Books tab API call (clients-tab, client-detail, advisor-book, etc.) silently fell through the guard and returned no data.

**Fix:** Updated guard to accept both `/scoped/` and `/shared/` paths.

### 5. Phantom ClientDetailPage export (portal)

`index.ts` barrel exported `ClientDetailPage` from a `ClientDetail.tsx` that was never created. The failed dynamic import blocked the entire AdvisorIntelligence module from loading in Vite dev.

**Fix:** Removed the phantom export and the associated route in `App.tsx`.

## Deployments

| Pipeline | What Changed | Tag |
|---|---|---|
| portal-auth | 9 depth-aware CF behaviors, shared-advisor-router v8->v10 | `portal-auth-v1.11.1`, `v1.11.2`, `v1.11.3` |
| partners-api | 2 new API GW routes, Lambda path guard fix | `partners-api-v1.15.1`, `v1.15.2` |
| portal (DEV) | Remove phantom ClientDetailPage | commit `c965495` |

## Commits

| Hash | Description |
|---|---|
| `6388d732` | CloudFront catch-all + API GW routes (initial fix, insufficient) |
| `ab7d5853` | Depth-aware CloudFront behaviors (full fix) |
| `0b4a2029` | shared-advisor-router v10 + Lambda path guard /scoped/ |
| `c965495` (portal) | Remove phantom ClientDetailPage export + route |

## Key Lesson

CloudFront `*` wildcard does NOT match `/`. This is documented in AWS docs but easy to miss. Any CloudFront behavior for a path with subdirectories needs explicit depth-level behaviors (`foo/*`, `foo/*/*`, etc.). This applies to all future portal path restructuring work.

## Coordination

- Messaged 0.4.0_DT_ClientPlatform at session start and after each fix iteration
- DT correctly identified the depth-awareness issue and multi-level path breakage
