# COO Delivery Status — Updated 2026-03-19

This file is the volatile dashboard. Corrected at every COO startup from agent logs,
git tags, and task order `<status>` fields. Do not treat as authoritative between sessions.

---

## Active Projects

| Project | Status | Pending Work |
|---------|--------|-------------|
| `DRFR_PTMCH` | P1-P6a COMPLETE | All backend + frontend delivered. 0.3.3 RD HistoryTab COMPLETE. Portal DEV not pushed/merged to PROD. P6b-d deferred. |
| `ADVI_MVPLVL` | NEAR-COMPLETE | ConsolidatedOverviewPanel live on portal DEV (62143e7). NEW: DS MVPLVL.007 (advisor timeseries endpoints for L2) + MVPLVL.008 (open_lots field names) issued 2026-03-18, pending. L2 view is skeleton until .007 done. Portal merge also gated on MVP318 WS5 (DE chart windows). |
| `ADVI_ADVTV2` | DS COMMITTED (8ef1da9b). EC2 deploy done (72c03d2a). | DT ADVTV2.002 (FULL gold layer run + rel_architect_lookup verification) pending. Will be batched into MVP318.003 full gold run by AE. |
| `ADVI_MIXV2` | DS + DE + DT COMPLETE | DS 001+002 committed. DE 005 (cbb9d38, fcb95c7 on portal DEV). DT 004 (partners-api-v1.3.0). AE 003 (06b EC2 deploy + gold run) in_progress/pending. Portal DEV->PROD merge pending (shared gate with ADVI_MVPLVL). |
| `ADVI_MVP318` | WS1-WS5 CODE COMPLETE. bd-v2.19.2 + partners-api-v1.4.0 deployed. | WS6 gate: WS4 (RD) DONE. WS5 (DE chart windows ADVI_MVP318.004 req 3) PENDING. AE.003 full gold run PENDING. DE.004 WS3e (advisor types+API functions) PENDING. DT portal DEV->PROD merge BLOCKED until WS5 done. |

## Recently Completed

| Project | Completed | Notes |
|---------|-----------|-------|

## Pod 4 (ClientPlatform) -- Status as of 2026-03-19

| Agent | Last Known Work | Status |
|-------|----------------|--------|
| 0.4.0_DE | MIXV2 WS4+WS5: firm mix chart (cbb9d38) + ClientDetailPage wiring (fcb95c7) committed to portal DEV 2026-03-18. | PENDING: ADVI_MVP318.004 (WS3e advisor types+functions, WS5 chart windows). WS3e gate cleared (partners-api-v1.4.0 live). |
| 0.4.0_DT | bd-v2.19.0 (WS2+WS3b), bd-v2.19.1 (WS1 fix), bd-v2.19.2 (API Gateway routes) deployed 2026-03-18. partners-api-v1.3.0 + v1.4.0 deployed. | PENDING: Portal DEV->PROD merge (WS6). Gate: DE MVP318 WS5 + AE gold run completion. |
| 0.4.0_DS | MVP318.001 COMPLETE (eb70758d, a3903a03, 6234d50c, fec1f7e4). ETF ticker fix done (b69d1ae6). | PENDING: MVPLVL.007 (advisor timeseries endpoints for L2 quarterly bar) + MVPLVL.008 (open_lots field canonicalization). Both issued 2026-03-18. |
| 0.4.2_RD | ConsolidatedOverviewPanel committed to portal DEV (62143e7), CLOUD pointer at a8b1c3e8. Issued MVPLVL.007+.008 to DS/DE. | IDLE (panel done; waiting DS .007 to wire L2 data). |

## Shared Services -- Status as of 2026-03-19

| Agent | Last Known Work | Pending |
|-------|----------------|---------|
| 0.5.0_AE_OpalETL | P5 + P6a complete (2026-03-12) | No pending DRFR_PTMCH work. P6b-d deferred. |
| 0.6.0_AE_PartnerETL | Script 07 isolation run complete (b2119882). ETF ticker fix (b69d1ae6). 06b wired (d1bd3a18). | PENDING: MVP318.003 FULL gold run (batches ADVTV2.002 + MIXV2.003 + WS5 script 10). Gate: DT confirms bd-portal-advisor-publisher deployed (DONE at bd-v2.19.0). Run is unblocked. |
| 0.7.0_AE_CloudOps | APISCP.007 dynamo patch + CF cache (2026-03-10) | None pending |
