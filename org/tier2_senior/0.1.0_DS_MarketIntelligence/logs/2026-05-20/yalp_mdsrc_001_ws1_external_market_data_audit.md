# Session Log -- 0.1.0_DS_MarketIntelligence
**Date:** 2026-05-20
**Branch:** CLOUD
**Task Order:** YALP_MDSRC.001 -- WS-1 External Market Data domain audit (from 2.0.0_SA_COO)

---

## Summary

Completed YALP_MDSRC.001 (WS-1) -- the External Market Data domain audit for the portal market-data-sourcing project. Audited (a) YCharts backend capability for market-data classes, (b) the portal surfaces in the domain (Market Overview, Valuation, Correlation, Macroeconomics + the DynamoDB price series), (c) per-surface source classification. Audit-only deliverable per PRD v0.2 -- no code/Terraform/portal change.

This TO was the WS-1 slice of a 5-workstream project (YALP_MDSRC) that the CTO decomposed from my own Phase-0 scoping brief earlier the same session.

## Verdict

The external-market-data domain is **largely YCharts-replaceable**. Of 12 WS-1 surfaces: 6 YCharts-replaceable (incl. the DynamoDB 71-entity price-series backbone, Market Overview heatmap/RSI/timeseries, Valuation multiples), 3 hybrid (market regime, risk premium, correlation -- Opal keeps the computation, inputs migrate), 2 already-API-sourced (VIX + yield curve already on FRED), 1 Bloomberg-pkl-leaning hybrid (macro indicators, Bloomberg-ticker-keyed).

## Findings of record

