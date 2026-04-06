# Yang Deploy + Bulk Commit -- 0.4.0_DT_ClientPlatform

**Date:** 2026-04-06
**Session:** Commit all pending work, deploy yang-pipeline

---

## Task

Andrew directed: "make sure everything is committed and deployed." CTO had also
asked whether the yang filename regex fixes were committed (they were not).

## Commits (this session)

| Commit | Author | Description |
|--------|--------|-------------|
| `629a2fef` | 0.4.0_DT_ClientPlatform | fix(yang): filename regex updates + S3 cache-control no-cache |
| `6ae897f9` | 0.4.0_DT_ClientPlatform | update(bd): gold layer runner scripts and EC2 deploy/setup improvements |
| `e55a0b79` | 0.4.0_DT_ClientPlatform | org: accumulated cross-pod updates (82 files) |
| `95d72468` | 0.4.0_DT_ClientPlatform | ci: upload artifacts for yang-pipeline |
| `31221c84` | record-terraform-deploy.sh | ci: record deploy yang-pipeline @ 95d72468 [skip ci] |

Note: `af47c84e` (fix ADVI_GLDOPS.002 pending marker check) landed between e55a0b79 and 95d72468 from another session -- not authored by this DT session.

## Yang Deploy

- Built and uploaded all 28 Lambda functions to S3
- `terraform apply` -- 0 added, 28 changed, 0 destroyed
- 0-diff verified
- CHANGELOG.json updated
- Tagged: `yang-v2.3.6` on commit 629a2fef
- Pushed CLOUD + tag to origin

### What Changed in yang-v2.3.6

**Filename regex fixes (trigger + peer-performance):**
- `attribution_excel` pattern: `Models Relative Performance` -> `Model Portfolio Attribution`
- `peer_excel` regex: `(\d{6})` -> `(\d{6,8})`
- `extract_date` dispatches on string length (8=YYYYMMDD, 6=YYYYMM, 4=YYYY)
- `yang-generate-peer-performance` extract_date: handles 8-digit YYYYMMDD filenames

**CacheControl changes (4 Lambdas):**
- macro-timeseries, generate-volatility, generate-allocation-summary, generate-positioning
- `public, max-age=3600, s-maxage=7200` -> `no-cache`

## Org Commit (e55a0b79)

82 files covering sessions 2026-03-31 through 2026-04-05:
- All tier2_senior prompt.md updates (12 agents)
- CTO prompt.md update
- New project JSONs: ADHC_TMSTEL, ADVI_GLDOPS
- Updated project JSONs: ADHC_HISTRY, ADVI_ANONYM, ADVI_GLDRST
- REGISTRY.md update
- Session logs for CTO, COO, DE, DS, DT, AE (CloudOps + PartnerETL), RD
- New task orders across DS, DT, DE, AE agents
- Architecture docs (6 new)
- EC2 watchdog/telemetry units
- BD diagnostic scripts
- CLAUDE.md, START_HERE.md, XXX.md, inbox-watch.sh updates

---

## Current State

**Status:** COMPLETE
**Active branch:** CLOUD (pushed)

## Full Session Deploy Log

| Tag | Pipeline | What |
|-----|----------|------|
| yang-v2.3.6 | yang-pipeline | Filename regex fixes + CacheControl no-cache |
| bd-v2.21.0 | bd-pipeline | GLDRST.007: publisher + advisor-publisher S3 path migration + dual-write |
| bd-v2.21.1 | bd-pipeline | GLDOPS.003: churn component in AUA decomposition |
| bd-v2.21.2 | bd-pipeline | Publisher GRO total uses actual AUA delta |
| partners-api-v1.13.0 | partners-api | GLDRST.007: opal-partners-data S3 path migration (19 reads) |
| partners-api-v1.13.1 | partners-api | GLDRST.018: serve market_growth + synthetic_correction |

## GLDRST.008: CloudFront Router v8

- shared-advisor-router Lambda@Edge published as version 8
- CloudFront distribution EVTSA9VEHNZVH updated, status: Deployed
- All 7 routing patterns verified via Lambda invoke:
  - artifacts (flat JSON) -- PASS
  - entities/advisors (per-advisor) -- PASS
  - entities/clients (client_timeseries rename) -- PASS
  - views/ passthrough -- PASS
  - timeseries/ passthrough -- PASS
  - summary/ -> artifacts -- PASS
  - snapshots/ -> artifacts -- PASS

## Portal Merges

- GLDRST.003 + ANONYM.014: DEV pushed + PROD merged (32d2655)
- GLDRST.018: DEV pushed + PROD merged (0ca650b)

## Task Order Status

| TO | Status |
|----|--------|
| ADVI_GLDRST.007 | COMPLETE |
| ADVI_GLDRST.008 | COMPLETE |
| ADVI_GLDRST.013 | staged (terminal gate) |
