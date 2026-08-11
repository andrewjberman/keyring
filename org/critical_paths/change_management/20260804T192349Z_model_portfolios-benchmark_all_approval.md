# SURFACE_ACK approval -- 20260804T192349Z

**class:** approval
**surfaces:** model_portfolios.benchmark,model_portfolios.headline
**firm:** all
**commit:** c56de73f78fb
**reason:** Andrew-direct 2026-08-04 (DE terminal): kill-both ruling on participation UI -- deletion-only change removing CI-R6R T2/T3 rendering; no benchmark/headline data-path logic touched; same authority+pattern as accepted 68fd700c

## Touched surfaces

- `portal/src/api/endpoints/aum.ts` (model_portfolios.headline, SEV1)
- `portal/src/api/portal-proxy.ts` (model_portfolios.benchmark, SEV1)
- `portal/src/components/BenchmarkHeatmap.tsx` (model_portfolios.benchmark, SEV1)
- `portal/src/pages/ModelPortfolios.tsx` (model_portfolios.benchmark, SEV1)
- `portal/src/pages/ModelPortfolios.tsx` (model_portfolios.headline, SEV1)

Durable record (D8-AE B1, NFRA_GRAPHS). See org/surface-check-ack-audit.log for the one-line summary.