- **F1 (load-bearing):** YCharts enforces a SINGLE concurrent session per credential -- empirically proven, the live-probe session was evicted mid-batch with HTTP 403 "You have been signed out due to a concurrent sign in using your credentials." A programmatic pull on a shared seat mutually evicts a human user. Hard mark against the session-scrape path; pushes toward a dedicated seat or the official API. Shared with WS-2/3/4.
- **F2:** PORTAL_DATA_FLOW.md (2026-01-19) is stale -- maps VIX to yang-generate-macro/data_pkl, but the live vix_data.json is FRED-sourced (data_source field = "FRED VIXCLS") on an independent daily cadence.
- **F3:** Serving-path delta -- PRD §5 + PORTAL_DATA_FLOW.md state /api/public/json*; comp-routes behaviors + portal/src grep show the WS-1 pages actually use /api/general/* (no /api/public/* CloudFront behavior exists). Minor; RAVC1 note to COO.
- **F4:** AWS WAF does NOT block headless replayed-token requests -- captured aws-waf-token replayed from plain curl returned HTTP 200 ~5.5h post-capture. WAF gates initial token acquisition only.
- **F5:** VIX + Treasury yield curve are already off Bloomberg-pkl (FRED-sourced today) -- the migration is partly already done.

## Q-resolution contributed to WS-5

- Q3 (WAF defeats headless capture?) -- ANSWERED: no (F4). Shared org-wide; WS-2/3/4 all ACK'd, no triplication.
- Q5 (catalog coverage) -- ANSWERED for WS-1: YCharts metric coverage for external market data is effectively complete (rsi_14, 64 total-return variants, 102 valuation multipliers, 34 std-dev metrics all index-applicable; correlation is the only non-primitive, computed from series YCharts supplies).
- Q1/Q7 (official API vs scrape / ToS) -- evidence contributed (Section 3.4 of the brief), leans official-API for this domain; NOT pre-decided (Andrew + CTO call at v0.3).
- New: WS1-MAC-01 needs a per-indicator Bloomberg-ticker -> FRED/YCharts mapping to quantify the genuinely Bloomberg-proprietary macro residue -- recommended to WS-5 as a small v0.3 task.

## Compiler Tools

| Phase | Tool | Command | Result vs expect |
|-------|------|---------|------------------|
| 1 before | comp-routes | `comp-routes behaviors` | PASS with delta -- confirmed public-data-router Lambda@Edge -> S3 opal-data-portal-v2 (behaviors 14/16) + direct /json-tiered/* (15). Delta: actual prefix /api/general/* not PRD §5's /api/public/json* -- recorded as finding F3. |
| 1 before | yang->portal map | PORTAL_DATA_FLOW.md + portal/src/api fetch grep (NOT comp-blast, per PRD §5) | PASS with staleness -- map obtained; PORTAL_DATA_FLOW.md found stale on VIX source + /api/public path (F2/F3). |
| 1 before | YCharts side | none (external system) | Documented-none per PRD §5: YCharts is not in the comp-graph; evidence base is the HAR (jq parse) + live-probe capture. |
| 2 before commit | none | -- | Audit deliverable -- no .py/Terraform/portal code authored; py_compile/ruff/ds-precommit gates N/A. |
| 3 after commit | none | -- | The WS-1 matrix slice is the deliverable's self-validation vs AC1-AC7. |

Compiler-tools-log.md row auto-appended by the comp-routes run.

## Files Modified

| File | Change |
|------|--------|
| `docs/briefs/mdsrc-ws1-external-market-data-audit-20260520.md` | NEW -- WS-1 domain audit brief |
| `docs/briefs/mdsrc-ws1-matrix-slice-20260520.tsv` | NEW -- WS-1 migration-matrix slice (14-col common schema; matches WS-2's standalone-TSV convention) |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/task_orders/YALP_MDSRC.001.ds-ws1-external-market-data-domain-audit.md` | status pending -> complete |
| `org/tier2_senior/0.1.0_DS_MarketIntelligence/logs/2026-05-20/yalp_mdsrc_001_ws1_external_market_data_audit.md` | NEW -- this session log |

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| WS-1 External Market Data domain audit | `docs/briefs/mdsrc-ws1-external-market-data-audit-20260520.md` | 2.0.0_SA_COO (RAVC2) + 1.0.0_SA_CTO (WS-5 synthesis) |

## RAVC Inbound / Outbound

| RAVC | From | To | Status |
|------|------|----|--------|
| GO YALP_MDSRC.001 | 2.0.0_SA_COO | 0.1.0_DS | RECEIVED |
| ACK YALP_MDSRC.001 | 0.1.0_DS | 2.0.0_SA_COO | SENT |
| Matrix-slice schema proposal | 0.1.0_DS | 0.2.0_DS + 0.4.0_DS_ClientPlatform | SENT -- both AGREED verbatim |
| Q3 auth/WAF shared finding | 0.1.0_DS | 0.7.0_AE_CloudOps + 0.2.0_DS + 0.4.0_DS_ClientPlatform | SENT -- all 3 ACK'd, no re-probe |
| RAVC2 (WS-1 complete) | 0.1.0_DS | 2.0.0_SA_COO + CC 1.0.0_SA_CTO | SENT this closeout |

## Coordination

- Common 14-column matrix-slice schema proposed by WS-1, AGREED verbatim by WS-2 (0.2.0_DS) and WS-3 (0.4.0_DS_ClientPlatform) -- the three domain slices compose at WS-5.
- Q3 auth/WAF probe done once by WS-1, shared; WS-2/3/4 consumed it without re-probing (PRD §4 anti-triplication satisfied).
- WS-2 complete same session (briefs 7de5d3b69 + 368510231); catalog counts cross-checked and agree (3,836 items / 27 categories). WS-3 starts after ADVI_INFGRO.009 per COO sequencing; schema confirmed regardless.
- Model Portfolios seam: WS-1 does not touch it -- clean.

## Next Steps

1. [CTO 1.0.0_SA_CTO] WS-5 synthesis -- compose WS-1/WS-2/WS-3 matrix slices into the migration decision matrix; WS-1 slice is `docs/briefs/mdsrc-ws1-matrix-slice-20260520.tsv`.
2. [CTO/Andrew] Q1 (official API vs scrape) + Q7 (ToS) -- WS-1 evidence leans official-API for this domain; F1 (single concurrent session) is the decisive operational mark. Andrew business call at v0.3.
3. [WS-5] Scope a small v0.3 task: per-indicator Bloomberg-ticker -> FRED/YCharts mapping for WS1-MAC-01 to quantify the Bloomberg-proprietary macro residue.
4. [DS 0.1.0_DS_MarketIntelligence] Available for WS-5-adjacent follow-ups or a v0.3 implementation TO on GO.
