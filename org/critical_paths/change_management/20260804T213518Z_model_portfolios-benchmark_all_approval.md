# SURFACE_ACK approval -- 20260804T213518Z

**class:** approval
**surfaces:** model_portfolios.benchmark,model_portfolios.headline
**firm:** all
**commit:** da790f53f1c6
**reason:** ANDREW-ASSIGNED LT/ULT closure (0.4.0_DE relay 202936Z, CTO canon 203229Z): portal-proxy change is a 4-line canonicalizeCodeKeys read seam on getHoldingsAttribution (attribution artifact, not benchmark logic); tsc clean + through-seam LT render observed via ui-smoke

## Touched surfaces

- `portal/src/api/portal-proxy.ts` (model_portfolios.benchmark, SEV1)
- `portal/src/components/BenchmarkHeatmap.tsx` (model_portfolios.benchmark, SEV1)
- `portal/src/pages/ModelPortfolios.tsx` (model_portfolios.benchmark, SEV1)
- `portal/src/pages/ModelPortfolios.tsx` (model_portfolios.headline, SEV1)

Durable record (D8-AE B1, NFRA_GRAPHS). See org/surface-check-ack-audit.log for the one-line summary.
