# SURFACE_ACK approval -- 20260715T153809Z

**class:** approval
**surfaces:** model_portfolios.benchmark
**firm:** all
**commit:** bf8f24728225
**reason:** comment-only diff on BenchmarkHeatmap.tsx, verified line-by-line pre-ack: all 6 changed lines are code comments (3 trailing on ROW_BACKGROUNDS whose class strings are byte-identical, 2 block comments, 1 JSX comment); zero behavioral/class/token change. Purpose: Andrew-direct #6 design-language sweep -- the removed comments falsely called the SEV1 surface's dark navy background 'light blue', the exact vocabulary that shipped the TicketCenter light-on-light defect.

## Touched surfaces

- `portal/src/components/BenchmarkHeatmap.tsx` (model_portfolios.benchmark, SEV1)

Durable record (D8-AE B1, NFRA_GRAPHS). See org/surface-check-ack-audit.log for the one-line summary.
