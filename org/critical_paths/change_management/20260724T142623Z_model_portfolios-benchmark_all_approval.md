# SURFACE_ACK approval -- 20260724T142623Z

**class:** approval
**surfaces:** model_portfolios.benchmark,model_portfolios.headline
**firm:** all
**commit:** ea4044d94405
**reason:** W-5 type-only widening ordered by CTO 140508Z under TO MDPF_3FIRMS.GC-W45: account_count number -> number|null at portal-proxy.ts:213-214 (source), aum.ts:404-405 (re-declaration) and aum.ts:63 (compiler-forced, same artifact). Zero runtime/render change, zero coercion, bun run typecheck CLEAN with an error-then-clean positive control. This makes the SEV1 headline surface contract STOP asserting a falsehood -- the served artifact carries 40 nulls of 447.

## Touched surfaces

- `portal/src/api/endpoints/aum.ts` (model_portfolios.headline, SEV1)
- `portal/src/api/portal-proxy.ts` (model_portfolios.benchmark, SEV1)

Durable record (D8-AE B1, NFRA_GRAPHS). See org/surface-check-ack-audit.log for the one-line summary.
