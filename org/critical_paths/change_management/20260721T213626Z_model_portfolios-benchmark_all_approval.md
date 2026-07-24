# SURFACE_ACK approval -- 20260721T213626Z

**class:** approval
**surfaces:** model_portfolios.benchmark,model_portfolios.headline
**firm:** all
**commit:** fb885c8d3e59
**reason:** MDPF_REVAMP.S5 dead-endpoint cleanup: remove getAUMTimeSeries/getModelTimeSeries (0 consumers after A2 2f603319, grep-verified); pure dead-code removal, typecheck clean, ModelPortfolios renders unchanged (no SEV1-surface behavior change)

## Touched surfaces

- `portal/src/api/endpoints/aum.ts` (model_portfolios.headline, SEV1)
- `portal/src/api/portal-proxy.ts` (model_portfolios.benchmark, SEV1)

Durable record (D8-AE B1, NFRA_GRAPHS). See org/surface-check-ack-audit.log for the one-line summary.
