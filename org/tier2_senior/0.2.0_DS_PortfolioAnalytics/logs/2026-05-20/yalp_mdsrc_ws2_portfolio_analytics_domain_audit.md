# Session Log — YALP_MDSRC.002 WS-2 Portfolio Analytics domain audit

| Field | Value |
|---|---|
| Agent | 0.2.0_DS_PortfolioAnalytics |
| Date | 2026-05-20 |
| Task Order | YALP_MDSRC.002 (WS-2 — Portfolio Analytics domain audit) |
| Status | COMPLETE — audit deliverable shipped; RAVC2 to COO + CC CTO |

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| WS-2 domain audit | docs/briefs/mdsrc-ws2-portfolio-analytics-audit-20260520.md | COO (RAVC2) / CTO (WS-5 synthesis) |
| WS-2 matrix slice | docs/briefs/mdsrc-ws2-matrix-slice-20260520.tsv | WS-5 (matrix merge) |

## What was done

End-to-end audit of the portfolio-analytics domain per YALP_MDSRC.002 / PRD v0.2 WS-2:
- (a) YCharts capability — HAR jq-parsed for analytics endpoints; `all_calc_menu` body
  (3.05 MB, captured in-HAR) parsed directly — 27 categories, 3,077 metrics.
- (b) Portal surfaces — 8 WS-2 yang generator Lambdas read in full; portal surfaces mapped
  via PORTAL_DATA_FLOW.md + portal/src fetch grep (NOT comp-blast, per PRD §5).
- (c) Per-surface classification — 13 WS-2 surfaces classified into the common 14-col
  matrix-slice schema.

## Headline finding

The portfolio-analytics domain is the portal's proprietary core. Of 13 WS-2 surfaces:
1 cleanly YCharts-replaceable (etf_returns), 5 hybrid (Model Portfolios benchmark/peer +
factor spreads), 7 stays-manual (Factor Tilts regression, all Positioning/Attribution, both
CMA). YCharts' analytics catalog is deeper than anything WS-2 renders, but coverage is
orthogonal — the proprietary surfaces' inputs are Opal model holdings, not YCharts-resident
data. Q5 answered (catalog complete but orthogonal); Q6 answered (cma/attribution permanently
manual, peer hybrid/methodology-bound). Q1/Q7 returned open per `<do_not>`.

## Coordination (AC6)

- WS-1 (0.1.0_DS_MarketIntelligence): AGREED the common 14-col matrix-slice schema verbatim
  (MCP 20260520T210037Z). Official-API coverage carried in `notes`, schema kept identical.
- WS-3 (0.4.0_DS_ClientPlatform): opened the Model Portfolios seam (MCP 20260520T210045Z) —
  WS-2 owns benchmark/ETF/peer analytics, WS-3 owns model-portfolio performance sourcing.
  One open item put to WS-3 (model_portfolio_timeseries.json column split).

## Files Modified

| File | Change |
|------|--------|
| docs/briefs/mdsrc-ws2-portfolio-analytics-audit-20260520.md | New — WS-2 domain audit brief |
| docs/briefs/mdsrc-ws2-matrix-slice-20260520.tsv | New — WS-2 migration-matrix slice (14-col) |
| org/tier2_senior/0.2.0_DS_PortfolioAnalytics/task_orders/YALP_MDSRC.002.ds-ws2-portfolio-analytics-domain-audit.md | status pending -> complete |

No code / Terraform / Lambda / portal file changed — PRD v0.2 is audit-only.

## Compiler Tools

| Tool | Command | Result | vs expect |
|------|---------|--------|-----------|
| comp-routes | `comp-routes behaviors` | 23 CF behaviors; behaviors 14-16 = `/api/general/*` + `/json-tiered/*` -> S3 opal-data-portal-v2 via public-data-router + cache-control-injector | PARTIAL MATCH — router/origin as PRD §5; path prefix is `/api/general/*` not PRD's `/api/public/json*`. Recorded as finding (brief §6.4-5). |
| yang->portal map | PORTAL_DATA_FLOW.md + portal/src fetch grep | Full WS-2 surface map produced; 4 doc-staleness deltas found (brief §6.4) | MATCH — comp-blast correctly NOT used (PRD §5: no yang->portal comp-graph edges). |
| YCharts side | none (external system) | Evidence = HAR jq parse + in-HAR all_calc_menu body | MATCH — documented-none per PRD §5. |
| Phase 2 | none (audit doc, no code) | No .py written | MATCH — no py_compile/ruff/ds-precommit gate applies. |
| Phase 3 | none (matrix slice = self-validation) | Slice checked vs AC1-AC7 | MATCH — documented-none. |

comp-routes run auto-logged to org/compiler-tools-log.md via .comp-graph/.agent_context.

## Pipeline-mechanism findings (for AE 0.5.0 consult + WS-5)

1. `yang-generate-benchmark-returns` referenced in the SFN definition but no source dir
   exists; actual producer of benchmark_returns.json is `yang-model-portfolio-benchmarks`.
2. `saa_excel` manifest field consumed by yang-generate-cma but undeclared in PRD §2.1.
3. PORTAL_DATA_FLOW.md CMA path stale (`json/cma/*` -> actual `json/capital-markets/*`).
4. endpoint-mapping.ts line 83 peer path stale (`benchmarks/` -> actual `peers/`).
5. Serving-path prefix delta vs PRD §5 (see Compiler Tools row 1).

## Next Steps

- [COO] RAVC2 — YALP_MDSRC.002 complete; validate brief + matrix slice.
- [CTO] WS-5 synthesis input — consume the WS-2 matrix slice; reconcile the WS-2/WS-3 Model
  Portfolios seam. Recommendation in brief §11.
- [WS-3 / 0.4.0_DS_ClientPlatform] Confirm the model_portfolio_timeseries.json column split
  (model_return = WS-3, benchmark_return + rfr = WS-2/WS-1).
