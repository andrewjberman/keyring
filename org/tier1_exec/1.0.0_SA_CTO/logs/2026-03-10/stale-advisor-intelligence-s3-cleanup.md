# Stale Advisor-Intelligence S3 Path Deletion — 1.0.0_SA_CTO

**Date:** 2026-03-10

## Objective

Delete orphaned advisor-intelligence JSON files from `opal-data-portal-v2` that were left behind after the portal migrated to the scoped proxy architecture reading from `opal-data-bd/gold/`. These stale files caused confusion during an investigation — a query hit the wrong bucket and returned 2-month-old data that appeared current.

---

## What Was Deleted

### Path 1: `s3://opal-data-portal-v2/api/public/advisor-intelligence/`

92 files. All frozen at **2026-01-16**.

| File | Size |
|------|------|
| `architect_leaderboard.json` | 12KB |
| `implementor_leaderboard.json` | 33KB |
| `clients_tab.json` | 278KB |
| `clients/{z_id}.json` | ~89 individual client detail files, ~5-6KB each |

This was the original direct-from-S3 path when the portal read via CloudFront without a proxy. Superseded by the scoped proxy.

### Path 2: `s3://opal-data-portal-v2/json/advisor-intelligence/`

95 files. Mixed staleness: Jan 16 to Feb 20, 2026.

| File | Size | Last Modified |
|------|------|---------------|
| `architect_leaderboard.json` | 71KB | 2026-02-20 |
| `implementor_leaderboard.json` | 195KB | 2026-02-20 |
| `clients_tab.json` | 278KB | 2026-02-18 |
| `flows_chart.json` | 2.3MB | 2026-02-20 |
| `timeseries_chart.json` | 1.3MB | 2026-02-20 |
| `aua_chart.json` | 643 bytes | 2026-02-18 |
| `clients/{z_id}.json` | ~89 client files | 2026-01-16 |

This was the intermediate path used before the scoped proxy. `aua_chart.json` was a deprecated artifact with no equivalent in gold (643 bytes, likely a stub or empty response).

### Total: 187 files deleted

---

## Why These Were Safe to Delete

1. **No active writer exists.** Searched all Lambda source (`infra/aws/lambda/`), EC2 services (`infra/aws/ec2/`), and Terraform configs. Nothing in the current codebase writes to `api/public/advisor-intelligence/` or `json/advisor-intelligence/` on `opal-data-portal-v2`.

2. **The portal does not read from these paths.** The AdvisorIntelligence page calls `/api/scoped/advisor-intelligence/timeseries_chart.json`, which the proxy resolves to `s3://opal-data-bd/gold/timeseries_chart.json`. The `api/public/` and `json/` prefixes are not referenced by any frontend endpoint.

3. **The canonical data lives in `opal-data-bd/gold/`.** The `bd-portal-publisher` Lambda writes exclusively to `opal-data-bd` (env vars `INPUT_BUCKET` and `OUTPUT_BUCKET` both default to `opal-data-bd`). Gold data is current through 2026-03-10.

---

## Canonical Data Path (unchanged)

All advisor-intelligence data is served from:

```
s3://opal-data-bd/gold/
  timeseries_chart.json     (29.7MB, 2026-03-10)
  architect_leaderboard.json
  implementor_leaderboard.json
  clients_tab.json
  flows_chart.json
  advisor_rolling_flows.json
  client_performance.parquet
  client_dimension.parquet
  advisor_assignments_history.parquet
  clients/                  (per-client detail JSONs)
  client_detail/            (detailed client data)
  advisors/                 (per-advisor data)
  timeseries/               (per-advisor timeseries)
```

Written by: `bd-portal-publisher` Lambda (triggered by `opal-data-bd/gold/pipeline-complete.json`).
Read by: portal scoped proxy via `/api/scoped/advisor-intelligence/*`.

---

## Decisions Made

| Decision | Rationale |
|----------|-----------|
| Delete both prefixes entirely, not selectively | No file in either prefix is referenced by any active system. Partial cleanup would leave the same confusion risk. |
| No backup taken | Files are 2+ months stale and contain no data not already present (and more current) in `opal-data-bd/gold/`. |

---

## Current State

**Status:** COMPLETE

Both stale prefixes are deleted. Verified 0 files remain at either path. The portal continues to serve correctly from `opal-data-bd/gold/` via the scoped proxy.
