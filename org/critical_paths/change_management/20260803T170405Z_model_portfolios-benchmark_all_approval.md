# SURFACE_ACK approval -- 20260803T170405Z

**class:** approval
**surfaces:** model_portfolios.benchmark
**firm:** all
**commit:** 4f7202796fff
**reason:** MDLP_MONPUB.W6 (TO 1.0.0_SA_CTO-2026-08-03-monpub-w6, CTO GO 160830Z, Andrew-watched): additive-only widening of DataRefreshRollbackResponse (newExecutionId->optional + additive fields) + rollback-success invalidation touching the benchmark surface's CLIENT CACHE only -- no read path, field name, or payload shape of model_portfolios.benchmark changes; invalidation makes open sessions refetch the SAME served artifact

## Touched surfaces

- `portal/src/api/portal-proxy.ts` (model_portfolios.benchmark, SEV1)

Durable record (D8-AE B1, NFRA_GRAPHS). See org/surface-check-ack-audit.log for the one-line summary.
