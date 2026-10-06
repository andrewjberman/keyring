# Andrew-direct, 2026-10-06 ~21:3xZ (5:3x PM Eastern), at the 4.0.0_SA_CRO terminal -- VERBATIM

Channel: typed by Andrew into the 4.0.0_SA_CRO (base) session, after this seat's finding
`docs/briefs/benchmark-heatmap-cix-finding-20261006.md` (@ead4fec67d), which asked: "Should I route item 3 to the CTO as a
fix?"

> Ok i need this routed to CTO for a fix now, and I need them to get it committed and pushed via MSTR and MSTR needs to
> send it over to MSTR~Z to have them run a repull

## What it orders (as stated, not widened)

1. **`1.0.0_SA_CTO`: fix item 3 now** -- the Benchmark tab's Since Inception mismatch in ETF mode (the browser blends
   cumulative ETF returns from `json/benchmarks/etf_returns.json` beside the Lambda's annualized model figure). The fix's
   form (annualize in the ETF producer, or take the ETF benchmark from the served model file) is the CTO's.
2. **Commit, then push via `0.0.0_AB_MSTR`.** This sentence is Andrew's word for that push.
3. **`0.0.0_AB_MSTR` sends it to `0.0.0_AB_MSTR~Z` to run a re-pull** -- the Bloomberg pull and `/data-refresh` that let the
   re-saved CIX (items 1 and 2 of the finding) reach the served file.

## Routing

One message to `1.0.0_SA_CTO` (the fix) and one to `0.0.0_AB_MSTR` (the push and the relay to site Z), both naming this
record.
