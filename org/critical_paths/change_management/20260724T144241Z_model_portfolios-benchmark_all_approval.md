# SURFACE_ACK approval -- 20260724T144241Z

**class:** approval
**surfaces:** model_portfolios.benchmark,model_portfolios.headline
**firm:** all
**commit:** aaf28cc59bbe
**reason:** W-5b type-contract + honest-null propagation, COO-approved 142950Z under TO MDPF_3FIRMS.GC-W45. aum number -> number|null at portal-proxy.ts (source), aum.ts (re-declaration) and PeriodData (compiler-forced); measured 24 nulls of 447 on the served artifact. No render path touched, zero coercions ADDED and five pre-existing zero-assertions REMOVED, bun run typecheck CLEAN with a five-state error-then-clean positive control.

## Touched surfaces

- `portal/src/api/endpoints/aum.ts` (model_portfolios.headline, SEV1)
- `portal/src/api/portal-proxy.ts` (model_portfolios.benchmark, SEV1)

Durable record (D8-AE B1, NFRA_GRAPHS). See org/surface-check-ack-audit.log for the one-line summary.
