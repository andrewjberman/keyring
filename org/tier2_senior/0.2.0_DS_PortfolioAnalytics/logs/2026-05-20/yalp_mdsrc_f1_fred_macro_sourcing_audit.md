# Session Log — YALP_MDSRC.F1 FRED macro-sourcing audit

| Field | Value |
|---|---|
| Agent | 0.2.0_DS_PortfolioAnalytics~A |
| Date | 2026-05-20 |
| Task Order | YALP_MDSRC.F1 (dsa-macro-page-input-audit-and-fred-exploration) |
| Status | COMPLETE — audit deliverable shipped; RAVC2 to CTO |

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| FRED macro-sourcing audit | docs/briefs/mdsrc-fred-macro-sourcing-audit-20260520.md | CTO (v0.4 amendment) / COO (RAVC) |
| Bloomberg->FRED mapping table | docs/briefs/mdsrc-fred-macro-mapping-20260520.tsv | implementation TO (machine-readable, 79 rows) |

## What was done

Two-phase Andrew-direct audit per YALP_MDSRC.F1.

PHASE 1 — structured input map of the whole Macroeconomics portal page. 4 components
(MacroHeatmap, YieldCurveTab, VolatilityTab, MacroTimeSeriesModal) -> 4 JSON artifacts
(macro_data.json, yield_curve_fred.json, volatility_data.json, macro/timeseries/*).
All 5 producing Lambdas/scripts read in full (yang-generate-macro, yang-generate-macro-timeseries,
opal-portal-volatility-fetcher, ingest_yield_curve_fred.py, refresh-fred-cache,
generate-volatility). 79 indicators in 12 groups enumerated per-input.

PHASE 2 — FRED API capability exploration. API surface, auth (free key), 120 req/min rate
limit, units= transform param documented. Existing FRED integration characterized as the
extension baseline (official-API path + keyless-CSV path; key in Secrets Manager
opal/external-apis). Every Phase-1 input mapped to FRED with empirical value-fidelity probes
(33+ FRED series pulled via keyless fredgraph.csv, compared to served macro_data.json).

## Headline finding

Of 79 served macro indicators: 50 (63%) cleanly FRED-replaceable (33 direct + 17 transform),
6 (8%) FRED-proxy, 23 (29%) genuine non-FRED residue. Residue concentrates in two whole groups
(Leading Indicator 8/8 + Investor Sentiment 7/7 = licensed survey data). v0.3 WS1-MAC-01
"Bloomberg-leaning hybrid" verdict upgraded to: 63% clean / 71% with proxies / 29% hard residue.
Where FRED and Bloomberg both carry the official series, fidelity is HIGH-to-EXACT (same
underlying BLS/BEA/Census/Fed/Treasury/DOL/UMich source). yield_curve_fred.json already 100%
FRED; volatility VIX already FRED.

## Pipeline-mechanism findings (for implementation TO + WS-5)

- F1: 2 indicators silently dropped — MACRO_GROUPS configures 81, macro_data.json serves 79
  (MOVE + S&P CoreLogic CS have no data_pkl row; Housing count:7 vs 6 served).
- F2: vix_data.json dual-writer — yang-generate-macro and opal-portal-volatility-fetcher both
  write json/macro/vix_data.json (latent; page consumes volatility_data.json).
- F3: yield_curve_fred.json ~4 months stale (data_as_of 2026-01-15) — ingest_yield_curve_fred.py
  has no deployed schedule; the "1Y Ago" yield-curve toggle serves stale FRED data.
- F4: yang-generate-macro invalidates /api/public/macro/* but the served behavior is
  /api/general/* (comp-routes behavior 16).
- F5: doc staleness — MacroHeatmap "73/10 groups" (actual 79/12); macro.ts "FRED API"/"slug=FRED
  series ID" (actually Bloomberg-pkl, slugified name); portal-proxy getVolatilityData producer
  attribution wrong; portal/etl macroeconomics README dated 2025-12-17 describes removed components.
- F6: Secrets Manager region inconsistency — generate-volatility reads opal/external-apis from
  us-east-2, opal-portal-volatility-fetcher from us-east-1.

## Files Modified

| File | Change |
|------|--------|
| docs/briefs/mdsrc-fred-macro-sourcing-audit-20260520.md | New — FRED macro-sourcing audit brief |
| docs/briefs/mdsrc-fred-macro-mapping-20260520.tsv | New — 79-row Bloomberg->FRED mapping table |
| org/tier2_senior/0.2.0_DS_PortfolioAnalytics/task_orders/YALP_MDSRC.F1.dsa-macro-page-input-audit-and-fred-exploration.md | status pending -> complete |
| org/tier2_senior/0.2.0_DS_PortfolioAnalytics/logs/2026-05-20/yalp_mdsrc_f1_fred_macro_sourcing_audit.md | New — this log |

No code / Terraform / Lambda / portal file changed — PRD v0.2 is audit-only.

## Compiler Tools

| Tool | Command | Result | vs expect |
|------|---------|--------|-----------|
| comp-routes | `comp-routes behaviors` | 23 CF behaviors; behavior 16 /api/general/* -> S3 opal-data-portal-v2 via public-data-router + cache-control-injector | MATCH — anchors per-artifact serving-path column. /api/general prefix vs PRD /api/public/json* delta recorded |
| comp-pipescript | `comp-pipescript io yang-generate-macro` + `-macro-timeseries` | "Unknown script" — yang generators not comp-graph nodes | MISMATCH handled per TO if_mismatch — fell back to direct source read of infra/aws/lambda/v2_portal/yang_pipeline/ |
| FRED probe | keyless fredgraph.csv x33+ series | empirical value-fidelity (brief §3.4) | MATCH — official-series fidelity HIGH/EXACT; residue + proxies confirmed |
| Phase 2/3 gates | none (audit doc, no .py authored) | no py_compile/ruff/ds-precommit applies | per TO mandate phase 2/3 = documented-none |

comp-routes auto-logged to org/compiler-tools-log.md via .comp-graph/.agent_context.

## Next Steps

- [CTO] RAVC2 — YALP_MDSRC.F1 complete; consume the audit + mapping table for the v0.4
  amendment; WS1-MAC-01 verdict upgrade in brief §4.
- [Implementation TO, later] FRED macro-ingestion Lambda (50 indicators, ingest_yield_curve_fred.py
  pattern). Independent fixes F1/F3 (user-visible) recommended ahead of the migration.
