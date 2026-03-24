# DEBT_1STRUN Scan — 0.4.1_RD_ModelPortfolios
**Date:** 2026-03-23
**Scope:** portal/src/pages/ModelPortfolios.tsx, portal/src/pages/ModelPortfolios/tabs/PeersTab.tsx

## Findings

| # | File | Lines | Category | Severity | Description |
|---|------|-------|----------|----------|-------------|
| 1 | ModelPortfolios.tsx | 257-259 | C1 Dead | Medium | `aggregateMetrics` is destructured from the `useMemo` return value but never referenced in the component JSX or any downstream logic. Dead variable adding confusion to the data flow. |
| 2 | ModelPortfolios.tsx | 639 | C1 Dead | Low | `isSelected` is declared for the Non-Model legend item but never used — the Non-Model legend renders a plain `<div>` with no conditional styling, unlike the model legend buttons that use their `isSelected`. |
| 3 | ModelPortfolios.tsx | 180, 191, 197, 203, 209, 225 | C2 Deprecated | Low | Six `PHASE1_PF_REQ_00X` checkpoint comments remain from the initial data-loading rollout. The phase is complete and all queries are enabled — these comments are stale markers that add noise. |
| 4 | ModelPortfolios.tsx | 801 | C2 Deprecated | High | Emoji character `U+26A0 U+FE0F` used in the distribution-unavailable fallback (`<span className="text-2xl">...`). Violates CLAUDE.md rule 13 — emojis break CloudWatch log queries on Windows and corrupt CI/CD pipelines that capture stdout. Replace with an ASCII icon or Lucide component. |
| 5 | ModelPortfolios.tsx | 1066-1123, 1288-1343 | C3 Duplication | High | The custom tooltip renderer for the stacked BarChart and the AreaChart are near-identical (~55 lines each): both compute total, sort by MODEL_ORDER, and render the same JSX structure. A single shared `<ChartTooltip>` component would eliminate this duplication. |
| 6 | ModelPortfolios.tsx | 1125-1153, 1345-1373 | C3 Duplication | Medium | The custom Legend renderer is duplicated between the BarChart and AreaChart — same MODEL_ORDER map, same color lookup, same Non-Model conditional. Should be extracted to a shared `<ModelLegend>` component. |
| 7 | ModelPortfolios.tsx:58-64, PeersTab.tsx:112-121 | 58-64 / 112-121 | C3 Duplication | Medium | Model portfolio canonical order is defined twice: `MODEL_ORDER` (full names) in the parent page and `MODEL_CODE_ORDER` + `MODEL_CODE_TO_NAME` (code-to-name mapping) in PeersTab. If a model is renamed or reordered, both files must be updated in sync — drift risk. A shared constant file would eliminate this. |
| 8 | PeersTab.tsx | 21 | C4 Hardcoded | Medium | `INCEPTION_DATE = '2024-04-30'` is hardcoded. If the inception date changes or differs per model, this becomes a silent bug. Should come from the API response or a shared config. |
| 9 | ModelPortfolios.tsx | 1186 | C4 Hardcoded | Medium | Footnote text hardcodes `~50 newly opened holdings` as a static string. The actual unfunded count is dynamic (computed on lines 777 and 743 for other footnotes). This footnote should use the computed value or be removed since the per-model footnotes already handle this correctly. |
| 10 | ModelPortfolios.tsx | 599-600 | C4 Hardcoded | Low | Donut chart dimensions `width={380} height={380}` are hardcoded magic numbers. Not responsive to container size changes. |
| 11 | ModelPortfolios.tsx | 538-543 | C4 Hardcoded | Low | ApexCharts animation config uses magic numbers (speed: 800, delay: 150, dynamicAnimation speed: 350) with no named constants explaining the intent. |
| 12 | ModelPortfolios.tsx | 800-810 | C6 Stale Error | Medium | Distribution-unavailable fallback tells the user "Account distribution analysis requires CORS configuration on the S3 bucket. The feature works in production but may not be accessible in local development." This is a developer-facing debug message, not actionable user feedback. Production users should never see CORS details. |
| 13 | ModelPortfolios.tsx | 239 | C6 Stale Error | Low | Error state is a hardcoded generic string `'Failed to load AUA metrics. Please try again.'` that discards the actual `metricsError` object. The real error (network timeout, 403, 500) is swallowed — no detail reaches the user or logs. |

## Summary
- Total findings: 13
- By category: C1: 2, C2: 2, C3: 3, C4: 4, C5: 0, C6: 2
- C5 (Orphaned Infrastructure): None found — all imports are consumed, all query hooks feed rendered UI, all tab routes resolve to active components.
- High severity: 2
- Recommended priority fixes:
  1. **#4 (C2 High)** — Remove emoji from line 801. Direct CLAUDE.md violation; blocks CI/CD on Windows. Trivial fix (replace with Lucide `AlertTriangle` icon or ASCII text).
  2. **#5 (C3 High)** — Extract shared tooltip renderer. Two 55-line blocks are nearly identical; any tooltip change must be made twice. Extract to `<ModelChartTooltip>` component.
  3. **#9 (C4 Medium)** — Replace hardcoded `~50` footnote with computed value. The infrastructure to compute it already exists (lines 743, 777); the count-mode footnote just isn't using it.
