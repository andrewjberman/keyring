# Andrew-direct, 2026-10-07 ~01:0xZ (9:0x PM Eastern, 2026-10-06), at the 4.0.0_SA_CRO terminal -- VERBATIM

Channel: typed by Andrew into the 4.0.0_SA_CRO (base) session.

> go, route it

## What he said go to (this seat's recommendation, as shown to him minutes before)

Read at 01:03Z: `json/benchmarks/model_portfolio_benchmarks.json` (generated 2026-10-07T00:18:26Z) has index benchmarks current
to 2026-10-05 and ETF benchmarks ending 2026-09-29 for UST, ST, LT and ULT; the CTO's Since Inception fix `1814185b` is on
portal origin/DEV and NOT on origin/PROD.

1. **Site Z re-pulls now** (the Bloomberg pull and `/data-refresh`), rather than waiting for the scheduled pull, to confirm
   Yang's re-saved ETF CIX (`.UST_ETF .ST_ETF .LT_ETF`) reach the served file.
2. **Promote portal DEV to PROD**, so `1814185b` reaches the live site.

## Routing

One message to `0.0.0_AB_MSTR` for relay to `0.0.0_AB_MSTR~Z` (the re-pull) and for the promote through its owner.
