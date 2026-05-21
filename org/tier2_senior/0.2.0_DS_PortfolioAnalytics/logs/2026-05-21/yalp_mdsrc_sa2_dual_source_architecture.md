# Session Log — YALP_MDSRC.SA2 Model Portfolios/Factor Tilts + dual-source architecture

| Field | Value |
|---|---|
| Agent | 0.2.0_DS_PortfolioAnalytics |
| Date | 2026-05-21 |
| Task Order | YALP_MDSRC.SA2 (v0.4 WS-B — headline dual-source model-data architecture) |
| Status | COMPLETE — assessment + architecture design committed; RAVC2 to COO CC CTO |

## Briefs Written

| Brief | Path | Audience |
|-------|------|----------|
| SA2 assessment + dual-source design | docs/briefs/mdsrc-sa2-model-portfolios-factortilts-dualsource-20260521.md | COO (RAVC2) / CTO / implementation follow-on |

## What was done

SA2 = (a) component assessment of Model Portfolios + Factor Tilts, (b) the v0.4 HEADLINE:
design of the dual-source model-data abstraction (CTO R2 / Andrew vendor-lock-avoidance).

Headline design: a source-abstraction layer where the model-performance series is sourced
from YCharts (preferred) OR SmartX (alternate) via a config switch, both feeding the
unchanged model_portfolio_timeseries.json / model_portfolio_benchmarks.json contract,
R3-additive-compatible (model.pkl design series retained; sourced realized series added).
Key honest nuance resolved: the two legs are NOT identical by construction — SmartX is
realized managed-account return (the S2 daily /models/{id}/performance find), YCharts is a
reconstruction from constituent returns + Opal weights — so parity (AC3) is specified as a
characterized-tolerance gate (fee/cash-drag/trade-timing wedge), not bitwise equality, with
fail-safe degrade + a divergence alarm.

## Findings

- Model Portfolios: benchmark/ETF legs YCharts-replaceable; model-performance legs = the
  dual-source target; peer performance hybrid/methodology-bound.
- Factor Tilts: largely Opal-proprietary (the 6-factor regression); only the market
  factor-spread inputs are YCharts-reconstructable (gated on C5 ratification).
- model_portfolio_timeseries.json has exactly ONE consumer — ReturnVolatilityScatter.tsx
  (MDLP_RVVALT); no siblings — clean R3 additive change.

## Files Modified

| File | Change |
|------|--------|
| docs/briefs/mdsrc-sa2-model-portfolios-factortilts-dualsource-20260521.md | New — SA2 deliverable |
| org/tier2_senior/0.2.0_DS_PortfolioAnalytics/task_orders/YALP_MDSRC.SA2*.md | status pending -> complete |

No code/Terraform/portal change — assessment + architecture design only (implementation is a follow-on TO).

## Compiler Tools

| Phase | Tool | Result |
|------|------|--------|
| 1 | comp-platinum reverse (json/benchmarks/**, json/factor-tilts/**) | No components returned (PRD §5 — comp-graph thin on yang pages); portal/src fetch-grep fallback -> model_portfolio_timeseries.json = 1 consumer (ReturnVolatilityScatter), model_portfolio_benchmarks.json -> ModelPortfolios.tsx |
| 2 | comp-cache collisions | 4 collisions project-wide, all advisor-intelligence domain; model-data key ['model-portfolio-timeseries'] single-consumer collision-free; dual-source keeps same fetch shape -> no new key. Clean. |
| 3 | (design self-check) | dual-source parity method specified — characterized-tolerance + freshness gate, two-sided, per-leg, pre-serve (brief §4) |

## Next Steps

- [COO] RAVC2 — SA2 complete; feeds v0.4 implementation.
- [0.4.0_DS] SA2 design targets the R3-additive model_portfolio_timeseries.json contract —
  coordinated; consumer enumeration (ReturnVolatilityScatter sole) shared with B3/B4.
- [0.2.0_DS] SA3 next (sequenced) — Attribution + Positioning + Valuation assessment.
