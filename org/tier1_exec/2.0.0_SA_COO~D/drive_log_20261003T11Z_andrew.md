# Drive log -- 2.0.0_SA_COO~D, 2026-10-03 11Z (host andrew)

| Time | Project | Limb | Act | Outcome |
|---|---|---|---|---|
| 10:5xZ-11:0xZ | DSGN_REBRND (FAST; IR lines still blocked: P-3/P-6 wait ~P's P-2 window, Case A waits ~Y) | round 3 E3, row W3-S4 | /market's Global RSI and Fear & Greed say a failed fetch: portal `55560835` on origin DEV (ls-remote 11:09Z) | DRIVE FORWARD |
| 11:1xZ-11:3xZ | DSGN_REBRND (FAST; IR still blocked on ~P) | round 3 E3, row W3-S4 | /market's Daily Cloud, Trending Topics and Top/Bottom Performers say a failed fetch: portal `a7b16628` on origin DEV (ls-remote 11:30Z) | DRIVE FORWARD |

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

## W3-S4 on /market, the rest

- Daily Cloud: `getKeywordFinBERTSentimentsWithTimestamp` returned an empty list on a failed request; it throws now and
  the tile is ERROR. A served empty list keeps "No keywords are trending".
- Trending Topics (its endpoint already threw): ONE error for the panel instead of "no topics" in both cards (C12, no
  repeated message).
- Top/Bottom Performers: the page's `error` reaches them as `failed` (through ExecutiveSummaryPanel); ONE error when
  nothing is held, the held returns otherwise.
- Pin arms (d)-(f) with controls; negative control on 55560835 fails all three. Real run: the live 401 for Daily Cloud
  and the performers; `--fail trending/latest` (20 s window) for Trending Topics, which was still retrying in the
  first 14 s render. Lease widened to ExecutiveSummary.tsx and panels/ExecutiveSummaryPanel.

## Still open on W3-S4

- ~~/market: Daily Cloud, Trending Topics and Top/Bottom Performers~~ LANDED a7b16628 (above).
- `useRSIValues`'s `segment.value ?? 50` for one missing class.
- The row's other six routes, not re-measured this tick.
