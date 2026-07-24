# SURFACE_ACK approval -- 20260722T140842Z

**class:** approval
**surfaces:** model_portfolios.benchmark,model_portfolios.headline
**firm:** all
**commit:** 03531a7f1bc1
**reason:** WSE_COTMDL absent-is-not-zero fix, CTO+COO ruled 20260722T135932Z. MP is the intended SEV1 surface. Closes two live defects ON it (a zero total beside a populated donut, and a false rolled-forward methodology claim) rather than adding risk. Sibling function + optional prop only -- lastNonNull signature and the global path UNTOUCHED (mid-rebuild). Existing firms unaffected: positive control renders 142M normally. Exercised before/after + positive control by rendering and READING the PNGs; tsc RC=0.

## Touched surfaces

- `portal/src/pages/ModelPortfolios.tsx` (model_portfolios.benchmark, SEV1)
- `portal/src/pages/ModelPortfolios.tsx` (model_portfolios.headline, SEV1)

Durable record (D8-AE B1, NFRA_GRAPHS). See org/surface-check-ack-audit.log for the one-line summary.
