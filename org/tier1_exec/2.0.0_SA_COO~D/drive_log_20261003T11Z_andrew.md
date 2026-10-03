# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 11Z (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 10:5xZ-11:0xZ | DSGN_REBRND (FAST; IR lines still blocked: P-3/P-6 wait ~P's P-2 window, Case A waits ~Y) | round 3 E3, row W3-S4 | /market's Global RSI and Fear & Greed say a failed fetch: portal `55560835` on origin DEV (ls-remote 11:09Z) | DRIVE FORWARD |

## W3-S4 on /market

- RSIBars ignored `useRSIValues`'s isLoading/hasData and drew the 50/50/50 placeholder. It now renders PanelLoading,
  then PanelError with no summary.
- The Fear & Greed fault was one layer down: `api/endpoints/sentiment.ts getFearGreedIndex` caught a failed request
  and returned value 50, 'neutral', stamped now. It now throws. Callers read: SentimentGauge (now LOADING/ERROR, the
  drilldown opens only with a reading), FearGreedModal (falls back to the data it is opened with), DataSourceContext
  (query disabled).
- Pin `components/market-performance/__tests__/market-failed-fetch.test.tsx` (bun mock.module for the hooks and the
  api client): three arms with controls; negative controls on HEAD fail arms (a), (b) and (c). The pending arm of (b)
  passes on HEAD too, so it is not claimed.
- Real run: ui-smoke on 5174 with `--fail rsi-summary --fail fear-greed-index`. HEAD: three RSI bars at 50 and the dial
  at "50 Neutral". After: both panels show their error state beside U.S. Regime's. Cropped and looked at.
- Lease widened to SentimentGauge.tsx, the pin's path and api/endpoints/sentiment.ts. VALGATE D-1 passed (no static
  partner adapters changed).

## Still open on W3-S4

- /market: Daily Cloud, Trending Topics and Top/Bottom Performers show EMPTY words when their fetches fail (seen in the
  same render, auth stubbed, so their requests answered 401).
- `useRSIValues`'s `segment.value ?? 50` for one missing class.
- The row's other six routes, not re-measured this tick.
