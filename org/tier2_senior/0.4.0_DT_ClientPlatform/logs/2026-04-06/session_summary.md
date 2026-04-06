# Session Summary -- 0.4.0_DT_ClientPlatform

**Date:** 2026-04-06
**Session:** Full deploy day -- yang, BD, partners-api, portal-auth, CloudFront, portal PROD merges

---

## Deploys

| Tag | Pipeline | What |
|-----|----------|------|
| yang-v2.3.6 | yang-pipeline | Filename regex fixes + CacheControl no-cache (28 Lambdas) |
| bd-v2.21.0 | bd-pipeline | GLDRST.007: publisher + advisor-publisher S3 path migration + dual-write |
| bd-v2.21.1 | bd-pipeline | GLDOPS.003: churn component in AUA decomposition |
| bd-v2.21.2 | bd-pipeline | Publisher GRO total uses actual AUA delta |
| partners-api-v1.13.0 | partners-api | GLDRST.007: opal-partners-data S3 path migration (19 reads) |
| partners-api-v1.13.1 | partners-api | GLDRST.018: serve market_growth + synthetic_correction |
| partners-api-v1.14.0 | partners-api | ANONYM.012: Lambda PII handlers for clients-tab + client-detail |
| shared-advisor-router:8 | CloudFront | GLDRST.008: categorized S3 key rewrite (7/7 patterns verified) |
| portal-auth-v1.6.0 | portal-auth | ANONYM.013: advisorId passthrough (fallback '' not 'null') |

## Portal PROD Merges

| Commit | What |
|--------|------|
| 32d2655 | GLDRST.003 + ANONYM.014 (a428ac5, 0a2c441) |
| 0ca650b | GLDRST.018 (478badb) |
| 397e6fc | ANONYM.014 revert (e24dab6) -- live incident, 5 PII endpoints 404 |
| de62fde | ANONYM.014 re-execute (d552234) -- crossref validated |

## Task Orders Completed

| TO | Project | What |
|----|---------|------|
| ADVI_GLDRST.007 | GLDRST | Publisher Lambda S3 path migration + dual-write (3 Lambdas, 42 key refs) |
| ADVI_GLDRST.008 | GLDRST | CloudFront shared-advisor-router v8 (categorized rewrite) |
| ADVI_ANONYM.013 | ANONYM | portal_authorizer advisorId passthrough |
| AUTH_TFIMPT.003 | AUTH_TFIMPT | Shared role ownership assessment (recommendation: shared-infra) |

## Incident

ANONYM.014 deployed to PROD before .012/.013 were ready. 5 PII endpoints returned 404 (Books tab, client detail, advisor book). Reverted via e24dab6 within minutes. Re-deployed after .012 + .013 confirmed live.

## Pushes for Other Agents

Pushed DS commits: GLDOPS.002/.003 (af47c84e, 8a6fef07, e419d83b, a26ba1f9, 6c2b23e9), churn fix (81ce9182), GRO total fix (2c45ae29), GLDRST.004/.005/.006 (426ac7ab through 1f1cf3c9), ANONYM.012 (4a1e289c), yahoo backfill (376c232b).

## Remaining

| TO | Status | Blocker |
|----|--------|---------|
| ADVI_GLDRST.013 | staged | AE gold rebuild (.009) must populate new S3 keys |

---

## Current State

**Status:** Session complete -- all actionable work done
**Active branch:** CLOUD (pushed)
**Portal:** DEV branch, up to date with origin
