# SURFACE_ACK approval -- 20260804T165324Z

**class:** approval
**surfaces:** model_portfolios.benchmark,model_portfolios.headline
**firm:** all
**commit:** d3b6ecc18538
**reason:** Andrew-direct order this session: adjust all FE listings LTC->LT / LTA->ULT (Yang model-code rename); SEV1 surfaces are the deliberate target; tsc -b clean + observed renders (live 3-model + mutant 5-model) on record; DT deploys on Andrew's word

## Touched surfaces

- `portal/src/api/endpoints/aum.ts` (model_portfolios.headline, SEV1)
- `portal/src/api/portal-proxy.ts` (model_portfolios.benchmark, SEV1)
- `portal/src/components/BenchmarkHeatmap.tsx` (model_portfolios.benchmark, SEV1)

Durable record (D8-AE B1, NFRA_GRAPHS). See org/surface-check-ack-audit.log for the one-line summary.
