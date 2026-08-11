# SURFACE_ACK approval -- 20260804T052349Z

**class:** approval
**surfaces:** model_portfolios.benchmark,model_portfolios.headline
**firm:** all
**commit:** 2fb465e65633
**reason:** Dead-code removal + comment corrections only (kill-list row 15, COO GO 042634Z via ~F 051830Z; zero live value paths -- killed pair had zero callers + measured-403 route; evidence @297db6f6bf + @b48634789a)

## Touched surfaces

- `portal/src/api/endpoints/aum.ts` (model_portfolios.headline, SEV1)
- `portal/src/api/portal-proxy.ts` (model_portfolios.benchmark, SEV1)

Durable record (D8-AE B1, NFRA_GRAPHS). See org/surface-check-ack-audit.log for the one-line summary.
