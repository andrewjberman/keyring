# SURFACE_ACK approval -- 20260722T132115Z

**class:** approval
**surfaces:** model_portfolios.benchmark,model_portfolios.headline
**firm:** all
**commit:** 685fcbc42845
**reason:** WSE_COTMDL, Andrew-direct 2026-07-22 'Let's push everything with Cottonwood' (one flip, Cottonwood inside the gate); CTO+COO both ruled the Select-Partner FE is on the flip critical path and in no workstream. MP IS the intended SEV1 surface -- adding the cottonwood cohort is the requested change, not a side effect. Existing global/49financial/inflection render strings preserved BYTE-IDENTICAL (no-op for every existing firm); the change is additive for cottonwood plus a structural fix converting a binary source-attribution ternary into a type-exhaustive Record, which CLOSES a live mislabel defect on this same surface rather than adding risk to it. tsc RC=0, gate exercised (5th firm -> TS2741 RC=2), /portfolios rendered and PNG read against the silver-canvas color law.

## Touched surfaces

- `portal/src/pages/ModelPortfolios.tsx` (model_portfolios.benchmark, SEV1)
- `portal/src/pages/ModelPortfolios.tsx` (model_portfolios.headline, SEV1)

Durable record (D8-AE B1, NFRA_GRAPHS). See org/surface-check-ack-audit.log for the one-line summary.
