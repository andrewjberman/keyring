# ANDREW-DIRECT 2026-09-24 ~05:3xZ -- Performance tab: the full-width time-series panel uses the "AUA Trend Analysis" area-chart style from /portfolios

**Channel:** the `4.0.0_SA_CRO~F` terminal, mid-turn, after the DSGN_IRPTV1 brief was committed.
**Received by:** `4.0.0_SA_CRO~F`. **Relayed to:** `1.0.0_SA_CTO`, `0.0.0_AB_MSTR` (brief addendum for L2).

## VERBATIM

> Also Something I want to be included in the Performance reporting. I think there should be some panel somewhere, whatever the full-wide time series performance one is (recommend using the area chart style from "AUA Trend Analysis" on opalinvest.dev/portfolios for this). You may have already included that functionality i think i saw it in your "Performance" /draw, but wanted to mention that again

## What it pins

- The concept already carries it: CONCEPTS s.2.3, the "Cumulative return, portfolio vs benchmark (area, hover = date/value)"
  full-width row. This word names its STYLE reference.
- The reference, measured at portal DEV HEAD: `portal/src/pages/ModelPortfolios.tsx`, the Growth tab's panel titled
  `${assetLbl.short} Trend Analysis` (`:1320`, `aumView === 'trend'`), rendered by the recharts `<AreaChart>` at `:2099`
  with per-series `<linearGradient>` fills (`:2114`) and `<ReferenceArea>` period shading (`:2164`).
- Data: `PerformanceReport.dailyCumulative` (portfolio series, on the wire today); the benchmark overlay waits on the
  benchmark daily series (brief Part IV.3, a P item per CTO 100194).
- Landed in the brief as O4's chart clause (`docs/briefs/irpt-page-remediation-brief-20260924.md`), same commit as this
  record. Surfaced, not adjudicated: `1.0.0_SA_CTO` cuts it at L2.
