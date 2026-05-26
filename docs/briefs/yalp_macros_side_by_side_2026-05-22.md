# YALP_MACROS — Side-by-side spreadsheet (T*=2026-05-22)

**TO:** YALP_MACROS.005
**Generated:** 2026-05-26 ~19:25Z
**Rows:** 134
**CSV:** `yalp_macros_side_by_side_2026-05-22.csv`

## §0 — DRIFT-status surface (Top-of-doc per YALP_MKTOVR precedent)

**ZERO material DRIFT findings** in yang-side internal-consistency verification (Path X scope).

**Verdict distribution:**
- **n/a-YCHARTS-COVERAGE-PENDING**: 134

## §1 — Per-component summary

All rows tagged `n/a-YCHARTS-COVERAGE-PENDING` per Path X ruling 19:15Z (YCharts macro-class symbol-resolution gap; YALP_MDSRC A4/A5 reverse-engineer FUTURE-TO scope). Yang-side internal-consistency Level-2 verification COMPLETE per 4-axis methodology — see `level2_verification_results.json` for detailed axis verdicts.

### Component cutover-trust verdicts (TO-VAL preview):

| Component | Verdict | Rationale |
|---|---|---|
| YieldCurveTab | **NEEDS-INVESTIGATION-YCharts-coverage-pending** | yang-side internal MATCH (single Treasury Yields source for current+1M; FRED daily for 1Y-ago); YCharts cross-validation deferred per Path X |
| MacroHeatmap | **NEEDS-INVESTIGATION-YCharts-coverage-pending** | yang-side internal MATCH for 79/79 indicators (Axis 3 distribution sanity PASS); 2 declared_count discrepancies surfaced as structural finding F4+F5 |
| MacroTimeSeriesModal | **NEEDS-INVESTIGATION-YCharts-coverage-pending** | yang-side slug-resolution MATCH 79/79 (Axis 4 enumeration PASS); per-slug history payload available; YCharts cross-validation deferred |
| VolatilityTab | **NEEDS-INVESTIGATION-YCharts-coverage-pending + STRUCTURAL-FINDING** | VIX cross-pipeline REPRESENTATIVE convergence (yang 16.7 vs market-overview 16.76 = 0.36%); MOVE yang-side gap (Market Indicator declared_count=2 actual=1 — MOVE missing from macro_data.json) |

## §2 — Structural findings (yang-side; net-new from TO-004)

1. **F4 — Market Indicator group declared_count=2 actual_indicators=1:** VIX present, MOVE MISSING from macro_data.json. MOVE present in volatility_data.json (market-overview pipeline). Either declared_count is wrong (-1) or yang-generate-macro should ingest MOVE per the declared spec. **Yang-pipeline bug class.**
2. **F5 — Housing Market group declared_count=7 actual_indicators=6:** 1-indicator gap in declared vs actual. Either declared_count is wrong or yang-generate-macro is missing 1 housing indicator. **Yang-pipeline bug class.**
3. **F6 — L1 lineage map §6.4 stale:** L1 claims 84 indicators total; empirical = 79 actual / 81 declared-summed. 3-5 indicator discrepancy in canonical L1 reference. **L1 update candidate.**

Per ws COO Path X disposition: DRIFT-routing rule (close-MCP to CTO + COO + Andrew) does NOT apply — these are yang-side internal gaps, NOT cutover DRIFT. Route as standard structural findings banked for future-project consideration; flag-only.

## §3 — Methodology

Per brief §1.4 v1.1 multi-T* per DS 0.2.0 consult `cb8760199` + brief §11 TO-002 results (cookie-stale-OK + corpus reuse) + brief §12 placeholder (TO-004 4-axis methodology).

Per-axis verdicts (full detail in `level2_verification_results.json`):
1. **Axis 1 VIX/MOVE cross-pipeline integrity gate:** MATCH-REPRESENTATIVE convergence
2. **Axis 2 Treasury Yields cross-component validation:** MATCH (trivially consistent; single yang source)
3. **Axis 3 Macro indicator value-distribution sanity:** MATCH (79/79 indicators have value+percentile; 0 out-of-range)
4. **Axis 4 Indicator-universe enumeration + slug-resolution:** MATCH (79 macro_data indicators ↔ 79 timeseries slugs; perfect 1:1)