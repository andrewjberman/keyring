# ADVI_APISCP.002: Post-Deploy Verification — 0.4.0_DE_ClientPlatform

**Date:** 2026-03-10
**Portal DEV commits:** none (verification only)
**Workspace CLOUD commit:** pending (DT)

## Objective

Complete the post-deploy verification for ADVI_APISCP. Phase 3 complete: AE CloudOps
migrated `opal-data-bd` from OAC to OAI (OAI ID: `E139998VWH0PD`), DT rewired the
CloudFront behavior and published `shared-advisor-router-v5` (git tag → `4eff8dee`).
Verify all scoped endpoints return correct JSON from `opal-data-bd/gold/`.

---

## Work Completed

### 1. Phase 1 Verification (v4, OAC) — FAILED, escalated to DT

See prior session log `advi_apiscp_002_post_deploy_verification.md` (first attempt).
Root cause: Lambda@Edge origin mutation broke OAC signing → S3 returned 403 →
CloudFront `403→200 /index.html` custom error rule masked it as portal HTML.

### 2. Phase 3 Verification (v5, OAI) — PASS

Generated a fresh RS256 test JWT (`firmId: bd`, `tier: advisor`, `iss: opal-portal-auth`).
Hit all five required endpoints via CloudFront with `Authorization: Bearer {JWT}`.

| Endpoint | HTTP | Content-Type | data_as_of |
|----------|------|-------------|------------|
| `timeseries_chart.json` | **200** | **application/json** | **2026-03-09** |
| `clients_tab.json` | **200** | **application/json** | confirmed JSON |
| `architect_leaderboard.json` | **200** | **application/json** | confirmed JSON |
| `partner_analytics/header_metrics_quarterly.json` | **200** | **application/json** | confirmed JSON |
| `snapshots/aua_by_architect.json` | **200** | **application/json** | confirmed JSON |

**timeseries_chart.json top-level keys:** `generated_at`, `data_as_of`, `firm_id`, `date_range`, `metadata`, `aua`, `nna`, `adv`

`firm_id` field present in response body — confirms routing to `opal-data-bd/gold/` (not portal-v2).
`is_json_not_html: True` — confirmed real JSON, not the SPA index.html.

**`data_as_of: 2026-03-09`** — current gold date. The bd pipeline ran again after the PRD
was written (PRD cited `2026-03-06` as current at authoring time). `2026-03-09` is correct
and more current.

### 3. No opal-data-portal-v2 Hits

All five endpoints routed through `S3-opal-data-bd` origin (confirmed via CloudFront
distribution config). No request touched `opal-data-portal-v2`. Acceptance criterion 2: PASS.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Accept `data_as_of: 2026-03-09` (not `2026-03-06`) | Pipeline ran again on 2026-03-10 publishing newer data. `2026-03-09` is the last trading day. This is correct, not a regression. |

---

## Files Modified

None.

---

## Blockers

None.

---

## Current State

**Status:** COMPLETE
**Active branch:** portal `DEV`, workspace `CLOUD`

All five advisor-intelligence scoped endpoints verified returning HTTP 200 `application/json`
with current gold data (`data_as_of: 2026-03-09`, `firm_id: bd`) via CloudFront
`d2n2nzpeqf34ge.cloudfront.net`. No portal-v2 hits. ADVI_APISCP acceptance criteria
1 and 2 confirmed. Project ADVI_APISCP is complete from DE perspective.

---

## Next Steps

1. **[0.4.0_DT_ClientPlatform] Commit org changes to CLOUD** — session logs (ADVI_APISCP.001 + .002), task order status updates, escalation doc, daily log.
2. **[0.4.0_DT_ClientPlatform] Push portal DEV** — commits `9c1881a` + `3367cd8` + `1433d2e` + `0a759de` queued from prior sessions.

**Do NOT:**
- Re-open OAC investigation — OAI is the correct model for Lambda@Edge dynamic origin routing in this distribution.
